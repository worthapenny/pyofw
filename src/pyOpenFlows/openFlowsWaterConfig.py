from enum import Enum
import os
import sys
from typing import Any, List
import clr
import logging


class AppType(Enum):
    WaterGEMS = 1
    WaterCAD = 2
    WaterOPS = 3


class OpenFlowsWaterConfig:
    wtrg_install_dir = r"C:\Program Files (x86)\Bentley\WaterGEMS\x64"
    wtrc_install_dir = r"C:\Program Files (x86)\Bentley\WaterCAD\x64"
    wops_install_dir = r"C:\Program Files\Bentley\WaterOPS"

    dlls_dir: str
    __IWaterModel: Any
    __app_type: AppType
    assemblies: List[str] = [
        "OpenFlows.Water",
    ]

    # region Constructor
    def __init__(self, app_type: AppType = AppType.WaterGEMS, dlls_dir: str = "") -> None:

        if not dlls_dir and os.path.exists(self.wtrg_install_dir):
            dlls_dir = self.wtrg_install_dir
        if not dlls_dir and os.path.exists(self.wtrc_install_dir):
            dlls_dir = self.wtrc_install_dir
        if not dlls_dir and os.path.extsep(self.wops_install_dir):
            dlls_dir = self.wops_install_dir

        self.__app_type = app_type
        self.dlls_dir = dlls_dir
        logging.debug(f"Assembly dir is set to: {self.dlls_dir}")
        if not os.path.exists(self.dlls_dir):
            raise ValueError(
                f"Given dlls_dir location is not valid. Dir: {self.dlls_dir}")

        self.__IWaterModel = None
        success = True
        try:
            sys.path.append(str(self.dlls_dir))
            success = self.load_assemblies(self.assemblies)
            success = success and self.open_session(app_type)
        except:
            success = False

        logging.debug(f"{__class__.__name__} initialized. Success: {success}")
        pass

    def __repr__(self) -> str:
        return f"{__class__.__name__}: {self.__app_type} assemblies from {self.dlls_dir}"

    # endregion

    def load_assemblies(self, assemblies: List[str]) -> bool:
        success = True
        for assembly in assemblies:
            added = None
            try:
                added = clr.AddReference(assembly)
                logging.debug(f"Assembly loaded: {assembly}")
            except:
                logging.exception(
                    f"FAILED to load the assembly: {assembly}. \nERROR: {added}")
                success = success & False
        if success:
            logging.info(
                f"Assemblies loaded successfully: Count = {len(assemblies)}")
        else:
            logging.error(
                f"Assemblies load was NOT successful. See previous error")

        return success

    def open_session(self, app_type: AppType = AppType.WaterGEMS) -> bool:
        success = True
        try:
            from OpenFlows.Water import OpenFlowsWater, WaterProductLicenseType

            if app_type == AppType.WaterGEMS:
                OpenFlowsWater.StartSession(WaterProductLicenseType.WaterGEMS)
            elif app_type == AppType.WaterCAD:
                OpenFlowsWater.StartSession(WaterProductLicenseType.WaterCAD)
            elif app_type == AppType.WaterOPS:
                OpenFlowsWater.StartSession(WaterProductLicenseType.WaterOPS)

            logging.debug(f"Session for {app_type} started")
        except:
            logging.exception(f"while starting the {app_type} session")
            success = False

        return success

    def open_model(self, wtg_filepath: str) -> Any:
        logging.debug(f"About to open up a model file: {wtg_filepath}")

        try:
            from OpenFlows.Water import OpenFlowsWater
            self.__IWaterModel = OpenFlowsWater.Open(wtg_filepath)

            logging.info(
                f"Successfully opened up the model. Path: {wtg_filepath}")
        except:
            logging.exception(
                f"Failed to open up the hydraulic model. Path: {wtg_filepath}")
        return self.__IWaterModel

    def end_session(self, end_session: bool = True) -> None:

        if self.__IWaterModel:
            logging.debug("About to close the model...")
            self.__IWaterModel.Close()
            logging.info("Closed the model.")

        if end_session:
            from OpenFlows.Water import OpenFlowsWater
            OpenFlowsWater.EndSession()
            logging.info("Session ended. See you soon.")
