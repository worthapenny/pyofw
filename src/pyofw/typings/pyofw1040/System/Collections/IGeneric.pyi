from typing import Iterator, Generic
from System import T


class IReadOnlyCollection(Generic[T], Iterator[T]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

