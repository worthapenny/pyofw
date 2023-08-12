from enum import Enum
from typing import overload, Dict
from System import Guid, IntPtr
from datetime import datetime
from Haestad.Support.User import IMessageHandler

class LicenseRunStatusEnum(Enum):
	OK = 1001
	Limited = 1002
	Shutdown = 1003
	Unknown = -1

class LicenseStatus(Enum):
	OK = 101
	Offline = 102
	PreActivation = 104
	Expired = 105
	AccessDenied = 106
	DisabledByLogSend = 107
	DisabledByPolicy = 108
	Trial = 109
	NotEntitled = 110
	Unknown = -999
	Error = -1

class LicenseType(Enum):
	Unknown = 0
	Commercial = 1
	Academic = 2
	HomeUse = 3
	NonCommercial = 4
	Trial = 5
	FutureType2 = 6
	Temporary = 99
	Error = -1

class LicenseEventType(Enum):
	LiveUsagePostingOccured = 0
	DeferredUsagePostingOccured = 1
	UsagePostingErrorOccured = 2
	ShutdownProduct = 3
	CCStartup = 4
	CCShutdown = 5
	CCLogin = 6
	CCLogout = 7

class ProductId(Enum):
	MicroStation = 1000
	Bentley_Redline = 1146
	Bentley_CivilStorm = 1207
	Bentley_CulvertMaster = 1210
	Bentley_Calibrator = 1211
	Bentley_Designer = 1212
	Bentley_FlowMaster = 1222
	Bentley_GISConnect = 1223
	Bentley_HEC_Pack = 1224
	Bentley_HAMMER = 1225
	Bentley_PondPack = 1233
	Bentley_SCADAConnect = 1239
	Bentley_SewerCAD = 1243
	Bentley_SewerGEMS = 1244
	Bentley_Skelebrator = 1245
	Bentley_StormCAD = 1246
	Bentley_WaterCAD = 1248
	Bentley_WaterGEMS = 1249
	Bentley_WaterSAFE = 1250
	Bentley_Scheduler = 1860
	Bentley_GasAnalysis = 1861
	Bentley_PipeAssetPlanner = 1895
	Bentley_SUE = 2335
	Bentley_OpenRoadsDesigner = 2515
	Bentley_OpenRailDesigner = 2641
	Bentley_CNCCBIMOpenRoads = 2697
	Bentley_OpenSiteDesigner = 2758
	Bentley_WaterOPS = 2922
	Bentley_SewerOPS = 2923
	Bentley_OverHeadLineDesigner = 2963
	Bentley_OpenRailChina = 3136
	Bentley_OpenRailUltimateChina = 3210
	Bentley_OpenRoadsUltimateChina = 3211
	Bentley_OpenRoadsChina = 3216
	Bentley_OpenFlows_Entitlement = 3276

class LicensePlatformType(Enum):
	Unknown = 0
	MicroStation = 1
	AutoCAD = 2
	ArcGIS = 3
	Standalone = 4
	Navigator = 5
	MX = 6
	GEOPAK = 7
	InRoads = 8
	OpenPlantModeler = 9
	OutlookConnector = 10
	SharePointConnector = 11
	ProjectWise = 12

class ArchitectureType(Enum):
	X86 = 0
	X64 = 1

class FeatureMap:

	@overload
	def __init__(self, apstring: str) -> None:
		"""No Description

		Args
		--------
			apstring (``str``) :  apstring
		"""
		pass

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			apstring (``str``) :  apstring
		"""
		pass

	def Value(self, apstringKey: str) -> str:
		"""No Description

		Args
		--------
			apstringKey (``str``) :  apstringKey

		Returns
		--------
			``str`` : 
		"""
		pass

	def Dispose(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Keys(self) -> StringCollection:
		"""No Description

		Returns
		--------
			``FeatureMap`` : 
		"""
		pass

	@property
	def ReadableFeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``FeatureMap`` : 
		"""
		pass

	@property
	def FeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``FeatureMap`` : 
		"""
		pass

	@property
	def CanonicalFeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``FeatureMap`` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``FeatureMap`` : 
		"""
		pass

