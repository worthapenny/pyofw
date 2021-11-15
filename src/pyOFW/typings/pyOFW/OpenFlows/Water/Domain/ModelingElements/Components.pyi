from OpenFlows.Domain.ModelingElements.Collections import ICollectionElements, ICollection, ICollectionElement
from typing import overload, Generic, Iterator
from OpenFlows.Units import IUnit
from OpenFlows.Domain.ModelingElements import IElementUnits, IElement, TElementManagerType, TElementType, TUnitsType, IModelingElementBase, IModelingElementsBase, IElements, IElementManager
from enum import Enum
from System import TypeCode
from Haestad.Domain.ModelingObjects.Water.Enumerations import ControlTypeEnum, ControlPriorityEnum, ConditionTypeEnum, NodeAttributeEnum, TankAttributeEnum, ControlConditionPressureValveAttributeEnum, ControlConditionFCVAttributeEnum, FCVStatusEnum, ControlConditionGPVAttributeEnum, ControlConditionGPVStatusEnum, ControlConditionTCVAttributeEnum, TCVStatusEnum, HydroTankAttributeEnum, SurgeTankAttributeEnum, LogicalOperatorEnum, ControlActionTypeEnum, PumpEfficiencyTypeEnum, UnitDemandLoadTypeEnum, MinorLossTypeEnum
from Haestad.Calculations.Pressure import SimpleConditionType, ControlConditionPumpAttribute, ControlConditionPipeAttribute, ControlConditionValveStatus, ControlActionPipeAttribute, ControlActionPipeStatus, ControlActionPumpAttribute, ControlActionPumpStatus, ControlActionTCVAttribute, ControlActionTCVStatus, ControlActionGPVAttribute, ControlActionGPVStatus, ControlActionFCVAttribute, ControlActionFCVStatus, ControlActionPressureValveAttribute, ControlActionPressureValveStatus, PatternCategory, PatternFormat, PumpDefinitionType, WallReactionOrder
from datetime import datetime
from OpenFlows.Domain.ModelingElements.Components import IComponentElements, IComponentElement, IModelComponents
from Haestad.Support.Units import PopulationUnit, AreaUnit
from Haestad.Support.Support import IEditLabeled, ILabeled
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


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirFlowPressures(ICollection[IAirFlowPressure]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, pressure: float) -> IAirFlowPressure:
		"""Adds a new row to the collection with the provided flow and pressure values.

		Args
		--------
			flow (``float``) :  flow
			pressure (``float``) :  pressure

		Returns
		--------
			``IAirFlowPressure`` : 
		"""
		pass

	@overload
	def Add(self) -> IAirFlowPressure:
		"""No Description

		Returns
		--------
			``IAirFlowPressure`` : 
		"""
		pass

