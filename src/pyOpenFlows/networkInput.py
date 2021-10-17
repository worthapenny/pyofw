from OpenFlows.Domain.ModelingElements.NetworkElements import IActiveElementsInput, IBaseLinksInput, IBasePolygonInput, IBasePolygonsInput, INetworkElements, IPointNodesInput
from OpenFlows.Water.Domain import IWaterModel
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IBaseDirectedNodesInput, IBaseNodesInput, IBasePumpsInput, IBaseValvesInput, ICheckValveElementsInput, IConventionalTanksInput, ICustomerMetersInput, IDemandNodesInput, IFireFlowNodesInput, IFlowControlValvesInput, IGeneralPurposeValves, IGeneralPurposeValvesInput, IHydrantsInput, IHydroTanksInput, IIsolationValveElementsInput, IJunctionsInput, ILateralsInput, IPhysicalNodeElementsInput, IPipes, IPressureBreakingValves, IPressureBreakingValvesInput, IPressureSustainingValvesInput, IPressureValvesInput, IPumpStations, IPumpStationsInput, IPumps, IPumpsInput, IReservoirs, ISCADAElements, ISCADAElementsInput, ITanks, ITanksInput, ITaps, IThrottleControlValvesInput, IVSPBsInput, IWaterQualityElementsInput, IWaterQualityNodesInput, IWaterZoneableNetworkElementsInput
import numpy as np
import pandas as pd
import networkx as nx
from typing import Any, List, Type


