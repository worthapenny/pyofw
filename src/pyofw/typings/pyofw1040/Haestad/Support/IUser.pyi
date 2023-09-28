from enum import Enum
from System import EventHandler, EventArgs, IAsyncResult, AsyncCallback, ICloneable, TimeSpan, IComparable, IntPtr
from typing import overload, List
from System.Runtime.Serialization import SerializationInfo, StreamingContext, ISerializable
from Haestad.Support.ISupport import INamable, ILabeled
from array import array
from System.Collections import SortedList
from datetime import datetime

class MessageHandlerResult(Enum):
	OK = 0
	Yes = 1
	No = 2
	Cancel = 3

class StatusMessageTypes(Enum):
	Message = 0
	Info = 1
	Warning = 2
	Error = 3

class DialogYesNoToAllResult(Enum):
	Yes = 0
	YesToAll = 1
	No = 2
	NoToAll = 3
	Cancel = 4

class PromptKey(Enum):
	SaveNewerSchema = 0
	AttachIsolationValve = 1
	AutoUpdateIsoValveGeometry = 2
	UseUnitandDemandControlCenter = 3
	UseDemandControlCenter = 4
	Skelebrator_SmartPipeRemoval = 5
	IDFStormEventsExportToLibrary = 6
	BatchUpdateConduitDescriptions = 7
	DarwinAdjustmentGroupExported = 8
	ScenarioCreator = 9
	ClearUndoForSubmodelImport = 10
	ClearUndoForModelBuilder = 11
	TransientResultsViewer = 12
	DeleteConfirmationPrompt = 13
	UseInflowControlCenter = 14
	UseSanitaryInflowControlCenter = 15
	UseSanitaryLoadsControlCenter = 16
	OpenUnfilteredFlexTable = 17
	SchedulerDimensionality = 18
	SchedulerRepresentativeScenarioNotCalculated = 19
	ComputeSingleFlushingEvent = 20
	OverrideInvalidMorph = 21
	OverrideInvalidLinkSplit = 22
	OverrideInvalidReconnectStart = 23
	OverrideInvalidReconnectStop = 24
	MDBsToBeConvertedToSQLite = 25
	LogicalControlsStormSewerNote = 26
	WildcardsChangedWithSQLite = 27
	ClearUndoForBatchMorph = 28
	UseConventionalEventQuickEdit = 29
	SCADAInitialSettingsImportWarning = 30
	ParallelFireFlowCalculationsOptionInformation = 31
	LayoutTapsWithoutAttachingToInvalidLinks = 32
	FlushingReportOverflowingValves = 33
	ImportControls = 34
	CandidateElementsToCloseReRunQuery = 35
	UpdateDatabaseCaches = 36
	CONNECTProjectAssociation = 37
	AddMyFlexTablesMessage = 38
	CONNECTProjectAssociationAdv = 39
	UseGISIDControlCenter = 40
	UseDeletedGISIDTable = 41
	SaveToPackage = 42
	DMAStatusAssigned = 43
	DMAStatusBoundaryCandidate = 44
	ArchiveChangeLog = 45
	ArchiveComplete = 46
	ArcGISProJoins = 47
	FireFlowConstraints = 48
	SELECTEntitlements = 49
	ExportToFile = 50
	Generate2DGridUponCompute = 51
	BackgroundLayerIssues = 52
	TrackedChangesSizeInformation = 53

