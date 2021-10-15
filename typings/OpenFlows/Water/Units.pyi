from OpenFlows.Domain.ModelingElements.NetworkElements import IBaseLinkUnits
from OpenFlows.Domain.ModelingElements import IGeometryUnits
from OpenFlows.Units import INetworkUnits, IComponentUnits
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IPumpUnits, IVariableSpeedPumpBatteryUnits, IFlowControlValveUnits, IGeneralPurposeValveUnits, IPressureBreakingValveUnits, IPressureReducingValveUnits, IPressureSustainingValveUnits, IThrottleControlValveUnits, IPipeUnits, IJunctionUnits, IHydrantUnits, ITankUnits, ICustomerMeterUnits, IReservoirUnits, ISpotElevationUnits, IValveWithLinearAreaChangeUnits, IPeriodicHeadFlowUnits, IAirValveUnits, IOrificeBetweenTwoPipesUnits, ISurgeValveUnits, IDischargeToAtmosphereUnits, IRuptureDiskUnits, ITurbineUnits, ISurgeTankUnits, IHydropneumaticTankUnits, IIsolationValveUnits, IPumpStationUnits, ICheckValveUnits
from OpenFlows.Water.Domain.ModelingElements.Components import IConstituentUnits, IControlConditionUnits, IControlActionUnits, IPatternUnits, IPumpDefinitionUnits, IUnitDemandLoadUnits, IAirFlowCurveUnits, IGPVHeadlossUnits, IValveCharacteristicUnits, IMinorLossCoefficientUnits

class INetworkElementUnits(INetworkUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pump(self) -> IPumpUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def VSPBUnits(self) -> IVariableSpeedPumpBatteryUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def FCV(self) -> IFlowControlValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def PBV(self) -> IPressureBreakingValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def PRV(self) -> IPressureReducingValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def PSV(self) -> IPressureSustainingValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Pipe(self) -> IPipeUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Lateral(self) -> IBaseLinkUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Junction(self) -> IJunctionUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Hydrant(self) -> IHydrantUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Tank(self) -> ITankUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def CustomerMeter(self) -> ICustomerMeterUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Reservoir(self) -> IReservoirUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def SCADAElement(self) -> IGeometryUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Tap(self) -> IGeometryUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def SpotElevation(self) -> ISpotElevationUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def ValveWithLinearAreaChange(self) -> IValveWithLinearAreaChangeUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def PeriodicHeadFlow(self) -> IPeriodicHeadFlowUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def AirValve(self) -> IAirValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def OrificeBetweenTwoPipes(self) -> IOrificeBetweenTwoPipesUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def SurgeValve(self) -> ISurgeValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def DischargeToAtmosphere(self) -> IDischargeToAtmosphereUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def RuptureDisk(self) -> IRuptureDiskUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def Turbine(self) -> ITurbineUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def SurgeTank(self) -> ISurgeTankUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def HydropneumaticTank(self) -> IHydropneumaticTankUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def IsolationValve(self) -> IIsolationValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def PumpStation(self) -> IPumpStationUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

	@property
	def CheckValve(self) -> ICheckValveUnits:
		"""No Description

		Returns:
			INetworkElementUnits: 
		"""
		pass

class IComponentElementUnits(IComponentUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Constituent(self) -> IConstituentUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def Condition(self) -> IControlConditionUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def Action(self) -> IControlActionUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def Pattern(self) -> IPatternUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinitionUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def UnitDemandLoad(self) -> IUnitDemandLoadUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def AirFlowCurve(self) -> IAirFlowCurveUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def GPVHeadlossCurve(self) -> IGPVHeadlossUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def ValveCharacteristic(self) -> IValveCharacteristicUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> IMinorLossCoefficientUnits:
		"""No Description

		Returns:
			IComponentElementUnits: 
		"""
		pass

class IWaterUnitsManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

