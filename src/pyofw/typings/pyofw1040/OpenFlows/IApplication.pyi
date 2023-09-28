from typing import overload
from System import IntPtr

class ApplicationManagerBase(IApplicationManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	def SetApplicationManager(applicationManager: IApplicationManager) -> None:
		"""Sets a custom implementation of IApplicationManager

		Args
		--------
			applicationManager (`IApplicationManager`) :  applicationManager

		Returns
		--------
			`None` : 
		"""
		pass

	def Start(self, openUI: bool = True) -> None:
		"""Starts the application

		Args
		--------
			openUI (`bool`) :  openUI

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def SetParentFormSurrogateDelegate(self, parentFormSurrogateDelegate: ParentFormSurrogateDelegate) -> None:
		"""Sets a custom ParentFormSurrogate for the application

		Args
		--------
			parentFormSurrogateDelegate (`ParentFormSurrogateDelegate`) :  parentFormSurrogateDelegate

		Returns
		--------
			`None` : 
		"""
		pass

	def Stop(self) -> None:
		"""Stops the application.  Should be closed when application exits.

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""Provides a custom ParentFormSurrogate to use for the application
            instead of the default implementation.

		Args
		--------
			parentFormSurrgateDelegate (`ParentFormSurrogateDelegate`) :  parentFormSurrgateDelegate

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""No Description

		Returns
		--------
			`IDomainApplicationModel` : 
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""No Description

		Returns
		--------
			`HaestadParentFormModel` : 
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""No Description

		Returns
		--------
			`GraphicalParentFormUIModelBase` : 
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""No Description

		Returns
		--------
			`IParentFormSurrogate` : 
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsStarted.setter
	def IsStarted(self, isstarted: bool) -> None:
		pass

	@property
	def ExitCode(self) -> int:
		"""The exit code returned on application shutdown.

		Returns
		--------
			`int` : 
		"""
		pass

	@ExitCode.setter
	def ExitCode(self, exitcode: int) -> None:
		pass

class IParentFormSurrogate(IWin32Window, IUserInterface):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetParentWindowHandle(self, handle: IntPtr) -> None:
		"""Sets the handle of the parent window.

		Args
		--------
			handle (`IntPtr`) :  handle

		Returns
		--------
			`None` : 
		"""
		pass

class IApplicationManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Start(self, openUI: bool = True) -> None:
		"""Starts the application

		Args
		--------
			openUI (`bool`) :  If true, opens the specified parent form.  Defaults to false.

		Returns
		--------
			`None` : 
		"""
		pass

	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""Provides a custom ParentFormSurrogate to use for the application
            instead of the default implementation.

		Args
		--------
			parentFormSurrgateDelegate (`ParentFormSurrogateDelegate`) :  parentFormSurrgateDelegate

		Returns
		--------
			`None` : 
		"""
		pass

	def Stop(self) -> None:
		"""Stops the application

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""The application model for the product

		Returns
		--------
			`IDomainApplicationModel` : 
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""The parent form model for primary dialog of the application

		Returns
		--------
			`HaestadParentFormModel` : 
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""The UI Model which allows for access to virtually all features of the product.

		Returns
		--------
			`GraphicalParentFormUIModelBase` : 
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""If no parent form is in use, this is what is used in its stead.

		Returns
		--------
			`IParentFormSurrogate` : 
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""The flag that determines if the application was started yet.

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def ExitCode(self) -> int:
		"""The exit code returned on application shutdown.

		Returns
		--------
			`int` : 
		"""
		pass

