from OpenFlows.IAnalysis import IAnalysisCalculator
from OpenFlows.Water.Domain.IModelingElements import IWaterScenario, IWaterScenarios
from OpenFlows.Water.Domain.ModelingElements.ICalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits

class IScenarioEnergyCostCalculator(IAnalysisCalculator[IWaterScenario, IWaterScenarios, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAnalysisTools:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ScenarioEnergyCostCalculator(self) -> IScenarioEnergyCostCalculator:
		"""Configures and runs a scenario energy cost calculation.

		Returns
		--------
			`IScenarioEnergyCostCalculator` : 
		"""
		pass

