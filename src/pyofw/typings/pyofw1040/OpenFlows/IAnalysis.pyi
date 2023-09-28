from OpenFlows.Domain.IDataObjects import TScenarioType
from typing import Generic, TypeVar
from OpenFlows.Domain.IModelingElements import IScenario, IScenarios, IScenarioOptions, IElementUnits

TScenarioManagerType = TypeVar("TScenarioManagerType")
TScenarioOptionsType = TypeVar("TScenarioOptionsType")
TScenarioOptionsUnitsType = TypeVar("TScenarioOptionsUnitsType")

class IAnalysisCalculator(Generic[TScenarioType, TScenarioManagerType, TScenarioOptionsType, TScenarioOptionsUnitsType]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Run(self, scenario: TScenarioType) -> None:
		"""No Description

		Args
		--------
			scenario (`TScenarioType`) :  scenario

		Returns
		--------
			`None` : 
		"""
		pass

