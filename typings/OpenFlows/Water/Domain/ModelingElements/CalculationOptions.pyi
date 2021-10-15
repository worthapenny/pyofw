from OpenFlows.Domain.ModelingElements.Collections import ICollectionElements, ICollection, ICollectionElement
from OpenFlows.Domain.ModelingElements import IElementUnits, IScenarioOptions
from OpenFlows.Water.Domain.ModelingElements import IWaterSelectionSet
from OpenFlows.Water.Domain.ModelingElements.Components import IPattern, IUnitDemandLoad
from OpenFlows.Water.Domain import AdjustmentOperationType, CalculationType, DemandAdjustmentsType, UnitDemandAdjustmentType, RoughnessAdjustmentType
from typing import overload
from datetime import datetime
from OpenFlows.Units import IUnit

class IActiveDemandAdjustmentsCollection(ICollectionElements[IActiveDemandAdjustments, IActiveDemandAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveDemandAdjustments(ICollection[IActiveDemandAdjustment]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, scope: IWaterSelectionSet, demandPattern: IPattern, operation: AdjustmentOperationType, value: float) -> IActiveDemandAdjustment:
		"""No Description

		Args:
			scope(IWaterSelectionSet): scope
			demandPattern(IPattern): demandPattern
			operation(AdjustmentOperationType): operation
			value(float): value

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@overload
	def Add(self) -> IActiveDemandAdjustment:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

class IActiveDemandAdjustment(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@DemandPattern.setter
	def DemandPattern(self, demandpattern: IPattern) -> None:
		pass

	@property
	def Value(self) -> float:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IActiveRoughnessAdjustmentCollection(ICollectionElements[IActiveRoughnessAdjustments, IActiveRoughnessAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveRoughnessAdjustments(ICollection[IActiveRoughnessAdjustment]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, scope: IWaterSelectionSet, operation: AdjustmentOperationType, value: float) -> IActiveRoughnessAdjustment:
		"""No Description

		Args:
			scope(IWaterSelectionSet): scope
			operation(AdjustmentOperationType): operation
			value(float): value

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

	@overload
	def Add(self) -> IActiveRoughnessAdjustment:
		"""No Description

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

class IActiveRoughnessAdjustment(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""No Description

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@property
	def Value(self) -> float:
		"""No Description

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""No Description

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IActiveUnitDemandAdjustmentCollection(ICollectionElements[IActiveUnitDemandAdjustments, IActiveUnitDemandAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveUnitDemandAdjustments(ICollection[IActiveUnitDemandAdjustment]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, scope: IWaterSelectionSet, unitDemandLoad: IUnitDemandLoad, operation: AdjustmentOperationType, value: float) -> IActiveUnitDemandAdjustment:
		"""No Description

		Args:
			scope(IWaterSelectionSet): scope
			unitDemandLoad(IUnitDemandLoad): unitDemandLoad
			operation(AdjustmentOperationType): operation
			value(float): value

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@overload
	def Add(self) -> IActiveUnitDemandAdjustment:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

class IActiveUnitDemandAdjustment(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@property
	def UnitLoadDemand(self) -> IUnitDemandLoad:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@UnitLoadDemand.setter
	def UnitLoadDemand(self, unitloaddemand: IUnitDemandLoad) -> None:
		pass

	@property
	def Value(self) -> float:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IWaterScenarioOptions(IScenarioOptions[IWaterScenarioOptionsUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CalculationType(self) -> CalculationType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@CalculationType.setter
	def CalculationType(self, calculationtype: CalculationType) -> None:
		pass

	@property
	def FrictionMethod(self) -> EpaNetEngine_FrictionMethodEnum:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@FrictionMethod.setter
	def FrictionMethod(self, frictionmethod: EpaNetEngine_FrictionMethodEnum) -> None:
		pass

	@property
	def SimulationStartDate(self) -> datetime:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@SimulationStartDate.setter
	def SimulationStartDate(self, simulationstartdate: datetime) -> None:
		pass

	@property
	def TimeAnalysisType(self) -> EpaNetEngine_TimeAnalysisTypeEnum:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@TimeAnalysisType.setter
	def TimeAnalysisType(self, timeanalysistype: EpaNetEngine_TimeAnalysisTypeEnum) -> None:
		pass

	@property
	def StartTime(self) -> datetime:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@StartTime.setter
	def StartTime(self, starttime: datetime) -> None:
		pass

	@property
	def Duration(self) -> float:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@Duration.setter
	def Duration(self, duration: float) -> None:
		pass

	@property
	def HydraulicTimeStep(self) -> float:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@HydraulicTimeStep.setter
	def HydraulicTimeStep(self, hydraulictimestep: float) -> None:
		pass

	@property
	def DemandAdjustments(self) -> DemandAdjustmentsType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@DemandAdjustments.setter
	def DemandAdjustments(self, demandadjustments: DemandAdjustmentsType) -> None:
		pass

	@property
	def ActiveDemandAdjustments(self) -> IActiveDemandAdjustmentsCollection:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def UnitDemandAdjustments(self) -> UnitDemandAdjustmentType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@UnitDemandAdjustments.setter
	def UnitDemandAdjustments(self, unitdemandadjustments: UnitDemandAdjustmentType) -> None:
		pass

	@property
	def ActiveUnitLoadDemandAdjustments(self) -> IActiveUnitDemandAdjustmentCollection:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def RoughnessAdjustments(self) -> RoughnessAdjustmentType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@RoughnessAdjustments.setter
	def RoughnessAdjustments(self, roughnessadjustments: RoughnessAdjustmentType) -> None:
		pass

	@property
	def ActiveRoughnessAdjustments(self) -> IActiveRoughnessAdjustmentCollection:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

class IWaterScenarioOptionsUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DurationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterScenarioOptionsUnits: 
		"""
		pass

	@property
	def HydraulicTimeStepUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterScenarioOptionsUnits: 
		"""
		pass

