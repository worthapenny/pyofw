from OpenFlows.Domain.ModelingElements.Collections import ICollectionElements, ICollection, ICollectionElement
from typing import overload, Generic
from OpenFlows.Units import IUnit
from OpenFlows.Domain.ModelingElements import IElementUnits, IElement, TElementManagerType, TElementType, TUnitsType
from enum import Enum
from datetime import datetime
from OpenFlows.Domain.ModelingElements.Components import IComponentElements, IComponentElement, IModelComponents
from Haestad.Support.Units import PopulationUnit, AreaUnit
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IWaterElement, IPipe, IPump, IThrottleControlValve, IGeneralPurposeValve, IFlowControlValve, IPressureSustainingValve, IPressureBreakingValve, IPressureReducingValve, IReservoir, IJunction, IHydrant, ITank


class ConditionComparisonOperator(Enum):
	Equals = 0
	GreaterThan = 1
	GreaterThanEqual = 2
	LessThan = 3
	LessThanEQual = 4
	NotEQual = 5

class PumpAttribute(Enum):
	Setting = 1
	TargetPressure = 2
	TargetHead = 3

class PressureValveAttribute(Enum):
	HydraulicGrade = 0
	Pressure = 2

class PumpConditionAttribute(Enum):
	Discharge = 0
	Setting = 1

class PressureValveConditionAttribute(Enum):
	Discharge = 0
	Setting = 1

class FCVConditionAttribute(Enum):
	Discharge = 0
	Setting = 1

class TCVConditionAttribute(Enum):
	Discharge = 0
	Setting = 1

class WaterComponentType(Enum):
	Pattern = 50
	PumpDefinition = 51
	Constituent = 52
	Zone = 53
	Control = 54
	ControlAction = 55
	ControlCondition = 56
	ControlSet = 59
	PDD = 60
	EnergyPrice = 61
	UnitDemandLoad = 62
	GPVHeadloss = 63
	ValveCharacteristic = 66
	AirFlowCurve = 68
	MinorLoss = 101
	UnitCarbonEmission = 202
	PowerMeter = 203
	MSXSetup = 220
	SCADASignal = 257

class SCADASignalTransformMethod(Enum):
	Threshold = 0
	Range = 1
	Formula = 2

