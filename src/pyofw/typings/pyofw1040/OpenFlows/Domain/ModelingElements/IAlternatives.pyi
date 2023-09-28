from OpenFlows.Domain.IModelingElements import IModelingElementsBase, IElements, IElement, IElementUnits, IElementInput, IModelingElementBase, IElementManager
from typing import Generic, TypeVar
from enum import Enum
from Haestad.Support.ISupport import IEditLabeled, ILabeled

TAlternativeManagerType = TypeVar("TAlternativeManagerType")
TAlternativeElementType = TypeVar("TAlternativeElementType")
TAlternativeTypeEnum = TypeVar("TAlternativeTypeEnum")
TAlternativeUnitsType = TypeVar("TAlternativeUnitsType")
TSystemAlternativeType = TypeVar("TSystemAlternativeType")

class IAlternativeElements(Generic[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum, TAlternativeUnitsType, TSystemAlternativeType], IModelingElementsBase[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAlternativeElement(Generic[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum, TAlternativeUnitsType, TSystemAlternativeType], IModelingElementBase[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeType(self) -> TAlternativeTypeEnum:
		"""The type of alternative element.

		Returns
		--------
			`TAlternativeTypeEnum` : 
		"""
		pass

	@property
	def System(self) -> TSystemAlternativeType:
		"""Access to system alternative properties for this alternative

		Returns
		--------
			`TSystemAlternativeType` : 
		"""
		pass

	@property
	def Units(self) -> TAlternativeUnitsType:
		"""Access the units for this alternative

		Returns
		--------
			`TAlternativeUnitsType` : 
		"""
		pass

