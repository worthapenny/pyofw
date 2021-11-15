from OpenFlows.Domain.ModelingElements import TElementTypeEnum, IElement, IModelingElementsBase, TElementManagerType, IElementUnits, IModelingElementBase, IElements, IElementManager
from typing import List, Generic, TypeVar
from enum import Enum
from Haestad.Support.Support import IEditLabeled, ILabeled

TElementType = TypeVar("TElementType", IElement)
TUnitsType = TypeVar("TUnitsType", IElementUnits)

class IModelComponents(Generic[TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TElementTypeEnum:
		"""Gets type of element for the given id.

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``TElementTypeEnum`` : 
		"""
		pass

	def Elements(self) -> List[TElementType]:
		"""Returns a list of all support elements in the model.

		Returns
		--------
			``List[TElementType]`` : 
		"""
		pass

class IComponentElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementsBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementBase[TElementManagerType, TElementType, TElementTypeEnum]):

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
		"""Provides easy access to this element's field formatters.

		Returns
		--------
			``IComponentElement`` : 
		"""
		pass

