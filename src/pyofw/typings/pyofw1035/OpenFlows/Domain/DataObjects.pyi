from Haestad.Domain import IDomainDataSet
from datetime import datetime

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