class NetworkInput:
    # region Fields
    __waterModel: IWaterModel
    # endregion

    # region Constructor
    def __init__(self, water_model: IWaterModel) -> None:
        self.__waterModel = water_model
        pass
    # endregion

    # region Public Methods
    def get_networkx_graph(self, laterals: bool = False) -> nx.Graph:
        columns = ["Id", "Label"] if laterals else [
            "Id", "Label", "Diameter", "IsActive"]

        links_df = self.pipe_df[columns].copy()
        if laterals:
            links_df.append(self.lateral_df[columns])

        graph: nx.Graph = nx.from_pandas_edgelist(
            df=links_df,
            source="StartNodeId",
            target="StopNodeId",
            edge_attr=columns)

        return graph

    # endregion // Public Methods

    # region Public Properties (Network Elements DF)

    @property
    def pipe_df(self) -> pd.DataFrame:
        return self.__get_pipe_input(self.__waterModel.Network.Pipes)

    @property
    def lateral_df(self) -> pd.DataFrame:
        return self.__get_lateral_input(self.__waterModel.Network.Laterals)

    @property
    def junction_df(self) -> pd.DataFrame:
        return self.__get_junction_input(self.__waterModel.Network.Junctions)

    @property
    def hydrant_df(self) -> pd.DataFrame:
        return self.__get_hydrant_input(self.__waterModel.Network.Hydrants)

    @property
    def tank_df(self) -> pd.DataFrame:
        return self.__get_tank_input(self.__waterModel.Network.Tanks)

    @property
    def reservoir_df(self) -> pd.DataFrame:
        return self.__get_reservoir_input(self.__waterModel.Network.Reservoirs)

    @property
    def tap_df(self) -> pd.DataFrame:
        return self.__get_tap_input(self.__waterModel.Network.Taps)

    @property
    def pump_df(self) -> pd.DataFrame:
        return self.__get_pump_input(self.__waterModel.Network.Pumps)

    @property
    def pump_stn_df(self) -> pd.DataFrame:
        return self.__get_pump_stn_input(self.__waterModel.Network.PumpStations)

    @property
    def customer_meter_df(self) -> pd.DataFrame:
        return self.__get_customer_meter_input(self.__waterModel.Network.CustomerMeters)

    @property
    def scada_elem_df(self) -> pd.DataFrame:
        return self.__get_scada_elem_input(self.__waterModel.Network.SCADAElements)

    @property
    def vspb_df(self) -> pd.DataFrame:
        return self.__get_vspb_input(self.__waterModel.Network.VSPBs)

    @property
    def prv_df(self) -> pd.DataFrame:
        return self.__get_prv_input(self.__waterModel.Network.PRVs)

    @property
    def psv_df(self) -> pd.DataFrame:
        return self.__get_psv_input(self.__waterModel.Network.PSVs)

    @property
    def pbv_df(self) -> pd.DataFrame:
        return self.__get_pbv_input(self.__waterModel.Network.PBVs)

    @property
    def fcv_df(self) -> pd.DataFrame:
        return self.__get_fcv_input(self.__waterModel.Network.FCVs)

    @property
    def tcv_df(self) -> pd.DataFrame:
        return self.__get_tcv_input(self.__waterModel.Network.TCVs)

    @property
    def gpv_df(self) -> pd.DataFrame:
        return self.__get_gpv_input(self.__waterModel.Network.GPVs)

    @property
    def iso_valve_df(self) -> pd.DataFrame:
        return self.__get_iso_valve_input(self.__waterModel.Network.IsolationValves)

    @property
    def hydro_tank_df(self) -> pd.DataFrame:
        return self.__get_hydro_tank_input(self.__waterModel.Network.HydropneumaticTanks)

    @property
    def check_valve_df(self) -> pd.DataFrame:
        return self.__get_check_valve_input(self.__waterModel.Network.CheckValves)

    # endregion // Public Properties

    # region Private methods

    def __dict_to_value(self, series: pd.Series, data_type: Type) -> pd.Series:
        series = series.apply(lambda d: d.Value)
        if data_type:
            if data_type is str:
                series = series.astype("string")
            else:
                series = series.astype(data_type)
        return series

    def __get_elements_input(self, elements: INetworkElements) -> pd.DataFrame:
        df = pd.DataFrame()
        df["Label"] = elements.Labels()
        df["Id"] = df["Label"].apply(lambda d: d.Key).astype(np.int64)
        df["Label"] = df["Label"].apply(lambda d: d.Value).astype("string")
        return df

    def __get_physical_elevation_input(self, elements: IPhysicalNodeElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Elevation"] = elements.Elevations()
        df["Elevation"] = self.__dict_to_value(df["Elevation"], float)
        return df

    def __get_active_elements_input(self, elements: IActiveElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["IsActive"] = elements.IsActives()
        df["IsActive"] = self.__dict_to_value(df["IsActive"], bool)
        return df

    def __get_zone_elements_input(self, elements: IWaterZoneableNetworkElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Zone"] = elements.Zones()
        df["Zone"] = self.__dict_to_value(df["Zone"], None)

        df["ZoneId"] = df["Zone"].apply(lambda z: z.Id if z else None)
        df["ZoneLabel"] = df["Zone"].apply(
            lambda z: z.Label if z else None).astype("string")
        return df

    def __get_point_node_input(self, elements: IPointNodesInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Geometry"] = elements.Geometries()
        df["Geometry"] = self.__dict_to_value(df["Geometry"], None)

        x_and_y: List[Any] = df["Geometry"].apply(
            lambda p: [p.X, p.Y]).tolist()
        if x_and_y:  # TODO: find the type of x&y
            df[["X", "Y"]] = x_and_y
        else:
            df["X"] = None
            df["Y"] = None

        return df

    def __get_polygons_geometry(self, elements: IBasePolygonsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Geometry"] = elements.Geometries()
        df["Geometry"] = self.__dict_to_value(df["Geometry"], None)

        df["Geometry"] = df["Geometry"].apply(
            lambda pts: [[p.X, p.Y] for p in pts]).tolist()
        return df

    def __get_water_quality_node_input(self, elements: IWaterQualityElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["InitAge"] = elements.InitialAge()
        df["InitAge"] = self.__dict_to_value(df["InitAge"], float)

        df["InitConc"] = elements.InitialConcentration()
        df["InitConc"] = self.__dict_to_value(df["InitConc"], float)

        df["InitTrace"] = elements.InitialTrace()
        df["InitTrace"] = self.__dict_to_value(df["InitTrace"], float)
        return df

    def __get_installation_year_input(self, elements: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["InstallYr"] = elements.InstallationYears()
        df["InstallYr"] = self.__dict_to_value(df["InstallYr"], np.int64)
        return df

    def __get_minor_loss_node_input(self, elements: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["dMLossCoeff"] = elements.DerivedMinorLossCoefficient()
        df["dMLossCoeff"] = self.__dict_to_value(df["dMLossCoeff"], float)

        df["IsLocalMLoss"] = elements.SpecifyLocalMinorLoss()
        df["IsLocalMLoss"] = self.__dict_to_value(df["IsLocalMLoss"], bool)

        df["LocalMLossCoeff"] = elements.LocalMinorLossCoefficient()
        df["LocalMLossCoeff"] = self.__dict_to_value(
            df["LocalMLossCoeff"], float)

        return df

    def __get_valve_characerstics_input(self, elements: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["ValveChrsts"] = elements.ValveCharacteristics()
        df["ValveChrsts"] = self.__dict_to_value(df["ValveChrsts"], None)
        return df

    def __get_hammer_valve_type_input(self, elements: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["ValveType"] = elements.ValveTypes()
        df["ValveType"] = self.__dict_to_value(df["ValveType"], np.int64)
        return df

    def __get_demand_node_input(self, elements: IDemandNodesInput) -> pd.DataFrame:
        df = self.__get_base_node_input(elements)
        return df

    def __get_fire_node_input(self, elements: IFireFlowNodesInput) -> pd.DataFrame:
        df = self.__get_demand_node_input(elements)
        return df


# region Base Node / Link / Polygon Inputs

    def __get_base_node_input(self, elements: IBaseNodesInput) -> pd.DataFrame:
        df = self.__get_elements_input(elements)
        df = self.__get_physical_elevation_input(elements, df)
        df = self.__get_active_elements_input(elements, df)
        df = self.__get_zone_elements_input(elements, df)
        df = self.__get_water_quality_node_input(elements, df)
        df = self.__get_point_node_input(elements, df)
        return df

    def __get_base_link_input(self, elements: IBaseLinksInput) -> pd.DataFrame:
        df = pd.DataFrame()
        df = self.__get_elements_input(elements)
        df = self.__get_active_elements_input(elements, df)

        df["StartNode"] = elements.StartNodes()
        df["StartNode"] = self.__dict_to_value(df["StartNode"], None)
        df["StartNodeId"] = df["StartNode"].apply(
            lambda n: n.Id).astype(np.int64)

        df["StopNode"] = elements.StopNodes()
        df["StopNode"] = self.__dict_to_value(df["StopNode"], None)
        df["StopNodeId"] = df["StopNode"].apply(
            lambda n: n.Id).astype(np.int64)

        df["IsUDLength"] = elements.IsUserDefinedLengths()
        df["IsUDLength"] = self.__dict_to_value(df["IsUDLength"], bool)

        df["Length"] = elements.Lengths()
        df["Length"] = self.__dict_to_value(df["Length"], float)

        df["Geometry"] = elements.Geometries()
        df["Geometry"] = self.__dict_to_value(df["Geometry"], None)

        return df

    def __get_base_polygon_input(self, elements: IBasePolygonsInput) -> pd.DataFrame:
        df = pd.DataFrame()
        df = self.__get_elements_input(elements)
        df = self.__get_active_elements_input(elements, df)
        df = self.__get_polygons_geometry(elements, df)

        return df

    # endregion

    def __get_associated_elements(self, elements: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["AssocElem"] = elements.AssociatedElements()
        df["AssocElem"] = self.__dict_to_value(df["AssocElem"], None)
        df["AssocElemId"] = df["AssocElem"].apply(
            lambda n: n.Id).astype(np.int64)
        return df

    # region Base Elements Input

    def __get_base_directed_node_input(self, elements: IBaseDirectedNodesInput) -> pd.DataFrame:
        df = self.__get_base_node_input(elements)
        df = self.__get_installation_year_input(elements, df)

        return df

    def __get_base_pump_node_input(self, elements: IPumpsInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(elements)

        df["InitSpeedFactor"] = elements.InitialRelativeSpeedFactors()
        df["InitSpeedFactor"] = self.__dict_to_value(
            df["InitSpeedFactor"], float)

        df["InitStatus"] = elements.InitialStatus()
        df["InitStatus"] = self.__dict_to_value(df["InitStatus"], bool)

        return df

    def __get_base_valve_node_input(self, elements: IBaseValvesInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(elements)
        df = self.__get_minor_loss_node_input(elements, df)

        df["InitStatus"] = elements.InitialStatus()
        df["InitStatus"] = self.__dict_to_value(df["InitStatus"], None)

        df["Diameter"] = elements.Diameters()
        df["Diameter"] = self.__dict_to_value(df["Diameter"], float)
        return df

    def __get_base_tank_node_input(self, elements: IConventionalTanksInput) -> pd.DataFrame:
        df = self.__get_demand_node_input(elements)
        return df

    def __get_conventional_tank_node_input(self, elements: IConventionalTanksInput) -> pd.DataFrame:
        df = self.__get_demand_node_input(elements)
        df = self.__get_water_quality_node_input(elements, df)

        df["SectionType"] = elements.TankSection()
        df["SectionType"] = self.__dict_to_value(
            df["SectionType"], None)

        df["ActiveVolFull"] = elements.ActiveVolumeFull()
        df["ActiveVolFull"] = self.__dict_to_value(
            df["ActiveVolFull"], float)

        df["Diameter"] = elements.Diameter()
        df["Diameter"] = self.__dict_to_value(
            df["Diameter"], float)

        df["AvgArea"] = elements.AverageArea()
        df["AvgArea"] = self.__dict_to_value(
            df["AvgArea"], float)

        df["BaseElev"] = elements.BaseElevation()
        df["BaseElev"] = self.__dict_to_value(
            df["BaseElev"], float)

        df["MinLevel"] = elements.MinimumLevel()
        df["MinLevel"] = self.__dict_to_value(
            df["MinLevel"], float)

        df["MaxLevel"] = elements.MaximumLevel()
        df["MaxLevel"] = self.__dict_to_value(
            df["MaxLevel"], float)

        df["InitLevel"] = elements.InitialLevel()
        df["InitLevel"] = self.__dict_to_value(
            df["InitLevel"], float)

        df["UseHighAlarm"] = elements.UseHighAlarm()
        df["UseHighAlarm"] = self.__dict_to_value(
            df["UseHighAlarm"], bool)

        df["HighAlarmLvl"] = elements.HighAlarmLevel()
        df["HighAlarmLvl"] = self.__dict_to_value(
            df["HighAlarmLvl"], float)

        df["UseLowAlarm"] = elements.UseLowAlarm()
        df["UseLowAlarm"] = self.__dict_to_value(
            df["UseLowAlarm"], bool)

        df["LowAlarmLvl"] = elements.LowAlarmLevel()
        df["LowAlarmLvl"] = self.__dict_to_value(
            df["LowAlarmLvl"], float)

        df["InactiveVol"] = elements.InactiveVolume()
        df["InactiveVol"] = self.__dict_to_value(
            df["InactiveVol"], float)

        return df

    def __get_base_pressure_valve_node_input(self, elements: IPressureValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(elements)

        df["PressureSettings"] = elements.PressureValveSettings()
        df["PressureSettings"] = self.__dict_to_value(
            df["PressureSettings"], float)

        df["InitSetting"] = elements.InitialSettings()
        df["InitSetting"] = self.__dict_to_value(df["InitSetting"], None)

        return df

    def __get_general_purpose_valve_node_input(self, elements: IGeneralPurposeValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(elements)

        df["GpvHlCurve"] = elements.GPVHeadlossCurves()
        df["GpvHlCurve"] = self.__dict_to_value(df["GpvHlCurve"], None)

        df["ValveChrsts"] = elements.ValveCharacteristics()
        df["ValveChrsts"] = self.__dict_to_value(df["ValveChrsts"], None)

        return df

    def __get_tank_input(self, elements: ITanksInput) -> pd.DataFrame:
        df = self.__get_conventional_tank_node_input(elements)
        df = self.__get_valve_characerstics_input(elements, df)
        df = self.__get_hammer_valve_type_input(elements, df)
        return df

    def __get_hydro_tank_input(self, elements: IHydroTanksInput) -> pd.DataFrame:
        df = self.__get_base_tank_node_input(elements)

        df["InitGasVol"] = elements.InitialVolumeOfGas()
        df["InitGasVol"] = self.__dict_to_value(df["InitGasVol"], float)

        df["InletOrifDia"] = elements.TankInletOrificeDiameter()
        df["InletOrifDia"] = self.__dict_to_value(df["InletOrifDia"], float)

        df["RatioOfLosses"] = elements.RatioOfLosses()
        df["RatioOfLosses"] = self.__dict_to_value(df["RatioOfLosses"], float)

        df["GasLawExponent"] = elements.GasLawExponent()
        df["GasLawExponent"] = self.__dict_to_value(
            df["GasLawExponent"], float)

        df["HasBladder"] = elements.HasBladder()
        df["HasBladder"] = self.__dict_to_value(df["HasBladder"], bool)

        df["GasPresetPressure"] = elements.GasPresetPressure()
        df["GasPresetPressure"] = self.__dict_to_value(
            df["GasPresetPressure"], float)

        df["MeanLqdElev"] = elements.MeanLiquidElevation()
        df["MeanLqdElev"] = self.__dict_to_value(df["MeanLqdElev"], float)

        df["AirInOrifDia"] = elements.AirInflowOrificeDiameter()
        df["AirInOrifDia"] = self.__dict_to_value(df["AirInOrifDia"], float)

        df["AirOutOrifDia"] = elements.AirOutflowOrificeDiameter()
        df["AirOutOrifDia"] = self.__dict_to_value(df["AirOutOrifDia"], float)

        df["DippingTubeDia"] = elements.DippingTubeDiameter()
        df["DippingTubeDia"] = self.__dict_to_value(
            df["DippingTubeDia"], float)

        df["CompChamberVol"] = elements.CompressionChamberVolume()
        df["CompChamberVol"] = self.__dict_to_value(
            df["CompChamberVol"], float)

        df["TopElevDippingTube"] = elements.TopElevationDippingTube()
        df["TopElevDippingTube"] = self.__dict_to_value(
            df["TopElevDippingTube"], float)

        df["LevelType"] = elements.LevelType()
        df["LevelType"] = self.__dict_to_value(df["LevelType"], None)

        df["HydroTankType"] = elements.HydroTankType()
        df["HydroTankType"] = self.__dict_to_value(df["HydroTankType"], None)

        # df["AirOutOrifDia"] = elements.AirOutflowOrificeDiameter()
        # df["AirOutOrifDia"] = self.__dict_to_value(df["AirOutOrifDia"], float)

        # df["DippingTubeDia"] = elements.DippingTubeDiameter()
        # df["DippingTubeDia"] = self.__dict_to_value(df["DippingTubeDia"], float)

        # df["CompChamberVol"] = elements.CompressionChamberVolume()
        # df["CompChamberVol"] = self.__dict_to_value(df["CompChamberVol"], float)

        # df["TopElevDippingTube"] = elements.TopElevationDippingTube()
        # df["TopElevDippingTube"] = self.__dict_to_value(df["TopElevDippingTube"], float)

        return df

    def __get_reservoir_input(self, elements: IReservoirs) -> pd.DataFrame:
        df = self.__get_base_node_input(elements)
        return df

    def __get_tap_input(self, elements: ITaps) -> pd.DataFrame:
        df = self.__get_elements_input(elements)
        df = self.__get_point_node_input(elements, df)
        df = self.__get_associated_elements(elements, df)
        return df

    # endregion

    # region Pipes/Laterals

    def __get_pipe_input(self, elements: IPipes) -> pd.DataFrame:
        df = self.__get_base_link_input(elements)
        df = self.__get_installation_year_input(elements, df)

        df["Status"] = elements.Input.PipeStatuses()
        df["Status"] = self.__dict_to_value(df["Status"], bool)

        df["Diameter"] = elements.Input.Diameters()
        df["Diameter"] = self.__dict_to_value(df["Diameter"], float)

        df["Material"] = elements.Input.Materials()
        df["Material"] = self.__dict_to_value(df["Material"], str)

        df["FrictionCoeff"] = elements.Input.FrictionCoefficients()
        df["FrictionCoeff"] = self.__dict_to_value(df["FrictionCoeff"], float)

        return df

    def __get_lateral_input(self, elements: ILateralsInput) -> pd.DataFrame:
        df = self.__get_base_link_input(elements)
        return df

    # endregion

    # region Fireflow Nodes
    def __get_junction_input(self, elements: IJunctionsInput) -> pd.DataFrame:
        df = self.__get_fire_node_input(elements)
        return df

    def __get_hydrant_input(self, elements: IHydrantsInput) -> pd.DataFrame:
        df = self.__get_fire_node_input(elements)
        return df
    # endregion

    # region Pumps / Pump Stations / VSPB
    def __get_pump_input(self, elements: IPumpsInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(elements)

        df["InitSpeedFactor"] = elements.InitialRelativeSpeedFactors()
        df["InitSpeedFactor"] = self.__dict_to_value(
            df["InitSpeedFactor"], float)

        df["InitStatus"] = elements.InitialStatus()
        df["InitStatus"] = self.__dict_to_value(df["InitStatus"], np.int64)

        # TODO: double check the fields
        return df

    def __get_pump_stn_input(self, elements: IPumpStationsInput) -> pd.DataFrame:
        df = self.__get_base_polygon_input(elements)
        return df

    def __get_vspb_input(self, elements: IVSPBsInput) -> pd.DataFrame:
        df = self.__get_base_pump_node_input(elements)

        df["PumpDefinition"] = elements.PumpDefinitions()
        df["PumpDefinition"] = self.__dict_to_value(
            df["PumpDefinition"], None)
        df["PumpDefinitionId"] = df["PumpDefinition"].apply(
            lambda p: p.Id).astype(np.int64)

        df["ControlNode"] = elements.ControlNodes()
        df["ControlNode"] = self.__dict_to_value(
            df["ControlNode"], None)
        df["ControlNodeId"] = df["ControlNode"].apply(
            lambda p: p.Id).astype(np.int64)

        df["TgtHGL"] = elements.TargetHydraulicGrades()
        df["TgtHGL"] = self.__dict_to_value(
            df["TgtHGL"], float)

        df["MaxSpeedFactor"] = elements.MaximumRelativeSpeedFactors()
        df["MaxSpeedFactor"] = self.__dict_to_value(
            df["MaxSpeedFactor"], float)

        df["NumLagPumps"] = elements.NumberOfLagPumps()
        df["NumLagPumps"] = self.__dict_to_value(
            df["NumLagPumps"], np.int64)

        df["CtrlNodeSucSide"] = elements.ControlNodeOnSuctionSide()
        df["CtrlNodeSucSide"] = self.__dict_to_value(
            df["CtrlNodeSucSide"], None)
        df["CtrlNodeSucSideId"] = df["CtrlNodeSucSide"].apply(
            lambda p: p.Id).astype(np.int64)

        df["TgtFlow"] = elements.TargetFlows()
        df["TgtFlow"] = self.__dict_to_value(
            df["TgtFlow"], float)

        df["TgtPressure"] = elements.TargetPressures()
        df["TgtPressure"] = self.__dict_to_value(
            df["TgtPressure"], float)

        df["VSPBType"] = elements.VSPBTypes()
        df["VSPBType"] = self.__dict_to_value(
            df["VSPBType"], None)

        df["VSPBFixedHeadType"] = elements.VSPBFixedHeadTypes()
        df["VSPBFixedHeadType"] = self.__dict_to_value(
            df["VSPBFixedHeadType"], None)

        return df
    # endregion

    # region Customer Meters
    def __get_customer_meter_input(self, elements: ICustomerMetersInput) -> pd.DataFrame:
        df = self.__get_elements_input(elements)
        df = self.__get_point_node_input(elements, df)

        df["Demand"] = elements.BaseDemands()
        df["Demand"] = self.__dict_to_value(df["Demand"], float)

        df["Pattern"] = elements.DemandPatterns()
        df["Pattern"] = self.__dict_to_value(df["Pattern"], None)
        df["PatternId"] = df["Pattern"].apply(lambda p: p.Id).astype(np.int64)

        df["StartDemandDist"] = elements.StartDemandDistributions()
        df["StartDemandDist"] = self.__dict_to_value(
            df["StartDemandDist"], float)

        df["AssocElem"] = elements.AssociatedElements()
        df["AssocElem"] = self.__dict_to_value(df["AssocElem"], None)
        df["AssocElemId"] = df["AssocElem"].apply(
            lambda c: c.Id).astype(np.int64)

        df["UnitDemand"] = elements.UnitDemands()
        df["UnitDemand"] = self.__dict_to_value(df["UnitDemand"], float)

        df["UnitDmdPattern"] = elements.UnitDemandPatterns()
        df["UnitDmdPattern"] = self.__dict_to_value(df["UnitDmdPattern"], None)
        df["UnitDmdPatternId"] = df["UnitDmdPattern"].apply(
            lambda p: p.Id).astype(np.int64)

        df["NumUnitDmd"] = elements.UnitDemands()
        df["NumUnitDmd"] = self.__dict_to_value(df["NumUnitDmd"], float)

        return df

    # endregion

    # region SCADA Elements
    def __get_scada_elem_input(self, elements: ISCADAElementsInput) -> pd.DataFrame:
        df = self.__get_elements_input(elements)
        df = self.__get_point_node_input(elements, df)

        df["TgtElem"] = elements.TargetElements()
        df["TgtElem"] = self.__dict_to_value(df["TgtElem"], None)
        df["TgtElemId"] = df["TgtElem"].apply(lambda e: e.Id).astype(np.int64)

        df["HistSignal"] = elements.HistoricalSignals()
        df["HistSignal"] = self.__dict_to_value(df["HistSignal"], None)
        df["HistSignalId"] = df["HistSignal"].apply(
            lambda s: s.Id).astype(np.int64)
        return df
    # endregion

    # region Valves

    # region Pressure Valves
    def __get_prv_input(self, elements: IPressureBreakingValvesInput) -> pd.DataFrame:
        df = self.__get_base_pressure_valve_node_input(elements)
        df = self.__get_valve_characerstics_input(elements, df)
        df = self.__get_hammer_valve_type_input(elements, df)
        return df

    def __get_psv_input(self, elements: IPressureSustainingValvesInput) -> pd.DataFrame:
        df = self.__get_base_pressure_valve_node_input(elements)
        df = self.__get_valve_characerstics_input(elements, df)
        df = self.__get_hammer_valve_type_input(elements, df)
        return df

    def __get_pbv_input(self, elements: IPressureSustainingValvesInput) -> pd.DataFrame:
        df = self.__get_base_pressure_valve_node_input(elements)
        return df
    # endregion

    # region Flow / Throttle Control Valve
    def __get_fcv_input(self, elements: IFlowControlValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(elements)

        df["InitFlowSetting"] = elements.InitialFlowSettings()
        df["InitFlowSetting"] = self.__dict_to_value(
            df["InitFlowSetting"], float)

        df["Characteristic"] = elements.ValveCharacteristics()
        df["Characteristic"] = self.__dict_to_value(
            df["Characteristic"], float)
        return df

    def __get_tcv_input(self, elements: IThrottleControlValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(elements)

        df["CoeffType"] = elements.TCVCoefficientTypes()
        df["CoeffType"] = self.__dict_to_value(df["CoeffType"], None)

        df["InitCoeff"] = elements.InitialCoefficients()
        df["InitCoeff"] = self.__dict_to_value(df["InitCoeff"], float)

        df["Characteristic"] = elements.ValveCharacteristics()
        df["Characteristic"] = self.__dict_to_value(
            df["Characteristic"], float)

        return df

    # endregion

    # region General Purpose Valves

    def __get_gpv_input(self, elements: IGeneralPurposeValvesInput) -> pd.DataFrame:
        df = self.__get_general_purpose_valve_node_input(elements)
        return df
    # endregion

    # region Isolation Valves
    def __get_iso_valve_input(self, elements: IIsolationValveElementsInput) -> pd.DataFrame:
        df = self.__get_elements_input(elements)
        df = self.__get_point_node_input(elements, df)

        df["RefPipe"] = elements.ReferencedPipes()
        df["RefPipe"] = self.__dict_to_value(df["RefPipe"], None)
        df["RefPipeId"] = df["RefPipe"].apply(lambda p: p.Id).astype(np.int64)

        df["Diameter"] = elements.ValveDiameters()
        df["Diameter"] = self.__dict_to_value(df["Diameter"], float)

        df["MinorLossCoeff"] = elements.MinorLossCoefficients()
        df["MinorLossCoeff"] = self.__dict_to_value(
            df["MinorLossCoeff"], float)

        df["IsOperable"] = elements.IsOperables()
        df["IsOperable"] = self.__dict_to_value(df["IsOperable"], bool)

        df["InitStatus"] = elements.InitialStatuses()
        df["InitStatus"] = self.__dict_to_value(df["InitStatus"], None)

        df = self.__get_installation_year_input(elements, df)
        return df
    # endregion

    # region Check Valve
    def __get_check_valve_input(self, elements: ICheckValveElementsInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(elements)

        df["AtY"] = elements.LocatedAtWyes()
        df["AtY"] = self.__dict_to_value(df["AtY"], bool)

        df["FlowDirection"] = elements.FlowDirections()
        df["FlowDirection"] = self.__dict_to_value(df["FlowDirection"], None)

        df["InitTypFlow"] = elements.InitialTypicalFlows()
        df["InitTypFlow"] = self.__dict_to_value(df["InitTypFlow"], float)

        df["ThresPressure"] = elements.ThresholdPressures()
        df["ThresPressure"] = self.__dict_to_value(df["ThresPressure"], float)

        return df

    # endregion

    # endregion

    # endregion // private methods
