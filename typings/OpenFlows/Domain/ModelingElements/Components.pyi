from OpenFlows.Domain.ModelingElements import TElementTypeEnum, IElement, IModelingElementsBase, TElementManagerType, IElementUnits, IModelingElementBase
from typing import List, Generic, TypeVar
from enum import Enum

TElementType = TypeVar("TElementType", IElement)
TUnitsType = TypeVar("TUnitsType", IElementUnits)

class IModelComponents(Generic[TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TElementTypeEnum:
		"""No Description

		Args:
			id(int): id

		Returns:
			TElementTypeEnum: 
		"""
		pass

	def Elements(self) -> List[TElementType]:
		"""No Description

		Returns:
			List[TElementType]: 
		"""
		pass

class IComponentElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementsBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementBase[TElementManagerType, TElementType, TElementTypeEnum]):

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
			IComponentElement: 
		"""
		pass

