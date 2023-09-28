from OpenFlows.Domain.ModelingElements.INetworkElements import IBaseLinkUnits
from OpenFlows.Domain.IModelingElements import IGeometryUnits
from OpenFlows.IUnits import INetworkUnits, IComponentUnits
from OpenFlows.Water.Domain.ModelingElements.INetworkElements import IPumpUnits, IVariableSpeedPumpBatteryUnits, IFlowControlValveUnits, IGeneralPurposeValveUnits, IPressureBreakingValveUnits, IPressureReducingValveUnits, IPressureSustainingValveUnits, IThrottleControlValveUnits, IPipeUnits, IJunctionUnits, IHydrantUnits, ITankUnits, ICustomerMeterUnits, IReservoirUnits, ISpotElevationUnits, IValveWithLinearAreaChangeUnits, IPeriodicHeadFlowUnits, IAirValveUnits, IOrificeBetweenTwoPipesUnits, ISurgeValveUnits, IDischargeToAtmosphereUnits, IRuptureDiskUnits, ITurbineUnits, ISurgeTankUnits, IHydropneumaticTankUnits, IIsolationValveUnits, IPumpStationUnits, ICheckValveUnits
from OpenFlows.Water.Domain.ModelingElements.IComponents import IConstituentUnits, IControlConditionUnits, IControlActionUnits, IPatternUnits, IPumpDefinitionUnits, IUnitDemandLoadUnits, IAirFlowCurveUnits, IGPVHeadlossUnits, IValveCharacteristicUnits, IMinorLossCoefficientUnits

