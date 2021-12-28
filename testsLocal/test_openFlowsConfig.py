'''
Author: Akshaya Niraula
Create Time: 2021-10-14 20:08:38
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''


import unittest
import logging
from typing import Any

from src.pyOFW.ofwConfig import AppType, OFWConfig


class TestOpenFlowsConfig(unittest.TestCase):
    wtrg_installation_path: str = r"D:\Development\Perforce\Aspen\Products\WaterGEMS\Output\_Starter\x64\Debug"
    wtrc_installation_path: str = r"_"  # left blank to test
    water_model_path = r"c:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"

    ofw_wtrg: OFWConfig
    ofw_wtro: OFWConfig

    # region Setup and Teardown

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s.%(msecs)03d %(levelname)s [%(filename)s]:\t%(message)s",
            datefmt="%d %H:%M:%S",
        )
        logging.info("")

        cls.ofw_wtrg = None
        cls.ofw_wtro = None
        pass

    @classmethod
    def tearDownClass(cls):
        if cls.ofw_wtrg:
            cls.ofw_wtrg.end_session()
        if cls.ofw_wtro:
            cls.ofw_wtro.end_session()

    # endregion

    # region Tests

    def test_wtrg(self):
        self.ofw_wtrg = OFWConfig(
            app_type=AppType.WaterGEMS,
            dlls_dir=self.wtrg_installation_path,
        )

        self.assertIsNotNone(self.ofw_wtrg)

        self.ofw_wtrg.open_model(self.water_model_path)
        self.assertIsNotNone(self.ofw_wtrg.water_model)

        end_session = self.ofw_wtrg.end_session()
        self.assertIsNone(end_session)

        pass

    def test_wtrc(self):
        self.assertRaises(
            ValueError,
            OFWConfig,
            app_type=AppType.WaterCAD,
            dlls_dir=self.wtrc_installation_path,
        )
        pass

    # endregion


if __name__ == '__main__':
    unittest.main()
