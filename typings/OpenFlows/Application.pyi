from typing import overload

class ApplicationManager(IApplicationManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	def GetInstance() -> IApplicationManager:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@staticmethod
	def SetApplicationManager(applicationManager: IApplicationManager) -> None:
		"""No Description

		Args:
			applicationManager(IApplicationManager): applicationManager

		Returns:
			None: 
		"""
		pass

	def Start(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	@overload
	def SetParentFormSurrogateDelegate(self, parentFormSurrogateDelegate: ParentFormSurrogateDelegate) -> None:
		"""No Description

		Args:
			parentFormSurrogateDelegate(ParentFormSurrogateDelegate): parentFormSurrogateDelegate

		Returns:
			None: 
		"""
		pass

	def Stop(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	@overload
	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""No Description

		Args:
			parentFormSurrgateDelegate(ParentFormSurrogateDelegate): parentFormSurrgateDelegate

		Returns:
			None: 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""No Description

		Returns:
			ApplicationManager: 
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""No Description

		Returns:
			ApplicationManager: 
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""No Description

		Returns:
			ApplicationManager: 
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""No Description

		Returns:
			ApplicationManager: 
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""No Description

		Returns:
			ApplicationManager: 
		"""
		pass

	@IsStarted.setter
	def IsStarted(self, isstarted: bool) -> None:
		pass

class IParentFormSurrogate(IWin32Window, IUserInterface):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetParentWindowHandle(self, handle: int) -> None:
		"""No Description

		Args:
			handle(int): handle

		Returns:
			None: 
		"""
		pass

class IApplicationManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Start(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""No Description

		Args:
			parentFormSurrgateDelegate(ParentFormSurrogateDelegate): parentFormSurrgateDelegate

		Returns:
			None: 
		"""
		pass

	def Stop(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

