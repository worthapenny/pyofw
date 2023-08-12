'''
Author: Akshaya Niraula
Create Time: 2021-10-14 19:35:38
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''
from OpenFlows.Domain.ModelingElements import IElementManager
from OpenFlows.Domain.ModelingElements.NetworkElements import IActiveElementsInput, IBaseLinksInput, IBasePolygonsInput, IPointNodesInput, IPointNodeInput
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IBaseDirectedNodesInput, IBaseNodesInput, IBasePumpsInput, IBaseValvesInput, ICheckValveElementsInput, IConventionalTanksInput, ICustomerMetersInput, IDemandNodesInput, IFireFlowNodesInput, IFlowControlValvesInput, IGeneralPurposeValves, IGeneralPurposeValvesInput, IHydrantsInput, IHydroTanksInput, IIsolationValveElementsInput, IJunctionsInput, ILateralsInput, IPhysicalNodeElementsInput, IPipesInput, IPressureBreakingValvesInput, IPressureBreakingValvesInput, IPressureSustainingValvesInput, IPressureValvesInput, IPumpStationsInput, IPumpsInput, IReservoirsInput, ISCADAElementsInput, ITanksInput, ITapsInput, IThrottleControlValvesInput, IVSPBsInput, IWaterQualityElementsInput, IWaterQualityNodesInput, IWaterZoneableNetworkElementsInput
from OpenFlows.Water.Domain import IWaterModel
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

    def __repr__(self) -> str:
        line1 = f"{__class__.__name__}: {self.__waterModel}. | "
        line2 = f"Pipes #: {self.__waterModel.Network.Pipes.Count} | "
        line3 = f"Junctions #: {self.__waterModel.Network.Junctions.Count}"
        return f"{line1} {line2} {line3}."
    # endregion

    # region Public Methods
    def get_networkx_graph(self, laterals: bool = False) -> nx.Graph:
        columns = ["Id", "Label", "StartNodeId", "StopNodeId"]
        if not laterals:
            columns += ["Diameter", "IsActive"]

        links_df = self.pipe_df[columns].copy()
        if laterals:
            links_df.append(self.lateral_df[columns])

        graph: nx.Graph = nx.from_pandas_edgelist(
            df=links_df,
            source="StartNodeId",
            target="StopNodeId",
            edge_attr=columns,
            )

        # Get Coordinates for all nodes
        all_node_ids = pd.concat([links_df["StartNodeId"], links_df["StopNodeId"]]).unique()

        node_loc_map = {}
        for node_id in all_node_ids:
            node_id = int(node_id)
            geo_point = IPointNodeInput(self.__waterModel.Element(node_id)).GetPoint()
            node_loc_map[node_id] = (geo_point.X, geo_point.Y)

        # update the location
        # link_loc_map = {}
        # for edge in graph.edges():
        #     links_df[edge] = node_loc_map[]
        nx.set_node_attributes(graph, node_loc_map, "pos")
        
        return graph

    # endregion // Public Methods

    # region Public Properties (Network Elements DF)

    @property
    def pipe_df(self) -> pd.DataFrame:
        return self.__get_pipe_input(self.__waterModel.Network.Pipes.Input)

    @property
    def lateral_df(self) -> pd.DataFrame:
        return self.__get_lateral_input(self.__waterModel.Network.Laterals.Input)

    @property
    def junction_df(self) -> pd.DataFrame:
        return self.__get_junction_input(self.__waterModel.Network.Junctions.Input)

    @property
    def hydrant_df(self) -> pd.DataFrame:
        return self.__get_hydrant_input(self.__waterModel.Network.Hydrants.Input)

    @property
    def tank_df(self) -> pd.DataFrame:
        return self.__get_tank_input(self.__waterModel.Network.Tanks.Input)

    @property
    def reservoir_df(self) -> pd.DataFrame:
        return self.__get_reservoir_input(self.__waterModel.Network.Reservoirs.Input)

    @property
    def tap_df(self) -> pd.DataFrame:
        return self.__get_tap_input(self.__waterModel.Network.Taps.Input)

    @property
    def pump_df(self) -> pd.DataFrame:
        return self.__get_pump_input(self.__waterModel.Network.Pumps.Input)

    @property
    def pump_stn_df(self) -> pd.DataFrame:
        return self.__get_pump_stn_input(self.__waterModel.Network.PumpStations.Input)

    @property
    def customer_meter_df(self) -> pd.DataFrame:
        return self.__get_customer_meter_input(self.__waterModel.Network.CustomerMeters.Input)

    @property
    def scada_elem_df(self) -> pd.DataFrame:
        return self.__get_scada_elem_input(self.__waterModel.Network.SCADAElements.Input)

    @property
    def vspb_df(self) -> pd.DataFrame:
        return self.__get_vspb_input(self.__waterModel.Network.VSPBs.Input)

    @property
    def prv_df(self) -> pd.DataFrame:
        return self.__get_prv_input(self.__waterModel.Network.PRVs.Input)

    @property
    def psv_df(self) -> pd.DataFrame:
        return self.__get_psv_input(self.__waterModel.Network.PSVs.Input)

    @property
    def pbv_df(self) -> pd.DataFrame:
        return self.__get_pbv_input(self.__waterModel.Network.PBVs.Input)

    @property
    def fcv_df(self) -> pd.DataFrame:
        return self.__get_fcv_input(self.__waterModel.Network.FCVs.Input)

    @property
    def tcv_df(self) -> pd.DataFrame:
        return self.__get_tcv_input(self.__waterModel.Network.TCVs.Input)

    @property
    def gpv_df(self) -> pd.DataFrame:
        return self.__get_gpv_input(self.__waterModel.Network.GPVs.Input)

    @property
    def iso_valve_df(self) -> pd.DataFrame:
        return self.__get_iso_valve_input(self.__waterModel.Network.IsolationValves.Input)

    @property
    def hydro_tank_df(self) -> pd.DataFrame:
        return self.__get_hydro_tank_input(self.__waterModel.Network.HydropneumaticTanks.Input)

    @property
    def check_valve_df(self) -> pd.DataFrame:
        return self.__get_check_valve_input(self.__waterModel.Network.CheckValves.Input)

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

    def __get_elements_input(self, elements) -> pd.DataFrame:
        df = pd.DataFrame()
        df["Label"] = IElementManager(elements).Labels()
        df["Id"] = df["Label"].apply(lambda d: d.Key).astype(pd.Int64Dtype())
        df["Label"] = df["Label"].apply(lambda d: d.Value).astype("string")
        return df

    def __get_physical_elevation_input(self, elementsInput: IPhysicalNodeElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Elevation"] = elementsInput.Elevations()
        df["Elevation"] = self.__dict_to_value(df["Elevation"], float)
        return df

    def __get_active_elements_input(self, elementsInput: IActiveElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["IsActive"] = elementsInput.IsActives()
        df["IsActive"] = self.__dict_to_value(df["IsActive"], bool)
        return df

    def __get_zone_elements_input(self, elementsInput: IWaterZoneableNetworkElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Zone"] = elementsInput.Zones()
        df["Zone"] = self.__dict_to_value(df["Zone"], None)

        df["ZoneId"] = df["Zone"].apply(lambda z: z.Id if z else None)
        df["ZoneLabel"] = df["Zone"].apply(
            lambda z: z.Label if z else None).astype("string")
        return df

    def __get_point_node_input(self, elementsInput: IPointNodesInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Geometry"] = elementsInput.Geometries()
        df["Geometry"] = self.__dict_to_value(df["Geometry"], None)

        x_and_y: List[Any] = df["Geometry"].apply(
            lambda p: [p.X, p.Y]).tolist()
        if x_and_y:  # TODO: find the type of x&y
            df[["X", "Y"]] = x_and_y
        else:
            df["X"] = None
            df["Y"] = None

        return df

    def __get_polygons_geometry(self, elementsInput: IBasePolygonsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["Geometry"] = elementsInput.Geometries()
        df["Geometry"] = self.__dict_to_value(df["Geometry"], None)

        df["Geometry"] = df["Geometry"].apply(
            lambda pts: [[p.X, p.Y] for p in pts]).tolist()
        return df

    def __get_water_quality_node_input(self, elementsInput: IWaterQualityElementsInput, df: pd.DataFrame) -> pd.DataFrame:
        df["InitAge"] = elementsInput.InitialAge()
        df["InitAge"] = self.__dict_to_value(df["InitAge"], float)

        df["InitConc"] = elementsInput.InitialConcentration()
        df["InitConc"] = self.__dict_to_value(df["InitConc"], float)

        df["InitTrace"] = elementsInput.InitialTrace()
        df["InitTrace"] = self.__dict_to_value(df["InitTrace"], float)
        return df

    def __get_installation_year_input(self, elementsInput: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["InstallYr"] = elementsInput.InstallationYears()
        df["InstallYr"] = self.__dict_to_value(
            df["InstallYr"], pd.Int64Dtype())
        return df

    def __get_minor_loss_node_input(self, elementsInput: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["dMLossCoeff"] = elementsInput.DerivedMinorLossCoefficient()
        df["dMLossCoeff"] = self.__dict_to_value(df["dMLossCoeff"], float)

        df["IsLocalMLoss"] = elementsInput.SpecifyLocalMinorLoss()
        df["IsLocalMLoss"] = self.__dict_to_value(df["IsLocalMLoss"], bool)

        df["LocalMLossCoeff"] = elementsInput.LocalMinorLossCoefficient()
        df["LocalMLossCoeff"] = self.__dict_to_value(
            df["LocalMLossCoeff"], float)

        return df

    def __get_valve_characteristics_input(self, elementsInput: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["ValveChrsts"] = elementsInput.ValveCharacteristics()
        df["ValveChrsts"] = self.__dict_to_value(df["ValveChrsts"], None)
        return df

    def __get_hammer_valve_type_input(self, elementsInput: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["ValveType"] = elementsInput.ValveTypes()
        df["ValveType"] = self.__dict_to_value(
            df["ValveType"], pd.Int64Dtype())
        return df

    def __get_demand_node_input(self, elementsInput: IDemandNodesInput) -> pd.DataFrame:
        df = self.__get_base_node_input(elementsInput)
        return df

    def __get_fire_node_input(self, elementsInput: IFireFlowNodesInput) -> pd.DataFrame:
        df = self.__get_demand_node_input(elementsInput)
        return df


# region Base Node / Link / Polygon Inputs


    def __get_base_node_input(self, elements: IBaseNodesInput) -> pd.DataFrame:
        df = self.__get_elements_input(elements)
        df = self.__get_physical_elevation_input(IPhysicalNodeElementsInput(elements), df)
        df = self.__get_active_elements_input(IActiveElementsInput(elements), df)
        df = self.__get_zone_elements_input(IWaterZoneableNetworkElementsInput(elements), df)
        df = self.__get_water_quality_node_input(IWaterQualityElementsInput(elements), df)
        df = self.__get_point_node_input(IPointNodesInput(elements), df)
        return df

    def __get_base_link_input(self, elements: IBaseLinksInput) -> pd.DataFrame:
        df = pd.DataFrame()
        df = self.__get_elements_input(elements)
        df = self.__get_active_elements_input(IActiveElementsInput(elements), df)

        df["StartNode"] = elements.StartNodes()
        df["StartNode"] = self.__dict_to_value(df["StartNode"], None)
        df["StartNodeId"] = df["StartNode"].apply(
            lambda n: n.Id).astype(pd.Int64Dtype())

        df["StopNode"] = elements.StopNodes()
        df["StopNode"] = self.__dict_to_value(df["StopNode"], None)
        df["StopNodeId"] = df["StopNode"].apply(
            lambda n: n.Id).astype(pd.Int64Dtype())

        df["IsUDLength"] = elements.IsUserDefinedLengths()
        df["IsUDLength"] = self.__dict_to_value(df["IsUDLength"], bool)

        df["Length"] = elements.Lengths()
        df["Length"] = self.__dict_to_value(df["Length"], float)

        df["Geometry"] = elements.Geometries()
        df["Geometry"] = self.__dict_to_value(df["Geometry"], None)

        return df

    def __get_base_polygon_input(self, elements) -> pd.DataFrame:
        df = pd.DataFrame()
        df = self.__get_elements_input(elements)
        df = self.__get_active_elements_input(IActiveElementsInput(elements), df)
        df = self.__get_polygons_geometry(IBasePolygonsInput(elements), df)

        return df

    # endregion

    def __get_associated_elements(self, elementsInput: Any, df: pd.DataFrame) -> pd.DataFrame:
        df["AssocElem"] = elementsInput.AssociatedElements()
        df["AssocElem"] = self.__dict_to_value(df["AssocElem"], None)
        df["AssocElemId"] = df["AssocElem"].apply(
            lambda n: n.Id if n else None).astype(pd.Int64Dtype())
        return df

    # region Base Elements Input

    def __get_base_directed_node_input(self, elementsInput: IBaseDirectedNodesInput) -> pd.DataFrame:
        df = self.__get_base_node_input(elementsInput)
        df = self.__get_installation_year_input(elementsInput, df)

        return df

    def __get_base_pump_node_input(self, elementsInput: IPumpsInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(IBaseDirectedNodesInput(elementsInput))

        df["InitSpeedFactor"] = elementsInput.InitialRelativeSpeedFactors()
        df["InitSpeedFactor"] = self.__dict_to_value(
            df["InitSpeedFactor"], float)

        df["InitStatus"] = elementsInput.InitialStatus()
        df["InitStatus"] = self.__dict_to_value(df["InitStatus"], bool)

        return df

    def __get_base_valve_node_input(self, elementsInput: IBaseValvesInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(IBaseDirectedNodesInput(elementsInput))
        df = self.__get_minor_loss_node_input(elementsInput, df)

        df["InitStatus"] = elementsInput.InitialStatus()
        df["InitStatus"] = self.__dict_to_value(df["InitStatus"], None)

        df["Diameter"] = elementsInput.Diameters()
        df["Diameter"] = self.__dict_to_value(df["Diameter"], float)
        return df

    def __get_base_tank_node_input(self, elementsInput: IConventionalTanksInput) -> pd.DataFrame:
        df = self.__get_demand_node_input(IDemandNodesInput(elementsInput))
        return df

    def __get_conventional_tank_node_input(self, elementsInput: IConventionalTanksInput) -> pd.DataFrame:
        df = self.__get_demand_node_input(IDemandNodesInput(elementsInput))
        df = self.__get_water_quality_node_input(IWaterQualityElementsInput(elementsInput), df)

        df["SectionType"] = elementsInput.TankSection()
        df["SectionType"] = self.__dict_to_value(
            df["SectionType"], None)

        df["ActiveVolFull"] = elementsInput.ActiveVolumeFull()
        df["ActiveVolFull"] = self.__dict_to_value(
            df["ActiveVolFull"], float)

        df["Diameter"] = elementsInput.Diameter()
        df["Diameter"] = self.__dict_to_value(
            df["Diameter"], float)

        df["AvgArea"] = elementsInput.AverageArea()
        df["AvgArea"] = self.__dict_to_value(
            df["AvgArea"], float)

        df["BaseElev"] = elementsInput.BaseElevation()
        df["BaseElev"] = self.__dict_to_value(
            df["BaseElev"], float)

        df["MinLevel"] = elementsInput.MinimumLevel()
        df["MinLevel"] = self.__dict_to_value(
            df["MinLevel"], float)

        df["MaxLevel"] = elementsInput.MaximumLevel()
        df["MaxLevel"] = self.__dict_to_value(
            df["MaxLevel"], float)

        df["InitLevel"] = elementsInput.InitialLevel()
        df["InitLevel"] = self.__dict_to_value(
            df["InitLevel"], float)

        df["UseHighAlarm"] = elementsInput.UseHighAlarm()
        df["UseHighAlarm"] = self.__dict_to_value(
            df["UseHighAlarm"], bool)

        df["HighAlarmLvl"] = elementsInput.HighAlarmLevel()
        df["HighAlarmLvl"] = self.__dict_to_value(
            df["HighAlarmLvl"], float)

        df["UseLowAlarm"] = elementsInput.UseLowAlarm()
        df["UseLowAlarm"] = self.__dict_to_value(
            df["UseLowAlarm"], bool)

        df["LowAlarmLvl"] = elementsInput.LowAlarmLevel()
        df["LowAlarmLvl"] = self.__dict_to_value(
            df["LowAlarmLvl"], float)

        df["InactiveVol"] = elementsInput.InactiveVolume()
        df["InactiveVol"] = self.__dict_to_value(
            df["InactiveVol"], float)

        return df

    def __get_base_pressure_valve_node_input(self, elementsInput: IPressureValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(IBaseValvesInput(elementsInput))

        df["PressureSettings"] = elementsInput.PressureValveSettings()
        df["PressureSettings"] = self.__dict_to_value(
            df["PressureSettings"], float)

        df["InitSetting"] = elementsInput.InitialSettings()
        df["InitSetting"] = self.__dict_to_value(df["InitSetting"], None)

        return df

    def __get_general_purpose_valve_node_input(self, elementsInput: IGeneralPurposeValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(IBaseValvesInput(elementsInput))

        df["GpvHlCurve"] = elementsInput.GPVHeadlossCurves()
        df["GpvHlCurve"] = self.__dict_to_value(df["GpvHlCurve"], None)

        df["ValveChrsts"] = elementsInput.ValveCharacteristics()
        df["ValveChrsts"] = self.__dict_to_value(df["ValveChrsts"], None)

        return df

    def __get_tank_input(self, elementsInput: ITanksInput) -> pd.DataFrame:
        df = self.__get_conventional_tank_node_input(IConventionalTanksInput(elementsInput))
        df = self.__get_valve_characteristics_input(elementsInput, df)
        # df = self.__get_hammer_valve_type_input(elementsInput, df)
        return df

    def __get_hydro_tank_input(self, elements: IHydroTanksInput) -> pd.DataFrame:
        df = self.__get_base_node_input(elements)

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

    def __get_reservoir_input(self, elementsInput: IReservoirsInput) -> pd.DataFrame:
        df = self.__get_base_node_input(IBaseNodesInput(elementsInput))
        return df

    def __get_tap_input(self, elementsInput: ITapsInput) -> pd.DataFrame:
        df = self.__get_elements_input(elementsInput)
        df = self.__get_point_node_input(IPointNodesInput(elementsInput), df)
        df = self.__get_associated_elements(elementsInput, df)
        return df

    # endregion

    # region Pipes/Laterals

    def __get_pipe_input(self, elementsInput: IPipesInput) -> pd.DataFrame:
        df = self.__get_base_link_input(IBaseLinksInput(elementsInput))
        df = self.__get_installation_year_input(elementsInput, df)

        df["Status"] = elementsInput.PipeStatuses()
        df["Status"] = self.__dict_to_value(df["Status"], bool)

        df["Diameter"] = elementsInput.Diameters()
        df["Diameter"] = self.__dict_to_value(df["Diameter"], float)

        df["Material"] = elementsInput.Materials()
        df["Material"] = self.__dict_to_value(df["Material"], str)

        df["FrictionCoeff"] = elementsInput.FrictionCoefficients()
        df["FrictionCoeff"] = self.__dict_to_value(df["FrictionCoeff"], float)

        return df

    def __get_lateral_input(self, elementsInput: ILateralsInput) -> pd.DataFrame:
        df = self.__get_base_link_input(IBaseLinksInput(elementsInput))
        return df

    # endregion

    # region Fireflow Nodes
    def __get_junction_input(self, elementsInput: IJunctionsInput) -> pd.DataFrame:
        df = self.__get_fire_node_input(IFireFlowNodesInput(elementsInput))
        return df

    def __get_hydrant_input(self, elementsInput: IHydrantsInput) -> pd.DataFrame:
        df = self.__get_fire_node_input(IFireFlowNodesInput(elementsInput))
        return df
    # endregion

    # region Pumps / Pump Stations / VSPB
    def __get_pump_input(self, elementsInput: IPumpsInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(IBaseDirectedNodesInput(elementsInput))

        df["InitSpeedFactor"] = elementsInput.InitialRelativeSpeedFactors()
        df["InitSpeedFactor"] = self.__dict_to_value(
            df["InitSpeedFactor"], float)

        df["InitStatus"] = elementsInput.InitialStatus()
        df["InitStatus"] = self.__dict_to_value(
            df["InitStatus"], pd.Int64Dtype())

        # TODO: double check the fields
        return df

    def __get_pump_stn_input(self, elementsInput: IPumpStationsInput) -> pd.DataFrame:
        df = self.__get_base_polygon_input(elementsInput)
        return df

    def __get_vspb_input(self, elementsInput: IVSPBsInput) -> pd.DataFrame:
        df = self.__get_base_pump_node_input(IBasePumpsInput(elementsInput))

        df["PumpDefinition"] = elementsInput.PumpDefinitions()
        df["PumpDefinition"] = self.__dict_to_value(
            df["PumpDefinition"], None)
        df["PumpDefinitionId"] = df["PumpDefinition"].apply(
            lambda p: p.Id if p else None).astype(pd.Int64Dtype())

        df["ControlNode"] = elementsInput.ControlNodes()
        df["ControlNode"] = self.__dict_to_value(
            df["ControlNode"], None)
        df["ControlNodeId"] = df["ControlNode"].apply(
            lambda p: p.Id if p else None).astype(pd.Int64Dtype())

        df["TgtHGL"] = elementsInput.TargetHydraulicGrades()
        df["TgtHGL"] = self.__dict_to_value(
            df["TgtHGL"], float)

        df["MaxSpeedFactor"] = elementsInput.MaximumRelativeSpeedFactors()
        df["MaxSpeedFactor"] = self.__dict_to_value(
            df["MaxSpeedFactor"], float)

        df["NumLagPumps"] = elementsInput.NumberOfLagPumps()
        df["NumLagPumps"] = self.__dict_to_value(
            df["NumLagPumps"], pd.Int64Dtype())

        df["CtrlNodeSucSide"] = elementsInput.ControlNodeOnSuctionSide()
        df["CtrlNodeSucSide"] = self.__dict_to_value(
            df["CtrlNodeSucSide"], None)
        df["CtrlNodeSucSideId"] = df["CtrlNodeSucSide"].apply(
            lambda p: p.Id if p else None).astype(pd.Int64Dtype())

        df["TgtFlow"] = elementsInput.TargetFlows()
        df["TgtFlow"] = self.__dict_to_value(
            df["TgtFlow"], float)

        df["TgtPressure"] = elementsInput.TargetPressures()
        df["TgtPressure"] = self.__dict_to_value(
            df["TgtPressure"], float)

        df["VSPBType"] = elementsInput.VSPBTypes()
        df["VSPBType"] = self.__dict_to_value(
            df["VSPBType"], None)

        df["VSPBFixedHeadType"] = elementsInput.VSPBFixedHeadTypes()
        df["VSPBFixedHeadType"] = self.__dict_to_value(
            df["VSPBFixedHeadType"], None)

        return df
    # endregion

    # region Customer Meters
    def __get_customer_meter_input(self, elementsInput: ICustomerMetersInput) -> pd.DataFrame:
        df = self.__get_elements_input(elementsInput)
        df = self.__get_point_node_input(IPointNodesInput(elementsInput), df)
        df = self.__get_physical_elevation_input(IPhysicalNodeElementsInput(elementsInput), df)

        df["Demand"] = elementsInput.BaseDemands()
        df["Demand"] = self.__dict_to_value(df["Demand"], float)

        df["Pattern"] = elementsInput.DemandPatterns()
        df["Pattern"] = self.__dict_to_value(df["Pattern"], None)
        df["PatternId"] = df["Pattern"].apply(
            lambda p: p.Id if p else None).astype(pd.Int64Dtype())

        df["StartDemandDist"] = elementsInput.StartDemandDistributions()
        df["StartDemandDist"] = self.__dict_to_value(
            df["StartDemandDist"], float)

        df["AssocElem"] = elementsInput.AssociatedElements()
        df["AssocElem"] = self.__dict_to_value(df["AssocElem"], None)
        df["AssocElemId"] = df["AssocElem"].apply(
            lambda c: c.Id if c else None).astype(pd.Int64Dtype())

        df["UnitDemand"] = elementsInput.UnitDemands()
        df["UnitDemand"] = self.__dict_to_value(df["UnitDemand"], float)

        df["UnitDmdPattern"] = elementsInput.UnitDemandPatterns()
        df["UnitDmdPattern"] = self.__dict_to_value(df["UnitDmdPattern"], None)
        df["UnitDmdPatternId"] = df["UnitDmdPattern"].apply(
            lambda p: p.Id if p else None).astype(pd.Int64Dtype())

        df["NumUnitDmd"] = elementsInput.UnitDemands()
        df["NumUnitDmd"] = self.__dict_to_value(df["NumUnitDmd"], float)

        return df

    # endregion

    # region SCADA Elements
    def __get_scada_elem_input(self, elementsInput: ISCADAElementsInput) -> pd.DataFrame:
        df = self.__get_elements_input(elementsInput)
        df = self.__get_point_node_input(IPointNodesInput(elementsInput), df)

        df["TgtElem"] = elementsInput.TargetElements()
        df["TgtElem"] = self.__dict_to_value(df["TgtElem"], None)
        df["TgtElemId"] = df["TgtElem"].apply(
            lambda e: e.Id if e else None).astype(pd.Int64Dtype())

        df["HistSignal"] = elementsInput.HistoricalSignals()
        df["HistSignal"] = self.__dict_to_value(df["HistSignal"], None)
        df["HistSignalId"] = df["HistSignal"].apply(
            lambda s: s.Id if s else None).astype(pd.Int64Dtype())
        return df
    # endregion

    # region Valves

    # region Pressure Valves
    def __get_prv_input(self, elementsInput: IPressureBreakingValvesInput) -> pd.DataFrame:
        df = self.__get_base_pressure_valve_node_input(IPressureValvesInput(elementsInput))
        df = self.__get_valve_characteristics_input(elementsInput, df)
        # df = self.__get_hammer_valve_type_input(elementsInput, df)
        return df

    def __get_psv_input(self, elementsInput: IPressureSustainingValvesInput) -> pd.DataFrame:
        df = self.__get_base_pressure_valve_node_input(IPressureValvesInput(elementsInput))
        df = self.__get_valve_characteristics_input(elementsInput, df)
        # df = self.__get_hammer_valve_type_input(elementsInput, df)
        return df

    def __get_pbv_input(self, elementsInput: IPressureSustainingValvesInput) -> pd.DataFrame:
        df = self.__get_base_pressure_valve_node_input(IPressureValvesInput(elementsInput))
        return df
    # endregion

    # region Flow / Throttle Control Valve
    def __get_fcv_input(self, elementsInput: IFlowControlValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(IBaseValvesInput(elementsInput))

        df["InitFlowSetting"] = elementsInput.InitialFlowSettings()
        df["InitFlowSetting"] = self.__dict_to_value(
            df["InitFlowSetting"], float)

        df["Characteristic"] = elementsInput.ValveCharacteristics()
        df["Characteristic"] = self.__dict_to_value(
            df["Characteristic"], float)
        return df

    def __get_tcv_input(self, elementsInput: IThrottleControlValvesInput) -> pd.DataFrame:
        df = self.__get_base_valve_node_input(IBaseValvesInput(elementsInput))

        df["CoeffType"] = elementsInput.TCVCoefficientTypes()
        df["CoeffType"] = self.__dict_to_value(df["CoeffType"], None)

        df["InitCoeff"] = elementsInput.InitialCoefficients()
        df["InitCoeff"] = self.__dict_to_value(df["InitCoeff"], float)

        df["Characteristic"] = elementsInput.ValveCharacteristics()
        df["Characteristic"] = self.__dict_to_value(
            df["Characteristic"], float)

        return df

    # endregion

    # region General Purpose Valves

    def __get_gpv_input(self, elementsInput: IGeneralPurposeValvesInput) -> pd.DataFrame:
        df = self.__get_general_purpose_valve_node_input(IGeneralPurposeValvesInput(elementsInput))
        return df
    # endregion

    # region Isolation Valves
    def __get_iso_valve_input(self, elementsInput: IIsolationValveElementsInput) -> pd.DataFrame:
        df = self.__get_elements_input(elementsInput)
        df = self.__get_point_node_input(IPointNodesInput(elementsInput), df)

        df["RefPipe"] = elementsInput.ReferencedPipes()
        df["RefPipe"] = self.__dict_to_value(df["RefPipe"], None)
        df["RefPipeId"] = df["RefPipe"].apply(
            lambda p: p.Id if p else None).astype(pd.Int64Dtype())

        df["Diameter"] = elementsInput.ValveDiameters()
        df["Diameter"] = self.__dict_to_value(df["Diameter"], float)

        df["MinorLossCoeff"] = elementsInput.MinorLossCoefficients()
        df["MinorLossCoeff"] = self.__dict_to_value(
            df["MinorLossCoeff"], float)

        df["IsOperable"] = elementsInput.IsOperables()
        df["IsOperable"] = self.__dict_to_value(df["IsOperable"], bool)

        df["InitStatus"] = elementsInput.InitialStatuses()
        df["InitStatus"] = self.__dict_to_value(df["InitStatus"], None)

        df = self.__get_installation_year_input(elementsInput, df)
        return df
    # endregion

    # region Check Valve
    def __get_check_valve_input(self, elementsInput: ICheckValveElementsInput) -> pd.DataFrame:
        df = self.__get_base_directed_node_input(IBaseDirectedNodesInput(elementsInput))

        df["AtY"] = elementsInput.LocatedAtWyes()
        df["AtY"] = self.__dict_to_value(df["AtY"], bool)

        df["FlowDirection"] = elementsInput.FlowDirections()
        df["FlowDirection"] = self.__dict_to_value(df["FlowDirection"], None)

        df["InitTypFlow"] = elementsInput.InitialTypicalFlows()
        df["InitTypFlow"] = self.__dict_to_value(df["InitTypFlow"], float)

        df["ThresPressure"] = elementsInput.ThresholdPressures()
        df["ThresPressure"] = self.__dict_to_value(df["ThresPressure"], float)

        return df

    # endregion

    # endregion

    # endregion // private methods