class MessageKeys(Enum):
	CoreReserved0 = 0
	CoreException = 1
	CoreReserved2 = 2
	CoreReserved3 = 3
	ReadOnlyResultsError = 4
	CoreImportElementLabeling = 5
	CoreMessagesAvailableForLoading = 6
	Success = 7
	UnsupportedSchemaVersionForImport = 8
	InvalidAlternativeId = 25
	InvalidDimension = 26
	InvalidStorageUnit = 27
	InvalidFormatter = 28
	DuplicateName = 29
	DuplicateLabel = 30
	DuplicateEnumerationValue = 31
	InvalidEnumerationDefaultValue = 32
	InvalidName = 33
	MaximumUserNotificationCountReached = 34
	PpkTableNoItemsTable = 136
	PpkTableNotEnoughItems = 137
	PpkTableNotSorted = 138
	PpkTableNoItem = 139
	PpkTableNoItems = 140
	CriticalityEngineUnbalancedBaseScenario = 4200
	CheckMinorLossesForSplitPipes = 5000
	CheckMinorLossesForSplitPipesInAlternative = 5001
	SaveToPackageMissingBackgroundLayer = 5002
	SaveToPackageMissingTerrainModel = 5003
	SaveToPackageMissingSWMMClimatologyFile = 5004
	SaveToPackageMissingSWMMRainfallFile = 5005
	SaveToPackageMissingSWMMInterfaceFile = 5006
	SaveToPackageMissingGridAdjustmentLayer = 5007
	SaveToPackageCustomResultsExcluded = 5008
	GridOutflowTributariesNotSupported = 6814
	GridChannelDoesNotIntersectPond = 6815
	FmwReserved10000 = 10000
	FmwReserved10001 = 10001
	FmwReserved10002 = 10002
	CsdReserved20000 = 20000
	CsdReserved20001 = 20001
	CsdOutflowNode = 20002
	CsdTopologyNodeNotInPolygon = 20003
	DMWControlStructureInvertElevation = 20004
	DMWControlStructureDownstreamID = 20005
	DMWControlStructureSameUpstreamDownstreamID = 20006
	DMWControlStructureManagerCount = 20007
	DMWControlStructureEQTWMaxed = 20008
	DMWCulvertHeight = 20010
	DMWCulvertWidth = 20011
	DMWCulvertDiameter = 20012
	DMWCulvertLength = 20013
	DMWCulvertManningsN = 20014
	DMWCulvertNumberOfBarrels = 20015
	DMWCulvertC = 20016
	DMWCulvertM = 20017
	DMWCulvertK = 20018
	DMWCulvertY = 20019
	DMWCulvertKe = 20020
	DMWCulvertKr = 20021
	DMWOrificeDiameter = 20022
	DMWOrificeArea = 20023
	DMWOrificeDatumVsInvert = 20024
	DMWOrificeTopElevationVsInvert = 20025
	DMWOrificeNumberOfOpenings = 20026
	DMWOrificeCoefficient = 20027
	DMWRiserWeirLength = 20030
	DMWRiserOrificeArea = 20031
	DMWRiserDiameter = 20032
	DMWRiserWeirCoefficient = 20033
	DMWRiserOrificeCoefficient = 20034
	DMWWeirLength = 20040
	DMWVnotchAngle = 20041
	DMWWeirCrossSectionCount = 20042
	DMWWeirOutOfRange = 20043
	DMWWeirOutOfRangeMax = 20044
	DMWWeirCoefficient = 20045
	DMWHeadwaterMinimum = 20050
	DMWHeadwaterIncrement = 20051
	DMWTailwaterMaxIterations = 20055
	DMWTailwaterMinimum = 20056
	DMWTailwaterIncrement = 20057
	DMWControlInvertLessDNInvert = 20058
	DmwPipeUPInvertVsDNInvert = 20060
	DmwPipeLengthMinimum = 20061
	DmwPipeLengthVsSlope = 20062
	DmwPipeDiameter = 20063
	DmwPipeNumberOfBarrels = 20064
	DmwGuhCount = 20065
	DmwGuhConvolutionTimeStep = 20066
	DmwTimeOfConcentration = 20067
	DmwCompositeCn = 20068
	DmwCompositeArea = 20069
	DmwCatchmentArea = 20070
	DmwfLoss = 20071
	DmwGAAKs = 20072
	DmwHortonK = 20073
	DmwHortonfc = 20074
	DmwHortonfo = 20075
	DmwUserDefinedHydrographCount = 20076
	EPARunoffFailed = 20077
	DmwRationalMethodC = 20078
	DmwMixHydrologyMethods = 20079
	DmwGlobalRainfall = 20080
	DmwRainfallStartTime = 20081
	DmwRainfallStepTime = 20082
	DmwRainfallEndTime = 20083
	DmwRainfallEndVsStartTime = 20084
	DmwRainfallStepVsStartEndTime = 20085
	DmwRainfallCount = 20086
	DmwRainfallPointVsPreviousPoint = 20087
	DmwStormEventDepth = 20088
	DmwInvalidRationalMethodStorm = 20089
	DmwIdfStormDuration = 20090
	DmwTcMultiplier = 20091
	DmwInvalidGlobalStormType = 20092
	DmwLocalRainfall = 20093
	DmwInvalidLocalStormType = 20094
	DmwRainfallPointNegative = 20095
	SwmmStructureHeadloss = 20100
	SwmmCatchbasinInletCapture = 20101
	SwmmCulvertData = 20102
	SwmmNumberOfBarrels = 20103
	SwmmCatchments = 20104
	SwmmGutters = 20105
	SwmmOutfallElevationFlow = 20106
	SwmmNoControlStructureAssigned = 20107
	SwmmVariantRoughnessMethod = 20108
	SwmmNoBoundaryElementSelected = 20109
	SwmmNoPumpsAtPumpStation = 20110
	SwmmNoSuctionNode = 20111
	SwmmIDFDataNotSupportedBySwmm = 20112
	SwmmCatchmentCharWidth = 20113
	SwmmCatchmentSlope = 20114
	SwmmCatchmentImperviousManningsN = 20115
	SwmmCatchmentPerviousManningsN = 20116
	SwmmNoOutfalls = 20117
	SwmmDuplicateLabels = 20118
	SwmmNoLabel = 20119
	SwmmNoPressurePipe = 20120
	SwmmNoPressureJunction = 20121
	SwmmNoPollutantSelected = 20122
	SwmmDryTimeIncrement = 20123
	SwmmNoPollutographSelected = 20124
	SwmmPollutographNegativeConcentration = 20125
	SwmmPollutographNegativeMass = 20126
	SwmmNegativeMassConversionRate = 20127
	SwmmTimesNotIncreasing = 20128
	SwmmNegativeTime = 20129
	SwmmClosedIrregularChannel = 20130
	SwmmStationsMustBeIncreasing = 20131
	SwmmRoutingIncrementLessThanOutputIncrement = 20132
	SwmmPumpIsDisconnected = 20133
	SwmmInvalidRimGroundInvert = 20134
	SwmmInvalidFillDepth = 20135
	SwmmProblemPumpCurve = 20136
	SwmmValueMustBeGreaterThanZero = 20137
	SwmmOnlySupportsConstantInfiltration = 20138
	SwmmDiversionCurveHasZeroPoints = 20139
	SwmmFileIsMissing = 20140
	SwmmValueCannotBeNegative = 20141
	SwmmLocalRainfallNotSpecified = 20142
	SwmmInvalidReference = 20143
	SwmmNonPrismaticChannelNotSupported = 20144
	SwmmElevationVolumeCurveWarning = 20145
	SwmmElevationVolumeNoZeroPoint = 20146
	SwmmElevationAreaCurveVoidSpace = 20147
	SwmmPumpHasTooManyBindingLinks = 20148
	SwmmTopWidthOverlandFlowCannotBeNegative = 20149
	SwmmShapeCompatibility = 20150
	SwmmConduitPolygon = 20151
	SwmmNodeCoordinates = 20152
	SwmmOldSwmmFile = 20153
	SwmmDWFMonthAndDailyPatterns = 20154
	SwmmHourlyPatternImport = 20156
	SwmmNoElementsFoundToImport = 20157
	SwmmPumpControlsAssumed = 20158
	SwmmWeekendPatternIgnored = 20159
	SwmmGageIntervalLargerThanTimeSeriesInterval = 20160
	SwmmGageIntervalDoesNotDivideTimeSeriesInterval = 20161
	SwmmDuplicateStationFound = 20162
	SwmmDoesNotSupportAirValves = 20163
	SwmmLIDAreaExceedsSubcatchmentArea = 20164
	SwmmInletCalculationFailed = 20165
	SwmmSurfaceStorageNotDefinedForInlet = 20166
	SwmmGenericLessThanCompare = 20167
	SwmmDitchInletMustHaveTrapezoidal = 20168
	SwmmUnassociatedLIDElement = 20169
	SwmmCollectionHasTooFewPoints = 20170
	SwmmPumpUpstreamLinkVirtual = 20171
	SwmmInvalidPercentValue = 20172
	SwmmLIDImperviousExceeds100Percent = 20173
	SwmmDoesNotSupportVSBPs = 20174
	SwmmInvalidHortonAttributes = 20175
	SwmmDoesNotIrregularInterceptGutters = 20176
	SwmmStormDataBeforeCalculationStartIgnored = 20177
	SwmmKuttersNotSupporter = 20178
	SwmmCollectionFieldMustBeIncreasing = 20179
	SwmmCollectionFieldMustBeDecreasing = 20180
	SwmmRDIIIgnoredOnPressureJunction = 20181
	SwmmPotentialPressureJunctionStayedManhole = 20182
	SwmmGenericCollectionValidations = 20183
	SwmmPollutantsNotSpecifiedForLandUse = 20184
	SwmmSurfaceStorageTypeNotSupported = 20185
	SwmmMultipleLinksFromANode = 20186
	SwmmEngineCalcFailed = 20187
	SwmmCollectionFieldCannotBeNegative = 20188
	SwmmCollecionFieldMustBeGreaterThanZero = 20189
	SwmmCollectionFieldMustBeLessThanOtherCollectionField = 20190
	SwmmInvalidStopNodeTypeForGutter = 20191
	SwmmInvalidStartNodeTypeForGutter = 20192
	SwmmOutfallHasTooManyInflowLinks = 20193
	SwmmDoesNotSupportVoidSpace = 20194
	SwmmPressurePipeNumberOfBarrelsNotSuipported = 20195
	SwmmPressureControlsIgnored = 20196
	SwmmAdverseSlopesNotSupport = 20197
	SwmmNegativeOffsetHappens = 20198
	SwmmEvaporationTimeSeries = 20199
	CSDManholeCatchbasinInvalidSize = 20200
	CSDManholeCatchbasinInvalidInvert = 20201
	CSDManholeCatchbasinNoDepthAreaCurve = 20202
	CSDManholeCatchbasinWrongDepthOrder = 20203
	CSDManholeCatchbasinDepthInCurveLessThanZero = 20204
	CSDManholeCatchbasinAreaInCurveLessThanZero = 20205
	CSDInletCapacityLessThanZero = 20206
	CSDInletRatingCurveInflowWrongOrder = 20207
	CSDInletRatingCurveInflowLessThanZero = 20208
	CSDInletRatingCurveCapturedFlowLessThanZero = 20209
	CSDInletRatingCurveInflowLessThanCapturedFlow = 20210
	CSDInletNoInletRatingCurve = 20211
	CSDInflowHydrographPointsLessThanTwo = 20212
	CSDInflowWrongTimeOrder = 20213
	CSDInflowHydrographFlowLessThanZero = 20214
	CSDInflowFixedFlowLessThanZero = 20215
	CSDWetWellWrongDepthOrder = 20217
	CSDWetWellDepthLessThanZero = 20218
	CSDWetWellAreaLessThanZero = 20219
	CSDWetWellConstantAreaLessThanZero = 20220
	CSDWetWellMaxDepthEqualOrLessThanZero = 20221
	CSDStorageStartWSElevLowerThanStorageBottom = 20222
	CSDStorageStartWSElevHigherThanStorageTop = 20223
	CSDWetWellNoDepthAreaCurve = 20224
	CSDNoChannelConnectedToCrossSectionNode = 20225
	CSDGenericChannelStationWrongOrder = 20226
	CSDManningNDepthTypeNoNDepthCurve = 20227
	CSDManningNFlowTypeNoNFlowCurve = 20228
	CSDManningNFlowTypeWrongFlowOrder = 20229
	CSDManningNDepthTypeWrongDepthOrder = 20230
	CSDManningEqualOrLessThanZero = 20231
	CSDManningTooLarge = 20232
	CSDLinkLengthEqualOrLessThanZero = 20233
	CSDFirstManningInHorizontalSegmentZero = 20234
	CSDManningInHorizontalSegmentLessThanZero = 20235
	CSDCrossSectionTrapezoidalDataLessThanZero = 20236
	CSDCrossSectionTrapezoidalDataEqualToOrLessThanZero = 20237
	CSDCrossSectionTrapezoidalAreaZero = 20238
	CSDCrossSectionGenericNoStationElevInput = 20239
	CSDManningTrapezoidalShapeHasHorizontalSegmentManning = 20240
	CSDLinkUpstreamNodeInactive = 20241
	CSDLinkDownstreamNodeInactive = 20242
	CSDCatchbasinHasMoreThanOneGutterComeOut = 20243
	CSDOutfallBoundaryElementTypeNoReferencedElement = 20244
	CSDOutfallElevFlowWrongElevOrder = 20245
	CSDOutfallNoElevFlowCurve = 20246
	CSDOutfallNoTidalCurve = 20247
	CSDOutfallTidalTypeWrongTimeOrder = 20248
	CSDBoundaryElementOfOutfallInactive = 20249
	CSDPondElevationAreaPercentVoidSpaceLargerThan100 = 20250
	CSDPondElevationVolumePercentVoidSpaceLargerThan100 = 20251
	CSDPondElevationAreaPercentVoidSpaceEqualToOrLessThanZero = 20252
	CSDPondElevationVolumePercentVoidSpaceEqualToOrLessThanZero = 20253
	CSDPondWrongElevationOrder = 20254
	CSDPondAreaLessThanZero = 20255
	CSDPondVolumeLessThanZero = 20256
	CSDPondVolumeWrongOrder = 20257
	CSDStorageVolumeFunctionCoefficientZero = 20258
	CSDStorageVolumeFunctionExponentLessThanZero = 20259
	CSDPondNoElevationAreaCurve = 20260
	CSDPondNoElevationVolumeCurve = 20261
	CSDPondPipeVolumeDiameterLessThanZero = 20262
	CSDPondPipeVolumePipeLengthLessThanZero = 20263
	CSDPondPipeVolumeNoBarrel = 20264
	CSDConduitNoPipeCatalogReference = 20265
	CSDCatalogPipeSpanZero = 20266
	CSDLocalPipeDiameterZero = 20267
	CSDLocalPipeSpanZero = 20268
	CSDLocalPipeRiseZero = 20269
	CSDCatalogPipeDiameterZero = 20270
	CSDLinkInvertLowerThanNodeInvert = 20271
	CSDLinkInvertHigherThanNodeRim = 20272
	CSDLinkInvertHigherThanAdjacentPondTopElev = 20273
	CSDConduitClosedConduitTypeHasSegmentManning = 20274
	CSDConduitEntranceLossLessThanZero = 20275
	CSDConduitEntranceLossLagerThanOne = 20276
	CSDConduitExitLossLessThanZero = 20277
	CSDConduitExitLossLargerThanOne = 20278
	CSDLinkUpstreamDownstreamSameNode = 20279
	CSDConduitOrChannelInvertNotSet = 20280
	CSDCatalogPipeHasHorizontalSegmentManning = 20281
	CSDLinkSlopeZero = 20282
	CSDLinkSlopeTooLarge = 20283
	CSDLinkHasAdverseSlope = 20284
	CSDLinkInvertLowerThanAdjacentPondBottomElev = 20285
	CSDOutletStructureUpstreamPondInactive = 20286
	CSDOutletStructureNoLinkConnected = 20287
	CSDOutletStructureInactiveLinkConnected = 20288
	CSDOutletStructureNodeMoreLinksConnected = 20289
	CSDCalculationTerminateTimeZero = 20290
	CSDCalculationTimeStepZero = 20291
	CSDPlottingTimeStepLessThanCalcTimeStep = 20292
	CSDComputationDistanceZero = 20293
	CSDPlottingTimeStepZero = 20294
	CSDGutterNotConnectToCorrectNodes = 20295
	CSDDisconnectedNetwork = 20296
	CSDOutletStructureUpstreamPondNotSet = 20297
	CSDConduitVirtualLinkNoControlStructure = 20298
	CSDLinkControlStructureNoItem = 20299
	CSDControlCrestLowerThanLinkInvert = 20300
	CSDVirtualControlCrestLowerThanUpInvert = 20301
	CSDControlCrestHigherThanOrEqualToTop = 20302
	CSDWeirCoefficientEqualToOrLessThanZero = 20303
	CSDWeirCoefficientZero = 20304
	CSDWeirLengthZeroOrLessThanZero = 20305
	CSDWeirNumOfContractionsLessThanZero = 20306
	CSDVNotchWeirAngleLessThanZero = 20307
	CSDWeirEndCoefficientLessThanZero = 20308
	CSDWeirSideSlopeLessThanZero = 20309
	CSDControlFuncnctionCoefficientZero = 20310
	CSDControlFuncnctionExponentZero = 20311
	CSDControlDepthDischargeTypeNoInputCurve = 20312
	CSDControlDepthDischargeCurveDepthWrongOrder = 20313
	CSDControlDepthDischargeCurveDepthLessThanZero = 20314
	CSDControlDepthDischargeCurveDischargeLessThanZero = 20315
	CSDOrificeDiameterZero = 20316
	CSDOrificeWidthZero = 20317
	CSDOrificeHeightZero = 20318
	CSDFlapGateDirectionDifferentFromMainFlowDirection = 20319
	CSDNoConduitOrChannelConnectedToOutfall = 20320
	CSDNoOutfallOrStorage = 20321
	CSDIrregularClosedSectionNoElevWidthCurve = 20322
	CSDIrregularClosedSectionWrongElevOrder = 20323
	CSDIrregularClosedSectionWidthInvalid = 20324
	CSDConduitClosedConduitTypeHasOverbankManning = 20325
	CSDLeftBankStationNotExist = 20326
	CSDRightBankStationNotExist = 20327
	CSDOverBankChannelManningEqualToOrLessThanZero = 20328
	CSDOverBankChannelManningTooLarge = 20329
	CSDTrapezoidalShapeHasOverBankChannelManning = 20330
	CSDPumpSupplyNodeShouldBeStorageType = 20331
	CSDPumpDownstreamMultipleConduits = 20332
	CSDNoPumpDownstreamConduit = 20333
	CSDPumpConnectedConduitCrossSectionOpenType = 20334
	CSDPumpSuppliedNodeNotSet = 20335
	CSDPumpSuppliedNodeNotExist = 20336
	CSDPumpSuppliedNodeInActive = 20337
	CSDNumberOfPumpsInPumpCollectionZero = 20338
	CSDPumpCurveNotSelected = 20339
	CSDPumpOffElevLowerThanSupplyNodeInvert = 20340
	CSDPumpOffElevHigherThanOrEqualToOnElev = 20341
	CSDDataInPumpCurveNotInAscendingOrder = 20342
	CSDDataInPumpCurveHasNegativeValue = 20343
	CSDDataInPumpCurveNotInDescendingOrder = 20344
	CSDPumpCurveHasLessThanTwoPoints = 20345
	CSDPumpSuppliedNodeManholeTypeHasVolumeCurve = 20346
	CSDOutletStructureDownstreamLinkBothHaveControl = 20347
	CSDIrregularChannelNoCrossSectionArea = 20348
	CSDDepthInDepthAreaCurveNotStartZero = 20349
	CSDProjectFileNameTooLong = 20350
	CSDLinkLengthTooShort = 20351
	CSDInlineControlStructureShouldBeSide = 20352
	CSDSideControlStructureShouldBeInline = 20353
	CSDPumpHasMoreThanOneSunctionLinks = 20354
	CSDPumpWithSunctionPipeHasMoreThanOnePumps = 20355
	CSDPumpWithSunctionPipeHasWrongPumpType = 20356
	CSDRectRoundChannelRadiusZero = 20357
	CSDRectTrianChannelTrianleHeightZero = 20358
	CSDPowerConduitExponentLessThanOne = 20359
	CSDPumpMoreThanTwoLinksConnected = 20360
	CSDPumpDownstreamLinkInactive = 20361
	CSDPumpNoSuctionLinkNoSuctionElement = 20362
	CSDPumpSuctionNodeWrongType = 20363
	CSDPumpWrongSuctionElement = 20364
	CSDPumpWrongSuctionElementType = 20365
	CSDPumpNoLinkConnected = 20366
	CSDPumpSuctionDischargeSameNode = 20367
	CSDNonBoltManholeRimLowerThanDownInvert = 20368
	CSDCatchbasinRimLowerThanDownInvert = 20369
	CSDWarmUpTimeLessThanZero = 20370
	CSDAbsoluteHeadLossLessThanZero = 20371
	CSDAbsoluteHeadLossTooLarge = 20372
	CSDHeadLossCoeffLessThanZero = 20373
	CSDHeadLossCoeffTooLarge = 20374
	CSDKinematicViscosityZero = 20375
	CSDChannelNotConnectToCrossSectionNode = 20376
	ScenarioWithInvalidCalculationOption = 20377
	CSDPondOutletStructureNotSameManner = 20378
	CSDPondBottomVolumeTooSmall = 20379
	CSDPondInfiltrationConstantFlowNegative = 20380
	CSDPondInfiltrationAverageInfiltrationNegative = 20381
	CSDPondInfiltrationConstantFlowZero = 20382
	CSDPondInfiltrationAverageInfiltrationZero = 20383
	CSDImplicitEngineOnlySupportRiseSpanArch = 20384
	CSDConduitDownstreamRiseSmalerThanUpstream = 20385
	CSDMustHaveZeroFlowPointInPumpHeadFlowCurve = 20386
	CSDCrossSectionNodeBetweenTwoConduitsInBranch = 20387
	CSDVirtualFlowDepthLessThanZero = 20388
	CSDVirtualFlowDepthZero = 20389
	CSDVirtualFlowDepthTooLarge = 20390
	CSDLinkLengthTooLarge = 20391
	CSDPumpConnectedToOutletStructureWithControls = 20392
	CSDLinkInvertLowerThanOutfallBoundaryElementInvert = 20393
	CSDLPISmallerThanZero = 20394
	CSDLPISmallerThanOne = 20395
	CSDCulvertConnectedToOutfall = 20396
	CSDPressurePipeHasSplitFlow = 20397
	CSDDataNotSet = 20398
	CSDPumpUpstreamConduitShapeNotVirtual = 20399
	CSDPumpUpstreamPressurePipeNotVirtual = 20400
	CSDMoreThanOneControlsInLinkControlStructure = 20401
	CSDExplicitEngineOnlySupportDiversionLink = 20402
	CSDOutletStructureDownstreamLinkIsVirtual = 20403
	CSDRTKUnitHydrographIgnored = 20404
	CSDConduitUnderPressureDuringSimulation = 20405
	CSDNoCatalogInletsSupported = 20406
	CSDNoCatalogInletReference = 20407
	CSDCatalogInletStructureLengthInvalid = 20408
	CSDCatalogInletStructureWidthInvalid = 20409
	CSDOnGradeLongitudinalSlopeInvalid = 20410
	CSDOnGradeManningsNInvalid = 20411
	CSDRoadCrossSlopeInvalid = 20412
	CSDGutterCrossSlopeInvalid = 20413
	CSDGutterComparedToRoadCrossSlopeInvalid = 20414
	CSDGutterWidthInvalid = 20415
	CSDCatalogInletSlotWidthInvalid = 20416
	CSDLocalSlotLengthInvalid = 20417
	CSDLocalDitchBottomWidthInvalid = 20418
	CSDLocalDitchSideSlopeInvalid = 20419
	CSDCatalogInletGrateWidthInvalid = 20420
	CSDLocalGrateLengthInvalid = 20421
	CSDCatalogInletDepressionWidthInvalid = 20422
	CSDCatalogInletLocalDepressionInvalid = 20423
	CSDCatalogInletCurbOpeningHeightInvalid = 20424
	CSDCatalogInletThroatAngleInvalid = 20425
	CSDLocalCurbOpeningLengthInvalid = 20426
	CSDLocalGrateCloggingInvalid = 20427
	CSDFirstStorageAreaLargerThanOneAcre = 20428
	CSDInletDepthCaptureCurveDepthWrongOrder = 20429
	CSDInletDepthCaptureCurveDepthLessThanZero = 20430
	CSDInletDepthCaptureCurveCapturedFlowLessThanZero = 20431
	CSDInletDepthCaptureCurveMustBeSag = 20432
	CSDWetWellNoCrossSectionCurve = 20433
	CSDWetWellWrongDepthRatioOrder = 20434
	CSDWetWellWrongVolumeRatioOrder = 20435
	CSDWetWellDepthRatioLessThanZero = 20436
	CSDWetWellVolumeRatioLessThanZero = 20437
	CSDWetWellTopNotHigherThanBottom = 20438
	CSDWetWellVolumeZero = 20439
	CSDCatalogPipeRiseZero = 20440
	CSDLeftBankStationLargerThanRightBank = 20441
	CSDInletInflowCaptureCurveFlowToInletWrongOrder = 20442
	CSDInletInflowCaptureCurveCapturedFlowLessThanZero = 20443
	CSDInletInflowCaptureCurveFlowToInletLessThanZero = 20444
	CSDCatalogInletOutOfRangeDuringSimulation = 20445
	CSDConstantStorageAreaLargerThanOneAcre = 20446
	CSDLinkInvertHigherThanOutfall = 20447
	CreateNoControlNearOutfallAllowed = 20448
	CSDGutterLinkMaxDepthInvalid = 20449
	CSDGutterParabolicHeightInvalid = 20450
	CSDGutterParabolicWidthInvalid = 20451
	CSDCurbCrossSlopeInvalid = 20452
	CSDInletPercentCaptureLessThanZero = 20453
	CSDInletPercentCaptureGreaterThan100Percent = 20454
	CSDGutterLinkLongitudinalSlopeInvalid = 20455
	CSDLeftSideSlopeInvalid = 20456
	CSDRightSideSlopeInvalid = 20457
	CSDBottomWidthInvalid = 20458
	CSDLocalDitchBottomWidthTooSmallInvalid = 20459
	CSDIrregularNotAsInterceptGutter = 20460
	CSDDWAdditionalCarryoverNotSupported = 20461
	CSDDWKnownFlowNotSupported = 20462
	CSDDWAdditionalSubsurfaceNotSupported = 20463
	CSDCrownBoundaryTypeNotSupported = 20464
	CurbCrossSlopeComparedToRoadCrossSlopeInvalid = 20465
	ParabolicGutterHeightComparedToWidthInvalid = 20466
	SwmmNoAirValve = 20467
	CSDRoadwayWeirNotSupported = 20468
	CSDConduitHasTransitionAtEachEnd = 20469
	TempConduitCrossSectionNotSupported = 20900
	TempPumpIsNotSupported = 20901
	TempOverbankChannelManningIsNotSupported = 20902
	CSDCatalogPipeNoExist = 20903
	DmwDuhCount = 21065
	DmwShapeFactor = 21066
	DWEngineIsFlooded = 22000
	DWEngineIsFloodedTimeStepSummary = 22001
	DWEngineIsFloodedRunSummary = 22002
	DWEngineIsDry = 22003
	DWEngineIsDryTimeStepSummary = 22004
	DWEngineIsDryRunSummary = 22005
	DWEngineIsNotConverging = 22006
	DWEngineIsNotConvergingTimeStepSummary = 22007
	DWEngineIsNotConvergingRunSummary = 22008
	DWEngineIsOverflowing = 22009
	DWEngineIsOverflowingTimeStepSummary = 22010
	DWEngineIsOverflowingRunSummary = 22011
	DWEngineIsPossibleHydraulicJump = 22012
	DWEngineIsPossibleHydraulicJumpTimeStepSummary = 22013
	DWEngineIsPossibleHydraulicJumpRunSummary = 22014
	DWEngineIsSuperCritical = 22015
	DWEngineIsSuperCriticalTimeStepSummary = 22016
	DWEngineIsSuperCriticalRunSummary = 22017
	DWEngineIsSurcharged = 22018
	DWEngineIsSurchargedTimeStepSummary = 22019
	DWEngineIsSurchargedRunSummary = 22020
	RTKSetIDNotSelected = 22021
	RTKRapidRZero = 22022
	RTKRapidTZero = 22023
	RTKRapidKZero = 22024
	RTKModerateRZero = 22025
	RTKModerateTZero = 22026
	RTKModerateKZero = 22027
	RTKSlowRZero = 22028
	RTKSlowTZero = 22029
	RTKSlowKZero = 22030
	RTKRSumGTOne = 22031
	RTKRapidGTMod = 22032
	RTKModGTSlow = 22033
	RTKRGTZeroNotTK = 22034
	RTKTSmallValue = 22035
	RTKSetIDDeleted = 22036
	DWEngineNotSupportAirValves = 22037
	TimeAreaNotMatch = 22038
	RainDataNotSupported = 22039
	TimeAreaNoUserDefinedTimeAreaData = 22040
	TotalAreaExceedsTimeAreaCombinedArea = 22041
	TimeAreaCombinedAreaExceedsTotalArea = 22042
	TimeArea_OutputIncrementExceedsTc = 22043
	TimeAreaSupplementalAreasIgnored = 22044
	TimeAreaPerviousSubareaRunoffCoefficientInvalid = 22045
	TimeAreaImperviousSubareaRunoffCoefficientInvalid = 22046
	TimeAreaLIDSendOutflowToPervious = 22047
	ReferencedCatchmentMustUseEpaSwmmRunoff = 22048
	SwmmTopWidthOverlandFlowMustBeGreaterThanZero = 28150
	DelReserved30000 = 30000
	DelReserved30001 = 30001
	DelReserved30002 = 30002
	SWGJunctionChamberBottomHigherThanTop = 30100
	SWGJunctionChamberTopHigherThanGround = 30101
	SWGCalcOptionPatternSetupNotSelected = 30102
	SWGUnitLoadPatternNotSelected = 30103
	SWGUnitLoadZero = 30104
	SWGPatternBaseInflowZero = 30105
	SWGPatternBaseInflowNegative = 30106
	SWGPatternInflowPatternNotSet = 30107
	SWGSanitaryKnownFlowNegative = 30108
	SWGSanitaryUnitLoadCountNegative = 30109
	SWGSanitaryUnitLoadCountZero = 30110
	SWGSanitaryUnitLoadNotSet = 30111
	SWGSanitaryPatternNotSet = 30112
	SWGSanitaryPatternBaseFlowZero = 30113
	SWGSanitaryPatternBaseFlowNegative = 30114
	SWGInfiltrationRateZero = 30115
	SWGInfiltrationRateLessThanZero = 30116
	SWGInfiltrationUnitCountZero = 30117
	SWGInfiltrationUnitCountLessThanZero = 30118
	SWGInfilAdditionalFlowLessThanZero = 30119
	SWGInfiltrationPatternBaseFlowNegative = 30120
	SWGInfiltrationPatternBaseFlowZero = 30121
	SWGPressurePipeMinorLossNegative = 30122
	SWGPressurePipeMinorLossTooLarge = 30123
	SWGPatternStartTimeLessThanZero = 30124
	SWGPatternStartMultiplierLessThanZero = 30125
	SWGPatternNoInputInPattrnTable = 30126
	SWGPatternTimeFromStartZero = 30127
	SWGPatternTimeFromStartNotIncreasing = 30128
	SWGPatternMultiplierNegative = 30129
	SWGPatternStartLastMultiplierDifferent = 30130
	SWGInfiltrationLoadingUnitNotSpecified = 30131
	SewerCADManningsImport = 30132
	SewerCADDiversionIgnored = 30133
	SewerCADFMainSettingIgnored = 30134
	SewerCADPumpControlsIgnored = 30135
	SWGPressurePipeRoughnessZero = 30136
	SWGPressurePipeDarcyWeisRoughHeightZero = 30137
	SWGPressurePipeRoughnessNotInRange = 30138
	SWGPressurePipeDarcyWeisRoughHeightNotInRange = 30139
	SWGWetwellDepthRatioVolumeRatioCurveInalid = 30140
	SWGWetwellDepthOrVolumeRatioNotInAscendingOrder = 30141
	SWGWetwellDepthOrVolumeRatioNotPositive = 30142
	SWGPumpDefinitionChangedToHeadFlowCurve = 30143
	SWGSewerCADControlsNotAllImported = 30144
	SWGConduitFrictionMethodChangedToMannings = 30145
	SWGPressurePipeFrictionMethodChangedToMannings = 30146
	SWGDesignConstraintsNotImported = 30147
	SWGPatternDailyMonthlyFactorsNotImported = 30148
	SWGExtremeFlowSetupNotImported = 30149
	SWGConduitAdditionalInfiltrationNotImported = 30150
	SWGManholeKnownFlowNotImported = 30151
	SWGManholeAASHTOHeadlossChangedToAbsolute = 30152
	SWGManholeHeadlossCurveChangedToAbsolute = 30153
	SWGBoundaryCrownTypeConvertedToUserDefined = 30154
	SWGDiversionRatingCurveIgnored = 30155
	SWGNoReportResultsForCatchmentsNodesAndLinks = 30156
	SWGNoElementsInReportSelectionSet = 30157
	SWGReportSelectionSetNotSelected = 30158
	SWGReportEmptySelectionSet = 30159
	SWGVariableSpeedPumpConvertedToStandardPump = 30160
	SWGAirValveConvertedToPressureJunction = 30161
	SWGHourlyPatternNotMatchSWMMHourlyPattern = 30162
	SWGSnowMoveToCatchmentNoExist = 30163
	SWGStepWisePatternUsedAsContinuousPatternInSWMM = 30164
	SWGPumpOnElevationNotInNodeTopBottomRange = 30165
	SWGPumpOffElevationNotInNodeTopBottomRange = 30166
	SWGVirtualPressurePipeNotConnectedToPump = 30167
	SWGPatternFormatIgnoredInSWMM = 30168
	SWGDiversionUpstreamNonManhole = 30169
	SWGInfiltrationRateEqualToZero = 30170
	SWGSWMMNOdeOnlySupportOneSanitaryPattern = 30171
	SWGElementSanitaryPatternIDNotSet = 30172
	SWGPlottingStepBeMultiplierOfCalculationStep = 30173
	TrapezoidalGutterRequiresDitchorGrateInlet = 30174
	SWGOutfallLinkConnectedNotPhysical = 30175
	SWGDWEngineCalculationCancelled = 30176
	DitchInletWidthExceedsTrapGutterWidth = 30177
	GrateInletWidthExceedsConvGutterWidth = 30178
	SWMMLandUseTotalCatchmentAreaPercentGreaterThan100 = 30179
	SWGContinuityNA = 30180
	SWGLinkBetweenOutfallsNotSupported = 30181
	SWGDWEngineNotSupportDailyMonthlyPattern = 30182
	SWGNoActiveTerrainModelUsedInDesign = 30183
	SWGTerrainModelUsedInDesign = 30184
	SWGTerrainModelSettingInvalid = 30185
	SWGLateralStartStopNodesMoreConnection = 30186
	SWGLateralConnectedToPressureElements = 30187
	SWGTapNodeReferencePressureElements = 30188
	SWGTapNodeNoReferenceLink = 30189
	SWGIsolatedTapNode = 30190
	SWGPressurePipeConnectedToBoundaryTypeOutfall = 30191
	SWGDiversionConnectedToOutletStructure = 30192
	SWGLateralConnectedToPondOutlet = 30193
	SWGLateralConnectedToOutlet = 30194
	SWGTapNodeReferenceDiversionLink = 30195
	SWGTapNodeConnectionElevationBelowPipeInvert = 30196
	SWGHydrographNotCoverWholeSimulation = 30197
	SWGHydrographNotCoverWholeSimulationForDifferentType = 30198
	SWGTapNodeReferenceCulvertLink = 30199
	SWGPropertyConnNodeSanLoadsIgnored = 30200
	GravityDiversionsNotHandled = 30201
	CatchbasinNotWithinTerrainModel = 30202
	CannotFindCatchmentForCatchbasin = 30203
	CatchmentHasMoreThanOneCatchment = 30204
	SWGDWEnginePondInfiltrationNotSupportedWithoutOutletStructure = 30205
	DownstreamInletNotInDownstreamPath = 30206
	InletNotInTerrainModel = 30207
	WrongGutterDirection = 30208
	NoGutterBetweenTwoInlets = 30209
	NodeMaxCoverSmallerThanMinCover = 30210
	MismatchUpstreamNodeMaxCover = 30211
	MismatchDownstreamNodeMaxCover = 30212
	ConduitCannotConnectToTapNode = 30213
	SWGGVFEngineNotSupportElementType = 35000
	SWGVSPBElementNotSupportedInDWEngine = 35001
	SWGElementFieldNotSupportedInEngineType = 35002
	SWGElementSelectedForFieldNoLongerExists = 35003
	SWGLateralLinkToPOSNodeIsInvalid = 35099
	SWGRoughnessValueMustBeGreaterOrEqualsAndLessOrEquals = 36000
	SWGRoughnessBankHorizontalSupportedByIrregular = 36001
	SWGRoughnessTypeNotSupportBySolver = 36002
	SWGRoughnessValueMustBeGreater = 36003
	SWGBankChannelStationsIsNotDefined = 36004
	SWGBankChannelStationsAreNotProperlyDefined = 36005
	SWGKnownAndAdditionalFlowIgnored = 36006
	SectionInvalidArchData = 36020
	OutletStructureElevationHigherThanLink = 36021
	SWGPondOutletStructureHasMoreThanOneLink = 36022
	SWGGratingWidthIsInvalid = 36023
	SWGGratingLengthIsInvalid = 36024
	SWGGratingMaintenanceFactorIsInvalid = 36025
	SWGKerbOpeningLengthIsInvalid = 36026
	SWGKerbAngleAlphaIsInvalid = 36027
	SWGKerbAngleBetaIsInvalid = 36028
	SWGKerbSumAngleAlphaAndBetaTooLarge = 36029
	SWGPondSeepageMethodNotSupported = 36030
	SWGPropertyConnectionNodeConnectedToMoreThanOneLink = 36031
	SWGRectRoundRadiusInvalidRelToRiseSpan = 36032
	SWGSanitaryLoadsHiddenInCivilStorm = 36100
	SWGGvfRationalDoesNotSupportTractiveStress = 36101
	SWGRectTriangleHeightMustBeLessThanRise = 36102
	SWGCrossSectionInputCreatorNaturalChannelNotConnectedToChannelCrossSectionNode = 36103
	SWGCrossSectionInputCreatorBaseChannelElementNotConnectedToHasCrossSectionNode = 36104
	SWGModBasketHandleRiseIsLessThanHalfTheSpan = 36105
	SWGGutterHasNoDefinedSections = 36106
	SWGNoChoiceSelectedForEnumeratedField = 36107
	SWGGutterDerivedFromStopNodeButIsNotACatchBasin = 36108
	SWGGutterSlopeShouldBeGreaterThanZero = 36109
	SWGSwmmMonthlyAdjustmentsNotSupported = 36110
	SWGForecastFailed = 36111
	SWGOverrideControlStructureIssue = 36112
	SWGInvalidWeirOrificeOverrideParameter = 36113
	SWGInvalidOutletOverrideParameter = 36114
	SWGControlOverrideElementNoLongerExists = 36115
	SWGOverrideElementIsInactive = 36116
	SWGOverrideConduitNotAConduit = 36117
	SWGForecastOIDCNotSignIn = 36118
	IdahoSystemUnbalanced = 40000
	IdahoMaxTrialsExceeded = 40001
	IdahoNodeDisconnected = 40002
	IdahoPumpExceedsOperatingPoint = 40003
	IdahoNegativePressure = 40004
	IdahoUnbalanced = 40005
	IdahoUnstable = 40006
	IdahoDisconnected = 40007
	IdahoPumpCannotDeliverFlowOrHead = 40008
	IdahoValveCannotDeliverFlow = 40009
	IdahoIllConditioned = 40010
	IdahoUnableToComputeOmegaForVSPump = 40011
	IdahoUnsupportedStartAndEndNodeConfiguration = 40012
	IdahoValveCannotSupplyPressure = 40013
	IdahoCalcSummaryTrialRelativeFlowChange = 40014
	IdahoDisconnecting = 40015
	IdahoTankEmpty = 40016
	IdahoInconsistentPumpBatteryResults = 40017
	IdahoDemandDisconnected = 40018
	IdahoPumpFixedFlowTargetIsTooLow = 40019
	IdahoTankLowLevelAlarm = 40020
	IdahoTankHighLevelAlarm = 40021
	IdahoTankFull = 40022
	IdahoValveHeadLossSmallerThanWhenFullyOpen = 40023
	IdahoControlActionExecutedOnValveWithPattern = 40024
	IdahoReverseFlow = 40025
	IdahoPumpCannotDeliverHead = 40026
	IdahoPumpFailsNPSHR = 40027
	IdahoTankOverflowing = 40028
	IdahoCalculationHalted = 40029
	PressureReservoirIsEmptying = 40200
	PressureReservoirIsFilling = 40201
	PressureTankIsEmptying = 40202
	PressureTankIsFilling = 40203
	PressureElementIsClosed = 40204
	PressureElementIsOpen = 40205
	PressureLinkStatusChange = 40206
	PressureLinkChangedByNodeControl = 40207
	PressureLinkChangedByTimeControl = 40208
	PressureReservoirIsClosed = 40209
	PressureTankIsClosed = 40210
	PressureElementIsActive = 40211
	PressureElementIsTemporarilyClosed = 40212
	PressureLinkChangedByRule = 40213
	PressureTankIsOverflowing = 40214
	PipeBreak_RawBreakRateEqualsIndivBreakRate = 40300
	PipeBreakGlobalHistoryLengthInvalid = 40301
	PipeBreakGroupHistoryLengthInvalid = 40302
	PipeBreakInterestRateInvalid = 40303
	PipeBreakRepresentativeScenarioDoesNotExist = 40304
	PipeBreakRepresentativeScenarioNotAssigned = 40305
	PipeBreakValidation = 40306
	PipeHistoryLengthInvalid = 40307
	PressureEngineErrorCheckModel = 41000
	PressureEngineInsufficientMemoryAvailable = 41101
	PressureEngineCannotSolveNetworkHydraulicEquations = 41110
	PressureEngineCannotSolveWaterQualityTransportEquations = 41120
	PressureEngineErrorInInputData = 41200
	PressureEngineActionCannotControlCheckValve = 41207
	PressureEngineReferenceToUndefinedNode = 41208
	PressureEngineReferenceToUndefinedLink = 41210
	PressureEngineNotEnoughNodesInNetwork = 41223
	PressureEngineNoTanksOrReservoirsInNetwork = 41224
	PressureEngineParallelVSPsDifferentPumpCurve = 41252
	PressureEngineParallelVSPsDifferentMaximumSpeed = 41253
	PressureEngineParallelVSPsDifferentTargetHeads = 41254
	PressureEngineParallelVSPsControlledByDifferentNodes = 41255
	PressureEngineParallelVSPsConnectedToDifferentNodes = 41256
	PressureEngineInvalidConditionForSimpleControl = 41257
	PressureEngineInvalidActionForSimpleControl = 41258
	PressureEngineInvalidComparisonOperatorForSimpleControl = 41259
	PressureEngineInvalidPumpCurve = 41260
	PressureEngineCannotOpenReportFile = 41303
	PressureEngineCannotOpenBinaryOutputFile = 41304
	PressureEngineCannotOpenHydraulicsFile = 41305
	PressureEngineCannotReadHydraulicsFile = 41307
	PressureEngineCannotSaveResultsToFile = 41308
	PressureEngineCannotSaveResultsToReportFile = 41309
	PressureEngineMiscellaneousNonFatalValidationWarnings = 41350
	PressureEngineIsolationValvesNotLoadedWarning = 41351
	PressureEngineControlsNotLoadedWarning = 41352
	PressureEngineNeededFireFlowWarning = 41353
	PressureEngineVariableSpeedDriveWithNoEfficiencyCurve = 41354
	PressureEngineHasSystemDisconnections = 41355
	PressureEngineSimpleControlTimeBasedConditionWarning = 41356
	PressureEngineUndefinedPDDFunction = 41400
	PressureEngineReferencePressureMustBeGreaterThanZero = 41401
	PressureEngineThresholdPressureMustBeGreaterThanZero = 41402
	PressureEnginePowerFunctionExponentMustBeGreaterThanZero = 41403
	PressureEnginePddDemandPercentMustNotBeNegative = 41404
	PressureEnginePddDemandPercentMustNotExceedHundred = 41405
	PressureEngineDifferentTargetHeadsForSameControlNode = 41500
	PressureEngineDeletedGlobalPDDFunction = 41501
	PressureEngineUndefinedGlobalPDDFunction = 41502
	PressureEngineDeletedLocalPDDFunction = 41503
	PressureEngineUndefinedLocalPDDFunction = 41504
	PressureEngineWaterQualityValueCannotBeNegative = 41505
	PressureEngineUndefinedConstituentPattern = 41506
	PressureEngineEmitterCoefficientCannotBeNegative = 41507
	PressureEngineUndefinedHGLPattern = 41508
	PressureEngineMinimumElevationMustBeGreaterThanOrEqualToBaseElevation = 41509
	PressureEngineInvalidTankOperatingRange = 41510
	PressureEngineTankDiameterMustBeGreaterThanZero = 41511
	PressureEngineTankAreaMustBeGreaterThanZero = 41512
	PressureEngineNotEnoughPointsInTankCrossSectionCurve = 41513
	PressureEngineActiveVolumeMustBeGreaterThanZero = 41514
	PressureEnginePipeDiameterMustBeGreaterThanZero = 41515
	PressureEngineDeletedPumpDefinition = 41516
	PressureEngineUndefinedPumpDefinition = 41517
	PressureEngineDeletedOrInactiveControlNode = 41518
	PressureEngineUndefinedControlNode = 41519
	PressureEnginePumpPowerMustBeGreaterThanZero = 41520
	PressureEngineInitialRelativeSpeedCannotBeNegative = 41521
	PressureEngineUndefinedPumpSpeedPattern = 41522
	PressureEngineMaximumRelativeSpeedFactorMustBeGreaterThanZero = 41523
	PressureEngineValveDiameterMustBeGreaterThanZero = 41524
	PressureEngineDeletedGPVCurve = 41525
	PressureEngineUndefinedGPVCurve = 41526
	PressureEngineNotEnoughPointsInGPVCurve = 41527
	PressureEngineDeletedOrInactiveDownstreamPipe = 41528
	PressureEngineUndefinedDownstreamPipe = 41529
	PressureEngineControlNodeCannotHaveDemands = 41530
	PressureEngineUndefinedDemandPattern = 41531
	PressureEnginePipeReferencesUndefinedNode = 41532
	PressureEngineDirectedNodeReferencesUndefinedNode = 41533
	PressureEngineDeletedControlCondition = 41534
	PressureEngineUndefinedControlCondition = 41535
	PressureEngineDeletedControlAction = 41536
	PressureEngineUndefinedControlAction = 41537
	PressureEngineDeletedControlThenAction = 41538
	PressureEngineUndefinedControlThenAction = 41539
	PressureEngineDeletedControlElseAction = 41540
	PressureEngineUndefinedControlElseAction = 41541
	PressureEngineDeletedOrInactiveConditionElement = 41542
	PressureEngineInvalidClockTime = 41543
	PressureEngineInvalidTimeFromStart = 41544
	PressureEngineDeletedOrInactiveActionElement = 41545
	PressureEngineUndefinedActionElement = 41546
	PressureEnginePumpSpeedFactorCannotBeNegative = 41547
	PressureEngineAgeToleranceCannotBeNegative = 41548
	PressureEngineConstituentToleranceCannotBeNegative = 41549
	PressureEngineTraceToleranceCannotBeNegative = 41550
	PressureEngineLiquidKinematicViscosityMustBeGreaterThanZero = 41551
	PressureEngineSpecificGravityMustBeGreaterThanZero = 41552
	PressureEngineDeletedOrInactiveTraceNode = 41553
	PressureEngineUndefinedTraceNode = 41554
	PressureEngineDeletedConstituent = 41555
	PressureEngineUndefinedConstituent = 41556
	PressureEngineDiffusivityCannotBeNegative = 41557
	PressureEnginePipeLengthMustBeGreaterThanZero = 41558
	PressureEnginePipeRoughnessCannotBeNegative = 41559
	PressureEnginePipeMinorLossCannotBeNegative = 41560
	PressureEngineValveMinorLossCannotBeNegative = 41561
	PressureEngineDeletedPDDSelectionSet = 41562
	PressureEngineNotEnoughPointsInPDDFunctionCurve = 41563
	PressureEngineSimpleControlCannotReferenceCompositeCondition = 41564
	PressureEngineSimpleControlCannotReferenceCompositeAction = 41565
	PressureEngineNotEnoughPointsInPattern = 41566
	PressureEngineDesignDischargeMustBeGreaterThanZero = 41567
	PressureEngineDesignHeadMustBeGreaterThanZero = 41568
	PressureEngineDesignDischargeMaxOperatingDischargeRuleViolated = 41569
	PressureEngineDesignHeadMaxOperatingHeadRuleViolated = 41570
	PressureEngineNotEnoughPointsInMultiplePointPumpCurve = 41571
	PressureEngineInconsistentMutliplePointPumpCurve = 41572
	PressureEngineDirectedNodeHasInvalidDownstreamLink = 41573
	PressureEngineOrphanedNode = 41574
	PressureEngineInvalidTankCompartmentSizes = 41575
	PressureEnginePatternCannotHaveDuplicateTimes = 41576
	PressureEngineThresholdPressureMustBeGreaterThanReferencePressure = 41577
	PressureEngineDeletedFireFlowSelectionSet = 41578
	PressureEngineNeededFireFlowMustBeGreaterThanZero = 41579
	PressureEngineFireFlowUpperLimitMustBeGreaterThanZero = 41580
	PressureEngineFireFlowUpperLimitMustBeGreaterThanNeededFireFlow = 41581
	PressureEngineDeletedIsolationValveReferencePipe = 41582
	PressureEngineUndefinedIsolationValveReferencePipe = 41583
	PressureEngineIsolationValveReferencesUndefinedLink = 41584
	PressureEngineMaximumLagPumpsExceeded = 41585
	PressureEngineFireFlowNoFireFlowNodesSelectedForRun = 41586
	PressureEnginePDDFunctionContainsDuplicatePoints = 41587
	PressureEnginePDDFunctionContainsNonIncreasingValues = 41588
	PressureEnginePDDFunctionContainsNegativeValues = 41589
	PressureEngineVSPCannotHaveConstantPowerCurve = 41590
	PressureEngineVSPBCannotHaveConstantPowerCurve = 41591
	PressureEngineFirstMultiplierMustMatchLastPatternMultiplier = 41592
	PressureEngineFirstTimeInPatternCannotBeZero = 41593
	PressureEnginePatternPointsOutOfOrder = 41594
	PressureEngineIsolatedNode = 41595
	PressureEngineIsolatedPipe = 41596
	PressureEngineFailedTopologicalValidation = 41597
	PressureEngineFailedToLoadModel = 41598
	PressureEngineFailedToValidateModel = 41599
	PressureEnginePipeReferencesDeletedOrInactiveNode = 41600
	PressureEngineLinkStartAndEndNodesAreTheSame = 41601
	PressureEngineFailedToRunModel = 41602
	PressureEngineMoreThan100DisconnectedElements = 41603
	PressureEngineOutOfMemory = 41604
	PressureEngineMoreThan20NegativePressures = 41605
	PressureEngineSimpleControlTimeBasedConditionValidationWarning = 41606
	PressureEngineTopologicalValidationOutOfMemory = 41607
	PressureEngineUnknownEnumerationValue = 41608
	PressureEngineConditionElementTypeMismatch = 41609
	PressureEngineFirstPointInTankCrossSectionCurveMustBeZeroZero = 41662
	PressureEngineLastPointInTankCrossSectionCurveMustBeOneOne = 41663
	PressureEngineMultiplePointPumpCurveContainsDuplicatePoints = 41669
	PressureEngineMultiplePointPumpCurveContainsNonIncreasingFlows = 41670
	PressureEngineMultiplePointPumpCurveContainsNegativeValues = 41671
	PressureEngineNegativeValueInPumpPattern = 41672
	PressureEngineCannotHaveVSPBActionsForSimpleControl = 41673
	PressureEngineGPVCurveContainsNegativeValues = 41674
	PressureEngineGPVCurveContainsDuplicatePoints = 41675
	PressureEngineGPVCurveContainsNonIncreasingValues = 41676
	PressureEngineGPVCurveContainsInfinityValues = 41677
	PressureEnginePipeCountLicensedExceeded = 41678
	PressureEngineNotValidLicenseInPlace = 41679
	PressureEngineUnsupportedAnalysisTypeForProduct = 41680
	PressureEngineHydropenumaticTankVolumeMustBeGreaterThanZero = 41681
	PressureEngineAtmosphericPressureMustBeGreaterThanZero = 41682
	PressureEngineHGLOffMustBeGreaterThanHGLOn = 41683
	PressureEngineHydraulicTimeStepMustFactorIntoDuration = 41684
	PressureEngineDurationMustBeGreaterThanOrEqualToZero = 41685
	PressureEngineHydraulicTimeStepMustBeGreaterThanZero = 41686
	PressureEngineMaximumTrialsMustBeGreaterThanZero = 41687
	PressureEngineInvalidControlNodeType = 41688
	PressureEngineHydrantLateralLengthMustBeGreaterThanZero = 41689
	PressureEngineHydrantLateralDiameterMustBeGreaterThanZero = 41690
	PressureEngineHydrantLateralMinorLossCannotBeNegative = 41691
	PressureEngineDeletedOutputSelectionSelectionSet = 41692
	PressureEngineVariableReportingTimeStepsMustIncludeAtLeastOneEntry = 41693
	PressureEngineVariableReportingTimeStepsNoResultsWouldBeStored = 41694
	PressureEngineVariableReportingTimeStepsContantStepsMustFactor = 41695
	PressureEngineVariableReportingTimeStepsFirstEntryMustStartAtHydraulicTimeZero = 41696
	PressureEngineInvalidTraceNodeType = 41697
	PressureEngineDeletedFlushingPipeSelectionSet = 41698
	PressureEngineMustDefineAtLeastOneValidTargetPipe = 41699
	PressureEngineNotEnoughPointsInTurbineCurve = 41700
	PressureEngineTurbineCurveContainsNegativeValues = 41701
	PressureEngineTurbineCurveContainsDuplicatePoints = 41702
	PressureEngineTurbineCurveContainsNonIncreasingValues = 41703
	PressureEngineTurbineCurveContainsInfinityValues = 41704
	PressureEngineMustDefineAtLeastOneFlushingEvent = 41705
	PressureEngineEveryFlushingEventMustHaveAtLeastOneValidFlushingNode = 41706
	PressureEngineHammerOrificeFlowMustBeGreaterThanZero = 41707
	PressureEngineHammerOrificePressureDropMustBeGreaterThanZero = 41708
	PressureEngineInvalidActionReference = 41709
	PressureEngineUndefinedActionReference = 41710
	PressureEngineSuctionSideVSPControlNodeMustBeTank = 41711
	PressureEngineInvalidElevation = 41712
	PressureEngineInitialLiquidVolumeMustBeGreaterThanZero = 41713
	PressureEngineEffectiveVolumeMustBeLessThanTotalVolume = 41714
	PressureEngineHGLOnMustBeGreaterThanMinimumElevation = 41715
	PressureEngineInitialLiquidVolumeMustBeLessThanTotalVolume = 41716
	PressureEngineEffectiveVolumeMustBeGreaterThanZero = 41717
	PressureEnginePeriodicHeadPatternMissingTimeZero = 41718
	PressureEnginePeriodicFlowPatternMissingTimeZero = 41719
	PressureEngineConstantAreaHydropneumaticTankControlsNotInPlace = 41720
	PressureEngineUnknownControlConditionHydroTankAttribute = 41721
	PressureEngineUnknownControlConditionSurgeTankAttribute = 41722
	PressureEngineDeletedOrInactivePipeWithWye = 41723
	PressureEngineUndefinedPipeWithWye = 41724
	PressureEngineDeletedControlSet = 41725
	PressureEngineVLADischargeCoefficientMustBeGreaterThanZero = 41727
	PressureEngineHammerTypicalFlowMustBeGreaterThanOrEqualToZero = 41728
	PressureEngineTCVDischargeCoefficientMustBeGreaterThanZero = 41729
	PressureEngineHGLOnMustBeSufficientlyAboveTankBase = 41730
	PressureEngineDeletedUnitDemand = 41731
	PressureEngineUndefinedUnitDemand = 41732
	PressureEngineNotEnoughPointsInRatingCurve = 41733
	PressureEngineRatingCurveContainsNegativeValues = 41734
	PressureEngineRatingCurveContainsDuplicatePoints = 41735
	PressureEngineRatingCurveContainsNonIncreasingValues = 41736
	PressureEngineRatingCurveContainsInfinityValues = 41737
	PressureEngineMoreThanOneVSPBCannotControlTheSameControlNode = 41738
	PressureEngineIsolationValveDiameterMustBeGreaterThanZero = 41739
	PressureEngineInvalidWetWellOperatingRange = 41740
	PressureEngineMinimumWetWellElevationMustBeGreaterThanOrEqualToBaseElevation = 41741
	PressureEngineWetWellDiameterMustBeGreaterThanZero = 41742
	PressureEngineWetWellAreaMustBeGreaterThanZero = 41743
	PressureEngineWetWellActiveVolumeMustBeGreaterThanZero = 41745
	PressureEngineNotEnoughPointsInWetWellCrossSectionCurve = 41746
	PressureEngineFirstPointInWetWellCrossSectionCurveMustBeZeroZero = 41747
	PressureEngineLastPointInWetWellCrossSectionCurveMustBeOneOne = 41748
	PressureEngineWetWellCrossSectionCurveContainsNegativeValues = 41749
	PressureEngineWetWellCrossSectionCurveContainsDuplicateValues = 41750
	PressureEngineWetWellCrossSectionCurveContainsNonIncreasingValues = 41751
	PressureEngineHighAlarmIsOutsideOperatingRange = 41752
	PressureEngineLowAlarmIsOutsideOperatingRange = 41753
	PressureEngineLowAlarmIsEqualToOrHigherThanHighAlarm = 41754
	PressureEngineCannotHaveMoreThanTwoPipesConnectedToAnAirValveThatSupportsAirRelease = 41755
	PressureEngineOutfallBoundaryElevationFlowCurveNotSupported = 41756
	PressureEngineUndefinedValveSettingPattern = 41757
	PressureEngineFirstClosureMustMatchLastPatternClosure = 41758
	PressureEngineDeletedValveCharacteristicsCurve = 41759
	PressureEngineUndefinedValveCharacteristicsCurve = 41760
	PressureEngineNotEnoughPointsInValveCharacteristicsCurve = 41761
	PressureEngineValveCharacteristicsCurveContainsIllegalValues = 41762
	PressureEngineValveCharacteristicsCurveContainsDuplicatePoints = 41763
	PressureEngineValveCharacteristicsCurveContainsNonIncreasingValues = 41764
	PressureEngineUndefinedRelativeClosurePattern = 41765
	PressureEngineValveRelativeClosurePatternValuesOutsideAllowableRange = 41766
	PressureEngineInitialRelativeClosureMismatchWarning = 41767
	PressureEngineInitialRelativeClosureMismatchValidationWarning = 41768
	PressureEngineUndefinedConditionElement = 41769
	PressureEngineLastPointInExtendedCurveMustHaveTheHighestFlow = 41770
	PressureEngineControlReferencesAnInvalidElement = 41771
	PressureEngineFullyOpenDischargeCoefficientMustBeGreaterThanZero = 41772
	PressureEngineUnsupportedPumpDefinitionType = 41773
	PressureEngineCannotModelFixedHeadAndFlowPumpsInSameSubNetwork = 41774
	PressureEngineCannotModelFixedHeadAndFlowPumpsInSameScenario = 41775
	PressureEngineThisPumpDoesNotSupportPumpPressureControlAction = 41776
	PressureEngineInvalidHydraulicAccuracyValue = 41777
	PressureEngineInvalidConditionReference = 41778
	PressureEngineUndefinedConditionReference = 41779
	PressureEngineValveCharactersticCurveMustBeFullRange = 41780
	PressureEngineAtLeastOneFireFlowNodeFailedResidualPressure = 41781
	PressureEngineSameElementControlledMoreThanOnceInSameAction = 41782
	PressureEngineEquivalentHydraulicTimeStepMustBeGreaterThanZero = 41783
	PressureEngineFlushingEventCannotIncludeVSPControlNode = 41784
	PressureEnginePumpCurveContainsNonDecreasingHeadValues = 41785
	PressureEngineCannotUsePatternsWithConstantPowerPumps = 41786
	PressureEngineVolumeRatioIsOutsideAllowableRange = 41787
	PressureEngineFirstDepthRatioMustBeLessThanOrEqualToZero = 41788
	PressureEngineLastDepthRatioMustBeGreaterThanOrEqualToOne = 41789
	PressureEngineInitialRelativeClosureMustBeBetweenZeroAndOne = 41790
	PressureEngineValvePatternIgnoredDueToInitialStatusWarning = 41791
	PressureEngineValvePatternIgnoredDueToInitialStatusValidationWarning = 41792
	PressureEngineInvalidDampingLimitValue = 41793
	PressureEngineInvalidCheckFrequencyValue = 41794
	PressureEngineInvalidMaximumCheckValue = 41795
	PressureEngineSuctionSideVSPControlNodeMustBeWetWell = 41796
	PressureEngineVSPNotSupportedByEpanet = 41797
	PressureEnginePDDNotSupportedByEpanet = 41798
	PressureEngineHydrantElementsNotSupportedByEpanet = 41799
	PressureEngineHydropneumaticTankElementsNotSupportedByEpanet = 41800
	PressureEngineAirValveElementsNotSupportedByEpanet = 41801
	PressureEnginePeriodicHeadFlowElementsNotSupportedByEpanet = 41802
	PressureEngineTurbineElementsNotSupportedByEpanet = 41803
	PressureEngineValveWithLinearAreaChangeElementsNotSupportedByEpanet = 41804
	PressureEngineOrificeBetweenPipesElementsNotSupportedByEpanet = 41805
	PressureEngineDischargeToAtmosphereElementsNotSupportedByEpanet = 41806
	PressureEngineRupureDiskElementsNotSupportedByEpanet = 41807
	PressureEngineCheckValveElementsNotSupportedByEpanet = 41808
	PressureEngineSurgeValveElementsNotSupportedByEpanet = 41809
	PressureEngineSurgeTankElementsNotSupportedByEpanet = 41810
	PressureEngineTankDemandsNotSupportedByEpanet = 41811
	PressureEnginePipeWithCheckValveCannotBeInitiallyClosed = 41812
	PressureEngineVSPBWithExtendedPumpCurveAndMoreThanZeroLagPumpsValidationWarning = 41813
	PressureEngineVSPBWithExtendedPumpCurveAndMoreThanZeroLagPumpsWarning = 41814
	PressureEngineVSPBWithMultipointPumpCurveAndOtherCriteriaThatAllAddUpToBadNews = 41815
	PressureEngineVSPBWithMultipointPumpCurveAndOtherCriteriaThatAllAddUpToBadNews_Alabama = 41816
	PressureEngineTankReferencesDeletedOrInactiveInletPipe = 41817
	PressureEngineUndefinedInletPipe = 41818
	PressureEngineTopFillingAndThrottlingInletTanksNotSupportedByEpanet = 41819
	PressureEngineTopFillTankNotEnoughPipesConnected = 41820
	PressureEngineTopFillTankSpecifiedInletPipeIsNotConnectedToTank = 41821
	PressureEngineTopFillTankInvalidInletPipeInvertLevel = 41822
	PressureEngineTopFillTankInvalidFullyClosedLevel = 41823
	PressureEngineTopFillTankInvalidStartsToCloseLevel = 41824
	PressureEngineTopFillTankIncompatibleThrottlingLevels = 41825
	PressureEngineTopFillTankCannotBeVspControlNode = 41826
	PressureEngineCannotHaveEmitterOnVSPControlNode = 41827
	PressureEngineEmitterOnVSPControlNodePostCalculationWarning = 41828
	PressureEngineReverseFlowsInSystem = 41829
	PressureEngineInvalidRoughnessAdjustmentScope = 41830
	PressureEngineInvalidDemandAdjustmentScope = 41831
	PressureEngineInvalidUnitDemandAdjustmentScope = 41832
	PressureEngineInvalidDemandAdjustmentDemandPattern = 41833
	PressureEngineInvalidUnitDemandAdjustmentUnitDemand = 41834
	PressureEngineInvalidOnOffBoundaryNode = 41835
	PressureEngineOnOffOutsideOfTankBounds = 41836
	PressureEnginePotentialConflictingControls = 41837
	PressureEngineFlushingEventWithDublicateOrderIndex = 41838
	PressureEngineFlushingEventsWithDublicateOrderIndex = 41839
	PressureEngineFlushingEventPipeRunPipeNotInAreaOfInterest = 41840
	PressureEngineFlushingEventPipeRunPipesNotInAreaOfInterest = 41841
	PressureEngineFlushingEmptyAreaOfInterest = 41842
	PressureEngineFlushingEventRunPipeClosed = 41843
	PressureEngineFlushingEventRunPipesClosed = 41844
	PressureEngineFlushingEventElementNotActive = 41845
	PressureEngineFlushingEventElementsNotActive = 41846
	PressureEngineFlushingEventPipeRunNotContinuous = 41847
	PressureEngineFlushingEventNoContinuousPipeRun = 41848
	PressureEngineFlushingEventRunPipeWithZeroVelocity = 41849
	PressureEnginePotentialConflictingControlsGlobal = 41850
	PressureEngineFlushingDeletedOrInactiveElementOfInterest = 41851
	PressureEngineFlushingUndefinedElementOfInterest = 41852
	PressureEngineOnOffElevationsAreEqual = 41853
	PressureEngineValvePatternsNotSupportedByEpanet = 41854
	PressureEngineValveCharacteristicsCurveCoefficientTypeNotSupportedByEpanet = 41855
	PressureEngineCustomerDeletedReferencedElement = 41856
	PressureEngineCustomerUndefinedReferencedElement = 41857
	PressureEngineCustomersWithoutAssociatedElement = 41858
	PressureEngineCustomerWithoutAssociatedElement = 41859
	PressureEngineCustomerReferenceDeletedDemandPattern = 41860
	PressureEngineCustomerReferenceDeletedUnitDemandPattern = 41861
	PressureEngineDeletedOrInactiveControlOverrideElement = 41862
	PressureEngineUndefinedControlOverrideElement = 41863
	PressureEngineControllOverrideDurationMustBeGreaterThanZero = 41864
	PressureEngineFireFlowNodeFailedResidualPressure = 41865
	PressureEngineAtLeastOneInitialValueSkippedDueToBadQuality = 41866
	PressureEngineParallelVSPAndVSPBNotAllowed = 41867
	PressureEngineParallelVSPBsNotAllowed = 41868
	PressureEngineParallelVSPWithMoreThanOneUpstreamPipe = 41869
	PressureEngineParallelVSPDifferentLagPipeDiameter = 41870
	PressureEngineParallelVSPDifferentLagPipeLength = 41871
	PressureEngineParallelVSPDifferentLagPipeRoughness = 41872
	PressureEngineParallelVSPDifferentLagPipeMinorLossCoefficient = 41873
	PressureEngineParallelVSPAtLeastOneLagPipeWithDifferentHydraulicAttributes = 41874
	PressureEngineFlushingStudyFlushingFlowIsMissing = 41875
	PressureEngineFlushingStudyAtLeastOneRunPipeDoesnMeetConstraint = 41876
	PressureEngineFlushingStudyAtLeastOneFlushingEventHasNoFlushingFlow = 41877
	PressureEngineDeletedOrInactiveSCADAFireFlowElement = 41878
	PressureEngineUndefinedSCADAFireFlowElement = 41879
	PressureEngineSCADAFireFlowDurationMustBeGreaterThanZero = 41880
	PressureEngineSCADAFireFlowDemandMustBeGreaterThanZero = 41881
	PressureEngineInvalidSCADADemandAdjustmentScope = 41882
	PressureEngineInvalidSCADAUnitDemandAdjustmentScope = 41883
	PressureEngineInvalidSCADADemandAdjustmentDemandPattern = 41884
	PressureEngineInvalidSCADAUnitDemandAdjustmentUnitDemand = 41885
	PressureEngineBaseFireFlowPressureBelowMinimumPressure = 41886
	PressureEngineBaseFireFlowVelocityExceedsMaximumVelocity = 41887
	PressureEngineBaseFireFlowAtLeastOneRunFailed = 41888
	PressureEngineAtLeastOneOverlappingFireFlowDemand = 41889
	PressureEnginePressuresBelowZero = 41890
	PressureEnginePressuresBelowMinPossiblePressure = 41891
	PressureEngineBaseFireFlowNodePressureBelowPressureConstraint = 41892
	PressureEngineBaseFireFlowPipeVelocityAboveVelocityConstraint = 41893
	PressureEngineDeletedOrInactivePipeBreakElement = 41894
	PressureEngineUndefinedPipeBreakElement = 41895
	PressureEngineDeletedOrInactivePipeBreakLeakageNode = 41896
	PressureEngineUndefinedPipeBreakLeakageNode = 41897
	PressureEnginePipeBreakRestorationDurationMustBeGreaterThanZero = 41898
	PressureEnginePipeBreakLeakageFlowMustBeGreaterThanZero = 41899
	PressureEnginePipeBreakLeakageStartTimeLaterThanRepairStartTime = 41900
	PressureEnginePipeBreakUndefinedIsolateElement = 41901
	PressureEnginePipeBreakDeletedOrInactiveIsolateElement = 41902
	PressureEnginePipeBreakNoValidDemandNodeFound = 41903
	PressureEnginePipeBreakAlreadyIsolated = 41904
	PressureEngineAtLeastOnePatternTimeStepSmallerThanCalculationTimeStep = 41905
	PressureEnginePatternTimeStepSmallerThanCalculationTimeStep = 41906
	PressureEnginePressuresBelowMinPossiblePressureShort = 41907
	PressureEngineFlushingBoundaryElementNotActive = 41908
	PressureEngineFlushingBoundaryElementsNotActive = 41909
	PressureEngineThisPumpDoesNotSupportPumpHeadControlAction = 41910
	PressureEngineCustomersWithInvalidAssociatedNode = 41911
	PressureEngineCustomerWithInvalidAssociatedNode = 41912
	PressureEngineLateralReferencesDeletedOrInactiveNode = 41913
	PressureEngineLateralReferencesUndefinedNode = 41914
	PressureEngineCustomersWithDifferentAssociatedElement = 41915
	PressureEngineCustomerWithDifferentAssociatedElement = 41916
	PressureEngineCustomerIsolatedByClosedIsoValve = 41917
	PressureEngineCustomersInvalidPipeDistribution = 41918
	PressureEngineCustomerInvalidPipeDistribution = 41919
	PressureEngineCustomersNoValidAssociatedNode = 41920
	PressureEngineCustomerNoValidAssociatedNode = 41921
	PressureEngineLateralsReferencesInactiveOrDeletedStopNode = 41922
	PressureEngineCustomersWithoutLateralConnection = 41923
	PressureEngineCustomerWithoutLateralConnection = 41924
	PressureEngineMissingFlushingArea = 41925
	PressureEngineCustomersWithMultipleLateralConnection = 41926
	PressureEngineCustomerWithMultipleLateralConnection = 41927
	PressureEngineCustomersAssociatedToClosedPipe = 41928
	PressureEngineCustomerAssociatedToClosedPipe = 41929
	PressureEngineDeletedOrInactivePipeShutdownElement = 41930
	PressureEngineUndefinedPipeShutdownElement = 41931
	PressureEnginePipeShutdownDurationMustBeGreaterThanZero = 41932
	PressureEnginePipeShutdownDeletedOrInactiveIsolateElement = 41933
	PressureEnginePipeShutdownUndefinedIsolateElement = 41934
	PressureEngineCustomerWithDistributionFactorOutOfRange = 41935
	PressureEngineCustomersWithDistributionFactorOutOfRange = 41936
	PressureEngineLateralsWithCustomerMeterAsStopNode = 41937
	PressureEngineLateralWithCustomerMeterAsStopNode = 41938
	PressureEnginePowerOutageDurationMustBeGreaterThanZero = 41939
	PressureEnginePowerOutageDeletedOrInactiveOutageElement = 41940
	PressureEnginePowerOutageUndefinedOutageElement = 41941
	PressureEngineInvalidTankControlCondition = 41942
	PressureEngineInvalidWetWellControlCondition = 41943
	PressureEngineNotEnoughPointsInNPSHCurve = 41944
	PressureEngineNPSHCurveContainsNegativeValues = 41945
	PressureEngineNPSHCurveContainsDuplicatePoints = 41946
	PressureEngineNPSHCurveContainsNonIncreasingValues = 41947
	PressureEngineNPSHCurveContainsInfinityValues = 41948
	PressureEngineNPSHCurveSafetyFactorMustBeGreaterThanZero = 41949
	PressureEngineUnsupportedNumericalValueInElementSetting = 41950
	PressureEngineLateralConnectedToInvalidNodeType = 41951
	PressureEnginePipeConnectedToInvalidNodeType = 41952
	PressureEngineLateralWithTapAsStartNode = 41953
	PressureEngineLateralWithJunctionAsStartNode = 41954
	PressureEngineCustomControlsLoadingErrorEncountered = 41955
	PressureEngineCustomControlsAfterHydraulicTimeStepErrorEncountered = 41956
	PressureEngineCustomControlsEvaluationErrorEncountered = 41957
	PressureEngineMSXRunDoesNotSupportOutputSelectionSet = 41958
	PressureEngineMSXRunDoesNotSupportCustomReportingTimeSteps = 41959
	PressureEnginePipeBreakDeletedOrInactiveElementToOpen = 41960
	PressureEnginePipeBreakUndefinedElementToOpen = 41961
	PressureEnginePipeShutdownDeletedOrInactiveElementToOpen = 41962
	PressureEnginePipeShutdownUndefinedElementToOpen = 41963
	PressureEngineInvalidFlowChangeLimitValue = 41964
	PressureEngineInvalidHeadLossErrorLimitValue = 41965
	PressureEngineExtraIterationsCannotBeNegative = 41966
	PressureEngineMWHFormulaNotSupportedByEpanet = 41967
	PressureEnginePDDOptionsNotSupportedByEpanet = 41968
	GenericEngineInvalidOrMissingCalculationOptions = 42000
	CulvertInletCoeffNotSelected_OnStartNode = 42001
	CulvertInletCoeffNotSelected_OnStopNode = 42002
	CulvertInletCoeffNotSelected = 42003
	CulvertInletCoefficientsSetToHeadwallButNotAHw = 42004
	CulvertEndwallCoefficientsSetToHeadwallButNotAHw = 42005
	HeadwallCannotBeBothPondInletAndPondOutletNode = 42006
	CulvertInletCoeffBarrelShapeDoesntMatch = 42007
	CulvertEndwallCoeffNotSelected = 42008
	CulvertHeadwallIsValidButConduitIsFalse = 42009
	InvalidTankLevel = 42300
	NoSupportForCustomerMetersAssociatedWithPipes = 42301
	MustHaveAtLeastOneActiveSnaphot = 42500
	MinimumRoughnessMultiplierMustBeGreaterThanZero = 42501
	MinimumRoughnessValueMustBeGreaterThanZero = 42502
	MaximumRoughnessMultiplierMustBeGreaterThanZero = 42503
	MaximumRoughnessValueMustBeGreaterThanZero = 42504
	IncrementValueMustBeGreaterThanZero = 42505
	MaximumRoughnessMultiplierMustBeGreaterThanMinimum = 42506
	MaximumRoughnessValueMustBeGreaterThanMinimum = 42507
	RoughnessMultiplierMustBeGreaterThanZero = 42508
	RoughnessValueMustBeGreaterThanZero = 42509
	RoughnessGroupInputError = 42510
	DemandGroupInputError = 42511
	LinkStatusInputError = 42512
	CalibratorEngineErrorCheckModel = 42513
	InvalidRoughnessGroupID = 42514
	InvalidDemandGroupID = 42515
	MustHaveAtLeastOneObservedValue = 42516
	InvalidCalibrationRepresentativeScenario = 42517
	DeletedCalibrationSnapshot = 42518
	UndefinedCalibrationSnapshot = 42519
	DeletedRoughnessAdjustmentGroup = 42520
	UndefinedRoughnessAdjustmentGroup = 42521
	DeletedDemandAdjustmentGroup = 42522
	UndefinedDemandAdjustmentGroup = 42523
	DeletedStatusAdjustmentPipe = 42524
	UndefinedStatusAdjustmentPipe = 42525
	DeletedRoughnessAdjustmentPipe = 42526
	UndefinedRoughnessAdjustmentPipe = 42527
	DeletedDemandAdjustmentNode = 42528
	UndefinedDemandAdjustmentNode = 42529
	DeletedObservedValueNode = 42530
	UndefinedObservedValueNode = 42531
	DeletedObservedFlowLink = 42532
	UndefinedObservedFlowLink = 42533
	DeletedObservedSettingElement = 42534
	UndefinedObservedSettingElement = 42535
	DeletedCalibrationDemandAlternative = 42536
	UndefinedCalibrationDemandAlternative = 42537
	DeletedCalibrationAdditionalDemandNode = 42538
	UndefinedCalibrationAdditionalDemandNode = 42539
	HeadPerFitnessPointMustBeGreaterThanOrEqualToZero = 42540
	FlowPerFitnessPointMustBeGreaterThanOrEqualToZero = 42541
	FitnessToleranceMustBeGreaterThanZero = 42542
	InsufficientMemoryForCalibrationAnalysis = 42543
	InsufficientMemoryForCalibrationGAOperations = 42544
	MustHaveAtleastOneAdjustmentGroup = 42545
	PipeExistsInMultipleActiveRoughnessGroups = 42546
	JunctionExistsInMultipleActiveDemandGroups = 42547
	PipeExistsInMultipleStatusAdjustmentGroups = 42548
	NumberOfLeakageNodesExceedsTheCorrespondingDemandGroup = 42549
	NumberOfLeakageNodesMustBeGreaterThanZero = 42550
	MustHaveAtleastOnePipeInEveryActiveRoughnessGroup = 42551
	MustHaveAtleastOneJunctionInEveryActiveDemandGroup = 42552
	IncorrectElementTypeInObservedFlow = 42553
	IncorrectElementTypeInObservedSetting = 42554
	TooManyStatusElements = 42555
	PipeDiameterMustBeGreaterThanOrEqualToZero = 43000
	InvalidRehabilitationFunction = 43001
	DeletedOrInactivePressureConstraintNode = 43002
	UndefinedPressureConstraintNode = 43003
	DeletedOrInactiveFlowConstraintLink = 43004
	UndefinedFlowConstraintLink = 43005
	DeletedOrInactiveBoundaryElement = 43006
	UndefinedBoundaryElement = 43007
	DeletedDesignOptionGroup = 43008
	UndefinedDesignOptionGroup = 43009
	DeletedRehabOptionGroup = 43010
	UndefinedRehabOptionGroup = 43011
	DeletedOrInactiveDesignPipeGroupPipe = 43012
	UndefinedDesignPipeGroupPipe = 43013
	DeletedOrInactiveRehabPipeGroupPipe = 43014
	UndefinedRehabPipeGroupPipe = 43015
	DeletedDiameterDiameterFunction = 43016
	UndefinedDiameterDiameterFunction = 43017
	DeletedDiameterRoughnessFunction = 43018
	UndefinedDiameterRoughnessFunction = 43019
	DeletedDiameterCostFunction = 43020
	UndefinedDiameterCostFunction = 43021
	DeletedDesignEvent = 43022
	UndefinedDesignEvent = 43023
	DeletedDesignDemandAlternative = 43024
	UndefinedDesignDemandAlternative = 43025
	DeletedDesignPipeGroup = 43026
	UndefinedDesignPipeGroup = 43027
	DeletedRehabPipeGroup = 43028
	UndefinedRehabPipeGroup = 43029
	DeletedDesignPipeConfiguration = 43030
	UndefinedDesignPipeConfiguration = 43031
	DeletedRehabAction = 43032
	UndefinedRehabAction = 43033
	DeletedDesignAdditionalDemandNode = 43034
	UndefinedDesignAdditionalDemandNode = 43035
	InvalidDesignRepresentativeScenario = 43036
	MustHaveAtLeastOneActiveDesignEvent = 43037
	MustHaveAtLeastOneActiveConstraint = 43038
	MustHaveAtLeastTwoActiveDesignOrRehabGroups = 43039
	MustHaveAtLeastOneDesignOptionInEachActiveDesignOptionTable = 43040
	MustHaveAtLeastOneRehabOptionInEachActiveRehabOptionTable = 43041
	PenaltyFactorMustBeGreaterThanOrEqualToZero = 43042
	AvailableBudgetMustBeGreaterThanZero = 43043
	DesignPipeGroupInputError = 43044
	InvalidSkipSizes = 43045
	DesignerLinkStatusInputError = 43046
	InvalidPipeGroupID = 43047
	NoPressureBenefitJunction = 43048
	ActionMissingForManualRun = 43049
	NoBudgetSpecified = 43050
	DesignerEngineErrorCheckModel = 43051
	MustHaveAtLeastOnePressureBenefitJunction = 43052
	InsufficientMemoryForDesignAnalysis = 43053
	InsufficientMemoryForDesignGAOperations = 43054
	VelocityConstraintCannotBeLessThanZero = 43055
	MaximumVelocityMustBeGreaterThanMinimumVelocityConstraint = 43056
	PressureConstraintCannotBeLessThanZero = 43057
	MaximumPressureMustBeGreaterThanMinimumPressureConstraint = 43058
	DuplicateDesignGroupPipe = 43059
	UseScenarioDiametersNoCostTableMatch = 43060
	MustHaveAtLeastOnePipeInEachActiveDesignPipeGroup = 43061
	MustHaveAtLeastOnePipeInEachActiveRehabPipeGroup = 43062
	PreRehabilitationDiameterMustBeGreaterThanZero = 43063
	PostRehabilitationDiameterMustBeGreaterThanZero = 43064
	DuplicatePreRehabilitationDiameter = 43065
	EraNumberMustBeGreaterThanZero = 43500
	EraGenerationNumberMustBeGreaterThanZero = 43501
	PopulationSizeMustBeGreaterThanZero = 43502
	CutProbabilityMustBeAValidPercentage = 43503
	SpliceProbabilityMustBeAValidPercentage = 43504
	MutationProbabilityMustBeAValidPercentage = 43505
	RandomSeedMustBeBetweenZeroandOneInclusive = 43506
	SolutionsToKeepMustBeGreaterThanZero = 43507
	MaximumTrialsMustBeGreaterThanZero = 43508
	NonImprovementGenerationsMustBeGreaterThanZero = 43509
	DemandMultiplierMustBeGreaterThanZero = 43510
	ModelMustHaveAtLeastOneDemand = 43511
	PenaltyFactorMustBeGreaterThanZero = 43512
	DarwinInvalidEngineLicense = 43513
	PressureEngineTankCrossSectionCurveContainsNegativeValues = 43664
	PressureEngineTankCrossSectionCurveContainsDuplicateValues = 43665
	PressureEngineTankCrossSectionCurveContainsNonIncreasingValues = 43666
	PressureEnginePipeMissingOneOrBothEndNodes = 43667
	PressureEngineMoreThan100PipesMissingOneOrBothEndNodes = 43668
	SchedulerInvalidEngineLicense = 43700
	SchedulerPenaltyValueMustBeAboveZero = 43701
	SchedulerUnknownSchedulerObjectiveType = 43702
	SchedulerUnknownSchedulerOptimizationAlgorithmType = 43703
	SchedulerInvalidPumpElementForDecision = 43704
	SchedulerInvalidPumpDecision = 43705
	SchedulerUndefinedPumpDecision = 43706
	SchedulerUndefinedPumpElementForDecision = 43707
	SchedulerMustHaveAtLeastOnePumpDecision = 43708
	SchedulerUnknownPumpDecisionType = 43709
	SchedulerInvalidNodeElementForPressureConstraint = 43710
	SchedulerUndefinedNodeElementForPressureConstraint = 43711
	SchedulerInvalidPipeElementForVelocityConstraint = 43712
	SchedulerUndefinedPipeElementForVelocityConstraint = 43713
	SchedulerInvalidPumpElementForPumpStartConstraint = 43714
	SchedulerUndefinedPumpElementForPumpStartConstraint = 43715
	SchedulerInvalidTankElementForTankConstraint = 43716
	SchedulerUndefinedTankElementForTankConstraint = 43717
	SchedulerRandomSeedMustBeGreaterThanZero = 43718
	SchedulerTopSolutionsMustFallWithinRange = 43719
	SchedulerPopulationSizeMustFallWithinRange = 43720
	SchedulerElitePopulationSizeMustFallWithinRange = 43721
	SchedulerCrossOverPointsMustFallWithinRange = 43722
	SchedulerMutationRateMustFallWithinRange = 43723
	SchedulerCreepRateMustFallWithinRange = 43724
	SchedulerCreepDownRateMustFallWithinRange = 43725
	SchedulerCutRateMustFallWithinRange = 43726
	SchedulerCrossOverRateMustFallWithinRange = 43727
	SchedulerTournamentRateMustFallWithinRange = 43728
	SchedulerMaximumGenerationsMustFallWithinRange = 43729
	SchedulerMaximumErasMustFallWithinRange = 43730
	SchedulerMaximumTrialsMustBeGreaterThan = 43731
	SchedulerMaxNonImproveGensMustFallWithinRange = 43732
	SchedulerEliteMateRateMustFallWithinRange = 43733
	SchedulerSpliceRateMustFallWithinRange = 43734
	SchedulerInvalidPumpElementForPumpObjective = 43735
	SchedulerUndefinedPumpElementForPumpObjective = 43736
	SchedulerInvalidPumpBatteryElementForPumpBatteryObjective = 43737
	SchedulerUndefinedPumpBatteryElementForPumpBatteryObjective = 43738
	SchedulerInvalidTankElementForTankObjective = 43739
	SchedulerUndefinedTankElementForTankObjective = 43740
	SchedulerMinimizeEnergyCostOptimizationNotYetSupported = 43741
	SchedulerGlobalMinimumPressureMustBeLessThanGlobalMaximumPressure = 43742
	SchedulerMinimumPressureMustBeLessThanMaximumPressure = 43743
	SchedulerTankMinimumFinalLevelFallsOutsideTankOperatingRange = 43744
	SchedulerVelocityMustBeGreaterThanZero = 43745
	SchedulerGlobalVelocityMustBeGreaterThanZero = 43746
	SchedulerInvalidScenario = 43747
	SchedulerInvalidPumpEfficiencyDataInPumpDefinition = 43748
	SchedulerMotorEfficiencyMustBeAboveZeroAndLessThanOrEqualTo100Percent = 43749
	SchedulerNotEnoughPointsInMotorEfficiencyCurve = 43750
	SchedulerInvalidPricePatternForPumpObjective = 43751
	SchedulerUndefinedPricePatternForPumpObjective = 43752
	SchedulerInvalidPricePatternForPumpBatteryObjective = 43753
	SchedulerUndefinedPricePatternForPumpBatteryObjective = 43754
	SchedulerNotEnoughPointsInEnergyPricingCurve = 43755
	SchedulerStartEnergyPriceMustGreaterThanZero = 43756
	SchedulerDuplicateTimesInEnergyPricePattern = 43757
	SchedulerFirstEnergyPriceInPatternMustMatchLast = 43758
	SchedulerEnergyPricePatternPointsOutOfOrder = 43759
	SchedulerDuplicatePumpDecision = 43760
	SchedulerNoConstraintsDefined = 43761
	SchedulerDuplicatePressureConstraint = 43762
	SchedulerDuplicateVelocityConstraint = 43763
	SchedulerDuplicatePumpStartConstraint = 43764
	SchedulerDuplicateTankConstraint = 43765
	SchedulerDuplicatePumpObjectiveElement = 43766
	SchedulerDuplicatePumpBatteryObjectiveElement = 43767
	SchedulerDuplicateTankObjectiveElement = 43768
	SchedulerCannotOptimizeConstantPowerPumps = 43769
	SchedulerScenarioToOptimizeMustBeEPSScenario = 43770
	SchedulerInvalidStartTimeForDecision = 43771
	SchedulerInvalidDurationForDecision = 43772
	SchedulerInvalidStartTimeAndDurationForDecision = 43773
	SchedulerMinimumSpeedMustBeLessThanMaximumSpeed = 43774
	SchedulerMinimumSpeedSettingMustBeGreaterThanZero = 43775
	SchedulerMaximumSpeedSettingMustBeLessThanTen = 43776
	SchedulerInvalidSpeedSettingsNotEnoughChoices = 43777
	SchedulerInvalidSpeedSettingsTooManyChoices = 43778
	SchedulerEnergyPricePatternFirstTimeIsZero = 43779
	SchedulerTankMinimumLevelRequiredLessThanTankMinimumLevel = 43780
	SchedulerTankMaximumLevelRequiredGreaterThanTankMaximumLevel = 43781
	SchedulerMinimumRequiredTankLevelGreaterThanOrEqualToMaximumRequiredLevel = 43782
	SchedulerAtLeastOnePumpIsIncludedInMultipleDecisions = 43783
	SchedulerInvalidPumpStationElementForDecision = 43784
	SchedulerUndefinedPumpStationElementForDecision = 43785
	SchedulerInvalidPumpStationDecision = 43786
	SchedulerUndefinedPumpStationDecision = 43787
	SchedulerCannotHaveMoreThanOnePumpBatteryWithTheSamePumpDefinition = 43788
	SchedulerProblemsInHydraulicModel = 43789
	SchedulerMinimumRequiredTankFinalLevelHigherThanMaximumAllowedLevel = 43790
	SchedulerMinimumAllowedLevelIsHigherThanInitialLevel = 43791
	SchedulerMaximumAllowedLevelIsLowerThanInitialLevel = 43792
	SchedulerUserAbortedBeforeRunCommenced = 43793
	STMGlobalStormEventNotSet = 44000
	STMCatalogInletNotSet = 44001
	STMValueMustBeGreaterThanZero = 44002
	STMValueMustBeNonNegative = 44003
	STMFieldInTableMustBeInAscendingOrder = 44004
	STMFieldInTableMustBeInDescendingOrder = 44005
	STMAtLeastTwoItemsInTable = 44006
	STMConduitCatalogPipeNotSelected = 44007
	STMCatchmentDrainToElementNotSelected = 44008
	STMCatchbasinInletNotSelected = 44009
	STMGutterDirectionFromLowToHigh = 44010
	STMThereIsLoopInNetwork = 44011
	STMThereAreDisconnectedElements = 44012
	STMCatalogConduitNotSelected = 44013
	STMValueCannotExceedLimit = 44014
	STMFieldInTableMustBeGreaterThanZero = 44015
	STMConduitVirtualConduitAsPhysicalLink = 44016
	STMFieldInTableMustBeNonNegative = 44017
	STMInletInSagNotHave100PercentCapture = 44018
	STMFieldMustBeSmallerThanOtherFieldInTable = 44019
	STMOutfallTailWaterHigherThanGround = 44020
	STMNodeFlowHeadlossCurveNotSet = 44021
	STMCatchmentTcCanNotBeLargerThanMaxDuration = 44022
	STMCatchbasinExternalTcCanNotBeLargerThanMaxDuration = 44023
	STMCatchmentRationalCIsGreaterThanOne = 44024
	STMInletOnGradeNoOutgoingGutter = 44025
	STMInletInSagWithOutgoingGutter = 44026
	STMOpenChannelOvertopped = 44027
	STMPipeArchSizesNotMatch = 44028
	STMPipeArchAreaMustBeInRange = 44029
	STMNoAvailableDesignPipeInPipeCatalog = 44030
	STMNoAvailableDesignLengthInInletCatalog = 44031
	STMNonCatalogInletCanNotBeDesigned = 44032
	STMElementValueNotInitialized = 44033
	STMNodeFlooded = 44034
	STMRationalIntensityInvalid = 44035
	STMConduitNotMeetMinCover = 44036
	STMConduitNotMeetMaxCover = 44037
	STMConduitNotMeetMinSlope = 44038
	STMConduitNotMeetMaxSlope = 44039
	STMConduitNotMeetMinVelocity = 44040
	STMConduitNotMeetMaxVelocity = 44041
	STMDisChargeAboveDesignCapacity = 44042
	STMMultipleDiversionLinkFromNode = 44043
	STMConduitShapeNotSelected = 44044
	STMTcLessThanMinTc = 44045
	STMHGLHigherThanRim = 44046
	STMInvalidConduitShapeDefinition = 44047
	STMOpenChannelCanNotBeDesigned = 44048
	STMStructurePipeInvertNotAgreeBenchingType = 44049
	STMConduitShapeMaterialDiffCatalogShapeMaterial = 44050
	STMConduitMaterialNotSelected = 44051
	STMValueNotSet = 44052
	STMOnGradeInletEfficiencyLowerThanMinimumEfficiency = 44053
	STMStandardHeadlossCoefficientSmallerThanZero = 44054
	STMGutterCrossSlopeSmallerThanRoadCrossSlope = 44055
	STMLinkEndNodeNotSet = 44056
	STMAvailableInletLengthNotPositive = 44057
	STMCanNotMatchUpstreamRise = 44058
	STMOutfallNotConnectedToConduit = 44059
	STMScaledLengthIsZero = 44060
	STMMultiplePondOutletStructureNotSupported = 44061
	STMGVFSolverOnlySupportRatingTableTypeDiversion = 44062
	STMCInletMethodNotSupported = 44063
	STMCWetWellMaxElevationInControl = 44064
	STMCWetWellMinElevationInControl = 44065
	STMCWetWellIniElevationInControl = 44066
	STMLinkInvertLowerThanNodeInvert = 44067
	STMCPondInitialHGLUsed = 44068
	STMCPressureRoughnessConvertToGravityRoughness = 44069
	STMCPressureRoughnessCanNotConvertToGravityRoughness = 44070
	STMValueMustBeZeroOrNegative = 44071
	STMCPondInfiltrationIgnored = 44072
	STMCPondOutflowPipeIsHigherThanControl = 44073
	STMPressurePipesTreatedAsConduits = 44074
	STMWetWellMinimumElevMustBeGreaterThanBase = 44075
	STMInvalidWetWellOperatingRange = 44076
	STMIrregularGutterShapeNotSupported = 44077
	STMTimeVaringInflowNotSupported = 44078
	STMDWFNotSupported = 44079
	STMWetWellDWFNotSupported = 44080
	STMWetWellWWFNotSupported = 44081
	STMPressureJucDWFNotSupported = 44082
	STMPressureJucWWFNotSupported = 44083
	STMOutfallWWFNotSupported = 44084
	STMPondIsFlooding = 44085
	STMGutterConnectedToPond = 44086
	STMPipeControlNotSupported = 44087
	STMDiversionDownstreamOutfallSetFree = 44088
	STMGutterConnectedBoundaryOutfallNoElement = 44089
	STMOutfallBoundaryElementNotSelected = 44090
	STMCatalogGutterNotSelected = 44091
	STMGutterStartNodeOutfall = 44092
	STMParallelPumpsNotSupported = 44093
	STMBoundaryElementInActive = 44094
	STMPumpCurveNotSupported = 44095
	STMPondInitialElevationIgnored = 44096
	STMAirValveWarning = 44097
	STMPumpCurveNotDecendingOrder = 44098
	STMCrossSectionIgnoredOnConduit = 44099
	STMCatchmentHydrographNotSupported = 44100
	STMFlapgateNotSupported = 44101
	STMPumpCurveNotUsed = 44102
	STMMaxConduitRiseExceeded = 44103
	STMPumpUpstreamMustBeWetwell = 44104
	STMPondDownstreamPipeCanNotBeVirtual = 44105
	STMIsolatedLinksNoResults = 44106
	STMLocalRunoffToPOSNodeNotSupported = 44107
	STMDiversionToPondInletNotSupported = 44108
	STMDiversionToPondOutletNotSupported = 44109
	STMIsolatedInletInflowLost = 44110
	STMOnlySurfaceFlowAndInletCalculation = 44111
	STMElevativeRelativeValuesMustBeNonNegative = 44112
	InletOnGradeBothBypassGutterDepthAndSpreadExceedsMax = 44113
	InletOnGradeBothGutterDepthAndSpreadExceedsMax = 44114
	InletOnGradeGutterDepthExceedsMax = 44115
	InletOnGradeGutterSpreadExceedsMax = 44116
	InletOnGradeBypassGutterDepthExceedsMax = 44117
	InletOnGradeBypassGutterSpreadExceedsMax = 44118
	InletInSagBothGutterDepthAndSpreadExceedsMax = 44119
	InletInSagGutterDepthExceedsMax = 44120
	InletInSagGutterSpreadExceedsMax = 44121
	InletInSagUKInletEfficiencyLowerThanMinimumEfficiency = 44122
	InletInSagUKInletTypeCannotBeDesigned = 44123
	STMNegativeIntensity = 44124
	STMHEC22ThirdEdJunctionLossMustBeEGLMode = 44125
	STMCatchmentRationalCWasGreaterThanOne = 44126
	STMGutterToInactiveInlet = 44127
	FrequencyFactorsDoesNotIncludeReturnPeriod = 44128
	STMFieldWithRespectToInTableMustBeInAscendingOrder = 44129
	STMOutfallToCatchmentElementNotSupported = 44130
	STMOutfallTailWaterIgnoredBySteepPipe = 44131
	HEC22MinorLossInvalidIncomingLinks = 44132
	MaximumSpreadLessThanDitchBottomWidth = 44133
	STMCModifiedRationalTreatedAsRational = 44134
	STMDiversionLinkWithoutParallelLink = 44135
	STSWBothRTKMethodsBeingUsed = 44136
	SewerOPSMixofRTKandNonRTKCatchmentsBeingUsed = 44137
	STMUKMultipleCatchmentsCantNotExport = 44480
	STMUKCatchbasinConvertedToManhole = 44481
	STMUKJunctionConvertedToManhole = 44482
	STMUKCatchmentHasZeroArea = 44483
	STMUKConduitIgnored = 44484
	STMUKSecFileDoesNotExist = 44485
	STMUKUnspecifiedLibraryConduit = 44486
	STMUKConduitDefDoesNotExistInLibrary = 44487
	STMUKIrregularChannelHasTooManyPoints = 44488
	STMUKClosedConduitPortionHasTooManyPoint = 44489
	STMUKTooManyNonCircularPipes = 44490
	STMUKMicroDrainageDoesNotSupportVariableRoughness = 44491
	STMUKMicroDrainageMoreThanThreeBarrels = 44492
	STMUKMicroDrainageInvalidPipeNumbers = 44493
	STMUKMicroDrainageUnsupportedMDXType = 44494
	STMUKWinDesVirtualLinksNotSupported = 44495
	STMUKWinDesVolumeTypeNotSupported = 44496
	STMUKWinDesFieldDataIgnoredOnExport = 44497
	STMUKMicrodarainageNonCircularConduitsNotExported = 44498
	STMCUKMicroDrainageMDXHasTooManyPoints = 44499
	HMREngineFailedToCompute = 44500
	HMREnginePipeCountLicensedExceeded = 44501
	HMREngineNotValidLicenseInPlace = 44502
	HMREngineSomeElementsAreMissingWTRGResults = 44503
	HMRAirValveAirOutflowDiameterMustNotBeNegative = 44510
	HMRAirValveSlowClosingAirOutflowDiameterMustBeGreaterThenZero = 44511
	HMRAirValveAirInflowDiameterMustNotBeNegative = 44512
	HMRAirValveTransitionVolumeMustMustNotBeNegative = 44513
	HMRAirValveInitialVolumeMustNotBeNegative = 44514
	HMRAirValvePressureTransitionNotSupportedInV7 = 44515
	AirvalveAirInflowCurveStartZero = 44516
	AirvalveAirInflowCurveEnd_34 = 44517
	AirvalveAirOutflowCurveStartZero = 44518
	AirvalveAirOutflowCurveEnd10000 = 44519
	AirvalveSmallAirOutflowCurveStartZero = 44520
	AirvalveSmallAirOutflowCurveEnd10000 = 44521
	AirvalveLargeAirOutflowCurveStartZero = 44522
	AirvalveLargeAirOutflowCurveEnd10000 = 44523
	AirvalveDiameterIsZero = 44524
	HMRSlowClosingAirValveNotSupportExtendedCAV = 44525
	HMROrificeTypicalFlowMustBeGreaterThenZero = 44530
	HMROrificePressureDropMustBeGreaterThenZero = 44531
	HMROrificeTypicalFlowMustNotBeNegative = 44532
	HMROrificePressureDropMustNotBeNegative = 44533
	HMRThresholdPressureMustNotBeNegative = 44534
	HMRThresholdPressureMustBeGreaterThenZero = 44535
	HMRSurgeValveTimeValveStaysOpenMustNotBeNegative = 44540
	HMRSurgeValveSpringConstantMustBeGreaterThenZero = 44541
	HMRSurgeValveDischargeCoefficientMustBeGreaterThenZero = 44542
	HMRSurgeValveSAVPressureClosureTriggerNotSupportedInV7 = 44543
	HMRSurgeTankWeirCoefficientMustNotBeNegative = 44550
	HMRSurgeTankDifferentialInternalRiserDiameterMustBeGreaterThenZero = 44551
	HMRSurgeTankWeirLengthMustNotBeGreaterThanZero = 44552
	HMRSurgeTankDifferentialExternalRiserDiameterMustBeGreaterThenZero = 44553
	HMRTankElevatedTanksNotHandledCorrectly = 44570
	HMRTankMissingInitialWaterElevationForSurgeTankWithCheckValve = 44571
	HMRTankNoAreaCurveGivenForVariableAreaTank = 44572
	HMRTankInitWaterElevationAboveTankTopForSurgeTankWithNoCheckValve = 44573
	HMRHydroTankInitialGasVolumeMustBeGreaterThenZero = 44580
	HMRHydroTankGasLawExponentNotInValidRange = 44581
	HMRHydroTankTankVolumeMustBeGreaterThenZero = 44582
	HMRHydropneumaticTankAirInflowCurveStartZero = 44583
	HMRHydropneumaticTankAirInflowCurveEnd_34 = 44584
	HMRHydropneumaticTankAirOutflowCurveStartZero = 44585
	HMRHydropneumaticTankAirOutflowCurveEnd10000 = 44586
	HMRHydropneumaticTankAirInflowDiameterMustNotBeNegative = 44587
	HMRHydropneumaticTankAirOutflowDiameterMustNotBeNegative = 44588
	HMRHydropneumaticTankDippingTubeDiameterMustBeGreaterThanZero = 44589
	HMRHydropneumaticTankCompressionChamberVolumeMustBeGreaterThanZero = 44590
	HMRHydropneumaticTankBottomElevationBiggerThanTopElevation = 44591
	HMRHydropneumaticTankDippingTubeDiameterBiggerThanTankDiameter = 44592
	HMRHydropneumaticTankBottomElevationBiggerDippingTubeBottomElevation = 44593
	HMRHydropneumaticTankTopElevationNotEqualDippingTubeTopElevation = 44594
	HMRHydropneumaticTankVoluneSmallerThanCompressionChamberVolume = 44595
	HMRJunctionInitialVaporVolumeMustNotBeNegative = 44600
	HMRJunctionInitialVaporVolumeOnlyAppliesToDeadEnds = 44601
	HMRJunctionPressureMustNotBeNegative = 44602
	HMRPumpTimeDelayMustNotBeNegative = 44610
	HMRPumpTimeToCloseMustNotBeNegative = 44611
	HMRPumpTimeOfOperationMustNotBeNegative = 44612
	HMRPumpNominalFlowTooSmall = 44613
	HMRPumpNominalFlowTooSmall_RunCopyTool = 44614
	HMRPumpSteadyFlowMustBeZeroForStartup = 44615
	HMRPumpOperatingRuleMustStartAtZeroSpeedForStartup = 44616
	HMRPumpDefSpecificSpeedValueIsUnknown = 44630
	HMRPumpDefEfficiencyNotInValidRange = 44631
	HMRPumpDefErrorConvertingPumpCurve = 44632
	HMRPumpDefUnknownSpecificSpeedValue = 44633
	HMRPumpDefInertiaMustNotBeNegative = 44634
	HMRPumpDefTooFewPointsInMultiPointEfficiencyCurve = 44635
	HMRPumpDefConstantPowerCurveNotSupported = 44636
	HMRPumpDefTooFewPointsInMultipointPumpCurve = 44637
	HMRPumpDefAllowReverseSpinOnlyAppliesToShutdownPump = 44638
	HMRPumpDefEfficiencyOutOfValidRange = 44639
	HMRTurbineUnknownSpecificSpeedValue = 44650
	HMRTurbineNotEnoughPointsInOperatingRule = 44651
	HMRTurbineLoadRejectionCurveNotValid = 44652
	HMRTurbineLoadAcceptanceCurveNotValid = 44653
	HMRTurbineLoadVariationCurveNotValid = 44654
	HMRTurbineInertiaMustBeGreaterThenZero = 44655
	HMRTurbineTimeDelayMustNotBeNegative = 44656
	HMRTurbineTimeOfOperationMustNotBeNegative = 44657
	HMRTurbineEfficiencyIsInvalid = 44658
	HMRTurbineInitialStateDoesNotMatchOperatingRule = 44659
	HMRValveNoHeadloss_UnableToCalculateDischargeCoefficient = 44660
	HMRValveDischargeCoefficientMustBeGreaterThenZero = 44661
	HMRValveCharacteristicCurveMissing = 44662
	HMRValveCharacteristicCurveValueOutOfRange = 44663
	HMRValveNonZeroFlowNeededToCalculateDischargeCoeff = 44664
	HMRValveOperatingRuleOpenConflict = 44665
	HMRValveOperatingRuleClosedConflict = 44666
	HMRValveInitialClosureMustBeBetween0And100 = 44667
	HMRValveDischargeCoeffCurveValueOutOfRange = 44668
	HMRValveDischargeCoeffCurveMissing = 44669
	HMRValveOperatingRuleDoesNotStartAtCorrectClosure = 44670
	HMRValveRelativeClosurePatternValuesOutsideAllowableRange = 44671
	HMRValveFullyOpenDischargeCoefficientMustBeGreaterThanZero = 44672
	HMRValveNominalFlowIsNegtive = 44673
	HMRValveNominalHeadIsNegtive = 44674
	HMRPeriodicPeriodMustBeGreaterThenZero = 44680
	HMRTurbineRatedFlowMustBeGreaterThanZero = 44685
	HMRTurbineRatedHeadMustBeGreaterThanZero = 44686
	HMRDischargeToAtmoTimeValveStartsOperating = 44690
	HMRCalcOptionsTimestepInvalid = 44700
	HMRCalcOptionsMaxAdjustmentForTimeMustBeGreaterThenZero = 44701
	HMRCalcOptionsTimeDurationNotInValidRange = 44702
	HMRCalcOptionsTimestepDurationNotInValidRange = 44703
	HMRCalcOptionsSpecificGravityNotInValidRange = 44704
	HMRCalcOptionsWaveSpeedMustNotBeNegative = 44705
	HMRCalcOptionsWaveSpeedIsTooLarge = 44706
	HMRCalcOptionsFlowToleranceIsTooSmall = 44707
	HMRCalcOptionsReportPeriodIsNegtive = 44708
	HMRCalcOptionsNoVaporPressureInput = 44709
	HMRCheckValveInitialFlowMustNotBeNegative = 44821
	HMRCheckValveDownstreamPipeMustBeSelected = 44822
	HMRCheckValvePipeWithCheckMustBeSelected = 44823
	HMRCheckValveUnableToExportInLongFormat = 44824
	HMRCheckValveOpeningTimeMustNotBeNegative = 44825
	HMRCheckValveClosureTimeMustNotBeNegative = 44826
	HMRCheckValveSlowClosingNotSupportedInV7 = 44827
	HMRCheckValveWyePipeMissing = 44828
	HMRCheckValveDynamicCurveMissing = 44829
	HMRNotEnoughPointsInCheckValveDynamicCurve = 44830
	HMRInactiveOrClosedValveCannotBeModulated = 44831
	HMRPipeWaveSpeedMustBeGreaterThenZero = 44840
	HMRPipeWaveSpeedShouldNotBeLessThen100FtPerSec = 44841
	HMRPipeDWFrictionCoefficientNotValid = 44842
	HMRPipeWaveSpeedIsTooLarge = 44843
	HMRPipesHaveBendsWithForceCalculationsEnabled = 44845
	HMRTimeToCloseMustBeGreaterThenZero = 44920
	HMRTimeToStartOperatingMustNotBeNegative = 44921
	HMRTimeToFullyOpenCloseMustNotBeNegative = 44922
	HMRTimeToCloseMustMustNotBeNegative = 44923
	HMRDiameterMustBeGreaterThenZero = 44924
	HMRTimeToOpenMustNotBeNegative = 44925
	HMRRotationalSpeedMustBeGreaterThenZero = 44927
	HMRElementDroppedBecauseStatusIsNotOn = 44929
	HMRElementDroppedBecauseStatusIsClosed = 44930
	HMRDroppedElementConnectedToPipeWithInactiveElement = 44931
	HMRDroppedElementConnectedToInactiveElement = 44932
	HMRDroppedElementConnectedToClosedPipe = 44933
	HMROperatingRuleCurveMissing = 44934
	HMRIsolatedNodeNotExported = 44935
	HMRIsolatedNodeExported = 44936
	HMRDownstreamPipeNotValid = 44937
	HMRTopologyOnlyOneConnectedPipeSupported = 44938
	HMRTopologyTwoConnectedPipesRequired = 44939
	HMRInletDiameterMustBeGreaterThenZero = 44940
	HMRRatioOfLossesMustNotBeNegative = 44941
	HMRMinorLossMustNotBeNegative = 44942
	HMRTopologyThreeConnectedPipesRequired = 44943
	HMRHeadLossMustNotBeNegative = 44944
	HMRWeirCoefficientDefinitionChanged = 44945
	HMRImportUnsupportedElementsInV7Model = 44946
	HAMRGasVesselInputTankVolumeIsDifferentWithCalculated = 44947
	HAMRGasVesselliquidLevelIsSmallerThanBaseElevation = 44948
	HAMRGasVesselInitialVolumeBiggerThanCalculated = 44949
	HAMRGasVesselliquidLevelMeanIsSmallerThanBaseElevation = 44950
	HMRwaveSpeedReductionFactorMustNotBeNegative = 44951
	HMRwaveSpeedReductionFactorMustNotBeGreaterThanOne = 44952
	HMRwaveSpeedDecreaseTimeMustNotBeNegative = 44953
	HMRwaveSpeedIncreaseTimeMustNotBeNegative = 44954
	HMRMultipleIncomingLinksConnectedToDirectedNode = 44955
	HMRInitialGasVolumeAndNodePressureArePositive = 44956
	HMRVairableLevelNotSupportBladderTank = 44957
	HMRPressureAirFlowCurveMissing = 44958
	HMRMinorLossMustBeGreaterThanZero = 44959
	MHRValveOpeningRateCoefficientMustBeGreaterThanZero = 44960
	HMRValveClosureRateCoefficientMustBeGreaterThanZero = 44961
	HMRVLANumberMustNotMoreThanHalfPipeNumber = 44962
	HMRTCVCharacteristicCurveMissing = 44963
	HMRSurgeTankHeadlossCoefficientMustBeGreaterThanZero = 44964
	HMRSurgeTankWeirCoefficientMustBeGreaterThanZero = 44965
	HMREngineBaseErrorCode = 45000
	HMREngineDataErrorInPipe = 45510
	HMREngineBeyondTurbineCurveLimit = 45514
	HMREngineZeroValveDischarge = 45519
	HMREngineEndPointsNotListed = 45520
	HMREngineRootNotObtainedQ2 = 45522
	HMREngineRootNotObtained = 45523
	HMREngineMaxIterationsExceeded = 45526
	HMREngineMaxIterationsExceededAtTime = 45527
	HMREngineDataError = 45528
	HMREngineEntryError = 45529
	HMREngineIncorrectSystemData = 45530
	HMREngineTooManyReportTimes = 45531
	HMREngineErrorInRoutine = 45532
	HMREngineVerticalLiftGate = 45534
	HMREngineTurbineDeterminant = 45536
	HMREngineZeroAREAHOR = 45539
	HMREngineHydFirstLineWrong = 45541
	HMREngineHydNumTimesInvalid = 45542
	HMREngineHydInitialTimeNotZero = 45543
	HMREngineHydTimesMustIncrease = 45544
	HMREngineInvalidSpecificGravity = 45560
	HMREnginePipeLengthTooShort = 45572
	HMREnginePipeDiameterTooSmall = 45574
	HMREngineErrorInPipeData = 45576
	HMREngineAssociatedDataIncorrect = 45578
	HMREngineWrongFlowIndicator = 45579
	HMREngineTooFewObjects = 45580
	HMREngineInvalidNumberOfTimesteps = 45582
	HMREngineEndpointsNumberedWrong = 45584
	HMREnginePointSpacingIncorrect = 45586
	HMREngineFrictionCoeffTooLarge = 45589
	HMREngineInitialPressureLessThenVaporPressure = 45592
	HMREngineReservoirPressureSubAtmosperic = 45593
	HMREngineNodeTypeNotIncluded = 45594
	HMREngineUnavailableType = 45595
	HMREngineIsolatedNode = 45596
	HMREngineIncorrectNodeLabel = 45597
	HMREngineIncorrectNodeNumbers = 45598
	HMREngineHighValveHeadloss = 45599
	HMREngineSystemUnitSystem = 45600
	HMREngineCalculationCanceledByUser = 45601
	HMREngineClosedNodeFlowMustBeZero = 45602
	HMREngineLiquidLevelLessThenElevation = 45607
	HMREngineOneElevationLessThenPipe = 45608
	HMREngineUnavailableSpecificSpeed = 45609
	HMREngineInvalidSpecificSpeed = 45610
	HMREngineNoZeroHeadRay1 = 45611
	HMREngineInitialValveFlowIsZero = 45612
	HMREngineMissingIncorrectData = 45614
	HMREngineValveDiameterMustBePositive = 45617
	HMREngineTooFewPipesAtNode = 45623
	HMREngineTooFewManyPipesAtNode = 45624
	HMREngineNodeNotInHydrograph = 45625
	HMREngineNegativeReservoirPressure = 45626
	HMREngineZeroInitialHead = 45627
	HMREngineReversePumpFlow = 45628
	HMREngineInitialPumpFlowNotSameAsOutflow = 45629
	HMREngineNominalFlowCantBeZero = 45632
	HMREnginePumpCurveNotComplete = 45634
	HMREngineMonotonicGateMovement = 45640
	HMREngineTurbineGateTop = 45641
	HMREngineGatePositionIncorrect = 45642
	HMREngineMandatoryForLoadAcceptance = 45645
	HMREngineInitialVolumeOfGasIsNotSufficientError = 45646
	HMREngineConsumpNodeHasNegativePressure = 45647
	HMREngineNodeInvalidData = 45750
	HMREngineNodeTableIsEmpty = 45751
	HMREnginePipeInvalidData = 45760
	HMREngineNodeDataIncorrect = 45812
	HMREngineDataErrorNearAirValve = 45924
	HMREngineDataErrorDiameterChange = 45926
	HMREngineDataErrorNearDeadEnd = 45928
	HMREngineDataErrorNearOrifice = 45932
	HMREngineSurgeLevelAbovePipeTop = 45962
	HMREngineDataErrorNearReservoir = 46023
	HMREngineDataErrorNearJunctionOrifice = 46062
	HMREngineDataErrorNearEndValve = 46064
	HMREngineDataErrorNearMiddleValve = 46066
	HMREngineDataErrorNearJunctionValve = 46068
	HMREnginePumpInZoneH = 46074
	HMREnginePumpInZoneE = 46076
	HMREnginePumpInZoneFGorH = 46202
	HMREnginePumpOutsideUniversalChart = 46204
	HMREnginePumpInZoneFG = 46206
	HMREnginePumpOutsideZones = 46207
	HMREngineInternalError = 46208
	HMREngineInvalidPath = 47130
	HMREngineGasVesselFillsContainer = 47202
	HMREngineNominalHeadAdjusted = 47205
	HMREngineIterationAffectingWeirA = 47206
	HMREngineIterationAffectingWeirB = 47207
	HMREngineWaveSpeedOrLengthDeviate = 47210
	HMREnginePossibleMissingData = 47215
	HMREngineNodeUpdateDiffers = 47217
	HMREngineAuxFileInvalid = 47220
	HMREngineConstantPumpOutsideNormalRange = 47227
	HMREngineIterationAffectingValveAtEndpoint = 47228
	HMREngineIterationForOrifice = 47229
	HMREngineExcessiveIterations = 47231
	HMREngineIterationAffectingValveBetweenPipes = 47233
	HMREngineUpstreamNodeOfCheckValveChosen = 47240
	HMREnginePressureZeroButNoCavity = 47249
	HMREngineFrictionCoeffSetToZero = 47250
	HMREngineIterationsForSurgeTank = 47252
	HMREngineIterationForSurgeTankAtTime = 47253
	HMREngineAirTrapped = 47257
	HMREngineNoConvergenceForVSP = 47258
	HMREngineBISECTWINRootIsInaccurate = 47259
	HMREngineFrictionLossError = 47260
	HMREnginePipeSubdividedTooManyTimes = 47265
	HMREngineTopOfVerticalShaftRaised = 47269
	HMREngineSurgeTankDrained = 47271
	HMREngineAllPathsInvalid = 47273
	HMREngineBISECTRootIsInaccurate = 47281
	HMREngineTurbineFunctionsFG = 47283
	HMREngineSetBranchVelocity = 47286
	HMREngineInitialSurgeTankLevelAboveTop = 47293
	HMREngineAirInPipeIsExpelled = 47299
	HMREngineBranchHasDrained = 47315
	HMREngineConcentratedCAVModelNeeded = 48112
	HMREngineCalculatedVolumeGreaterThanTankVolume = 48113
	HMRCalcOptionsTimestepSmallerThanSuggested = 48115
	HMREngineSAVZeroPressureReached = 48116
	HMREngineHTMaxAndMinPressureAndVolume = 48117
	HMREngineCalculatedHeadlossDiffersFromInput = 49130
	HMREngineModelSizeTooBig = 49202
	HMREngineErrorDuringInput = 49302
	HMREngineErrorDuringSimulation = 49304
	HMREngineRecordTooLong = 49323
	HMREngineSurgeValveOpens = 49506
	HMREngineSurgeTotalDischarge = 49507
	HMREngineManholeOverflow = 49508
	HMREngineManholeCoverEjected = 49509
	HMREngineValveDischarge = 49510
	HMREngineCheckValveCloses = 49511
	HMREnginePumpCheckValveCloses = 49512
	HMREngineWeirNoConvergenceHB = 49513
	HMREngineWeirNoConvergenceElev = 49514
	HMREngineCheckValveOpens = 49515
	HMREnginePathIntervalIncreased = 49516
	HMREngineCavityOpens = 49517
	HMREngineCavityCloses = 49518
	HMREngineTransitionToExtended = 49521
	HMREngineTransitionToConcentrated = 49522
	HMREngineCheckValveFullyClosed = 49530
	HMREngineCheckValveFullyOpen = 49531
	HMREngineCheckValveStartsToOpen = 49532
	HMREngineCheckValveStartsToClose = 49533
	HMREngineOneWaySurgeTankOverflow = 49565
	HMREngineSurgeTankOverflow = 49567
	HMREngineSurgeTankMaxAir = 49568
	HMREngineSlowAirValveOutflow = 49569
	HMREngineOpenPipeHasAlmostDrained = 49586
	HMREngineValveCavationOccured = 49587
	HMREngineAtLeast2ItemsInValveCharacteristicsCurve = 49588
	HMRRunDurationToLongOrTooSmallTimeStep = 49589
	HMRTooManyPipesConnectedToNode = 49590
	LANDXMLDuplicateElement = 50501
	LANDXMLInvalidNodeReference = 50502
	LANDXMLNoPipeNetwork = 50503
	LANDXMLNotWellFormedXml = 50504
	LANDXMLPipeBendExport = 50505
	LANDXMLPipeNetworkNotSpecified = 50506
	LANDXMLPipeNetworkNotConsistent = 50507
	LANDXMLElementLabelChanged = 50508
	LANDXMLLinkAssociatedWithInactiveNode = 50509
	SWCGravityConduitConnectedToPressureNode = 51001
	SWCHasIsolatedGravityElements = 51002
	SWCHasPressureElementsWithoutGravityReceivingNodes = 51003
	SWCDiversionLinksFormsDirectedLoop = 51004
	SWCPressurePipeFormsDirectedLoop = 51005
	SWCWetWellDownstreamPressureSubNetworFormsDirectedLoop = 51006
	SWCConnectedNetworkElementsWithoutOutfall = 51007
	SWCNoElementsInNetwork = 51008
	SWCDiversionLinkFromDownstreamToUpstreamInOneSubNetwork = 51009
	SWCGravitySubNetworkWithMoreThanOneWetWellOrOutfall = 51010
	SWCHasLoopsInGravityNetwork = 51011
	SWCHydrologicHydraulicTimeStepsInvalid = 51012
	SWCVariableReportingHydraulicTimeStepInvalid = 51013
	SWCVariableReportingTimeStepInvalid = 51014
	SWCWetWellInflowGreaterThanOutflow = 51015
	SWCWetWellIncrementMustBeGreaterThanZero = 51016
	SWCInfiltrationPatternNoExists = 51017
	SWCTooFewNodesInPressureSubNetwork = 51018
	SWCPressurePipeInvertHigherThanWetWellBase = 51019
	SWCPressurePipeInvertLowerThanGravityNodeInvert = 51020
	SWCConduitInfiltrationUnitNotDefined = 51021
	SWCMoreThanOneConduitOutOfGravityNode = 51022
	SWCMoreThanOneConduitConnectedToFreeOutfall = 51023
	SWCPressureEngineDeletedOrInactiveConditionElement = 51024
	SWCPressureEngineDeletedOrInactiveActionElement = 51025
	SWCPressureReservoirIsEmptying = 51026
	SWCPressureReservoirIsFilling = 51027
	SWCPressureReservoirIsClosed = 51028
	SWCInvalidPumpDefinitionType = 51029
	SWCPumpDefInvalidPoints = 51030
	SWCKuttersPressureFrictionMethod = 51031
	SWRCInvertPlusHeightHigherNodeRim = 51032
	SWRCConduitHasStartAndStopControl = 51033
	SWRCConduitStartControlEmpty = 51034
	SWRCConduitStopControlEmpty = 51035
	SWRCConduitStartControlStructureHasMoreThan2Controls = 51036
	SWRCConduitStopControlStructureHasMoreThan2Controls = 51037
	SWRCConduitControlCrestElevLowerThanConduitInvert = 51038
	SWRCConduitWeirCoefficientEqualToOrLessThanZero = 51039
	SWRCConduitWeirLengthZeroOrLessThanZero = 51040
	SWRCConduitWeirNumOfContractionsLessThanZero = 51041
	SWRCVNotchWeirAngleLessThanZero = 51042
	SWRCWeirEndCoefficientLessThanZero = 51043
	SWRCWeirSideSlopeLessThanZero = 51044
	SWRCControlFuncnctionCoefficientZero = 51045
	SWRCControlFuncnctionExponentZero = 51046
	SWRCControlDepthDischargeCurveDepthWrongOrder = 51047
	SWRCControlDepthDischargeCurveDepthLessThanZero = 51048
	SWRCControlDepthDischargeCurveDischargeLessThanZero = 51049
	SWRCOrificeDiameterZeroOrLessThanZero = 51050
	SWRCOrificeWidthZeroOrLessThanZero = 51051
	SWRCOrificeHeightZeroOrLessThanZero = 51052
	SWRCOrificeCoefficientEqualToOrLessThanZero = 51053
	SWRCWeirTopEqualToOrLowerThanCrest = 51054
	SWRCControlDepthDischargeCurvePointNumberLessThan2 = 51055
	SWRCConduitControlSubmerged = 51056
	SWRCPipeFailedToConverge = 51057
	SWRCManholeHGLHigherThanPressurePipeCrown = 51058
	SWRCStructureIsPressurized = 51059
	SWRCCatchmentNotSupportedInSteadyStateRun = 51060
	SWRCMultipleDiversionTotalDivertedFlowGreaterThanSystemFlow = 51061
	SWRCGVFSolverOnlySupportRatingTableTypeDiversion = 51062
	SWRCPumpMustConnectToPressurePipe = 51063
	SWRCPondInfiltrationIgnoredSteadyState = 51064
	SWRCPondInfiltrationIgnoredNoOutletStructure = 51065
	SWRCInletOpeningIgnoredTreatedAsFullCapture = 51066
	SWRCMultipleDiversionWithCutoffType = 51067
	SWRCCulvertIgnoredCapacityAnalysis = 51068
	SWRCPipeLocalLossIgnored = 51069
	SWCCalcOptionMinConvexCInvalid = 51070
	SWCKuttersNotValidPressureFrictionMethod = 51071
	SWRCPondRoutingInfo = 51072
	SWRCInletNotDesigned = 51073
	SWRCVSPBOnOffElevOverrideControls = 51074
	SWRCPumpSuctionSideNodeMustBeWetWellOrPressureJunction = 51075
	SWRGPondsNotSupported = 52000
	SWRGGuttersNotSupported = 52001
	SWRGPondOutletStructureConverted = 52002
	SWRGCrossSectionNodeConverted = 52003
	SWRGCatchBasinConverted = 52004
	SWRGChannelConverted = 52005
	SWRGCatchmentNotSupported = 52006
	SWRGWwFlowNotSupported = 52007
	SWRGDwFlowNotSupported = 52008
	SWRConduitTypeNotSet = 52009
	STMCCatchmentsNotSupported = 53000
	STMCGuttersNotSupported = 53001
	STMCSWRCDiversionsIgnoredForHEC22Nodes = 53002
	STMCDepthVsCapturedInletTypeForInSagOnly = 53003
	STMCInletTypeForInSagWillBe100CaptureAnyways = 53004
	STMCInvalidEndNodeForGutterLink = 53005
	STMCCulvertInvalidConduitShape = 53006
	GVFBoundaryNodeDoesntSupportWWFs = 53007
	STMPressureEnginePressuresBelowZero = 53008
	STMPressureEnginePressuresBelowMinPossiblePressure = 53009
	PPKCN = 56000
	PPKArea = 56001
	PPKDepth = 56002
	PPKRationalC = 56003
	PPKTableItemCount = 56004
	PPKFrequency = 56005
	PPKStartTime = 56006
	PPKIncrementLessThanZero = 56007
	PPKIncrementGreaterDifference = 56008
	PPKEndTime = 56009
	PPKEndTimeLessStartTime = 56010
	PPKNoOutletStructureSpecified = 56011
	PPKNoPondSpecified = 56012
	PPKOutletStructureNoExist = 56013
	PPKPondNoExist = 56014
	PPKTC = 56015
	PPKOutflow = 56016
	PPKIDFCurveList = 56017
	PPKLength = 56018
	PPKDiameter = 56019
	PPKNumberOfBarrels = 56020
	PPKSlope = 56021
	PPKIncrement = 56022
	PPKElevation = 56023
	PPKNoHydrographSpecified = 56024
	PPKHydrographNoExist = 56025
	PPKFlow = 56026
	PPKHydrographsSame = 56027
	PPKManningsN = 56028
	PPKLeftXGreaterRightX = 56029
	PPKRightXLessLeftX = 56030
	PPKElevationLessInvert = 56031
	PPKWidth = 56032
	PPKAverageRate = 56033
	PPKInfiltrationUnitHead = 56034
	PPKExponent = 56035
	PPKfLoss = 56036
	PPKGaPSI = 56037
	PPKGaKs = 56038
	PPKTd = 56039
	PPKNoQqpTemplate = 56040
	PPKQqpTemplateNoExist = 56041
	PPKVoidSpace = 56042
	PPKNoChannel = 56043
	PPKChannelNoExist = 56044
	PPKOSStep = 56045
	PPKRangeMax = 56046
	PPKDownstreamOutletID = 56047
	PPKHeight = 56048
	PPKInletControlCoefficient = 56049
	PPKNumberOfCrossSections = 56050
	PPKNumberOfOpenings = 56051
	PPKOrificeCoefficient = 56052
	PPKDatumElevation = 56053
	PPKWeirCoefficient = 56054
	PPKAngle = 56055
	PPKDurationMultiplier = 56056
	PPKNoSCSRainfallList = 56057
	PPKSCSRainfallListNoExist = 56058
	PPKNoRainfallCurve = 56059
	PPKRainfallCurveNoExist = 56060
	PPKE = 56061
	PPKB = 56062
	PPKD = 56063
	PPKSubReachs = 56064
	PPKKCoefficient = 56065
	PPKXCoefficient = 56066
	PPKTransitionTime = 56067
	PPKUserDefinedTC = 56068
	PPKRadius = 56069
	PPKChannelFactor = 56070
	PPKImpervious = 56071
	PPKTCMultiplier = 56072
	PPKVelocity = 56073
	PPKWettedPerimeter = 56074
	PPKOffset = 56075
	PPKQTolMaxLessMin = 56076
	PPKInvalidLabel = 56077
	PPKDownstreamIDEqualsUpstreamID = 56078
	PPKUPlusUCExceeds30Percent = 56079
	PPKPercentUExceeds100Percent = 56080
	PPKInvalidRainfallFractions = 56081
	PPKInvalidTimeDepthCurve = 56082
	PPKNoIDFCurveSpecified = 56083
	PPKNoRNFCurveSpecified = 56084
	PPKNoTDCCurveSpecified = 56085
	PPKTrapezoidalBaseWidth = 56086
	PPKMinHWElevationNotFound = 56087
	PPKMaxHWElevationNotFound = 56088
	PPKMinTWElevationNotFound = 56089
	PPKMaxTWElevationNotFound = 56090
	PPKHeadwaterPondRangeNotSpecified = 56091
	PPKTailwaterPondRangeNotSpecified = 56092
	PPKNoUnitHydrographSpecified = 56093
	PPKUnitHydrographNotExisting = 56094
	PPKShapeFactorInvalid = 56095
	PPKDepressionStorage = 56096
	PPKUnitHydrographPoints = 56097
	PPKMaximumnPondsExceeded = 56098
	PPKHfc = 56099
	PPKHfo = 56100
	PPKhK = 56101
	PPKHfoLessThanHfc = 56102
	PPKRatingTableMin = 56103
	PPKRatingTableMax = 56104
	PPKRatingTableOutOfRange = 56105
	PPKConvolutionTimeStep = 56106
	PPKDuration = 56107
	PPKnPoints = 56108
	PPKNoLinks = 56109
	PPKNoSubareasNoHydQueue = 56110
	PPKRegisteredNumberOfPondsExceeded = 56111
	PPKInvalidPipeLength = 56112
	PPKTofTcValueCount = 56113
	PPKNoUserDefinedTag = 56114
	PPKNoUserDefinedFlow = 56115
	PPKNoUserDefinedData = 56116
	PPKNoESItemsCheckedForUse = 56117
	PPKNoChannelBankTypeSpecified = 56118
	PPKNoIterpolateValue = 56119
	PPKFlowTol = 56120
	PPKRatingTableStep = 56121
	PPKCustom = 56122
	PPKMissingHydrographTag = 56123
	PPKTagNoExist = 56124
	PPKNoWeirTableSpecified = 56125
	PPKWeirTableNoExist = 56126
	PPKDisconnectedNodes = 56127
	PPKDirectoryLength = 56128
	PPKTableItemCountXSection = 56129
	PPKStretchPercent = 56130
	PPKNoStormsInuse = 56131
	PPKNoLocalSCSRainfallList = 56132
	PPKTableItemCountWeirXY = 56133
	PPKTagLengthExceeded = 56134
	PPKNoOverflowChannel = 56135
	PPKInvalidTopOfWeir = 56136
	PPKMinimumHeadwaterElevationOutofRange = 56137
	PPKMaximumHeadwaterElevationOutofRange = 56138
	PPKHWandTWSteps = 56139
	PPKIncrementIsTooLittle = 56140
	PPKOutletStructureMismatchLink = 56141
	PMNoDesignScenario = 60001
	PMNoTargetScenario = 60002
	PMNoTargetElement = 60003
	PMNoDesignScenariosSelected = 60004
	ControlRoomUsedModelInitialSettingsValue = 61000
	ControlRoomNotSCADAConnectLicense = 61001
	ControlRoomSCADAConnectSignalCountExceeded = 61002
	ControlRoomUnsupportedElementType = 61003
	ControlRoomUnsupportedAttribute = 61004
	ControlRoomOPCDAConnectionFailed = 61005
	ControlRoomOPCHDAConnectionFailed = 61006
	ControlRoomCitectConnectionFailed = 61007
	ControlRoomDatabaseConnectionFailed = 61008
	ControlRoomConnectionFailed = 61009
	GAEngineReferenceToUndefinedNode = 65000
	GAEngineReferenceToUndefinedLink = 65001
	GAEngineNotEnoughNodesInNetwork = 65002
	GAEngineNoGasRegulatingValvesInNetwork = 65003
	GAEngineNoGasRegulatingValvesWithSupplyPressureInNetwork = 65004
	GAEngineOutOfMemory = 65005
	GAEngineFailedToValidateModel = 65006
	GAEngineFailedToLoadModel = 65007
	GAEngineViscosityMustBeGreaterThanZero = 65100
	GAEngineSutherlandConstantMustBeGreaterThanZero = 65101
	GAEngineCalorificValueMustBeGreaterThanOrEqualToZero = 65102
	GAEngineDensityMustBeGreaterThanZero = 65103
	GAEngineGasRegulatingValveSupplyPressureGreaterThanMaxPressure = 65110
	GAEngineGasRegulatingValveSupplyFlowGreaterThanMaxFlow = 65111
	GAEngineGasRegulatingValveSupplyPressureMustBeGreaterThanZero = 65112
	GAEngineGasRegulatingValveSupplyFlowMustBeGreaterThanZero = 65113
	GAEngineUnknownRegulatingValveSupplyMode = 65114
	GAEngineUnknownRegulatingValveInitialSetting = 65115
	GAEngineDeletedIsolationValveReferencePipe = 65120
	GAEngineUndefinedIsolationValveReferencePipe = 65121
	GAEnginePatternMinPressureMustBeGreaterThanOrEqualToZero = 65122
	GAEngineUnknownIsolationValveInitialSetting = 65123
	GAEngineDirectedNodeReferencesUndefinedNode = 65131
	GAEngineDeletedOrInactiveDownstreamPipe = 65132
	GAEngineUndefinedDownstreamPipe = 65133
	GAEnginePipeLengthMustBeGreaterThanZero = 65140
	GAEnginePatternMaxPressureMustBeGreaterThanOrEqualToZero = 65141
	GAEnginePipeRoughnessCannotBeNegative = 65142
	GAEnginePipeReferencesUndefinedNode = 65143
	GAEnginePipeReferencesDeletedOrInactiveNode = 65144
	GAEngineLinkStartAndEndNodesAreTheSame = 65145
	GAEngineUnknownGasPipeInitialSetting = 65146
	GAEngineNoGasPipesInNetwork = 65147
	GAEngineNoGasPipeTypes = 65148
	GAEngineUndefinedDemandPattern = 65150
	GAEngineNoDemandFlow = 65151
	GAEngineNotEnoughPointsInPattern = 65152
	GAEnginePatternCannotHaveDuplicateTimes = 65153
	GAEngineFirstTimeInPatternCannotBeZero = 65154
	GAEngineFirstMultiplierMustMatchLastPatternMultiplier = 65155
	GAEnginePatternPointsOutOfOrder = 65156
	GAEngineUndefinedPipeDiameter = 65157
	GAEngineUndefinedPipeRoughness = 65158
	GAEngineUndefinedPipeType = 65159
	GAEngineFailedToRunModel = 65200
	GAEngineMaximumVelocityMustBeGreaterThanZero = 65201
	GAEngineMaximumHeadlossGradientMustBeGreaterThanZero = 65202
	GAEnginePipeIDFromSelectionNotFound = 65203
	GAEnginePressureAccuracyMustBeGreaterThanZero = 65204
	GAEngineMaxTrialsMustBeGreaterThanZero = 65205
	GAEnginePatternMaxPressureMustBeGreaterThanMinPressure = 65206
	GAEngineRoughnessMustBeSmallerThanPipeRadius = 65207
	GAEngineInnerDiameterMustBeGreaterThanZero = 65208
	GAEngineAirDensityMustBeGreaterThanZero = 65209
	GAEngineReferenceAtmosphericPressureMustBeGreaterThanZero = 65210
	GAEnginePressureFactorMustBeGreaterThanValue = 65211
	GAEnginePressureFactorMustBeSmallerThanValue = 65212
	GAEngineGenericMessage = 65499
	BerlinEngine1001 = 65500
	BerlinEngine1010 = 65501
	BerlinEngine1011 = 65502
	BerlinEngine1012 = 65503
	BerlinEngine1013 = 65504
	BerlinEngine1014 = 65505
	BerlinEngine5001 = 65506
	BerlinEngine5002 = 65507
	BerlinEngine5003 = 65508
	BerlinEngine5004 = 65509
	BerlinEngine5005 = 65510
	BerlinEngine5006 = 65511
	BerlinEngine5007 = 65512
	BerlinEngine5008 = 65513
	BerlinEngine5009 = 65514
	BerlinEngine5010 = 65515
	BerlinEngine5011 = 65516
	BerlinEngine5012 = 65517
	BerlinEngine5013 = 65518
	BerlinEngine5014 = 65519
	BerlinEngine5015 = 65520
	BerlinEngine5016 = 65521
	BerlinEngine5017 = 65522
	BerlinEngine5018 = 65523
	BerlinEngine5019 = 65524
	BerlinEngine5020 = 65525
	BerlinEngine5021 = 65526
	BerlinEngine5022 = 65527
	BerlinEngine5023 = 65528
	BerlinEngine5103 = 65529
	BerlinEngine5104 = 65530
	BerlinEngine5105 = 65531
	BerlinEngine5106 = 65532
	BerlinEngine5107 = 65533
	BerlinEngine5109 = 65534
	BerlinEngine5113 = 65535
	BerlinEngine5114 = 65536
	BerlinEngine5115 = 65537
	BerlinEngine5121 = 65538
	BerlinEngine5122 = 65539
	BerlinEngine5123 = 65540
	BerlinEngine5124 = 65541
	BerlinEngine5125 = 65542
	BerlinEngine5126 = 65543
	BerlinEngine5127 = 65544
	BerlinEngine5128 = 65545
	BerlinEngine5130 = 65546
	BerlinEngine5131 = 65547
	BerlinEngine5223 = 65548
	BerlinEngine5301 = 65549
	BerlinEngine5302 = 65550
	BerlinEngine5303 = 65551
	BerlinEngine5304 = 65552
	BerlinEngine5305 = 65553
	BerlinEngine5306 = 65554
	BerlinEngine5309 = 65555
	BerlinEngine5310 = 65556
	BerlinEngine5401 = 65557
	BerlinEngine5402 = 65558
	BerlinEngine5403 = 65559
	BerlinEngine5404 = 65560
	BerlinEngine5405 = 65561
	BerlinEngine5406 = 65562
	BerlinEngine5407 = 65563
	BerlinEngine5408 = 65564
	BerlinEngine5409 = 65565
	BerlinEngine5410 = 65566
	BerlinEngine5411 = 65567
	BerlinEngine5412 = 65568
	BerlinEngine5413 = 65569
	BerlinEngine5414 = 65570
	BerlinEngine5415 = 65571
	BerlinEngine5416 = 65572
	BerlinEngine5503 = 65573
	BerlinEngine5504 = 65574
	BerlinEngine5505 = 65575
	BerlinEngine5506 = 65576
	BerlinEngine5507 = 65577
	BerlinEngine5510 = 65578
	BerlinEngine5512 = 65579
	BerlinEngine5516 = 65580
	BerlinEngine5518 = 65581
	BerlinEngine5519 = 65582
	BerlinEngine5520 = 65583
	BerlinEngine5521 = 65584
	BerlinEngine5522 = 65585
	BerlinEngine5523 = 65586
	BerlinEngine5524 = 65587
	BerlinEngine5525 = 65588
	BerlinEngine5526 = 65589
	BerlinEngine5527 = 65590
	BerlinEngine5528 = 65591
	BerlinEngine5529 = 65592
	BerlinEngine5530 = 65593
	BerlinEngine5531 = 65594
	BerlinEngine5532 = 65595
	BerlinEngine5533 = 65596
	BerlinEngine5600 = 65597
	BerlinEngine5601 = 65598
	BerlinEngine5602 = 65599
	BerlinEngine5603 = 65600
	BerlinEngine5604 = 65601
	BerlinEngine5650 = 65602
	BerlinEngine5701 = 65603
	BerlinEngine5703 = 65604
	BerlinEngine5708 = 65605
	BerlinEngine5709 = 65606
	BerlinEngine5710 = 65607
	BerlinEngine5711 = 65608
	BerlinEngine5712 = 65609
	BerlinEngine5713 = 65610
	BerlinEngine5714 = 65611
	BerlinEngine5715 = 65612
	BerlinEngine5716 = 65613
	BerlinEngine5717 = 65614
	BerlinEngine5718 = 65615
	BerlinEngine5719 = 65616
	BerlinEngine5720 = 65617
	BerlinEngine5723 = 65618
	BerlinEngine5727 = 65619
	BerlinEngine5728 = 65620
	BerlinEngine5729 = 65621
	BerlinEngine5730 = 65622
	BerlinEngine5731 = 65623
	BerlinEngine5732 = 65624
	BerlinEngine5733 = 65625
	BerlinEngine5734 = 65626
	BerlinEngine5735 = 65627
	BerlinEngine5736 = 65628
	BerlinEngine5737 = 65629
	BerlinEngine5738 = 65630
	BerlinEngine5739 = 65631
	BerlinEngine5741 = 65632
	BerlinEngine5742 = 65633
	BerlinEngine5743 = 65634
	BerlinEngine5744 = 65635
	BerlinEngine5745 = 65636
	BerlinEngine5746 = 65637
	BerlinEngine5747 = 65638
	BerlinEngine5748 = 65639
	BerlinEngine5749 = 65640
	BerlinEngine5751 = 65641
	BerlinEngine5752 = 65642
	BerlinEngine5753 = 65643
	BerlinEngine5754 = 65644
	BerlinEngine5755 = 65645
	BerlinEngine5756 = 65646
	BerlinEngine5757 = 65647
	BerlinEngine5758 = 65648
	BerlinEngine5759 = 65649
	BerlinEngine5760 = 65650
	BerlinEngine5761 = 65651
	BerlinEngine5762 = 65652
	BerlinEngine6170 = 65653
	BerlinEngine6171 = 65654
	BerlinEngine6209 = 65655
	BerlinEngine6210 = 65656
	BerlinEngine6240 = 65657
	BerlinEngine6241 = 65658
	BerlinEngine6242 = 65659
	BerlinEngine6243 = 65660
	BerlinEngine6244 = 65661
	BerlinEngine6245 = 65662
	BerlinEngine6246 = 65663
	BerlinEngine6247 = 65664
	BerlinEngine6249 = 65665
	BerlinEngine6250 = 65666
	BerlinEngine6255 = 65667
	BerlinEngine6256 = 65668
	BerlinEngine6257 = 65669
	BerlinEngine6258 = 65670
	BerlinEngine6259 = 65671
	BerlinEngine6260 = 65672
	BerlinEngine6261 = 65673
	BerlinEngine6262 = 65674
	BerlinEngine6602 = 65675
	BerlinEngine6603 = 65676
	BerlinEngine6604 = 65677
	BerlinEngine6605 = 65678
	BerlinEngine6606 = 65679
	BerlinEngine6607 = 65680
	BerlinEngine6608 = 65681
	BerlinEngine6609 = 65682
	BerlinEngine6620 = 65683
	BerlinEngine6621 = 65684
	BerlinEngine6622 = 65685
	BerlinEngine6623 = 65686
	BerlinEngine6624 = 65687
	BerlinEngine6625 = 65688
	BerlinEngine6626 = 65689
	BerlinEngine6627 = 65690
	BerlinEngine6628 = 65691
	BerlinEngine6629 = 65692
	BerlinEngine6630 = 65693
	BerlinEngine6631 = 65694
	BerlinEngine6632 = 65695
	BerlinEngine6633 = 65696
	BerlinEngine6634 = 65697
	BerlinEngine6635 = 65698
	BerlinEngine6636 = 65699
	BerlinEngine6637 = 65700
	BerlinEngine6638 = 65701
	BerlinEngine6639 = 65702
	BerlinEngine6640 = 65703
	BerlinEngine6641 = 65704
	BerlinEngine6642 = 65705
	BerlinEngine6643 = 65706
	BerlinEngine6644 = 65707
	BerlinEngine6645 = 65708
	BerlinEngine6646 = 65709
	BerlinEngine6647 = 65710
	BerlinEngine6648 = 65711
	BerlinEngine6650 = 65712
	BerlinEngine6651 = 65713
	BerlinEngine6652 = 65714
	BerlinEngine6653 = 65715
	BerlinEngine6701 = 65716
	BerlinEngine6702 = 65717
	BerlinEngine6703 = 65718
	BerlinEngine6704 = 65719
	BerlinEngine6705 = 65720
	BerlinEngine6706 = 65721
	BerlinEngine6707 = 65722
	BerlinEngine6708 = 65723
	BerlinEngine6709 = 65724
	BerlinEngine6710 = 65725
	BerlinEngine6711 = 65726
	BerlinEngine6712 = 65727
	BerlinEngine6713 = 65728
	BerlinEngine6714 = 65729
	BerlinEngine6715 = 65730
	BerlinEngine6716 = 65731
	BerlinEngine6717 = 65732
	BerlinEngine6718 = 65733
	BerlinEngine6719 = 65734
	BerlinEngine6800 = 65735
	BerlinEngine6801 = 65736
	BerlinEngine6802 = 65737
	BerlinEngine6803 = 65738
	BerlinEngine6804 = 65739
	BerlinEngine6805 = 65740
	BerlinEngine6806 = 65741
	BerlinEngine6807 = 65742
	BerlinEngine6808 = 65743
	BerlinEngine6809 = 65744
	BerlinEngine6810 = 65745
	BerlinEngine6811 = 65746
	BerlinEngine6814 = 65747
	BerlinEngine6815 = 65748
	BerlinEngine6816 = 65749
	BerlinEngine6817 = 65750
	BerlinEngine6818 = 65751
	BerlinEngine6819 = 65752
	BerlinEngine6823 = 65753
	BerlinEngine6824 = 65754
	BerlinEngine6825 = 65755
	BerlinEngine6826 = 65756
	BerlinEngine6827 = 65757
	BerlinEngine6828 = 65758
	BerlinEngine6829 = 65759
	BerlinEngine6830 = 65760
	BerlinEngine6831 = 65761
	BerlinEngine6832 = 65762
	BerlinEngine6833 = 65763
	BerlinEngine6834 = 65764
	BerlinEngine6835 = 65765
	BerlinEngine6836 = 65766
	BerlinEngine6911 = 65767
	BerlinEngine6912 = 65768
	BerlinEngine6913 = 65769
	BerlinEngine6915 = 65770
	BerlinEngine6916 = 65771
	BerlinEngine6917 = 65772
	BerlinEngine7002 = 65773
	BerlinEngine7003 = 65774
	BerlinEngine7004 = 65775
	BerlinEngine7005 = 65776
	BerlinEngine7006 = 65777
	BerlinEngine7007 = 65778
	BerlinEngine7008 = 65779
	BerlinEngine7011 = 65780
	BerlinEngine7012 = 65781
	BerlinEngine7018 = 65782
	BerlinEngine7019 = 65783
	BerlinEngine7406 = 65784
	BerlinEngine7407 = 65785
	BerlinEngine7408 = 65786
	BerlinEngine7410 = 65787
	BerlinEngine7411 = 65788
	BerlinEngine7412 = 65789
	BerlinEngine7413 = 65790
	BerlinEngine7414 = 65791
	BerlinEngine7415 = 65792
	BerlinEngine7416 = 65793
	BerlinEngine7417 = 65794
	BerlinEngine7418 = 65795
	BerlinEngine7419 = 65796
	BerlinEngine7600 = 65797
	BerlinEngine7601 = 65798
	BerlinEngine7709 = 65799
	BerlinEngine7710 = 65800
	BerlinEngine7800 = 65801
	BerlinEngine7801 = 65802
	BerlinEngine7810 = 65803
	BerlinEngine7811 = 65804
	BerlinEngine7812 = 65805
	BerlinEngine7813 = 65806
	BerlinEngine7814 = 65807
	BerlinEngine7900 = 65808
	BerlinEngine7999 = 65832
	BerlinEngine7998 = 65833
	BerlinEngine8000 = 65834
	BerlinEngine8001 = 65835
	BerlinEngine8002 = 65836
	BerlinEngine8003 = 65837
	BerlinEngine7009 = 65838
	BerlinEngine8004 = 65839
	BerlinEngine8005 = 65840
	BerlinEngine8006 = 65841
	BerlinEngine8007 = 65842
	BerlinEngine8008 = 65843
	BerlinEngine5534 = 65844
	BerlinEngine5535 = 65845
	BerlinEngine5536 = 65846
	BerlinEngine7420 = 65847
	BerlinEngine5537 = 65848
	BerlinEngine8009 = 65849
	BerlinEngineSupplyPressureExceedsMaxAllowedValue = 65850
	BerlinEngineSupplyTemperatureExceedsMaxAllowedValue = 65851
	BerlinEngineMaxSupplyPressureExceedsMaxAllowedValue = 65852
	BerlinEngineMaxSupplyTemperatureExceedsMaxAllowedValue = 65853
	BerlinEngineNodePressureExceedsMaxAllowedValue = 65854
	BerlinEngineRoughnessCannotBeNegative = 65855
	BerlinEngineNumberOfNotConvergingNodes = 65856
	sisHYDNoPipeTypesDefined = 65857
	sisHYDPipeWithDefaultPipeType = 65858
	MSXEngineInputFileOpenError = 66000
	MSXEngineResultFileOpenError = 66001
	MSXEngineResultFileReadError = 66002
	MSXEngineInputFileReadError = 66003
	MSXEngineTooFewPipeReactions = 66004
	MSXEngineTooFewTankReactions = 66005
	MSXEngineCouldNotOpenDifferentialEquationSolver = 66006
	MSXEngineCouldNotOpenAlgebraicSolver = 66007
	MSXEngineCouldNotOpenBinaryResultsFile = 66008
	MSXEngineCouldNotReadOrWriteBinaryResultsFile = 66009
	MSXEngineCouldNotIntegrateReactionRateExpressions = 66010
	MSXEngineCouldNotSolveReactionEquilibriumExpressions = 66011
	MSXEngineReferenceToUnknownObjecttype = 66012
	MSXEngineReferenceToIllegalObjectIndex = 66013
	MSXEngineReferenceToUndefinedObjectID = 66014
	MSXEngineInvalidPropertyValues = 66015
	MSXEngineCouldNotCompileChemistryFunctions = 66016
	MSXEngineCouldNotLoadFunctionsFromCompiledChemistryFile = 66017
	MSXEngineIllegalMathOperation = 66018
	MSXEngineErrorCheckModel = 66020
	MSXEngineTooManyCharacters = 66025
	MSXEngineTooFewInputItems = 66026
	MSXEngineInvalidKeyword = 66027
	MSXEngineInvalidNumericValue = 66028
	MSXEngineReferenceToUndefinedObject = 66029
	MSXEngineIllegalUseOfReservedName = 66030
	MSXEngineNameAlreadyUsedByAnotherObject = 66031
	MSXEngineSpeciesAlreadyAssignedAnExpression = 66032
	MSXEngineIllegalMathExpression = 66033
	MSXEngineTermContainsCylicReference = 66034
	MSXEngineIllegalMathOperationForTerm = 66035
	MSXEngineIllegalMathOperationInExpression = 66036
	MSXEngineTooManyTokens = 66037
	MSXLoaderReferenceToDeletedMSXSetup = 66040
	MSXLoaderReferenceToUndefinedMSXSetup = 66041
	MSXLoaderEmptyMSXSetup = 66042
	MSXLoaderMissingModelConfiguration = 66043
	MSXLoaderEmptyModelConfiguration = 66044
	EABillingPeriodMustBePositive = 67000
	EACannotCalculateWithADeletedScenario = 67001
	EAEnergyCostsNotComputed = 67002
	EAMustDefinePowerMeters = 67003
	EAMustSelectAtLeastOneScenario = 67004
	EANumberOfPeriodsMustBePositive = 67005
	EAScenarioMustBeEPSType = 67006
	EAScenarioNotComputed = 67007
	EAScenarioWeightsDontAddUpToHundred = 67008
	EAPercentCostShouldNotBeNegative = 67009
	EAPercentTypeCostsShouldNotExceedHundred = 67010
	EAPowerMeterHasNoEnergyElementsAssociated = 67011
	EAPricingForPowerMeterIsDifferentFromOneOfAssociatedPumps = 67012
	EAEnergyPricesCannotBeNegative = 67013
	EAInterestRateMustBeBetween0And100 = 67014
	EABasePowerMustBePositive = 67015
	EAPatternForNonPumpingElementIsUndefined = 67017
	EAPricingPatternForPowerMeterIsInvalid = 67018
	EAPricingPatternForPowerMeterIsUndefined = 67019
	EAEnergyElementIsInvalid = 67020
	EAEnergyElementIsUndefined = 67021
	EAEnergyPricingAboveRangePriceMustBePositive = 67022
	EAEnergyPricingBillingDemandMustBePositive = 67023
	EABlockRateEnergyUseMustBeIncreasing = 67024
	EABlockRateMustHaveAtLeastOnePoint = 67025
	EAPeakDemandChargeMustBePositive = 67026
	EAPatternCannotContainDuplicateTimes = 67027
	EAFirstPointInPatternCannotHaveATimeOfZero = 67028
	EALastTimeInPatternMustMatchStartingValue = 67029
	EANotEnoughPointsInPattern = 67030
	EAPatternPointsOutOfOrder = 67031
	EAAdvancedPeakChargesOverlap = 67032
	EAAdvancedPeakChargesOutsideRange = 67033
	EAAdvancedPeakChargeBackToFrontAndIgnored = 67034
	EAUsingAdvancedPeakChargesButNoneSpecified = 67035
	ScadaElementInvalidTargetElement = 67500
	ScadaElementUndefinedTargetElement = 67501
	ScadaElementUndefinedTargetAttribute = 67502
	ScadaElementLowLowAlarmRaised = 67503
	ScadaElementLowAlarmRaised = 67504
	ScadaElementHighAlarmRaised = 67505
	ScadaElementHighHighAlarmRaised = 67506
	AlertMessageUndefinedElementType = 67507
	AlertMessageInvalidReferencedIncludeSelectionSet = 67508
	AlertMessageUndefinedReferencedIncludeSelectionSet = 67509
	AlertMessageUndefinedCriterionFieldName = 67510
	AlertMessageUndefinedCriterionOperator = 67511
	AlertMessageUnknownMessageKey = 67512
	AlertMessageEqualRaised = 67513
	AlertMessageNotEqualRaised = 67514
	AlertMessageGreaterThanRaised = 67515
	AlertMessageGreaterThanOrEqualRaised = 67516
	AlertMessageLessThanRaised = 67517
	AlertMessageLessThanOrEqualRaised = 67518
	AlertMessageSummaryEqualRaised = 67519
	AlertMessageSummaryNotEqualRaised = 67520
	AlertMessageSummaryGreaterThanRaised = 67521
	AlertMessageSummaryGreaterThanOrEqualRaised = 67522
	AlertMessageSummaryLessThanRaised = 67523
	AlertMessageSummaryLessThanOrEqualRaised = 67524
	ScadaElementInvalidTargetAttribute = 67525
	ScadaElementActiveAlarmNotAllowedForTargetAttribute = 67526
	EAPatternForNonPumpingElementIsInvalid = 67716
	MohidNotSetUpForVariableRainData = 68001
	AccessDeniedTo2DDataFilesForUrbanFlood = 68002
	UnsupportedRainfallType = 68003
	UnsupportedRainFileType = 68004
	NoRainfallOccursDuringSimulation = 68005
	RainfileContainsBadData = 68006
	GridElementInvalidGeometry = 68025
	GridElementInvalidGridCellSize = 68026
	GridElementInvalidGridAngle = 68027
	GridHasInvalidTerrain = 68028
	GridElementDefaultManningsInvalid = 68029
	GridElementDefaultCNInvalid = 68030
	GridElementDefaultImpFactorInvalid = 68031
	GriddedManningsInvalid = 68032
	GriddedCNInvalid = 68033
	GriddedImpFactorInvalid = 68034
	GriddedGroundElevationWarning = 68035
	GridAdjustmentIntersectsOnlyVoidSpace = 68036
	GridAdjustmentPartiallyIntersectsVoidSpace = 68037
	GridAdjustmentPartiallyOutsideGrid = 68038
	GridAdjustmentElementHasNoAdjustments = 68039
	GridAdjustmentElementNotInGrid = 68040
	GridAdjustmentAreaTooSmall = 68041
	GridAdjustmentAreaIsComplex = 68042
	GridAdjustmentAreaIsMultiRing = 68043
	GridAdjustmentLineIsLooped = 68044
	GridAdjustmentAreaHasNoOverlapWithCellCenters = 68045
	GridAdjustmentInGridButNoCellsFound = 68046
	GridAdjustmentAreaIntersectsOnlyVoidSpace = 68047
	GridBreaklineHasZeroElevationPt = 68048
	GridBreaklineHasInvalidElevationPt = 68049
	GridDataInputManningsInvalid = 68050
	GridDataInputCNInvalid = 68051
	GridDataInputSetToInvalidGroundElevation = 68052
	GridDataInputImpFactorInvalid = 68053
	GridDataInputManningsInvalidWithFileName = 68054
	GridDataInputCNInvalidWithFileName = 68055
	GridDataInputSetToInvalidGroundElevationWithFileName = 68056
	GridDataInputImpFactorInvalidWithFileName = 68057
	GridDataInputRelativeElevGreaterThanZeroWithFileName = 68058
	GridDataExternalLayerLookupValuesAreMissing = 68059
	GridDataExternalLayerFieldUnitNotSet = 68060
	GridDataExternalLayerFileIsMissing = 68061
	GridDataExternalLayerSourceFieldIsNotSet = 68062
	GridDataExternalLayerUserDefinedValueInvalid = 68063
	GridRoadCenterlineHasBiggerWThanL = 68064
	LandCoverCatalogReferenceMissing = 68065
	GridElementDeletedOrInactive = 68066
	GriddedLayersInvalidRunValidateInfoMsg = 68077
	GridCrossSectionTrapezoidalInvalid = 68088
	GridCrossSectionIrregularNotEnoughPoints = 68089
	GridChannelBurnInDoesntAllTributary = 68090
	GridCrossSectionIrregularGeomInvalid = 68091
	GridCrossSectionCatalogTrapezoidalInvalid = 68092
	GridCrossSectionCatalogIrregularInvalid = 68093
	GridCrossSectionCatalogDimensionsInvalid = 68094
	GridCrossSectionCatalogRefMissing = 68095
	CatchmentDoesNotIntersectLandUseAreaInfoMsg = 68096
	LandUseAreasOverlapAndLastOneCreatedWins = 68097
	LandUseAreaIsSetToNone = 68098
	GridBoundaryIntersectsOnlyVoidSpace = 68099
	GridBoundaryLinePartiallyIntersectsVoidSpace = 68100
	GridBoundaryLinePartiallyOutsideGrid = 68101
	GridBoundaryElementNotInGrid = 68102
	CatchmentToElevationBoundary = 68103
	GridElementInitialDepthInvalid = 68104
	GridCalcOptionMaxCourantNumberInvalid = 68105
	GridCalcOptionMaxVolumeVariationInvalid = 68106
	GridCalcOptionMaxIterationsInvalid = 68107
	GridDataExternalLayerLookupTableEmpty = 68108
	GridDataExternalLayerLayerTypeNotSet = 68109
	GridDataExternalLayerNoAspectSelected = 68110
	GridHasMultipleTerrainsForAutoMode = 68111
	GridHasMultipleGridElementsForAutoMode = 68112
	UrbanBoundaryNoFlowAssigned = 68113
	GridChannelBankStationIsOutsideofGrid = 68114
	GridSectionBankIsOutsideOfGridPolygon = 68115
	GridChannelBankDoesNotIntersectGrid = 68116
	GridChannelCrossSectionIsSmallerThanGridSpacing = 68117
	GridMultipleChannelsIntersectSameGridArea = 68118
	TwoDSwmmStepMustBeCompatibleWithGridStep = 68119
	TwoDMinDepthOptionsInvalid = 68120
	TwoDFloodPeriodDepthLessThanMinDepthOption = 68121
	GridPondIsNotEntirelyInTheGrid = 68122
	GridPondAreaIsDifferentThanScaledArea = 68123
	GridCellToBeSetByMultipleRims = 68124
	GridHasClosedBoundaryAndAllowInflowIsIgnored = 68125
	GridElevBoundaryLineIntersectsInteriorCells = 68126
	GridElevBoundaryLineIsLowerThanGridCells = 68127
	GridPotentialCatchmentDoubleCount = 68128
	GridTwoDCalcCapturesFullFlow = 68129
	GridCoupledToGutters = 68130
	GridBurningInPondFailedCheckPondDimensions = 68132
	GridFlowBoundaryLineIntersectsVoidCells = 68133
	GridChannelTerminatesTooCloseToBorder = 68134
	GridWillOverrideTheOutfallsBoundaryCondition = 68135
	GridWillIgnoreOutfallRouteToCatchmentID = 68136
	GridMaxTerrainBoundaryElevationLowerThanGrid = 68137
	GridBoundaryTailwaterElevationLowerThanGrid = 68138
	GridBoundaryTailwaterElevationLowerThanMaxTerrain = 68139
	GridGenerationNoActivateGridElement = 68140
	GridBoundaryTailwaterElevationIsTooLarge = 68141
	GridCrossSectionIsSmallerThanGridSpacing = 68142
	GridMultipleIncomingTributaries = 68143
	FDNodeDepthLessThanMinDepth = 70000
	FDNodeDepthGreaterThanMaxDepth = 70001
	FDConduitRiseLessThanMinSize = 70002
	FDConduitRiseGreaterThanMaxSize = 70003
	NumberOfPointsExceedsMaximum = 200079
	DMWCulvertWithOvertoppingWeir = 200118
	SwmmBulkCatchmentLossMethodNotCalcOptions = 201241
	SwmmCatchmentLossMethodNotCalcOptions = 201242
	SwmmInconsistenSuctionElements = 201243
	SwmmStopStructuresIgnored = 201244
	SwmmInterfaceRainfallFileNotExist = 201245
	SwmmInterfaceRunoffFileNotExist = 201246
	SwmmInterfaceRdiiFileNotExist = 201247
	SwmmInterfaceHotStartFileToUseNotExist = 201248
	SwmmInterfaceInflowFileNotExist = 201249
	SwmmInterfaceRainfallFileEmpty = 201250
	SwmmInterfaceRunoffFileEmpty = 201251
	SwmmInterfaceRdiiFileEmpty = 201252
	SwmmInterfaceHotStartFileToSaveEmpty = 201253
	SwmmInterfaceHotStartFileToUseEmpty = 201254
	SwmmInterfaceInflowFileEmpty = 201255
	SwmmInterfaceOutflowFileEmpty = 201256
	SwmmMoreThanOneDiversionLinkOffOfNode = 201257
	DmwGuhTimeNotIncreasing = 210561
	DMWWeirOvertoppingDepth = 360341
	DMWWeirMaxTailwaterLessDownCulvertInvEl = 360342
	DWMWeirInvElLessCulvertUpstreamTopEl = 360343
	STMUKMDXClosedConduitPortionHasTooManyPoint = 444500
	PMNoTargetHydrograph = 600005
	SwmmDiversionsIgnoredForDynamicRun = 800000
	SwmmInletAssumesOnGrade = 800001
	SwmmNoBypassGutterForOnGradeInlet = 800002
	SwmmSanitaryUnitCountZero = 800003
	SwmmHydrographInCollectionHasZeroPoints = 800004
	SwmmVSBPExportedAsRegularPump = 800005
	SwmmInvalidCharacterInLabel = 800006
	SwmmEvaporationTimeSeriesInvalid = 800007
	SwmmPondOutletStructuresAssumesFreeOutfall = 800008
	SwmmPollutographAndWetWeatherInflow = 800009
	SwmmElementReferencesEmptyPattern = 800010
	SwmmPondSeepageTypeNotSupport = 800011
	SwmmLateralConnectedToVirtualConduit = 800012
	SwmmNetworkNodeConnectedtToMoreThanOneLateral = 800013
	SwmmInvalidFractionValue = 800014
	SwmmInvalidCulvertCode = 800015
	SwmmConduitHasMismatchingCulvertsCoefficients = 800016
	SwmmCulvertCodeShapeDoesNotMatchCulvertInletShape = 800017
	SwmmCatchmentOutflowTargetNotUsingEpaSwmmRunoffMethod = 800018
	SwmmLIDUnderdrainTargetNotUsingEpaSwmmRunoffMethod = 800019
	SwmmLIDUnderdrainTargetNotSupported = 800020
	SwmmLIDHasMissingParentCatchment = 800021
	SwmmLIDUnderdrainTargetNotUsingSameRunoffMethodAsParentCatchment = 800022
	SwmmLIDFieldCapacityMustBeLessThanSoilPorosity = 800023
	SwmmLIDVegetativeCoverFractionInvalid = 800024
	SwmmLIDSurfaceManningsNTooLarge = 800025
	SwmmLIDSurfaceSlopeTooLarge = 800026
	SwmmLIDSoilPorosityInvalid = 800027
	SwmmLIDFieldCapacityInvalid = 800028
	SwmmLIDWiltingPointInvalid = 800029
	SwmmLIDSoilConductivityTooLarge = 800030
	SwmmLIDSoilConductivitySlopeTooLarge = 800031
	SwmmLIDSuctionHeadTooLarge = 800032
	SwmmLIDStorageVoidRatioInvalid = 800033
	SwmmLIDStorageConductivityInvalid = 800034
	SwmmLIDStorageCloggingFactorInvalid = 800035
	SwmmRouteToCatchmentRunoffMethodMustBeEPASWMM = 800036
	SwmmLIDDrainExponentOutOfRange = 800037
	SwmmLIDWiltingPointMustBeLessThanSoilPorosity = 800038
	SwmmPumpHasNonVirtualPumpLink = 800039
	SwmmLIDUnderdrainTargetUnassigned = 800040
	SwmmClimateFileConverted = 800041
	SwmmCollectionFieldCannotDecrease = 800042
	SwmmInvertAboveTopOfTheNode = 800043
	SwmmInvalidEventsDateTime = 800044
	SwmmEventsOutsideRangeOfCalc = 800045
	SwmmNoGlobalStormEventFor2DCalc = 800046
	Swmm2DCalcOnlySupportIntansityTypeRaifall = 800047
	SwmmControlStructureMustLinkToStorageForNonDynamicRouting = 800048
	SwmmWeirTopElevationIsLessThanOrEqualToBottomElevation = 800049
	SwmmEpaTractiveStressNotSupported = 800050
	SwmmEpaH2SNotSupported = 800051
	SwmmEpaNodeHeadlossNotSupported = 800052
	SwmmPumpWrongDirection = 800053
	SwmmSelfRefCatchmentHasNoGroundwater = 800054
	SwmmMissingReference = 800055
	SwmmForecastedRainfallNotSupported = 800056
	SwmmDepthIntensityCurveNotSupported = 800057
	SwmmRainFile2DIgnored = 800058
	SwmmRainFileApplicableRangeOnly = 800059
	SwmmForecastedRainfallNotSupported2 = 800060
	SwmmStartStopControlStructuresRestriction = 800061
	SwmmSweepStartTimeGreaterThanStopTime = 800062
	SWMMExternalTimeSeriesDataFilePathInvalid = 800063
	SWMMInvalidMoistureDeficitData = 800064
	SwmmMissingNodeReference = 805000
	SwmmStorageUnitHasSeepageAndRDII = 805001
	SwmmConduitControlUsedByMoreThanOneElement = 805002
	SwmmConduitControlHasDuplicateLabel = 805003
	SwmmMissingPatternReference = 805004
	SwmmLIDPollutantRemovalNotSupported = 805005
	PpkOutletStructureEQTWTableNotSpecified = 2000025
	PpkOutletStructureHWStepInvalid = 2000028
	PpkOutletStructureTailwaterChannelNotSpecified = 2000029
	PpkOutletStructureOrificeNumberOpeningsInvalid = 2000030
	PpkOutletStructureOrificeCoefficientInvalid = 2000031
	PpkOutletStructureOrificeAreaInvalid = 2000032
	PpkOutletStructureOrificeAreaDatumLowerInvert = 2000033
	PpkOutletStructureOrificeAreaTopElevationBelowEqualInvert = 2000034
	PpkOutletStructureIDInvalid = 2000035
	PpkOutletStructureDownstreamIDInvalid = 2000036
	PpkOutletStructureOrificeCircularDiameterInvalid = 2000037
	PpkOutletStructureCulvertNumberBarrelsInvalid = 2000038
	PpkOutletStructureCulvertWidthInvalid = 2000039
	PpkOutletStructureCulvertHeightInvalid = 2000040
	PpkOutletStructureCulvertLengthInvalid = 2000041
	PpkOutletStructureCulvertManningsNInvalid = 2000042
	PpkOutletStructureCulvertKCoefficientInvalid = 2000043
	PpkOutletStructureCulvertMCoefficientInvalid = 2000044
	PpkOutletStructureCulvertCCoefficientInvalid = 2000045
	PpkOutletStructureCulvertYCoefficientInvalid = 2000046
	PpkOutletStructureCulvertToleranceInvalid = 2000047
	PpkOutletStructureCulvertNumberCrossSectionsInvalid = 2000048
	PpkOutletStructureCulvertDiameterInvalid = 2000049
	PpkOutletStructureWeirLengthInvalid = 2000050
	PpkOutletStructureWeirCoefficientInvalid = 2000051
	PpkOutletStructureStandPipeDiameterInvalid = 2000052
	PpkOutletStructureRiserTransitionElevationInvalid = 2000053
	PpkOutletStructureWeirDepthCoefficientIDInvalid = 2000054
	PpkOutletStructureWeirSubmergenceIDInvalid = 2000055
	PpkOutletStructureVNotchAngleInvalid = 2000056
	PpkOutletStructureWeirCrosSectionOrderInvalid = 2000057
	PpkOutletStructureCrossSectionWeirMaxElevationInvalid = 2000058
	PpkOutletStructureCrossSectionWeirMaxElevationInvalidLower = 2000059
	PpkOutletStructureHWPondNotSpecified = 2000060
	PpkOutletStructureTWMinQTolInvalid = 2000061
	PpkOutletStructureTWMinHWTolInvalid = 2000062
	PpkOutletStructureTWStepInvalid = 2000063
	PpkOutletStructureCulvertDownstreamInvertLessChannelInvert = 2000064
	PpkOutletStructureTWPondNotSpecified = 2000065
	PpkOutletStructureRatingTableOutOfRange = 2000066
	PpkOutletStructureRatingTableMaxOutOfRange = 2000067
	PpkOutletStructureMinHWGreaterThanEqualMaxHW = 2000068
	PpkOutletStructureHWCountExceeded = 2000069
	PpkOutletStructureHWPondHasNoVolume = 2000070
	PpkOutletStructureTWPondHasNoVolume = 2000071
	PpkOutletStructureRatingTableWithNoFreeOutfall = 2000072
	PpkOutletStructureRatingTableNoItems = 2000073
	PpkOutletStructureTWCountExceeded = 2000074
	PpkOutletStructureTWIterationsInvalid = 2000075
	PpkOutletStructureTWEpsMinInvalid = 2000076
	PpkOutletStructureTWEpsMinMaxInvalid = 2000077
	PpkOutletStructureQEpsMinInvalid = 2000078
	PpkOutletStructureQEpsMinMaxInvalid = 2000079
	PpkOutletStructureTWIncrementInvalid = 2000080
	PpkOutletStructureRatingTableSectionOrderInvalid = 20000516
	PpkOutletStructureRatingTableMinBelowHWMin = 20000535
	PpkOutletStructureRatingTableMaxAboveHWMax = 20000536

