from typing import overload, List, Dict, Iterator, Generic
from System import ICloneable, EventHandler, EventArgs, IAsyncResult, AsyncCallback, Guid, T, IntPtr
from array import array
from Haestad.Support.ISupport import HmIDCollection, ILabeled, IField, FieldCollection, FieldDataType, IEditLabeled, SortContextCollection, FilterContextCollection, GeometryPoint, IEditField, INamable
from Haestad.Support.IUser import ExceptionEventHandler, IProcessInProgress, IMessageQuestionHandler, IProgressIndicator, IProcessInProgressEx, IMessageHandler
from enum import Enum
from System.Runtime.Serialization import SerializationInfo, StreamingContext, ISerializable
from Haestad.Support.IUnits import UnitIndex, NumericFormatter, TimeUnit, Unit, UnitSystem
from Haestad.ILicensingFacade import License, ILicenseProvider
from datetime import datetime
from System.Collections import IEnumerator, ICollection
from Haestad.IDomain import IFieldManager


class ModelingElementType(Enum):
	All = 0
	Alternative = 1
	Scenario = 2
	DomainElement = 3
	SupportElement = 4
	CalculationOptions = 5
	EngineeringLibrary = 6
	SelectionSet = 7
	EmbeddedStickyObject = 8
	PrototypeDomainElement = 9
	Profile = 10

class ReferencedElementType(Enum):
	NONE = 0
	DomainElement = 1
	SupportElement = 2
	Scenario = 3
	Alternative = 4
	SelectionSet = 5

class DomainElementType(Enum):
	ManholeElementManager = 1
	CatchBasinElementManager = 2
	ConduitElementManager = 3
	ChannelElementManager = 4
	OutfallElementManager = 5
	CatchmentElementManager = 6
	PondElementManager = 7
	PondOutletStructureElementManager = 8
	CrossSectionNodeElementManager = 9
	GutterLinkElementManager = 10
	PumpElementManager = 11
	WetWellElementManager = 12
	PressureJunctionElementManager = 13
	PressurePipeElementManager = 14
	JunctionChamberElementManager = 15
	BaseNodeElementManager = 20
	BaseLinkElementManager = 21
	BasePolygonElementManager = 22
	ScadaElementManager = 23
	LateralLinkElementManager = 24
	TapNodeElementManager = 26
	BaseIdahoNodeElementManager = 50
	IdahoDemandNodeElementManager = 51
	IdahoTankElementManager = 52
	IdahoFireFlowNodeManager = 53
	IdahoHydrantElementManager = 54
	IdahoJunctionElementManager = 55
	IdahoReservoirElementManager = 56
	BaseDirectedNodeElementManager = 57
	BaseValveElementManager = 58
	BasePump = 59
	FCVElementManager = 60
	TCVElementManager = 61
	GPVElementManager = 62
	PressureValveElementManager = 63
	PRVElementManager = 64
	PSVElementManager = 65
	PBVElementManager = 66
	PumpStationElementManager = 67
	StandardPumpElementManager = 68
	IdahoPipeElementManager = 69
	IdahoSpotElevationElementManager = 70
	PressureIsolationValveElementManager = 71
	VariableSpeedPumpBatteryElementManager = 72
	CustomerNodeElementManager = 73
	GravitySurfaceStructureElementManager = 100
	GravityLinkElementManager = 201
	GravityStructureElementManager = 203
	GravityNodeElementManager = 204
	PhysicalLinkElementManager = 240
	TurbineElementManager = 300
	AirValveElementManager = 301
	HydropneumaticTankElementManager = 302
	SavSrvElementManager = 303
	BaseOrifice = 304
	DischargeToAtmosphere = 305
	RuptureDisk = 306
	OrificeBetweenTwoPipes = 307
	SurgeTank = 308
	CheckValve = 309
	ValveWithLinearAreaChange = 310
	BaseTank = 311
	ConventionalTank = 312
	BaseHammerNode = 313
	PeriodicHeadFlow = 321
	PressureSystemNode = 400
	PondRouteElementManager = 500
	GasRegulatingValve = 602
	GasPipe = 603
	GasNode = 605
	IdahoPumpStation = 700
	LIDElementManager = 701
	Headwall = 800
	Grid = 801
	BoundaryConditionLine2D = 803
	BoundaryPoint2D = 804
	PropertyConnectionElementManager = 810
	BaseSimplePolyline = 999
	SurfacePoint = 1802
	SurfacePolygon = 1900
	SurfacePolyline = 2000
	SurfaceProfilePolyline = 2001
	ConflictNode = 3000
	CommunicationNode = 3001
	ElectricalNode = 3002
	POLNode = 3003
	ThermalNode = 3004
	WasteWaterNode = 3005
	WaterNode = 3006
	GenericUtilityNode = 3007
	CommunicationSegment = 3008
	ElectricalSegment = 3009
	POLSegment = 3010
	ThermalSegment = 3011
	WasteWaterSegment = 3012
	WaterSegment = 3013
	GasSegment = 3014
	GenericUtilitySegment = 3015
	StormWaterNode = 3016
	StormWaterSegment = 3017
	ReferenceElement = 3018

class DomainElementSubType(Enum):
	TwoDPolygon_Building = 901
	TwoDPolygon_VoidArea = 902
	TwoDPolygon_AdjustmentArea = 903
	TwoDPolygon_LandUse = 904
	TwoDPolygon_RoadArea = 905
	TwoDPolyline_Breakline = 1001
	TwoDPolyline_RoadCenterline = 1002
	TwoDPoint_ReportingPoint = 8020
	TwoDPoint_SpotElevation = 8021
	TwoDPoint_VoidPoint = 8022

class AlternativeType(Enum):
	HmiDataSetGeometryAlternative = 1
	HMIDataSetTopologyAlternative = 2
	HMIActiveTopologyAlternative = 3
	PhysicalAlternative = 4
	BoundaryConditionAlternative = 5
	InitialConditionAlternative = 6
	HydrologicAlternative = 7
	OutputAlternative = 8
	DryLoadAlternative = 9
	RainfallRunoffAlternative = 10
	WaterQualityAlternative = 11
	SanitaryLoadingAlternative = 12
	InfiltrationAndInflowAlternative = 13
	ScadaAlternative = 14
	DemandAlternative = 20
	InitialSettingsAlternative = 21
	OperationalAlternative = 22
	AgeAlternative = 23
	ConstituentAlternative = 24
	TraceAlternative = 25
	FireFlowAlternative = 26
	EnergyCostAlternative = 28
	PressureDependentDemandAlternative = 29
	CriticalityAlternative = 30
	FlushingAlternative = 31
	CapitalCostAlternative = 36
	HeadlossAlternative = 40
	DesignAlternative = 41
	SystemFlowsAlternative = 45
	HammerAlternative = 50
	PipeBreakAlternative = 51
	HMIUserDefinedExtensionsAlternative = 100
	ConflictAlternative = 1000
	NetworkDataAlternative = 1001
	SurfaceAlternative = 1003

class SupportElementType(Enum):
	CatalogPipeElementManager = 1
	CompositeOutletStructureElementManager = 2
	ProfileElementManager = 3
	PollutantElementManager = 4
	AquifersElementManager = 5
	ControlSetElementManager = 6
	LandUseElementManager = 8
	ControlStructureElementElementManager = 9
	StormEventElementManager = 10
	PatternElementManager = 11
	ExtremeFlowFactorElementManager = 12
	UnitSanitaryLoadElementManager = 13
	ExtremeFlowSetupElementManager = 14
	PatternSetupElementManager = 15
	DimensionlessUnitHydrographElementManager = 16
	RTKSetElementManager = 17
	PrototypeManager = 18
	PollutographElementManager = 19
	CatalogGutter = 20
	LIDControl = 21
	TimeSeriesControlDataManager = 22
	IdahoPatternElementManager = 50
	IdahoPumpDefinitionElementManager = 51
	IdahoConstituentElementManager = 52
	ZoneElementManager = 53
	IdahoControlElementManager = 54
	IdahoControlActionElementManager = 55
	IdahoControlConditionElementManager = 56
	IdahoLogicalControlSetElementManager = 59
	PressureDependentDemandFunctionElementManager = 60
	EnergyPricingElementManager = 61
	UnitDemandLoadElementManager = 62
	GpvHeadlossCurveElementManager = 63
	CriticalityStudyGroupElementManager = 64
	CriticalityStudyElementManager = 65
	ValveCharacteristicsElementManager = 66
	FlushingEventElementManager = 67
	AirFlowCurveManager = 68
	CheckValveDynamicCharacteristicsCurveManager = 69
	MinorLossCoefficientElementManager = 101
	TimeSeriesElementManager = 102
	InletElementManager = 103
	GenericHeadlossElementManager = 104
	StormEventGroup = 105
	CatalogConduitElementManager = 106
	SCSCNVolumeElementManager = 107
	TR55GraphicalPeakStorage = 108
	FirstFlushCalculator = 109
	WeirDepthCoefficientManager = 111
	WeirSubmergenceManager = 112
	HydrographManager = 113
	TR55TabularHydrograph = 114
	MinDrainTime = 115
	PeakFlowEstimatedStorage = 116
	EQTWTableElementManager = 117
	QqpTemplateElementManager = 118
	OverlayHydrograph = 119
	RationalMethodQPeak = 120
	PondMaker = 121
	StorageChamber = 124
	VortexValve = 125
	GenericUnitHydrograph = 126
	MainScoreAspect = 150
	MainScore = 151
	PipeBreakGroup = 152
	PipeBreakAnalysis = 153
	FlushingStudy = 175
	FlushingArea = 176
	FlushingReportView = 177
	CulvertInletCoefficients = 180
	PressureZoneStudyGroupElementManager = 200
	PressureZoneStudyElementManager = 201
	UnitCarbonEmissions = 202
	PowerMeter = 203
	EnergyAggregationStudy = 204
	MSXSetup = 220
	SnowPack = 250
	SWMMRTKUnitHydrographSet = 251
	PumpStation = 252
	ScadaDataSource = 256
	ScadaSignal = 257
	AlertMessage = 260
	SCADAConnectSimulator = 261
	OPCPublishingResult = 262
	PerformanceStudy = 263
	DistrictMeterArea = 265
	GasPipeType = 300
	GasCustomer = 301
	TwoDDataSource = 350
	DigitalTerrainModel = 351
	DigitalTerrainModelGroup = 352
	LandCover = 353

class DomainElementShapeType(Enum):
	Point = 0
	Polyline = 1
	Polygon = 2
	DirectedNode = 3
	ReferenceNode = 4
	Lateral = 5
	SimplePolyline = 6

class wkbByteOrder(Enum):
	wkbXDR = 0
	wkbNDR = 1

class wkbGeometryType(Enum):
	wkbPoint = 1
	wkbLineString = 2
	wkbPolygon = 3
	wkbMultiPoint = 4
	wkbMultiLineString = 5
	wkbMultiPolygon = 6
	wkbGeometryCollection = 7

class StandardFieldType(Enum):
	Label = 0
	Notes = 1

class ConnectionType(Enum):
	Jet4pt0 = 1
	Sqlite = 2

class ConnectionProperty(Enum):
	FileName = 1
	ConnectionType = 2
	DatabasePassword = 3
	JetWorkspaceUserName = 4
	JetWorkspacePassword = 5
	EnableSchemaUpdate = 6
	ShouldUpdateCounters = 7
	EnableCoreSchemaUpdate = 8
	CheckSuccessfulCloseFlag = 9

class SelectionSetType(Enum):
	Standard = 1
	Profile = 2

class FlowDirection(Enum):
	NoFlow = 0
	Positive = 1
	Negative = -1

class DomainFieldType(Enum):
	ModelingElementField = 1
	SupportElementField = 2
	DomainElementField = 3
	ResultField = 4
	AlternativeField = 5
	SystemRecordField = 6

class ReferenceCardinality(Enum):
	OneToMany = 0
	OneToOne = 1

class NumericalEngineType(Enum):
	EpaNET = 1
	GVFEngine = 2

class StatisticType(Enum):
	Minimum = 1
	Maximum = 2
	Mean = 3
	Sum = 4
	Count = 5
	StandardDeviation = 6
	AreaUnderCurve = 7

class BulkOperationType(Enum):
	NONE = 0
	Insert = 1
	Load = 2

class StoredQueryType(Enum):
	View = 0
	StoredProcedure = 1

class CompactOperationTask(Enum):
	All = 0
	PurgeDeletedRows = 1
	RefreshBoundingBox = 2
	RefreshCachedManagerCounts = 3
	RefreshCachedGeometryProperties = 4
	RefreshReferenceNodeCachesOnly = 5
	RefreshCachedCollectionCounts = 6
	RefreshCachedSmartLabels = 7
	VerifyVisualLinkConnectivity = 8
	PurgeDeletedGISIDs = 9
	PurgeDataRowsFromGISIDsMarkedAsDeleted = 10
	VerifySelectionSetsThoroughly = 11
	RefreshCachedAlternativeLevels = 12
	WaterRefreshCachedUnitDemandBaseFlow = 13
	WaterRefreshCachedMinorlosses = 14

class ExpressionType(Enum):
	NONE = 0
	ECExpressions = 1

class FieldUpdateTypeEnum(Enum):
	NoChange = 0
	Change = 1
	Eliminated = 2

class ExternalIDType(Enum):
	PersistentElementPath = 1

class PressureZoneValveStatusEnum(Enum):
	AlwaysUse = 0
	UseWhenClosed = 1
	DoNotUse = 2
	UseWhenActive = 3
	UseWhenClosedOrActive = 4

class PressureZonePipeStatusEnum(Enum):
	UseWhenClosedCheckValve = 0
	UseWhenClosed = 1
	DoNotUse = 2

class PressureZonePumpStatusEnum(Enum):
	AlwaysUse = 0
	DoNotUse = 1

class PressureZoneCheckValveStatusEnum(Enum):
	AlwaysUse = 0
	DoNotUse = 2

class PressureZoneOrificeBetweenPipesStatusEnum(Enum):
	AlwaysUse = 0
	DoNotUse = 1

