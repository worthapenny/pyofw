from OpenFlows.Domain.DataObjects import TScenarioType
from typing import Generic, TypeVar
from OpenFlows.Domain.ModelingElements import IScenario, IScenarios, IScenarioOptions, IElementUnits

TScenarioManagerType = TypeVar("TScenarioManagerType", IScenarios)
TScenarioOptionsType = TypeVar("TScenarioOptionsType", IScenarioOptions)
TScenarioOptionsUnitsType = TypeVar("TScenarioOptionsUnitsType", IElementUnits)

class IAnalysisCalculator(Generic[TScenarioType, TScenarioManagerType, TScenarioOptionsType, TScenarioOptionsUnitsType]):

	def __init__(self) -> None:
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
			scenario (``TScenarioType``) :  scenario

		Returns
		--------
			``None`` : 
		"""
		pass

