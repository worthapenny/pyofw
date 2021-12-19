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

    wm: Any = None
    setup_wtrg: OFWConfig
    setup_wtro: OFWConfig

    # region Setup and Teardown

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s.%(msecs)03d %(levelname)s [%(filename)s]:\t%(message)s",
            datefmt="%d %H:%M:%S",
        )
        logging.info("")

        cls.setup_wtrg = None
        cls.setup_wtro = None
        pass

    @classmethod
    def tearDownClass(cls):
        if cls.setup_wtrg:
            cls.setup_wtrg.end_session()
        if cls.setup_wtro:
            cls.setup_wtro.end_session()

    # endregion

    # region Tests

    def test_wtrg(self):
        TestOpenFlowsConfig.setup_wtrg = OFWConfig(
            app_type=AppType.WaterGEMS,
            dlls_dir=self.wtrg_installation_path,
        )

        self.assertIsNotNone(TestOpenFlowsConfig.setup_wtrg)

        wm = TestOpenFlowsConfig.setup_wtrg.open_model(self.water_model_path)
        self.assertIsNotNone(wm)

        end_session = TestOpenFlowsConfig.setup_wtrg.end_session()
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
