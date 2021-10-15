from enum import Enum
from OpenFlows.Domain.DataObjects import IModel
from OpenFlows.Water.Units import INetworkElementUnits, IComponentElementUnits
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IWaterNetwork, IWaterElement
from OpenFlows.Water.Domain.ModelingElements.Components import IWaterModelSupport, IWaterComponent
from OpenFlows.Water.Domain.ModelingElements import IWaterScenarios, IWaterScenario, IWaterSelectionSets, IWaterSelectionSet
from OpenFlows.Water.Domain.ModelingElements.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits
from OpenFlows.Water.Analysis import IAnalysisTools

class CalculationType(Enum):
	FireFlow = 0
	Flushing = 1
	Age = 2
	Constituent = 3
	Trace = 4
	HydraulicsOnly = 5
	MSX = 6
	SCADAConnectAnalysis = 7
	WaterQuality = 8

class DemandAdjustmentsType(Enum):
	None = 0
	Active = 1

class UnitDemandAdjustmentType(Enum):
	None = 0
	Active = 1

class RoughnessAdjustmentType(Enum):
	None = 0
	Active = 1

class AdjustmentOperationType(Enum):
	Add = 0
	Subtrace = 1
	Multiply = 2
	Divide = 3
	Set = 4

class ConstituentSourceType(Enum):
	Concentration = 0
	FlowPacedBooster = 1
	SetpointBooster = 2
	MassBooster = 3

class PipeStatusType(Enum):
	Open = 0
	Closed = 1

class ValveSettingType(Enum):
	Active = 0
	Inactive = 1
	Closed = 2

class TCVCoefficientType(Enum):
	Headloss = 1
	Discharge = 2
	ValveCharacteristics = 3

class PressureValvesettingType(Enum):
	ValvePressure = 0
	ValveHGL = 1

class TankSectionType(Enum):
	Circular = 0
	NonCircular = 1
	VariableArea = 2

class IWaterModel(IModel[IWaterNetwork, IWaterModelSupport, IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits, IWaterSelectionSets, IWaterSelectionSet, IWaterElement, IWaterElement, WaterNetworkElementType, IWaterComponent, WaterComponentType, INetworkElementUnits, IComponentElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AnalysisTools(self) -> IAnalysisTools:
		"""No Description

		Returns:
			IWaterModel: 
		"""
		pass