class ProductRelease:

	@overload
	def __init__(self, productId: ProductId, name: str, productVersion: str) -> None:
		"""No Description

		Args
		--------
			productId (``ProductId``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``ProductId``) :  productId
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			productVersion (``str``) :  productVersion
		"""
		pass

	@overload
	def __init__(self, productId: ProductId, productVersion: str) -> None:
		"""No Description

		Args
		--------
			productId (``ProductId``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``ProductId``) :  productId
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			productVersion (``str``) :  productVersion
		"""
		pass

	@overload
	def __init__(self, productId: int, name: str, productVersion: str) -> None:
		"""No Description

		Args
		--------
			productId (``ProductId``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``ProductId``) :  productId
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			productVersion (``str``) :  productVersion
		"""
		pass

	@overload
	def __init__(self, productId: int, productVersion: str) -> None:
		"""No Description

		Args
		--------
			productId (``ProductId``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``ProductId``) :  productId
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			name (``str``) :  name
			productVersion (``str``) :  productVersion
			productId (``int``) :  productId
			productVersion (``str``) :  productVersion
		"""
		pass

	def Dispose(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@staticmethod
	@property
	def UnlimitedSize() -> int:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@property
	def IsSUDA(self) -> bool:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@IsSUDA.setter
	def IsSUDA(self, issuda: bool) -> None:
		pass

	@property
	def OffersFeatures(self) -> bool:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@property
	def IsMunicipal(self) -> bool:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@property
	def PlatformVersion(self) -> str:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@PlatformVersion.setter
	def PlatformVersion(self, platformversion: str) -> None:
		pass

	@property
	def Region(self) -> str:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@Region.setter
	def Region(self, region: str) -> None:
		pass

	@property
	def Architecture(self) -> ArchitectureType:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@Architecture.setter
	def Architecture(self, architecture: ArchitectureType) -> None:
		pass

	@property
	def PlatformType(self) -> LicensePlatformType:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@PlatformType.setter
	def PlatformType(self, platformtype: LicensePlatformType) -> None:
		pass

	@property
	def Locale(self) -> str:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@Locale.setter
	def Locale(self, locale: str) -> None:
		pass

	@property
	def Version(self) -> str:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

	@property
	def ID(self) -> int:
		"""No Description

		Returns
		--------
			``ProductRelease`` : 
		"""
		pass

class ILicense:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Initialize(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetLicenseStatus(self) -> LicenseStatus:
		"""No Description

		Returns
		--------
			``LicenseStatus`` : 
		"""
		pass

	def StartDesktop(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns
		--------
			``LicenseRunStatusEnum`` : 
		"""
		pass

	def StopDesktop(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def StartFeatureTracking(self, featureID: Guid, featureUserDataMap: Dict[str,str], instanceID: int) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			featureUserDataMap (``Dict[str,str]``) :  featureUserDataMap
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def StartFeatureTracking(self, featureID: Guid, instanceID: int) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StopFeatureTracking(self, instanceID: int) -> bool:
		"""No Description

		Args
		--------
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def FeatureTrackingMark(self, featureID: Guid, featureUserDataKeyValMap: Dict[str,str]) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			featureUserDataKeyValMap (``Dict[str,str]``) :  featureUserDataKeyValMap

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def FeatureTrackingMark(self, featureID: Guid) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StartDesktopProject(self, projectID: str) -> bool:
		"""No Description

		Args
		--------
			projectID (``str``) :  projectID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StopDesktopProject(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StartMLA(self, apProduct: ProductRelease, waitForExit: bool) -> None:
		"""No Description

		Args
		--------
			apProduct (``ProductRelease``) :  apProduct
			waitForExit (``bool``) :  waitForExit

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsAnalysisEnabledMessage(self, showMessage: bool) -> bool:
		"""No Description

		Args
		--------
			showMessage (``bool``) :  showMessage

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IsPrintingEnabledMessage(self, showMessage: bool) -> bool:
		"""No Description

		Args
		--------
			showMessage (``bool``) :  showMessage

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetProxyInformation(self, proxyName: str, proxyNeedsAuth: bool, proxyUserName: str, proxyPw: str, handshake: str) -> bool:
		"""No Description

		Args
		--------
			proxyName (``str``) :  proxyName
			proxyNeedsAuth (``bool``) :  proxyNeedsAuth
			proxyUserName (``str``) :  proxyUserName
			proxyPw (``str``) :  proxyPw
			handshake (``str``) :  handshake

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetComputerName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetDaysUntilDisabled(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetOrganizationName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetUsername(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetLicenseType(self) -> LicenseType:
		"""No Description

		Returns
		--------
			``LicenseType`` : 
		"""
		pass

	def GetExpirationDate(self) -> datetime:
		"""No Description

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def ClearDefaultFeatureString(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def IsTemporaryLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def RunStatus(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def SizeEnabled(self) -> int:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsSUDAEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@IsSUDAEnabled.setter
	def IsSUDAEnabled(self, issudaenabled: bool) -> None:
		pass

	@property
	def IsMicroStationEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsArcGISEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsAutoCADEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsPrintingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsAnalysisEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsDefaultFeatureSet(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def ReadableType(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def ReadableFeatureStringType(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def FeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def Features(self) -> FeatureMap:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def DefaultFeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@DefaultFeatureString.setter
	def DefaultFeatureString(self, defaultfeaturestring: str) -> None:
		pass

	@property
	def IsCheckedOutLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsInitialized(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def Product(self) -> ProductRelease:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

class ILicenseProvider:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetActiveLicense(self) -> License:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	def GetComputeTrackingID(self) -> Guid:
		"""No Description

		Returns
		--------
			``Guid`` : 
		"""
		pass

	def GetComputeSCADATrackingID(self) -> Guid:
		"""No Description

		Returns
		--------
			``Guid`` : 
		"""
		pass

	def AddFeatureUserData(self, userKey: str, userValue: str) -> None:
		"""No Description

		Args
		--------
			userKey (``str``) :  userKey
			userValue (``str``) :  userValue

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def FeatureDataMap(self) -> Dict[str,str]:
		"""No Description

		Returns
		--------
			``ILicenseProvider`` : 
		"""
		pass

class License(ILicense):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	@overload
	def Default(productRelease: ProductRelease, windowOwner: IntPtr, messageHandler: IMessageHandler, defaultFeatureString: str, isEntitlementLicense: bool) -> License:
		"""No Description

		Args
		--------
			productRelease (``ProductRelease``) :  productRelease
			windowOwner (``IntPtr``) :  windowOwner
			messageHandler (``IMessageHandler``) :  messageHandler
			defaultFeatureString (``str``) :  defaultFeatureString
			isEntitlementLicense (``bool``) :  isEntitlementLicense

		Returns
		--------
			``License`` : 
		"""
		pass

	@staticmethod
	@overload
	def Default(productRelease: ProductRelease, windowOwner: IntPtr, messageHandler: IMessageHandler, defaultFeatureString: str) -> License:
		"""No Description

		Args
		--------
			productRelease (``ProductRelease``) :  productRelease
			windowOwner (``IntPtr``) :  windowOwner
			messageHandler (``IMessageHandler``) :  messageHandler
			defaultFeatureString (``str``) :  defaultFeatureString

		Returns
		--------
			``License`` : 
		"""
		pass

	@staticmethod
	@overload
	def Default(productRelease: ProductRelease, windowOwner: IntPtr, messageHandler: IMessageHandler) -> License:
		"""No Description

		Args
		--------
			productRelease (``ProductRelease``) :  productRelease
			windowOwner (``IntPtr``) :  windowOwner
			messageHandler (``IMessageHandler``) :  messageHandler

		Returns
		--------
			``License`` : 
		"""
		pass

	def add_LicenseStatusChanged(self, value: LicenseStatusChangedDelegate) -> None:
		"""No Description

		Args
		--------
			value (``LicenseStatusChangedDelegate``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_LicenseStatusChanged(self, value: LicenseStatusChangedDelegate) -> None:
		"""No Description

		Args
		--------
			value (``LicenseStatusChangedDelegate``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def InternalLicenseSimulatorShutdownProduct(self, productID: int) -> None:
		"""No Description

		Args
		--------
			productID (``int``) :  productID

		Returns
		--------
			``None`` : 
		"""
		pass

	def Initialize(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetLicenseStatus(self) -> LicenseStatus:
		"""No Description

		Returns
		--------
			``LicenseStatus`` : 
		"""
		pass

	def StartDesktop(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns
		--------
			``LicenseRunStatusEnum`` : 
		"""
		pass

	def StopDesktop(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def StartFeatureTracking(self, featureID: Guid, featureUserDataMap: Dict[str,str], instanceID: int) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			featureUserDataMap (``Dict[str,str]``) :  featureUserDataMap
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def StartFeatureTracking(self, featureID: Guid, instanceID: int) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StopFeatureTracking(self, instanceID: int) -> bool:
		"""No Description

		Args
		--------
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def FeatureTrackingMark(self, featureID: Guid, featureUserDataKeyValMap: Dict[str,str]) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			featureUserDataKeyValMap (``Dict[str,str]``) :  featureUserDataKeyValMap

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def FeatureTrackingMark(self, featureID: Guid) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StartDesktopProject(self, projectID: str) -> bool:
		"""No Description

		Args
		--------
			projectID (``str``) :  projectID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StopDesktopProject(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StartMLA(self, apProduct: ProductRelease, waitForExit: bool) -> None:
		"""No Description

		Args
		--------
			apProduct (``ProductRelease``) :  apProduct
			waitForExit (``bool``) :  waitForExit

		Returns
		--------
			``None`` : 
		"""
		pass

	def ChangeFeatureLevel(self, handle: int) -> None:
		"""No Description

		Args
		--------
			handle (``int``) :  handle

		Returns
		--------
			``None`` : 
		"""
		pass

	def OpenFeatureLevelSelector(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsAnalysisEnabledMessage(self, showMessage: bool) -> bool:
		"""No Description

		Args
		--------
			showMessage (``bool``) :  showMessage

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IsPrintingEnabledMessage(self, showMessage: bool) -> bool:
		"""No Description

		Args
		--------
			showMessage (``bool``) :  showMessage

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetProxyInformation(self, proxyName: str, proxyNeedsAuth: bool, proxyUserName: str, proxyPw: str, handshake: str) -> bool:
		"""No Description

		Args
		--------
			proxyName (``str``) :  proxyName
			proxyNeedsAuth (``bool``) :  proxyNeedsAuth
			proxyUserName (``str``) :  proxyUserName
			proxyPw (``str``) :  proxyPw
			handshake (``str``) :  handshake

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetComputerName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetDaysUntilDisabled(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetOrganizationName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetUsername(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetExpirationDate(self) -> datetime:
		"""No Description

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def GetFeatureLevelSelectorToolPath(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def ClearDefaultFeatureString(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetLicenseType(self) -> LicenseType:
		"""No Description

		Returns
		--------
			``LicenseType`` : 
		"""
		pass

	def PeekEntitlement(self) -> LicenseType:
		"""No Description

		Returns
		--------
			``LicenseType`` : 
		"""
		pass

	def Dispose(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def StartFeatureTracking(self, featureID: Guid, instanceID: int) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def FeatureTrackingMark(self, featureID: Guid) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def UseTitleDecorationForTemporaryLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsTemporaryLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def RunStatus(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsEntitlementLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def SizeEnabled(self) -> int:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsSUDAEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@IsSUDAEnabled.setter
	def IsSUDAEnabled(self, issudaenabled: bool) -> None:
		pass

	@property
	def IsMicroStationEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsArcGISEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsAutoCADEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsPrintingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsAnalysisEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsDefaultFeatureSet(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def ReadableType(self) -> str:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def ReadableFeatureStringType(self) -> str:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def FeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def Features(self) -> FeatureMap:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def DefaultFeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@DefaultFeatureString.setter
	def DefaultFeatureString(self, defaultfeaturestring: str) -> None:
		pass

	@property
	def IsCheckedOutLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def IsInitialized(self) -> bool:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@property
	def WindowOwner(self) -> IntPtr:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	@WindowOwner.setter
	def WindowOwner(self, windowowner: IntPtr) -> None:
		pass

	@property
	def Product(self) -> ProductRelease:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

