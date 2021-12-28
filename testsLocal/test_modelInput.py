'''
Author: Akshaya Niraula
Create Time: 2021-10-18 06:57:08
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''

import pandas as pd
import unittest
import logging
from typing import Any

from testsLocal.test_base import TestOfwBase

from src.pyOFW.ofwConfig import AppType, OFWConfig
from src.pyOFW import modelInput as mi


class TestModelInput(TestOfwBase):
    water_model_path = r"c:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
    setup_water: OFWConfig
    wm: Any
    # region Setup and Teardown

    @classmethod
    def setUpClass(cls):
        logging.info("Test for Model Input started.")

        #
        cls.setup_water = OFWConfig(
            AppType.WaterCAD, dlls_dir=OFWConfig.WTRC_INSTALL_DIR)

        from OpenFlows.Water.Domain import IWaterModel

        cls.wm: IWaterModel = cls.setup_water.open_model(cls.water_model_path)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.wm.Close()
        cls.setup_water.end_session()
        logging.info("Test for Network Input ended.")

    # endregion

    # region Tests

    # region Test Lat / Lng
    def test_scenario_df(self):
        scenario_df = mi.scenario_df(self.wm)
        self.assertFalse(scenario_df.empty)
    # endregion

    # endregion


if __name__ == '__main__':
    unittest.main()
