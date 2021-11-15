from Haestad.Domain import IDomainDataSet
from datetime import datetime
from typing import overload, Generic, List, TypeVar
from OpenFlows.Domain.ModelingElements import IModelingElementBase, IModelingElementsBase, IElement, ModelElementType, ISelectionSets, ISelectionSet, IScenarios, IScenario, IScenarioOptions, IElementUnits
from OpenFlows.Domain.ModelingElements.Support import TNetworkElementTypeEnum, IUserFieldManager
from OpenFlows.Domain.ModelingElements.NetworkElements import ElementStateType
from enum import Enum
from OpenFlows.Units import IModelUnits, TNetworkUnitsType, TComponentUnitsType, INetworkUnits, IComponentUnits
from OpenFlows.Domain.ModelingElements.Components import IModelComponents

TScenarioManagerType = TypeVar("TScenarioManagerType", IModelingElementsBase)
TScenarioType = TypeVar("TScenarioType", IModelingElementBase)
TNetworkElementType = TypeVar("TNetworkElementType", IElement)
TSelectionSetsType = TypeVar("TSelectionSetsType", ISelectionSets)
TSelectionSetElementType = TypeVar("TSelectionSetElementType", ISelectionSet)
TSelectionSetNetworkElementType = TypeVar("TSelectionSetNetworkElementType", IElement)
TNetworkType = TypeVar("TNetworkType", INetwork)
TModelComponentsType = TypeVar("TModelComponentsType", IModelComponents)
TScenarioOptionsType = TypeVar("TScenarioOptionsType", IScenarioOptions)
TScenarioOptionsUnitsType = TypeVar("TScenarioOptionsUnitsType", IElementUnits)
TComponentElementType = TypeVar("TComponentElementType", IElement)
TComponentElementTypeEnum = TypeVar("TComponentElementTypeEnum", Enum)
TModelType = TypeVar("TModelType", IModel)

class IDomainModel:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsQuerySelectionSet(self, id: int) -> bool:
		"""Determines if a selection set is query-based.

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""The DomainDataSet for the current model to allow for advanced API usage.

		Returns
		--------
			``IDomainModel`` : 
		"""
		pass

class IModelInfo:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Filename(self) -> str:
		"""The full path and filename of the model

		Returns
		--------
			``IModelInfo`` : 
		"""
		pass

	@property
	def Date(self) -> datetime:
		"""The project date

		Returns
		--------
			``IModelInfo`` : 
		"""
		pass

	@property
	def Title(self) -> str:
		"""The project title

		Returns
		--------
			``IModelInfo`` : 
		"""
		pass

	@property
	def Company(self) -> str:
		"""The company creating the model

		Returns
		--------
			``IModelInfo`` : 
		"""
		pass

	@property
	def Engineer(self) -> str:
		"""The project engineer for the model

		Returns
		--------
			``IModelInfo`` : 
		"""
		pass

	@property
	def Notes(self) -> str:
		"""Any notes about the model.

		Returns
		--------
			``IModelInfo`` : 
		"""
		pass

class IModelIOOperations:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Save(self) -> None:
		"""Saves the model from the temporary location back to the original location.
            Only the SQLite database is copied.

		Returns
		--------
			``None`` : 
		"""
		pass

	def SaveAs(self, filename: str) -> None:
		"""Saves the model to the specified location.

		Args
		--------
			filename (``str``) :  The full path and filename of the project.

		Returns
		--------
			``None`` : 
		"""
		pass

	def Close(self) -> None:
		"""Closes the model.

		Returns
		--------
			``None`` : 
		"""
		pass