class INetworkElementUnits(INetworkUnits):

	def __new__(self) -> None:
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
			`IPumpUnits` : 
		"""
		pass

	@property
	def VSPBUnits(self) -> IVariableSpeedPumpBatteryUnits:
		"""Units for VSPBs

		Returns
		--------
			`IVariableSpeedPumpBatteryUnits` : 
		"""
		pass

	@property
	def FCV(self) -> IFlowControlValveUnits:
		"""FCV units

		Returns
		--------
			`IFlowControlValveUnits` : 
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveUnits:
		"""GPV units

		Returns
		--------
			`IGeneralPurposeValveUnits` : 
		"""
		pass

	@property
	def PBV(self) -> IPressureBreakingValveUnits:
		"""PBV units

		Returns
		--------
			`IPressureBreakingValveUnits` : 
		"""
		pass

	@property
	def PRV(self) -> IPressureReducingValveUnits:
		"""PRV units

		Returns
		--------
			`IPressureReducingValveUnits` : 
		"""
		pass

	@property
	def PSV(self) -> IPressureSustainingValveUnits:
		"""PSV units

		Returns
		--------
			`IPressureSustainingValveUnits` : 
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveUnits:
		"""TCV units

		Returns
		--------
			`IThrottleControlValveUnits` : 
		"""
		pass

	@property
	def Pipe(self) -> IPipeUnits:
		"""Pipe units

		Returns
		--------
			`IPipeUnits` : 
		"""
		pass

	@property
	def Lateral(self) -> IBaseLinkUnits:
		"""Lateral units

		Returns
		--------
			`IBaseLinkUnits` : 
		"""
		pass

	@property
	def Junction(self) -> IJunctionUnits:
		"""Junction units

		Returns
		--------
			`IJunctionUnits` : 
		"""
		pass

	@property
	def Hydrant(self) -> IHydrantUnits:
		"""Hydrant units

		Returns
		--------
			`IHydrantUnits` : 
		"""
		pass

	@property
	def Tank(self) -> ITankUnits:
		"""Tank units

		Returns
		--------
			`ITankUnits` : 
		"""
		pass

	@property
	def CustomerMeter(self) -> ICustomerMeterUnits:
		"""Customer meter units

		Returns
		--------
			`ICustomerMeterUnits` : 
		"""
		pass

	@property
	def Reservoir(self) -> IReservoirUnits:
		"""Reservoir units

		Returns
		--------
			`IReservoirUnits` : 
		"""
		pass

	@property
	def SCADAElement(self) -> IGeometryUnits:
		"""SCADA element units

		Returns
		--------
			`IGeometryUnits` : 
		"""
		pass

	@property
	def Tap(self) -> IGeometryUnits:
		"""Tap units

		Returns
		--------
			`IGeometryUnits` : 
		"""
		pass

	@property
	def SpotElevation(self) -> ISpotElevationUnits:
		"""Units for spot eelvations

		Returns
		--------
			`ISpotElevationUnits` : 
		"""
		pass

	@property
	def ValveWithLinearAreaChange(self) -> IValveWithLinearAreaChangeUnits:
		"""Units for valve with linear area change

		Returns
		--------
			`IValveWithLinearAreaChangeUnits` : 
		"""
		pass

	@property
	def PeriodicHeadFlow(self) -> IPeriodicHeadFlowUnits:
		"""Units for periodic head-flow nodes

		Returns
		--------
			`IPeriodicHeadFlowUnits` : 
		"""
		pass

	@property
	def AirValve(self) -> IAirValveUnits:
		"""Units for air valves

		Returns
		--------
			`IAirValveUnits` : 
		"""
		pass

	@property
	def OrificeBetweenTwoPipes(self) -> IOrificeBetweenTwoPipesUnits:
		"""Units for orifice between two pipes

		Returns
		--------
			`IOrificeBetweenTwoPipesUnits` : 
		"""
		pass

	@property
	def SurgeValve(self) -> ISurgeValveUnits:
		"""The units for surge valve (Sav/Srv)

		Returns
		--------
			`ISurgeValveUnits` : 
		"""
		pass

	@property
	def DischargeToAtmosphere(self) -> IDischargeToAtmosphereUnits:
		"""Units for discharge to atmosphere nodes

		Returns
		--------
			`IDischargeToAtmosphereUnits` : 
		"""
		pass

	@property
	def RuptureDisk(self) -> IRuptureDiskUnits:
		"""Unit information for rupture disk

		Returns
		--------
			`IRuptureDiskUnits` : 
		"""
		pass

	@property
	def Turbine(self) -> ITurbineUnits:
		"""The unit information for turbines

		Returns
		--------
			`ITurbineUnits` : 
		"""
		pass

	@property
	def SurgeTank(self) -> ISurgeTankUnits:
		"""Unit information for surge tank

		Returns
		--------
			`ISurgeTankUnits` : 
		"""
		pass

	@property
	def HydropneumaticTank(self) -> IHydropneumaticTankUnits:
		"""Unit information for hydropneumatic tank

		Returns
		--------
			`IHydropneumaticTankUnits` : 
		"""
		pass

	@property
	def IsolationValve(self) -> IIsolationValveUnits:
		"""Units for isolation valves

		Returns
		--------
			`IIsolationValveUnits` : 
		"""
		pass

	@property
	def PumpStation(self) -> IPumpStationUnits:
		"""Units for pump station

		Returns
		--------
			`IPumpStationUnits` : 
		"""
		pass

	@property
	def CheckValve(self) -> ICheckValveUnits:
		"""Units for check valve

		Returns
		--------
			`ICheckValveUnits` : 
		"""
		pass

class IComponentElementUnits(IComponentUnits):

	def __new__(self) -> None:
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
			`IConstituentUnits` : 
		"""
		pass

	@property
	def Condition(self) -> IControlConditionUnits:
		"""Control condition units

		Returns
		--------
			`IControlConditionUnits` : 
		"""
		pass

	@property
	def Action(self) -> IControlActionUnits:
		"""Control action units

		Returns
		--------
			`IControlActionUnits` : 
		"""
		pass

	@property
	def Pattern(self) -> IPatternUnits:
		"""Pattern units

		Returns
		--------
			`IPatternUnits` : 
		"""
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinitionUnits:
		"""Pump definition units

		Returns
		--------
			`IPumpDefinitionUnits` : 
		"""
		pass

	@property
	def UnitDemandLoad(self) -> IUnitDemandLoadUnits:
		"""Unit demand load units

		Returns
		--------
			`IUnitDemandLoadUnits` : 
		"""
		pass

	@property
	def AirFlowCurve(self) -> IAirFlowCurveUnits:
		"""Units for air flow curve

		Returns
		--------
			`IAirFlowCurveUnits` : 
		"""
		pass

	@property
	def GPVHeadlossCurve(self) -> IGPVHeadlossUnits:
		"""Unit information for GPV Headloss Curve

		Returns
		--------
			`IGPVHeadlossUnits` : 
		"""
		pass

	@property
	def ValveCharacteristic(self) -> IValveCharacteristicUnits:
		"""Unit information for valve characteristic

		Returns
		--------
			`IValveCharacteristicUnits` : 
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> IMinorLossCoefficientUnits:
		"""Unit information for minor loss

		Returns
		--------
			`IMinorLossCoefficientUnits` : 
		"""
		pass

class IWaterUnitsManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

