from OpenFlows.Domain.ModelingElements.NetworkElements import IBaseLinkUnits
from OpenFlows.Domain.ModelingElements import IGeometryUnits
from OpenFlows.Units import INetworkUnits, IComponentUnits
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IPumpUnits, IVariableSpeedPumpBatteryUnits, IFlowControlValveUnits, IGeneralPurposeValveUnits, IPressureBreakingValveUnits, IPressureReducingValveUnits, IPressureSustainingValveUnits, IThrottleControlValveUnits, IPipeUnits, IJunctionUnits, IHydrantUnits, ITankUnits, ICustomerMeterUnits, IReservoirUnits, ISpotElevationUnits, IValveWithLinearAreaChangeUnits, IPeriodicHeadFlowUnits, IAirValveUnits, IOrificeBetweenTwoPipesUnits, ISurgeValveUnits, IDischargeToAtmosphereUnits, IRuptureDiskUnits, ITurbineUnits, ISurgeTankUnits, IHydropneumaticTankUnits, IIsolationValveUnits, IPumpStationUnits, ICheckValveUnits
from OpenFlows.Water.Domain.ModelingElements.Components import IConstituentUnits, IControlConditionUnits, IControlActionUnits, IPatternUnits, IPumpDefinitionUnits, IUnitDemandLoadUnits, IAirFlowCurveUnits, IGPVHeadlossUnits, IValveCharacteristicUnits, IMinorLossCoefficientUnits

class INetworkElementUnits(INetworkUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pump(self) -> IPumpUnits:
		"""Units for pumps

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def VSPBUnits(self) -> IVariableSpeedPumpBatteryUnits:
		"""Units for VSPBs

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def FCV(self) -> IFlowControlValveUnits:
		"""FCV units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveUnits:
		"""GPV units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def PBV(self) -> IPressureBreakingValveUnits:
		"""PBV units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def PRV(self) -> IPressureReducingValveUnits:
		"""PRV units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def PSV(self) -> IPressureSustainingValveUnits:
		"""PSV units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveUnits:
		"""TCV units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Pipe(self) -> IPipeUnits:
		"""Pipe units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Lateral(self) -> IBaseLinkUnits:
		"""Lateral units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Junction(self) -> IJunctionUnits:
		"""Junction units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Hydrant(self) -> IHydrantUnits:
		"""Hydrant units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Tank(self) -> ITankUnits:
		"""Tank units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def CustomerMeter(self) -> ICustomerMeterUnits:
		"""Customer meter units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Reservoir(self) -> IReservoirUnits:
		"""Reservoir units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def SCADAElement(self) -> IGeometryUnits:
		"""SCADA element units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Tap(self) -> IGeometryUnits:
		"""Tap units

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def SpotElevation(self) -> ISpotElevationUnits:
		"""Units for spot eelvations

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def ValveWithLinearAreaChange(self) -> IValveWithLinearAreaChangeUnits:
		"""Units for valve with linear area change

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def PeriodicHeadFlow(self) -> IPeriodicHeadFlowUnits:
		"""Units for periodic head-flow nodes

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def AirValve(self) -> IAirValveUnits:
		"""Units for air valves

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def OrificeBetweenTwoPipes(self) -> IOrificeBetweenTwoPipesUnits:
		"""Units for orifice between two pipes

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def SurgeValve(self) -> ISurgeValveUnits:
		"""The units for surge valve (Sav/Srv)

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def DischargeToAtmosphere(self) -> IDischargeToAtmosphereUnits:
		"""Units for discharge to atmosphere nodes

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def RuptureDisk(self) -> IRuptureDiskUnits:
		"""Unit information for rupture disk

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def Turbine(self) -> ITurbineUnits:
		"""The unit information for turbines

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def SurgeTank(self) -> ISurgeTankUnits:
		"""Unit information for surge tank

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def HydropneumaticTank(self) -> IHydropneumaticTankUnits:
		"""Unit information for hydropneumatic tank

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def IsolationValve(self) -> IIsolationValveUnits:
		"""Units for isolation valves

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def PumpStation(self) -> IPumpStationUnits:
		"""Units for pump station

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

	@property
	def CheckValve(self) -> ICheckValveUnits:
		"""Units for check valve

		Returns
		--------
			``INetworkElementUnits`` : 
		"""
		pass

class IComponentElementUnits(IComponentUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Constituent(self) -> IConstituentUnits:
		"""Constituent units

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def Condition(self) -> IControlConditionUnits:
		"""Control condition units

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def Action(self) -> IControlActionUnits:
		"""Control action units

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def Pattern(self) -> IPatternUnits:
		"""Pattern units

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinitionUnits:
		"""Pump definition units

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def UnitDemandLoad(self) -> IUnitDemandLoadUnits:
		"""Unit demand load units

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def AirFlowCurve(self) -> IAirFlowCurveUnits:
		"""Units for air flow curve

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def GPVHeadlossCurve(self) -> IGPVHeadlossUnits:
		"""Unit information for GPV Headloss Curve

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def ValveCharacteristic(self) -> IValveCharacteristicUnits:
		"""Unit information for valve characteristic

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> IMinorLossCoefficientUnits:
		"""Unit information for minor loss

		Returns
		--------
			``IComponentElementUnits`` : 
		"""
		pass

class IWaterUnitsManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