class IAirFlowPressure(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns
		--------
			``IAirFlowPressure`` : 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""No Description

		Returns
		--------
			``IAirFlowPressure`` : 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class IAirFlowPressureUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""Unit information for flow

		Returns
		--------
			``IAirFlowPressureUnits`` : 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""Unit information for pressure

		Returns
		--------
			``IAirFlowPressureUnits`` : 
		"""
		pass

class IAirFlowCurve(IWaterComponentBase[IAirFlowCurves, IAirFlowCurve, IAirFlowCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AirFlowPressureCollection(self) -> IAirFlowPressureCollection:
		"""No Description

		Returns
		--------
			``IAirFlowCurve`` : 
		"""
		pass

class IAirFlowCurves(IWaterComponentsBase[IAirFlowCurves, IAirFlowCurve, IAirFlowCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirFlowCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControl(IWaterComponentBase[IControls, IControl, IElementUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ControlType(self) -> ControlTypeEnum:
		"""Defines the type of control - Logical or Simple.  Logical allows for use of an Else action.

		Returns
		--------
			``IControl`` : 
		"""
		pass

	@ControlType.setter
	def ControlType(self, controltype: ControlTypeEnum) -> None:
		pass

	@property
	def Condition(self) -> IControlCondition:
		"""A condition on which to act when this control is used.

		Returns
		--------
			``IControl`` : 
		"""
		pass

	@Condition.setter
	def Condition(self, condition: IControlCondition) -> None:
		pass

	@property
	def Action(self) -> IControlAction:
		"""The action to execute when the condition is filled.

		Returns
		--------
			``IControl`` : 
		"""
		pass

	@Action.setter
	def Action(self, action: IControlAction) -> None:
		pass

	@property
	def LogicalControl(self) -> ILogicalControl:
		"""Logical control properties

		Returns
		--------
			``IControl`` : 
		"""
		pass

	@property
	def DefineDescription(self) -> bool:
		"""Determines whether the control description is automatically generated or user defined.

		Returns
		--------
			``IControl`` : 
		"""
		pass

	@DefineDescription.setter
	def DefineDescription(self, definedescription: bool) -> None:
		pass

	@property
	def Description(self) -> str:
		"""The description of the control.  If not user defined, returns Summary.

		Returns
		--------
			``IControl`` : 
		"""
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

	@property
	def Summary(self) -> str:
		"""The control statement in a readable format.

		Returns
		--------
			``IControl`` : 
		"""
		pass

class ILogicalControl:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsLogicalControl(self) -> bool:
		"""Determines if the current control is a logical control.

		Returns
		--------
			``ILogicalControl`` : 
		"""
		pass

	@property
	def HasPriority(self) -> bool:
		"""If set to true, can set a custom priority.

		Returns
		--------
			``ILogicalControl`` : 
		"""
		pass

	@HasPriority.setter
	def HasPriority(self, haspriority: bool) -> None:
		pass

	@property
	def Priority(self) -> ControlPriorityEnum:
		"""The priority of the control.

		Returns
		--------
			``ILogicalControl`` : 
		"""
		pass

	@Priority.setter
	def Priority(self, priority: ControlPriorityEnum) -> None:
		pass

	@property
	def HasElse(self) -> bool:
		"""Set to true to use an else action

		Returns
		--------
			``ILogicalControl`` : 
		"""
		pass

	@HasElse.setter
	def HasElse(self, haselse: bool) -> None:
		pass

	@property
	def ElseAction(self) -> IControlAction:
		"""If a logical control and condition resolves to false, executes this action.

		Returns
		--------
			``ILogicalControl`` : 
		"""
		pass

	@ElseAction.setter
	def ElseAction(self, elseaction: IControlAction) -> None:
		pass

class IControls(IWaterComponentsBase[IControls, IControl, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlCondition(IWaterComponentBase[IControlConditions, IControlCondition, IControlConditionUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ConditionType(self) -> ConditionTypeEnum:
		"""The type of condition - simple or composite

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@ConditionType.setter
	def ConditionType(self, conditiontype: ConditionTypeEnum) -> None:
		pass

	@property
	def SimpleConditionType(self) -> SimpleConditionType:
		"""The type of simple condition to define.

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@SimpleConditionType.setter
	def SimpleConditionType(self, simpleconditiontype: SimpleConditionType) -> None:
		pass

	@property
	def ElementCondition(self) -> IElementControlConditionInput:
		"""Element-based condition

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@property
	def SystemDemandCondition(self) -> ISystemDemandConditionInput:
		"""System demand based condition

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@property
	def ClockTimeCondition(self) -> IClockTimeConditionInput:
		"""Clock time based condition

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@property
	def TimeFromStartCondition(self) -> ITimeFromStartConditionInput:
		"""Time from start based condition

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@property
	def CompositeConditionCollection(self) -> ICompositeConditionCollection:
		"""The list of conditions making up a composite condition.

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@property
	def IsUserDefinedDescriptionFormat(self) -> bool:
		"""Determines whether the condition description is automatically generated or user defined.

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@IsUserDefinedDescriptionFormat.setter
	def IsUserDefinedDescriptionFormat(self, isuserdefineddescriptionformat: bool) -> None:
		pass

	@property
	def Description(self) -> str:
		"""The description of the condition.  If not user defined, returns Summary.

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

	@property
	def Summary(self) -> str:
		"""The condition statement in a readable format.

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

class IControlSimpleConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SimpleConditionType(self) -> SimpleConditionType:
		"""The type of simple condition to define.

		Returns
		--------
			``IControlSimpleConditionInput`` : 
		"""
		pass

	@property
	def Comparison(self) -> ConditionComparisonOperator:
		"""Defines how the condition is compared to return true.

		Returns
		--------
			``IControlSimpleConditionInput`` : 
		"""
		pass

	@Comparison.setter
	def Comparison(self, comparison: ConditionComparisonOperator) -> None:
		pass

class IElementControlConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsElementCondition(self) -> bool:
		"""True if the ConditionType is set to Element.

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def Element(self) -> IWaterElement:
		"""The element to associate with this condition.

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@Element.setter
	def Element(self, element: IWaterElement) -> None:
		pass

	@property
	def Node(self) -> INodeConditionInput:
		"""The node condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def Tank(self) -> ITankConditionInput:
		"""The tank condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def Pump(self) -> IPumpConditionInput:
		"""The pump condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def Pipe(self) -> IPipeConditionInput:
		"""The pipe condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def PressureValve(self) -> IPressureValveConditionInput:
		"""The pressure valve condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def FCV(self) -> IFlowControLValveConditionInput:
		"""The FCV condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveConditionInput:
		"""The GPV condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveConditionInput:
		"""The TCV condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def HydroTank(self) -> IHydroTankConditionInput:
		"""The hydro-tank condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

	@property
	def SurgeTank(self) -> ISurgeTankConditionInput:
		"""The surge tank condition settings

		Returns
		--------
			``IElementControlConditionInput`` : 
		"""
		pass

class IElementConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Element(self) -> IWaterElement:
		"""The element assigned to the condition.

		Returns
		--------
			``IElementConditionInput`` : 
		"""
		pass

class INodeConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def NodeAttribute(self) -> NodeAttributeEnum:
		"""The node attribute for this condition.

		Returns
		--------
			``INodeConditionInput`` : 
		"""
		pass

	@NodeAttribute.setter
	def NodeAttribute(self, nodeattribute: NodeAttributeEnum) -> None:
		pass

	@property
	def Demand(self) -> float:
		"""Demand

		Returns
		--------
			``INodeConditionInput`` : 
		"""
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""Hydraulic Grade

		Returns
		--------
			``INodeConditionInput`` : 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""Pressure

		Returns
		--------
			``INodeConditionInput`` : 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ITankConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TankAttribute(self) -> TankAttributeEnum:
		"""The tank attribute for this condition.

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@TankAttribute.setter
	def TankAttribute(self, tankattribute: TankAttributeEnum) -> None:
		pass

	@property
	def Demand(self) -> float:
		"""Demand

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""Hydraulic Grade

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""Pressure

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

	@property
	def Level(self) -> float:
		"""Tank Level

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@Level.setter
	def Level(self, level: float) -> None:
		pass

	@property
	def TimeToDrain(self) -> float:
		"""Time to drain

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@TimeToDrain.setter
	def TimeToDrain(self, timetodrain: float) -> None:
		pass

	@property
	def TimeToFill(self) -> float:
		"""Time to fill

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@TimeToFill.setter
	def TimeToFill(self, timetofill: float) -> None:
		pass

	@property
	def PercentFull(self) -> float:
		"""Percent full.

		Returns
		--------
			``ITankConditionInput`` : 
		"""
		pass

	@PercentFull.setter
	def PercentFull(self, percentfull: float) -> None:
		pass

class IPumpConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpAttribute(self) -> ControlConditionPumpAttribute:
		"""The pump attribute for this condition.

		Returns
		--------
			``IPumpConditionInput`` : 
		"""
		pass

	@PumpAttribute.setter
	def PumpAttribute(self, pumpattribute: ControlConditionPumpAttribute) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""Discharge

		Returns
		--------
			``IPumpConditionInput`` : 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def PumpSetting(self) -> float:
		"""Relative Speed Factor

		Returns
		--------
			``IPumpConditionInput`` : 
		"""
		pass

	@PumpSetting.setter
	def PumpSetting(self, pumpsetting: float) -> None:
		pass

	@property
	def PumpStatus(self) -> PumpStatus:
		"""Pump status

		Returns
		--------
			``IPumpConditionInput`` : 
		"""
		pass

	@PumpStatus.setter
	def PumpStatus(self, pumpstatus: PumpStatus) -> None:
		pass

class IPipeConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PipeAttribute(self) -> ControlConditionPipeAttribute:
		"""The pipe attribute for this condition

		Returns
		--------
			``IPipeConditionInput`` : 
		"""
		pass

	@PipeAttribute.setter
	def PipeAttribute(self, pipeattribute: ControlConditionPipeAttribute) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""Discharge

		Returns
		--------
			``IPipeConditionInput`` : 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def PipeStatus(self) -> PipeStatus:
		"""Pipe status

		Returns
		--------
			``IPipeConditionInput`` : 
		"""
		pass

	@PipeStatus.setter
	def PipeStatus(self, pipestatus: PipeStatus) -> None:
		pass

class IPressureValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureValveAttribute(self) -> ControlConditionPressureValveAttributeEnum:
		"""The pressure valve attribute for this condition

		Returns
		--------
			``IPressureValveConditionInput`` : 
		"""
		pass

	@PressureValveAttribute.setter
	def PressureValveAttribute(self, pressurevalveattribute: ControlConditionPressureValveAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""Dishcarge

		Returns
		--------
			``IPressureValveConditionInput`` : 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""Headloss coefficient

		Returns
		--------
			``IPressureValveConditionInput`` : 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@property
	def ValveStatus(self) -> ControlConditionValveStatus:
		"""Valve status

		Returns
		--------
			``IPressureValveConditionInput`` : 
		"""
		pass

	@ValveStatus.setter
	def ValveStatus(self, valvestatus: ControlConditionValveStatus) -> None:
		pass

class IFlowControLValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FCVAttribute(self) -> ControlConditionFCVAttributeEnum:
		"""The FCV attribute for this condition.

		Returns
		--------
			``IFlowControLValveConditionInput`` : 
		"""
		pass

	@FCVAttribute.setter
	def FCVAttribute(self, fcvattribute: ControlConditionFCVAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""Discharge

		Returns
		--------
			``IFlowControLValveConditionInput`` : 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""Headloss coefficient

		Returns
		--------
			``IFlowControLValveConditionInput`` : 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@property
	def FCVStatus(self) -> FCVStatusEnum:
		"""FCV status

		Returns
		--------
			``IFlowControLValveConditionInput`` : 
		"""
		pass

	@FCVStatus.setter
	def FCVStatus(self, fcvstatus: FCVStatusEnum) -> None:
		pass

class IGeneralPurposeValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVAttribute(self) -> ControlConditionGPVAttributeEnum:
		"""GPV attribute for this condition.

		Returns
		--------
			``IGeneralPurposeValveConditionInput`` : 
		"""
		pass

	@GPVAttribute.setter
	def GPVAttribute(self, gpvattribute: ControlConditionGPVAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""Discharge

		Returns
		--------
			``IGeneralPurposeValveConditionInput`` : 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def GPVStatus(self) -> ControlConditionGPVStatusEnum:
		"""GPV status

		Returns
		--------
			``IGeneralPurposeValveConditionInput`` : 
		"""
		pass

	@GPVStatus.setter
	def GPVStatus(self, gpvstatus: ControlConditionGPVStatusEnum) -> None:
		pass

class IThrottleControlValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TCVAttribute(self) -> ControlConditionTCVAttributeEnum:
		"""The TCV attribute for this condition.

		Returns
		--------
			``IThrottleControlValveConditionInput`` : 
		"""
		pass

	@TCVAttribute.setter
	def TCVAttribute(self, tcvattribute: ControlConditionTCVAttributeEnum) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""Discharge

		Returns
		--------
			``IThrottleControlValveConditionInput`` : 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""Setting

		Returns
		--------
			``IThrottleControlValveConditionInput`` : 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@property
	def TCVStatus(self) -> TCVStatusEnum:
		"""TCV status

		Returns
		--------
			``IThrottleControlValveConditionInput`` : 
		"""
		pass

	@TCVStatus.setter
	def TCVStatus(self, tcvstatus: TCVStatusEnum) -> None:
		pass

class IHydroTankConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def HydroTankAttribute(self) -> HydroTankAttributeEnum:
		"""The HydroTank attribute for this condition.

		Returns
		--------
			``IHydroTankConditionInput`` : 
		"""
		pass

	@HydroTankAttribute.setter
	def HydroTankAttribute(self, hydrotankattribute: HydroTankAttributeEnum) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""Hydraulic Grade

		Returns
		--------
			``IHydroTankConditionInput`` : 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""Pressure

		Returns
		--------
			``IHydroTankConditionInput`` : 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ISurgeTankConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SurgeTankAttribute(self) -> SurgeTankAttributeEnum:
		"""The surge tank attribute for this condition.

		Returns
		--------
			``ISurgeTankConditionInput`` : 
		"""
		pass

	@SurgeTankAttribute.setter
	def SurgeTankAttribute(self, surgetankattribute: SurgeTankAttributeEnum) -> None:
		pass

	@property
	def Demand(self) -> float:
		"""Demand

		Returns
		--------
			``ISurgeTankConditionInput`` : 
		"""
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""Hydraulic Grade

		Returns
		--------
			``ISurgeTankConditionInput`` : 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""Pressure

		Returns
		--------
			``ISurgeTankConditionInput`` : 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ISystemDemandConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsSystemDemandCondition(self) -> bool:
		"""True if the ConditionType is set to system demand

		Returns
		--------
			``ISystemDemandConditionInput`` : 
		"""
		pass

	@property
	def SystemDemand(self) -> float:
		"""The system demand to compare against to trigger the condition

		Returns
		--------
			``ISystemDemandConditionInput`` : 
		"""
		pass

	@SystemDemand.setter
	def SystemDemand(self, systemdemand: float) -> None:
		pass

class IClockTimeConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsClockTimeCondition(self) -> bool:
		"""True if the ConditionType is set to clock time.

		Returns
		--------
			``IClockTimeConditionInput`` : 
		"""
		pass

	@property
	def ClockTime(self) -> datetime:
		"""The clock time to use to trigger the condition

		Returns
		--------
			``IClockTimeConditionInput`` : 
		"""
		pass

	@ClockTime.setter
	def ClockTime(self, clocktime: datetime) -> None:
		pass

class ITimeFromStartConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsTimeFromStartCondition(self) -> bool:
		"""True if the ConditionType is set to time from start

		Returns
		--------
			``ITimeFromStartConditionInput`` : 
		"""
		pass

	@property
	def TimeFromStart(self) -> float:
		"""The time from start to trigger the condition.

		Returns
		--------
			``ITimeFromStartConditionInput`` : 
		"""
		pass

	@TimeFromStart.setter
	def TimeFromStart(self, timefromstart: float) -> None:
		pass

class IControlConditions(IWaterComponentsBase[IControlConditions, IControlCondition, IControlConditionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlConditionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandUnit(self) -> IUnit:
		"""Formatter for demand attribute

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""Formatter for HGL

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""Formatter for pressure

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def LevelUnit(self) -> IUnit:
		"""Formatter for tank level

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def TimeToFillUnit(self) -> IUnit:
		"""Formatter for tank time to fill

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def TimeToDrainUnit(self) -> IUnit:
		"""Formatter for tank time to drain

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def PercentFullUnit(self) -> IUnit:
		"""Formatter for tank percent full

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""Formatter for discharge

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def HeadlossCoefficientUnit(self) -> IUnit:
		"""Formatter for headloss coefficient

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

	@property
	def TimeFromStartUnit(self) -> IUnit:
		"""Formatter for time from start

		Returns
		--------
			``IControlConditionUnits`` : 
		"""
		pass

class ICompositeCondition(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LogicalOperator(self) -> LogicalOperatorEnum:
		"""If the first row of the composite conditions collection, always returns If.
            If not the first row, then use AND or OR.

		Returns
		--------
			``ICompositeCondition`` : 
		"""
		pass

	@LogicalOperator.setter
	def LogicalOperator(self, logicaloperator: LogicalOperatorEnum) -> None:
		pass

	@property
	def Condition(self) -> IControlCondition:
		"""The condition for this row.

		Returns
		--------
			``ICompositeCondition`` : 
		"""
		pass

	@Condition.setter
	def Condition(self, condition: IControlCondition) -> None:
		pass

class ICompositeConditions(ICollection[ICompositeCondition]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, logicalOperator: LogicalOperatorEnum, condition: IControlCondition) -> ICompositeCondition:
		"""Adds a condition to the collection

		Args
		--------
			logicalOperator (``LogicalOperatorEnum``) :  If the first row, can be IF.  Otherwise, must be AND or OR.
			condition (``IControlCondition``) :  The condition to use for the row.

		Returns
		--------
			``ICompositeCondition`` : The composite condition created with the assigned parameters.
		"""
		pass

	@overload
	def Add(self) -> ICompositeCondition:
		"""No Description

		Returns
		--------
			``ICompositeCondition`` : 
		"""
		pass

class ICompositeConditionCollection(ICollectionElements[ICompositeConditions, ICompositeCondition, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlAction(IWaterComponentBase[IControlActions, IControlAction, IControlActionUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ActionType(self) -> ControlActionTypeEnum:
		"""The type of action - simple or composite

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@ActionType.setter
	def ActionType(self, actiontype: ControlActionTypeEnum) -> None:
		pass

	@property
	def Element(self) -> IWaterElement:
		"""The element assigned to the action.

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@Element.setter
	def Element(self, element: IWaterElement) -> None:
		pass

	@property
	def Pipe(self) -> IPipeActionInput:
		"""The pipe action properties

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@property
	def Pump(self) -> IPumpActionInput:
		"""The pump action properties

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveActionInput:
		"""The TCV action properties

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveActionInput:
		"""The GPV action properties

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@property
	def FCV(self) -> IFlowControlValveActionInput:
		"""The FCV action properties

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@property
	def PressureValve(self) -> IPressureValveActionInput:
		"""The pressure valve action properties

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@property
	def CompositeActionCollection(self) -> ICompositeActionCollection:
		"""The list of actions making up a composite action.

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@property
	def DefineDescription(self) -> bool:
		"""Determines whether the action description is automatically generated or user defined.

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@DefineDescription.setter
	def DefineDescription(self, definedescription: bool) -> None:
		pass

	@property
	def Description(self) -> str:
		"""The description of the action.  If not user defined, returns Summary.

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

	@property
	def Summary(self) -> str:
		"""The action statement in a readable format.

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

class IElementActionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Element(self) -> IWaterElement:
		"""The assigned element for the action

		Returns
		--------
			``IElementActionInput`` : 
		"""
		pass

class IPipeActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPipeAction(self) -> bool:
		"""True if a pipe is assigned as the action element

		Returns
		--------
			``IPipeActionInput`` : 
		"""
		pass

	@property
	def PipeAttribute(self) -> ControlActionPipeAttribute:
		"""The pipe attribute to use for the action

		Returns
		--------
			``IPipeActionInput`` : 
		"""
		pass

	@PipeAttribute.setter
	def PipeAttribute(self, pipeattribute: ControlActionPipeAttribute) -> None:
		pass

	@property
	def PipeStatus(self) -> ControlActionPipeStatus:
		"""The pipe status to set.

		Returns
		--------
			``IPipeActionInput`` : 
		"""
		pass

	@PipeStatus.setter
	def PipeStatus(self, pipestatus: ControlActionPipeStatus) -> None:
		pass

class IPumpActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPumpAction(self) -> bool:
		"""True if a pump is assigned as the action element

		Returns
		--------
			``IPumpActionInput`` : 
		"""
		pass

	@property
	def PumpAttribute(self) -> ControlActionPumpAttribute:
		"""the pump attribute to use for the action

		Returns
		--------
			``IPumpActionInput`` : 
		"""
		pass

	@PumpAttribute.setter
	def PumpAttribute(self, pumpattribute: ControlActionPumpAttribute) -> None:
		pass

	@property
	def PumpStatus(self) -> ControlActionPumpStatus:
		"""The pump status to use

		Returns
		--------
			``IPumpActionInput`` : 
		"""
		pass

	@PumpStatus.setter
	def PumpStatus(self, pumpstatus: ControlActionPumpStatus) -> None:
		pass

	@property
	def RelativeSpeedFactor(self) -> float:
		"""The relative speed factor to use.

		Returns
		--------
			``IPumpActionInput`` : 
		"""
		pass

	@RelativeSpeedFactor.setter
	def RelativeSpeedFactor(self, relativespeedfactor: float) -> None:
		pass

	@property
	def TargetPressure(self) -> float:
		"""The target pressure to set.

		Returns
		--------
			``IPumpActionInput`` : 
		"""
		pass

	@TargetPressure.setter
	def TargetPressure(self, targetpressure: float) -> None:
		pass

	@property
	def TargetHead(self) -> float:
		"""the target head to set.

		Returns
		--------
			``IPumpActionInput`` : 
		"""
		pass

	@TargetHead.setter
	def TargetHead(self, targethead: float) -> None:
		pass

class IThrottleControlValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsTCVAction(self) -> bool:
		"""True if a TCV is assigned as the action element.

		Returns
		--------
			``IThrottleControlValveActionInput`` : 
		"""
		pass

	@property
	def TCVAttribute(self) -> ControlActionTCVAttribute:
		"""The TCV attribute to use for this action

		Returns
		--------
			``IThrottleControlValveActionInput`` : 
		"""
		pass

	@TCVAttribute.setter
	def TCVAttribute(self, tcvattribute: ControlActionTCVAttribute) -> None:
		pass

	@property
	def TCVStatus(self) -> ControlActionTCVStatus:
		"""The TCV status to use

		Returns
		--------
			``IThrottleControlValveActionInput`` : 
		"""
		pass

	@TCVStatus.setter
	def TCVStatus(self, tcvstatus: ControlActionTCVStatus) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""The headloss coefficient to use.

		Returns
		--------
			``IThrottleControlValveActionInput`` : 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

class IGeneralPurposeValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsGPVAction(self) -> bool:
		"""True if a GPV is assigned as the action element.

		Returns
		--------
			``IGeneralPurposeValveActionInput`` : 
		"""
		pass

	@property
	def GPVAttribute(self) -> ControlActionGPVAttribute:
		"""The GPV attribute to use.

		Returns
		--------
			``IGeneralPurposeValveActionInput`` : 
		"""
		pass

	@GPVAttribute.setter
	def GPVAttribute(self, gpvattribute: ControlActionGPVAttribute) -> None:
		pass

	@property
	def GPVStatus(self) -> ControlActionGPVStatus:
		"""The GPV status.

		Returns
		--------
			``IGeneralPurposeValveActionInput`` : 
		"""
		pass

	@GPVStatus.setter
	def GPVStatus(self, gpvstatus: ControlActionGPVStatus) -> None:
		pass

class IFlowControlValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsFCVAction(self) -> bool:
		"""True if an FCV is assigned as the action element

		Returns
		--------
			``IFlowControlValveActionInput`` : 
		"""
		pass

	@property
	def FCVAttribute(self) -> ControlActionFCVAttribute:
		"""The FCv attribute to use.

		Returns
		--------
			``IFlowControlValveActionInput`` : 
		"""
		pass

	@FCVAttribute.setter
	def FCVAttribute(self, fcvattribute: ControlActionFCVAttribute) -> None:
		pass

	@property
	def Discharge(self) -> float:
		"""The discharge to use

		Returns
		--------
			``IFlowControlValveActionInput`` : 
		"""
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@property
	def FCVStatus(self) -> ControlActionFCVStatus:
		"""The FCV status to use.

		Returns
		--------
			``IFlowControlValveActionInput`` : 
		"""
		pass

	@FCVStatus.setter
	def FCVStatus(self, fcvstatus: ControlActionFCVStatus) -> None:
		pass

class IPressureValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPressureValveAction(self) -> bool:
		"""True if a PRV, PBV or PSV is assigned as the action element.

		Returns
		--------
			``IPressureValveActionInput`` : 
		"""
		pass

	@property
	def PressureValveAttribute(self) -> ControlActionPressureValveAttribute:
		"""the pressure valve attribue to use.

		Returns
		--------
			``IPressureValveActionInput`` : 
		"""
		pass

	@PressureValveAttribute.setter
	def PressureValveAttribute(self, pressurevalveattribute: ControlActionPressureValveAttribute) -> None:
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""The hGL to set.

		Returns
		--------
			``IPressureValveActionInput`` : 
		"""
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@property
	def Pressure(self) -> float:
		"""The pressure to set.

		Returns
		--------
			``IPressureValveActionInput`` : 
		"""
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

	@property
	def PressureValveStatus(self) -> ControlActionPressureValveStatus:
		"""The status to set.

		Returns
		--------
			``IPressureValveActionInput`` : 
		"""
		pass

	@PressureValveStatus.setter
	def PressureValveStatus(self, pressurevalvestatus: ControlActionPressureValveStatus) -> None:
		pass

class IControlActions(IWaterComponentsBase[IControlActions, IControlAction, IControlActionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlActionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeSpeedFactorUnit(self) -> IUnit:
		"""Formatter for relative speed factor

		Returns
		--------
			``IControlActionUnits`` : 
		"""
		pass

	@property
	def TargetPressureUnit(self) -> IUnit:
		"""Formatter for target pressure

		Returns
		--------
			``IControlActionUnits`` : 
		"""
		pass

	@property
	def TargetHeadUnit(self) -> IUnit:
		"""Formatter for target head

		Returns
		--------
			``IControlActionUnits`` : 
		"""
		pass

	@property
	def HeadlossCoefficientUnit(self) -> IUnit:
		"""Formatter for headloss coefficient

		Returns
		--------
			``IControlActionUnits`` : 
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""Formatter for discharge

		Returns
		--------
			``IControlActionUnits`` : 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""Formatter for hydraulic grade

		Returns
		--------
			``IControlActionUnits`` : 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""Formatter for pressure

		Returns
		--------
			``IControlActionUnits`` : 
		"""
		pass

class ICompositeAction(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Action(self) -> IControlAction:
		"""The action for this row.

		Returns
		--------
			``ICompositeAction`` : 
		"""
		pass

	@Action.setter
	def Action(self, action: IControlAction) -> None:
		pass

class ICompositeActions(ICollection[ICompositeAction]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, action: IControlAction) -> ICompositeAction:
		"""Adds an action to the composite action collection.

		Args
		--------
			action (``IControlAction``) :  The action to add.

		Returns
		--------
			``ICompositeAction`` : Represents the new row added to the collection
		"""
		pass

	@overload
	def Add(self) -> ICompositeAction:
		"""No Description

		Returns
		--------
			``ICompositeAction`` : 
		"""
		pass

class ICompositeActionCollection(ICollectionElements[ICompositeActions, ICompositeAction, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ControlExtensionMethods:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pipe: IPipe, attribute: ControlActionPipeAttribute, status: ControlActionPipeStatus) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			pipe (``IPipe``) :  pipe
			attribute (``ControlActionPipeAttribute``) :  attribute
			status (``ControlActionPipeStatus``) :  status

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pump: IPump, attribute: PumpAttribute, value: float) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			pump (``IPump``) :  pump
			attribute (``PumpAttribute``) :  attribute
			value (``float``) :  value

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pump: IPump, status: ControlActionPumpStatus) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			pump (``IPump``) :  pump
			status (``ControlActionPumpStatus``) :  status

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, tcv: IThrottleControlValve, status: ControlActionTCVStatus) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			tcv (``IThrottleControlValve``) :  tcv
			status (``ControlActionTCVStatus``) :  status

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, tcv: IThrottleControlValve, value: float) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			tcv (``IThrottleControlValve``) :  tcv
			value (``float``) :  value

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, gpv: IGeneralPurposeValve, status: ControlActionGPVStatus) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			gpv (``IGeneralPurposeValve``) :  gpv
			status (``ControlActionGPVStatus``) :  status

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, fcv: IFlowControlValve, status: ControlActionFCVStatus) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			fcv (``IFlowControlValve``) :  fcv
			status (``ControlActionFCVStatus``) :  status

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, psv: IPressureSustainingValve, attribute: PressureValveAttribute, value: float) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			psv (``IPressureSustainingValve``) :  psv
			attribute (``PressureValveAttribute``) :  attribute
			value (``float``) :  value

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pbv: IPressureBreakingValve, attribute: PressureValveAttribute, value: float) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			pbv (``IPressureBreakingValve``) :  pbv
			attribute (``PressureValveAttribute``) :  attribute
			value (``float``) :  value

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, prv: IPressureReducingValve, attribute: PressureValveAttribute, value: float) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			prv (``IPressureReducingValve``) :  prv
			attribute (``PressureValveAttribute``) :  attribute
			value (``float``) :  value

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, pbv: IPressureBreakingValve, status: ControlActionPressureValveStatus) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			pbv (``IPressureBreakingValve``) :  pbv
			status (``ControlActionPressureValveStatus``) :  status

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateAction(actions: IControlActions, prv: IPressureReducingValve, status: ControlActionPressureValveStatus) -> IControlAction:
		"""No Description

		Args
		--------
			actions (``IControlActions``) :  actions
			prv (``IPressureReducingValve``) :  prv
			status (``ControlActionPressureValveStatus``) :  status

		Returns
		--------
			``IControlAction`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, reservoir: IReservoir, attribute: NodeAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""Create a condition for a reservoir using the attribute value.

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			reservoir (``IReservoir``) :  reservoir
			attribute (``NodeAttributeEnum``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, junction: IJunction, attribute: NodeAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""Create a condition for the junction

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			junction (``IJunction``) :  junction
			attribute (``NodeAttributeEnum``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, hydrant: IHydrant, attribute: NodeAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""Create a condition for the hydrant.

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			hydrant (``IHydrant``) :  hydrant
			attribute (``NodeAttributeEnum``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, tank: ITank, attribute: TankAttributeEnum, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""Create a condition for the tank using the attribute and value.

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			tank (``ITank``) :  tank
			attribute (``TankAttributeEnum``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pump: IPump, attribute: PumpConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""Create a condition for the pump

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			pump (``IPump``) :  pump
			attribute (``PumpConditionAttribute``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pump: IPump, status: PumpStatus) -> IControlCondition:
		"""Create a condition for the pump using its status.

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			pump (``IPump``) :  pump
			status (``PumpStatus``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pipe: IPipe, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""Create a condition for the pipe

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			pipe (``IPipe``) :  pipe
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pipe: IPipe, status: PipeStatus) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			pipe (``IPipe``) :  pipe
			status (``PipeStatus``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, psv: IPressureSustainingValve, attribute: PressureValveConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""Create a condition for the psv

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			psv (``IPressureSustainingValve``) :  psv
			attribute (``PressureValveConditionAttribute``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, psv: IPressureSustainingValve, status: ControlConditionValveStatus) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			psv (``IPressureSustainingValve``) :  psv
			status (``ControlConditionValveStatus``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pbv: IPressureBreakingValve, attribute: PressureValveConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			pbv (``IPressureBreakingValve``) :  pbv
			attribute (``PressureValveConditionAttribute``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, pbv: IPressureBreakingValve, status: ControlConditionValveStatus) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			pbv (``IPressureBreakingValve``) :  pbv
			status (``ControlConditionValveStatus``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, prv: IPressureReducingValve, attribute: PressureValveConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			prv (``IPressureReducingValve``) :  prv
			attribute (``PressureValveConditionAttribute``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, prv: IPressureReducingValve, status: ControlConditionValveStatus) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			prv (``IPressureReducingValve``) :  prv
			status (``ControlConditionValveStatus``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, fcv: IFlowControlValve, attribute: FCVConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			fcv (``IFlowControlValve``) :  fcv
			attribute (``FCVConditionAttribute``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, fcv: IFlowControlValve, status: FCVStatusEnum) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			fcv (``IFlowControlValve``) :  fcv
			status (``FCVStatusEnum``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, gpv: IGeneralPurposeValve, status: ControlConditionGPVStatusEnum) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			gpv (``IGeneralPurposeValve``) :  gpv
			status (``ControlConditionGPVStatusEnum``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, gpv: IGeneralPurposeValve, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			gpv (``IGeneralPurposeValve``) :  gpv
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, tcv: IThrottleControlValve, attribute: TCVConditionAttribute, op: ConditionComparisonOperator, value: float) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			tcv (``IThrottleControlValve``) :  tcv
			attribute (``TCVConditionAttribute``) :  attribute
			op (``ConditionComparisonOperator``) :  op
			value (``float``) :  value

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	@overload
	def CreateCondition(conditions: IControlConditions, tcv: IThrottleControlValve, status: TCVStatusEnum) -> IControlCondition:
		"""No Description

		Args
		--------
			conditions (``IControlConditions``) :  conditions
			tcv (``IThrottleControlValve``) :  tcv
			status (``TCVStatusEnum``) :  status

		Returns
		--------
			``IControlCondition`` : 
		"""
		pass

	@staticmethod
	def CreateControl(controls: IControls, controlStatement: str) -> IControl:
		"""Creates a logical control using a readable string

		Args
		--------
			controls (``IControls``) :  The controls manager
			controlStatement (``str``) :  The string in a readable format representing the logical control to create.

		Returns
		--------
			``IControl`` : If the control statement is in the appropriate format, a non-null control.  Otherwise, null.
		"""
		pass

class SCADASignalExtensions:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	def CreateFormulaSignal(scadaSignals: ISCADASignals, label: str, signalLabel: str, formula: str) -> ISCADASignal:
		"""Creates a new derived SCADA signal based on a formula.

		Args
		--------
			scadaSignals (``ISCADASignals``) :  The SCADA signals manager for a specific data source
			label (``str``) :  The label of the new derived signal
			signalLabel (``str``) :  The label of the signal in the data source.
			formula (``str``) :  The formula to use for the derived signal

		Returns
		--------
			``ISCADASignal`` : 
		"""
		pass

	@staticmethod
	def CreateSignal(scadaSignals: ISCADASignals, label: str, signalLabel: str) -> ISCADASignal:
		"""Creates a new SCADA signal.

		Args
		--------
			scadaSignals (``ISCADASignals``) :  The SCADA signals manager for a specific data source
			label (``str``) :  The custom label of the signal.
			signalLabel (``str``) :  The label of the signal in the data source.

		Returns
		--------
			``ISCADASignal`` : A new SCADA signal
		"""
		pass

class IWaterComponent(IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElementType(self) -> WaterComponentType:
		"""The type of support element

		Returns
		--------
			``IWaterComponent`` : 
		"""
		pass

class IWaterComponentsBase(Generic[TElementManagerType, TElementType, TUnitsType], IComponentElements[TElementManagerType, TElementType, TUnitsType, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterComponentBase(Generic[TElementManagerType, TElementType, TUnitsType], IComponentElement[TElementManagerType, TElementType, TUnitsType, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IZones(IWaterComponentsBase[IZones, IZone, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IZone(IWaterComponentBase[IZones, IZone, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPattern(IWaterComponentBase[IPatterns, IPattern, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PatternCategory(self) -> PatternCategory:
		"""The type of pattern this represents

		Returns
		--------
			``IPattern`` : 
		"""
		pass

	@PatternCategory.setter
	def PatternCategory(self, patterncategory: PatternCategory) -> None:
		pass

	@property
	def PatternFormat(self) -> PatternFormat:
		"""The format of the pattern - stepwise or continuous

		Returns
		--------
			``IPattern`` : 
		"""
		pass

	@PatternFormat.setter
	def PatternFormat(self, patternformat: PatternFormat) -> None:
		pass

	@property
	def PatternStartTime(self) -> datetime:
		"""The first time step in the pattern. The start time format is a standard 24-hour clock.

		Returns
		--------
			``IPattern`` : 
		"""
		pass

	@PatternStartTime.setter
	def PatternStartTime(self, patternstarttime: datetime) -> None:
		pass

	@property
	def PatternStartingMultiplier(self) -> float:
		"""The multiplier value of the first time step point in your pattern. Any real number can be used for this multiplier (it does not have to be 1.0).

		Returns
		--------
			``IPattern`` : 
		"""
		pass

	@PatternStartingMultiplier.setter
	def PatternStartingMultiplier(self, patternstartingmultiplier: float) -> None:
		pass

	@property
	def PatternCurve(self) -> IPatternCurveCollection:
		"""The pattern curve for this pattern.

		Returns
		--------
			``IPattern`` : 
		"""
		pass

	@property
	def DailyMultipliers(self) -> IDailyMultipliers:
		"""The daily multipliers for this pattern.

		Returns
		--------
			``IPattern`` : 
		"""
		pass

	@property
	def MonthlyMultipliers(self) -> IMonthlyMultipliers:
		"""The monthly multipliers for this pattern.

		Returns
		--------
			``IPattern`` : 
		"""
		pass

class IPatternUnits(IPatternMultiplierUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeFromStartUnit(self) -> IUnit:
		"""The formatter name for time from start

		Returns
		--------
			``IPatternUnits`` : 
		"""
		pass

class IPatternMultiplierUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MultiplierUnit(self) -> IUnit:
		"""The formatter name for multiplier

		Returns
		--------
			``IPatternMultiplierUnits`` : 
		"""
		pass

class IPatterns(IWaterComponentsBase[IPatterns, IPattern, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPatternCurveCollection(ICollectionElements[IPatternCurve, IPatternCurveElement, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPatternCurve(ICollection[IPatternCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, timeFromStart: float, multiplier: float) -> IPatternCurveElement:
		"""Adds a new row to the collection using the parameter provided.

		Args
		--------
			timeFromStart (``float``) :  The amount of time from the Start Time of the pattern to the time step point being defined.
			multiplier (``float``) :  The multiplier value associated with the time step point.

		Returns
		--------
			``IPatternCurveElement`` : 
		"""
		pass

	@overload
	def Add(self) -> IPatternCurveElement:
		"""No Description

		Returns
		--------
			``IPatternCurveElement`` : 
		"""
		pass

class IPatternCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeFromStart(self) -> float:
		"""The amount of time from the Start Time of the pattern to the time step point being defined.

		Returns
		--------
			``IPatternCurveElement`` : 
		"""
		pass

	@TimeFromStart.setter
	def TimeFromStart(self, timefromstart: float) -> None:
		pass

	@property
	def Multiplier(self) -> float:
		"""The multiplier value associated with the time step point.

		Returns
		--------
			``IPatternCurveElement`` : 
		"""
		pass

	@Multiplier.setter
	def Multiplier(self, multiplier: float) -> None:
		pass

class IDailyMultipliers:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Sunday(self) -> float:
		"""Sunday multiplier

		Returns
		--------
			``IDailyMultipliers`` : 
		"""
		pass

	@Sunday.setter
	def Sunday(self, sunday: float) -> None:
		pass

	@property
	def Monday(self) -> float:
		"""Monday multiplier

		Returns
		--------
			``IDailyMultipliers`` : 
		"""
		pass

	@Monday.setter
	def Monday(self, monday: float) -> None:
		pass

	@property
	def Tuesday(self) -> float:
		"""Tuesday multiplier

		Returns
		--------
			``IDailyMultipliers`` : 
		"""
		pass

	@Tuesday.setter
	def Tuesday(self, tuesday: float) -> None:
		pass

	@property
	def Wednesday(self) -> float:
		"""Wednesday multiplier

		Returns
		--------
			``IDailyMultipliers`` : 
		"""
		pass

	@Wednesday.setter
	def Wednesday(self, wednesday: float) -> None:
		pass

	@property
	def Thursday(self) -> float:
		"""Thursday multiplier

		Returns
		--------
			``IDailyMultipliers`` : 
		"""
		pass

	@Thursday.setter
	def Thursday(self, thursday: float) -> None:
		pass

	@property
	def Friday(self) -> float:
		"""Friday multiplier

		Returns
		--------
			``IDailyMultipliers`` : 
		"""
		pass

	@Friday.setter
	def Friday(self, friday: float) -> None:
		pass

	@property
	def Saturday(self) -> float:
		"""Saturday multiplier

		Returns
		--------
			``IDailyMultipliers`` : 
		"""
		pass

	@Saturday.setter
	def Saturday(self, saturday: float) -> None:
		pass

class IMonthlyMultipliers:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def January(self) -> float:
		"""January multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@January.setter
	def January(self, january: float) -> None:
		pass

	@property
	def February(self) -> float:
		"""February multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@February.setter
	def February(self, february: float) -> None:
		pass

	@property
	def March(self) -> float:
		"""March multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@March.setter
	def March(self, march: float) -> None:
		pass

	@property
	def April(self) -> float:
		"""April multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@April.setter
	def April(self, april: float) -> None:
		pass

	@property
	def May(self) -> float:
		"""May multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@May.setter
	def May(self, may: float) -> None:
		pass

	@property
	def June(self) -> float:
		"""June multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@June.setter
	def June(self, june: float) -> None:
		pass

	@property
	def July(self) -> float:
		"""July multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@July.setter
	def July(self, july: float) -> None:
		pass

	@property
	def August(self) -> float:
		"""August multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@August.setter
	def August(self, august: float) -> None:
		pass

	@property
	def September(self) -> float:
		"""September multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@September.setter
	def September(self, september: float) -> None:
		pass

	@property
	def October(self) -> float:
		"""October multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@October.setter
	def October(self, october: float) -> None:
		pass

	@property
	def November(self) -> float:
		"""November multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@November.setter
	def November(self, november: float) -> None:
		pass

	@property
	def December(self) -> float:
		"""December multiplier

		Returns
		--------
			``IMonthlyMultipliers`` : 
		"""
		pass

	@December.setter
	def December(self, december: float) -> None:
		pass

class IPumpDefinitions(IWaterComponentsBase[IPumpDefinitions, IPumpDefinition, IPumpDefinitionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinition(IWaterComponentBase[IPumpDefinitions, IPumpDefinition, IPumpDefinitionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Head(self) -> IPumpDefinitionHead:
		"""The pump definition head settings.

		Returns
		--------
			``IPumpDefinition`` : 
		"""
		pass

	@property
	def Efficiency(self) -> IPumpDefinitionEfficiency:
		"""The efficiency settings for the pump definition

		Returns
		--------
			``IPumpDefinition`` : 
		"""
		pass

	@property
	def NPSH(self) -> IPumpDefinitionNPSH:
		"""The NPSH settings for the pump definition

		Returns
		--------
			``IPumpDefinition`` : 
		"""
		pass

	@property
	def Motor(self) -> IPumpDefinitionMotor:
		"""The motor settings for the pump definition

		Returns
		--------
			``IPumpDefinition`` : 
		"""
		pass

class IPumpDefinitionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""Unit information for flow

		Returns
		--------
			``IPumpDefinitionUnits`` : 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""Unit information for head

		Returns
		--------
			``IPumpDefinitionUnits`` : 
		"""
		pass

	@property
	def PowerUnit(self) -> IUnit:
		"""Unit information for power

		Returns
		--------
			``IPumpDefinitionUnits`` : 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""The field formatter information for efficiency

		Returns
		--------
			``IPumpDefinitionUnits`` : 
		"""
		pass

	@property
	def SpeedUnit(self) -> IUnit:
		"""The unit information for speed.

		Returns
		--------
			``IPumpDefinitionUnits`` : 
		"""
		pass

class IPumpDefinitionHead:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpDefinitionType(self) -> PumpDefinitionType:
		"""DepthFlowVariableSpeed

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@PumpDefinitionType.setter
	def PumpDefinitionType(self, pumpdefinitiontype: PumpDefinitionType) -> None:
		pass

	@property
	def ConstantPower(self) -> float:
		"""This is available only for constant-power pumps.

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@ConstantPower.setter
	def ConstantPower(self, constantpower: float) -> None:
		pass

	@property
	def DesignFlow(self) -> float:
		"""The pump definition's design flow.

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@DesignFlow.setter
	def DesignFlow(self, designflow: float) -> None:
		pass

	@property
	def DesignHead(self) -> float:
		"""The pump definitions design head.

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@DesignHead.setter
	def DesignHead(self, designhead: float) -> None:
		pass

	@property
	def ShutoffHead(self) -> float:
		"""The pump definition's shutoff head

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@ShutoffHead.setter
	def ShutoffHead(self, shutoffhead: float) -> None:
		pass

	@property
	def MaxOperatingHead(self) -> float:
		"""The pump definition's maximum operating head

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@MaxOperatingHead.setter
	def MaxOperatingHead(self, maxoperatinghead: float) -> None:
		pass

	@property
	def MaxOperatingFlow(self) -> float:
		"""The pump definition's maximum operating flow

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@MaxOperatingFlow.setter
	def MaxOperatingFlow(self, maxoperatingflow: float) -> None:
		pass

	@property
	def MaxExtendedFlow(self) -> float:
		"""The pump definition's max extended flow

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

	@MaxExtendedFlow.setter
	def MaxExtendedFlow(self, maxextendedflow: float) -> None:
		pass

	@property
	def PumpCurve(self) -> IPumpCurveCollection:
		"""Gets the pump curve collection

		Returns
		--------
			``IPumpDefinitionHead`` : 
		"""
		pass

class IPumpCurveCollection(ICollectionElements[IPumpCurve, IPumpCurveElement, IPumpCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpCurve(ICollection[IPumpCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, head: float) -> IPumpCurveElement:
		"""Adds a new row to the pump curve.

		Args
		--------
			flow (``float``) :  flow
			head (``float``) :  head

		Returns
		--------
			``IPumpCurveElement`` : 
		"""
		pass

	@overload
	def Add(self) -> IPumpCurveElement:
		"""No Description

		Returns
		--------
			``IPumpCurveElement`` : 
		"""
		pass

class IPumpCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""The flow for this row.

		Returns
		--------
			``IPumpCurveElement`` : 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Head(self) -> float:
		"""The head for this row.

		Returns
		--------
			``IPumpCurveElement`` : 
		"""
		pass

	@Head.setter
	def Head(self, head: float) -> None:
		pass

class IPumpCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""The field formatter for flow

		Returns
		--------
			``IPumpCurveUnits`` : 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""The field formatter for head.

		Returns
		--------
			``IPumpCurveUnits`` : 
		"""
		pass

class IPumpDefinitionEfficiency:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpEfficiencyType(self) -> PumpEfficiencyTypeEnum:
		"""The type of efficiency to use for this pump definition

		Returns
		--------
			``IPumpDefinitionEfficiency`` : 
		"""
		pass

	@PumpEfficiencyType.setter
	def PumpEfficiencyType(self, pumpefficiencytype: PumpEfficiencyTypeEnum) -> None:
		pass

	@property
	def BEPFlow(self) -> float:
		"""The BEP Flow for this pump definition

		Returns
		--------
			``IPumpDefinitionEfficiency`` : 
		"""
		pass

	@BEPFlow.setter
	def BEPFlow(self, bepflow: float) -> None:
		pass

	@property
	def BEPEfficiency(self) -> float:
		"""The BEP efficiency for this pump definition.

		Returns
		--------
			``IPumpDefinitionEfficiency`` : 
		"""
		pass

	@BEPEfficiency.setter
	def BEPEfficiency(self, bepefficiency: float) -> None:
		pass

	@property
	def DefineBEPMaximumFlow(self) -> bool:
		"""If true, set a user defined BEP maximum flow.

		Returns
		--------
			``IPumpDefinitionEfficiency`` : 
		"""
		pass

	@DefineBEPMaximumFlow.setter
	def DefineBEPMaximumFlow(self, definebepmaximumflow: bool) -> None:
		pass

	@property
	def UserDefinedBEPMaximumFlow(self) -> float:
		"""The user defined maximum BEP flow for this pump definition.

		Returns
		--------
			``IPumpDefinitionEfficiency`` : 
		"""
		pass

	@UserDefinedBEPMaximumFlow.setter
	def UserDefinedBEPMaximumFlow(self, userdefinedbepmaximumflow: float) -> None:
		pass

	@property
	def ConstantEfficiency(self) -> float:
		"""The constant efficiency for the pump definition.

		Returns
		--------
			``IPumpDefinitionEfficiency`` : 
		"""
		pass

	@ConstantEfficiency.setter
	def ConstantEfficiency(self, constantefficiency: float) -> None:
		pass

	@property
	def FlowEfficiencyCurve(self) -> IFlowEfficiencyCollection:
		"""The flow-efficiency curve for this pump definition

		Returns
		--------
			``IPumpDefinitionEfficiency`` : 
		"""
		pass

class IFlowEfficiencyCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""The flow in display units.

		Returns
		--------
			``IFlowEfficiencyCurveElement`` : 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Efficiency(self) -> float:
		"""The efficiency in display units

		Returns
		--------
			``IFlowEfficiencyCurveElement`` : 
		"""
		pass

	@Efficiency.setter
	def Efficiency(self, efficiency: float) -> None:
		pass

class IFlowEfficiencyCurve(ICollection[IFlowEfficiencyCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, efficiency: float) -> IFlowEfficiencyCurveElement:
		"""Adds a new row to the pump efficiency curve

		Args
		--------
			flow (``float``) :  The flow in display units
			efficiency (``float``) :  The efficiency in display units

		Returns
		--------
			``IFlowEfficiencyCurveElement`` : 
		"""
		pass

	@overload
	def Add(self) -> IFlowEfficiencyCurveElement:
		"""No Description

		Returns
		--------
			``IFlowEfficiencyCurveElement`` : 
		"""
		pass

class IFlowEfficiencyUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""The field formatter information for flow

		Returns
		--------
			``IFlowEfficiencyUnits`` : 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""The field formatter information for efficiency

		Returns
		--------
			``IFlowEfficiencyUnits`` : 
		"""
		pass

class IFlowEfficiencyCollection(ICollectionElements[IFlowEfficiencyCurve, IFlowEfficiencyCurveElement, IFlowEfficiencyUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinitionNPSH:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UseNPSHCurve(self) -> bool:
		"""Sets whether the NPSH curve is used during calculations.

		Returns
		--------
			``IPumpDefinitionNPSH`` : 
		"""
		pass

	@UseNPSHCurve.setter
	def UseNPSHCurve(self, usenpshcurve: bool) -> None:
		pass

	@property
	def NPSHCurveSafetyFactor(self) -> float:
		"""The safety factor to use with the NPSH curve duration calculations.

		Returns
		--------
			``IPumpDefinitionNPSH`` : 
		"""
		pass

	@NPSHCurveSafetyFactor.setter
	def NPSHCurveSafetyFactor(self, npshcurvesafetyfactor: float) -> None:
		pass

	@property
	def NPSHCurve(self) -> INPSHCurveCollection:
		"""The NPSH curve collection

		Returns
		--------
			``IPumpDefinitionNPSH`` : 
		"""
		pass

class IFlowNPSHr(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns
		--------
			``IFlowNPSHr`` : 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def NPSHr(self) -> float:
		"""No Description

		Returns
		--------
			``IFlowNPSHr`` : 
		"""
		pass

	@NPSHr.setter
	def NPSHr(self, npshr: float) -> None:
		pass

class IFlowNPSHrCurve(ICollection[IFlowNPSHr]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, NPSHr: float) -> IFlowNPSHr:
		"""Adds a new row to the colletion with the given data.

		Args
		--------
			flow (``float``) :  flow
			NPSHr (``float``) :  NPSHr

		Returns
		--------
			``IFlowNPSHr`` : 
		"""
		pass

	@overload
	def Add(self) -> IFlowNPSHr:
		"""No Description

		Returns
		--------
			``IFlowNPSHr`` : 
		"""
		pass

class INPSHCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""Unit information for flow

		Returns
		--------
			``INPSHCurveUnits`` : 
		"""
		pass

	@property
	def NPSHUnit(self) -> IUnit:
		"""Unit information for NPSH

		Returns
		--------
			``INPSHCurveUnits`` : 
		"""
		pass

class INPSHCurveCollection(ICollectionElements[IFlowNPSHrCurve, IFlowNPSHr, INPSHCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinitionMotor:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsVariableSpeedDrive(self) -> bool:
		"""Sets if the pump definition's motor is variable speed.

		Returns
		--------
			``IPumpDefinitionMotor`` : 
		"""
		pass

	@IsVariableSpeedDrive.setter
	def IsVariableSpeedDrive(self, isvariablespeeddrive: bool) -> None:
		pass

	@property
	def MotorEfficiency(self) -> float:
		"""The efficiency of the constant speed motor

		Returns
		--------
			``IPumpDefinitionMotor`` : 
		"""
		pass

	@MotorEfficiency.setter
	def MotorEfficiency(self, motorefficiency: float) -> None:
		pass

	@property
	def SpeedEfficiencyCurve(self) -> ISpeedEfficiencyCurveCollection:
		"""The variable speed efficiency curve for the pump definition

		Returns
		--------
			``IPumpDefinitionMotor`` : 
		"""
		pass

class ISpeedEfficiency(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Speed(self) -> float:
		"""No Description

		Returns
		--------
			``ISpeedEfficiency`` : 
		"""
		pass

	@Speed.setter
	def Speed(self, speed: float) -> None:
		pass

	@property
	def Efficiency(self) -> float:
		"""No Description

		Returns
		--------
			``ISpeedEfficiency`` : 
		"""
		pass

	@Efficiency.setter
	def Efficiency(self, efficiency: float) -> None:
		pass

class ISpeedEfficiencyCurve(ICollection[ISpeedEfficiency]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, speed: float, efficiency: float) -> ISpeedEfficiency:
		"""Adds a new row to the collection with the given data.

		Args
		--------
			speed (``float``) :  speed
			efficiency (``float``) :  efficiency

		Returns
		--------
			``ISpeedEfficiency`` : 
		"""
		pass

	@overload
	def Add(self) -> ISpeedEfficiency:
		"""No Description

		Returns
		--------
			``ISpeedEfficiency`` : 
		"""
		pass

class ISpeedEfficiencyUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SpeedUnit(self) -> IUnit:
		"""Unit information for speed

		Returns
		--------
			``ISpeedEfficiencyUnits`` : 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""Unit information for efficiency

		Returns
		--------
			``ISpeedEfficiencyUnits`` : 
		"""
		pass

class ISpeedEfficiencyCurveCollection(ICollectionElements[ISpeedEfficiencyCurve, ISpeedEfficiency, ISpeedEfficiencyUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IConstituent(IWaterComponentBase[IConstituents, IConstituent, IConstituentUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Diffusivity(self) -> float:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@Diffusivity.setter
	def Diffusivity(self, diffusivity: float) -> None:
		pass

	@property
	def HasUnlimitedConcentration(self) -> bool:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@HasUnlimitedConcentration.setter
	def HasUnlimitedConcentration(self, hasunlimitedconcentration: bool) -> None:
		pass

	@property
	def ConcentrationLimit(self) -> float:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@ConcentrationLimit.setter
	def ConcentrationLimit(self, concentrationlimit: float) -> None:
		pass

	@property
	def BulkReactionOrder(self) -> int:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@BulkReactionOrder.setter
	def BulkReactionOrder(self, bulkreactionorder: int) -> None:
		pass

	@property
	def BulkReactionRate(self) -> float:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@BulkReactionRate.setter
	def BulkReactionRate(self, bulkreactionrate: float) -> None:
		pass

	@property
	def IsRoughnessCorrelated(self) -> bool:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@IsRoughnessCorrelated.setter
	def IsRoughnessCorrelated(self, isroughnesscorrelated: bool) -> None:
		pass

	@property
	def RoughnessCorrelationFactor(self) -> float:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@RoughnessCorrelationFactor.setter
	def RoughnessCorrelationFactor(self, roughnesscorrelationfactor: float) -> None:
		pass

	@property
	def WallReactionOrder(self) -> WallReactionOrder:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@WallReactionOrder.setter
	def WallReactionOrder(self, wallreactionorder: WallReactionOrder) -> None:
		pass

	@property
	def ZeroOrderWallReactionRate(self) -> float:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@ZeroOrderWallReactionRate.setter
	def ZeroOrderWallReactionRate(self, zeroorderwallreactionrate: float) -> None:
		pass

	@property
	def FirstOrderWallReactionRate(self) -> float:
		"""No Description

		Returns
		--------
			``IConstituent`` : 
		"""
		pass

	@FirstOrderWallReactionRate.setter
	def FirstOrderWallReactionRate(self, firstorderwallreactionrate: float) -> None:
		pass

class IConstituents(IWaterComponentsBase[IConstituents, IConstituent, IConstituentUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IConstituentUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitDemandLoad(IWaterComponentBase[IUnitDemandLoads, IUnitDemandLoad, IUnitDemandLoadUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UnitDemand(self) -> float:
		"""The unit load.

		Returns
		--------
			``IUnitDemandLoad`` : 
		"""
		pass

	@UnitDemand.setter
	def UnitDemand(self, unitdemand: float) -> None:
		pass

	@property
	def UnitDemandType(self) -> UnitDemandLoadTypeEnum:
		"""The type of unit demand load

		Returns
		--------
			``IUnitDemandLoad`` : 
		"""
		pass

	@UnitDemandType.setter
	def UnitDemandType(self, unitdemandtype: UnitDemandLoadTypeEnum) -> None:
		pass

	@property
	def PopulationUnit(self) -> PopulationUnit:
		"""The population unit to use for population unit demand load

		Returns
		--------
			``IUnitDemandLoad`` : 
		"""
		pass

	@PopulationUnit.setter
	def PopulationUnit(self, populationunit: PopulationUnit) -> None:
		pass

	@property
	def AreaUnit(self) -> AreaUnit:
		"""The area unit to use for area unit demand load

		Returns
		--------
			``IUnitDemandLoad`` : 
		"""
		pass

	@AreaUnit.setter
	def AreaUnit(self, areaunit: AreaUnit) -> None:
		pass

	@property
	def CountUnit(self) -> str:
		"""A user defined unit for count unit demand loads

		Returns
		--------
			``IUnitDemandLoad`` : 
		"""
		pass

	@CountUnit.setter
	def CountUnit(self, countunit: str) -> None:
		pass

	@property
	def ReportPopulationEquivalent(self) -> bool:
		"""Flag to specify the population equivalent of the unit demand load.

		Returns
		--------
			``IUnitDemandLoad`` : 
		"""
		pass

	@ReportPopulationEquivalent.setter
	def ReportPopulationEquivalent(self, reportpopulationequivalent: bool) -> None:
		pass

	@property
	def PopulationEquivalent(self) -> float:
		"""The population density applicable only to area and count unit loads.

		Returns
		--------
			``IUnitDemandLoad`` : 
		"""
		pass

	@PopulationEquivalent.setter
	def PopulationEquivalent(self, populationequivalent: float) -> None:
		pass

class IUnitDemandLoads(IWaterComponentsBase[IUnitDemandLoads, IUnitDemandLoad, IUnitDemandLoadUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitDemandLoadUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISCADASignal(IWaterComponentBase[ISCADASignals, ISCADASignal, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ScadaDatasourceID(self) -> int:
		"""The SCADA data source that this signal is part of.

		Returns
		--------
			``ISCADASignal`` : 
		"""
		pass

	@property
	def SignalLabel(self) -> str:
		"""The label of the SCADA signal

		Returns
		--------
			``ISCADASignal`` : 
		"""
		pass

	@SignalLabel.setter
	def SignalLabel(self, signallabel: str) -> None:
		pass

	@property
	def IsDerived(self) -> bool:
		"""Flag that this SCADA signal is a dervied signal where the value is based on other signals.

		Returns
		--------
			``ISCADASignal`` : 
		"""
		pass

	@IsDerived.setter
	def IsDerived(self, isderived: bool) -> None:
		pass

	@property
	def Formula(self) -> str:
		"""The formula to use for this derived signal

		Returns
		--------
			``ISCADASignal`` : 
		"""
		pass

	@Formula.setter
	def Formula(self, formula: str) -> None:
		pass

	@property
	def TransformMethod(self) -> SCADASignalTransformMethod:
		"""The transform method to use for this signal.  Only applies if it is derived.

		Returns
		--------
			``ISCADASignal`` : 
		"""
		pass

	@TransformMethod.setter
	def TransformMethod(self, transformmethod: SCADASignalTransformMethod) -> None:
		pass

class ISCADASignals(IWaterComponentsBase[ISCADASignals, ISCADASignal, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVHeadlossCurve(IWaterComponentBase[IGPVHeadlossCurves, IGPVHeadlossCurve, IGPVHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVHeadlossFlowCurve(self) -> IGPVFlowHeadlossCurveCollection:
		"""The GPV flow-headloss curve collection

		Returns
		--------
			``IGPVHeadlossCurve`` : 
		"""
		pass

class IGPVHeadlossCurves(IWaterComponentsBase[IGPVHeadlossCurves, IGPVHeadlossCurve, IGPVHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVHeadlossUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVFlowHeadloss(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns
		--------
			``IGPVFlowHeadloss`` : 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Headloss(self) -> float:
		"""No Description

		Returns
		--------
			``IGPVFlowHeadloss`` : 
		"""
		pass

	@Headloss.setter
	def Headloss(self, headloss: float) -> None:
		pass

class IGPVFlowHeadlossCurve(ICollection[IGPVFlowHeadloss]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, headloss: float) -> IGPVFlowHeadloss:
		"""Adds a row to the collection with the given data.

		Args
		--------
			flow (``float``) :  flow
			headloss (``float``) :  headloss

		Returns
		--------
			``IGPVFlowHeadloss`` : 
		"""
		pass

	@overload
	def Add(self) -> IGPVFlowHeadloss:
		"""No Description

		Returns
		--------
			``IGPVFlowHeadloss`` : 
		"""
		pass

class IGPVFlowHeadlossCurveCollection(ICollectionElements[IGPVFlowHeadlossCurve, IGPVFlowHeadloss, IGPVFlowHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVFlowHeadlossUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> IUnit:
		"""Unit information for flow

		Returns
		--------
			``IGPVFlowHeadlossUnits`` : 
		"""
		pass

	@property
	def Headloss(self) -> IUnit:
		"""Unit information for headloss

		Returns
		--------
			``IGPVFlowHeadlossUnits`` : 
		"""
		pass

class IValveCharacteristic(IWaterComponentBase[IValveCharacteristics, IValveCharacteristic, IValveCharacteristicUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristicsCurve(self) -> IValveCharacteristicsCurveCollection:
		"""The valve characteristics curve

		Returns
		--------
			``IValveCharacteristic`` : 
		"""
		pass

class IValveCharacteristics(IWaterComponentsBase[IValveCharacteristics, IValveCharacteristic, IValveCharacteristicUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveCharacteristicUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRelativeClosureRelativeArea(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeClosure(self) -> float:
		"""No Description

		Returns
		--------
			``IRelativeClosureRelativeArea`` : 
		"""
		pass

	@RelativeClosure.setter
	def RelativeClosure(self, relativeclosure: float) -> None:
		pass

	@property
	def RelativeArea(self) -> float:
		"""No Description

		Returns
		--------
			``IRelativeClosureRelativeArea`` : 
		"""
		pass

	@RelativeArea.setter
	def RelativeArea(self, relativearea: float) -> None:
		pass

class IRelativeClosureRelativeAreas(ICollection[IRelativeClosureRelativeArea]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, relativeClosure: float, relativeArea: float) -> IRelativeClosureRelativeArea:
		"""Adds a new row to the collection with the given data.

		Args
		--------
			relativeClosure (``float``) :  relativeClosure
			relativeArea (``float``) :  relativeArea

		Returns
		--------
			``IRelativeClosureRelativeArea`` : 
		"""
		pass

	@overload
	def Add(self) -> IRelativeClosureRelativeArea:
		"""No Description

		Returns
		--------
			``IRelativeClosureRelativeArea`` : 
		"""
		pass

class IValveCharacteristicsCurveCollection(ICollectionElements[IRelativeClosureRelativeAreas, IRelativeClosureRelativeArea, IRelativeClosureRelativeAreaUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRelativeClosureRelativeAreaUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ClosureUnit(self) -> IUnit:
		"""Unit information for relative closure

		Returns
		--------
			``IRelativeClosureRelativeAreaUnits`` : 
		"""
		pass

	@property
	def AreaUnit(self) -> IUnit:
		"""Unit information for relative area

		Returns
		--------
			``IRelativeClosureRelativeAreaUnits`` : 
		"""
		pass

class IMinorLossCoefficients(IWaterComponentsBase[IMinorLossCoefficients, IMinorLossCoefficient, IMinorLossCoefficientUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IMinorLossCoefficient(IWaterComponentBase[IMinorLossCoefficients, IMinorLossCoefficient, IMinorLossCoefficientUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MinorLossType(self) -> MinorLossTypeEnum:
		"""The type of minor loss.

		Returns
		--------
			``IMinorLossCoefficient`` : 
		"""
		pass

	@MinorLossType.setter
	def MinorLossType(self, minorlosstype: MinorLossTypeEnum) -> None:
		pass

	@property
	def MinorLoss(self) -> float:
		"""the minor loss coefficient, typically from a shared library

		Returns
		--------
			``IMinorLossCoefficient`` : 
		"""
		pass

	@MinorLoss.setter
	def MinorLoss(self, minorloss: float) -> None:
		pass

class IMinorLossCoefficientUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""Uni tinformation about the minor loss

		Returns
		--------
			``IMinorLossCoefficientUnits`` : 
		"""
		pass

class IWaterModelSupport(IModelComponents[IWaterComponent, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SCADASignals(self, dataSourceID: int) -> ISCADASignals:
		"""Gets the SCADA signals for the given ID
            Any new signals added in this instance will
            automatically be associated with this id.

		Args
		--------
			dataSourceID (``int``) :  A valid, non-zero SCADA data source ID

		Returns
		--------
			``ISCADASignals`` : If the dataSourceID is valid, returns the manager, otherwise null
		"""
		pass

	@property
	def Zones(self) -> IZones:
		"""The zones in the model.

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def Patterns(self) -> IPatterns:
		"""The patterns in the model.

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def PumpDefinitions(self) -> IPumpDefinitions:
		"""The pump definitions in the model.

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def Constituents(self) -> IConstituents:
		"""The constituents in the model.

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def UnitDemandLoads(self) -> IUnitDemandLoads:
		"""The unit demand loads in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def Controls(self) -> IControls:
		"""The controls in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def ControlConditions(self) -> IControlConditions:
		"""The control conditions in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def ControlActions(self) -> IControlActions:
		"""The control actions in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def AirFlowCurves(self) -> IAirFlowCurves:
		"""The air flow curves in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def GPVHeadlossCurves(self) -> IGPVHeadlossCurves:
		"""The GPV headloss curves in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristics:
		"""The valve characteristics in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

	@property
	def MinorLossCoefficients(self) -> IMinorLossCoefficients:
		"""The minor loss coefficients in the model

		Returns
		--------
			``IWaterModelSupport`` : 
		"""
		pass

