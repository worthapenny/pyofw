from enum import Enum
from System import TypeCode
from typing import List, Dict, Generic, overload, TypeVar
from Haestad.Support.Support import SortContextCollection, FilterContextCollection, IEditLabeled, ILabeled
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


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementIDs(self) -> List[int]:
		"""The list of IDs for each element in the manager.

		Returns
		--------
			``List[int]`` : 
		"""
		pass

	def Exists(self, id: int) -> bool:
		"""Determines if the ID exists.

		Args
		--------
			id (``int``) :  A valid ID of 0 or greater.

		Returns
		--------
			``bool`` : True if the ID exists, otherwise false.
		"""
		pass

	def Labels(self) -> Dict[int,int]:
		"""Returns all the labels for this element manager keyed by element id.

		Returns
		--------
			``Dict[int,int]`` : A dictionary keyed by element id with the value of the element label
		"""
		pass

	@property
	def Count(self) -> int:
		"""The number of elements in the manager.

		Returns
		--------
			``IElementManager`` : 
		"""
		pass

class IElements(Generic[TElementType], IElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Elements(self) -> List[TElementType]:
		"""A list of all elements in the manager.

		Returns
		--------
			``List[TElementType]`` : 
		"""
		pass

	def SelectElements(self, sorts: SortContextCollection, filters: FilterContextCollection) -> List[TElementType]:
		"""Selects a set of elements given the criteria.

		Args
		--------
			sorts (``SortContextCollection``) :  Sorts the list based on one or more fields in ascending or descending order
			filters (``FilterContextCollection``) :  A list of filters against IFields or a provided SQL statement

		Returns
		--------
			``List[TElementType]`` : A list of elements that match the provided criteria.  If no elements found, returns an empty List
		"""
		pass

class IElement(IEditLabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Id(self) -> int:
		"""The ID of the element.

		Returns
		--------
			``IElement`` : 
		"""
		pass

	@property
	def Notes(self) -> str:
		"""User specified notes about the element.

		Returns
		--------
			``IElement`` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def ModelElementType(self) -> ModelElementType:
		"""The type of basic element

		Returns
		--------
			``IElement`` : 
		"""
		pass

class IElementUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElementInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InputFields(self) -> IFieldManager:
		"""Access to fields for this element.

		Returns
		--------
			``IElementInput`` : 
		"""
		pass

class IElementsInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElementResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ResultFields(self) -> IFieldManager:
		"""Access to result fields for this element.

		Returns
		--------
			``IElementResults`` : 
		"""
		pass

class IElementsResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IModelingElementBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Delete(self) -> None:
		"""Deletes the modeling element from the data source.

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Manager(self) -> TElementManagerType:
		"""The element's manager.

		Returns
		--------
			``IModelingElementBase`` : 
		"""
		pass

	@property
	def ElementType(self) -> TElementTypeEnum:
		"""The type of element this object represents.

		Returns
		--------
			``IModelingElementBase`` : 
		"""
		pass

class IModelingElementsBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElements[TElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Create(self) -> TElementType:
		"""Creates a new element and returns the object.

		Returns
		--------
			``TElementType`` : Returns a non-null object with minimally initialized properties.
		"""
		pass

	@overload
	def Element(self, id: int) -> TElementType:
		"""Retrieves an element given the ID.

		Args
		--------
			id (``int``) :  The non-0 ID of the element.

		Returns
		--------
			``TElementType`` : A  non-null object representing the element of the given ID.  If the ID does not exist, returns null.
		"""
		pass

	@overload
	def Element(self, label: str) -> TElementType:
		"""Returns the first element that matches the given label.  If not found, returns null.

		Args
		--------
			label (``str``) :  label

		Returns
		--------
			``TElementType`` : 
		"""
		pass

	@overload
	def Elements(self, label: str) -> List[TElementType]:
		"""Returns a list of elements with the given label.

		Args
		--------
			label (``str``) :  Case-sensitive label to search for

		Returns
		--------
			``List[TElementType]`` : A non-null list containing 0 or more elements with the given label
		"""
		pass

	@overload
	def Elements(self) -> List[TElementType]:
		"""No Description

		Returns
		--------
			``List[TElementType]`` : 
		"""
		pass

	@property
	def ElementType(self) -> TElementTypeEnum:
		"""The elementTypeID of the domain element

		Returns
		--------
			``IModelingElementsBase`` : 
		"""
		pass

	@property
	def InputFields(self) -> IFieldManager:
		"""Access to input fields for this manager

		Returns
		--------
			``IModelingElementsBase`` : 
		"""
		pass

class IGeometryUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GeometryUnit(self) -> IUnit:
		"""The formatter name for the geometry of the element.

		Returns
		--------
			``IGeometryUnits`` : 
		"""
		pass

class IScenarioOptions(Generic[TUnitsType], IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> TUnitsType:
		"""Access to unit information for properties in scenario options.

		Returns
		--------
			``IScenarioOptions`` : 
		"""
		pass

class IScenarios(Generic[TElementManagerType, TElementType, TScenarioOptionsType, TScenarioOptionsUnitsType], IModelingElementsBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Create(self, parentID: int) -> TElementType:
		"""Creates a new scenario.  If parentID is non-0, creates a child of that ID.  Otherwise creates a base scenario

		Args
		--------
			parentID (``int``) :  parentID

		Returns
		--------
			``TElementType`` : 
		"""
		pass

	def ChildrenOfElement(self, parentID: int) -> List[TElementType]:
		"""Returns a list of scenarios that have the given parent ID

		Args
		--------
			parentID (``int``) :  parentID

		Returns
		--------
			``List[TElementType]`` : 
		"""
		pass

	def BaseElements(self) -> List[TElementType]:
		"""Returns a list of base scenarios

		Returns
		--------
			``List[TElementType]`` : 
		"""
		pass

	@overload
	def Create(self) -> TElementType:
		"""No Description

		Returns
		--------
			``TElementType`` : 
		"""
		pass

	@property
	def ActiveScenario(self) -> TElementType:
		"""Gets the currently active scenario

		Returns
		--------
			``IScenarios`` : 
		"""
		pass

class IScenario(Generic[TElementManagerType, TElementType, TScenarioOptionsType, TScenarioOptionsUnitsType], IModelingElementBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TimeIndexToDateTime(self, timeStepIndex: int) -> datetime:
		"""Converts the time at the given time step to a DateTime taking into account
            the start date and time in the scenario options.

		Args
		--------
			timeStepIndex (``int``) :  Th time step index to use with TimeStepsInSeconds.

		Returns
		--------
			``datetime`` : The DateTime at the given time step index taking into account the start date/time of the simulation.
		"""
		pass

	def TimeStepToDateTime(self, timeStepInSeconds: float) -> datetime:
		"""Converts the given time in seconds to a date-time.

		Args
		--------
			timeStepInSeconds (``float``) :  The time step in seconds.

		Returns
		--------
			``datetime`` : A date-time object representing the time step taking into account the simulation start date and time.
		"""
		pass

	def MakeCurrent(self) -> None:
		"""Makes this scenario the active scenario in the model.

		Returns
		--------
			``None`` : 
		"""
		pass

	def Run(self) -> None:
		"""Runs the active solver for this scenario

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Options(self) -> TScenarioOptionsType:
		"""A set of calculation options for the scenario.

		Returns
		--------
			``IScenario`` : 
		"""
		pass

	@property
	def TimeStepsInSeconds(self) -> array[float]:
		"""The list of time steps, in seconds, for the scenario if results are available.  Returns an empty array if no results are available.

		Returns
		--------
			``IScenario`` : 
		"""
		pass

	@property
	def HasResults(self) -> bool:
		"""Determines if results are available.

		Returns
		--------
			``IScenario`` : 
		"""
		pass

	@property
	def ActiveTimeStep(self) -> int:
		"""The active time step index for this scenario

		Returns
		--------
			``IScenario`` : 
		"""
		pass

	@ActiveTimeStep.setter
	def ActiveTimeStep(self, activetimestep: int) -> None:
		pass

	@property
	def ParentScenario(self) -> IScenario[TElementManagerType,TElementType,TScenarioOptionsType,TScenarioOptionsUnitsType]:
		"""Gets a parent if not a base scenario.  Assigns a parent if not null.  If null, sets the scenario as a base scenario

		Returns
		--------
			``IScenario`` : 
		"""
		pass

	@ParentScenario.setter
	def ParentScenario(self, parentscenario: IScenario[TElementManagerType,TElementType,TScenarioOptionsType,TScenarioOptionsUnitsType]) -> None:
		pass

class ISelectionSet(Generic[TElementManagerType, TElementType, TNetworkElementType], IModelingElementBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Get(self) -> List[int]:
		"""Gets the IDs in the selection set.

		Returns
		--------
			``List[int]`` : A non-null list of IDs in the selection set.  May include deleted IDs.
		"""
		pass

	def Elements(self) -> List[TNetworkElementType]:
		"""A list of elements representing each ID.

		Returns
		--------
			``List[TNetworkElementType]`` : A non-null list of elements representing each ID in the selection set.
		"""
		pass

	@overload
	def Set(self, ids: List[int]) -> None:
		"""No Description

		Args
		--------
			ids (``List[int]``) :  ids

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def Set(self, elements: List[TNetworkElementType]) -> None:
		"""No Description

		Args
		--------
			elements (``List[TNetworkElementType]``) :  elements

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""The number of ids in the selection set.

		Returns
		--------
			``ISelectionSet`` : 
		"""
		pass

class ISelectionSets(Generic[TElementManagerType, TElementType, TNetworkElementType], IModelingElementsBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

