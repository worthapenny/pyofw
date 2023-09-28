from OpenFlows.Domain.ModelingElements.ICollections import ICollectionElements, ICollection, ICollectionElement
from OpenFlows.Domain.IModelingElements import IElementUnits, IScenarioOptions, IElement
from OpenFlows.Water.Domain.IModelingElements import IWaterSelectionSet
from OpenFlows.Water.Domain.ModelingElements.IComponents import IPattern, IUnitDemandLoad
from OpenFlows.Water.IDomain import AdjustmentOperationType, CalculationType, DemandAdjustmentsType, UnitDemandAdjustmentType, RoughnessAdjustmentType
from typing import overload, Iterator
from Haestad.Domain.ModelingObjects.Water.IEnumerations import EpaNetEngine_FrictionMethodEnum, EpaNetEngine_TimeAnalysisTypeEnum
from datetime import datetime
from OpenFlows.IUnits import IUnit
from Haestad.Support.ISupport import IEditLabeled, ILabeled

class IActiveDemandAdjustmentsCollection(ICollectionElements[IActiveDemandAdjustments, IActiveDemandAdjustment, IElementUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveDemandAdjustments(ICollection[IActiveDemandAdjustment]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, scope: IWaterSelectionSet, demandPattern: IPattern, operation: AdjustmentOperationType, value: float) -> IActiveDemandAdjustment:
		"""Adds a new demand adjustment and assigns the values.

		Args
		--------
			scope (`IWaterSelectionSet`) :  scope
			demandPattern (`IPattern`) :  demandPattern
			operation (`AdjustmentOperationType`) :  operation
			value (`float`) :  value

		Returns
		--------
			`IActiveDemandAdjustment` : 
		"""
		pass

	@overload
	def Add(self) -> IActiveDemandAdjustment:
		"""No Description

		Returns
		--------
			`IActiveDemandAdjustment` : 
		"""
		pass

class IActiveDemandAdjustment(ICollectionElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""If null, applies to appropriate elements in entire network

		Returns
		--------
			`IWaterSelectionSet` : 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""The pattern to use for the adjustment.

		Returns
		--------
			`IPattern` : 
		"""
		pass

	@DemandPattern.setter
	def DemandPattern(self, demandpattern: IPattern) -> None:
		pass

	@property
	def Value(self) -> float:
		"""The value to apply

		Returns
		--------
			`float` : 
		"""
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""The operation to apply the value.

		Returns
		--------
			`AdjustmentOperationType` : 
		"""
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IActiveRoughnessAdjustmentCollection(ICollectionElements[IActiveRoughnessAdjustments, IActiveRoughnessAdjustment, IElementUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveRoughnessAdjustments(ICollection[IActiveRoughnessAdjustment]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, scope: IWaterSelectionSet, operation: AdjustmentOperationType, value: float) -> IActiveRoughnessAdjustment:
		"""Adds a new roughness adjustment.

		Args
		--------
			scope (`IWaterSelectionSet`) :  scope
			operation (`AdjustmentOperationType`) :  operation
			value (`float`) :  value

		Returns
		--------
			`IActiveRoughnessAdjustment` : 
		"""
		pass

	@overload
	def Add(self) -> IActiveRoughnessAdjustment:
		"""No Description

		Returns
		--------
			`IActiveRoughnessAdjustment` : 
		"""
		pass

class IActiveRoughnessAdjustment(ICollectionElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""The scope of pipes to apply adjustments

		Returns
		--------
			`IWaterSelectionSet` : 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@property
	def Value(self) -> float:
		"""The value to use to apply the adjustment

		Returns
		--------
			`float` : 
		"""
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""The operation to use to apply the adjustment

		Returns
		--------
			`AdjustmentOperationType` : 
		"""
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IActiveUnitDemandAdjustmentCollection(ICollectionElements[IActiveUnitDemandAdjustments, IActiveUnitDemandAdjustment, IElementUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveUnitDemandAdjustments(ICollection[IActiveUnitDemandAdjustment]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, scope: IWaterSelectionSet, unitDemandLoad: IUnitDemandLoad, operation: AdjustmentOperationType, value: float) -> IActiveUnitDemandAdjustment:
		"""Add a new unit demand adjustment.

		Args
		--------
			scope (`IWaterSelectionSet`) :  scope
			unitDemandLoad (`IUnitDemandLoad`) :  unitDemandLoad
			operation (`AdjustmentOperationType`) :  operation
			value (`float`) :  value

		Returns
		--------
			`IActiveUnitDemandAdjustment` : 
		"""
		pass

	@overload
	def Add(self) -> IActiveUnitDemandAdjustment:
		"""No Description

		Returns
		--------
			`IActiveUnitDemandAdjustment` : 
		"""
		pass

class IActiveUnitDemandAdjustment(ICollectionElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""The scope to apply the adjustment to

		Returns
		--------
			`IWaterSelectionSet` : 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@property
	def UnitLoadDemand(self) -> IUnitDemandLoad:
		"""The unit load demand to use.

		Returns
		--------
			`IUnitDemandLoad` : 
		"""
		pass

	@UnitLoadDemand.setter
	def UnitLoadDemand(self, unitloaddemand: IUnitDemandLoad) -> None:
		pass

	@property
	def Value(self) -> float:
		"""The value to apply the adjustment

		Returns
		--------
			`float` : 
		"""
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""How to apply the adjustment to the scope.

		Returns
		--------
			`AdjustmentOperationType` : 
		"""
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IWaterScenarioOptions(IScenarioOptions[IWaterScenarioOptionsUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CalculationType(self) -> CalculationType:
		"""The type of calculation to perform.

		Returns
		--------
			`CalculationType` : 
		"""
		pass

	@CalculationType.setter
	def CalculationType(self, calculationtype: CalculationType) -> None:
		pass

	@property
	def FrictionMethod(self) -> EpaNetEngine_FrictionMethodEnum:
		"""The friction method to use on pipes.

		Returns
		--------
			`EpaNetEngine_FrictionMethodEnum` : 
		"""
		pass

	@FrictionMethod.setter
	def FrictionMethod(self, frictionmethod: EpaNetEngine_FrictionMethodEnum) -> None:
		pass

	@property
	def SimulationStartDate(self) -> datetime:
		"""The simulation start date.

		Returns
		--------
			`datetime` : 
		"""
		pass

	@SimulationStartDate.setter
	def SimulationStartDate(self, simulationstartdate: datetime) -> None:
		pass

	@property
	def TimeAnalysisType(self) -> EpaNetEngine_TimeAnalysisTypeEnum:
		"""The analysis type - EPS or Steady-state.

		Returns
		--------
			`EpaNetEngine_TimeAnalysisTypeEnum` : 
		"""
		pass

	@TimeAnalysisType.setter
	def TimeAnalysisType(self, timeanalysistype: EpaNetEngine_TimeAnalysisTypeEnum) -> None:
		pass

	@property
	def StartTime(self) -> datetime:
		"""The start time of the analysis.

		Returns
		--------
			`datetime` : 
		"""
		pass

	@StartTime.setter
	def StartTime(self, starttime: datetime) -> None:
		pass

	@property
	def Duration(self) -> float:
		"""The length of the simulation.

		Returns
		--------
			`float` : 
		"""
		pass

	@Duration.setter
	def Duration(self, duration: float) -> None:
		pass

	@property
	def HydraulicTimeStep(self) -> float:
		"""The time step to use when calculating.

		Returns
		--------
			`float` : 
		"""
		pass

	@HydraulicTimeStep.setter
	def HydraulicTimeStep(self, hydraulictimestep: float) -> None:
		pass

	@property
	def ReportingTimeStep(self) -> float:
		"""Data will be presented every reporting time step.  The reporting time step should be a multiple of the Hydraulic Time Step.

		Returns
		--------
			`float` : 
		"""
		pass

	@ReportingTimeStep.setter
	def ReportingTimeStep(self, reportingtimestep: float) -> None:
		pass

	@property
	def DemandAdjustments(self) -> DemandAdjustmentsType:
		"""Select whether or not to apply adjustment factors to standard demands.

		Returns
		--------
			`DemandAdjustmentsType` : 
		"""
		pass

	@DemandAdjustments.setter
	def DemandAdjustments(self, demandadjustments: DemandAdjustmentsType) -> None:
		pass

	@property
	def ActiveDemandAdjustments(self) -> IActiveDemandAdjustmentsCollection:
		"""The collection of demand adjustment which are applied to the analysis.

		Returns
		--------
			`IActiveDemandAdjustmentsCollection` : 
		"""
		pass

	@property
	def UnitDemandAdjustments(self) -> UnitDemandAdjustmentType:
		"""Select whether or not to apply adjustment factors to unit demands.

		Returns
		--------
			`UnitDemandAdjustmentType` : 
		"""
		pass

	@UnitDemandAdjustments.setter
	def UnitDemandAdjustments(self, unitdemandadjustments: UnitDemandAdjustmentType) -> None:
		pass

	@property
	def ActiveUnitLoadDemandAdjustments(self) -> IActiveUnitDemandAdjustmentCollection:
		"""The collection of unit demand adjustments which are applied to the analysis.

		Returns
		--------
			`IActiveUnitDemandAdjustmentCollection` : 
		"""
		pass

	@property
	def RoughnessAdjustments(self) -> RoughnessAdjustmentType:
		"""Select whether or not to apply adjustment factors to roughnesses.

		Returns
		--------
			`RoughnessAdjustmentType` : 
		"""
		pass

	@RoughnessAdjustments.setter
	def RoughnessAdjustments(self, roughnessadjustments: RoughnessAdjustmentType) -> None:
		pass

	@property
	def ActiveRoughnessAdjustments(self) -> IActiveRoughnessAdjustmentCollection:
		"""The collection of pipe roughness adjustments which are applied to the analysis.

		Returns
		--------
			`IActiveRoughnessAdjustmentCollection` : 
		"""
		pass

class IWaterScenarioOptionsUnits(IElementUnits):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DurationUnit(self) -> IUnit:
		"""The units and formatter information for duration

		Returns
		--------
			`IUnit` : 
		"""
		pass

	@property
	def HydraulicTimeStepUnit(self) -> IUnit:
		"""The units and formatter information for hydraulic time step

		Returns
		--------
			`IUnit` : 
		"""
		pass

