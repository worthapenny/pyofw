'''
Author: Akshaya Niraula
Create Time: 2021-10-14 20:08:58
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''

import unittest
import logging
from typing import Any

from src.pyofw.config import AppType, OFWConfig
from testsLocal.test_base import TestOfwBase


class TestNetworkInput(TestOfwBase):
    ofw: OFWConfig
    ni: Any

    # region Setup and Teardown
    @classmethod
    def setUpClass(cls):
        logging.info("Test for Network Input started.")

        #
        cls.ofw = OFWConfig(
            AppType.WaterGEMS, dlls_dir=OFWConfig.WTRG_INSTALL_DIR)

        from pyofw.network_input import NetworkInput

        cls.ofw.open_model(super().WTRG_EX_5_WTG)
        cls.ni: NetworkInput = NetworkInput(cls.ofw.water_model)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.ofw.water_model.Close()
        cls.ofw.end_session()
        logging.info("Test for Network Input ended.")

    # endregion

    # region Tests

    def test_pipe_df(self):
        df = TestNetworkInput.ni.pipe_df
        columns = ['Label', 'Id', 'IsActive', 'StartNode', 'StartNodeId', 'StopNode', 'StopNodeId',
                   'IsUDLength', 'Length', 'Geometry', 'InstallYr', 'Status', 'Diameter',
                   'Material', 'FrictionCoeff']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (268, 15)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_lateral_df(self):
        df = TestNetworkInput.ni.lateral_df
        columns = ['Label', 'Id', 'IsActive', 'StartNode', 'StartNodeId', 'StopNode', 'StopNodeId',
                   'IsUDLength', 'Length', 'Geometry']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 10)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_junction_df(self):
        df = TestNetworkInput.ni.junction_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (181, 13)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_hydrant_df(self):
        df = TestNetworkInput.ni.hydrant_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 13)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_tank_df(self):
        df = TestNetworkInput.ni.tank_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel',
                   'InitAge', 'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'SectionType',
                   'ActiveVolFull', 'Diameter', 'AvgArea', 'BaseElev', 'MinLevel',
                   'MaxLevel', 'InitLevel', 'UseHighAlarm', 'HighAlarmLvl', 'UseLowAlarm',
                   'LowAlarmLvl', 'InactiveVol', 'ValveChrsts']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (1, 27)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_reservoir_df(self):
        df = TestNetworkInput.ni.reservoir_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (1, 13)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_tap_df(self):
        df = TestNetworkInput.ni.tap_df
        columns = ['Label', 'Id', 'Geometry',
                   'X', 'Y', 'AssocElem', 'AssocElemId']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 7)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_pump_df(self):
        df = TestNetworkInput.ni.pump_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'InitSpeedFactor']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (2, 16)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_customer_meter_df(self):
        df = TestNetworkInput.ni.customer_meter_df
        columns = ['Label', 'Id', 'Geometry', 'X', 'Y', 'Demand', 'Pattern', 'PatternId',
                   'StartDemandDist', 'AssocElem', 'AssocElemId', 'UnitDemand',
                   'UnitDmdPattern', 'UnitDmdPatternId', 'NumUnitDmd']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 16)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_scada_elem_df(self):
        df = TestNetworkInput.ni.scada_elem_df
        columns = ['Label', 'Id', 'Geometry', 'X', 'Y', 'TgtElem', 'TgtElemId', 'HistSignal',
                   'HistSignalId']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (7, 9)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_pump_stn_df(self):
        df = TestNetworkInput.ni.pump_stn_df
        columns = ['Label', 'Id', 'IsActive', 'Geometry']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 4)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_vspb_df(self):
        df = TestNetworkInput.ni.vspb_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'InitSpeedFactor', 'InitStatus', 'PumpDefinition', 'PumpDefinitionId',
                   'ControlNode', 'ControlNodeId', 'TgtHGL', 'MaxSpeedFactor',
                   'NumLagPumps', 'CtrlNodeSucSide', 'CtrlNodeSucSideId', 'TgtFlow',
                   'TgtPressure', 'VSPBType', 'VSPBFixedHeadType']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 29)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_prv_df(self):
        df = TestNetworkInput.ni.prv_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'dMLossCoeff', 'IsLocalMLoss', 'LocalMLossCoeff', 'InitStatus',
                   'Diameter', 'PressureSettings', 'InitSetting', 'ValveChrsts',
                   ] # 'ValveType'
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (3, 22)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_psv_df(self):
        df = TestNetworkInput.ni.psv_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'dMLossCoeff', 'IsLocalMLoss', 'LocalMLossCoeff', 'InitStatus',
                   'Diameter', 'PressureSettings', 'InitSetting', 'ValveChrsts',
                   ] #'ValveType'
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 22)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_pbv_df(self):
        df = TestNetworkInput.ni.pbv_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'dMLossCoeff', 'IsLocalMLoss', 'LocalMLossCoeff', 'InitStatus',
                   'Diameter', 'PressureSettings', 'InitSetting']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 21)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_fcv_df(self):
        df = TestNetworkInput.ni.fcv_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'dMLossCoeff', 'IsLocalMLoss', 'LocalMLossCoeff', 'InitStatus',
                   'Diameter', 'InitFlowSetting', 'Characteristic']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 21)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_tcv_df(self):
        df = TestNetworkInput.ni.tcv_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'dMLossCoeff', 'IsLocalMLoss', 'LocalMLossCoeff', 'InitStatus',
                   'Diameter', 'CoeffType', 'InitCoeff', 'Characteristic']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 22)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_gpv_df(self):
        df = TestNetworkInput.ni.gpv_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr',
                   'dMLossCoeff', 'IsLocalMLoss', 'LocalMLossCoeff', 'InitStatus',
                   'Diameter', 'GpvHlCurve', 'ValveChrsts']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 21)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_iso_valve_df(self):
        df = TestNetworkInput.ni.iso_valve_df
        columns = ['Label', 'Id', 'Geometry', 'X', 'Y', 'RefPipe', 'RefPipeId', 'Diameter',
                   'MinorLossCoeff', 'IsOperable', 'InitStatus', 'InstallYr']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 12)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_hydro_tank_df(self):
        df = TestNetworkInput.ni.hydro_tank_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InitGasVol',
                   'InletOrifDia', 'RatioOfLosses', 'GasLawExponent', 'HasBladder',
                   'GasPresetPressure', 'MeanLqdElev', 'AirInOrifDia', 'AirOutOrifDia',
                   'DippingTubeDia', 'CompChamberVol', 'TopElevDippingTube', 'LevelType',
                   'HydroTankType']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 27)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    def test_check_valve_df(self):
        df = TestNetworkInput.ni.check_valve_df
        columns = ['Label', 'Id', 'Elevation', 'IsActive', 'Zone', 'ZoneId', 'ZoneLabel', 'InitAge',
                   'InitConc', 'InitTrace', 'Geometry', 'X', 'Y', 'InstallYr', 'AtY',
                   'FlowDirection', 'InitTypFlow', 'ThresPressure']
        self.assertTrue(set(columns).issubset(df.columns))

        df_shape = (0, 18)
        self.assertEqual(df_shape[0], df.shape[0])
        self.assertEqual(df_shape[1], df.shape[1])

    # endregion


if __name__ == '__main__':
    unittest.main()