class NotificationLevel(Enum):
	Status = 0
	Information = 1
	Warning = 2
	Error = 3

class SourceKeys:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class MessageKeyMapIds:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

class GenericProcessInProgress(IProcessInProgress):

	def __new__(self, name: str, label: str, allowCancel: bool) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name
			label (`str`) :  label
			allowCancel (`bool`) :  allowCancel
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

	def FinishProcess(self) -> None:
		"""No Description

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
	def AllowCancel(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
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

class GenericProcessInProgressEx(IProcessInProgressEx):

	def __new__(self, name: str, label: str, allowCancel: bool) -> None:
		"""No Description

		Args
		--------
			name (`str`) :  name
			label (`str`) :  label
			allowCancel (`bool`) :  allowCancel
		"""
		pass

	def UpdateProcess(self, description: str, progress: int) -> None:
		"""No Description

		Args
		--------
			description (`str`) :  description
			progress (`int`) :  progress

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

	def FinishProcess(self) -> None:
		"""No Description

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

	@property
	def IsAborted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsAborted.setter
	def IsAborted(self, isaborted: bool) -> None:
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
	def AllowCancel(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
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

class IMessageHandler:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ShowWarning(self, astringMessage: str) -> None:
		"""No Description

		Args
		--------
			astringMessage (`str`) :  astringMessage

		Returns
		--------
			`None` : 
		"""
		pass

class IMessageQuestionHandler(IMessageHandler):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ShowQuestion(self, question: str, caption: str, allowCancel: bool) -> MessageHandlerResult:
		"""No Description

		Args
		--------
			question (`str`) :  question
			caption (`str`) :  caption
			allowCancel (`bool`) :  allowCancel

		Returns
		--------
			`MessageHandlerResult` : 
		"""
		pass

class IStoredResponseMessageQuestionHandler(IMessageQuestionHandler):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ShowQuestion(self, key: PromptKey, defaultResult: MessageHandlerResult, question: str, caption: str, allowCancel: bool) -> MessageHandlerResult:
		"""No Description

		Args
		--------
			key (`PromptKey`) :  key
			defaultResult (`MessageHandlerResult`) :  defaultResult
			question (`str`) :  question
			caption (`str`) :  caption
			allowCancel (`bool`) :  allowCancel

		Returns
		--------
			`MessageHandlerResult` : 
		"""
		pass

	@overload
	def ShowQuestion(self, question: str, caption: str, allowCancel: bool) -> MessageHandlerResult:
		"""No Description

		Args
		--------
			question (`str`) :  question
			caption (`str`) :  caption
			allowCancel (`bool`) :  allowCancel

		Returns
		--------
			`MessageHandlerResult` : 
		"""
		pass

class ExceptionEventHandler(ICloneable, ISerializable):

	def __new__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args
		--------
			object (`object`) :  object
			method (`IntPtr`) :  method
		"""
		pass

	def Invoke(self, sender: object, e: ExceptionEventArgs) -> None:
		"""No Description

		Args
		--------
			sender (`object`) :  sender
			e (`ExceptionEventArgs`) :  e

		Returns
		--------
			`None` : 
		"""
		pass

	def BeginInvoke(self, sender: object, e: ExceptionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args
		--------
			sender (`object`) :  sender
			e (`ExceptionEventArgs`) :  e
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

class IProcessInProgress(INamable, ILabeled):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
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
	def AllowCancel(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class ExceptionEventArgs:

	def __new__(self, exceptionMsg: str) -> None:
		"""No Description

		Args
		--------
			exceptionMsg (`str`) :  exceptionMsg
		"""
		pass

	@property
	def ExceptionMessage(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Handled(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@Handled.setter
	def Handled(self, handled: bool) -> None:
		pass

class IProcessInProgressEx(IProcessInProgress):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def UpdateProcess(self, description: str, progress: int) -> None:
		"""No Description

		Args
		--------
			description (`str`) :  description
			progress (`int`) :  progress

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def IsAborted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

class IProgressIndicator:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddTask(self, alabel: str) -> ProgressIndicatorTask:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`ProgressIndicatorTask` : 
		"""
		pass

	def IncrementTask(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def BeginTask(self, anumsteps: int) -> None:
		"""No Description

		Args
		--------
			anumsteps (`int`) :  anumsteps

		Returns
		--------
			`None` : 
		"""
		pass

	def IncrementStep(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def EndTask(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def Done(self) -> None:
		"""No Description

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

	@property
	def Tasks(self) -> List:
		"""No Description

		Returns
		--------
			`List` : 
		"""
		pass

	@Tasks.setter
	def Tasks(self, tasks: List) -> None:
		pass

	@property
	def Task(self) -> ProgressIndicatorTask:
		"""No Description

		Returns
		--------
			`ProgressIndicatorTask` : 
		"""
		pass

	@property
	def IsAborted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsAborted.setter
	def IsAborted(self, isaborted: bool) -> None:
		pass

	@property
	def ElapsedTime(self) -> TimeSpan:
		"""No Description

		Returns
		--------
			`TimeSpan` : 
		"""
		pass

	@CancelText.setter
	def CancelText(self, canceltext: str) -> None:
		pass

	@CanCancel.setter
	def CanCancel(self, cancancel: bool) -> None:
		pass

class IUserNotification(ILabeled):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MessageId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def ElementId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def ElementType(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def HelpId(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Level(self) -> NotificationLevel:
		"""No Description

		Returns
		--------
			`NotificationLevel` : 
		"""
		pass

	@property
	def MessageKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def Parameters(self) -> List[object]:
		"""No Description

		Returns
		--------
			`List[object]` : 
		"""
		pass

	@property
	def ScenarioId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def SourceKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@property
	def WorkingUnits(self) -> List[Unit]:
		"""No Description

		Returns
		--------
			`List[Unit]` : 
		"""
		pass

	@property
	def NumericFormatterKeys(self) -> array[str]:
		"""No Description

		Returns
		--------
			`array[str]` : 
		"""
		pass

	@property
	def HasSubUserNotifications(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@HasSubUserNotifications.setter
	def HasSubUserNotifications(self, hassubusernotifications: bool) -> None:
		pass

	@property
	def ExcludeFromDuplicateProcessing(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ExcludeFromDuplicateProcessing.setter
	def ExcludeFromDuplicateProcessing(self, excludefromduplicateprocessing: bool) -> None:
		pass

class ICalculationUserNotification(IUserNotification):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeStepIndex(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class IObjectValidater:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Validate(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def IsValid(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def UserNotifications(self) -> List:
		"""No Description

		Returns
		--------
			`List` : 
		"""
		pass

class IStatusManager:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddInfoMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddErrorMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddWarningMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	@overload
	def IncrementStatistics(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def IncrementStatistics(self, alabel: str, incrementAmount: int) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
			incrementAmount (`int`) :  incrementAmount

		Returns
		--------
			`None` : 
		"""
		pass

class IYesNoToAllPrompt:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ShowMessage(self) -> DialogYesNoToAllResult:
		"""No Description

		Returns
		--------
			`DialogYesNoToAllResult` : 
		"""
		pass

	@Title.setter
	def Title(self, title: str) -> None:
		pass

	@Message.setter
	def Message(self, message: str) -> None:
		pass

	@DefaultButton.setter
	def DefaultButton(self, defaultbutton: DialogYesNoToAllResult) -> None:
		pass

class NullMessageHandler(IMessageHandler):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def ShowWarning(self, message: str) -> None:
		"""No Description

		Args
		--------
			message (`str`) :  message

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def ShowWarning(self, astringMessage: str) -> None:
		"""No Description

		Args
		--------
			astringMessage (`str`) :  astringMessage

		Returns
		--------
			`None` : 
		"""
		pass

class NullProgressIndicator(IProgressIndicator):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def AddTask(self, alabel: str) -> ProgressIndicatorTask:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`ProgressIndicatorTask` : 
		"""
		pass

	def BeginTask(self, anumsteps: int) -> None:
		"""No Description

		Args
		--------
			anumsteps (`int`) :  anumsteps

		Returns
		--------
			`None` : 
		"""
		pass

	def Done(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def EndTask(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def IncrementStep(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def IncrementTask(self) -> None:
		"""No Description

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

	def Hide(self) -> None:
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

	@property
	def IsAborted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsAborted.setter
	def IsAborted(self, isaborted: bool) -> None:
		pass

	@CancelText.setter
	def CancelText(self, canceltext: str) -> None:
		pass

	@CanCancel.setter
	def CanCancel(self, cancancel: bool) -> None:
		pass

	@property
	def ElapsedTime(self) -> TimeSpan:
		"""No Description

		Returns
		--------
			`TimeSpan` : 
		"""
		pass

	@property
	def Task(self) -> ProgressIndicatorTask:
		"""No Description

		Returns
		--------
			`ProgressIndicatorTask` : 
		"""
		pass

	@property
	def Tasks(self) -> List:
		"""No Description

		Returns
		--------
			`List` : 
		"""
		pass

	@Tasks.setter
	def Tasks(self, tasks: List) -> None:
		pass

class ProgressIndicatorTask:

	def __new__(self, alabel: str, aintsteps: int) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
			aintsteps (`int`) :  aintsteps
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
	def Steps(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Steps.setter
	def Steps(self, steps: int) -> None:
		pass

	@property
	def IsCompleted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsCompleted.setter
	def IsCompleted(self, iscompleted: bool) -> None:
		pass

class ReportManager:

	def __new__(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
		"""
		pass

	def GetSection(self, alabel: str) -> ReportSection:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`ReportSection` : 
		"""
		pass

	def DeleteSection(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`None` : 
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
	def Sorted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@Sorted.setter
	def Sorted(self, sorted: bool) -> None:
		pass

	@property
	def Sections(self) -> List:
		"""No Description

		Returns
		--------
			`List` : 
		"""
		pass

class ReportSection(IComparable):

	def __new__(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
		"""
		pass

	def SetItem(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`None` : 
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
	def Sorted(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@Sorted.setter
	def Sorted(self, sorted: bool) -> None:
		pass

	@property
	def Items(self) -> List:
		"""No Description

		Returns
		--------
			`List` : 
		"""
		pass

class ReportSectionItem(IComparable):

	def __new__(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
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

class StatisticsManager:

	def __new__(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
		"""
		pass

	def GetSection(self, alabel: str) -> StatisticsSection:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`StatisticsSection` : 
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
	def Sections(self) -> SortedList:
		"""No Description

		Returns
		--------
			`SortedList` : 
		"""
		pass

class StatisticsSection:

	def __new__(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
		"""
		pass

	@overload
	def IncrementItem(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def IncrementItem(self, alabel: str, incrementAmount: int) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
			incrementAmount (`int`) :  incrementAmount

		Returns
		--------
			`None` : 
		"""
		pass

	def SetItemCount(self, alabel: str, acount: int) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
			acount (`int`) :  acount

		Returns
		--------
			`None` : 
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
	def Items(self) -> SortedList:
		"""No Description

		Returns
		--------
			`SortedList` : 
		"""
		pass

class StatisticsSectionItem:

	def __new__(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
		"""
		pass

	def Increment(self) -> None:
		"""No Description

		Returns
		--------
			`None` : 
		"""
		pass

	def IncrementByAmount(self, incrementAmount: int) -> None:
		"""No Description

		Args
		--------
			incrementAmount (`int`) :  incrementAmount

		Returns
		--------
			`None` : 
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
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@Count.setter
	def Count(self, count: int) -> None:
		pass

class StatusManager(IStatusManager):

	def __new__(self, alabel: str, adescription: str, aprogress: IProgressIndicator) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
			adescription (`str`) :  adescription
			aprogress (`IProgressIndicator`) :  aprogress
		"""
		pass

	def AddMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddInfoMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddErrorMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddWarningMessage(self, anid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			anid (`int`) :  anid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	@overload
	def IncrementStatistics(self, alabel: str) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def IncrementStatistics(self, alabel: str, incrementAmount: int) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
			incrementAmount (`int`) :  incrementAmount

		Returns
		--------
			`None` : 
		"""
		pass

	@overload
	def IncrementStatistics(self, alabel: str, incrementAmount: int) -> None:
		"""No Description

		Args
		--------
			alabel (`str`) :  alabel
			incrementAmount (`int`) :  incrementAmount

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Description(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

	@property
	def DateStamp(self) -> datetime:
		"""No Description

		Returns
		--------
			`datetime` : 
		"""
		pass

	@property
	def ElapsedTimeMessage(self) -> str:
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

	@property
	def ProgressIndicator(self) -> IProgressIndicator:
		"""No Description

		Returns
		--------
			`IProgressIndicator` : 
		"""
		pass

	@property
	def StatisticsManager(self) -> StatisticsManager:
		"""No Description

		Returns
		--------
			`StatisticsManager` : 
		"""
		pass

	@property
	def ReportManager(self) -> ReportManager:
		"""No Description

		Returns
		--------
			`ReportManager` : 
		"""
		pass

	@property
	def MessageManager(self) -> StatusMessageManager:
		"""No Description

		Returns
		--------
			`StatusMessageManager` : 
		"""
		pass

class StatusMessageItem:

	def __new__(self, aelementid: int, amessagetype: StatusMessageTypes, amessage: str) -> None:
		"""No Description

		Args
		--------
			aelementid (`int`) :  aelementid
			amessagetype (`StatusMessageTypes`) :  amessagetype
			amessage (`str`) :  amessage
		"""
		pass

	@property
	def ElementID(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ElementID.setter
	def ElementID(self, elementid: int) -> None:
		pass

	@property
	def MessageType(self) -> StatusMessageTypes:
		"""No Description

		Returns
		--------
			`StatusMessageTypes` : 
		"""
		pass

	@MessageType.setter
	def MessageType(self, messagetype: StatusMessageTypes) -> None:
		pass

	@property
	def Message(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@Message.setter
	def Message(self, message: str) -> None:
		pass

class StatusMessageManager:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def AddMessage(self, aid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			aid (`int`) :  aid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddInfoMessage(self, aid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			aid (`int`) :  aid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddWarningMessage(self, aid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			aid (`int`) :  aid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	def AddErrorMessage(self, aid: int, amessage: str) -> StatusMessageItem:
		"""No Description

		Args
		--------
			aid (`int`) :  aid
			amessage (`str`) :  amessage

		Returns
		--------
			`StatusMessageItem` : 
		"""
		pass

	@property
	def HasMessages(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def HasInfoMessages(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def HasWarningMessages(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def HasErrorMessages(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@property
	def Messages(self) -> List:
		"""No Description

		Returns
		--------
			`List` : 
		"""
		pass

class TraceMessageHandler(IMessageHandler):

	def __new__(self) -> None:
		"""No Description
		"""
		pass

	def ShowWarning(self, astringMessage: str) -> None:
		"""No Description

		Args
		--------
			astringMessage (`str`) :  astringMessage

		Returns
		--------
			`None` : 
		"""
		pass

	@staticmethod
	@property
	def Instance() -> TraceMessageHandler:
		"""No Description

		Returns
		--------
			`TraceMessageHandler` : 
		"""
		pass

class UserNotificationBase(ICalculationUserNotification):

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int, aobjectParameters: List[object], aunitsWorking: List[Unit], astringNumericFormatters: array[str]) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MessageId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def ElementId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ElementId.setter
	def ElementId(self, elementid: int) -> None:
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
	def ElementType(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ElementType.setter
	def ElementType(self, elementtype: int) -> None:
		pass

	@property
	def HelpId(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@HelpId.setter
	def HelpId(self, helpid: str) -> None:
		pass

	@property
	def Level(self) -> NotificationLevel:
		"""No Description

		Returns
		--------
			`NotificationLevel` : 
		"""
		pass

	@Level.setter
	def Level(self, level: NotificationLevel) -> None:
		pass

	@property
	def MessageKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@MessageKey.setter
	def MessageKey(self, messagekey: str) -> None:
		pass

	@property
	def Parameters(self) -> List[object]:
		"""No Description

		Returns
		--------
			`List[object]` : 
		"""
		pass

	@Parameters.setter
	def Parameters(self, parameters: List[object]) -> None:
		pass

	@property
	def ScenarioId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ScenarioId.setter
	def ScenarioId(self, scenarioid: int) -> None:
		pass

	@property
	def SourceKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@SourceKey.setter
	def SourceKey(self, sourcekey: str) -> None:
		pass

	@property
	def WorkingUnits(self) -> List[Unit]:
		"""No Description

		Returns
		--------
			`List[Unit]` : 
		"""
		pass

	@WorkingUnits.setter
	def WorkingUnits(self, workingunits: List[Unit]) -> None:
		pass

	@property
	def NumericFormatterKeys(self) -> array[str]:
		"""No Description

		Returns
		--------
			`array[str]` : 
		"""
		pass

	@NumericFormatterKeys.setter
	def NumericFormatterKeys(self, numericformatterkeys: array[str]) -> None:
		pass

	@property
	def HasSubUserNotifications(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@HasSubUserNotifications.setter
	def HasSubUserNotifications(self, hassubusernotifications: bool) -> None:
		pass

	@property
	def ExcludeFromDuplicateProcessing(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ExcludeFromDuplicateProcessing.setter
	def ExcludeFromDuplicateProcessing(self, excludefromduplicateprocessing: bool) -> None:
		pass

	@property
	def TimeStepIndex(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

class StandardUserNotification(ICalculationUserNotification):

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int, aobjectParameters: List[object]) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int, aobjectParameters: List[object], aunitsWorking: List[Unit], astringNumericFormatters: array[str]) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
		"""
		pass

	@property
	def TimeStepIndex(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def MessageId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def ElementId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ElementId.setter
	def ElementId(self, elementid: int) -> None:
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
	def ElementType(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ElementType.setter
	def ElementType(self, elementtype: int) -> None:
		pass

	@property
	def HelpId(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@HelpId.setter
	def HelpId(self, helpid: str) -> None:
		pass

	@property
	def Level(self) -> NotificationLevel:
		"""No Description

		Returns
		--------
			`NotificationLevel` : 
		"""
		pass

	@Level.setter
	def Level(self, level: NotificationLevel) -> None:
		pass

	@property
	def MessageKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@MessageKey.setter
	def MessageKey(self, messagekey: str) -> None:
		pass

	@property
	def Parameters(self) -> List[object]:
		"""No Description

		Returns
		--------
			`List[object]` : 
		"""
		pass

	@Parameters.setter
	def Parameters(self, parameters: List[object]) -> None:
		pass

	@property
	def ScenarioId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ScenarioId.setter
	def ScenarioId(self, scenarioid: int) -> None:
		pass

	@property
	def SourceKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@SourceKey.setter
	def SourceKey(self, sourcekey: str) -> None:
		pass

	@property
	def WorkingUnits(self) -> List[Unit]:
		"""No Description

		Returns
		--------
			`List[Unit]` : 
		"""
		pass

	@WorkingUnits.setter
	def WorkingUnits(self, workingunits: List[Unit]) -> None:
		pass

	@property
	def NumericFormatterKeys(self) -> array[str]:
		"""No Description

		Returns
		--------
			`array[str]` : 
		"""
		pass

	@NumericFormatterKeys.setter
	def NumericFormatterKeys(self, numericformatterkeys: array[str]) -> None:
		pass

	@property
	def HasSubUserNotifications(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@HasSubUserNotifications.setter
	def HasSubUserNotifications(self, hassubusernotifications: bool) -> None:
		pass

	@property
	def ExcludeFromDuplicateProcessing(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ExcludeFromDuplicateProcessing.setter
	def ExcludeFromDuplicateProcessing(self, excludefromduplicateprocessing: bool) -> None:
		pass

class CalculationUserNotification(ICalculationUserNotification):

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
			aintTimeStepIndex (`int`) :  aintTimeStepIndex
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
			aintTimeStepIndex (`int`) :  aintTimeStepIndex
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
			aintTimeStepIndex (`int`) :  aintTimeStepIndex
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
			aintTimeStepIndex (`int`) :  aintTimeStepIndex
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int, aobjectParameters: List[object]) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
			aintTimeStepIndex (`int`) :  aintTimeStepIndex
		"""
		pass

	@overload
	def __new__(self, aintElementType: int, anotificationlevel: NotificationLevel, astringMessageKey: str, astringSourceKey: str, aintElementId: int, astringHelpId: str, aintScenarioId: int, aobjectParameters: List[object], aunitsWorking: List[Unit], astringNumericFormatters: array[str], aintTimeStepIndex: int) -> None:
		"""No Description

		Args
		--------
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aintElementType (`int`) :  aintElementType
			anotificationlevel (`NotificationLevel`) :  anotificationlevel
			astringMessageKey (`str`) :  astringMessageKey
			astringSourceKey (`str`) :  astringSourceKey
			aintElementId (`int`) :  aintElementId
			astringHelpId (`str`) :  astringHelpId
			aintScenarioId (`int`) :  aintScenarioId
			aobjectParameters (`List[object]`) :  aobjectParameters
			aunitsWorking (`List[Unit]`) :  aunitsWorking
			astringNumericFormatters (`array[str]`) :  astringNumericFormatters
			aintTimeStepIndex (`int`) :  aintTimeStepIndex
		"""
		pass

	@property
	def TimeStepIndex(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def MessageId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@property
	def ElementId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ElementId.setter
	def ElementId(self, elementid: int) -> None:
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
	def ElementType(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ElementType.setter
	def ElementType(self, elementtype: int) -> None:
		pass

	@property
	def HelpId(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@HelpId.setter
	def HelpId(self, helpid: str) -> None:
		pass

	@property
	def Level(self) -> NotificationLevel:
		"""No Description

		Returns
		--------
			`NotificationLevel` : 
		"""
		pass

	@Level.setter
	def Level(self, level: NotificationLevel) -> None:
		pass

	@property
	def MessageKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@MessageKey.setter
	def MessageKey(self, messagekey: str) -> None:
		pass

	@property
	def Parameters(self) -> List[object]:
		"""No Description

		Returns
		--------
			`List[object]` : 
		"""
		pass

	@Parameters.setter
	def Parameters(self, parameters: List[object]) -> None:
		pass

	@property
	def ScenarioId(self) -> int:
		"""No Description

		Returns
		--------
			`int` : 
		"""
		pass

	@ScenarioId.setter
	def ScenarioId(self, scenarioid: int) -> None:
		pass

	@property
	def SourceKey(self) -> str:
		"""No Description

		Returns
		--------
			`str` : 
		"""
		pass

	@SourceKey.setter
	def SourceKey(self, sourcekey: str) -> None:
		pass

	@property
	def WorkingUnits(self) -> List[Unit]:
		"""No Description

		Returns
		--------
			`List[Unit]` : 
		"""
		pass

	@WorkingUnits.setter
	def WorkingUnits(self, workingunits: List[Unit]) -> None:
		pass

	@property
	def NumericFormatterKeys(self) -> array[str]:
		"""No Description

		Returns
		--------
			`array[str]` : 
		"""
		pass

	@NumericFormatterKeys.setter
	def NumericFormatterKeys(self, numericformatterkeys: array[str]) -> None:
		pass

	@property
	def HasSubUserNotifications(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@HasSubUserNotifications.setter
	def HasSubUserNotifications(self, hassubusernotifications: bool) -> None:
		pass

	@property
	def ExcludeFromDuplicateProcessing(self) -> bool:
		"""No Description

		Returns
		--------
			`bool` : 
		"""
		pass

	@ExcludeFromDuplicateProcessing.setter
	def ExcludeFromDuplicateProcessing(self, excludefromduplicateprocessing: bool) -> None:
		pass

class UserNotificationFieldNames:

	def __new__(self) -> None:
		"""No Description
		"""
		pass

