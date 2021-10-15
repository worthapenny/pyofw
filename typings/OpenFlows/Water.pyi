from enum import Enum
from Haestad.LicensingFacade import LicenseRunStatusEnum
from typing import overload
from OpenFlows.Water.Domain import IWaterModel
from OpenFlows.Water.Support import IOpenFlowsWaterDefaults

class WaterProductLicenseType(Enum):
	WaterCAD = 1248
	WaterGEMS = 1249
	WaterOPS = 2922

class OpenFlowsWater:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	@overload
	def StartSession(product: WaterProductLicenseType) -> LicenseRunStatusEnum:
		"""No Description

		Args:
			product(WaterProductLicenseType): product

		Returns:
			LicenseRunStatusEnum: 
		"""
		pass

	@staticmethod
	@overload
	def StartSession(licensedFeatureSet: ILicensedFeatureSet) -> LicenseRunStatusEnum:
		"""No Description

		Args:
			licensedFeatureSet(ILicensedFeatureSet): licensedFeatureSet

		Returns:
			LicenseRunStatusEnum: 
		"""
		pass

	@staticmethod
	def IsValid() -> bool:
		"""No Description

		Returns:
			bool: 
		"""
		pass

	@staticmethod
	def SetMaxProjects(count: int) -> None:
		"""No Description

		Args:
			count(int): count

		Returns:
			None: 
		"""
		pass

	@staticmethod
	def Open(filename: str, openInPlace: bool = False) -> IWaterModel:
		"""No Description

		Args:
			filename(str): filename
			openInPlace(bool): openInPlace

		Returns:
			IWaterModel: 
		"""
		pass

	@staticmethod
	def GetModel(project: IProject) -> IWaterModel:
		"""No Description

		Args:
			project(IProject): project

		Returns:
			IWaterModel: 
		"""
		pass

	@staticmethod
	def EndSession() -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

	@staticmethod
	@property
	def Options() -> IOpenFlowsWaterDefaults:
		"""No Description

		Returns:
			OpenFlowsWater: 
		"""
		pass

