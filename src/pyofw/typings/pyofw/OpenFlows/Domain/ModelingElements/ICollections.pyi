from OpenFlows.Domain.IModelingElements import TUnitsType, IElementUnits
from typing import List, Generic, Iterator, TypeVar
from Haestad.Support.ISupport import SortContextCollection, FilterContextCollection
from OpenFlows.Domain.ModelingElements.ISupport import IFieldManager

TCollectionType = TypeVar("TCollectionType")
TElementType = TypeVar("TElementType")

class ICollectionElements(Generic[TCollectionType, TElementType, TUnitsType]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Get(self) -> TCollectionType:
		"""Returns the collection data.

		Returns
		--------
			`TCollectionType` : 
		"""
		pass

	def Set(self, collection: TCollectionType) -> None:
		"""No Description

		Args
		--------
			collection (`TCollectionType`) :  collection

		Returns
		--------
			`None` : 
		"""
		pass

	def SelectElements(self, sorts: SortContextCollection, filters: FilterContextCollection) -> List[TElementType]:
		"""Applies a sort and/or filter against the collection and returns the matching elements.

		Args
		--------
			sorts (`SortContextCollection`) :  Sorts on a field in either ascending or descending order
			filters (`FilterContextCollection`) :  Filters the collection on one or more fields

		Returns
		--------
			`List[TElementType]` :  containing matching elements for the provided criteria.
		"""
		pass

	@property
	def Count(self) -> int:
		"""The number of items in the collection stored in the model.

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""Gets the field units for the collection to modify.

		Returns
		--------
			`TUnitsType` : 
		"""
		pass

class IResultCollectionElements(Generic[TCollectionType, TElementType, TUnitsType]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Get(self) -> TCollectionType:
		"""Gets the results collection

		Returns
		--------
			`TCollectionType` : 
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""The units that are used with the results collection

		Returns
		--------
			`TUnitsType` : 
		"""
		pass

class ICollectionElement:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICollection(Generic[TElementType], Iterator[TElementType]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self) -> TElementType:
		"""Creates a new item, adds it to the collection and returns the object.

		Returns
		--------
			`TElementType` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""Removes the System.Collections.Generic.IList`1 item at the specified index.

		Args
		--------
			index (`int`) :  The zero-based index of the item to remove.

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: TElementType) -> bool:
		"""No Description

		Args
		--------
			item (`TElementType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def Clear(self) -> None:
		"""Removes all items from the collection.

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Item(self) -> TElementType:
		"""No Description

		Returns
		--------
			`TElementType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: TElementType) -> None:
		pass

	@property
	def Count(self) -> int:
		"""Gets the number of elements contained in the System.Collections.Generic.ICollection`1.

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Fields(self) -> IFieldManager:
		"""Gets the fields for this collection

		Returns
		--------
			`IFieldManager` : 
		"""
		pass

class IResultCollection(Generic[TElementType], Iterator[TElementType]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AsReadOnly(self) -> ReadOnlyCollection[TElementType]:
		"""Returns a ReadOnlyColection containing the elements in the collection

		Returns
		--------
			`ReadOnlyCollection` : 
		"""
		pass

	@property
	def Item(self) -> TElementType:
		"""No Description

		Returns
		--------
			`TElementType` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""The number of items in the collection

		Returns
		--------
			`int` : 
		"""
		pass

