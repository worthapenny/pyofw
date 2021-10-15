from enum import Enum
from typing import List, Generic, overload, TypeVar
from Haestad.Support.Support import SortContextCollection, FilterContextCollection, IEditLabeled
from OpenFlows.Domain.ModelingElements.Support import IFieldManager
from OpenFlows.Units import IUnit
from array import array
from datetime import datetime

TElementType = TypeVar("TElementType", IElement)
TElementManagerType = TypeVar("TElementManagerType", IModelingElementsBase)
TElementTypeEnum = TypeVar("TElementTypeEnum", Enum)
TUnitsType = TypeVar("TUnitsType", IElementUnits)
TScenarioOptionsType = TypeVar("TScenarioOptionsType", IScenarioOptions)
TScenarioOptionsUnitsType = TypeVar("TScenarioOptionsUnitsType", IElementUnits)
TNetworkElementType = TypeVar("TNetworkElementType", IElement)

class ModelingElementTypes(Enum):
	Scenario = 2
	SelectionSet = 7

class ModelElementType(Enum):
	All = 0
	Scenario = 2
	NetworkElement = 3
	ComponentElement = 4
	Options = 5
	SelectionSet = 6

class IElementManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementIDs(self) -> List[int]:
		"""No Description

		Returns:
			List[int]: 
		"""
		pass

	def Exists(self, id: int) -> bool:
		"""No Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns:
			IElementManager: 
		"""
		pass

class IElements(Generic[TElementType], IElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Elements(self) -> List[TElementType]:
		"""No Description

		Returns:
			List[TElementType]: 
		"""
		pass

	def SelectElements(self, sorts: SortContextCollection, filters: FilterContextCollection) -> List[TElementType]:
		"""No Description

		Args:
			sorts(SortContextCollection): sorts
			filters(FilterContextCollection): filters

		Returns:
			List[TElementType]: 
		"""
		pass

class IElement(IEditLabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns:
			IElement: 
		"""
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns:
			IElement: 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def ModelElementType(self) -> ModelElementType:
		"""No Description

		Returns:
			IElement: 
		"""
		pass

class IElementUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElementInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InputFields(self) -> IFieldManager:
		"""No Description

		Returns:
			IElementInput: 
		"""
		pass

class IElementsInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElementResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ResultFields(self) -> IFieldManager:
		"""No Description

		Returns:
			IElementResults: 
		"""
		pass

class IElementsResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IModelingElementBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Delete(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	@property
	def Manager(self) -> TElementManagerType:
		"""No Description

		Returns:
			IModelingElementBase: 
		"""
		pass

	@property
	def ElementType(self) -> TElementTypeEnum:
		"""No Description

		Returns:
			IModelingElementBase: 
		"""
		pass

class IModelingElementsBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElements[TElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Create(self) -> TElementType:
		"""No Description

		Returns:
			TElementType: 
		"""
		pass

	@overload
	def Element(self, id: int) -> TElementType:
		"""No Description

		Args:
			id(int): id

		Returns:
			TElementType: 
		"""
		pass

	@overload
	def Element(self, label: str) -> TElementType:
		"""No Description

		Args:
			label(str): label

		Returns:
			TElementType: 
		"""
		pass

	@overload
	def Elements(self, label: str) -> List[TElementType]:
		"""No Description

		Args:
			label(str): label

		Returns:
			List[TElementType]: 
		"""
		pass

	@overload
	def Elements(self) -> List[TElementType]:
		"""No Description

		Returns:
			List[TElementType]: 
		"""
		pass

	@property
	def ElementType(self) -> TElementTypeEnum:
		"""No Description

		Returns:
			IModelingElementsBase: 
		"""
		pass

	@property
	def InputFields(self) -> IFieldManager:
		"""No Description

		Returns:
			IModelingElementsBase: 
		"""
		pass

class IGeometryUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GeometryUnit(self) -> IUnit:
		"""No Description

		Returns:
			IGeometryUnits: 
		"""
		pass

class IScenarioOptions(Generic[TUnitsType], IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> TUnitsType:
		"""No Description

		Returns:
			IScenarioOptions: 
		"""
		pass

class IScenarios(Generic[TElementManagerType, TElementType, TScenarioOptionsType, TScenarioOptionsUnitsType], IModelingElementsBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Create(self, parentID: int) -> TElementType:
		"""No Description

		Args:
			parentID(int): parentID

		Returns:
			TElementType: 
		"""
		pass

	def ChildrenOfElement(self, parentID: int) -> List[TElementType]:
		"""No Description

		Args:
			parentID(int): parentID

		Returns:
			List[TElementType]: 
		"""
		pass

	def BaseElements(self) -> List[TElementType]:
		"""No Description

		Returns:
			List[TElementType]: 
		"""
		pass

	@overload
	def Create(self) -> TElementType:
		"""No Description

		Returns:
			TElementType: 
		"""
		pass

	@property
	def ActiveScenario(self) -> TElementType:
		"""No Description

		Returns:
			IScenarios: 
		"""
		pass

class IScenario(Generic[TElementManagerType, TElementType, TScenarioOptionsType, TScenarioOptionsUnitsType], IModelingElementBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TimeIndexToDateTime(self, timeStepIndex: int) -> datetime:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			datetime: 
		"""
		pass

	def TimeStepToDateTime(self, timeStepInSeconds: float) -> datetime:
		"""No Description

		Args:
			timeStepInSeconds(float): timeStepInSeconds

		Returns:
			datetime: 
		"""
		pass

	def MakeCurrent(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	def Run(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	@property
	def Options(self) -> TScenarioOptionsType:
		"""No Description

		Returns:
			IScenario: 
		"""
		pass

	@property
	def TimeStepsInSeconds(self) -> array(float):
		"""No Description

		Returns:
			IScenario: 
		"""
		pass

	@property
	def HasResults(self) -> bool:
		"""No Description

		Returns:
			IScenario: 
		"""
		pass

	@property
	def ActiveTimeStep(self) -> int:
		"""No Description

		Returns:
			IScenario: 
		"""
		pass

	@ActiveTimeStep.setter
	def ActiveTimeStep(self, activetimestep: int) -> None:
		pass

	@property
	def ParentScenario(self) -> IScenario:
		"""No Description

		Returns:
			IScenario: 
		"""
		pass

	@ParentScenario.setter
	def ParentScenario(self, parentscenario: IScenario) -> None:
		pass

class ISelectionSet(Generic[TElementManagerType, TElementType, TNetworkElementType], IModelingElementBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Get(self) -> List[int]:
		"""No Description

		Returns:
			List[int]: 
		"""
		pass

	def Elements(self) -> List[TNetworkElementType]:
		"""No Description

		Returns:
			List[TNetworkElementType]: 
		"""
		pass

	@overload
	def Set(self, ids: List[int]) -> None:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			None: 
		"""
		pass

	@overload
	def Set(self, elements: List[TNetworkElementType]) -> None:
		"""No Description

		Args:
			elements(List[TNetworkElementType]): elements

		Returns:
			None: 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns:
			ISelectionSet: 
		"""
		pass

class ISelectionSets(Generic[TElementManagerType, TElementType, TNetworkElementType], IModelingElementsBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

