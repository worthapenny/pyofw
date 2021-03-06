from OpenFlows.Domain.ModelingElements import IScenario, IScenarios, ISelectionSet, ISelectionSets, IModelingElementBase, IElement, IModelingElementsBase, IElements, IElementManager
from OpenFlows.Water.Domain.ModelingElements.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IWaterElement
from Haestad.Support.Support import IEditLabeled, ILabeled

class IWaterScenario(IScenario[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterScenarios(IScenarios[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterSelectionSet(ISelectionSet[IWaterSelectionSets, IWaterSelectionSet, IWaterElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterSelectionSets(ISelectionSets[IWaterSelectionSets, IWaterSelectionSet, IWaterElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

