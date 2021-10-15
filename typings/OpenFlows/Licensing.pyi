from Haestad.LicensingFacade import LicenseRunStatusEnum, ProductId, LicenseStatus, ILicenseProvider
from typing import overload

class ILicenseManager(ILicenseProvider):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsInitialized(self) -> bool:
		"""No Description

		Returns:
			bool: 
		"""
		pass

	@overload
	def Initialize(self, product: ProductId, parentWindow: IntPtr) -> LicenseRunStatusEnum:
		"""No Description

		Args:
			product(ProductId): product
			parentWindow(IntPtr): parentWindow

		Returns:
			LicenseRunStatusEnum: 
		"""
		pass

	@overload
	def Initialize(self, licensedFeatureSet: ILicensedFeatureSet) -> LicenseRunStatusEnum:
		"""No Description

		Args:
			licensedFeatureSet(ILicensedFeatureSet): licensedFeatureSet

		Returns:
			LicenseRunStatusEnum: 
		"""
		pass

	def CheckLicenseState(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	def IsLicenseValid(self) -> bool:
		"""No Description

		Returns:
			bool: 
		"""
		pass

	def GetLicenseStatus(self) -> LicenseStatus:
		"""No Description

		Returns:
			LicenseStatus: 
		"""
		pass

	@property
	def LicenseRunStatus(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns:
			ILicenseManager: 
		"""
		pass