class IModelScenarioManagement(Generic[TScenarioManagerType, TScenarioType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def SetActiveScenario(self, scenarioID: int) -> None:
		"""Sets the scenario as active.

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def SetActiveScenario(self, scenario: TScenarioType) -> None:
		"""No Description

		Args
		--------
			scenario (``TScenarioType``) :  scenario

		Returns
		--------
			``None`` : 
		"""
		pass

	def RunActiveScenario(self) -> None:
		"""Calculates the active scenario using the current set of alternatives and calculation options assigned to the scenario

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Scenarios(self) -> TScenarioManagerType:
		"""A list of scenarios in the model.

		Returns
		--------
			``IModelScenarioManagement`` : 
		"""
		pass

	@property
	def ActiveScenario(self) -> TScenarioType:
		"""The currently active scenario.

		Returns
		--------
			``IModelScenarioManagement`` : 
		"""
		pass

class INetwork(Generic[TNetworkElementType, TNetworkElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TNetworkElementTypeEnum:
		"""Gets the element type of the given ID

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``TNetworkElementTypeEnum`` : 
		"""
		pass

	def Elements(self, state: ElementStateType = ElementStateType.All) -> List[TNetworkElementType]:
		"""Returns a list of all domain elements in the model.

		Args
		--------
			state (``ElementStateType``) :  state

		Returns
		--------
			``List[TNetworkElementType]`` : 
		"""
		pass

class IModelElementManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Element(self, id: int) -> IElement:
		"""Gets an element for the given iD.  Returns null if the id does not exist.

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``IElement`` : 
		"""
		pass

	def NetworkElements(self, label: str, useWildcard: bool = False) -> List[IElement]:
		"""Gets a list of domain elements that has the given label.

		Args
		--------
			label (``str``) :  The label to search for
			useWildcard (``bool``) :  Specifies whether or not the label contains wildcards.  Defaults to false.

		Returns
		--------
			``List[IElement]`` : A list of elements that use the label.  May be empty but never null.
		"""
		pass

	def ModelElementType(self, id: int) -> ModelElementType:
		"""Gets the type of model element type of the id, if it exists.

		Args
		--------
			id (``int``) :  The id of the element

		Returns
		--------
			``ModelElementType`` : If the id does not exist, throws exception.  Otherwise, returns the model element type.
		"""
		pass

	def Delete(self, id: int) -> bool:
		"""Deletes the element of the given id.

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Exists(self, id: int) -> bool:
		"""Determines if the id is valid and it exists in the model.

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IsLink(self, id: int) -> bool:
		"""Determines if the provided id is a link.

		Args
		--------
			id (``int``) :  The ID of the element.

		Returns
		--------
			``bool`` : True if the ID is a link, otherwise false
		"""
		pass

	def IsNode(self, id: int) -> bool:
		"""Determines if the provided id is a node.

		Args
		--------
			id (``int``) :  The ID of the element.

		Returns
		--------
			``bool`` : True if the ID is a node, otherwise false.
		"""
		pass

	def IsPolygon(self, id: int) -> bool:
		"""Determines if the provided is a polygon.

		Args
		--------
			id (``int``) :  The ID of the element.

		Returns
		--------
			``bool`` : True if the id is a polygon, otherwise false.
		"""
		pass

	def NextNetworkElementLabel(self, domainElementType: int) -> str:
		"""Gets the next label for the element type.

		Args
		--------
			domainElementType (``int``) :  The type of network element

		Returns
		--------
			``str`` : 
		"""
		pass

class IModelSelectionSetManagement(Generic[TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SelectionSets(self) -> TSelectionSetsType:
		"""A list of selection sets in the model.

		Returns
		--------
			``IModelSelectionSetManagement`` : 
		"""
		pass

class IModel(Generic[TNetworkType, TModelComponentsType, TScenarioManagerType, TScenarioType, TScenarioOptionsType, TScenarioOptionsUnitsType, TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType, TNetworkElementType, TNetworkElementTypeEnum, TComponentElementType, TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType], IModelElementManager, IModelIOOperations, IModelUnits[TNetworkUnitsType, TComponentUnitsType], IModelScenarioManagement[TScenarioManagerType, TScenarioType], IDomainModel, IModelSelectionSetManagement[TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def NextNetworkElementLabel(self, domainElementType: TNetworkElementTypeEnum) -> str:
		"""No Description

		Args
		--------
			domainElementType (``TNetworkElementTypeEnum``) :  domainElementType

		Returns
		--------
			``str`` : 
		"""
		pass

	@overload
	def NextNetworkElementLabel(self, domainElementType: int) -> str:
		"""Gets the next label for the element type.

		Args
		--------
			domainElementType (``int``) :  The type of network element

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def Network(self) -> TNetworkType:
		"""The network elements in the model.

		Returns
		--------
			``IModel`` : 
		"""
		pass

	@property
	def Components(self) -> TModelComponentsType:
		"""The supporting objects in the model like selection sets and patterns.

		Returns
		--------
			``IModel`` : 
		"""
		pass

	@property
	def ModelInfo(self) -> IModelInfo:
		"""Basic information about the model.

		Returns
		--------
			``IModel`` : 
		"""
		pass

	@property
	def UserFieldManager(self) -> IUserFieldManager[TNetworkElementTypeEnum]:
		"""Provides a way to create custom fields in the current model.

		Returns
		--------
			``IModel`` : 
		"""
		pass

class IOpenFlows(Generic[TNetworkType, TModelType, TModelComponentsType, TScenarioManagerType, TScenarioType, TScenarioOptionsType, TScenarioOptionsUnitsType, TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType, TNetworkElementType, TNetworkElementTypeEnum, TComponentElementType, TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Open(self, filename: str, openInPlace: bool = False) -> TModelType:
		"""Opens a model at the given location

		Args
		--------
			filename (``str``) :  The full path and filename ending in wtg.  The wtg and any support files are automatically copied to the temp folder.
			openInPlace (``bool``) :  An option to open the specified project in its original location and not make a copy in the temp folder.

		Returns
		--------
			``TModelType`` : A model object representing the data in the specified file.
		"""
		pass

	@overload
	def Open(self, project: IProject) -> TModelType:
		"""that wrappers a Framework-managed IProject

		Args
		--------
			project (``IProject``) :  project

		Returns
		--------
			``TModelType`` : 
		"""
		pass

