from enum import Enum
from System import TypeCode
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


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	@overload
	def StartSession(product: WaterProductLicenseType) -> LicenseRunStatusEnum:
		"""Starts a session of OpenFlows.  Must be called before opening a model.

		Args
		--------
			product (``WaterProductLicenseType``) :  product

		Returns
		--------
			``LicenseRunStatusEnum`` : 
		"""
		pass

	@staticmethod
	@overload
	def StartSession(licensedFeatureSet: ILicensedFeatureSet) -> LicenseRunStatusEnum:
		"""Starts an OpenFlows session using a Framework-managed ILicensedFeatureSet

		Args
		--------
			licensedFeatureSet (``ILicensedFeatureSet``) :  licensedFeatureSet

		Returns
		--------
			``LicenseRunStatusEnum`` : 
		"""
		pass

	@staticmethod
	def IsValid() -> bool:
		"""Checks the state of the OpenFlows session.

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def SetMaxProjects(count: int) -> None:
		"""Sets the maximum number of projects that can be opened.
            The default is 1.

		Args
		--------
			count (``int``) :  A minimum of 1 and a maximum of 5 is allowed.

		Returns
		--------
			``None`` : 
		"""
		pass

	@staticmethod
	def Open(filename: str, openInPlace: bool = False) -> IWaterModel:
		"""Opens a model using the provided filename.

		Args
		--------
			filename (``str``) :  The file to open.  Can be the project (wtg) file or the sqlite database.
			openInPlace (``bool``) :  True to open model without a copy.  Otherwise, a copy of the model is made when opened.  Save() has no effect if true.

		Returns
		--------
			``IWaterModel`` : 
		"""
		pass

	@staticmethod
	def GetModel(project: IProject) -> IWaterModel:
		"""Creates an IWaterModel given a Framework-managed project

		Args
		--------
			project (``IProject``) :  project

		Returns
		--------
			``IWaterModel`` : 
		"""
		pass

	@staticmethod
	def EndSession() -> None:
		"""If Save() was not previously called, closes the project without saving changes or results.

		Returns
		--------
			``None`` : 
		"""
		pass

	@staticmethod
	@property
	def Options() -> IOpenFlowsWaterDefaults:
		"""Configure default settings

		Returns
		--------
			``OpenFlowsWater`` : 
		"""
		pass

