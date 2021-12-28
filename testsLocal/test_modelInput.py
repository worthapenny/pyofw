'''
Author: Akshaya Niraula
Create Time: 2021-10-18 06:57:08
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''

import unittest
import logging

from testsLocal.test_base import TestOfwBase

from src.pyOFW.ofwConfig import AppType, OFWConfig
from src.pyOFW import modelInput as mi


class TestModelInput(TestOfwBase):
    ofw: OFWConfig
    # region Setup and Teardown

    @classmethod
    def setUpClass(cls):
        logging.info("Test for Model Input started.")

        #
        cls.ofw = OFWConfig(
            AppType.WaterCAD, dlls_dir=OFWConfig.WTRC_INSTALL_DIR)

        cls.ofw.open_model(super().WTRG_EX_5_WTG)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.ofw.water_model.Close()
        cls.ofw.end_session()
        logging.info("Test for Network Input ended.")

    # endregion

    # region Tests

    # region Test Lat / Lng
    def test_scenario_df(self):
        scenario_df = mi.scenario_df(self.ofw.water_model)
        self.assertFalse(scenario_df.empty)
    # endregion

    # endregion


if __name__ == '__main__':
    unittest.main()
