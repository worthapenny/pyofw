from typing import Any

from pyOpenFlows.setupOpenFlows import AppType, SetupOpenFlowsWater
import unittest


class TestSetupOpenFlows(unittest.TestCase):
    wtrg_installation_path: str = r"D:\Development\Perforce\Aspen\Products\WaterGEMS\Output\_Starter\x64\Debug"
    wtrc_installation_path: str = r"_"  # left blank to test
    water_model_path = r"c:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"

    wm: Any = None
    setup_wtrg: SetupOpenFlowsWater
    setup_wtro: SetupOpenFlowsWater

    # region Setup and Teardown

    @classmethod
    def setUpClass(cls):
        cls.setup_wtrg = None
        cls.setup_wtro = None
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
        TestSetupOpenFlows.setup_wtrg = SetupOpenFlowsWater(
            app_type=AppType.WaterGEMS,
            dlls_dir=self.wtrg_installation_path,
        )

        self.assertIsNotNone(TestSetupOpenFlows.setup_wtrg)

        wm = TestSetupOpenFlows.setup_wtrg.open_model(self.water_model_path)
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

    # endregion


if __name__ == '__main__':
    unittest.main()