class IAirFlowPressureCollection(ICollectionElements[IAirFlowPressures, IAirFlowPressure, IAirFlowPressureUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirFlowPressures(ICollection[IAirFlowPressure]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, pressure: float) -> IAirFlowPressure:
		"""No Description

		Args:
			flow(float): flow
			pressure(float): pressure

		Returns:
			IAirFlowPressure: 
		"""
		pass

	@overload
	def Add(self) -> IAirFlowPressure:
		"""No Description

		Returns:
			IAirFlowPressure: 
		"""
		pass

class IAirFlowPressure(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IAirFlowPressure: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""No Description

		Returns:
			IAirFlowPressure: 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class IAirFlowPressureUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirFlowPressureUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirFlowPressureUnits: 
		"""
		pass

class IAirFlowCurve(IWaterComponentBase[IAirFlowCurves, IAirFlowCurve, IAirFlowCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AirFlowPressureCollection(self) -> IAirFlowPressureCollection:
		"""No Description

		Returns:
			IAirFlowCurve: 
		"""
		pass

class IAirFlowCurves(IWaterComponentsBase[IAirFlowCurves, IAirFlowCurve, IAirFlowCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirFlowCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControl(IWaterComponentBase[IControls, IControl, IElementUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ControlType(self) -> ControlTypeEnum:
		"""No Description

		Returns:
			IControl: 
		"""
		pass

	@ControlType.setter
	def ControlType(self, controltype: ControlTypeEnum) -> None:
		pass

	@property
	def Condition(self) -> IControlCondition:
		"""No Description

		Returns:
			IControl: 
		"""
		pass

	@Condition.setter
	def Condition(self, condition: IControlCondition) -> None:
		pass

	@property
	def Action(self) -> IControlAction:
		"""No Description

		Returns:
			IControl: 
		"""
		pass

	@Action.setter
	def Action(self, action: IControlAction) -> None:
		pass

	@property
	def LogicalControl(self) -> ILogicalControl:
		"""No Description

		Returns:
			IControl: 
		"""
		pass

	@property
	def DefineDescription(self) -> bool:
		"""No Description

		Returns:
			IControl: 
		"""
		pass

	@DefineDescription.setter
	def DefineDescription(self, definedescription: bool) -> None:
		pass

	@property
	def Description(self) -> str:
		"""No Description

		Returns:
			IControl: 
		"""
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

	@property
	def Summary(self) -> str:
		"""No Description

		Returns:
			IControl: 
		"""
		pass

class ILogicalControl:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsLogicalControl(self) -> bool:
		"""No Description

		Returns:
			ILogicalControl: 
		"""
		pass

	@property
	def HasPriority(self) -> bool:
		"""No Description

		Returns:
			ILogicalControl: 
		"""
		pass

	@HasPriority.setter
	def HasPriority(self, haspriority: bool) -> None:
		pass

	@property
	def Priority(self) -> ControlPriorityEnum:
		"""No Description

		Returns:
			ILogicalControl: 
		"""
		pass

	@Priority.setter
	def Priority(self, priority: ControlPriorityEnum) -> None:
		pass

	@property
	def HasElse(self) -> bool:
		"""No Description

		Returns:
			ILogicalControl: 
		"""
		pass

	@HasElse.setter
	def HasElse(self, haselse: bool) -> None:
		pass

	@property
	def ElseAction(self) -> IControlAction:
		"""No Description

		Returns:
			ILogicalControl: 
		"""
		pass

	@ElseAction.setter
	def ElseAction(self, elseaction: IControlAction) -> None:
		pass

class IControls(IWaterComponentsBase[IControls, IControl, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlCondition(IWaterComponentBase[IControlConditions, IControlCondition, IControlConditionUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ConditionType(self) -> ConditionTypeEnum:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@ConditionType.setter
	def ConditionType(self, conditiontype: ConditionTypeEnum) -> None:
		pass

	@property
	def SimpleConditionType(self) -> SimpleConditionType:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@SimpleConditionType.setter
	def SimpleConditionType(self, simpleconditiontype: SimpleConditionType) -> None:
		pass

	@property
	def ElementCondition(self) -> IElementControlConditionInput:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@property
	def SystemDemandCondition(self) -> ISystemDemandConditionInput:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@property
	def ClockTimeCondition(self) -> IClockTimeConditionInput:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@property
	def TimeFromStartCondition(self) -> ITimeFromStartConditionInput:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@property
	def CompositeConditionCollection(self) -> ICompositeConditionCollection:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@property
	def IsUserDefinedDescriptionFormat(self) -> bool:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@IsUserDefinedDescriptionFormat.setter
	def IsUserDefinedDescriptionFormat(self, isuserdefineddescriptionformat: bool) -> None:
		pass

	@property
	def Description(self) -> str:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

	@property
	def Summary(self) -> str:
		"""No Description

		Returns:
			IControlCondition: 
		"""
		pass

class IControlSimpleConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SimpleConditionType(self) -> SimpleConditionType:
		"""No Description

		Returns:
			IControlSimpleConditionInput: 
		"""
		pass

	@property
	def Comparison(self) -> ConditionComparisonOperator:
		"""No Description

		Returns:
			IControlSimpleConditionInput: 
		"""
		pass

	@Comparison.setter
	def Comparison(self, comparison: ConditionComparisonOperator) -> None:
		pass

class IElementControlConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsElementCondition(self) -> bool:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def Element(self) -> IWaterElement:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@Element.setter
	def Element(self, element: IWaterElement) -> None:
		pass

	@property
	def Node(self) -> INodeConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def Tank(self) -> ITankConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def Pump(self) -> IPumpConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def Pipe(self) -> IPipeConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def PressureValve(self) -> IPressureValveConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def FCV(self) -> IFlowControLValveConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def HydroTank(self) -> IHydroTankConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

	@property
	def SurgeTank(self) -> ISurgeTankConditionInput:
		"""No Description

		Returns:
			IElementControlConditionInput: 
		"""
		pass

class IElementConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Element(self) -> IWaterElement:
		"""No Description

		Returns:
			IElementConditionInput: 
		"""
		pass

class INodeConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def NodeAttribute(self) -> NodeAttributeEnum:
		"""No Description

		Returns:
			INodeConditionInput: 
		"""
		pass

	@NodeAttribute.setter
	def NodeAttribute(self, nodeattribute: NodeAttributeEnum) -> None:
		pass

	@property
	def Demand(self) -> float:
		"""No Description

		Returns:
			INodeConditionInput: 
		"""
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""No Description

		Returns:
			INodeConditionInput: 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""No Description

		Returns:
			INodeConditionInput: 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ITankConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TankAttribute(self) -> TankAttributeEnum:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@TankAttribute.setter
	def TankAttribute(self, tankattribute: TankAttributeEnum) -> None:
		pass

	@property
	def Demand(self) -> float:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

	@property
	def Level(self) -> float:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@Level.setter
	def Level(self, level: float) -> None:
		pass

	@property
	def TimeToDrain(self) -> float:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@TimeToDrain.setter
	def TimeToDrain(self, timetodrain: float) -> None:
		pass

	@property
	def TimeToFill(self) -> float:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@TimeToFill.setter
	def TimeToFill(self, timetofill: float) -> None:
		pass

	@property
	def PercentFull(self) -> float:
		"""No Description

		Returns:
			ITankConditionInput: 
		"""
		pass

	@PercentFull.setter
	def PercentFull(self, percentfull: float) -> None:
		pass

class IPumpConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpAttribute(self) -> ControlConditionPumpAttribute:
		"""No Description

		Returns:
			IPumpConditionInput: 
		"""
		pass

	@PumpAttribute.setter
	def PumpAttribute(self, pumpattribute: ControlConditionPumpAttribute) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""No Description

		Returns:
			IPumpConditionInput: 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def PumpSetting(self) -> float:
		"""No Description

		Returns:
			IPumpConditionInput: 
		"""
		pass

	@PumpSetting.setter
	def PumpSetting(self, pumpsetting: float) -> None:
		pass

	@property
	def PumpStatus(self) -> PumpStatus:
		"""No Description

		Returns:
			IPumpConditionInput: 
		"""
		pass

	@PumpStatus.setter
	def PumpStatus(self, pumpstatus: PumpStatus) -> None:
		pass

class IPipeConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PipeAttribute(self) -> ControlConditionPipeAttribute:
		"""No Description

		Returns:
			IPipeConditionInput: 
		"""
		pass

	@PipeAttribute.setter
	def PipeAttribute(self, pipeattribute: ControlConditionPipeAttribute) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""No Description

		Returns:
			IPipeConditionInput: 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def PipeStatus(self) -> PipeStatus:
		"""No Description

		Returns:
			IPipeConditionInput: 
		"""
		pass

	@PipeStatus.setter
	def PipeStatus(self, pipestatus: PipeStatus) -> None:
		pass

class IPressureValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureValveAttribute(self) -> ControlConditionPressureValveAttributeEnum:
		"""No Description

		Returns:
			IPressureValveConditionInput: 
		"""
		pass

	@PressureValveAttribute.setter
	def PressureValveAttribute(self, pressurevalveattribute: ControlConditionPressureValveAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""No Description

		Returns:
			IPressureValveConditionInput: 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""No Description

		Returns:
			IPressureValveConditionInput: 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@property
	def ValveStatus(self) -> ControlConditionValveStatus:
		"""No Description

		Returns:
			IPressureValveConditionInput: 
		"""
		pass

	@ValveStatus.setter
	def ValveStatus(self, valvestatus: ControlConditionValveStatus) -> None:
		pass

class IFlowControLValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FCVAttribute(self) -> ControlConditionFCVAttributeEnum:
		"""No Description

		Returns:
			IFlowControLValveConditionInput: 
		"""
		pass

	@FCVAttribute.setter
	def FCVAttribute(self, fcvattribute: ControlConditionFCVAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""No Description

		Returns:
			IFlowControLValveConditionInput: 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""No Description

		Returns:
			IFlowControLValveConditionInput: 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@property
	def FCVStatus(self) -> FCVStatusEnum:
		"""No Description

		Returns:
			IFlowControLValveConditionInput: 
		"""
		pass

	@FCVStatus.setter
	def FCVStatus(self, fcvstatus: FCVStatusEnum) -> None:
		pass

class IGeneralPurposeValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVAttribute(self) -> ControlConditionGPVAttributeEnum:
		"""No Description

		Returns:
			IGeneralPurposeValveConditionInput: 
		"""
		pass

	@GPVAttribute.setter
	def GPVAttribute(self, gpvattribute: ControlConditionGPVAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""No Description

		Returns:
			IGeneralPurposeValveConditionInput: 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def GPVStatus(self) -> ControlConditionGPVStatusEnum:
		"""No Description

		Returns:
			IGeneralPurposeValveConditionInput: 
		"""
		pass

	@GPVStatus.setter
	def GPVStatus(self, gpvstatus: ControlConditionGPVStatusEnum) -> None:
		pass

class IThrottleControlValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TCVAttribute(self) -> ControlConditionTCVAttributeEnum:
		"""No Description

		Returns:
			IThrottleControlValveConditionInput: 
		"""
		pass

	@TCVAttribute.setter
	def TCVAttribute(self, tcvattribute: ControlConditionTCVAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""No Description

		Returns:
			IThrottleControlValveConditionInput: 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""No Description

		Returns:
			IThrottleControlValveConditionInput: 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@property
	def TCVStatus(self) -> TCVStatusEnum:
		"""No Description

		Returns:
			IThrottleControlValveConditionInput: 
		"""
		pass

	@TCVStatus.setter
	def TCVStatus(self, tcvstatus: TCVStatusEnum) -> None:
		pass

class IHydroTankConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def HydroTankAttribute(self) -> HydroTankAttributeEnum:
		"""No Description

		Returns:
			IHydroTankConditionInput: 
		"""
		pass

	@HydroTankAttribute.setter
	def HydroTankAttribute(self, hydrotankattribute: HydroTankAttributeEnum) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""No Description

		Returns:
			IHydroTankConditionInput: 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""No Description

		Returns:
			IHydroTankConditionInput: 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ISurgeTankConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SurgeTankAttribute(self) -> SurgeTankAttributeEnum:
		"""No Description

		Returns:
			ISurgeTankConditionInput: 
		"""
		pass

	@SurgeTankAttribute.setter
	def SurgeTankAttribute(self, surgetankattribute: SurgeTankAttributeEnum) -> None:
		pass

	@property
	def Demand(self) -> float:
		"""No Description

		Returns:
			ISurgeTankConditionInput: 
		"""
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""No Description

		Returns:
			ISurgeTankConditionInput: 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""No Description

		Returns:
			ISurgeTankConditionInput: 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ISystemDemandConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsSystemDemandCondition(self) -> bool:
		"""No Description

		Returns:
			ISystemDemandConditionInput: 
		"""
		pass

	@property
	def SystemDemand(self) -> float:
		"""No Description

		Returns:
			ISystemDemandConditionInput: 
		"""
		pass

	@SystemDemand.setter
	def SystemDemand(self, systemdemand: float) -> None:
		pass

class IClockTimeConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsClockTimeCondition(self) -> bool:
		"""No Description

		Returns:
			IClockTimeConditionInput: 
		"""
		pass

	@property
	def ClockTime(self) -> datetime:
		"""No Description

		Returns:
			IClockTimeConditionInput: 
		"""
		pass

	@ClockTime.setter
	def ClockTime(self, clocktime: datetime) -> None:
		pass

class ITimeFromStartConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsTimeFromStartCondition(self) -> bool:
		"""No Description

		Returns:
			ITimeFromStartConditionInput: 
		"""
		pass

	@property
	def TimeFromStart(self) -> float:
		"""No Description

		Returns:
			ITimeFromStartConditionInput: 
		"""
		pass

	@TimeFromStart.setter
	def TimeFromStart(self, timefromstart: float) -> None:
		pass

class IControlConditions(IWaterComponentsBase[IControlConditions, IControlCondition, IControlConditionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlConditionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def LevelUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def TimeToFillUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def TimeToDrainUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def PercentFullUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def HeadlossCoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

	@property
	def TimeFromStartUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlConditionUnits: 
		"""
		pass

class ICompositeCondition(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LogicalOperator(self) -> LogicalOperatorEnum:
		"""No Description

		Returns:
			ICompositeCondition: 
		"""
		pass

	@LogicalOperator.setter
	def LogicalOperator(self, logicaloperator: LogicalOperatorEnum) -> None:
		pass

	@property
	def Condition(self) -> IControlCondition:
		"""No Description

		Returns:
			ICompositeCondition: 
		"""
		pass

	@Condition.setter
	def Condition(self, condition: IControlCondition) -> None:
		pass

class ICompositeConditions(ICollection[ICompositeCondition]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, logicalOperator: LogicalOperatorEnum, condition: IControlCondition) -> ICompositeCondition:
		"""No Description

		Args:
			logicalOperator(LogicalOperatorEnum): logicalOperator
			condition(IControlCondition): condition

		Returns:
			ICompositeCondition: 
		"""
		pass

	@overload
	def Add(self) -> ICompositeCondition:
		"""No Description

		Returns:
			ICompositeCondition: 
		"""
		pass

class ICompositeConditionCollection(ICollectionElements[ICompositeConditions, ICompositeCondition, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlAction(IWaterComponentBase[IControlActions, IControlAction, IControlActionUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ActionType(self) -> ControlActionTypeEnum:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@ActionType.setter
	def ActionType(self, actiontype: ControlActionTypeEnum) -> None:
		pass

	@property
	def Element(self) -> IWaterElement:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@Element.setter
	def Element(self, element: IWaterElement) -> None:
		pass

	@property
	def Pipe(self) -> IPipeActionInput:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@property
	def Pump(self) -> IPumpActionInput:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveActionInput:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveActionInput:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@property
	def FCV(self) -> IFlowControlValveActionInput:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@property
	def PressureValve(self) -> IPressureValveActionInput:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@property
	def CompositeActionCollection(self) -> ICompositeActionCollection:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@property
	def DefineDescription(self) -> bool:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@DefineDescription.setter
	def DefineDescription(self, definedescription: bool) -> None:
		pass

	@property
	def Description(self) -> str:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

	@property
	def Summary(self) -> str:
		"""No Description

		Returns:
			IControlAction: 
		"""
		pass

class IElementActionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Element(self) -> IWaterElement:
		"""No Description

		Returns:
			IElementActionInput: 
		"""
		pass

class IPipeActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPipeAction(self) -> bool:
		"""No Description

		Returns:
			IPipeActionInput: 
		"""
		pass

	@property
	def PipeAttribute(self) -> ControlActionPipeAttribute:
		"""No Description

		Returns:
			IPipeActionInput: 
		"""
		pass

	@PipeAttribute.setter
	def PipeAttribute(self, pipeattribute: ControlActionPipeAttribute) -> None:
		pass

	@property
	def PipeStatus(self) -> ControlActionPipeStatus:
		"""No Description

		Returns:
			IPipeActionInput: 
		"""
		pass

	@PipeStatus.setter
	def PipeStatus(self, pipestatus: ControlActionPipeStatus) -> None:
		pass

class IPumpActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPumpAction(self) -> bool:
		"""No Description

		Returns:
			IPumpActionInput: 
		"""
		pass

	@property
	def PumpAttribute(self) -> ControlActionPumpAttribute:
		"""No Description

		Returns:
			IPumpActionInput: 
		"""
		pass

	@PumpAttribute.setter
	def PumpAttribute(self, pumpattribute: ControlActionPumpAttribute) -> None:
		pass

	@property
	def PumpStatus(self) -> ControlActionPumpStatus:
		"""No Description

		Returns:
			IPumpActionInput: 
		"""
		pass

	@PumpStatus.setter
	def PumpStatus(self, pumpstatus: ControlActionPumpStatus) -> None:
		pass

	@property
	def RelativeSpeedFactor(self) -> float:
		"""No Description

		Returns:
			IPumpActionInput: 
		"""
		pass

	@RelativeSpeedFactor.setter
	def RelativeSpeedFactor(self, relativespeedfactor: float) -> None:
		pass

	@property
	def TargetPressure(self) -> float:
		"""No Description

		Returns:
			IPumpActionInput: 
		"""
		pass

	@TargetPressure.setter
	def TargetPressure(self, targetpressure: float) -> None:
		pass

	@property
	def TargetHead(self) -> float:
		"""No Description

		Returns:
			IPumpActionInput: 
		"""
		pass

	@TargetHead.setter
	def TargetHead(self, targethead: float) -> None:
		pass

class IThrottleControlValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsTCVAction(self) -> bool:
		"""No Description

		Returns:
			IThrottleControlValveActionInput: 
		"""
		pass

	@property
	def TCVAttribute(self) -> ControlActionTCVAttribute:
		"""No Description

		Returns:
			IThrottleControlValveActionInput: 
		"""
		pass

	@TCVAttribute.setter
	def TCVAttribute(self, tcvattribute: ControlActionTCVAttribute) -> None:
		pass

	@property
	def TCVStatus(self) -> ControlActionTCVStatus:
		"""No Description

		Returns:
			IThrottleControlValveActionInput: 
		"""
		pass

	@TCVStatus.setter
	def TCVStatus(self, tcvstatus: ControlActionTCVStatus) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""No Description

		Returns:
			IThrottleControlValveActionInput: 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

class IGeneralPurposeValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsGPVAction(self) -> bool:
		"""No Description

		Returns:
			IGeneralPurposeValveActionInput: 
		"""
		pass

	@property
	def GPVAttribute(self) -> ControlActionGPVAttribute:
		"""No Description

		Returns:
			IGeneralPurposeValveActionInput: 
		"""
		pass

	@GPVAttribute.setter
	def GPVAttribute(self, gpvattribute: ControlActionGPVAttribute) -> None:
		pass

	@property
	def GPVStatus(self) -> ControlActionGPVStatus:
		"""No Description

		Returns:
			IGeneralPurposeValveActionInput: 
		"""
		pass

	@GPVStatus.setter
	def GPVStatus(self, gpvstatus: ControlActionGPVStatus) -> None:
		pass

class IFlowControlValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsFCVAction(self) -> bool:
		"""No Description

		Returns:
			IFlowControlValveActionInput: 
		"""
		pass

	@property
	def FCVAttribute(self) -> ControlActionFCVAttribute:
		"""No Description

		Returns:
			IFlowControlValveActionInput: 
		"""
		pass

	@FCVAttribute.setter
	def FCVAttribute(self, fcvattribute: ControlActionFCVAttribute) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""No Description

		Returns:
			IFlowControlValveActionInput: 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def FCVStatus(self) -> ControlActionFCVStatus:
		"""No Description

		Returns:
			IFlowControlValveActionInput: 
		"""
		pass

	@FCVStatus.setter
	def FCVStatus(self, fcvstatus: ControlActionFCVStatus) -> None:
		pass

class IPressureValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPressureValveAction(self) -> bool:
		"""No Description

		Returns:
			IPressureValveActionInput: 
		"""
		pass

	@property
	def PressureValveAttribute(self) -> ControlActionPressureValveAttribute:
		"""No Description

		Returns:
			IPressureValveActionInput: 
		"""
		pass

	@PressureValveAttribute.setter
	def PressureValveAttribute(self, pressurevalveattribute: ControlActionPressureValveAttribute) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""No Description

		Returns:
			IPressureValveActionInput: 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""No Description

		Returns:
			IPressureValveActionInput: 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

	@property
	def PressureValveStatus(self) -> ControlActionPressureValveStatus:
		"""No Description

		Returns:
			IPressureValveActionInput: 
		"""
		pass

	@PressureValveStatus.setter
	def PressureValveStatus(self, pressurevalvestatus: ControlActionPressureValveStatus) -> None:
		pass

class IControlActions(IWaterComponentsBase[IControlActions, IControlAction, IControlActionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlActionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeSpeedFactorUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlActionUnits: 
		"""
		pass

	@property
	def TargetPressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlActionUnits: 
		"""
		pass

	@property
	def TargetHeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlActionUnits: 
		"""
		pass

	@property
	def HeadlossCoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlActionUnits: 
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlActionUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlActionUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IControlActionUnits: 
		"""
		pass

class ICompositeAction(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Action(self) -> IControlAction:
		"""No Description

		Returns:
			ICompositeAction: 
		"""
		pass

	@Action.setter
	def Action(self, action: IControlAction) -> None:
		pass

class ICompositeActions(ICollection[ICompositeAction]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, action: IControlAction) -> ICompositeAction:
		"""No Description

		Args:
			action(IControlAction): action

		Returns:
			ICompositeAction: 
		"""
		pass

	@overload
	def Add(self) -> ICompositeAction:
		"""No Description

		Returns:
			ICompositeAction: 
		"""
		pass

class ICompositeActionCollection(ICollectionElements[ICompositeActions, ICompositeAction, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ControlExtensionMethods:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pipe: IPipe, attribute: ControlActionPipeAttribute, status: ControlActionPipeStatus) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			pipe(IPipe): pipe
			attribute(ControlActionPipeAttribute): attribute
			status(ControlActionPipeStatus): status

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pump: IPump, attribute: PumpAttribute, value: float) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			pump(IPump): pump
			attribute(PumpAttribute): attribute
			value(float): value

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pump: IPump, status: ControlActionPumpStatus) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			pump(IPump): pump
			status(ControlActionPumpStatus): status

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, tcv: IThrottleControlValve, status: ControlActionTCVStatus) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			tcv(IThrottleControlValve): tcv
			status(ControlActionTCVStatus): status

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, tcv: IThrottleControlValve, value: float) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			tcv(IThrottleControlValve): tcv
			value(float): value

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, gpv: IGeneralPurposeValve, status: ControlActionGPVStatus) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			gpv(IGeneralPurposeValve): gpv
			status(ControlActionGPVStatus): status

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, fcv: IFlowControlValve, status: ControlActionFCVStatus) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			fcv(IFlowControlValve): fcv
			status(ControlActionFCVStatus): status

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, psv: IPressureSustainingValve, attribute: PressureValveAttribute, value: float) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			psv(IPressureSustainingValve): psv
			attribute(PressureValveAttribute): attribute
			value(float): value

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pbv: IPressureBreakingValve, attribute: PressureValveAttribute, value: float) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			pbv(IPressureBreakingValve): pbv
			attribute(PressureValveAttribute): attribute
			value(float): value

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, prv: IPressureReducingValve, attribute: PressureValveAttribute, value: float) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			prv(IPressureReducingValve): prv
			attribute(PressureValveAttribute): attribute
			value(float): value

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pbv: IPressureBreakingValve, status: ControlActionPressureValveStatus) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			pbv(IPressureBreakingValve): pbv
			status(ControlActionPressureValveStatus): status

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, prv: IPressureReducingValve, status: ControlActionPressureValveStatus) -> IControlAction:
		"""No Description

		Args:
			actions(IControlActions): actions
			prv(IPressureReducingValve): prv
			status(ControlActionPressureValveStatus): status

		Returns:
			IControlAction: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, reservoir: IReservoir, attribute: NodeAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			reservoir(IReservoir): reservoir
			attribute(NodeAttributeEnum): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, junction: IJunction, attribute: NodeAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			junction(IJunction): junction
			attribute(NodeAttributeEnum): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, hydrant: IHydrant, attribute: NodeAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			hydrant(IHydrant): hydrant
			attribute(NodeAttributeEnum): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, tank: ITank, attribute: TankAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			tank(ITank): tank
			attribute(TankAttributeEnum): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pump: IPump, attribute: PumpConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			pump(IPump): pump
			attribute(PumpConditionAttribute): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pump: IPump, status: PumpStatus) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			pump(IPump): pump
			status(PumpStatus): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pipe: IPipe, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			pipe(IPipe): pipe
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pipe: IPipe, status: PipeStatus) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			pipe(IPipe): pipe
			status(PipeStatus): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, psv: IPressureSustainingValve, attribute: PressureValveConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			psv(IPressureSustainingValve): psv
			attribute(PressureValveConditionAttribute): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, psv: IPressureSustainingValve, status: ControlConditionValveStatus) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			psv(IPressureSustainingValve): psv
			status(ControlConditionValveStatus): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pbv: IPressureBreakingValve, attribute: PressureValveConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			pbv(IPressureBreakingValve): pbv
			attribute(PressureValveConditionAttribute): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pbv: IPressureBreakingValve, status: ControlConditionValveStatus) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			pbv(IPressureBreakingValve): pbv
			status(ControlConditionValveStatus): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, prv: IPressureReducingValve, attribute: PressureValveConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			prv(IPressureReducingValve): prv
			attribute(PressureValveConditionAttribute): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, prv: IPressureReducingValve, status: ControlConditionValveStatus) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			prv(IPressureReducingValve): prv
			status(ControlConditionValveStatus): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, fcv: IFlowControlValve, attribute: FCVConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			fcv(IFlowControlValve): fcv
			attribute(FCVConditionAttribute): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, fcv: IFlowControlValve, status: FCVStatusEnum) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			fcv(IFlowControlValve): fcv
			status(FCVStatusEnum): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, gpv: IGeneralPurposeValve, status: ControlConditionGPVStatusEnum) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			gpv(IGeneralPurposeValve): gpv
			status(ControlConditionGPVStatusEnum): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, gpv: IGeneralPurposeValve, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			gpv(IGeneralPurposeValve): gpv
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, tcv: IThrottleControlValve, attribute: TCVConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			tcv(IThrottleControlValve): tcv
			attribute(TCVConditionAttribute): attribute
			op(ConditionComparisonOperator): op
			value(float): value

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, tcv: IThrottleControlValve, status: TCVStatusEnum) -> IControlCondition:
		"""No Description

		Args:
			conditions(IControlConditions): conditions
			tcv(IThrottleControlValve): tcv
			status(TCVStatusEnum): status

		Returns:
			IControlCondition: 
		"""
		pass

	@staticmethod
	def CreateControl(controls: IControls, controlStatement: str) -> IControl:
		"""No Description

		Args:
			controls(IControls): controls
			controlStatement(str): controlStatement

		Returns:
			IControl: 
		"""
		pass

class SCADASignalExtensions:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	def CreateFormulaSignal(scadaSignals: ISCADASignals, label: str, signalLabel: str, formula: str) -> ISCADASignal:
		"""No Description

		Args:
			scadaSignals(ISCADASignals): scadaSignals
			label(str): label
			signalLabel(str): signalLabel
			formula(str): formula

		Returns:
			ISCADASignal: 
		"""
		pass

	@staticmethod
	def CreateSignal(scadaSignals: ISCADASignals, label: str, signalLabel: str) -> ISCADASignal:
		"""No Description

		Args:
			scadaSignals(ISCADASignals): scadaSignals
			label(str): label
			signalLabel(str): signalLabel

		Returns:
			ISCADASignal: 
		"""
		pass

class IWaterComponent(IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElementType(self) -> WaterComponentType:
		"""No Description

		Returns:
			IWaterComponent: 
		"""
		pass

class IWaterComponentsBase(Generic[TElementManagerType, TElementType, TUnitsType], IComponentElements[TElementManagerType, TElementType, TUnitsType, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterComponentBase(Generic[TElementManagerType, TElementType, TUnitsType], IComponentElement[TElementManagerType, TElementType, TUnitsType, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IZones(IWaterComponentsBase[IZones, IZone, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IZone(IWaterComponentBase[IZones, IZone, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPattern(IWaterComponentBase[IPatterns, IPattern, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PatternCategory(self) -> PatternCategory:
		"""No Description

		Returns:
			IPattern: 
		"""
		pass

	@PatternCategory.setter
	def PatternCategory(self, patterncategory: PatternCategory) -> None:
		pass

	@property
	def PatternFormat(self) -> PatternFormat:
		"""No Description

		Returns:
			IPattern: 
		"""
		pass

	@PatternFormat.setter
	def PatternFormat(self, patternformat: PatternFormat) -> None:
		pass

	@property
	def PatternStartTime(self) -> datetime:
		"""No Description

		Returns:
			IPattern: 
		"""
		pass

	@PatternStartTime.setter
	def PatternStartTime(self, patternstarttime: datetime) -> None:
		pass

	@property
	def PatternStartingMultiplier(self) -> float:
		"""No Description

		Returns:
			IPattern: 
		"""
		pass

	@PatternStartingMultiplier.setter
	def PatternStartingMultiplier(self, patternstartingmultiplier: float) -> None:
		pass

	@property
	def PatternCurve(self) -> IPatternCurveCollection:
		"""No Description

		Returns:
			IPattern: 
		"""
		pass

	@property
	def DailyMultipliers(self) -> IDailyMultipliers:
		"""No Description

		Returns:
			IPattern: 
		"""
		pass

	@property
	def MonthlyMultipliers(self) -> IMonthlyMultipliers:
		"""No Description

		Returns:
			IPattern: 
		"""
		pass

class IPatternUnits(IPatternMultiplierUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeFromStartUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPatternUnits: 
		"""
		pass

class IPatternMultiplierUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MultiplierUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPatternMultiplierUnits: 
		"""
		pass

class IPatterns(IWaterComponentsBase[IPatterns, IPattern, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPatternCurveCollection(ICollectionElements[IPatternCurve, IPatternCurveElement, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPatternCurve(ICollection[IPatternCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, timeFromStart: float, multiplier: float) -> IPatternCurveElement:
		"""No Description

		Args:
			timeFromStart(float): timeFromStart
			multiplier(float): multiplier

		Returns:
			IPatternCurveElement: 
		"""
		pass

	@overload
	def Add(self) -> IPatternCurveElement:
		"""No Description

		Returns:
			IPatternCurveElement: 
		"""
		pass

class IPatternCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeFromStart(self) -> float:
		"""No Description

		Returns:
			IPatternCurveElement: 
		"""
		pass

	@TimeFromStart.setter
	def TimeFromStart(self, timefromstart: float) -> None:
		pass

	@property
	def Multiplier(self) -> float:
		"""No Description

		Returns:
			IPatternCurveElement: 
		"""
		pass

	@Multiplier.setter
	def Multiplier(self, multiplier: float) -> None:
		pass

class IDailyMultipliers:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Sunday(self) -> float:
		"""No Description

		Returns:
			IDailyMultipliers: 
		"""
		pass

	@Sunday.setter
	def Sunday(self, sunday: float) -> None:
		pass

	@property
	def Monday(self) -> float:
		"""No Description

		Returns:
			IDailyMultipliers: 
		"""
		pass

	@Monday.setter
	def Monday(self, monday: float) -> None:
		pass

	@property
	def Tuesday(self) -> float:
		"""No Description

		Returns:
			IDailyMultipliers: 
		"""
		pass

	@Tuesday.setter
	def Tuesday(self, tuesday: float) -> None:
		pass

	@property
	def Wednesday(self) -> float:
		"""No Description

		Returns:
			IDailyMultipliers: 
		"""
		pass

	@Wednesday.setter
	def Wednesday(self, wednesday: float) -> None:
		pass

	@property
	def Thursday(self) -> float:
		"""No Description

		Returns:
			IDailyMultipliers: 
		"""
		pass

	@Thursday.setter
	def Thursday(self, thursday: float) -> None:
		pass

	@property
	def Friday(self) -> float:
		"""No Description

		Returns:
			IDailyMultipliers: 
		"""
		pass

	@Friday.setter
	def Friday(self, friday: float) -> None:
		pass

	@property
	def Saturday(self) -> float:
		"""No Description

		Returns:
			IDailyMultipliers: 
		"""
		pass

	@Saturday.setter
	def Saturday(self, saturday: float) -> None:
		pass

class IMonthlyMultipliers:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def January(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@January.setter
	def January(self, january: float) -> None:
		pass

	@property
	def February(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@February.setter
	def February(self, february: float) -> None:
		pass

	@property
	def March(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@March.setter
	def March(self, march: float) -> None:
		pass

	@property
	def April(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@April.setter
	def April(self, april: float) -> None:
		pass

	@property
	def May(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@May.setter
	def May(self, may: float) -> None:
		pass

	@property
	def June(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@June.setter
	def June(self, june: float) -> None:
		pass

	@property
	def July(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@July.setter
	def July(self, july: float) -> None:
		pass

	@property
	def August(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@August.setter
	def August(self, august: float) -> None:
		pass

	@property
	def September(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@September.setter
	def September(self, september: float) -> None:
		pass

	@property
	def October(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@October.setter
	def October(self, october: float) -> None:
		pass

	@property
	def November(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@November.setter
	def November(self, november: float) -> None:
		pass

	@property
	def December(self) -> float:
		"""No Description

		Returns:
			IMonthlyMultipliers: 
		"""
		pass

	@December.setter
	def December(self, december: float) -> None:
		pass

class IPumpDefinitions(IWaterComponentsBase[IPumpDefinitions, IPumpDefinition, IPumpDefinitionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinition(IWaterComponentBase[IPumpDefinitions, IPumpDefinition, IPumpDefinitionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Head(self) -> IPumpDefinitionHead:
		"""No Description

		Returns:
			IPumpDefinition: 
		"""
		pass

	@property
	def Efficiency(self) -> IPumpDefinitionEfficiency:
		"""No Description

		Returns:
			IPumpDefinition: 
		"""
		pass

	@property
	def NPSH(self) -> IPumpDefinitionNPSH:
		"""No Description

		Returns:
			IPumpDefinition: 
		"""
		pass

	@property
	def Motor(self) -> IPumpDefinitionMotor:
		"""No Description

		Returns:
			IPumpDefinition: 
		"""
		pass

class IPumpDefinitionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPumpDefinitionUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPumpDefinitionUnits: 
		"""
		pass

	@property
	def PowerUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPumpDefinitionUnits: 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPumpDefinitionUnits: 
		"""
		pass

	@property
	def SpeedUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPumpDefinitionUnits: 
		"""
		pass

class IPumpDefinitionHead:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpDefinitionType(self) -> PumpDefinitionType:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@PumpDefinitionType.setter
	def PumpDefinitionType(self, pumpdefinitiontype: PumpDefinitionType) -> None:
		pass

	@property
	def ConstantPower(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@ConstantPower.setter
	def ConstantPower(self, constantpower: float) -> None:
		pass

	@property
	def DesignFlow(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@DesignFlow.setter
	def DesignFlow(self, designflow: float) -> None:
		pass

	@property
	def DesignHead(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@DesignHead.setter
	def DesignHead(self, designhead: float) -> None:
		pass

	@property
	def ShutoffHead(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@ShutoffHead.setter
	def ShutoffHead(self, shutoffhead: float) -> None:
		pass

	@property
	def MaxOperatingHead(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@MaxOperatingHead.setter
	def MaxOperatingHead(self, maxoperatinghead: float) -> None:
		pass

	@property
	def MaxOperatingFlow(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@MaxOperatingFlow.setter
	def MaxOperatingFlow(self, maxoperatingflow: float) -> None:
		pass

	@property
	def MaxExtendedFlow(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

	@MaxExtendedFlow.setter
	def MaxExtendedFlow(self, maxextendedflow: float) -> None:
		pass

	@property
	def PumpCurve(self) -> IPumpCurveCollection:
		"""No Description

		Returns:
			IPumpDefinitionHead: 
		"""
		pass

class IPumpCurveCollection(ICollectionElements[IPumpCurve, IPumpCurveElement, IPumpCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpCurve(ICollection[IPumpCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, head: float) -> IPumpCurveElement:
		"""No Description

		Args:
			flow(float): flow
			head(float): head

		Returns:
			IPumpCurveElement: 
		"""
		pass

	@overload
	def Add(self) -> IPumpCurveElement:
		"""No Description

		Returns:
			IPumpCurveElement: 
		"""
		pass

class IPumpCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IPumpCurveElement: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Head(self) -> float:
		"""No Description

		Returns:
			IPumpCurveElement: 
		"""
		pass

	@Head.setter
	def Head(self, head: float) -> None:
		pass

class IPumpCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPumpCurveUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPumpCurveUnits: 
		"""
		pass

class IPumpDefinitionEfficiency:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpEfficiencyType(self) -> PumpEfficiencyTypeEnum:
		"""No Description

		Returns:
			IPumpDefinitionEfficiency: 
		"""
		pass

	@PumpEfficiencyType.setter
	def PumpEfficiencyType(self, pumpefficiencytype: PumpEfficiencyTypeEnum) -> None:
		pass

	@property
	def BEPFlow(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionEfficiency: 
		"""
		pass

	@BEPFlow.setter
	def BEPFlow(self, bepflow: float) -> None:
		pass

	@property
	def BEPEfficiency(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionEfficiency: 
		"""
		pass

	@BEPEfficiency.setter
	def BEPEfficiency(self, bepefficiency: float) -> None:
		pass

	@property
	def DefineBEPMaximumFlow(self) -> bool:
		"""No Description

		Returns:
			IPumpDefinitionEfficiency: 
		"""
		pass

	@DefineBEPMaximumFlow.setter
	def DefineBEPMaximumFlow(self, definebepmaximumflow: bool) -> None:
		pass

	@property
	def UserDefinedBEPMaximumFlow(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionEfficiency: 
		"""
		pass

	@UserDefinedBEPMaximumFlow.setter
	def UserDefinedBEPMaximumFlow(self, userdefinedbepmaximumflow: float) -> None:
		pass

	@property
	def ConstantEfficiency(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionEfficiency: 
		"""
		pass

	@ConstantEfficiency.setter
	def ConstantEfficiency(self, constantefficiency: float) -> None:
		pass

	@property
	def FlowEfficiencyCurve(self) -> IFlowEfficiencyCollection:
		"""No Description

		Returns:
			IPumpDefinitionEfficiency: 
		"""
		pass

class IFlowEfficiencyCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IFlowEfficiencyCurveElement: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Efficiency(self) -> float:
		"""No Description

		Returns:
			IFlowEfficiencyCurveElement: 
		"""
		pass

	@Efficiency.setter
	def Efficiency(self, efficiency: float) -> None:
		pass

class IFlowEfficiencyCurve(ICollection[IFlowEfficiencyCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, efficiency: float) -> IFlowEfficiencyCurveElement:
		"""No Description

		Args:
			flow(float): flow
			efficiency(float): efficiency

		Returns:
			IFlowEfficiencyCurveElement: 
		"""
		pass

	@overload
	def Add(self) -> IFlowEfficiencyCurveElement:
		"""No Description

		Returns:
			IFlowEfficiencyCurveElement: 
		"""
		pass

class IFlowEfficiencyUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowEfficiencyUnits: 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowEfficiencyUnits: 
		"""
		pass

class IFlowEfficiencyCollection(ICollectionElements[IFlowEfficiencyCurve, IFlowEfficiencyCurveElement, IFlowEfficiencyUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinitionNPSH:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UseNPSHCurve(self) -> bool:
		"""No Description

		Returns:
			IPumpDefinitionNPSH: 
		"""
		pass

	@UseNPSHCurve.setter
	def UseNPSHCurve(self, usenpshcurve: bool) -> None:
		pass

	@property
	def NPSHCurveSafetyFactor(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionNPSH: 
		"""
		pass

	@NPSHCurveSafetyFactor.setter
	def NPSHCurveSafetyFactor(self, npshcurvesafetyfactor: float) -> None:
		pass

	@property
	def NPSHCurve(self) -> INPSHCurveCollection:
		"""No Description

		Returns:
			IPumpDefinitionNPSH: 
		"""
		pass

class IFlowNPSHr(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IFlowNPSHr: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def NPSHr(self) -> float:
		"""No Description

		Returns:
			IFlowNPSHr: 
		"""
		pass

	@NPSHr.setter
	def NPSHr(self, npshr: float) -> None:
		pass

class IFlowNPSHrCurve(ICollection[IFlowNPSHr]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, NPSHr: float) -> IFlowNPSHr:
		"""No Description

		Args:
			flow(float): flow
			NPSHr(float): NPSHr

		Returns:
			IFlowNPSHr: 
		"""
		pass

	@overload
	def Add(self) -> IFlowNPSHr:
		"""No Description

		Returns:
			IFlowNPSHr: 
		"""
		pass

class INPSHCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			INPSHCurveUnits: 
		"""
		pass

	@property
	def NPSHUnit(self) -> IUnit:
		"""No Description

		Returns:
			INPSHCurveUnits: 
		"""
		pass

class INPSHCurveCollection(ICollectionElements[IFlowNPSHrCurve, IFlowNPSHr, INPSHCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinitionMotor:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsVariableSpeedDrive(self) -> bool:
		"""No Description

		Returns:
			IPumpDefinitionMotor: 
		"""
		pass

	@IsVariableSpeedDrive.setter
	def IsVariableSpeedDrive(self, isvariablespeeddrive: bool) -> None:
		pass

	@property
	def MotorEfficiency(self) -> float:
		"""No Description

		Returns:
			IPumpDefinitionMotor: 
		"""
		pass

	@MotorEfficiency.setter
	def MotorEfficiency(self, motorefficiency: float) -> None:
		pass

	@property
	def SpeedEfficiencyCurve(self) -> ISpeedEfficiencyCurveCollection:
		"""No Description

		Returns:
			IPumpDefinitionMotor: 
		"""
		pass

class ISpeedEfficiency(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Speed(self) -> float:
		"""No Description

		Returns:
			ISpeedEfficiency: 
		"""
		pass

	@Speed.setter
	def Speed(self, speed: float) -> None:
		pass

	@property
	def Efficiency(self) -> float:
		"""No Description

		Returns:
			ISpeedEfficiency: 
		"""
		pass

	@Efficiency.setter
	def Efficiency(self, efficiency: float) -> None:
		pass

class ISpeedEfficiencyCurve(ICollection[ISpeedEfficiency]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, speed: float, efficiency: float) -> ISpeedEfficiency:
		"""No Description

		Args:
			speed(float): speed
			efficiency(float): efficiency

		Returns:
			ISpeedEfficiency: 
		"""
		pass

	@overload
	def Add(self) -> ISpeedEfficiency:
		"""No Description

		Returns:
			ISpeedEfficiency: 
		"""
		pass

class ISpeedEfficiencyUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SpeedUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpeedEfficiencyUnits: 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpeedEfficiencyUnits: 
		"""
		pass

class ISpeedEfficiencyCurveCollection(ICollectionElements[ISpeedEfficiencyCurve, ISpeedEfficiency, ISpeedEfficiencyUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IConstituent(IWaterComponentBase[IConstituents, IConstituent, IConstituentUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Diffusivity(self) -> float:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@Diffusivity.setter
	def Diffusivity(self, diffusivity: float) -> None:
		pass

	@property
	def HasUnlimitedConcentration(self) -> bool:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@HasUnlimitedConcentration.setter
	def HasUnlimitedConcentration(self, hasunlimitedconcentration: bool) -> None:
		pass

	@property
	def ConcentrationLimit(self) -> float:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@ConcentrationLimit.setter
	def ConcentrationLimit(self, concentrationlimit: float) -> None:
		pass

	@property
	def BulkReactionOrder(self) -> int:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@BulkReactionOrder.setter
	def BulkReactionOrder(self, bulkreactionorder: int) -> None:
		pass

	@property
	def BulkReactionRate(self) -> float:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@BulkReactionRate.setter
	def BulkReactionRate(self, bulkreactionrate: float) -> None:
		pass

	@property
	def IsRoughnessCorrelated(self) -> bool:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@IsRoughnessCorrelated.setter
	def IsRoughnessCorrelated(self, isroughnesscorrelated: bool) -> None:
		pass

	@property
	def RoughnessCorrelationFactor(self) -> float:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@RoughnessCorrelationFactor.setter
	def RoughnessCorrelationFactor(self, roughnesscorrelationfactor: float) -> None:
		pass

	@property
	def WallReactionOrder(self) -> WallReactionOrder:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@WallReactionOrder.setter
	def WallReactionOrder(self, wallreactionorder: WallReactionOrder) -> None:
		pass

	@property
	def ZeroOrderWallReactionRate(self) -> float:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@ZeroOrderWallReactionRate.setter
	def ZeroOrderWallReactionRate(self, zeroorderwallreactionrate: float) -> None:
		pass

	@property
	def FirstOrderWallReactionRate(self) -> float:
		"""No Description

		Returns:
			IConstituent: 
		"""
		pass

	@FirstOrderWallReactionRate.setter
	def FirstOrderWallReactionRate(self, firstorderwallreactionrate: float) -> None:
		pass

class IConstituents(IWaterComponentsBase[IConstituents, IConstituent, IConstituentUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IConstituentUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitDemandLoad(IWaterComponentBase[IUnitDemandLoads, IUnitDemandLoad, IUnitDemandLoadUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UnitDemand(self) -> float:
		"""No Description

		Returns:
			IUnitDemandLoad: 
		"""
		pass

	@UnitDemand.setter
	def UnitDemand(self, unitdemand: float) -> None:
		pass

	@property
	def UnitDemandType(self) -> UnitDemandLoadTypeEnum:
		"""No Description

		Returns:
			IUnitDemandLoad: 
		"""
		pass

	@UnitDemandType.setter
	def UnitDemandType(self, unitdemandtype: UnitDemandLoadTypeEnum) -> None:
		pass

	@property
	def PopulationUnit(self) -> PopulationUnit:
		"""No Description

		Returns:
			IUnitDemandLoad: 
		"""
		pass

	@PopulationUnit.setter
	def PopulationUnit(self, populationunit: PopulationUnit) -> None:
		pass

	@property
	def AreaUnit(self) -> AreaUnit:
		"""No Description

		Returns:
			IUnitDemandLoad: 
		"""
		pass

	@AreaUnit.setter
	def AreaUnit(self, areaunit: AreaUnit) -> None:
		pass

	@property
	def CountUnit(self) -> str:
		"""No Description

		Returns:
			IUnitDemandLoad: 
		"""
		pass

	@CountUnit.setter
	def CountUnit(self, countunit: str) -> None:
		pass

	@property
	def ReportPopulationEquivalent(self) -> bool:
		"""No Description

		Returns:
			IUnitDemandLoad: 
		"""
		pass

	@ReportPopulationEquivalent.setter
	def ReportPopulationEquivalent(self, reportpopulationequivalent: bool) -> None:
		pass

	@property
	def PopulationEquivalent(self) -> float:
		"""No Description

		Returns:
			IUnitDemandLoad: 
		"""
		pass

	@PopulationEquivalent.setter
	def PopulationEquivalent(self, populationequivalent: float) -> None:
		pass

class IUnitDemandLoads(IWaterComponentsBase[IUnitDemandLoads, IUnitDemandLoad, IUnitDemandLoadUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitDemandLoadUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISCADASignal(IWaterComponentBase[ISCADASignals, ISCADASignal, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ScadaDatasourceID(self) -> int:
		"""No Description

		Returns:
			ISCADASignal: 
		"""
		pass

	@property
	def SignalLabel(self) -> str:
		"""No Description

		Returns:
			ISCADASignal: 
		"""
		pass

	@SignalLabel.setter
	def SignalLabel(self, signallabel: str) -> None:
		pass

	@property
	def IsDerived(self) -> bool:
		"""No Description

		Returns:
			ISCADASignal: 
		"""
		pass

	@IsDerived.setter
	def IsDerived(self, isderived: bool) -> None:
		pass

	@property
	def Formula(self) -> str:
		"""No Description

		Returns:
			ISCADASignal: 
		"""
		pass

	@Formula.setter
	def Formula(self, formula: str) -> None:
		pass

	@property
	def TransformMethod(self) -> SCADASignalTransformMethod:
		"""No Description

		Returns:
			ISCADASignal: 
		"""
		pass

	@TransformMethod.setter
	def TransformMethod(self, transformmethod: SCADASignalTransformMethod) -> None:
		pass

class ISCADASignals(IWaterComponentsBase[ISCADASignals, ISCADASignal, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVHeadlossCurve(IWaterComponentBase[IGPVHeadlossCurves, IGPVHeadlossCurve, IGPVHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVHeadlossFlowCurve(self) -> IGPVFlowHeadlossCurveCollection:
		"""No Description

		Returns:
			IGPVHeadlossCurve: 
		"""
		pass

class IGPVHeadlossCurves(IWaterComponentsBase[IGPVHeadlossCurves, IGPVHeadlossCurve, IGPVHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVHeadlossUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVFlowHeadloss(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IGPVFlowHeadloss: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Headloss(self) -> float:
		"""No Description

		Returns:
			IGPVFlowHeadloss: 
		"""
		pass

	@Headloss.setter
	def Headloss(self, headloss: float) -> None:
		pass

class IGPVFlowHeadlossCurve(ICollection[IGPVFlowHeadloss]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, headloss: float) -> IGPVFlowHeadloss:
		"""No Description

		Args:
			flow(float): flow
			headloss(float): headloss

		Returns:
			IGPVFlowHeadloss: 
		"""
		pass

	@overload
	def Add(self) -> IGPVFlowHeadloss:
		"""No Description

		Returns:
			IGPVFlowHeadloss: 
		"""
		pass

class IGPVFlowHeadlossCurveCollection(ICollectionElements[IGPVFlowHeadlossCurve, IGPVFlowHeadloss, IGPVFlowHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVFlowHeadlossUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> IUnit:
		"""No Description

		Returns:
			IGPVFlowHeadlossUnits: 
		"""
		pass

	@property
	def Headloss(self) -> IUnit:
		"""No Description

		Returns:
			IGPVFlowHeadlossUnits: 
		"""
		pass

class IValveCharacteristic(IWaterComponentBase[IValveCharacteristics, IValveCharacteristic, IValveCharacteristicUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristicsCurve(self) -> IValveCharacteristicsCurveCollection:
		"""No Description

		Returns:
			IValveCharacteristic: 
		"""
		pass

class IValveCharacteristics(IWaterComponentsBase[IValveCharacteristics, IValveCharacteristic, IValveCharacteristicUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveCharacteristicUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRelativeClosureRelativeArea(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeClosure(self) -> float:
		"""No Description

		Returns:
			IRelativeClosureRelativeArea: 
		"""
		pass

	@RelativeClosure.setter
	def RelativeClosure(self, relativeclosure: float) -> None:
		pass

	@property
	def RelativeArea(self) -> float:
		"""No Description

		Returns:
			IRelativeClosureRelativeArea: 
		"""
		pass

	@RelativeArea.setter
	def RelativeArea(self, relativearea: float) -> None:
		pass

class IRelativeClosureRelativeAreas(ICollection[IRelativeClosureRelativeArea]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, relativeClosure: float, relativeArea: float) -> IRelativeClosureRelativeArea:
		"""No Description

		Args:
			relativeClosure(float): relativeClosure
			relativeArea(float): relativeArea

		Returns:
			IRelativeClosureRelativeArea: 
		"""
		pass

	@overload
	def Add(self) -> IRelativeClosureRelativeArea:
		"""No Description

		Returns:
			IRelativeClosureRelativeArea: 
		"""
		pass

class IValveCharacteristicsCurveCollection(ICollectionElements[IRelativeClosureRelativeAreas, IRelativeClosureRelativeArea, IRelativeClosureRelativeAreaUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRelativeClosureRelativeAreaUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ClosureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IRelativeClosureRelativeAreaUnits: 
		"""
		pass

	@property
	def AreaUnit(self) -> IUnit:
		"""No Description

		Returns:
			IRelativeClosureRelativeAreaUnits: 
		"""
		pass

class IMinorLossCoefficients(IWaterComponentsBase[IMinorLossCoefficients, IMinorLossCoefficient, IMinorLossCoefficientUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IMinorLossCoefficient(IWaterComponentBase[IMinorLossCoefficients, IMinorLossCoefficient, IMinorLossCoefficientUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MinorLossType(self) -> MinorLossTypeEnum:
		"""No Description

		Returns:
			IMinorLossCoefficient: 
		"""
		pass

	@MinorLossType.setter
	def MinorLossType(self, minorlosstype: MinorLossTypeEnum) -> None:
		pass

	@property
	def MinorLoss(self) -> float:
		"""No Description

		Returns:
			IMinorLossCoefficient: 
		"""
		pass

	@MinorLoss.setter
	def MinorLoss(self, minorloss: float) -> None:
		pass

class IMinorLossCoefficientUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IMinorLossCoefficientUnits: 
		"""
		pass

class IWaterModelSupport(IModelComponents[IWaterComponent, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SCADASignals(self, dataSourceID: int) -> ISCADASignals:
		"""No Description

		Args:
			dataSourceID(int): dataSourceID

		Returns:
			ISCADASignals: 
		"""
		pass

	@property
	def Zones(self) -> IZones:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def Patterns(self) -> IPatterns:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def PumpDefinitions(self) -> IPumpDefinitions:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def Constituents(self) -> IConstituents:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def UnitDemandLoads(self) -> IUnitDemandLoads:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def Controls(self) -> IControls:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def ControlConditions(self) -> IControlConditions:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def ControlActions(self) -> IControlActions:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def AirFlowCurves(self) -> IAirFlowCurves:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def GPVHeadlossCurves(self) -> IGPVHeadlossCurves:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristics:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

	@property
	def MinorLossCoefficients(self) -> IMinorLossCoefficients:
		"""No Description

		Returns:
			IWaterModelSupport: 
		"""
		pass

