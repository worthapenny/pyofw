from typing import List, Iterator
from OpenFlows.Domain.ModelingElements.ICollections import IResultCollectionElements, IResultCollection, ICollectionElement
from OpenFlows.IUnits import IUnit
from OpenFlows.Domain.IModelingElements import IElementUnits, IScenario, IScenarios, ISelectionSet, ISelectionSets, IModelingElementBase, IElement, IModelingElementsBase, IElements, IElementManager
from OpenFlows.Domain.IDataObjects import INetworkPrototypes
from OpenFlows.Water.Domain.ModelingElements.ICalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits
from OpenFlows.Water.Domain.ModelingElements.INetworkElements import IWaterElement
from Haestad.Support.ISupport import IEditLabeled, ILabeled

class IPressureCalculationSummaryResults:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetCalculationResultsMessages(self) -> List[ICalculationResultsMessage]:
		"""Gets all the calculation results messages across all time steps

		Returns
		--------
			`List[ICalculationResultsMessage]` : A list of messages (can be empty) or null if there are no results
		"""
		pass

	def GetCalculationResultsIntraTrialStatusMessages(self) -> List[ICalculationResultsMessage]:
		"""Gets the intro-status messages for the analysis

		Returns
		--------
			`List[ICalculationResultsMessage]` : A list of messages (can be empty) or null if there are no results
		"""
		pass

	def GetCalculationResultsInfoMessages(self) -> List[ICalculationResultsMessage]:
		"""Gets the calculation information messages for the analysis.

		Returns
		--------
			`List[ICalculationResultsMessage]` : A list of messages (can be empty) or null if thre are no results
		"""
		pass

	def Trials(self, timeStepIndex: int) -> ITrialCollection:
		"""Gets the trial collection at the given time step index

		Args
		--------
			timeStepIndex (`int`) :  The 0-based time step index to us to get the trial collection.

		Returns
		--------
			`ITrialCollection` : 
		"""
		pass

	@property
	def IsBalanced(self) -> Union[bool, None]:
		"""True if the network calculation was balanced overall.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def TotalIterations(self) -> Union[int, None]:
		"""Total number of iterations used.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def MaximumRelativeFlowChange(self) -> Union[float, None]:
		"""The maximum relative flow change across all time steps.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def FlowSupplied(self) -> Union[float, None]:
		"""The total flow supplied to the system.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def FlowDemanded(self) -> Union[float, None]:
		"""The total flow demanded by the system.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def FlowStored(self) -> Union[float, None]:
		"""The total flow stored by the system.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def Status(self) -> Union[int, None]:
		"""The overall status of the system.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def CalculationSumamryCollection(self) -> ICalculationSummaryCollection:
		"""The calculation summary across all time steps

		Returns
		--------
			`ICalculationSummaryCollection` : 
		"""
		pass

	@property
	def Units(self) -> ICalculationSummaryUnits:
		"""The units for the calculation summary

		Returns
		--------
			`ICalculationSummaryUnits` : 
		"""
		pass

	@property
	def CalculationTimeStemp(self) -> Union[datetime, None]:
		"""Date and time when the calculation was started.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def LoadTime(self) -> str:
		"""Time taken to load the calculation data.

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def RunTime(self) -> str:
		"""Time take to run the analysis.

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def TimeStepCount(self) -> Union[int, None]:
		"""Number of calculated time steps for the analysis.

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def LinkCount(self) -> Union[int, None]:
		"""Number of links used in the computational analysis (this statistic is a core engine statistic and will not necessarily match number of pipes in a model).

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def NodeCount(self) -> Union[int, None]:
		"""Number of nodes used in the computational analysis (this statistic is a core engine statistic and will not necessarily match number of nodes in a model).

		Returns
		--------
			`Nullable` : 
		"""
		pass

class ICalculationSummaryCollection(IResultCollectionElements[ICalculationSummary, ICalculationSummaryElement, ICalculationSummaryUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICalculationSummaryUnits(IElementUnits):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""Unit for FlowSupplied, FlowDemanded and FlowStored

		Returns
		--------
			`IUnit` : 
		"""
		pass

	@property
	def RelativeFlowChangeUnit(self) -> IUnit:
		"""Unit for relative flow change

		Returns
		--------
			`IUnit` : 
		"""
		pass

class ICalculationSummary(IResultCollection[ICalculationSummaryElement]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICalculationSummaryElement(ICollectionElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeStepIndex(self) -> int:
		"""The time step index this row represents

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Time(self) -> str:
		"""The date/time of this time step index represents

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Status(self) -> Union[int, None]:
		"""The status of the simulation at this time step

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def IsBAlanced(self) -> Union[bool, None]:
		"""Whether or not the system balanced athtis times tep

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def Trials(self) -> Union[int, None]:
		"""The number of trials used to calculate this time step

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def RelativeFlowChange(self) -> Union[float, None]:
		"""the relative flow change at this time step

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def FlowSupplied(self) -> Union[float, None]:
		"""The flow supplied at this time step

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def FlowDemanded(self) -> Union[float, None]:
		"""The flow demanded at this time step

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@property
	def FlowStored(self) -> Union[float, None]:
		"""The flow stored at this time step

		Returns
		--------
			`Nullable` : 
		"""
		pass

class ICalculationResultsMessage(ICollectionElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> str:
		"""The time of the message

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def ElementId(self) -> int:
		"""The id of the element

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Message(self) -> str:
		"""the user notification message

		Returns
		--------
			`str` : 
		"""
		pass

class ITrialCollection(IResultCollectionElements[ITrials, ITrial, ITrialUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITrialUnits(IElementUnits):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeFlowChangeUnit(self) -> IUnit:
		"""The units for relative flow change

		Returns
		--------
			`IUnit` : 
		"""
		pass

class ITrials(IResultCollection[ITrial]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITrial(ICollectionElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> str:
		"""The time of this trial relative flow change

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def TrialIndex(self) -> int:
		"""The trial number

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def TrialRelativeFlowChange(self) -> float:
		"""The relative flow change for this trial.

		Returns
		--------
			`float` : 
		"""
		pass

class IWaterScenario(IScenario[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureCalculationResults(self) -> IPressureCalculationSummaryResults:
		"""The pressure calculation results for the scenario.  Returns null if there are no results.

		Returns
		--------
			`IPressureCalculationSummaryResults` : 
		"""
		pass

class IWaterScenarios(IScenarios[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterSelectionSet(ISelectionSet[IWaterSelectionSets, IWaterSelectionSet, IWaterElement]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterSelectionSets(ISelectionSets[IWaterSelectionSets, IWaterSelectionSet, IWaterElement]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterNetworkPrototypes(INetworkPrototypes[WaterNetworkElementType]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

