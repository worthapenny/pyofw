from array import array
from typing import Iterator, Dict, List
from System import ICloneable

class DictionaryEntry:

	def __init__(self, key: object, value: object) -> None:
		"""No Description

		Args
		--------
			key (``object``) :  key
			value (``object``) :  value
		"""
		pass

	@property
	def Key(self) -> object:
		"""No Description

		Returns
		--------
			``DictionaryEntry`` : 
		"""
		pass

	@Key.setter
	def Key(self, key: object) -> None:
		pass

	@property
	def Value(self) -> object:
		"""No Description

		Returns
		--------
			``DictionaryEntry`` : 
		"""
		pass

	@Value.setter
	def Value(self, value: object) -> None:
		pass

class ICollection(Iterator):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CopyTo(self, array: array, index: int) -> None:
		"""No Description

		Args
		--------
			array (``array``) :  array
			index (``int``) :  index

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``ICollection`` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			``ICollection`` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			``ICollection`` : 
		"""
		pass

class IComparer:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Compare(self, x: object, y: object) -> int:
		"""No Description

		Args
		--------
			x (``object``) :  x
			y (``object``) :  y

		Returns
		--------
			``int`` : 
		"""
		pass

class IDictionaryEnumerator(IEnumerator):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Key(self) -> object:
		"""No Description

		Returns
		--------
			``IDictionaryEnumerator`` : 
		"""
		pass

	@property
	def Value(self) -> object:
		"""No Description

		Returns
		--------
			``IDictionaryEnumerator`` : 
		"""
		pass

	@property
	def Entry(self) -> DictionaryEntry:
		"""No Description

		Returns
		--------
			``IDictionaryEnumerator`` : 
		"""
		pass

class IEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> object:
		"""No Description

		Returns
		--------
			``IEnumerator`` : 
		"""
		pass

class SortedList(Dict, ICloneable):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			initialCapacity (``int``) :  initialCapacity
			comparer (``IComparer``) :  comparer
			comparer (``IComparer``) :  comparer
			capacity (``int``) :  capacity
			d (``Dict``) :  d
			d (``Dict``) :  d
			comparer (``IComparer``) :  comparer
		"""
		pass

	@overload
	def __init__(self, initialCapacity: int) -> None:
		"""No Description

		Args
		--------
			initialCapacity (``int``) :  initialCapacity
			comparer (``IComparer``) :  comparer
			comparer (``IComparer``) :  comparer
			capacity (``int``) :  capacity
			d (``Dict``) :  d
			d (``Dict``) :  d
			comparer (``IComparer``) :  comparer
		"""
		pass

	@overload
	def __init__(self, comparer: IComparer) -> None:
		"""No Description

		Args
		--------
			initialCapacity (``int``) :  initialCapacity
			comparer (``IComparer``) :  comparer
			comparer (``IComparer``) :  comparer
			capacity (``int``) :  capacity
			d (``Dict``) :  d
			d (``Dict``) :  d
			comparer (``IComparer``) :  comparer
		"""
		pass

	@overload
	def __init__(self, comparer: IComparer, capacity: int) -> None:
		"""No Description

		Args
		--------
			initialCapacity (``int``) :  initialCapacity
			comparer (``IComparer``) :  comparer
			comparer (``IComparer``) :  comparer
			capacity (``int``) :  capacity
			d (``Dict``) :  d
			d (``Dict``) :  d
			comparer (``IComparer``) :  comparer
		"""
		pass

	@overload
	def __init__(self, d: Dict) -> None:
		"""No Description

		Args
		--------
			initialCapacity (``int``) :  initialCapacity
			comparer (``IComparer``) :  comparer
			comparer (``IComparer``) :  comparer
			capacity (``int``) :  capacity
			d (``Dict``) :  d
			d (``Dict``) :  d
			comparer (``IComparer``) :  comparer
		"""
		pass

	@overload
	def __init__(self, d: Dict, comparer: IComparer) -> None:
		"""No Description

		Args
		--------
			initialCapacity (``int``) :  initialCapacity
			comparer (``IComparer``) :  comparer
			comparer (``IComparer``) :  comparer
			capacity (``int``) :  capacity
			d (``Dict``) :  d
			d (``Dict``) :  d
			comparer (``IComparer``) :  comparer
		"""
		pass

	def Add(self, key: object, value: object) -> None:
		"""No Description

		Args
		--------
			key (``object``) :  key
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

	def Contains(self, key: object) -> bool:
		"""No Description

		Args
		--------
			key (``object``) :  key

		Returns
		--------
			``bool`` : 
		"""
		pass

	def ContainsKey(self, key: object) -> bool:
		"""No Description

		Args
		--------
			key (``object``) :  key

		Returns
		--------
			``bool`` : 
		"""
		pass

	def ContainsValue(self, value: object) -> bool:
		"""No Description

		Args
		--------
			value (``object``) :  value

		Returns
		--------
			``bool`` : 
		"""
		pass

	def CopyTo(self, array: array, arrayIndex: int) -> None:
		"""No Description

		Args
		--------
			array (``array``) :  array
			arrayIndex (``int``) :  arrayIndex

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetByIndex(self, index: int) -> object:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``object`` : 
		"""
		pass

	def GetEnumerator(self) -> IDictionaryEnumerator:
		"""No Description

		Returns
		--------
			``IDictionaryEnumerator`` : 
		"""
		pass

	def GetKey(self, index: int) -> object:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``object`` : 
		"""
		pass

	def GetKeyList(self) -> List:
		"""No Description

		Returns
		--------
			``List`` : 
		"""
		pass

	def GetValueList(self) -> List:
		"""No Description

		Returns
		--------
			``List`` : 
		"""
		pass

	def IndexOfKey(self, key: object) -> int:
		"""No Description

		Args
		--------
			key (``object``) :  key

		Returns
		--------
			``int`` : 
		"""
		pass

	def IndexOfValue(self, value: object) -> int:
		"""No Description

		Args
		--------
			value (``object``) :  value

		Returns
		--------
			``int`` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``None`` : 
		"""
		pass

	def Remove(self, key: object) -> None:
		"""No Description

		Args
		--------
			key (``object``) :  key

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetByIndex(self, index: int, value: object) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@staticmethod
	def Synchronized(list: SortedList) -> SortedList:
		"""No Description

		Args
		--------
			list (``SortedList``) :  list

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@property
	def Keys(self) -> ICollection:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@property
	def Values(self) -> ICollection:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@property
	def Item(self) -> object:
		"""No Description

		Returns
		--------
			``SortedList`` : 
		"""
		pass

	@Item.setter
	def Item(self, item: object) -> None:
		pass