class UseInPressureZoneTraceEnum(Enum):
	PzTraceAlwaysUseType = 0
	PzTraceUseWhenClosedType = 1
	PzTraceUseWhenClosedCheckValveType = 2
	PzTraceDoNotUseType = 3
	PzTraceUseWhenActiveType = 4
	PzTraceUseWhenClosedOrActiveType = 5

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class AlternativeTypeCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`AlternativeTypeCollection`) :  c
			a (`List[IAlternativeType]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`AlternativeTypeCollection`) :  c
			a (`List[IAlternativeType]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: AlternativeTypeCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`AlternativeTypeCollection`) :  c
			a (`List[IAlternativeType]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IAlternativeType]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`AlternativeTypeCollection`) :  c
			a (`List[IAlternativeType]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: AlternativeTypeCollection) -> AlternativeTypeCollection:
		"""No Description

		Args
		--------
			list (`AlternativeTypeCollection`) :  list

		Returns
		--------
			`AlternativeTypeCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: AlternativeTypeCollection) -> AlternativeTypeCollection:
		"""No Description

		Args
		--------
			list (`AlternativeTypeCollection`) :  list

		Returns
		--------
			`AlternativeTypeCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IAlternativeType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IAlternativeType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IAlternativeType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IAlternativeType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IAlternativeType) -> int:
		"""No Description

		Args
		--------
			item (`IAlternativeType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IAlternativeType) -> bool:
		"""No Description

		Args
		--------
			item (`IAlternativeType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IAlternativeType) -> int:
		"""No Description

		Args
		--------
			item (`IAlternativeType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IAlternativeType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			item (`IAlternativeType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IAlternativeTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IAlternativeTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: AlternativeTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`AlternativeTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IAlternativeType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IAlternativeType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IAlternativeType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class AssemblyLibrary:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	def GetAssembly(assemblyName: str, domainPath: str) -> Assembly:
		"""No Description

		Args
		--------
			assemblyName (`str`) :  assemblyName
			domainPath (`str`) :  domainPath

		Returns
		--------
			`Assembly` : 
		"""
		pass

	@staticmethod
	def GetSolverAssembly(assemblyName: str, domainPath: str) -> Assembly:
		"""No Description

		Args
		--------
			assemblyName (`str`) :  assemblyName
			domainPath (`str`) :  domainPath

		Returns
		--------
			`Assembly` : 
		"""
		pass

class FieldTypeCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`FieldTypeCollection`) :  c
			a (`List[IFieldType]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`FieldTypeCollection`) :  c
			a (`List[IFieldType]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: FieldTypeCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`FieldTypeCollection`) :  c
			a (`List[IFieldType]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IFieldType]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`FieldTypeCollection`) :  c
			a (`List[IFieldType]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: FieldTypeCollection) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			list (`FieldTypeCollection`) :  list

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: FieldTypeCollection) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			list (`FieldTypeCollection`) :  list

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFieldType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IFieldType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFieldType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IFieldType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IFieldType) -> int:
		"""No Description

		Args
		--------
			item (`IFieldType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IFieldType) -> bool:
		"""No Description

		Args
		--------
			item (`IFieldType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IFieldType) -> int:
		"""No Description

		Args
		--------
			item (`IFieldType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IFieldType) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IFieldType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IFieldType) -> None:
		"""No Description

		Args
		--------
			item (`IFieldType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IFieldTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IFieldTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: FieldTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`FieldTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IFieldType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IFieldType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IFieldType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class CompactOperationContext:

	def __new__(self, tasks: List[CompactOperationTask]) -> None:
		"""No Description

		Args
		--------
			tasks (`List[CompactOperationTask]`) :  tasks
		"""
		pass

	def AddTask(self, task: CompactOperationTask) -> None:
		"""No Description

		Args
		--------
			task (`CompactOperationTask`) :  task

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveTask(self, task: CompactOperationTask) -> None:
		"""No Description

		Args
		--------
			task (`CompactOperationTask`) :  task

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, task: CompactOperationTask) -> bool:
		"""No Description

		Args
		--------
			task (`CompactOperationTask`) :  task

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Tasks(self) -> List[CompactOperationTask]:
		"""No Description

		Returns
		--------
			`List[CompactOperationTask]` : 
		"""
		pass

class DataViewDelayedHmIDCollection(IHmIDDelayedCollection):

	@overload
	def __new__(self, dataView: DataView) -> None:
		"""No Description

		Args
		--------
			dataView (`DataView`) :  dataView
			dataView (`DataView`) :  dataView
			fieldIndex (`int`) :  fieldIndex
		"""
		pass

	@overload
	def __new__(self, dataView: DataView, fieldIndex: int) -> None:
		"""No Description

		Args
		--------
			dataView (`DataView`) :  dataView
			dataView (`DataView`) :  dataView
			fieldIndex (`int`) :  fieldIndex
		"""
		pass

	def Dispose(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int]) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], start: int) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], startInTarget: int, startInSource: int, length: int) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array
			startInTarget (`int`) :  startInTarget
			startInSource (`int`) :  startInSource
			length (`int`) :  length

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: int) -> bool:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`int`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: int) -> None:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IHmIDCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IHmIDCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: HmIDCollection) -> int:
		"""No Description

		Args
		--------
			x (`HmIDCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: array[int]) -> int:
		"""No Description

		Args
		--------
			x (`array[int]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Sort(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ReverseInPlace(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ToArray(self) -> array[int]:
		"""No Description

		Returns
		--------
			`array[int]` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Item.setter
	def Item(self, item: int) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class DomainDataSetCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetCollection`) :  c
			a (`List[IDomainDataSet]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetCollection`) :  c
			a (`List[IDomainDataSet]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: DomainDataSetCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetCollection`) :  c
			a (`List[IDomainDataSet]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IDomainDataSet]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetCollection`) :  c
			a (`List[IDomainDataSet]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: DomainDataSetCollection) -> DomainDataSetCollection:
		"""No Description

		Args
		--------
			list (`DomainDataSetCollection`) :  list

		Returns
		--------
			`DomainDataSetCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: DomainDataSetCollection) -> DomainDataSetCollection:
		"""No Description

		Args
		--------
			list (`DomainDataSetCollection`) :  list

		Returns
		--------
			`DomainDataSetCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSet]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSet]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSet], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSet]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IDomainDataSet) -> int:
		"""No Description

		Args
		--------
			item (`IDomainDataSet`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IDomainDataSet) -> bool:
		"""No Description

		Args
		--------
			item (`IDomainDataSet`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IDomainDataSet) -> int:
		"""No Description

		Args
		--------
			item (`IDomainDataSet`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IDomainDataSet) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IDomainDataSet`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IDomainDataSet) -> None:
		"""No Description

		Args
		--------
			item (`IDomainDataSet`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainDataSetCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainDataSetCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainDataSetCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainDataSetCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainDataSet]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainDataSet]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainDataSet) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class DomainDataSetTypeCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetTypeCollection`) :  c
			a (`List[IDomainDataSetType]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetTypeCollection`) :  c
			a (`List[IDomainDataSetType]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: DomainDataSetTypeCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetTypeCollection`) :  c
			a (`List[IDomainDataSetType]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IDomainDataSetType]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainDataSetTypeCollection`) :  c
			a (`List[IDomainDataSetType]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: DomainDataSetTypeCollection) -> DomainDataSetTypeCollection:
		"""No Description

		Args
		--------
			list (`DomainDataSetTypeCollection`) :  list

		Returns
		--------
			`DomainDataSetTypeCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: DomainDataSetTypeCollection) -> DomainDataSetTypeCollection:
		"""No Description

		Args
		--------
			list (`DomainDataSetTypeCollection`) :  list

		Returns
		--------
			`DomainDataSetTypeCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSetType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSetType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSetType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSetType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IDomainDataSetType) -> int:
		"""No Description

		Args
		--------
			item (`IDomainDataSetType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IDomainDataSetType) -> bool:
		"""No Description

		Args
		--------
			item (`IDomainDataSetType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IDomainDataSetType) -> int:
		"""No Description

		Args
		--------
			item (`IDomainDataSetType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IDomainDataSetType) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IDomainDataSetType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IDomainDataSetType) -> None:
		"""No Description

		Args
		--------
			item (`IDomainDataSetType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainDataSetTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainDataSetTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainDataSetTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainDataSetTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainDataSetType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainDataSetType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainDataSetType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class DomainElementTypeCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainElementTypeCollection`) :  c
			a (`List[IDomainElementType]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainElementTypeCollection`) :  c
			a (`List[IDomainElementType]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: DomainElementTypeCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainElementTypeCollection`) :  c
			a (`List[IDomainElementType]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IDomainElementType]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`DomainElementTypeCollection`) :  c
			a (`List[IDomainElementType]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: DomainElementTypeCollection) -> DomainElementTypeCollection:
		"""No Description

		Args
		--------
			list (`DomainElementTypeCollection`) :  list

		Returns
		--------
			`DomainElementTypeCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: DomainElementTypeCollection) -> DomainElementTypeCollection:
		"""No Description

		Args
		--------
			list (`DomainElementTypeCollection`) :  list

		Returns
		--------
			`DomainElementTypeCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainElementType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainElementType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainElementType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainElementType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IDomainElementType) -> int:
		"""No Description

		Args
		--------
			item (`IDomainElementType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IDomainElementType) -> bool:
		"""No Description

		Args
		--------
			item (`IDomainElementType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IDomainElementType) -> int:
		"""No Description

		Args
		--------
			item (`IDomainElementType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IDomainElementType) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IDomainElementType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IDomainElementType) -> None:
		"""No Description

		Args
		--------
			item (`IDomainElementType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainElementTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainElementTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainElementTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainElementTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainElementType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainElementType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainElementType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class DomainElementTypeLibrary:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	def GetConcreteDomainElementTypeIDs(domainDataSetType: IDomainDataSetType, baseDomainElementTypeIDs: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainDataSetType (`IDomainDataSetType`) :  domainDataSetType
			baseDomainElementTypeIDs (`HmIDCollection`) :  baseDomainElementTypeIDs

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@staticmethod
	def GetSubtypeIds(domainDataSet: IDomainDataSet, elementTypeId: int, includeBaseTypes: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			elementTypeId (`int`) :  elementTypeId
			includeBaseTypes (`bool`) :  includeBaseTypes

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@staticmethod
	def GetOrderIndex(domainDataSetType: IDomainDataSetType, domainElementTypeID: int) -> int:
		"""No Description

		Args
		--------
			domainDataSetType (`IDomainDataSetType`) :  domainDataSetType
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`int` : 
		"""
		pass

	@staticmethod
	@overload
	def GetOrderedDomainElementTypeIDs(domainDataSetType: IDomainDataSetType, domainElementTypeIDs: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainDataSetType (`IDomainDataSetType`) :  domainDataSetType
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def GetOrderedDomainElementTypes(domainDataSet: IDomainDataSet) -> DomainElementTypeCollection:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet

		Returns
		--------
			`DomainElementTypeCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def GetOrderedDomainElementTypes(domainDataSet: IDomainDataSet, includeBaseTypes: bool) -> DomainElementTypeCollection:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			includeBaseTypes (`bool`) :  includeBaseTypes

		Returns
		--------
			`DomainElementTypeCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def GetOrderedDomainElementTypeIDs(domainDataSet: IDomainDataSet) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def GetOrderedDomainElementTypeIDs(domainDataSet: IDomainDataSet, includeBaseTypes: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			includeBaseTypes (`bool`) :  includeBaseTypes

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@staticmethod
	def UpdateElementTypeID(originalElementTypeID: int) -> int:
		"""No Description

		Args
		--------
			originalElementTypeID (`int`) :  originalElementTypeID

		Returns
		--------
			`int` : 
		"""
		pass

	@staticmethod
	def UpdateSupportElementTypeID(originalElementTypeID: int) -> int:
		"""No Description

		Args
		--------
			originalElementTypeID (`int`) :  originalElementTypeID

		Returns
		--------
			`int` : 
		"""
		pass

class EngineProgressAdapterBase(IProcessInProgress):

	def __new__(self, numericalEngine: INumericalEngine) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def add_ProcessFailed(self, value: ExceptionEventHandler) -> None:
		"""No Description

		Args
		--------
			value (`ExceptionEventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_ProcessFailed(self, value: ExceptionEventHandler) -> None:
		"""No Description

		Args
		--------
			value (`ExceptionEventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_ProcessUpdated(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_ProcessUpdated(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_ProcessFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_ProcessFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_ProcessStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_ProcessStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def CancelProcess(self, sender: object, e: EventArgs) -> None:
		"""No Description

		Args
		--------
			sender (`object`) :  sender
			e (`EventArgs`) :  e

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def AllowCancel(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def ProgressValue(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ProgressValue.setter
	def ProgressValue(self, progressvalue: int) -> None:
		pass

	@property
	def ProgressDescription(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@ProgressDescription.setter
	def ProgressDescription(self, progressdescription: str) -> None:
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

class CalculationStepEventHandler(ICloneable, ISerializable):

	def __new__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args
		--------
			object (`object`) :  object
			method (`IntPtr`) :  method
		"""
		pass

	def Invoke(self, sender: object, e: CalculationStepEventArgs) -> None:
		"""No Description

		Args
		--------
			sender (`object`) :  sender
			e (`CalculationStepEventArgs`) :  e

		Returns
		--------
			`None` : 
		"""
		pass

	def BeginInvoke(self, sender: object, e: CalculationStepEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args
		--------
			sender (`object`) :  sender
			e (`CalculationStepEventArgs`) :  e
			callback (`AsyncCallback`) :  callback
			object (`object`) :  object

		Returns
		--------
			`IAsyncResult` : 
		"""
		pass

	def EndInvoke(self, result: IAsyncResult) -> None:
		"""No Description

		Args
		--------
			result (`IAsyncResult`) :  result

		Returns
		--------
			`None` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (`SerializationInfo`) :  info
			context (`StreamingContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	def GetInvocationList(self) -> List[Delegate]:
		"""No Description

		Returns
		--------
			`List[Delegate]` : 
		"""
		pass

	def DynamicInvoke(self, args: List[object]) -> object:
		"""No Description

		Args
		--------
			args (`List[object]`) :  args

		Returns
		--------
			`object` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Method(self) -> MethodInfo:
		"""No Description

		Returns
		--------
			`MethodInfo` : 
		"""
		pass

	@property
	def Target(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

class CalculationStepProgressEventHandler(ICloneable, ISerializable):

	def __new__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args
		--------
			object (`object`) :  object
			method (`IntPtr`) :  method
		"""
		pass

	def Invoke(self, sender: object, e: CalculationStepProgressEventArgs) -> None:
		"""No Description

		Args
		--------
			sender (`object`) :  sender
			e (`CalculationStepProgressEventArgs`) :  e

		Returns
		--------
			`None` : 
		"""
		pass

	def BeginInvoke(self, sender: object, e: CalculationStepProgressEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args
		--------
			sender (`object`) :  sender
			e (`CalculationStepProgressEventArgs`) :  e
			callback (`AsyncCallback`) :  callback
			object (`object`) :  object

		Returns
		--------
			`IAsyncResult` : 
		"""
		pass

	def EndInvoke(self, result: IAsyncResult) -> None:
		"""No Description

		Args
		--------
			result (`IAsyncResult`) :  result

		Returns
		--------
			`None` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (`SerializationInfo`) :  info
			context (`StreamingContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	def GetInvocationList(self) -> List[Delegate]:
		"""No Description

		Returns
		--------
			`List[Delegate]` : 
		"""
		pass

	def DynamicInvoke(self, args: List[object]) -> object:
		"""No Description

		Args
		--------
			args (`List[object]`) :  args

		Returns
		--------
			`object` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Method(self) -> MethodInfo:
		"""No Description

		Returns
		--------
			`MethodInfo` : 
		"""
		pass

	@property
	def Target(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

class CalculationStepEventArgs(ILabeled):

	def __new__(self, label: str) -> None:
		"""No Description

		Args
		--------
			label (`str`) :  label
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

class CalculationStepProgressEventArgs(ILabeled):

	def __new__(self, progress: int, label: str, cancel: bool) -> None:
		"""No Description

		Args
		--------
			progress (`int`) :  progress
			label (`str`) :  label
			cancel (`bool`) :  cancel
		"""
		pass

	def UpdateState(self, label: str, progress: int) -> None:
		"""No Description

		Args
		--------
			label (`str`) :  label
			progress (`int`) :  progress

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Progress(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Cancel(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@Cancel.setter
	def Cancel(self, cancel: bool) -> None:
		pass

class ScenarioCalculationEventArgs:

	def __new__(self, scenarioId: int) -> None:
		"""No Description

		Args
		--------
			scenarioId (`int`) :  scenarioId
		"""
		pass

	@property
	def ScenarioID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class PossibleCorruptedDatabaseException(ISerializable, _Exception):

	def __new__(self, message: str, corruptedFileName: str) -> None:
		"""No Description

		Args
		--------
			message (`str`) :  message
			corruptedFileName (`str`) :  corruptedFileName
		"""
		pass

	def GetBaseException(self) -> Exception:
		"""No Description

		Returns
		--------
			`Exception` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (`SerializationInfo`) :  info
			context (`StreamingContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def CorruptedFileName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Message(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Data(self) -> Dict:
		"""No Description

		Returns
		--------
			`Dict` : 
		"""
		pass

	@property
	def InnerException(self) -> Exception:
		"""No Description

		Returns
		--------
			`Exception` : 
		"""
		pass

	@property
	def TargetSite(self) -> MethodBase:
		"""No Description

		Returns
		--------
			`MethodBase` : 
		"""
		pass

	@property
	def StackTrace(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def HelpLink(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@HelpLink.setter
	def HelpLink(self, helplink: str) -> None:
		pass

	@property
	def Source(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Source.setter
	def Source(self, source: str) -> None:
		pass

	@property
	def HResult(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@HResult.setter
	def HResult(self, hresult: int) -> None:
		pass

class CancelledDatabaseOpenException(ISerializable, _Exception):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def GetBaseException(self) -> Exception:
		"""No Description

		Returns
		--------
			`Exception` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (`SerializationInfo`) :  info
			context (`StreamingContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def ErrorCode(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Message(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Data(self) -> Dict:
		"""No Description

		Returns
		--------
			`Dict` : 
		"""
		pass

	@property
	def InnerException(self) -> Exception:
		"""No Description

		Returns
		--------
			`Exception` : 
		"""
		pass

	@property
	def TargetSite(self) -> MethodBase:
		"""No Description

		Returns
		--------
			`MethodBase` : 
		"""
		pass

	@property
	def StackTrace(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def HelpLink(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@HelpLink.setter
	def HelpLink(self, helplink: str) -> None:
		pass

	@property
	def Source(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Source.setter
	def Source(self, source: str) -> None:
		pass

	@property
	def HResult(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@HResult.setter
	def HResult(self, hresult: int) -> None:
		pass

class FieldDescriptor:

	def __new__(self, type: DomainFieldType, name: str, descriptor1: str, descriptor2: str) -> None:
		"""No Description

		Args
		--------
			type (`DomainFieldType`) :  type
			name (`str`) :  name
			descriptor1 (`str`) :  descriptor1
			descriptor2 (`str`) :  descriptor2
		"""
		pass

class FieldDescriptorFilterCallback(ICloneable, ISerializable):

	def __new__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args
		--------
			object (`object`) :  object
			method (`IntPtr`) :  method
		"""
		pass

	def Invoke(self, descriptor: FieldDescriptor) -> bool:
		"""No Description

		Args
		--------
			descriptor (`FieldDescriptor`) :  descriptor

		Returns
		--------
			`bool` : 
		"""
		pass

	def BeginInvoke(self, descriptor: FieldDescriptor, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args
		--------
			descriptor (`FieldDescriptor`) :  descriptor
			callback (`AsyncCallback`) :  callback
			object (`object`) :  object

		Returns
		--------
			`IAsyncResult` : 
		"""
		pass

	def EndInvoke(self, result: IAsyncResult) -> bool:
		"""No Description

		Args
		--------
			result (`IAsyncResult`) :  result

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (`SerializationInfo`) :  info
			context (`StreamingContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	def GetInvocationList(self) -> List[Delegate]:
		"""No Description

		Returns
		--------
			`List[Delegate]` : 
		"""
		pass

	def DynamicInvoke(self, args: List[object]) -> object:
		"""No Description

		Args
		--------
			args (`List[object]`) :  args

		Returns
		--------
			`object` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Method(self) -> MethodInfo:
		"""No Description

		Returns
		--------
			`MethodInfo` : 
		"""
		pass

	@property
	def Target(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

class FieldFilterDelegate(ICloneable, ISerializable):

	def __new__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args
		--------
			object (`object`) :  object
			method (`IntPtr`) :  method
		"""
		pass

	def Invoke(self, field: IField) -> bool:
		"""No Description

		Args
		--------
			field (`IField`) :  field

		Returns
		--------
			`bool` : 
		"""
		pass

	def BeginInvoke(self, field: IField, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args
		--------
			field (`IField`) :  field
			callback (`AsyncCallback`) :  callback
			object (`object`) :  object

		Returns
		--------
			`IAsyncResult` : 
		"""
		pass

	def EndInvoke(self, result: IAsyncResult) -> bool:
		"""No Description

		Args
		--------
			result (`IAsyncResult`) :  result

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (`SerializationInfo`) :  info
			context (`StreamingContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	def GetInvocationList(self) -> List[Delegate]:
		"""No Description

		Returns
		--------
			`List[Delegate]` : 
		"""
		pass

	def DynamicInvoke(self, args: List[object]) -> object:
		"""No Description

		Args
		--------
			args (`List[object]`) :  args

		Returns
		--------
			`object` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Method(self) -> MethodInfo:
		"""No Description

		Returns
		--------
			`MethodInfo` : 
		"""
		pass

	@property
	def Target(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

class EnumeratedMemberFilterDelegate(ICloneable, ISerializable):

	def __new__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args
		--------
			object (`object`) :  object
			method (`IntPtr`) :  method
		"""
		pass

	def Invoke(self, enumMember: IEnumeratedMember) -> bool:
		"""No Description

		Args
		--------
			enumMember (`IEnumeratedMember`) :  enumMember

		Returns
		--------
			`bool` : 
		"""
		pass

	def BeginInvoke(self, enumMember: IEnumeratedMember, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args
		--------
			enumMember (`IEnumeratedMember`) :  enumMember
			callback (`AsyncCallback`) :  callback
			object (`object`) :  object

		Returns
		--------
			`IAsyncResult` : 
		"""
		pass

	def EndInvoke(self, result: IAsyncResult) -> bool:
		"""No Description

		Args
		--------
			result (`IAsyncResult`) :  result

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (`SerializationInfo`) :  info
			context (`StreamingContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	def GetInvocationList(self) -> List[Delegate]:
		"""No Description

		Returns
		--------
			`List[Delegate]` : 
		"""
		pass

	def DynamicInvoke(self, args: List[object]) -> object:
		"""No Description

		Args
		--------
			args (`List[object]`) :  args

		Returns
		--------
			`object` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Method(self) -> MethodInfo:
		"""No Description

		Returns
		--------
			`MethodInfo` : 
		"""
		pass

	@property
	def Target(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

class FieldLibrary:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	def DeserializeSelectionSetIDsBuffer(buffer: List[int]) -> HmIDCollection:
		"""No Description

		Args
		--------
			buffer (`List[int]`) :  buffer

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@staticmethod
	def SerializeSelectionSetIDs(ids: HmIDCollection) -> List[int]:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids

		Returns
		--------
			`List[int]` : 
		"""
		pass

	@staticmethod
	@overload
	def FilterFields(fields: Iterator, fieldFilter: FieldFilterDelegate) -> Iterator[IField]:
		"""No Description

		Args
		--------
			fields (`Iterator`) :  fields
			fieldFilter (`FieldFilterDelegate`) :  fieldFilter

		Returns
		--------
			`Iterator[IField]` : 
		"""
		pass

	@staticmethod
	@overload
	def FilterFields(fields: Iterator[IField], fieldFilter: FieldFilterDelegate) -> Iterator[IField]:
		"""No Description

		Args
		--------
			fields (`Iterator[IField]`) :  fields
			fieldFilter (`FieldFilterDelegate`) :  fieldFilter

		Returns
		--------
			`Iterator[IField]` : 
		"""
		pass

	@staticmethod
	def FilterFieldsByNumericalEngineType(fields: FieldCollection, numericalEngineTypeName: str) -> FieldCollection:
		"""No Description

		Args
		--------
			fields (`FieldCollection`) :  fields
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@staticmethod
	def GetFilteredEnumeratedMembersByNumericalEngineType(enumField: IEnumeratedField, numericalEngineTypeName: str) -> List[IEnumeratedMember]:
		"""No Description

		Args
		--------
			enumField (`IEnumeratedField`) :  enumField
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`List[IEnumeratedMember]` : 
		"""
		pass

	@staticmethod
	def GetFilteredEnumeratedMembersByProduct(enumField: IEnumeratedField, product: str) -> List[IEnumeratedMember]:
		"""No Description

		Args
		--------
			enumField (`IEnumeratedField`) :  enumField
			product (`str`) :  product

		Returns
		--------
			`List[IEnumeratedMember]` : 
		"""
		pass

	@staticmethod
	def GetSubEnumeratedFieldTypes(enumeratedFieldType: IFieldType) -> Iterator[IFieldType]:
		"""No Description

		Args
		--------
			enumeratedFieldType (`IFieldType`) :  enumeratedFieldType

		Returns
		--------
			`Iterator[IFieldType]` : 
		"""
		pass

	@staticmethod
	def FilterFieldsForPrototypes(fields: FieldCollection) -> FieldCollection:
		"""No Description

		Args
		--------
			fields (`FieldCollection`) :  fields

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@staticmethod
	def FilterFieldsForComputeCenter(fields: FieldCollection) -> FieldCollection:
		"""No Description

		Args
		--------
			fields (`FieldCollection`) :  fields

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@staticmethod
	def GetEnumFieldParentMemberIDOrZero(field: IField) -> int:
		"""No Description

		Args
		--------
			field (`IField`) :  field

		Returns
		--------
			`int` : 
		"""
		pass

	@staticmethod
	def GetIsFieldIncludedByProduct(fieldProducts: array[str], productFilter: str) -> bool:
		"""No Description

		Args
		--------
			fieldProducts (`array[str]`) :  fieldProducts
			productFilter (`str`) :  productFilter

		Returns
		--------
			`bool` : 
		"""
		pass

	@staticmethod
	def GetCommonFields(modelingElementManagers: List[IModelingElementManager], includeResultFields: bool) -> FieldCollection:
		"""No Description

		Args
		--------
			modelingElementManagers (`List[IModelingElementManager]`) :  modelingElementManagers
			includeResultFields (`bool`) :  includeResultFields

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def GetCommonFieldDescriptors(modelingElementManagers: List[IModelingElementManager], includeResultFields: bool) -> List[FieldDescriptor]:
		"""No Description

		Args
		--------
			modelingElementManagers (`List[IModelingElementManager]`) :  modelingElementManagers
			includeResultFields (`bool`) :  includeResultFields

		Returns
		--------
			`List[FieldDescriptor]` : 
		"""
		pass

	@staticmethod
	@overload
	def GetCommonFieldDescriptors(modelingElementManagers: List[IModelingElementManager], includeResultFields: bool, fieldDescriptorFilterCallback: FieldDescriptorFilterCallback) -> List[FieldDescriptor]:
		"""No Description

		Args
		--------
			modelingElementManagers (`List[IModelingElementManager]`) :  modelingElementManagers
			includeResultFields (`bool`) :  includeResultFields
			fieldDescriptorFilterCallback (`FieldDescriptorFilterCallback`) :  fieldDescriptorFilterCallback

		Returns
		--------
			`List[FieldDescriptor]` : 
		"""
		pass

	@staticmethod
	@overload
	def GetFieldsUnion(modelingElementManagers: List[IModelingElementManager], includeResultFields: bool) -> FieldCollection:
		"""No Description

		Args
		--------
			modelingElementManagers (`List[IModelingElementManager]`) :  modelingElementManagers
			includeResultFields (`bool`) :  includeResultFields

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def GetFieldsUnion(modelingElementManagers: List[IModelingElementManager], includeResultFields: bool, shouldIncludeInheritedManagers: bool) -> FieldCollection:
		"""No Description

		Args
		--------
			modelingElementManagers (`List[IModelingElementManager]`) :  modelingElementManagers
			includeResultFields (`bool`) :  includeResultFields
			shouldIncludeInheritedManagers (`bool`) :  shouldIncludeInheritedManagers

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def CopyFieldValues(fieldDescriptors: List[FieldDescriptor], sourceManager: IModelingElementManager, targetManager: IModelingElementManager, sourceElementID: int, targetElementID: int) -> None:
		"""No Description

		Args
		--------
			fieldDescriptors (`List[FieldDescriptor]`) :  fieldDescriptors
			sourceManager (`IModelingElementManager`) :  sourceManager
			targetManager (`IModelingElementManager`) :  targetManager
			sourceElementID (`int`) :  sourceElementID
			targetElementID (`int`) :  targetElementID

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	@overload
	def CopyFieldValues(dataSet: IDomainDataSet, commonFields: FieldCollection, sourceElementID: int, targetElementID: int) -> None:
		"""No Description

		Args
		--------
			dataSet (`IDomainDataSet`) :  dataSet
			commonFields (`FieldCollection`) :  commonFields
			sourceElementID (`int`) :  sourceElementID
			targetElementID (`int`) :  targetElementID

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	@overload
	def CopyFieldValues(sourceFields: FieldCollection, targetFields: FieldCollection, sourceElementID: int, targetElementID: int) -> None:
		"""No Description

		Args
		--------
			sourceFields (`FieldCollection`) :  sourceFields
			targetFields (`FieldCollection`) :  targetFields
			sourceElementID (`int`) :  sourceElementID
			targetElementID (`int`) :  targetElementID

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	@overload
	def CopyFieldValues(domainDataSet: IDomainDataSet, sourceFields: FieldCollection, targetFields: FieldCollection, sourceElementID: int, targetElementID: int) -> None:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			sourceFields (`FieldCollection`) :  sourceFields
			targetFields (`FieldCollection`) :  targetFields
			sourceElementID (`int`) :  sourceElementID
			targetElementID (`int`) :  targetElementID

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	def GetFilteredFields(fields: FieldCollection, type: FieldDataType) -> FieldCollection:
		"""No Description

		Args
		--------
			fields (`FieldCollection`) :  fields
			type (`FieldDataType`) :  type

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@staticmethod
	@overload
	def GetPersistantDataForField(field: IField) -> FieldDescriptor:
		"""No Description

		Args
		--------
			field (`IField`) :  field

		Returns
		--------
			`FieldDescriptor` : 
		"""
		pass

	@staticmethod
	@overload
	def GetPersistantDataForField(field: IField, type: DomainFieldType, name: str, descriptor1: str, descriptor2: str) -> None:
		"""No Description

		Args
		--------
			field (`IField`) :  field
			type (`DomainFieldType`) :  type
			name (`str`) :  name
			descriptor1 (`str`) :  descriptor1
			descriptor2 (`str`) :  descriptor2

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	@overload
	def GetFieldFromPersistantData(manager: IModelingElementManager, fieldDescriptor: FieldDescriptor) -> IField:
		"""No Description

		Args
		--------
			manager (`IModelingElementManager`) :  manager
			fieldDescriptor (`FieldDescriptor`) :  fieldDescriptor

		Returns
		--------
			`IField` : 
		"""
		pass

	@staticmethod
	@overload
	def GetFieldFromPersistantData(dataSet: IDomainDataSet, fieldDescriptor: FieldDescriptor) -> IField:
		"""No Description

		Args
		--------
			dataSet (`IDomainDataSet`) :  dataSet
			fieldDescriptor (`FieldDescriptor`) :  fieldDescriptor

		Returns
		--------
			`IField` : 
		"""
		pass

	@staticmethod
	@overload
	def GetFieldFromPersistantData(dataSet: IDomainDataSet, type: DomainFieldType, name: str, descriptor1: str, descriptor2: str) -> IField:
		"""No Description

		Args
		--------
			dataSet (`IDomainDataSet`) :  dataSet
			type (`DomainFieldType`) :  type
			name (`str`) :  name
			descriptor1 (`str`) :  descriptor1
			descriptor2 (`str`) :  descriptor2

		Returns
		--------
			`IField` : 
		"""
		pass

class GenericDelayedHmIDCollection(IHmIDDelayedCollection):

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			col (`HmIDCollection`) :  col
		"""
		pass

	@overload
	def __new__(self, col: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			col (`HmIDCollection`) :  col
		"""
		pass

	def Dispose(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int]) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], start: int) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], startInTarget: int, startInSource: int, length: int) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array
			startInTarget (`int`) :  startInTarget
			startInSource (`int`) :  startInSource
			length (`int`) :  length

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: int) -> bool:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`int`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: int) -> None:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IHmIDCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IHmIDCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: HmIDCollection) -> int:
		"""No Description

		Args
		--------
			x (`HmIDCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: array[int]) -> int:
		"""No Description

		Args
		--------
			x (`array[int]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Sort(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ReverseInPlace(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ToArray(self) -> array[int]:
		"""No Description

		Returns
		--------
			`array[int]` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Item.setter
	def Item(self, item: int) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class GenericHmIDDelayedCollection(IHmIDDelayedCollection):

	def __new__(self, ids: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids
		"""
		pass

	def Dispose(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int]) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], start: int) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], startInTarget: int, startInSource: int, length: int) -> None:
		"""No Description

		Args
		--------
			array (`array[int]`) :  array
			startInTarget (`int`) :  startInTarget
			startInSource (`int`) :  startInSource
			length (`int`) :  length

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: int) -> bool:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`int`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: int) -> None:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IHmIDCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IHmIDCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: HmIDCollection) -> int:
		"""No Description

		Args
		--------
			x (`HmIDCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: array[int]) -> int:
		"""No Description

		Args
		--------
			x (`array[int]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Sort(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ReverseInPlace(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ToArray(self) -> array[int]:
		"""No Description

		Returns
		--------
			`array[int]` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Item.setter
	def Item(self, item: int) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class GenericPoint(IBlobable):

	@overload
	def __new__(self, x: float, y: float) -> None:
		"""No Description

		Args
		--------
			x (`float`) :  x
			y (`float`) :  y
			buffer (`List[int]`) :  buffer
		"""
		pass

	@overload
	def __new__(self, buffer: List[int]) -> None:
		"""No Description

		Args
		--------
			x (`float`) :  x
			y (`float`) :  y
			buffer (`List[int]`) :  buffer
		"""
		pass

	def GetBytes(self) -> List[int]:
		"""No Description

		Returns
		--------
			`List[int]` : 
		"""
		pass

	def GetNumberOfBytes(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def X(self) -> float:
		"""No Description

		Returns
		--------
			`float` : 
		"""
		pass

	@X.setter
	def X(self, x: float) -> None:
		pass

	@property
	def Y(self) -> float:
		"""No Description

		Returns
		--------
			`float` : 
		"""
		pass

	@Y.setter
	def Y(self, y: float) -> None:
		pass

class IDataSource:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddDomainDataSetType(self, name: str) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	@overload
	def DomainDataSetType(self, id: int) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	@overload
	def DomainDataSetType(self, name: str) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	def GetDomainDataSetTypeID(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`int` : 
		"""
		pass

	def SupportedDataSetTypes(self) -> DomainDataSetTypeCollection:
		"""No Description

		Returns
		--------
			`DomainDataSetTypeCollection` : 
		"""
		pass

	def GetCurrentlyHiddenDomainDataSetTypes(self) -> DomainDataSetTypeCollection:
		"""No Description

		Returns
		--------
			`DomainDataSetTypeCollection` : 
		"""
		pass

	def AddSubDomainDataSetType(self, name: str, parentDomainDataSetTypeID: int) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			parentDomainDataSetTypeID (`int`) :  parentDomainDataSetTypeID

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	def SubDomainDataSetTypeExists(self, parentDomainDataSetTypeID: int, subDomainDataSetTypeName: str) -> bool:
		"""No Description

		Args
		--------
			parentDomainDataSetTypeID (`int`) :  parentDomainDataSetTypeID
			subDomainDataSetTypeName (`str`) :  subDomainDataSetTypeName

		Returns
		--------
			`bool` : 
		"""
		pass

	def SupportedSubDataSetTypes(self, parentDomainDataSetTypeID: int) -> DomainDataSetTypeCollection:
		"""No Description

		Args
		--------
			parentDomainDataSetTypeID (`int`) :  parentDomainDataSetTypeID

		Returns
		--------
			`DomainDataSetTypeCollection` : 
		"""
		pass

	@property
	def DomainDataSetManager(self) -> IDomainDataSetManager:
		"""No Description

		Returns
		--------
			`IDomainDataSetManager` : 
		"""
		pass

	@property
	def ActiveDataSetTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActiveDataSetTypeID.setter
	def ActiveDataSetTypeID(self, activedatasettypeid: int) -> None:
		pass

class IDataSourceConnection:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Open(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Close(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def IsOpen(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def IsDataSource(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def BeginSchemaEdit(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def LoadSchema(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def EndSchemaEdit(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Compact(self, context: CompactOperationContext) -> None:
		"""No Description

		Args
		--------
			context (`CompactOperationContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	def UpdateCaches(self, context: CompactOperationContext) -> None:
		"""No Description

		Args
		--------
			context (`CompactOperationContext`) :  context

		Returns
		--------
			`None` : 
		"""
		pass

	def ComputeBoundingBox(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ExecuteSchemaUpdate(self, domainDataSetTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainDataSetTypeID (`int`) :  domainDataSetTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def Flush(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ClearConnectionCaches(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Deactivate(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def CreateExtendedProperty(self, propertyName: str, type: FieldDataType, defaultValue: object) -> None:
		"""No Description

		Args
		--------
			propertyName (`str`) :  propertyName
			type (`FieldDataType`) :  type
			defaultValue (`object`) :  defaultValue

		Returns
		--------
			`None` : 
		"""
		pass

	def GetExtendedPropertyValue(self, propertyName: str) -> object:
		"""No Description

		Args
		--------
			propertyName (`str`) :  propertyName

		Returns
		--------
			`object` : 
		"""
		pass

	def SetExtendedPropertyValue(self, propertyName: str, propertyValue: object) -> None:
		"""No Description

		Args
		--------
			propertyName (`str`) :  propertyName
			propertyValue (`object`) :  propertyValue

		Returns
		--------
			`None` : 
		"""
		pass

	def SetConnectionProperty(self, key: ConnectionProperty, val: object) -> None:
		"""No Description

		Args
		--------
			key (`ConnectionProperty`) :  key
			val (`object`) :  val

		Returns
		--------
			`None` : 
		"""
		pass

	def GetConnectionProperty(self, key: ConnectionProperty) -> object:
		"""No Description

		Args
		--------
			key (`ConnectionProperty`) :  key

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def IsSchemaEditing(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class ITransactionalConnection:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def BeginTransaction(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def CommitTransaction(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def RollbackTransaction(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

class IDataSourceMessaging:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Initialize(self, questionHandler: IMessageQuestionHandler, progressIndicator: IProgressIndicator) -> None:
		"""No Description

		Args
		--------
			questionHandler (`IMessageQuestionHandler`) :  questionHandler
			progressIndicator (`IProgressIndicator`) :  progressIndicator

		Returns
		--------
			`None` : 
		"""
		pass

class IDataSourceSchemaUpdateResults:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetNewElementIdForOldElementId(self, elementTypeId: int, oldElementId: int) -> int:
		"""No Description

		Args
		--------
			elementTypeId (`int`) :  elementTypeId
			oldElementId (`int`) :  oldElementId

		Returns
		--------
			`int` : 
		"""
		pass

	def GetUpdatedDomainFieldInformation(self, elementTypeId: int, oldFieldName: str) -> IUpdatedFieldInformation:
		"""No Description

		Args
		--------
			elementTypeId (`int`) :  elementTypeId
			oldFieldName (`str`) :  oldFieldName

		Returns
		--------
			`IUpdatedFieldInformation` : 
		"""
		pass

	def GetUpdatedSupportFieldInformation(self, elementTypeId: int, oldFieldName: str) -> IUpdatedFieldInformation:
		"""No Description

		Args
		--------
			elementTypeId (`int`) :  elementTypeId
			oldFieldName (`str`) :  oldFieldName

		Returns
		--------
			`IUpdatedFieldInformation` : 
		"""
		pass

	def GetOldDomainFieldNamesThatHaveChanged(self, elementTypeId: int) -> List[str]:
		"""No Description

		Args
		--------
			elementTypeId (`int`) :  elementTypeId

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def CreateSchemaStringMap(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def ElementIdsWereChanged(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def HasFieldChanges(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class IElementType:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def IsStandardType(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class IElementTypeUpdatable:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetId(self, newId: int) -> None:
		"""No Description

		Args
		--------
			newId (`int`) :  newId

		Returns
		--------
			`None` : 
		"""
		pass

	def SetName(self, newName: str) -> None:
		"""No Description

		Args
		--------
			newName (`str`) :  newName

		Returns
		--------
			`None` : 
		"""
		pass

class IFieldType(IElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def FieldDataType(self) -> FieldDataType:
		"""No Description

		Returns
		--------
			`FieldDataType` : 
		"""
		pass

	@overload
	def FieldDataType(self, type: FieldDataType) -> None:
		"""No Description

		Args
		--------
			type (`FieldDataType`) :  type

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def Type(self) -> Type:
		"""No Description

		Returns
		--------
			`Type` : 
		"""
		pass

	@overload
	def Type(self, type: Type) -> None:
		"""No Description

		Args
		--------
			type (`Type`) :  type

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def StorageUnit(self) -> UnitIndex:
		"""No Description

		Returns
		--------
			`UnitIndex` : 
		"""
		pass

	@overload
	def StorageUnit(self, unit: UnitIndex) -> None:
		"""No Description

		Args
		--------
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def TextLength(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def TextLength(self, length: int) -> None:
		"""No Description

		Args
		--------
			length (`int`) :  length

		Returns
		--------
			`None` : 
		"""
		pass

	def GetReferenceElementType(self) -> IElementType:
		"""No Description

		Returns
		--------
			`IElementType` : 
		"""
		pass

	def SetReferenceElementType(self, elementType: IElementType) -> None:
		"""No Description

		Args
		--------
			elementType (`IElementType`) :  elementType

		Returns
		--------
			`None` : 
		"""
		pass

	def SetIsReadOnly(self, value: bool) -> None:
		"""No Description

		Args
		--------
			value (`bool`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def GetReferenceCardinality(self) -> ReferenceCardinality:
		"""No Description

		Returns
		--------
			`ReferenceCardinality` : 
		"""
		pass

	def SetReferenceCardinality(self, cardinality: ReferenceCardinality) -> None:
		"""No Description

		Args
		--------
			cardinality (`ReferenceCardinality`) :  cardinality

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def DefaultValue(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@overload
	def DefaultValue(self, value: object) -> None:
		"""No Description

		Args
		--------
			value (`object`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@overload
	def CollectionFieldType(self, fieldTypeId: int) -> IFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (`int`) :  fieldTypeId

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@overload
	def CollectionFieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def CollectionFieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	def CollectionFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def EnumeratedTypeMemberExists(self, value: int) -> bool:
		"""No Description

		Args
		--------
			value (`int`) :  value

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetEnumeratedTypeMembers(self) -> List[IEnumeratedTypeMember]:
		"""No Description

		Returns
		--------
			`List[IEnumeratedTypeMember]` : 
		"""
		pass

	def SetEnumeratedTypeMembers(self, names: array[str], values: array[int]) -> List[IEnumeratedTypeMember]:
		"""No Description

		Args
		--------
			names (`array[str]`) :  names
			values (`array[int]`) :  values

		Returns
		--------
			`List[IEnumeratedTypeMember]` : 
		"""
		pass

	def GetNumericalRange(self, minValue: float, maxValue: float) -> None:
		"""No Description

		Args
		--------
			minValue (`float`) :  minValue
			maxValue (`float`) :  maxValue

		Returns
		--------
			`None` : 
		"""
		pass

	def SetNumericalRange(self, minValue: float, maxValue: float) -> None:
		"""No Description

		Args
		--------
			minValue (`float`) :  minValue
			maxValue (`float`) :  maxValue

		Returns
		--------
			`None` : 
		"""
		pass

	def GetSharedEnumeratedMembers(self) -> List[IEnumeratedTypeMember]:
		"""No Description

		Returns
		--------
			`List[IEnumeratedTypeMember]` : 
		"""
		pass

	def GetFilteringByProduct(self) -> List[str]:
		"""No Description

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def SetFilteringByProduct(self, products: List[str]) -> None:
		"""No Description

		Args
		--------
			products (`List[str]`) :  products

		Returns
		--------
			`None` : 
		"""
		pass

	def GetUniqueId(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

	def SetUniqueId(self, uuid: Guid) -> None:
		"""No Description

		Args
		--------
			uuid (`Guid`) :  uuid

		Returns
		--------
			`None` : 
		"""
		pass

	def GetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (`str`) :  factoryClassName
			methodName (`str`) :  methodName
			parameters (`Dict[str,str]`) :  parameters

		Returns
		--------
			`None` : 
		"""
		pass

	def SetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (`str`) :  factoryClassName
			methodName (`str`) :  methodName
			parameters (`Dict[str,str]`) :  parameters

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Category(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Category.setter
	def Category(self, category: str) -> None:
		pass

	@property
	def IsEnumeratedMemberField(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsSharedEnumeratedMemberField(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def ParentEnumeratedTypeMember(self) -> IEnumeratedTypeMember:
		"""No Description

		Returns
		--------
			`IEnumeratedTypeMember` : 
		"""
		pass

	@property
	def IsCollectionMemberField(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def ParentCollectionFieldType(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsSerializedAsBinary(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsSerializedAsBinary.setter
	def IsSerializedAsBinary(self, isserializedasbinary: bool) -> None:
		pass

	@property
	def OrderIndex(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@OrderIndex.setter
	def OrderIndex(self, orderindex: int) -> None:
		pass

	@property
	def NumericFormatterName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@NumericFormatterName.setter
	def NumericFormatterName(self, numericformattername: str) -> None:
		pass

class IFieldTypeEx:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	def GetSharedEnumeratedMemberFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

class IFieldTypeUI:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetBlankIfReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def SetBlankIfReadOnly(self, val: bool) -> None:
		"""No Description

		Args
		--------
			val (`bool`) :  val

		Returns
		--------
			`None` : 
		"""
		pass

	def GetRefreshDependentsOnChange(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def SetRefreshDependentsOnChange(self, val: bool) -> None:
		"""No Description

		Args
		--------
			val (`bool`) :  val

		Returns
		--------
			`None` : 
		"""
		pass

	def GetAssociatedElementTypes(self) -> List[IElementType]:
		"""No Description

		Returns
		--------
			`List[IElementType]` : 
		"""
		pass

	def SetAssociatedElementTypes(self, elementTypes: List[IElementType]) -> None:
		"""No Description

		Args
		--------
			elementTypes (`List[IElementType]`) :  elementTypes

		Returns
		--------
			`None` : 
		"""
		pass

	def GetFilteringByNumericalEngineType(self) -> List[str]:
		"""No Description

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def SetFilteringByNumericalEngineType(self, numericalEngineTypes: List[str]) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypes (`List[str]`) :  numericalEngineTypes

		Returns
		--------
			`None` : 
		"""
		pass

	def GetHideInPrototypes(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def SetHideInPrototypes(self, val: bool) -> None:
		"""No Description

		Args
		--------
			val (`bool`) :  val

		Returns
		--------
			`None` : 
		"""
		pass

class IFieldTypeInternal:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetEnumeratedTypeMember(self, enumeratedTypeMemberID: int) -> IEnumeratedTypeMember:
		"""No Description

		Args
		--------
			enumeratedTypeMemberID (`int`) :  enumeratedTypeMemberID

		Returns
		--------
			`IEnumeratedTypeMember` : 
		"""
		pass

class IEnumeratedTypeMember(IElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, serializeAsBinary: bool) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			serializeAsBinary (`bool`) :  serializeAsBinary

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def GetFieldTypeNamed(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def DeleteFieldType(self, attributeTypeID: int) -> None:
		"""No Description

		Args
		--------
			attributeTypeID (`int`) :  attributeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def GetFilteringByProduct(self) -> List[str]:
		"""No Description

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def SetFilteringByProduct(self, products: List[str]) -> None:
		"""No Description

		Args
		--------
			products (`List[str]`) :  products

		Returns
		--------
			`None` : 
		"""
		pass

	def GetFilteringByNumericalEngineType(self) -> List[str]:
		"""No Description

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def SetFilteringByNumericalEngineType(self, numericalEngineTypeNames: List[str]) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeNames (`List[str]`) :  numericalEngineTypeNames

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def ParentFieldType(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@property
	def EnumerationValue(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IEnumeratedTypeMemberUpdatable:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def RefactorSubEnumFieldTypeToNonEnumerated(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`None` : 
		"""
		pass

class IModelingElementFieldType(IFieldType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			`ModelingElementType` : 
		"""
		pass

	@property
	def ElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class ISupportElementFieldType(IFieldType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportElementType(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

	@property
	def TableName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

class ICalculationOptionsFieldType(IFieldType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def NumericalEngineType(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@property
	def ShowInComputeCenter(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ShowInComputeCenter.setter
	def ShowInComputeCenter(self, showincomputecenter: bool) -> None:
		pass

class IResultFieldType(IFieldType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportedDomainElementTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@property
	def ResultRecordType(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

	@property
	def IsTimeVariant(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsTimeVariant.setter
	def IsTimeVariant(self, istimevariant: bool) -> None:
		pass

	@property
	def Expression(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Expression.setter
	def Expression(self, expression: str) -> None:
		pass

	@property
	def ExpressionType(self) -> ExpressionType:
		"""No Description

		Returns
		--------
			`ExpressionType` : 
		"""
		pass

	@ExpressionType.setter
	def ExpressionType(self, expressiontype: ExpressionType) -> None:
		pass

class IDomainElementFieldType(IFieldType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TableName(self, domainElementTypeID: int) -> str:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`str` : 
		"""
		pass

	def SupportedDomainElementTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

class ISystemRecordFieldType(IFieldType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

class ISupportElementType(IModelingElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`ISupportElementFieldType` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, serializeAsBinary: bool) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			serializeAsBinary (`bool`) :  serializeAsBinary

		Returns
		--------
			`ISupportElementFieldType` : 
		"""
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType, enumFieldTypeID: int, sharedEnumMembers: array[str]) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type
			enumFieldTypeID (`int`) :  enumFieldTypeID
			sharedEnumMembers (`array[str]`) :  sharedEnumMembers

		Returns
		--------
			`ISupportElementFieldType` : 
		"""
		pass

	def DeleteFieldType(self, supportElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			supportElementFieldTypeID (`int`) :  supportElementFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def FieldType(self, fieldTypeId: int) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (`int`) :  fieldTypeId

		Returns
		--------
			`ISupportElementFieldType` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`ISupportElementFieldType` : 
		"""
		pass

	def GetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (`str`) :  factoryClassName
			methodName (`str`) :  methodName
			parameters (`Dict[str,str]`) :  parameters

		Returns
		--------
			`None` : 
		"""
		pass

	def SetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (`str`) :  factoryClassName
			methodName (`str`) :  methodName
			parameters (`Dict[str,str]`) :  parameters

		Returns
		--------
			`None` : 
		"""
		pass

class ITreeElementType(IElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SubElementTypes(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@property
	def ParentID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class ITreeElementTypeUpdatable:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetParentID(self, newParentID: int) -> None:
		"""No Description

		Args
		--------
			newParentID (`int`) :  newParentID

		Returns
		--------
			`None` : 
		"""
		pass

class IAlternativeType(IModelingElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`IDomainElementFieldType` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, serializeAsBinary: bool) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			serializeAsBinary (`bool`) :  serializeAsBinary

		Returns
		--------
			`IDomainElementFieldType` : 
		"""
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType, enumFieldTypeID: int, sharedEnumMembers: array[str]) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type
			enumFieldTypeID (`int`) :  enumFieldTypeID
			sharedEnumMembers (`array[str]`) :  sharedEnumMembers

		Returns
		--------
			`IDomainElementFieldType` : 
		"""
		pass

	def AddSystemRecordFieldType(self, name: str, type: FieldDataType) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`ISystemRecordFieldType` : 
		"""
		pass

	def AddSystemRecordCollectionFieldType(self, name: str, serializeAsBinary: bool) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			serializeAsBinary (`bool`) :  serializeAsBinary

		Returns
		--------
			`ISystemRecordFieldType` : 
		"""
		pass

	def SystemRecordFieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	def DeleteSystemRecordFieldType(self, systemRecordFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			systemRecordFieldTypeID (`int`) :  systemRecordFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IDomainElementFieldType` : 
		"""
		pass

	@overload
	def FieldType(self, attributeTypeId: int) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			attributeTypeId (`int`) :  attributeTypeId

		Returns
		--------
			`IDomainElementFieldType` : 
		"""
		pass

	@overload
	def SystemRecordFieldType(self, fieldTypeId: int) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (`int`) :  fieldTypeId

		Returns
		--------
			`ISystemRecordFieldType` : 
		"""
		pass

	@overload
	def SystemRecordFieldType(self, name: str) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`ISystemRecordFieldType` : 
		"""
		pass

	def SystemRecordFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@overload
	def FieldTypes(self, domainElementTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@overload
	def FieldTypes(self, domainElementTypeID: int, excludeInherited: bool) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID
			excludeInherited (`bool`) :  excludeInherited

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def DeleteFieldType(self, domainElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (`int`) :  domainElementFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def SupportedDomainElementTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def DropObsoleteObjects(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

class IAlternativeTypeUI:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetHideInUI(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def SetHideInUI(self, value: bool) -> None:
		"""No Description

		Args
		--------
			value (`bool`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

class IDomainElementType(ITreeElementType, IModelingElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DomainElementShapeType(self) -> DomainElementShapeType:
		"""No Description

		Returns
		--------
			`DomainElementShapeType` : 
		"""
		pass

	@overload
	def AddFieldType(self, domainElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (`int`) :  domainElementFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def AddFieldType(self, name: str, dataType: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			dataType (`FieldDataType`) :  dataType

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@overload
	def SupportsFieldType(self, domainElementFieldTypeID: int) -> bool:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (`int`) :  domainElementFieldTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def SupportsFieldType(self, domainElementFieldTypeID: int, includeParentTypes: bool) -> bool:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (`int`) :  domainElementFieldTypeID
			includeParentTypes (`bool`) :  includeParentTypes

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def SupportsResultFieldType(self, resultFieldTypeID: int) -> bool:
		"""No Description

		Args
		--------
			resultFieldTypeID (`int`) :  resultFieldTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def SupportsResultFieldType(self, resultFieldTypeID: int, includeParentTypes: bool) -> bool:
		"""No Description

		Args
		--------
			resultFieldTypeID (`int`) :  resultFieldTypeID
			includeParentTypes (`bool`) :  includeParentTypes

		Returns
		--------
			`bool` : 
		"""
		pass

	def DropFieldType(self, domainElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (`int`) :  domainElementFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def RefactorFieldTypeUp(self, domainElementFieldTypeID: int, parentElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (`int`) :  domainElementFieldTypeID
			parentElementTypeID (`int`) :  parentElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def RefactorFieldTypeDown(self, domainElementFieldTypeID: int, parentElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (`int`) :  domainElementFieldTypeID
			parentElementTypeID (`int`) :  parentElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def AddResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (`int`) :  resultFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def DropResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (`int`) :  resultFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def FieldTypes(self, nonAlternativeFieldTypesOnly: bool) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			nonAlternativeFieldTypesOnly (`bool`) :  nonAlternativeFieldTypesOnly

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@overload
	def FieldTypes(self, alternativeTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@overload
	def FieldTypes(self, alternativeTypeID: int, includeParentTypes: bool) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID
			includeParentTypes (`bool`) :  includeParentTypes

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def SupportedAlternativeTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def SupportsAlternativeType(self, alternativeTypeID: int, includeParentTypes: bool) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID
			includeParentTypes (`bool`) :  includeParentTypes

		Returns
		--------
			`bool` : 
		"""
		pass

	def DeleteFieldType(self, fieldTypeId: int) -> None:
		"""No Description

		Args
		--------
			fieldTypeId (`int`) :  fieldTypeId

		Returns
		--------
			`None` : 
		"""
		pass

	def SupportedResultRecordTypeNames(self) -> StringCollection:
		"""No Description

		Returns
		--------
			`StringCollection` : 
		"""
		pass

	@overload
	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

class IDomainElementTypeEx:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def FieldTypeExists(self, name: str, includeHierarchy: bool) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name
			includeHierarchy (`bool`) :  includeHierarchy

		Returns
		--------
			`bool` : 
		"""
		pass

class IModelingElementTypeUI:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def OrderIndex(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@OrderIndex.setter
	def OrderIndex(self, orderindex: int) -> None:
		pass

class IDomainDataSetType(IElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def DeleteFieldType(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`None` : 
		"""
		pass

	def FieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	def FieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def ModelingElementType(self, type: ModelingElementType) -> IStandardModelingElementType:
		"""No Description

		Args
		--------
			type (`ModelingElementType`) :  type

		Returns
		--------
			`IStandardModelingElementType` : 
		"""
		pass

	def AddAlternativeType(self, name: str) -> IAlternativeType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	def AddStandardAlternativeType(self, standardAlternativeTypeName: str) -> IAlternativeType:
		"""No Description

		Args
		--------
			standardAlternativeTypeName (`str`) :  standardAlternativeTypeName

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	@overload
	def AlternativeTypeExists(self, alternativeTypeName: str) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def AlternativeTypeExists(self, alternativeTypeID: int) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def AlternativeType(self, alternativeTypeID: int) -> IAlternativeType:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	@overload
	def AlternativeType(self, alternativeTypeName: str) -> IAlternativeType:
		"""No Description

		Args
		--------
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	def DeleteAlternativeType(self, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def AlternativeTypes(self) -> AlternativeTypeCollection:
		"""No Description

		Returns
		--------
			`AlternativeTypeCollection` : 
		"""
		pass

	@overload
	def AddDomainElementType(self, name: str, shapeType: DomainElementShapeType) -> IDomainElementType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			shapeType (`DomainElementShapeType`) :  shapeType

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@overload
	def AddDomainElementType(self, name: str, shapeType: DomainElementShapeType, standardAlternativeTypesToSupport: StringCollection) -> IDomainElementType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			shapeType (`DomainElementShapeType`) :  shapeType
			standardAlternativeTypesToSupport (`StringCollection`) :  standardAlternativeTypesToSupport

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@overload
	def AddDomainElementType(self, name: str, shapeType: DomainElementShapeType, parentDomainElementTypeID: int) -> IDomainElementType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			shapeType (`DomainElementShapeType`) :  shapeType
			parentDomainElementTypeID (`int`) :  parentDomainElementTypeID

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@overload
	def DomainElementType(self, domainElementTypeID: int) -> IDomainElementType:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@overload
	def DomainElementType(self, domainElementTypeName: str) -> IDomainElementType:
		"""No Description

		Args
		--------
			domainElementTypeName (`str`) :  domainElementTypeName

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@overload
	def DomainElementTypeExists(self, domainElementTypeID: int) -> bool:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def DomainElementTypeExists(self, domainElementTypeName: str) -> bool:
		"""No Description

		Args
		--------
			domainElementTypeName (`str`) :  domainElementTypeName

		Returns
		--------
			`bool` : 
		"""
		pass

	def DeleteDomainElementType(self, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def DomainElementTypes(self) -> DomainElementTypeCollection:
		"""No Description

		Returns
		--------
			`DomainElementTypeCollection` : 
		"""
		pass

	@overload
	def DomainElementTypes(self, includeBaseTypes: bool) -> DomainElementTypeCollection:
		"""No Description

		Args
		--------
			includeBaseTypes (`bool`) :  includeBaseTypes

		Returns
		--------
			`DomainElementTypeCollection` : 
		"""
		pass

	def AddSupportElementType(self, name: str) -> ISupportElementType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

	@overload
	def SupportElementType(self, supportElementTypeID: int) -> ISupportElementType:
		"""No Description

		Args
		--------
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

	@overload
	def SupportElementType(self, supportElementTypeName: str) -> ISupportElementType:
		"""No Description

		Args
		--------
			supportElementTypeName (`str`) :  supportElementTypeName

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

	@overload
	def SupportElementTypeExists(self, supportElementTypeName: str) -> bool:
		"""No Description

		Args
		--------
			supportElementTypeName (`str`) :  supportElementTypeName

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def SupportElementTypeExists(self, supportElementTypeID: int) -> bool:
		"""No Description

		Args
		--------
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	def DeleteSupportElementType(self, supportElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def SupportElementTypes(self) -> SupportElementTypeCollection:
		"""No Description

		Returns
		--------
			`SupportElementTypeCollection` : 
		"""
		pass

	def AddNumericalEngineType(self, name: str) -> INumericalEngineType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@overload
	def NumericalEngineType(self, name: str) -> INumericalEngineType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@overload
	def NumericalEngineType(self, numericalEngineTypeID: int) -> INumericalEngineType:
		"""No Description

		Args
		--------
			numericalEngineTypeID (`int`) :  numericalEngineTypeID

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@overload
	def NumericalEngineTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def NumericalEngineTypeExists(self, numericalEngineTypeID: int) -> bool:
		"""No Description

		Args
		--------
			numericalEngineTypeID (`int`) :  numericalEngineTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	def DeleteNumericalEngineType(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`None` : 
		"""
		pass

	def NumericalEngineTypes(self) -> NumericalEngineTypeCollection:
		"""No Description

		Returns
		--------
			`NumericalEngineTypeCollection` : 
		"""
		pass

	def GetMainNumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	def SetMainNumericalEngineTypeName(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`None` : 
		"""
		pass

	def AddResultRecordType(self, name: str) -> IResultRecordType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

	def ResultRecordType(self, resultRecordTypeName: str) -> IResultRecordType:
		"""No Description

		Args
		--------
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

	def ResultRecordTypeExists(self, resultRecordTypeName: str) -> bool:
		"""No Description

		Args
		--------
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`bool` : 
		"""
		pass

	def ResultRecordTypes(self) -> ResultRecordTypeCollection:
		"""No Description

		Returns
		--------
			`ResultRecordTypeCollection` : 
		"""
		pass

	def AddNumericFormatter(self, name: str) -> NumericFormatter:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`NumericFormatter` : 
		"""
		pass

	def NumericFormatter(self, name: str) -> NumericFormatter:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`NumericFormatter` : 
		"""
		pass

	def NumericFormatters(self) -> StringCollection:
		"""No Description

		Returns
		--------
			`StringCollection` : 
		"""
		pass

	def AddStoredQuery(self, name: str, type: StoredQueryType, queryText: str) -> IStoredQuery:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`StoredQueryType`) :  type
			queryText (`str`) :  queryText

		Returns
		--------
			`IStoredQuery` : 
		"""
		pass

	def DeleteStoredQuery(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`None` : 
		"""
		pass

	def StoredQuery(self, name: str) -> IStoredQuery:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IStoredQuery` : 
		"""
		pass

	def StoredQueryExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	def StoredQueryNames(self) -> StringCollection:
		"""No Description

		Returns
		--------
			`StringCollection` : 
		"""
		pass

	def GetSchemaVersion(self) -> Version:
		"""No Description

		Returns
		--------
			`Version` : 
		"""
		pass

	def SetSchemaVersion(self, version: Version) -> None:
		"""No Description

		Args
		--------
			version (`Version`) :  version

		Returns
		--------
			`None` : 
		"""
		pass

	def AddProduct(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`None` : 
		"""
		pass

	def ProductExists(self, productName: str) -> bool:
		"""No Description

		Args
		--------
			productName (`str`) :  productName

		Returns
		--------
			`bool` : 
		"""
		pass

	def Products(self) -> List[str]:
		"""No Description

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def DeleteProduct(self, productName: str) -> None:
		"""No Description

		Args
		--------
			productName (`str`) :  productName

		Returns
		--------
			`None` : 
		"""
		pass

	def GetMainTextResourceAssemblyName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	def SetMainTextResourceAssemblyName(self, assemblyName: str) -> None:
		"""No Description

		Args
		--------
			assemblyName (`str`) :  assemblyName

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def DataSource(self) -> IDataSource:
		"""No Description

		Returns
		--------
			`IDataSource` : 
		"""
		pass

	@property
	def ParentDomainDataSetTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def CanBeHidden(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@CanBeHidden.setter
	def CanBeHidden(self, canbehidden: bool) -> None:
		pass

	@property
	def ActiveProductFilter(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@ActiveProductFilter.setter
	def ActiveProductFilter(self, activeproductfilter: str) -> None:
		pass

class IDomainDataSetTypeRefactoring:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveFieldTypesBetweenAlternativeTypes(self, fieldTypes: FieldTypeCollection, targetAlternativeType: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			fieldTypes (`FieldTypeCollection`) :  fieldTypes
			targetAlternativeType (`IAlternativeType`) :  targetAlternativeType

		Returns
		--------
			`None` : 
		"""
		pass

class IStoredQuery(IElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def QueryText(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@QueryText.setter
	def QueryText(self, querytext: str) -> None:
		pass

	@property
	def QueryType(self) -> StoredQueryType:
		"""No Description

		Returns
		--------
			`StoredQueryType` : 
		"""
		pass

class IModelingElementType(IElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def FieldType(self, fieldTypeId: int) -> IFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (`int`) :  fieldTypeId

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def FieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@property
	def DomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

class IStandardModelingElementType(IModelingElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddModelingElementFieldType(self, fieldName: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			type (`FieldDataType`) :  type

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def AddModelingElementCollectionFieldType(self, fieldName: str, serializeAsBinary: bool) -> IFieldType:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			serializeAsBinary (`bool`) :  serializeAsBinary

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def ModelingElementFieldTypeExists(self, fieldName: str, elementTypeID: int) -> bool:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			elementTypeID (`int`) :  elementTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	def ModelingElementFieldType(self, fieldName: str) -> IFieldType:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def ModelingElementFieldTypes(self, elementTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			elementTypeID (`int`) :  elementTypeID

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@property
	def ModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			`ModelingElementType` : 
		"""
		pass

class INumericalEngineType(IModelingElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (`int`) :  resultFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def SupportedResultRecordTypeNames(self) -> StringCollection:
		"""No Description

		Returns
		--------
			`StringCollection` : 
		"""
		pass

	def ResultFieldType(self, name: str, resultRecordTypeName: str) -> IResultFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`IResultFieldType` : 
		"""
		pass

	def ResultFieldTypes(self, resultRecordTypeName: str, domainElementTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			resultRecordTypeName (`str`) :  resultRecordTypeName
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def ScenarioResultFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def DropResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (`int`) :  resultFieldTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def AddCalculationOptionsFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@overload
	def AddCalculationOptionsFieldType(self, name: str, type: FieldDataType, enumFieldTypeID: int, sharedEnumMembers: array[str]) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type
			enumFieldTypeID (`int`) :  enumFieldTypeID
			sharedEnumMembers (`array[str]`) :  sharedEnumMembers

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def AddCalculationOptionsCollectionFieldType(self, name: str, serializeAsBinary: bool) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			serializeAsBinary (`bool`) :  serializeAsBinary

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def CalculationOptionsFieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def CalculationOptionsFieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	def CalculationOptionsFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	def DeleteCalculationOptionsFieldType(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`None` : 
		"""
		pass

	def SupportsFieldType(self, fieldTypeID: int) -> bool:
		"""No Description

		Args
		--------
			fieldTypeID (`int`) :  fieldTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	def MakeComposite(self, subNumericalEngineTypes: List[INumericalEngineType], defaultActiveNumericalEngineType: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			subNumericalEngineTypes (`List[INumericalEngineType]`) :  subNumericalEngineTypes
			defaultActiveNumericalEngineType (`INumericalEngineType`) :  defaultActiveNumericalEngineType

		Returns
		--------
			`None` : 
		"""
		pass

	def GetFilteringByProduct(self) -> List[str]:
		"""No Description

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def SetFilteringByProduct(self, products: List[str]) -> None:
		"""No Description

		Args
		--------
			products (`List[str]`) :  products

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def CalculationAssemblyName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@CalculationAssemblyName.setter
	def CalculationAssemblyName(self, calculationassemblyname: str) -> None:
		pass

	@property
	def CalculationClassName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@CalculationClassName.setter
	def CalculationClassName(self, calculationclassname: str) -> None:
		pass

	@property
	def IsComposite(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class IResultRecordType(IElementType):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`FieldDataType`) :  type

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def DeleteFieldType(self, resultFieldTypeId: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeId (`int`) :  resultFieldTypeId

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@overload
	def FieldType(self, fieldTypeId: int) -> IFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (`int`) :  fieldTypeId

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	def FieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			`FieldTypeCollection` : 
		"""
		pass

	@property
	def DomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

class IDomainDatabaseContext:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CurrentDomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

	def CurrentDbConnection(self) -> DbConnection:
		"""No Description

		Returns
		--------
			`DbConnection` : 
		"""
		pass

	def Flush(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

class IDomainDataSetManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddDomainDataSet(self, domainDataSetTypeID: int, name: str) -> IDomainDataSet:
		"""No Description

		Args
		--------
			domainDataSetTypeID (`int`) :  domainDataSetTypeID
			name (`str`) :  name

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

	def DomainDataSet(self, domainDataSetID: int) -> IDomainDataSet:
		"""No Description

		Args
		--------
			domainDataSetID (`int`) :  domainDataSetID

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

	def DomainDataSets(self, domainDataSetTypeID: int) -> DomainDataSetCollection:
		"""No Description

		Args
		--------
			domainDataSetTypeID (`int`) :  domainDataSetTypeID

		Returns
		--------
			`DomainDataSetCollection` : 
		"""
		pass

	def DeleteDomainDataSet(self, domainDataSetID: int) -> None:
		"""No Description

		Args
		--------
			domainDataSetID (`int`) :  domainDataSetID

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def DataSource(self) -> IDataSource:
		"""No Description

		Returns
		--------
			`IDataSource` : 
		"""
		pass

class IDomainDataSet:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Exists(self, modelingElementID: int) -> bool:
		"""No Description

		Args
		--------
			modelingElementID (`int`) :  modelingElementID

		Returns
		--------
			`bool` : 
		"""
		pass

	def AlternativeTypeID(self, alternativeID: int) -> int:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`int` : 
		"""
		pass

	def DomainElementTypeID(self, domainElementID: int) -> int:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`int` : 
		"""
		pass

	def NumericalEngineTypeName(self, calculationOptionsID: int) -> str:
		"""No Description

		Args
		--------
			calculationOptionsID (`int`) :  calculationOptionsID

		Returns
		--------
			`str` : 
		"""
		pass

	def DomainElementTypeIDs(self) -> IHmIDToObjectDictionary:
		"""No Description

		Returns
		--------
			`IHmIDToObjectDictionary` : 
		"""
		pass

	def SupportElementTypeID(self, supportElementID: int) -> int:
		"""No Description

		Args
		--------
			supportElementID (`int`) :  supportElementID

		Returns
		--------
			`int` : 
		"""
		pass

	def ModelingElementType(self, elementID: int) -> ModelingElementType:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`ModelingElementType` : 
		"""
		pass

	def NumericalEngine(self, numericalEngineType: str) -> INumericalEngine:
		"""No Description

		Args
		--------
			numericalEngineType (`str`) :  numericalEngineType

		Returns
		--------
			`INumericalEngine` : 
		"""
		pass

	def DomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	def GeometryAlternativeManager(self) -> IAlternativeManager:
		"""No Description

		Returns
		--------
			`IAlternativeManager` : 
		"""
		pass

	@overload
	def AlternativeManager(self, alternativeTypeID: int) -> IAlternativeManager:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`IAlternativeManager` : 
		"""
		pass

	@overload
	def AlternativeManager(self, alternativeTypeName: str) -> IAlternativeManager:
		"""No Description

		Args
		--------
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`IAlternativeManager` : 
		"""
		pass

	@overload
	def DomainElementManager(self, domainElementTypeID: int) -> IDomainElementManager:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IDomainElementManager` : 
		"""
		pass

	@overload
	def DomainElementManager(self, domainElementTypeName: str) -> IDomainElementManager:
		"""No Description

		Args
		--------
			domainElementTypeName (`str`) :  domainElementTypeName

		Returns
		--------
			`IDomainElementManager` : 
		"""
		pass

	@overload
	def SupportElementManager(self, supportElementTypeID: int) -> ISupportElementManager:
		"""No Description

		Args
		--------
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`ISupportElementManager` : 
		"""
		pass

	@overload
	def SupportElementManager(self, supportElementTypeName: str) -> ISupportElementManager:
		"""No Description

		Args
		--------
			supportElementTypeName (`str`) :  supportElementTypeName

		Returns
		--------
			`ISupportElementManager` : 
		"""
		pass

	def PrototypeSupportElementManager(self, supportElementTypeID: int) -> IPrototypeManager:
		"""No Description

		Args
		--------
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`IPrototypeManager` : 
		"""
		pass

	def PrototypeDomainElementManager(self, domainElementTypeID: int) -> IPrototypeDomainElementManager:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IPrototypeDomainElementManager` : 
		"""
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Guid(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def DomainDataSetManager(self) -> IDomainDataSetManager:
		"""No Description

		Returns
		--------
			`IDomainDataSetManager` : 
		"""
		pass

	@property
	def FieldManager(self) -> IFieldManager:
		"""No Description

		Returns
		--------
			`IFieldManager` : 
		"""
		pass

	@property
	def ScenarioManager(self) -> IScenarioManager:
		"""No Description

		Returns
		--------
			`IScenarioManager` : 
		"""
		pass

	@property
	def SelectionSetManager(self) -> ISelectionSetManager:
		"""No Description

		Returns
		--------
			`ISelectionSetManager` : 
		"""
		pass

	@property
	def ProfileManager(self) -> ISelectionSetManager:
		"""No Description

		Returns
		--------
			`ISelectionSetManager` : 
		"""
		pass

	@property
	def EmbeddedStickyObjectManager(self) -> IEmbeddedStickyObjectManager:
		"""No Description

		Returns
		--------
			`IEmbeddedStickyObjectManager` : 
		"""
		pass

	@property
	def ChangeTrackingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ChangeTrackingEnabled.setter
	def ChangeTrackingEnabled(self, changetrackingenabled: bool) -> None:
		pass

	@property
	def SmartChangeTrackingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@SmartChangeTrackingEnabled.setter
	def SmartChangeTrackingEnabled(self, smartchangetrackingenabled: bool) -> None:
		pass

	@property
	def ChangeTrackingLocked(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ChangeTrackingLocked.setter
	def ChangeTrackingLocked(self, changetrackinglocked: bool) -> None:
		pass

	@property
	def ChangeTrackingPassword(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@ChangeTrackingPassword.setter
	def ChangeTrackingPassword(self, changetrackingpassword: str) -> None:
		pass

	@property
	def ChangeTrackingPromptOnOpen(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ChangeTrackingPromptOnOpen.setter
	def ChangeTrackingPromptOnOpen(self, changetrackingpromptonopen: bool) -> None:
		pass

class IDomainDataSetUnitPresentation(IDomainDataSet):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PresentationUnitManager(self) -> IPresentationUnitsManager:
		"""No Description

		Returns
		--------
			`IPresentationUnitsManager` : 
		"""
		pass

class IDomainDataSet2DModeling:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def HasRainfallInflowToNode(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@HasRainfallInflowToNode.setter
	def HasRainfallInflowToNode(self, hasrainfallinflowtonode: bool) -> None:
		pass

	@property
	def MeshSize(self) -> float:
		"""No Description

		Returns
		--------
			`float` : 
		"""
		pass

	@MeshSize.setter
	def MeshSize(self, meshsize: float) -> None:
		pass

class IDomainDataSetUpdatable:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def LocalizeExistingLabels(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def SetGuid(self, guid: Guid) -> None:
		"""No Description

		Args
		--------
			guid (`Guid`) :  guid

		Returns
		--------
			`None` : 
		"""
		pass

class IDomainDataSetSearch:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetElementIDsForLabel(self, label: str, type: ModelingElementType, elementTypeID: int, useWildcards: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			label (`str`) :  label
			type (`ModelingElementType`) :  type
			elementTypeID (`int`) :  elementTypeID
			useWildcards (`bool`) :  useWildcards

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def GetDomainElementIDsForLabel(self, label: str, useWildcards: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			label (`str`) :  label
			useWildcards (`bool`) :  useWildcards

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def GetLabel(self, elementID: int) -> str:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`str` : 
		"""
		pass

	def GetLabelForDomainElementID(self, domainElementID: int) -> str:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`str` : 
		"""
		pass

	@overload
	def GetIncomingLinkIDsToNode(self, domainElementID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@overload
	def GetIncomingLinkIDsToNode(self, domainElementID: int, alternativeID: int, domainElementTypeIDs: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@overload
	def GetOutcomingLinkIDsFromNode(self, domainElementID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@overload
	def GetOutcomingLinkIDsFromNode(self, domainElementID: int, alternativeID: int, domainElementTypeIDs: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def GetElementIDsWithDuplicateLabels(self, modelingElementType: ModelingElementType, elementTypeIDs: array[int], ignoreBlanks: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			modelingElementType (`ModelingElementType`) :  modelingElementType
			elementTypeIDs (`array[int]`) :  elementTypeIDs
			ignoreBlanks (`bool`) :  ignoreBlanks

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

class IDomainDataSetLog:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ChangeLogDatabase(self) -> IChangeLogDatabase:
		"""No Description

		Returns
		--------
			`IChangeLogDatabase` : 
		"""
		pass

	@property
	def ChangeLog(self) -> IChangeLog:
		"""No Description

		Returns
		--------
			`IChangeLog` : 
		"""
		pass

class IDocumentSpecificationRegistryDataSet:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DocumentSpecificationRegistry(self) -> IDocumentSpecificationRegistry:
		"""No Description

		Returns
		--------
			`IDocumentSpecificationRegistry` : 
		"""
		pass

class IChangeLogDatabase:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DeleteFromChangeLog(self, process: IProcessInProgressEx, elementIDs: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			process (`IProcessInProgressEx`) :  process
			elementIDs (`HmIDCollection`) :  elementIDs

		Returns
		--------
			`None` : 
		"""
		pass

	def DeleteAllChangeTracking(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	def DeleteChangeTrackingByRange(self, startID: int, endID: int) -> int:
		"""No Description

		Args
		--------
			startID (`int`) :  startID
			endID (`int`) :  endID

		Returns
		--------
			`int` : 
		"""
		pass

	def GetChangeLogWriter(self) -> IChangeLogWriter:
		"""No Description

		Returns
		--------
			`IChangeLogWriter` : 
		"""
		pass

	def GetTotalCountWithLimit(self, limit: int) -> int:
		"""No Description

		Args
		--------
			limit (`int`) :  limit

		Returns
		--------
			`int` : 
		"""
		pass

	def GetTotalCount(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	def GetIds(self, numberIds: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			numberIds (`int`) :  numberIds

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def IsInitialized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@overload
	def ReadChangeLog(self, dataSet: DataSet, domainDataSet: IDomainDataSet, process: IProcessInProgress, dataRowLoader: IChangeLogDataRowLoader) -> DataSet:
		"""No Description

		Args
		--------
			dataSet (`DataSet`) :  dataSet
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			process (`IProcessInProgress`) :  process
			dataRowLoader (`IChangeLogDataRowLoader`) :  dataRowLoader

		Returns
		--------
			`DataSet` : 
		"""
		pass

	@overload
	def ReadChangeLog(self, domainDataSet: IDomainDataSet, process: IProcessInProgress, dataRowLoader: IChangeLogDataRowLoader) -> DataSet:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			process (`IProcessInProgress`) :  process
			dataRowLoader (`IChangeLogDataRowLoader`) :  dataRowLoader

		Returns
		--------
			`DataSet` : 
		"""
		pass

	def ReadChangeLogByIds(self, domainDataSet: IDomainDataSet, process: IProcessInProgress, dataRowLoader: IChangeLogDataRowLoader, elementIDs: HmIDCollection) -> DataSet:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			process (`IProcessInProgress`) :  process
			dataRowLoader (`IChangeLogDataRowLoader`) :  dataRowLoader
			elementIDs (`HmIDCollection`) :  elementIDs

		Returns
		--------
			`DataSet` : 
		"""
		pass

	@property
	def LogConnection(self) -> SQLiteConnection:
		"""No Description

		Returns
		--------
			`SQLiteConnection` : 
		"""
		pass

class IChangeLogDataRowLoader:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def LoadDataRow(self, values: List[object]) -> None:
		"""No Description

		Args
		--------
			values (`List[object]`) :  values

		Returns
		--------
			`None` : 
		"""
		pass

class IChangeLogFieldEntryVerifier:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ShouldLogEntryFor(self, fieldName: str) -> bool:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`bool` : 
		"""
		pass

class IChangeLogWriter:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CommitSQLTransaction(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeAdd(self, alternativeID: int, parentAlternativeID: int, alternativeTypeID: int, isChildAlternative: bool) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			parentAlternativeID (`int`) :  parentAlternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			isChildAlternative (`bool`) :  isChildAlternative

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeDelete(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeDuplicated(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			parentID (`int`) :  parentID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeMerge(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			parentID (`int`) :  parentID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeModified(self, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			fieldTypeLabel (`str`) :  fieldTypeLabel
			newValue (`object`) :  newValue

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeParentIDChanged(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			parentID (`int`) :  parentID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeRestore(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteChangeLogArchived(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteCollectionFieldGlobalEdit(self, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldType: str, elementIDs: List[int], value: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType
			fieldType (`str`) :  fieldType
			elementIDs (`List[int]`) :  elementIDs
			value (`object`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteCollectionValueAdd(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteCollectionValueDelete(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementAdd(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementDelete(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementEdit(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			fieldTypeLabel (`str`) :  fieldTypeLabel
			newValue (`object`) :  newValue

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementEditCollection(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldTypeLabel: str) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType
			fieldTypeLabel (`str`) :  fieldTypeLabel

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementEditNoAlternative(self, domainElementID: int, domainElementTypeID: Nullable[int], fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			domainElementTypeID (`Nullable`) :  domainElementTypeID
			fieldTypeLabel (`str`) :  fieldTypeLabel
			newValue (`object`) :  newValue

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementGlobalEdit(self, alternativeID: int, alternativeTypeID: int, fieldType: str, elementIDNewValueDictionary: Dict[int,int][int,object]) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			fieldType (`str`) :  fieldType
			elementIDNewValueDictionary (`Dict[int,int]`) :  elementIDNewValueDictionary

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementIDs: HmIDCollection, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementIDs (`HmIDCollection`) :  elementIDs
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementTypeLogContext(self, elementID: int, elementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			elementTypeID (`int`) :  elementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteTrackingTurnedOff(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteTrackingTurnedOn(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteTrackingViewed(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def CurrentContext(self) -> Union[Guid, None]:
		"""No Description

		Returns
		--------
			`Nullable` : 
		"""
		pass

	@CurrentContext.setter
	def CurrentContext(self, currentcontext: Nullable[Guid]) -> None:
		pass

	@property
	def Enabled(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@Enabled.setter
	def Enabled(self, enabled: bool) -> None:
		pass

	@property
	def SmartChangeTrackingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@SmartChangeTrackingEnabled.setter
	def SmartChangeTrackingEnabled(self, smartchangetrackingenabled: bool) -> None:
		pass

class IChangeLog:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Archive(self, process: IProcessInProgressEx, changeLogDataTable: DataTable, orderedIDs: array[int], filteredIDs: HmIDCollection, filename: str, whereClause: str, append: bool = False) -> None:
		"""No Description

		Args
		--------
			process (`IProcessInProgressEx`) :  process
			changeLogDataTable (`DataTable`) :  changeLogDataTable
			orderedIDs (`array[int]`) :  orderedIDs
			filteredIDs (`HmIDCollection`) :  filteredIDs
			filename (`str`) :  filename
			whereClause (`str`) :  whereClause
			append (`bool`) :  append

		Returns
		--------
			`None` : 
		"""
		pass

	def BeginArchive(self, filename: str) -> SQLiteConnection:
		"""No Description

		Args
		--------
			filename (`str`) :  filename

		Returns
		--------
			`SQLiteConnection` : 
		"""
		pass

	@overload
	def Archive(self, archiveConnection: SQLiteConnection, changeLogDataTable: DataTable, orderedIDs: array[int]) -> None:
		"""No Description

		Args
		--------
			archiveConnection (`SQLiteConnection`) :  archiveConnection
			changeLogDataTable (`DataTable`) :  changeLogDataTable
			orderedIDs (`array[int]`) :  orderedIDs

		Returns
		--------
			`None` : 
		"""
		pass

	def EndArchive(self, archiveConnection: SQLiteConnection) -> None:
		"""No Description

		Args
		--------
			archiveConnection (`SQLiteConnection`) :  archiveConnection

		Returns
		--------
			`None` : 
		"""
		pass

	def CommitSQLTransaction(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeAdd(self, alternativeID: int, parentAlternativeID: int, alternativeTypeID: int, isChildAlternative: bool) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			parentAlternativeID (`int`) :  parentAlternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			isChildAlternative (`bool`) :  isChildAlternative

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeDelete(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeDuplicated(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			parentID (`int`) :  parentID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeMerge(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			parentID (`int`) :  parentID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeModified(self, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			fieldTypeLabel (`str`) :  fieldTypeLabel
			newValue (`object`) :  newValue

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeParentChanged(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			parentID (`int`) :  parentID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteAlternativeRestore(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteChangeLogArchived(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteCollectionFieldGlobalEdit(self, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldType: str, elementIDs: List[int], value: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType
			fieldType (`str`) :  fieldType
			elementIDs (`List[int]`) :  elementIDs
			value (`object`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteCollectionValueAdd(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteCollectionValueDelete(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementAdd(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementDelete(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementEdit(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			fieldTypeLabel (`str`) :  fieldTypeLabel
			newValue (`object`) :  newValue

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementEditCollection(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldTypeLabel: str) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementCollectionFieldType (`IDomainElementFieldType`) :  domainElementCollectionFieldType
			fieldTypeLabel (`str`) :  fieldTypeLabel

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementEditNoAlternative(self, domainElementID: int, domainElementTypeID: Nullable[int], fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			domainElementTypeID (`Nullable`) :  domainElementTypeID
			fieldTypeLabel (`str`) :  fieldTypeLabel
			newValue (`object`) :  newValue

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementGlobalEdit(self, alternativeID: int, alternativeTypeID: int, fieldType: str, elementIDNewValueDictionary: Dict[int,int][int,object]) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			alternativeTypeID (`int`) :  alternativeTypeID
			fieldType (`str`) :  fieldType
			elementIDNewValueDictionary (`Dict[int,int]`) :  elementIDNewValueDictionary

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementIDs: HmIDCollection, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementIDs (`HmIDCollection`) :  elementIDs
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteDomainElementTypeLogContext(self, elementID: int, elementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			elementTypeID (`int`) :  elementTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteTrackingTurnedOff(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteTrackingTurnedOn(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def WriteTrackingViewed(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Database(self) -> IChangeLogDatabase:
		"""No Description

		Returns
		--------
			`IChangeLogDatabase` : 
		"""
		pass

	@property
	def Enabled(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@Enabled.setter
	def Enabled(self, enabled: bool) -> None:
		pass

	@property
	def SmartChangeTrackingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@SmartChangeTrackingEnabled.setter
	def SmartChangeTrackingEnabled(self, smartchangetrackingenabled: bool) -> None:
		pass

class IDomainDataSetGISIDLinks:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DeleteAllGISIDs(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`None` : 
		"""
		pass

	def GetGISIDsForElementID(self, elementID: int) -> StringCollection:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`StringCollection` : 
		"""
		pass

	def GetElementIDsForGISID(self, gisID: str) -> HmIDCollection:
		"""No Description

		Args
		--------
			gisID (`str`) :  gisID

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def GetDeletedElementIDsForGISID(self, gisID: str) -> HmIDCollection:
		"""No Description

		Args
		--------
			gisID (`str`) :  gisID

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def GetDeletedGISIDToElementIDsMap(self) -> Dict:
		"""No Description

		Returns
		--------
			`Dict` : 
		"""
		pass

	def GetUniqueGISIDsSet(self) -> Dict:
		"""No Description

		Returns
		--------
			`Dict` : 
		"""
		pass

	def AddGISIDToElementID(self, elementID: int, gisID: str) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			gisID (`str`) :  gisID

		Returns
		--------
			`None` : 
		"""
		pass

	def AddGISIDsToElementID(self, elementID: int, gisIDs: StringCollection) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			gisIDs (`StringCollection`) :  gisIDs

		Returns
		--------
			`None` : 
		"""
		pass

	def IsElementAvailable(self, elementID: int) -> bool:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetAllElementIdsWithGISIDs(self) -> Iterator[GenericPair]:
		"""No Description

		Returns
		--------
			`Iterator[GenericPair]` : 
		"""
		pass

	def SetGISIDs(self, elementID: int, value: str) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			value (`str`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

class IDomainDataSetExternalIDLinks:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetElementIDForExternalID(self, idType: ExternalIDType, externalID: str) -> Union[int, None]:
		"""No Description

		Args
		--------
			idType (`ExternalIDType`) :  idType
			externalID (`str`) :  externalID

		Returns
		--------
			`Nullable` : 
		"""
		pass

	def GetExternalIDs(self, elementID: int, idType: ExternalIDType) -> List[str]:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			idType (`ExternalIDType`) :  idType

		Returns
		--------
			`List[str]` : 
		"""
		pass

	def AddExternalIDs(self, elementID: int, idType: ExternalIDType, externalIDs: List[str]) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			idType (`ExternalIDType`) :  idType
			externalIDs (`List[str]`) :  externalIDs

		Returns
		--------
			`None` : 
		"""
		pass

	def ClearExternalIDs(self, elementID: int, idType: ExternalIDType) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			idType (`ExternalIDType`) :  idType

		Returns
		--------
			`None` : 
		"""
		pass

	def ClearAllExternalIDs(self, idType: ExternalIDType) -> None:
		"""No Description

		Args
		--------
			idType (`ExternalIDType`) :  idType

		Returns
		--------
			`None` : 
		"""
		pass

class IDomainDataSetBulkOperations:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EnterBulkOperationState(self, type: BulkOperationType) -> None:
		"""No Description

		Args
		--------
			type (`BulkOperationType`) :  type

		Returns
		--------
			`None` : 
		"""
		pass

	def ExitBulkOperationState(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def CurrentBulkOperationState(self) -> BulkOperationType:
		"""No Description

		Returns
		--------
			`BulkOperationType` : 
		"""
		pass

class IModelingElement(IEditLabeled):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportedFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def ModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			`ModelingElementType` : 
		"""
		pass

	@property
	def Manager(self) -> IModelingElementManager:
		"""No Description

		Returns
		--------
			`IModelingElementManager` : 
		"""
		pass

class IModelingElementManager(IListManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Copy(self, id: int) -> int:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`int` : 
		"""
		pass

	def Element(self, id: int) -> IModelingElement:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`IModelingElement` : 
		"""
		pass

	def Exists(self, id: int) -> bool:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`bool` : 
		"""
		pass

	def Restore(self, id: int) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`None` : 
		"""
		pass

	def Elements(self) -> ModelingElementCollection:
		"""No Description

		Returns
		--------
			`ModelingElementCollection` : 
		"""
		pass

	def ElementIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def ModelingElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

class IModelingElementManagerBatch:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Restore(self, ids: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids

		Returns
		--------
			`None` : 
		"""
		pass

class ITreeElement(IModelingElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Children(self) -> ModelingElementCollection:
		"""No Description

		Returns
		--------
			`ModelingElementCollection` : 
		"""
		pass

	@property
	def ParentID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ParentID.setter
	def ParentID(self, parentid: int) -> None:
		pass

class ITreeElement2:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetLevelInHierarchy(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	def IsDescendantOf(self, treeElement: ITreeElement, numberOfLevels: int) -> bool:
		"""No Description

		Args
		--------
			treeElement (`ITreeElement`) :  treeElement
			numberOfLevels (`int`) :  numberOfLevels

		Returns
		--------
			`bool` : 
		"""
		pass

class ITreeElementManager(IModelingElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def BaseElements(self) -> ModelingElementCollection:
		"""No Description

		Returns
		--------
			`ModelingElementCollection` : 
		"""
		pass

	def ChildrenOfElement(self, parentID: int) -> ModelingElementCollection:
		"""No Description

		Args
		--------
			parentID (`int`) :  parentID

		Returns
		--------
			`ModelingElementCollection` : 
		"""
		pass

class IDomainElement(IModelingElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@property
	def DomainElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IDomainElementManager(IModelingElementManager, ISelectableManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	def DelayedElementIDs(self) -> IHmIDDelayedCollection:
		"""No Description

		Returns
		--------
			`IHmIDDelayedCollection` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str, resultRecordTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str, numericalEngineTypeName: str, resultRecordTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			numericalEngineTypeName (`str`) :  numericalEngineTypeName
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def SupportedResultFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@overload
	def SupportedResultFields(self, numericalEngineTypeName: str) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def CrossElementFieldListManager(self, collectionFieldName: str, alternativeTypeName: str, alternativeID: int, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> ICrossElementFieldListManager:
		"""No Description

		Args
		--------
			collectionFieldName (`str`) :  collectionFieldName
			alternativeTypeName (`str`) :  alternativeTypeName
			alternativeID (`int`) :  alternativeID
			sortContexts (`SortContextCollection`) :  sortContexts
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`ICrossElementFieldListManager` : 
		"""
		pass

class IAlternative(ITreeElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	def AlternativeRecord(self, domainElementTypeID: int) -> IAlternativeRecord:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IAlternativeRecord` : 
		"""
		pass

	def AlternativeField(self, name: str, domainElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IField` : 
		"""
		pass

	def SystemRecordField(self, name: str) -> ISystemRecordField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`ISystemRecordField` : 
		"""
		pass

	def AlternativeFields(self, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def ReferencedScenarios(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@property
	def AlternativeTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IAlternativeManager(ITreeElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	def SystemAlternativeRecord(self) -> ISystemAlternativeRecord:
		"""No Description

		Returns
		--------
			`ISystemAlternativeRecord` : 
		"""
		pass

	@overload
	def Add(self, alternativeParentId: int) -> int:
		"""No Description

		Args
		--------
			alternativeParentId (`int`) :  alternativeParentId

		Returns
		--------
			`int` : 
		"""
		pass

	def SystemRecordField(self, name: str) -> ISystemRecordField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`ISystemRecordField` : 
		"""
		pass

	def AlternativeField(self, name: str, domainElementTypeID: int, initialAlternativeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			domainElementTypeID (`int`) :  domainElementTypeID
			initialAlternativeID (`int`) :  initialAlternativeID

		Returns
		--------
			`IField` : 
		"""
		pass

	def Merge(self, sourceAlternativeID: int) -> None:
		"""No Description

		Args
		--------
			sourceAlternativeID (`int`) :  sourceAlternativeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def Add(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IAlternativeRecord:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsLocal(self, elementID: int) -> bool:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`bool` : 
		"""
		pass

	def MakeLocal(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`None` : 
		"""
		pass

	def MakeInherited(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def GetValue(self, elementID: int, fieldTypeID: int, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			fieldTypeID (`int`) :  fieldTypeID
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`object` : 
		"""
		pass

	@overload
	def GetValue(self, elementID: int, fieldName: str, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			fieldName (`str`) :  fieldName
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`object` : 
		"""
		pass

	@overload
	def SetValue(self, elementID: int, fieldTypeID: int, unit: UnitIndex, newVal: object) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			fieldTypeID (`int`) :  fieldTypeID
			unit (`UnitIndex`) :  unit
			newVal (`object`) :  newVal

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def SetValue(self, elementID: int, fieldName: str, unit: UnitIndex, newVal: object) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			fieldName (`str`) :  fieldName
			unit (`UnitIndex`) :  unit
			newVal (`object`) :  newVal

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def GetValues(self, fieldTypeID: int, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			fieldTypeID (`int`) :  fieldTypeID
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetValues(self, fieldName: str, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetDataReader(self) -> IAlternativeRecordDataReader:
		"""No Description

		Returns
		--------
			`IAlternativeRecordDataReader` : 
		"""
		pass

	@overload
	def GetDataReader(self, fieldTypeNames: array[str]) -> IAlternativeRecordDataReader:
		"""No Description

		Args
		--------
			fieldTypeNames (`array[str]`) :  fieldTypeNames

		Returns
		--------
			`IAlternativeRecordDataReader` : 
		"""
		pass

	@property
	def Alternative(self) -> IAlternative:
		"""No Description

		Returns
		--------
			`IAlternative` : 
		"""
		pass

class IFieldCollectionDataReader:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetValues(self, fieldTypeName: str) -> Dict:
		"""No Description

		Args
		--------
			fieldTypeName (`str`) :  fieldTypeName

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetValues(self, fieldTypeName: str, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			fieldTypeName (`str`) :  fieldTypeName
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`Dict` : 
		"""
		pass

	def Dispose(self, fieldTypeName: str) -> None:
		"""No Description

		Args
		--------
			fieldTypeName (`str`) :  fieldTypeName

		Returns
		--------
			`None` : 
		"""
		pass

	def Refresh(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Close(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

class IAlternativeRecordDataReader(IFieldCollectionDataReader):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeRecord(self) -> IAlternativeRecord:
		"""No Description

		Returns
		--------
			`IAlternativeRecord` : 
		"""
		pass

class ISystemAlternativeRecord:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsLocal(self, alternativeID: int) -> bool:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`bool` : 
		"""
		pass

	def MakeLocal(self, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`None` : 
		"""
		pass

	def MakeInherited(self, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`None` : 
		"""
		pass

	def GetValue(self, alternativeID: int, fieldTypeID: int, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			fieldTypeID (`int`) :  fieldTypeID
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`object` : 
		"""
		pass

	def SetValue(self, alternativeID: int, fieldTypeID: int, unit: UnitIndex, newVal: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			fieldTypeID (`int`) :  fieldTypeID
			unit (`UnitIndex`) :  unit
			newVal (`object`) :  newVal

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def AlternativeTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IGeometryPointAlternativeRecord(IAlternativeRecord):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoint(self, domainElementID: int) -> GeometryPoint:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`GeometryPoint` : 
		"""
		pass

	def SetPoint(self, domainElementID: int, point: GeometryPoint) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			point (`GeometryPoint`) :  point

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryPolylineAlternativeRecord(IAlternativeRecord):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self, domainElementID: int) -> List[GeometryPoint]:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`List[GeometryPoint]` : 
		"""
		pass

	def SetPoints(self, domainElementID: int, points: List[GeometryPoint]) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			points (`List[GeometryPoint]`) :  points

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryPolyline3DAlternativeRecord(IAlternativeRecord):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self, domainElementID: int) -> List[GeometryPoint3D]:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`List[GeometryPoint3D]` : 
		"""
		pass

	def SetPoints(self, domainElementID: int, points3D: List[GeometryPoint3D]) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			points3D (`List[GeometryPoint3D]`) :  points3D

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryPolygonAlternativeRecord(IAlternativeRecord):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetRings(self, domainElementID: int) -> List[List[GeometryPoint]]:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`List[List[GeometryPoint]]` : 
		"""
		pass

	def SetRings(self, domainElementID: int, rings: List[List[GeometryPoint]]) -> None:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID
			rings (`List[List[GeometryPoint]]`) :  rings

		Returns
		--------
			`None` : 
		"""
		pass

class IScenario(ITreeElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def AlternativeID(self, alternativeTypeID: int) -> int:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AlternativeID(self, alternativeTypeName: str) -> int:
		"""No Description

		Args
		--------
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AlternativeID(self, alternativeTypeID: int, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def AlternativeID(self, alternativeTypeName: str, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeName (`str`) :  alternativeTypeName
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`None` : 
		"""
		pass

	def IsAlternativeLocal(self, alternativeTypeID: int) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`bool` : 
		"""
		pass

	def MakeAlternativeLocal(self, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def MakeAlternativeInherited(self, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`None` : 
		"""
		pass

	def IsCalculationOptionsLocal(self, numericalEngineTypeName: str) -> bool:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`bool` : 
		"""
		pass

	def MakeCalculationOptionsLocal(self, numericalEngineTypeName: str) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`None` : 
		"""
		pass

	def MakeCalculationOptionsInherited(self, numericalEngineTypeName: str) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CalculationOptionsID(self, numericalEngineTypeName: str) -> int:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def CalculationOptionsID(self, numericalEngineTypeName: str, calculationOptionsID: int) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName
			calculationOptionsID (`int`) :  calculationOptionsID

		Returns
		--------
			`None` : 
		"""
		pass

	def ResultManager(self, numericalEngineTypeName: str) -> IResultManager:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`IResultManager` : 
		"""
		pass

	def GetActiveNumericalEngineTypeName(self, resultRecordTypeName: str) -> str:
		"""No Description

		Args
		--------
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`str` : 
		"""
		pass

	def SetActiveNumericalEngineTypeName(self, numericalEngineTypeName: str) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def ActiveTimeStep(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActiveTimeStep.setter
	def ActiveTimeStep(self, activetimestep: int) -> None:
		pass

	@property
	def ActiveTimeIncrement(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActiveTimeIncrement.setter
	def ActiveTimeIncrement(self, activetimeincrement: int) -> None:
		pass

class IScenarioManager(ITreeElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CalculationOptionsManager(self, numericalEngineTypeName: str) -> ICalculationOptionsManager:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`ICalculationOptionsManager` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str, numericalEngineTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def SupportedResultFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@overload
	def SupportedResultFields(self, numericalEngineTypeName: str) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@property
	def ActiveScenarioID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActiveScenarioID.setter
	def ActiveScenarioID(self, activescenarioid: int) -> None:
		pass

class ICalculationOptionsManager(IModelingElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CalculationOptionsField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

class ICalculationOptions(IModelingElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CalculationOptionsField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

class ISelectionSetManager(IModelingElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SelectionSetField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

class ISelectionSet(IModelingElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SelectionSetField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

class IEmbeddedStickyObjectManager(IModelingElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EmbeddedStickyObjectField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def ElementIDs(self, domainElementID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (`int`) :  domainElementID

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def ElementIDsForDomainElementType(self, domainElementTypeID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	@overload
	def ElementIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

class IEmbeddedStickyObject(IModelingElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EmbeddedStickyObjectField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

class IResultManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Open(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Close(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Deactivate(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def TimeSteps(self, unit: TimeUnit) -> array[float]:
		"""No Description

		Args
		--------
			unit (`TimeUnit`) :  unit

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def ResultRecord(self, resultRecordTypeID: int) -> IResultRecord:
		"""No Description

		Args
		--------
			resultRecordTypeID (`int`) :  resultRecordTypeID

		Returns
		--------
			`IResultRecord` : 
		"""
		pass

	@overload
	def ResultRecord(self, resultRecordTypeName: str) -> IResultRecord:
		"""No Description

		Args
		--------
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`IResultRecord` : 
		"""
		pass

	def ResultRecords(self, domainElementTypeID: int) -> ResultRecordCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`ResultRecordCollection` : 
		"""
		pass

	@property
	def IsActive(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def HasResults(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Scenario(self) -> IScenario:
		"""No Description

		Returns
		--------
			`IScenario` : 
		"""
		pass

class IResultRecord:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, elementID: int, resultFieldTypeName: str, timeStep: int, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			resultFieldTypeName (`str`) :  resultFieldTypeName
			timeStep (`int`) :  timeStep
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`object` : 
		"""
		pass

	def GetValues(self, domainElementTypeIDs: HmIDCollection, resultFieldTypeName: str, timeStep: int, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			resultFieldTypeName (`str`) :  resultFieldTypeName
			timeStep (`int`) :  timeStep
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`Dict` : 
		"""
		pass

	def GetValuesOverTime(self, elementID: int, resultFieldTypeName: str, unit: UnitIndex) -> array:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			resultFieldTypeName (`str`) :  resultFieldTypeName
			unit (`UnitIndex`) :  unit

		Returns
		--------
			`array` : 
		"""
		pass

class IResultField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsActive(self, scenarioId: int) -> bool:
		"""No Description

		Args
		--------
			scenarioId (`int`) :  scenarioId

		Returns
		--------
			`bool` : 
		"""
		pass

	def HasResults(self, scenarioId: int) -> bool:
		"""No Description

		Args
		--------
			scenarioId (`int`) :  scenarioId

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetValuesForElementIDs(self, ids: HmIDCollection, scenarioID: int) -> Dict:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`Dict` : 
		"""
		pass

	@property
	def NumericalEngineType(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@property
	def ResultRecordType(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

class IResultNonTimeVariantField(IResultField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetValue(self, elementID: int, scenarioID: int) -> object:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`object` : 
		"""
		pass

	@overload
	def GetValues(self, domainElementTypeIDs: HmIDCollection, scenarioID: int) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int) -> array:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`array` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int, domainElementTypeIDs: HmIDCollection) -> array:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs

		Returns
		--------
			`array` : 
		"""
		pass

	@overload
	def GetValue(self, id: int) -> object:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`object` : 
		"""
		pass

	@overload
	def GetValues(self) -> Dict:
		"""No Description

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetValues(self, ids: HmIDCollection) -> Dict:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids

		Returns
		--------
			`Dict` : 
		"""
		pass

class IResultTimeVariantField(IResultField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetValue(self, elementID: int, scenarioID: int, timeStep: int) -> object:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			scenarioID (`int`) :  scenarioID
			timeStep (`int`) :  timeStep

		Returns
		--------
			`object` : 
		"""
		pass

	def GetValuesOverTime(self, elementID: int, scenarioID: int) -> array:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`array` : 
		"""
		pass

	@overload
	def GetValues(self, domainElementTypeIDs: HmIDCollection, scenarioID: int, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			scenarioID (`int`) :  scenarioID
			timeStep (`int`) :  timeStep

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int, timeStep: int) -> array:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			timeStep (`int`) :  timeStep

		Returns
		--------
			`array` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int, timeStep: int, domainElementTypeIDs: HmIDCollection) -> array:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			timeStep (`int`) :  timeStep
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs

		Returns
		--------
			`array` : 
		"""
		pass

	@overload
	def GetValuesForElementIDs(self, ids: HmIDCollection, scenarioID: int, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids
			scenarioID (`int`) :  scenarioID
			timeStep (`int`) :  timeStep

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetValuesForElementIDs(self, ids: HmIDCollection, scenarioID: int) -> Dict:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetValue(self, id: int) -> object:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`object` : 
		"""
		pass

	@overload
	def GetValues(self) -> Dict:
		"""No Description

		Returns
		--------
			`Dict` : 
		"""
		pass

	@overload
	def GetValues(self, ids: HmIDCollection) -> Dict:
		"""No Description

		Args
		--------
			ids (`HmIDCollection`) :  ids

		Returns
		--------
			`Dict` : 
		"""
		pass

class IFieldStatistics:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (`List[StatisticType]`) :  statTypes

		Returns
		--------
			`array[float]` : 
		"""
		pass

class ISelectableFieldStatistics(IFieldStatistics):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (`List[StatisticType]`) :  statTypes
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (`List[StatisticType]`) :  statTypes

		Returns
		--------
			`array[float]` : 
		"""
		pass

class IResultFieldStatistics(ISelectableFieldStatistics):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetStatistics(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			statTypes (`List[StatisticType]`) :  statTypes
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	def GetStatisticsEstimate(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			statTypes (`List[StatisticType]`) :  statTypes
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (`List[StatisticType]`) :  statTypes
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (`List[StatisticType]`) :  statTypes

		Returns
		--------
			`array[float]` : 
		"""
		pass

class IResultTimeVariantFieldStatistics(IResultFieldStatistics):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetStatistics(self, elementID: int, scenarioID: int, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			scenarioID (`int`) :  scenarioID
			statTypes (`List[StatisticType]`) :  statTypes

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetStatistics(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], timeStepIndex: int, filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			statTypes (`List[StatisticType]`) :  statTypes
			timeStepIndex (`int`) :  timeStepIndex
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetStatistics(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			statTypes (`List[StatisticType]`) :  statTypes
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (`List[StatisticType]`) :  statTypes
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (`List[StatisticType]`) :  statTypes

		Returns
		--------
			`array[float]` : 
		"""
		pass

class INumericalEngine:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Run(self, scenarios: ModelingElementCollection) -> None:
		"""No Description

		Args
		--------
			scenarios (`ModelingElementCollection`) :  scenarios

		Returns
		--------
			`None` : 
		"""
		pass

	def IsRunning(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`bool` : 
		"""
		pass

	def add_ScenarioCalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_ScenarioCalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_ScenarioCalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_ScenarioCalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_CalculationStepStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_CalculationStepStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_CalculationStepProgress(self, value: CalculationStepProgressEventHandler) -> None:
		"""No Description

		Args
		--------
			value (`CalculationStepProgressEventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_CalculationStepProgress(self, value: CalculationStepProgressEventHandler) -> None:
		"""No Description

		Args
		--------
			value (`CalculationStepProgressEventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_CalculationStepFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_CalculationStepFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_CalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_CalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def add_CalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	def remove_CalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (`EventHandler`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def NumericalEnginePath(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@NumericalEnginePath.setter
	def NumericalEnginePath(self, numericalenginepath: str) -> None:
		pass

	@property
	def ResultDataConnection(self) -> IResultDataConnection:
		"""No Description

		Returns
		--------
			`IResultDataConnection` : 
		"""
		pass

class ICompositeNumericalEngine:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetActiveNumericalEngine(self, scenarioID: int) -> INumericalEngine:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`INumericalEngine` : 
		"""
		pass

	def SupportsValidation(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`bool` : 
		"""
		pass

class ICompositeResultDataConnection:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetActiveResultDataConnection(self, scenarioID: int) -> IResultDataConnection:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`IResultDataConnection` : 
		"""
		pass

class IResultDataConnectionFactory:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def NewResultDataConnection(self, domainDataSet: IDomainDataSet, numericalEngine: INumericalEngine) -> IResultDataConnection:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			numericalEngine (`INumericalEngine`) :  numericalEngine

		Returns
		--------
			`IResultDataConnection` : 
		"""
		pass

class IValidatingNumericalEngine(INumericalEngine):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Validate(self, scenarios: ModelingElementCollection) -> None:
		"""No Description

		Args
		--------
			scenarios (`ModelingElementCollection`) :  scenarios

		Returns
		--------
			`None` : 
		"""
		pass

class ILicensedNumericalEngine(INumericalEngine):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetLicensingInfo(self, license: License) -> None:
		"""No Description

		Args
		--------
			license (`License`) :  license

		Returns
		--------
			`None` : 
		"""
		pass

class IEntitledNumericalEngine(ILicensedNumericalEngine):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetEntitledLicensingInfo(self, license: License, messageHandler: IMessageHandler) -> None:
		"""No Description

		Args
		--------
			license (`License`) :  license
			messageHandler (`IMessageHandler`) :  messageHandler

		Returns
		--------
			`None` : 
		"""
		pass

class INumericalEngineWithResultDataConnectionFactory:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@ResultDataConnectionFactory.setter
	def ResultDataConnectionFactory(self, resultdataconnectionfactory: IResultDataConnectionFactory) -> None:
		pass

class ILicensedNumericalEngineEx(ILicensedNumericalEngine):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def SetLicensingInfo(self, licenseProvider: ILicenseProvider) -> None:
		"""No Description

		Args
		--------
			licenseProvider (`ILicenseProvider`) :  licenseProvider

		Returns
		--------
			`None` : 
		"""
		pass

	def SetLicenseKey(self, licenseKey: str) -> None:
		"""No Description

		Args
		--------
			licenseKey (`str`) :  licenseKey

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def SetLicensingInfo(self, license: License) -> None:
		"""No Description

		Args
		--------
			license (`License`) :  license

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def IgnoreLicensing(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class IResultDataConnection:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Open(self, scenarioID: int) -> None:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`None` : 
		"""
		pass

	def Close(self, scenarioID: int) -> None:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`None` : 
		"""
		pass

	def Deactivate(self, scenarioID: int) -> None:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`None` : 
		"""
		pass

	def IsActive(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`bool` : 
		"""
		pass

	def HasResults(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`bool` : 
		"""
		pass

	def TimeStepsInSeconds(self, scenarioID: int) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`array[float]` : 
		"""
		pass

	def ResultRecordDataBroker(self, resultRecordTypeName: str) -> IResultRecordDataBroker:
		"""No Description

		Args
		--------
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`IResultRecordDataBroker` : 
		"""
		pass

	def GetScenarioStartDateTime(self, scenarioID: int) -> datetime:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`datetime` : 
		"""
		pass

	def GetRunUserNotificationsSummary(self, scenarioID: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`List[IUserNotification]` : 
		"""
		pass

	def GetTimeStepUserNotificationsSummary(self, scenarioID: int, timeStepIndex: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			timeStepIndex (`int`) :  timeStepIndex

		Returns
		--------
			`List[IUserNotification]` : 
		"""
		pass

	def GetUserNotifications(self, scenarioID: int, elementID: int, timeStepIndex: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			elementID (`int`) :  elementID
			timeStepIndex (`int`) :  timeStepIndex

		Returns
		--------
			`List[IUserNotification]` : 
		"""
		pass

	def ResultConnectionIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			`HmIDCollection` : 
		"""
		pass

	def ResultPathAndFileNamesFor(self, databasePathAndFileName: str) -> array[str]:
		"""No Description

		Args
		--------
			databasePathAndFileName (`str`) :  databasePathAndFileName

		Returns
		--------
			`array[str]` : 
		"""
		pass

	def NewResultPathAndFileNameFor(self, currentResultFileAndPathName: str, databasePathAndFileName: str) -> str:
		"""No Description

		Args
		--------
			currentResultFileAndPathName (`str`) :  currentResultFileAndPathName
			databasePathAndFileName (`str`) :  databasePathAndFileName

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

	@property
	def NumericalEngine(self) -> INumericalEngine:
		"""No Description

		Returns
		--------
			`INumericalEngine` : 
		"""
		pass

class IResultDataConnectionEX:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def HasHydraulicResults(self, elementId: int, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			elementId (`int`) :  elementId
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`bool` : 
		"""
		pass

class ITranslatingTimeStepsResultDataConnection(IResultDataConnection):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetTranslatedTimeStepIndex(self, scenarioID: int, elementID: int, uberTimeStepIndex: int, isGravityResultField: bool) -> int:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			elementID (`int`) :  elementID
			uberTimeStepIndex (`int`) :  uberTimeStepIndex
			isGravityResultField (`bool`) :  isGravityResultField

		Returns
		--------
			`int` : 
		"""
		pass

	def GetTimeStepsForSubnetworkID(self, scenarioID: int, subnetworkIndex: int) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			subnetworkIndex (`int`) :  subnetworkIndex

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@overload
	def GetTimeStepUserNotificationsSummary(self, scenarioID: int, timeStepIndex: int, pressureSubnetworkID: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			timeStepIndex (`int`) :  timeStepIndex
			pressureSubnetworkID (`int`) :  pressureSubnetworkID

		Returns
		--------
			`List[IUserNotification]` : 
		"""
		pass

	def PrepareResultDataConnectionForTimeStepsRequest(self, factor: int) -> None:
		"""No Description

		Args
		--------
			factor (`int`) :  factor

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def GetTimeStepUserNotificationsSummary(self, scenarioID: int, timeStepIndex: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			timeStepIndex (`int`) :  timeStepIndex

		Returns
		--------
			`List[IUserNotification]` : 
		"""
		pass

	@property
	def UseHydrologicTimeSteps(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@UseHydrologicTimeSteps.setter
	def UseHydrologicTimeSteps(self, usehydrologictimesteps: bool) -> None:
		pass

	@property
	def UseReportingHydraulicTimeSteps(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@UseReportingHydraulicTimeSteps.setter
	def UseReportingHydraulicTimeSteps(self, usereportinghydraulictimesteps: bool) -> None:
		pass

	@property
	def ActiveSubnetworkID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActiveSubnetworkID.setter
	def ActiveSubnetworkID(self, activesubnetworkid: int) -> None:
		pass

class IResultRecordDataBroker:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, elementID: int, scenarioID: int, fieldTypeName: str, timeStep: int) -> object:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			scenarioID (`int`) :  scenarioID
			fieldTypeName (`str`) :  fieldTypeName
			timeStep (`int`) :  timeStep

		Returns
		--------
			`object` : 
		"""
		pass

	def GetValues(self, domainElementTypeIDs: HmIDCollection, scenarioID: int, fieldTypeName: str, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			scenarioID (`int`) :  scenarioID
			fieldTypeName (`str`) :  fieldTypeName
			timeStep (`int`) :  timeStep

		Returns
		--------
			`Dict` : 
		"""
		pass

	def GetValuesForElementIDs(self, elementIDs: HmIDCollection, scenarioID: int, fieldTypeName: str, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			elementIDs (`HmIDCollection`) :  elementIDs
			scenarioID (`int`) :  scenarioID
			fieldTypeName (`str`) :  fieldTypeName
			timeStep (`int`) :  timeStep

		Returns
		--------
			`Dict` : 
		"""
		pass

	def GetValuesOverTime(self, elementID: int, scenarioID: int, fieldTypeName: str) -> array:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			scenarioID (`int`) :  scenarioID
			fieldTypeName (`str`) :  fieldTypeName

		Returns
		--------
			`array` : 
		"""
		pass

	def GetStatisticValues(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, fieldTypeName: str, statTypes: List[StatisticType], timeStepIndex: int, filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			fieldTypeName (`str`) :  fieldTypeName
			statTypes (`List[StatisticType]`) :  statTypes
			timeStepIndex (`int`) :  timeStepIndex
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	def GetStatisticEstimateValues(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, fieldTypeName: str, statTypes: List[StatisticType], timeStepIndex: int, filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			domainElementTypeIDs (`HmIDCollection`) :  domainElementTypeIDs
			fieldTypeName (`str`) :  fieldTypeName
			statTypes (`List[StatisticType]`) :  statTypes
			timeStepIndex (`int`) :  timeStepIndex
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`array[float]` : 
		"""
		pass

	def GetStatisticValuesOverTime(self, elementID: int, scenarioID: int, fieldTypeName: str, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			scenarioID (`int`) :  scenarioID
			fieldTypeName (`str`) :  fieldTypeName
			statTypes (`List[StatisticType]`) :  statTypes

		Returns
		--------
			`array[float]` : 
		"""
		pass

	@property
	def ResultDataConnection(self) -> IResultDataConnection:
		"""No Description

		Returns
		--------
			`IResultDataConnection` : 
		"""
		pass

	@property
	def ResultRecordTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

class ISupportElement(IModelingElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportElementField(self, attributeName: str) -> IField:
		"""No Description

		Args
		--------
			attributeName (`str`) :  attributeName

		Returns
		--------
			`IField` : 
		"""
		pass

	def SynchronizeFrom(self, engineeringReference: IEngineeringReference) -> None:
		"""No Description

		Args
		--------
			engineeringReference (`IEngineeringReference`) :  engineeringReference

		Returns
		--------
			`None` : 
		"""
		pass

	def ConnectTo(self, engineeringReference: IEngineeringReference) -> None:
		"""No Description

		Args
		--------
			engineeringReference (`IEngineeringReference`) :  engineeringReference

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def SupportElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def EngineeringReferenceGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

	@property
	def EngineeringLibraryGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

	@property
	def DateModified(self) -> datetime:
		"""No Description

		Returns
		--------
			`datetime` : 
		"""
		pass

class ISupportElement2:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetEngineeringReference(self, engineeringLibraryGuid: Guid, engineeringReferenceGuid: Guid) -> None:
		"""No Description

		Args
		--------
			engineeringLibraryGuid (`Guid`) :  engineeringLibraryGuid
			engineeringReferenceGuid (`Guid`) :  engineeringReferenceGuid

		Returns
		--------
			`None` : 
		"""
		pass

class ISupportElementManager(IModelingElementManager, ISelectableManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportElementField(self, attributeName: str) -> IField:
		"""No Description

		Args
		--------
			attributeName (`str`) :  attributeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def Add(self, engineeringReference: IEngineeringReference) -> int:
		"""No Description

		Args
		--------
			engineeringReference (`IEngineeringReference`) :  engineeringReference

		Returns
		--------
			`int` : 
		"""
		pass

	def CrossElementFieldListManager(self, collectionFieldName: str, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> ICrossElementFieldListManager:
		"""No Description

		Args
		--------
			collectionFieldName (`str`) :  collectionFieldName
			sortContexts (`SortContextCollection`) :  sortContexts
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`ICrossElementFieldListManager` : 
		"""
		pass

	@overload
	def Add(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def SupportElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IControlManager(ISupportElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Flush(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def ResetWorkingUnits(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

class IPrototypeManager(IModelingElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ActivePrototypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActivePrototypeID.setter
	def ActivePrototypeID(self, activeprototypeid: int) -> None:
		pass

class IPrototypeDomainElementManager(IPrototypeManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def Exists(self, prototypeGuid: Guid) -> bool:
		"""No Description

		Args
		--------
			prototypeGuid (`Guid`) :  prototypeGuid

		Returns
		--------
			`bool` : 
		"""
		pass

	def ElementID(self, prototypeGuid: Guid) -> int:
		"""No Description

		Args
		--------
			prototypeGuid (`Guid`) :  prototypeGuid

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def Exists(self, id: int) -> bool:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def DomainElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IPrototypeDomainElement(IModelingElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	def SetPrototypeGuid(self, prototypeGuid: Guid) -> None:
		"""No Description

		Args
		--------
			prototypeGuid (`Guid`) :  prototypeGuid

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def DomainElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def PrototypeGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

class IFieldManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ModelingElementField(self, name: str, type: ModelingElementType, elementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			type (`ModelingElementType`) :  type
			elementTypeID (`int`) :  elementTypeID

		Returns
		--------
			`IField` : 
		"""
		pass

	def ModelingElementFields(self, type: ModelingElementType, elementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			type (`ModelingElementType`) :  type
			elementTypeID (`int`) :  elementTypeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def SupportElementFields(self, supportElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@overload
	def SupportElementField(self, name: str, supportElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def SupportElementField(self, name: str, supportElementTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			supportElementTypeName (`str`) :  supportElementTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, domainElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, domainElementTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			domainElementTypeName (`str`) :  domainElementTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, alternativeTypeID: int, domainElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, alternativeTypeName: str, domainElementTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			alternativeTypeName (`str`) :  alternativeTypeName
			domainElementTypeName (`str`) :  domainElementTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def AlternativeField(self, name: str, alternativeTypeID: int, domainElementTypeID: int, alternativeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementTypeID (`int`) :  domainElementTypeID
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def AlternativeField(self, name: str, alternativeTypeName: str, domainElementTypeName: str, alternativeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			alternativeTypeName (`str`) :  alternativeTypeName
			domainElementTypeName (`str`) :  domainElementTypeName
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def SystemRecordField(self, name: str, alternativeTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def SystemRecordField(self, name: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			alternativeTypeName (`str`) :  alternativeTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	def SystemRecordFields(self, alternativeTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@overload
	def AlternativeFields(self, alternativeTypeID: int, domainElementTypeID: int, alternativeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementTypeID (`int`) :  domainElementTypeID
			alternativeID (`int`) :  alternativeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@overload
	def AlternativeFields(self, domainElementTypeID: int, scenarioID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID
			scenarioID (`int`) :  scenarioID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def ResultField(self, name: str, numericalEngineType: str, resultRecordTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name
			numericalEngineType (`str`) :  numericalEngineType
			resultRecordTypeName (`str`) :  resultRecordTypeName

		Returns
		--------
			`IField` : 
		"""
		pass

	@overload
	def DomainElementFields(self, alternativeTypeID: int, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (`int`) :  alternativeTypeID
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@overload
	def DomainElementFields(self, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def ResultFields(self, numericalEngineTypeName: str, resultRecordTypeName: str, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName
			resultRecordTypeName (`str`) :  resultRecordTypeName
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def ScenarioResultFields(self, numericalEngineTypeName: str) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (`str`) :  numericalEngineTypeName

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def DomainDataSetField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

class IControlFieldManager(IFieldManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsLoadingControls(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsLoadingControls.setter
	def IsLoadingControls(self, isloadingcontrols: bool) -> None:
		pass

class IFieldManagerEx(IFieldManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportedFlexTableFields(self, domainElementTyepID: int, isPipeTwoScenarioFlexTable: bool) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTyepID (`int`) :  domainElementTyepID
			isPipeTwoScenarioFlexTable (`bool`) :  isPipeTwoScenarioFlexTable

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	def FlexTableField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

	def FlexTableFieldExists(self, elementTypeId: int, name: str) -> bool:
		"""No Description

		Args
		--------
			elementTypeId (`int`) :  elementTypeId
			name (`str`) :  name

		Returns
		--------
			`bool` : 
		"""
		pass

class IDomainField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetUniqueValues(self) -> array:
		"""No Description

		Returns
		--------
			`array` : 
		"""
		pass

	@property
	def FieldType(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

class IEnumeratedField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetEnumeratedMembers(self) -> List[IEnumeratedMember]:
		"""No Description

		Returns
		--------
			`List[IEnumeratedMember]` : 
		"""
		pass

class IEnumeratedMember:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Field(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

	def SupportedFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			`FieldCollection` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@property
	def ParentField(self) -> IField:
		"""No Description

		Returns
		--------
			`IField` : 
		"""
		pass

	@property
	def EnumerationValue(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IDataField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TableName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

class ICollectionField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetEmptyCollectionFieldListManager(self) -> ICollectionFieldListManager:
		"""No Description

		Returns
		--------
			`ICollectionFieldListManager` : 
		"""
		pass

class IUnitizedField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDoubleValue(self, id: int) -> float:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`float` : 
		"""
		pass

	@property
	def WorkingUnitIndex(self) -> UnitIndex:
		"""No Description

		Returns
		--------
			`UnitIndex` : 
		"""
		pass

	@WorkingUnitIndex.setter
	def WorkingUnitIndex(self, workingunitindex: UnitIndex) -> None:
		pass

	@property
	def StorageUnitIndex(self) -> UnitIndex:
		"""No Description

		Returns
		--------
			`UnitIndex` : 
		"""
		pass

class IPresentationUnitsManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDisplayUnitFor(self, formatterName: str) -> Unit:
		"""No Description

		Args
		--------
			formatterName (`str`) :  formatterName

		Returns
		--------
			`Unit` : 
		"""
		pass

	def StringFromDoubleUnit(self, value: float, formatterName: str, storageUnit: Unit) -> str:
		"""No Description

		Args
		--------
			value (`float`) :  value
			formatterName (`str`) :  formatterName
			storageUnit (`Unit`) :  storageUnit

		Returns
		--------
			`str` : 
		"""
		pass

class IGridElevationRetriever:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetGridElevationAtPoint(self, scenarioID: int, pointInMeters: GeometryPoint) -> float:
		"""No Description

		Args
		--------
			scenarioID (`int`) :  scenarioID
			pointInMeters (`GeometryPoint`) :  pointInMeters

		Returns
		--------
			`float` : 
		"""
		pass

class IGeometryField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ShouldUpdateBoundingBox(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ShouldUpdateBoundingBox.setter
	def ShouldUpdateBoundingBox(self, shouldupdateboundingbox: bool) -> None:
		pass

class IRealGeometryField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetGeometry(self, id: int) -> List[int]:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`List[int]` : 
		"""
		pass

	def SetGeometry(self, id: int, bytes: List[int]) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id
			bytes (`List[int]`) :  bytes

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def StorageUnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			`UnitSystem` : 
		"""
		pass

	@property
	def WorkingUnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			`UnitSystem` : 
		"""
		pass

	@WorkingUnitSystem.setter
	def WorkingUnitSystem(self, workingunitsystem: UnitSystem) -> None:
		pass

class IReferenceField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ReferencedElementManager(self) -> IModelingElementManager:
		"""No Description

		Returns
		--------
			`IModelingElementManager` : 
		"""
		pass

class IGeometryPointField(IUnitizedField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoint(self, id: int) -> GeometryPoint:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`GeometryPoint` : 
		"""
		pass

	def SetPoint(self, id: int, point: GeometryPoint) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id
			point (`GeometryPoint`) :  point

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryReferenceNodeField:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def RefreshReferenceNode(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`None` : 
		"""
		pass

	def RefreshReferenceNodes(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (`IHmIDToObjectDictionary`) :  valuesDic

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryPolylineField(IUnitizedField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self, id: int) -> List[GeometryPoint]:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`List[GeometryPoint]` : 
		"""
		pass

	def SetPoints(self, id: int, points: List[GeometryPoint]) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id
			points (`List[GeometryPoint]`) :  points

		Returns
		--------
			`None` : 
		"""
		pass

	def RefreshScaledLengths(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (`IHmIDToObjectDictionary`) :  valuesDic

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryPolyline3DField(IUnitizedField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self, id: int) -> List[GeometryPoint3D]:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`List[GeometryPoint3D]` : 
		"""
		pass

	def SetPoints(self, id: int, points3D: List[GeometryPoint3D]) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id
			points3D (`List[GeometryPoint3D]`) :  points3D

		Returns
		--------
			`None` : 
		"""
		pass

	def RefreshScaledLengths(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (`IHmIDToObjectDictionary`) :  valuesDic

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryLateralField:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def RefreshLateral(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID

		Returns
		--------
			`None` : 
		"""
		pass

	def RefreshLaterals(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (`IHmIDToObjectDictionary`) :  valuesDic

		Returns
		--------
			`None` : 
		"""
		pass

class IGeometryPolygonField(IUnitizedField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetRings(self, id: int) -> List[List[GeometryPoint]]:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`List[List[GeometryPoint]]` : 
		"""
		pass

	def SetRings(self, id: int, rings: List[List[GeometryPoint]]) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id
			rings (`List[List[GeometryPoint]]`) :  rings

		Returns
		--------
			`None` : 
		"""
		pass

	def RefreshScaledAreas(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (`IHmIDToObjectDictionary`) :  valuesDic

		Returns
		--------
			`None` : 
		"""
		pass

class IModelingElementField:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportedModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			`ModelingElementType` : 
		"""
		pass

	@property
	def ElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class ISupportElementField(IEditField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportElementType(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

class IDomainElementField(IDataField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AlternativeRecord(self) -> IAlternativeRecord:
		"""No Description

		Returns
		--------
			`IAlternativeRecord` : 
		"""
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	@property
	def DomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@property
	def OwnerDomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

class IEditDomainElementField(IEditField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def SetValue(self, elementID: int, makeLocal: bool, newValue: object) -> None:
		"""No Description

		Args
		--------
			elementID (`int`) :  elementID
			makeLocal (`bool`) :  makeLocal
			newValue (`object`) :  newValue

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def SetValue(self, id: int, value: object) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id
			value (`object`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

class ISystemRecordField(IField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

class IAlternativeField(IDomainElementField):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ActiveAlternativeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActiveAlternativeID.setter
	def ActiveAlternativeID(self, activealternativeid: int) -> None:
		pass

class ICollectionFieldListManager(IOrderedListManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Field(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (`str`) :  name

		Returns
		--------
			`IField` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

class ICrossElementFieldListManager(ICollectionFieldListManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Delete(self, indices: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			indices (`HmIDCollection`) :  indices

		Returns
		--------
			`None` : 
		"""
		pass

	def Reload(self, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			sortContexts (`SortContextCollection`) :  sortContexts
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def Delete(self, id: int) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def ActiveElementID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ActiveElementID.setter
	def ActiveElementID(self, activeelementid: int) -> None:
		pass

	@property
	def ActiveSortContexts(self) -> SortContextCollection:
		"""No Description

		Returns
		--------
			`SortContextCollection` : 
		"""
		pass

	@property
	def ActiveFilterContexts(self) -> FilterContextCollection:
		"""No Description

		Returns
		--------
			`FilterContextCollection` : 
		"""
		pass

class IAlternativeCrossElementFieldListManager(ICrossElementFieldListManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Reload(self, alternativeID: int, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			alternativeID (`int`) :  alternativeID
			sortContexts (`SortContextCollection`) :  sortContexts
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def Reload(self, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			sortContexts (`SortContextCollection`) :  sortContexts
			filterContexts (`FilterContextCollection`) :  filterContexts

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def ActiveAlternativeID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class ISelectableManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SelectElementIDs(self, sortContextCollection: SortContextCollection, filterContextCollection: FilterContextCollection) -> IHmIDDelayedCollection:
		"""No Description

		Args
		--------
			sortContextCollection (`SortContextCollection`) :  sortContextCollection
			filterContextCollection (`FilterContextCollection`) :  filterContextCollection

		Returns
		--------
			`IHmIDDelayedCollection` : 
		"""
		pass

	def Validate(self, filterContextCollection: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			filterContextCollection (`FilterContextCollection`) :  filterContextCollection

		Returns
		--------
			`None` : 
		"""
		pass

	def GetDataReader(self, queryName: str, fields: FieldTypeCollection, parametersMap: Dict) -> IFieldCollectionDataReader:
		"""No Description

		Args
		--------
			queryName (`str`) :  queryName
			fields (`FieldTypeCollection`) :  fields
			parametersMap (`Dict`) :  parametersMap

		Returns
		--------
			`IFieldCollectionDataReader` : 
		"""
		pass

class ISelectableManagerEx:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDataReader(self, queryName: str, fields: FieldTypeCollection, parametersMap: Dict) -> IDisposableEnumerable[IEnumeratorDataAccessor]:
		"""No Description

		Args
		--------
			queryName (`str`) :  queryName
			fields (`FieldTypeCollection`) :  fields
			parametersMap (`Dict`) :  parametersMap

		Returns
		--------
			`IDisposableEnumerable` : 
		"""
		pass

class IEnumeratorDataAccessor:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetElementID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	def GetNullableInt32(self, fieldIndex: int) -> Union[int, None]:
		"""No Description

		Args
		--------
			fieldIndex (`int`) :  fieldIndex

		Returns
		--------
			`Nullable` : 
		"""
		pass

	def GetInt32(self, fieldIndex: int) -> int:
		"""No Description

		Args
		--------
			fieldIndex (`int`) :  fieldIndex

		Returns
		--------
			`int` : 
		"""
		pass

	def GetDouble(self, fieldIndex: int, unitIndex: UnitIndex) -> float:
		"""No Description

		Args
		--------
			fieldIndex (`int`) :  fieldIndex
			unitIndex (`UnitIndex`) :  unitIndex

		Returns
		--------
			`float` : 
		"""
		pass

	def GetBoolean(self, fieldIndex: int) -> bool:
		"""No Description

		Args
		--------
			fieldIndex (`int`) :  fieldIndex

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetDateTime(self, fieldIndex: int) -> datetime:
		"""No Description

		Args
		--------
			fieldIndex (`int`) :  fieldIndex

		Returns
		--------
			`datetime` : 
		"""
		pass

	def GetString(self, fieldIndex: int) -> str:
		"""No Description

		Args
		--------
			fieldIndex (`int`) :  fieldIndex

		Returns
		--------
			`str` : 
		"""
		pass

	def GetBlob(self, fieldIndex: int) -> List[int]:
		"""No Description

		Args
		--------
			fieldIndex (`int`) :  fieldIndex

		Returns
		--------
			`List[int]` : 
		"""
		pass

	@property
	def FieldTypes(self) -> List[IFieldType]:
		"""No Description

		Returns
		--------
			`List[IFieldType]` : 
		"""
		pass

class IDisposableEnumerable(Generic[T], Iterator[T]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAlternativeRecordEx:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetDataReader(self, fieldTypeNames: array[str], filterContexts: FilterContextCollection, sortContexts: SortContextCollection) -> IDisposableEnumerable[IEnumeratorDataAccessor]:
		"""No Description

		Args
		--------
			fieldTypeNames (`array[str]`) :  fieldTypeNames
			filterContexts (`FilterContextCollection`) :  filterContexts
			sortContexts (`SortContextCollection`) :  sortContexts

		Returns
		--------
			`IDisposableEnumerable` : 
		"""
		pass

	@overload
	def GetDataReader(self, fieldTypeNames: array[str], domainElementTypeID: int) -> IAlternativeRecordDataReader:
		"""No Description

		Args
		--------
			fieldTypeNames (`array[str]`) :  fieldTypeNames
			domainElementTypeID (`int`) :  domainElementTypeID

		Returns
		--------
			`IAlternativeRecordDataReader` : 
		"""
		pass

class IHmIDDelayedCollection(ICloneable, List):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Contains(self, item: int) -> bool:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Sort(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: int) -> None:
		"""No Description

		Args
		--------
			item (`int`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Item(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Item.setter
	def Item(self, item: int) -> None:
		pass

class IUpdatedFieldInformation:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def OldFieldName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def NewFieldName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def NewSource(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def FieldUpdateType(self) -> FieldUpdateTypeEnum:
		"""No Description

		Returns
		--------
			`FieldUpdateTypeEnum` : 
		"""
		pass

	@property
	def IsResultField(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class IEngineeringLibrary(IEditLabeled, ITreeElementManager):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Exists(self, guid: Guid) -> bool:
		"""No Description

		Args
		--------
			guid (`Guid`) :  guid

		Returns
		--------
			`bool` : 
		"""
		pass

	def IsSourceAvailable(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def EngineeringLibraryField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	def GetEngineeringObject(self, aguid: Guid) -> IEngineeringReference:
		"""No Description

		Args
		--------
			aguid (`Guid`) :  aguid

		Returns
		--------
			`IEngineeringReference` : 
		"""
		pass

	def AddFolder(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	def Commit(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Close(self, allowPrompts: bool) -> None:
		"""No Description

		Args
		--------
			allowPrompts (`bool`) :  allowPrompts

		Returns
		--------
			`None` : 
		"""
		pass

	def ForceCheckIfAvailable(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def GetSourceEngineeringLibraryTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@overload
	def Exists(self, id: int) -> bool:
		"""No Description

		Args
		--------
			id (`int`) :  id

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Guid(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

	@property
	def Source(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Source.setter
	def Source(self, source: str) -> None:
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def EngineeringLibraryTypeName(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def DateModified(self) -> datetime:
		"""No Description

		Returns
		--------
			`datetime` : 
		"""
		pass

	@property
	def IsEditable(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsEnumerable(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsInProjectWise(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class IEngineeringLibraryEx:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPersistedGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

class IEngineeringReference(ITreeElement):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EngineeringReferenceField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (`str`) :  fieldName

		Returns
		--------
			`IField` : 
		"""
		pass

	def SynchronizeFrom(self, supportElement: ISupportElement) -> None:
		"""No Description

		Args
		--------
			supportElement (`ISupportElement`) :  supportElement

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Guid(self) -> Guid:
		"""No Description

		Returns
		--------
			`Guid` : 
		"""
		pass

	@property
	def DateModified(self) -> datetime:
		"""No Description

		Returns
		--------
			`datetime` : 
		"""
		pass

	@property
	def EngineeringLibrary(self) -> IEngineeringLibrary:
		"""No Description

		Returns
		--------
			`IEngineeringLibrary` : 
		"""
		pass

class IBlobable:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetBytes(self) -> List[int]:
		"""No Description

		Returns
		--------
			`List[int]` : 
		"""
		pass

	def GetNumberOfBytes(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class ModelingElementCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ModelingElementCollection`) :  c
			a (`List[IModelingElement]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ModelingElementCollection`) :  c
			a (`List[IModelingElement]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: ModelingElementCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ModelingElementCollection`) :  c
			a (`List[IModelingElement]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IModelingElement]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ModelingElementCollection`) :  c
			a (`List[IModelingElement]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: ModelingElementCollection) -> ModelingElementCollection:
		"""No Description

		Args
		--------
			list (`ModelingElementCollection`) :  list

		Returns
		--------
			`ModelingElementCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: ModelingElementCollection) -> ModelingElementCollection:
		"""No Description

		Args
		--------
			list (`ModelingElementCollection`) :  list

		Returns
		--------
			`ModelingElementCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IModelingElement]) -> None:
		"""No Description

		Args
		--------
			array (`List[IModelingElement]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IModelingElement], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IModelingElement]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IModelingElement) -> int:
		"""No Description

		Args
		--------
			item (`IModelingElement`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IModelingElement) -> bool:
		"""No Description

		Args
		--------
			item (`IModelingElement`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IModelingElement) -> int:
		"""No Description

		Args
		--------
			item (`IModelingElement`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IModelingElement) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IModelingElement`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IModelingElement) -> None:
		"""No Description

		Args
		--------
			item (`IModelingElement`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IModelingElementCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IModelingElementCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ModelingElementCollection) -> int:
		"""No Description

		Args
		--------
			x (`ModelingElementCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IModelingElement]) -> int:
		"""No Description

		Args
		--------
			x (`List[IModelingElement]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IModelingElement:
		"""No Description

		Returns
		--------
			`IModelingElement` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IModelingElement) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class NumericalEngineTypeCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`NumericalEngineTypeCollection`) :  c
			a (`List[INumericalEngineType]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`NumericalEngineTypeCollection`) :  c
			a (`List[INumericalEngineType]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: NumericalEngineTypeCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`NumericalEngineTypeCollection`) :  c
			a (`List[INumericalEngineType]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[INumericalEngineType]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`NumericalEngineTypeCollection`) :  c
			a (`List[INumericalEngineType]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: NumericalEngineTypeCollection) -> NumericalEngineTypeCollection:
		"""No Description

		Args
		--------
			list (`NumericalEngineTypeCollection`) :  list

		Returns
		--------
			`NumericalEngineTypeCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: NumericalEngineTypeCollection) -> NumericalEngineTypeCollection:
		"""No Description

		Args
		--------
			list (`NumericalEngineTypeCollection`) :  list

		Returns
		--------
			`NumericalEngineTypeCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[INumericalEngineType]) -> None:
		"""No Description

		Args
		--------
			array (`List[INumericalEngineType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[INumericalEngineType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[INumericalEngineType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: INumericalEngineType) -> int:
		"""No Description

		Args
		--------
			item (`INumericalEngineType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: INumericalEngineType) -> bool:
		"""No Description

		Args
		--------
			item (`INumericalEngineType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: INumericalEngineType) -> int:
		"""No Description

		Args
		--------
			item (`INumericalEngineType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`INumericalEngineType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			item (`INumericalEngineType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> INumericalEngineTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`INumericalEngineTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: NumericalEngineTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`NumericalEngineTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[INumericalEngineType]) -> int:
		"""No Description

		Args
		--------
			x (`List[INumericalEngineType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: INumericalEngineType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ResultRecordCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordCollection`) :  c
			a (`List[IResultRecord]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordCollection`) :  c
			a (`List[IResultRecord]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: ResultRecordCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordCollection`) :  c
			a (`List[IResultRecord]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IResultRecord]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordCollection`) :  c
			a (`List[IResultRecord]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: ResultRecordCollection) -> ResultRecordCollection:
		"""No Description

		Args
		--------
			list (`ResultRecordCollection`) :  list

		Returns
		--------
			`ResultRecordCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: ResultRecordCollection) -> ResultRecordCollection:
		"""No Description

		Args
		--------
			list (`ResultRecordCollection`) :  list

		Returns
		--------
			`ResultRecordCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecord]) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecord]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecord], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecord]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IResultRecord) -> int:
		"""No Description

		Args
		--------
			item (`IResultRecord`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IResultRecord) -> bool:
		"""No Description

		Args
		--------
			item (`IResultRecord`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IResultRecord) -> int:
		"""No Description

		Args
		--------
			item (`IResultRecord`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IResultRecord) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IResultRecord`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IResultRecord) -> None:
		"""No Description

		Args
		--------
			item (`IResultRecord`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IResultRecordCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IResultRecordCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ResultRecordCollection) -> int:
		"""No Description

		Args
		--------
			x (`ResultRecordCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IResultRecord]) -> int:
		"""No Description

		Args
		--------
			x (`List[IResultRecord]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IResultRecord:
		"""No Description

		Returns
		--------
			`IResultRecord` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IResultRecord) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ResultRecordTypeCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordTypeCollection`) :  c
			a (`List[IResultRecordType]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordTypeCollection`) :  c
			a (`List[IResultRecordType]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: ResultRecordTypeCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordTypeCollection`) :  c
			a (`List[IResultRecordType]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[IResultRecordType]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`ResultRecordTypeCollection`) :  c
			a (`List[IResultRecordType]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: ResultRecordTypeCollection) -> ResultRecordTypeCollection:
		"""No Description

		Args
		--------
			list (`ResultRecordTypeCollection`) :  list

		Returns
		--------
			`ResultRecordTypeCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: ResultRecordTypeCollection) -> ResultRecordTypeCollection:
		"""No Description

		Args
		--------
			list (`ResultRecordTypeCollection`) :  list

		Returns
		--------
			`ResultRecordTypeCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecordType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecordType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecordType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecordType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: IResultRecordType) -> int:
		"""No Description

		Args
		--------
			item (`IResultRecordType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: IResultRecordType) -> bool:
		"""No Description

		Args
		--------
			item (`IResultRecordType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: IResultRecordType) -> int:
		"""No Description

		Args
		--------
			item (`IResultRecordType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: IResultRecordType) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`IResultRecordType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: IResultRecordType) -> None:
		"""No Description

		Args
		--------
			item (`IResultRecordType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IResultRecordTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IResultRecordTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ResultRecordTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`ResultRecordTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IResultRecordType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IResultRecordType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IResultRecordType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class StandardFieldName:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class StandardAlternativeName:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class StandardDomainElementTypeName:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	def GetStandardDomainElementTypeName(DomainElementTypeID: int) -> str:
		"""No Description

		Args
		--------
			DomainElementTypeID (`int`) :  DomainElementTypeID

		Returns
		--------
			`str` : 
		"""
		pass

class StandardDomainDataSetFieldNames:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class StandardSupportElementTypeName:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	def GetStandardSupportElementTypeName(supportElementTypeID: int) -> str:
		"""No Description

		Args
		--------
			supportElementTypeID (`int`) :  supportElementTypeID

		Returns
		--------
			`str` : 
		"""
		pass

class StandardResultRecordName:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class StandardResultFieldName:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class StandardCalculationOptionFieldName:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class StandardExtendedProperty:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class UntitledNameLibrary:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	def NewElementLabel(typeName: str, manager: IModelingElementManager) -> str:
		"""No Description

		Args
		--------
			typeName (`str`) :  typeName
			manager (`IModelingElementManager`) :  manager

		Returns
		--------
			`str` : 
		"""
		pass

class StandardFieldNameLibrary:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	@overload
	def GetUnifiedLengthField(domainDataSet: IDomainDataSet, linkElementId: int) -> IUnitizedField:
		"""No Description

		Args
		--------
			domainDataSet (`IDomainDataSet`) :  domainDataSet
			linkElementId (`int`) :  linkElementId

		Returns
		--------
			`IUnitizedField` : 
		"""
		pass

	@staticmethod
	@overload
	def GetUnifiedLengthField(domainElementType: int, domainDataSet: IDomainDataSet) -> IUnitizedField:
		"""No Description

		Args
		--------
			domainElementType (`int`) :  domainElementType
			domainDataSet (`IDomainDataSet`) :  domainDataSet

		Returns
		--------
			`IUnitizedField` : 
		"""
		pass

	@staticmethod
	def GetSlopeField(domainElementType: int, domainDataSet: IDomainDataSet) -> IUnitizedField:
		"""No Description

		Args
		--------
			domainElementType (`int`) :  domainElementType
			domainDataSet (`IDomainDataSet`) :  domainDataSet

		Returns
		--------
			`IUnitizedField` : 
		"""
		pass

class PipeNodeFieldNames:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class StandardElementTypePermission:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@staticmethod
	def Assert() -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	def RevertAssert() -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	def IsGranted() -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class SupportElementTypeCollection(List, ICloneable):

	@overload
	def __new__(self) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`SupportElementTypeCollection`) :  c
			a (`List[ISupportElementType]`) :  a
		"""
		pass

	@overload
	def __new__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`SupportElementTypeCollection`) :  c
			a (`List[ISupportElementType]`) :  a
		"""
		pass

	@overload
	def __new__(self, c: SupportElementTypeCollection) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`SupportElementTypeCollection`) :  c
			a (`List[ISupportElementType]`) :  a
		"""
		pass

	@overload
	def __new__(self, a: List[ISupportElementType]) -> None:
		"""No Description

		Args
		--------
			capacity (`int`) :  capacity
			c (`SupportElementTypeCollection`) :  c
			a (`List[ISupportElementType]`) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: SupportElementTypeCollection) -> SupportElementTypeCollection:
		"""No Description

		Args
		--------
			list (`SupportElementTypeCollection`) :  list

		Returns
		--------
			`SupportElementTypeCollection` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: SupportElementTypeCollection) -> SupportElementTypeCollection:
		"""No Description

		Args
		--------
			list (`SupportElementTypeCollection`) :  list

		Returns
		--------
			`SupportElementTypeCollection` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISupportElementType]) -> None:
		"""No Description

		Args
		--------
			array (`List[ISupportElementType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISupportElementType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[ISupportElementType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, item: ISupportElementType) -> int:
		"""No Description

		Args
		--------
			item (`ISupportElementType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def Contains(self, item: ISupportElementType) -> bool:
		"""No Description

		Args
		--------
			item (`ISupportElementType`) :  item

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, item: ISupportElementType) -> int:
		"""No Description

		Args
		--------
			item (`ISupportElementType`) :  item

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, index: int, item: ISupportElementType) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index
			item (`ISupportElementType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, item: ISupportElementType) -> None:
		"""No Description

		Args
		--------
			item (`ISupportElementType`) :  item

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (`int`) :  index

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> ISupportElementTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`ISupportElementTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: SupportElementTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`SupportElementTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[ISupportElementType]) -> int:
		"""No Description

		Args
		--------
			x (`List[ISupportElementType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: ISupportElementType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IAlternativeTypeCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

class Enumerator(IEnumerator, IAlternativeTypeCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

class SyncAlternativeTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IAlternativeType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IAlternativeType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IAlternativeType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IAlternativeType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IAlternativeType) -> int:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IAlternativeType) -> bool:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IAlternativeType) -> int:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IAlternativeType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IAlternativeTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IAlternativeTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: AlternativeTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`AlternativeTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IAlternativeType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IAlternativeType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IAlternativeType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyAlternativeTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IAlternativeType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IAlternativeType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IAlternativeType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IAlternativeType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IAlternativeType) -> int:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IAlternativeType) -> bool:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IAlternativeType) -> int:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IAlternativeType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			x (`IAlternativeType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IAlternativeTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IAlternativeTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: AlternativeTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`AlternativeTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IAlternativeType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IAlternativeType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			`IAlternativeType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IAlternativeType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IFieldTypeCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

class Enumerator(IEnumerator, IFieldTypeCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

class SyncFieldTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFieldType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IFieldType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFieldType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IFieldType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IFieldType) -> int:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IFieldType) -> bool:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IFieldType) -> int:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IFieldType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IFieldType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IFieldType) -> None:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IFieldTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IFieldTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: FieldTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`FieldTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IFieldType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IFieldType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IFieldType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyFieldTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFieldType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IFieldType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFieldType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IFieldType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IFieldType) -> int:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IFieldType) -> bool:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IFieldType) -> int:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IFieldType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IFieldType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IFieldType) -> None:
		"""No Description

		Args
		--------
			x (`IFieldType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IFieldTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IFieldTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: FieldTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`FieldTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IFieldType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IFieldType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IFieldType:
		"""No Description

		Returns
		--------
			`IFieldType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IFieldType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IDomainDataSetCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

class Enumerator(IEnumerator, IDomainDataSetCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

class SyncDomainDataSetCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSet]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSet]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSet], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSet]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IDomainDataSet) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IDomainDataSet) -> bool:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IDomainDataSet) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IDomainDataSet) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IDomainDataSet) -> None:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainDataSetCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainDataSetCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainDataSetCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainDataSetCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainDataSet]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainDataSet]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainDataSet) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyDomainDataSetCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSet]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSet]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSet], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSet]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IDomainDataSet) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IDomainDataSet) -> bool:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IDomainDataSet) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IDomainDataSet) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IDomainDataSet) -> None:
		"""No Description

		Args
		--------
			x (`IDomainDataSet`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainDataSetCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainDataSetCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainDataSetCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainDataSetCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainDataSet]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainDataSet]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			`IDomainDataSet` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainDataSet) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IDomainDataSetTypeCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

class Enumerator(IEnumerator, IDomainDataSetTypeCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

class SyncDomainDataSetTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSetType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSetType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSetType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSetType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IDomainDataSetType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IDomainDataSetType) -> bool:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IDomainDataSetType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IDomainDataSetType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IDomainDataSetType) -> None:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainDataSetTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainDataSetTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainDataSetTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainDataSetTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainDataSetType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainDataSetType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainDataSetType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyDomainDataSetTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSetType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSetType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainDataSetType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainDataSetType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IDomainDataSetType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IDomainDataSetType) -> bool:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IDomainDataSetType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IDomainDataSetType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IDomainDataSetType) -> None:
		"""No Description

		Args
		--------
			x (`IDomainDataSetType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainDataSetTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainDataSetTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainDataSetTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainDataSetTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainDataSetType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainDataSetType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			`IDomainDataSetType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainDataSetType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IDomainElementTypeCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

class Enumerator(IEnumerator, IDomainElementTypeCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

class SyncDomainElementTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainElementType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainElementType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainElementType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainElementType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IDomainElementType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IDomainElementType) -> bool:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IDomainElementType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IDomainElementType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IDomainElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IDomainElementType) -> None:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainElementTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainElementTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainElementTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainElementTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainElementType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainElementType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainElementType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyDomainElementTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainElementType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainElementType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IDomainElementType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IDomainElementType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IDomainElementType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IDomainElementType) -> bool:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IDomainElementType) -> int:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IDomainElementType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IDomainElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IDomainElementType) -> None:
		"""No Description

		Args
		--------
			x (`IDomainElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IDomainElementTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IDomainElementTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: DomainElementTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`DomainElementTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IDomainElementType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IDomainElementType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			`IDomainElementType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IDomainElementType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IModelingElementCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IModelingElement:
		"""No Description

		Returns
		--------
			`IModelingElement` : 
		"""
		pass

class Enumerator(IEnumerator, IModelingElementCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IModelingElement:
		"""No Description

		Returns
		--------
			`IModelingElement` : 
		"""
		pass

class SyncModelingElementCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IModelingElement]) -> None:
		"""No Description

		Args
		--------
			array (`List[IModelingElement]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IModelingElement], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IModelingElement]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IModelingElement) -> int:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IModelingElement) -> bool:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IModelingElement) -> int:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IModelingElement) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IModelingElement`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IModelingElement) -> None:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IModelingElementCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IModelingElementCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ModelingElementCollection) -> int:
		"""No Description

		Args
		--------
			x (`ModelingElementCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IModelingElement]) -> int:
		"""No Description

		Args
		--------
			x (`List[IModelingElement]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IModelingElement:
		"""No Description

		Returns
		--------
			`IModelingElement` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IModelingElement) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyModelingElementCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IModelingElement]) -> None:
		"""No Description

		Args
		--------
			array (`List[IModelingElement]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IModelingElement], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IModelingElement]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IModelingElement) -> int:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IModelingElement) -> bool:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IModelingElement) -> int:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IModelingElement) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IModelingElement`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IModelingElement) -> None:
		"""No Description

		Args
		--------
			x (`IModelingElement`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IModelingElementCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IModelingElementCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ModelingElementCollection) -> int:
		"""No Description

		Args
		--------
			x (`ModelingElementCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IModelingElement]) -> int:
		"""No Description

		Args
		--------
			x (`List[IModelingElement]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IModelingElement:
		"""No Description

		Returns
		--------
			`IModelingElement` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IModelingElement) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class INumericalEngineTypeCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

class Enumerator(IEnumerator, INumericalEngineTypeCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

class SyncNumericalEngineTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[INumericalEngineType]) -> None:
		"""No Description

		Args
		--------
			array (`List[INumericalEngineType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[INumericalEngineType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[INumericalEngineType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: INumericalEngineType) -> int:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: INumericalEngineType) -> bool:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: INumericalEngineType) -> int:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> INumericalEngineTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`INumericalEngineTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: NumericalEngineTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`NumericalEngineTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[INumericalEngineType]) -> int:
		"""No Description

		Args
		--------
			x (`List[INumericalEngineType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: INumericalEngineType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyNumericalEngineTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[INumericalEngineType]) -> None:
		"""No Description

		Args
		--------
			array (`List[INumericalEngineType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[INumericalEngineType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[INumericalEngineType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: INumericalEngineType) -> int:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: INumericalEngineType) -> bool:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: INumericalEngineType) -> int:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			x (`INumericalEngineType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> INumericalEngineTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`INumericalEngineTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: NumericalEngineTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`NumericalEngineTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[INumericalEngineType]) -> int:
		"""No Description

		Args
		--------
			x (`List[INumericalEngineType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			`INumericalEngineType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: INumericalEngineType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IResultRecordCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IResultRecord:
		"""No Description

		Returns
		--------
			`IResultRecord` : 
		"""
		pass

class Enumerator(IEnumerator, IResultRecordCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IResultRecord:
		"""No Description

		Returns
		--------
			`IResultRecord` : 
		"""
		pass

class SyncResultRecordCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecord]) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecord]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecord], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecord]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IResultRecord) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IResultRecord) -> bool:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IResultRecord) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IResultRecord) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IResultRecord`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IResultRecord) -> None:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IResultRecordCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IResultRecordCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ResultRecordCollection) -> int:
		"""No Description

		Args
		--------
			x (`ResultRecordCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IResultRecord]) -> int:
		"""No Description

		Args
		--------
			x (`List[IResultRecord]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IResultRecord:
		"""No Description

		Returns
		--------
			`IResultRecord` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IResultRecord) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyResultRecordCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecord]) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecord]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecord], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecord]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IResultRecord) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IResultRecord) -> bool:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IResultRecord) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IResultRecord) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IResultRecord`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IResultRecord) -> None:
		"""No Description

		Args
		--------
			x (`IResultRecord`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IResultRecordCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IResultRecordCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ResultRecordCollection) -> int:
		"""No Description

		Args
		--------
			x (`ResultRecordCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IResultRecord]) -> int:
		"""No Description

		Args
		--------
			x (`List[IResultRecord]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IResultRecord:
		"""No Description

		Returns
		--------
			`IResultRecord` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IResultRecord) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IResultRecordTypeCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

class Enumerator(IEnumerator, IResultRecordTypeCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

class SyncResultRecordTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecordType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecordType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecordType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecordType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IResultRecordType) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IResultRecordType) -> bool:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IResultRecordType) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IResultRecordType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IResultRecordType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IResultRecordType) -> None:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IResultRecordTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IResultRecordTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ResultRecordTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`ResultRecordTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IResultRecordType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IResultRecordType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IResultRecordType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlyResultRecordTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecordType]) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecordType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IResultRecordType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[IResultRecordType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: IResultRecordType) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: IResultRecordType) -> bool:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: IResultRecordType) -> int:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: IResultRecordType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`IResultRecordType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: IResultRecordType) -> None:
		"""No Description

		Args
		--------
			x (`IResultRecordType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> IResultRecordTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`IResultRecordTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: ResultRecordTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`ResultRecordTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IResultRecordType]) -> int:
		"""No Description

		Args
		--------
			x (`List[IResultRecordType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			`IResultRecordType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IResultRecordType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ISupportElementTypeCollectionEnumerator:

	def __new__(self) -> None:
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
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

class Enumerator(IEnumerator, ISupportElementTypeCollectionEnumerator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Current(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

class SyncSupportElementTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISupportElementType]) -> None:
		"""No Description

		Args
		--------
			array (`List[ISupportElementType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISupportElementType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[ISupportElementType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: ISupportElementType) -> int:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: ISupportElementType) -> bool:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: ISupportElementType) -> int:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: ISupportElementType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`ISupportElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: ISupportElementType) -> None:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> ISupportElementTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`ISupportElementTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: SupportElementTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`SupportElementTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[ISupportElementType]) -> int:
		"""No Description

		Args
		--------
			x (`List[ISupportElementType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: ISupportElementType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class ReadOnlySupportElementTypeCollection(List, ICloneable):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISupportElementType]) -> None:
		"""No Description

		Args
		--------
			array (`List[ISupportElementType]`) :  array

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISupportElementType], start: int) -> None:
		"""No Description

		Args
		--------
			array (`List[ISupportElementType]`) :  array
			start (`int`) :  start

		Returns
		--------
			`None` : 
		"""
		pass

	def Add(self, x: ISupportElementType) -> int:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Contains(self, x: ISupportElementType) -> bool:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`bool` : 
		"""
		pass

	def IndexOf(self, x: ISupportElementType) -> int:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Insert(self, pos: int, x: ISupportElementType) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos
			x (`ISupportElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def Remove(self, x: ISupportElementType) -> None:
		"""No Description

		Args
		--------
			x (`ISupportElementType`) :  x

		Returns
		--------
			`None` : 
		"""
		pass

	def RemoveAt(self, pos: int) -> None:
		"""No Description

		Args
		--------
			pos (`int`) :  pos

		Returns
		--------
			`None` : 
		"""
		pass

	def GetEnumerator(self) -> ISupportElementTypeCollectionEnumerator:
		"""No Description

		Returns
		--------
			`ISupportElementTypeCollectionEnumerator` : 
		"""
		pass

	@overload
	def AddRange(self, x: SupportElementTypeCollection) -> int:
		"""No Description

		Args
		--------
			x (`SupportElementTypeCollection`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[ISupportElementType]) -> int:
		"""No Description

		Args
		--------
			x (`List[ISupportElementType]`) :  x

		Returns
		--------
			`int` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			`object` : 
		"""
		pass

	@property
	def Item(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			`ISupportElementType` : 
		"""
		pass

	@Item.setter
	def Item(self, item: ISupportElementType) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

