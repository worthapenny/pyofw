from typing import Any

from pyOpenFlows.setupOpenFlows import AppType, SetupOpenFlowsWater
import unittest


class TestSetupOpenFlows(unittest.TestCase):
    wtrg_installation_path = r"C:\Program Files (x86)\Bentley\WaterGEMS\x64"
    wtrc_installation_path = r"_"  # left blank to test
    wtro_installation_path = r"C:\Program Files\Bentley\WaterOPS"

    water_model_path = r"c:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
    wm: Any
    setup_wtrg: SetupOpenFlowsWater
    setup_wtro: SetupOpenFlowsWater

    # region Setup and Teardown
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        if cls.setup_wtrg:
            cls.setup_wtrg.end()
        if cls.setup_wtro:
            cls.setup_wtro.end()

    # endregion

    # region Tests

    def test_wtrg(self):
        self.setup_wtrg = SetupOpenFlowsWater(
            app_type=AppType.WaterGEMS,
            dlls_dir=self.wtrg_installation_path,
        )

        self.assertIsNotNone(self.setup_wtrg)

        wm = self.setup_wtrg.open_model(self.water_model_path)
        self.assertIsNotNone(wm)
        pass

    def test_wtrc(self):
        self.assertRaises(
            ValueError,
            SetupOpenFlowsWater,
            app_type=AppType.WaterCAD,
            dlls_dir=self.wtrc_installation_path,
        )
        pass

    def test_wtro(self):
        self.setup_wtro = SetupOpenFlowsWater(
            app_type=AppType.WaterOPS,
            dlls_dir=self.wtro_installation_path,
        )

        self.assertIsNotNone(self.setup_wtro)

        self.assertIsNotNone(self.setup_wtro.open_model(self.water_model_path))
        pass
    # endregion


if __name__ == '__main__':
    unittest.main()
