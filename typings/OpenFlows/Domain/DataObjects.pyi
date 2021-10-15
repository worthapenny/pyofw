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


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsQuerySelectionSet(self, id: int) -> bool:
		"""No Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns:
			IDomainModel: 
		"""
		pass

class IModelInfo:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Filename(self) -> str:
		"""No Description

		Returns:
			IModelInfo: 
		"""
		pass

	@property
	def Date(self) -> datetime:
		"""No Description

		Returns:
			IModelInfo: 
		"""
		pass

	@property
	def Title(self) -> str:
		"""No Description

		Returns:
			IModelInfo: 
		"""
		pass

	@property
	def Company(self) -> str:
		"""No Description

		Returns:
			IModelInfo: 
		"""
		pass

	@property
	def Engineer(self) -> str:
		"""No Description

		Returns:
			IModelInfo: 
		"""
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns:
			IModelInfo: 
		"""
		pass

class IModelIOOperations:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Save(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	def SaveAs(self, filename: str) -> None:
		"""No Description

		Args:
			filename(str): filename

		Returns:
			None: 
		"""
		pass

	def Close(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

class IModelScenarioManagement(Generic[TScenarioManagerType, TScenarioType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def SetActiveScenario(self, scenarioID: int) -> None:
		"""No Description

		Args:
			scenarioID(int): scenarioID

		Returns:
			None: 
		"""
		pass

	@overload
	def SetActiveScenario(self, scenario: TScenarioType) -> None:
		"""No Description

		Args:
			scenario(TScenarioType): scenario

		Returns:
			None: 
		"""
		pass

	def RunActiveScenario(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	@property
	def Scenarios(self) -> TScenarioManagerType:
		"""No Description

		Returns:
			IModelScenarioManagement: 
		"""
		pass

	@property
	def ActiveScenario(self) -> TScenarioType:
		"""No Description

		Returns:
			IModelScenarioManagement: 
		"""
		pass

class INetwork(Generic[TNetworkElementType, TNetworkElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TNetworkElementTypeEnum:
		"""No Description

		Args:
			id(int): id

		Returns:
			TNetworkElementTypeEnum: 
		"""
		pass

	def Elements(self, state: ElementStateType = ElementStateType.All) -> List[TNetworkElementType]:
		"""No Description

		Args:
			state(ElementStateType): state

		Returns:
			List[TNetworkElementType]: 
		"""
		pass

class IModelElementManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Element(self, id: int) -> IElement:
		"""No Description

		Args:
			id(int): id

		Returns:
			IElement: 
		"""
		pass

	def NetworkElements(self, label: str, useWildcard: bool = False) -> List[IElement]:
		"""No Description

		Args:
			label(str): label
			useWildcard(bool): useWildcard

		Returns:
			List[IElement]: 
		"""
		pass

	def ModelElementType(self, id: int) -> ModelElementType:
		"""No Description

		Args:
			id(int): id

		Returns:
			ModelElementType: 
		"""
		pass

	def Delete(self, id: int) -> bool:
		"""No Description

		Args:
			id(int): id

		Returns:
			bool: 
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

	def IsLink(self, id: int) -> bool:
		"""No Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	def IsNode(self, id: int) -> bool:
		"""No Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	def IsPolygon(self, id: int) -> bool:
		"""No Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	def NextNetworkElementLabel(self, domainElementType: int) -> str:
		"""No Description

		Args:
			domainElementType(int): domainElementType

		Returns:
			str: 
		"""
		pass

class IModelSelectionSetManagement(Generic[TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SelectionSets(self) -> TSelectionSetsType:
		"""No Description

		Returns:
			IModelSelectionSetManagement: 
		"""
		pass

class IModel(Generic[TNetworkType, TModelComponentsType, TScenarioManagerType, TScenarioType, TScenarioOptionsType, TScenarioOptionsUnitsType, TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType, TNetworkElementType, TNetworkElementTypeEnum, TComponentElementType, TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType], IModelElementManager, IModelIOOperations, IModelUnits[TNetworkUnitsType, TComponentUnitsType], IModelScenarioManagement[TScenarioManagerType, TScenarioType], IDomainModel, IModelSelectionSetManagement[TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def NextNetworkElementLabel(self, domainElementType: TNetworkElementTypeEnum) -> str:
		"""No Description

		Args:
			domainElementType(TNetworkElementTypeEnum): domainElementType

		Returns:
			str: 
		"""
		pass

	@overload
	def NextNetworkElementLabel(self, domainElementType: int) -> str:
		"""No Description

		Args:
			domainElementType(int): domainElementType

		Returns:
			str: 
		"""
		pass

	@property
	def Network(self) -> TNetworkType:
		"""No Description

		Returns:
			IModel: 
		"""
		pass

	@property
	def Components(self) -> TModelComponentsType:
		"""No Description

		Returns:
			IModel: 
		"""
		pass

	@property
	def ModelInfo(self) -> IModelInfo:
		"""No Description

		Returns:
			IModel: 
		"""
		pass

	@property
	def UserFieldManager(self) -> IUserFieldManager:
		"""No Description

		Returns:
			IModel: 
		"""
		pass

class IOpenFlows(Generic[TNetworkType, TModelType, TModelComponentsType, TScenarioManagerType, TScenarioType, TScenarioOptionsType, TScenarioOptionsUnitsType, TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType, TNetworkElementType, TNetworkElementTypeEnum, TComponentElementType, TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Open(self, filename: str, openInPlace: bool = False) -> TModelType:
		"""No Description

		Args:
			filename(str): filename
			openInPlace(bool): openInPlace

		Returns:
			TModelType: 
		"""
		pass

	@overload
	def Open(self, project: IProject) -> TModelType:
		"""No Description

		Args:
			project(IProject): project

		Returns:
			TModelType: 
		"""
		pass

