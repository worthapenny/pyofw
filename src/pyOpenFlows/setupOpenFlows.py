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


class SetupOpenFlowsWater:
    dlls_dir: str
    __IWaterModel: Any
    assemblies: List[str] = [
        "OpenFlows.Water",
    ]

    def __init__(self, app_type: AppType = AppType.WaterGEMS, dlls_dir: str = "") -> None:

        # TODO: point to installation location
        if not dlls_dir:
            dlls_dir = r"D:\Development\Perforce\Aspen\Products\WaterGEMS\Output\_Starter\x64\Debug"
        if not dlls_dir:
            dlls_dir = r"C:\Program Files (x86)\Bentley\WaterGEMS\x64"

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

        logging.debug(f"{__class__.__name__} initialized")
        pass

    def load_assemblies(self, assemblies: List[str]) -> bool:
        success = True
        for assembly in assemblies:
            try:
                clr.AddReference(assembly)
                logging.debug(f"Assembly loaded: {assembly}")
            except:
                logging.critical(f"FAILED to load the assembly: {assembly}")
                success = success & False

        logging.info(
            f"Assemblies loaded successfully: Count = {len(assemblies)}")
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
        except:
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

    def end(self, close_session: bool = True) -> None:
        if self.__IWaterModel:
            logging.debug("About to close the model...")
            self.__IWaterModel.Close()
            logging.info("Closed the model.")

        if close_session:
            from OpenFlows.Water.Python import OpenFlowsWaterPython as ofw
            ofw.EndSession()
            logging.info("Session ended. See you soon.")
