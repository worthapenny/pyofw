from enum import Enum
from System import TypeCode

class IdahoAlternativeTypes(Enum):
	HmiDataSetGeometryAlternative = 1
	HMIDataSetTopologyAlternative = 2
	HMIActiveTopologyAlternative = 3
	PhysicalAlternative = 4
	DemandAlternative = 20
	InitialSettingsAlternative = 21
	OperationalAlternative = 22
	AgeAlternative = 23
	ConstituentAlternative = 24
	TraceAlternative = 25
	FireFlowAlternative = 26
	CapitalCostAlternative = 27
	EnergyCostAlternative = 28
	PressureDependentDemandAlternative = 29
	CriticalityAlternative = 30
	HMIUserDefinedExtensionsAlternative = 100

class DemandTypeEnum(Enum):
	DemandType = 0
	InflowType = 1

class SCADAUnitDemandSourceType(Enum):
	UserDefinedType = 0
	SignalType = 1

class SCADANormalDemandSourceType(Enum):
	UserDefinedType = 0
	SignalType = 1

class TankSectionEnum(Enum):
	CircularTankSectionType = 0
	NonCircularTankSectionType = 1
	VariableAreaTankSectionType = 2

class OperatingRangeTypeEnum(Enum):
	OperatingRange_ElevationType = 0
	OperatingRange_LevelType = 1

class TankMixingModelEnum(Enum):
	TwoCompartmentType = 0
	CompletelyMixedType = 1
	FIFOType = 2
	LIFOType = 3

class ConstituentSourceTypeEnum(Enum):
	ConcentrationType = 0
	FlowPacedBoosterType = 1
	SetpointBoosterType = 2
	MassBoosterType = 3

class ValveSettingEnum(Enum):
	ValveActiveType = 0
	ValveInactiveType = 1
	ValveClosedType = 2

class PressureValveSettingEnum(Enum):
	ValvePressureType = 0
	ValveHGLType = 1

class PumpStatusEnum(Enum):
	PumpOnType = 0
	PumpOffType = 1
	PumpResultCannotDeliverHead = 2
	PumpResultCannotDeliverFlow = 3

class PumpResultControlStatus(Enum):
	PumpResultOnType = 0
	PumpResultOffType = 1
	PumpResultCannotDeliverHeadType = 2
	PumpResultCannotDeliverFlowType = 3

class VSPTypeEnum(Enum):
	PatternBasedType = 0
	FixedHeadType = 1
	FixedFlowType = 2

class PipeStatusEnum(Enum):
	OpenType = 0
	ClosedType = 1

class TurbineStatusEnum(Enum):
	OpenType = 0
	ClosedType = 1

class IdahoDomainElementTypes(Enum):
	IdahoTankElementManager = 52
	IdahoHydrantElementManager = 54
	IdahoJunctionElementManager = 55
	IdahoReservoirElementManager = 56
	FCVElementManager = 60
	TCVElementManager = 61
	GPVElementManager = 62
	PRVElementManager = 64
	PSVElementManager = 65
	PBVElementManager = 66
	StandardPumpElementManager = 68
	IdahoPipeElementManager = 69
	IdahoSpotElevationElementManager = 70
	PressureIsolationValveElementManager = 71
	VariableSpeedPumpBatteryElementManager = 72

class ApplyFireFlowsEnum(Enum):
	AddToBaseLineType = 0
	ReplaceBaselineType = 1

class NumericalEngineTypeEnum(Enum):
	EpaNetEngine = 1

class EpaNetEngine_TimeAnalysisTypeEnum(Enum):
	SteadyStateType = 0
	EpsType = 1

class EpaNetEngine_CalculationTypeEnum(Enum):
	FireFlowType = 0
	FlushingType = 1
	AgeAnalysisType = 2
	ConstituentAnalysisType = 3
	TraceAnalysisType = 4
	HydraulicsOnlyType = 5
	MSXAnalysisType = 6
	SCADAAnalaysisType = 7
	QualityAnalysisType = 8
	CriticalityType = 9999

class EpaNetEngine_WaterQualityAnalysisEnum(Enum):
	NoAnalysisType = 0
	AgeAnalysisType = 1
	ConstituentAnalysisType = 2
	TraceAnalysisType = 3
	AllQualitiesType = 4

class EpaNetEngine_FrictionMethodEnum(Enum):
	DarcyWeisbachType = 0
	HazenWilliamsType = 1
	ManningsType = 2

class EpaNetEngine_EngineCompatibilityEnum(Enum):
	V8iSS2 = 0
	V8iSS1 = 1
	EPANET2_12 = 2
	EPANET2_10 = 3

class EpaNetEngine_OverrideReportingTimeStepEnum(Enum):
	All = 0
	Constant = 1
	Variable = 2

class IsolationValveInitialSettingEnum(Enum):
	IsolationValveOpenType = 0
	IsolationValveClosedType = 1

class SegmentationScopeType(Enum):
	EntireNetwork = 0
	SubsetNetwork = 1

class MinorLossTypeEnum(Enum):
	EntranceType = 0
	BendType = 1
	ContractionType = 2
	CrossType = 3
	ExitType = 4
	ExpansionType = 5
	TeeType = 6
	ValveType = 7
	WyeType = 8

class TCVCoefficientType(Enum):
	Headloss = 1
	Discharge = 2
	ValveCharacteristicsCurve = 3

class ControlValveCoefficientType(Enum):
	Minorloss = 1
	DischargeCoefficient = 2

class BoundaryPumpStatusEnum(Enum):
	PumpOn = 0
	PumpOff = 1

class BoundaryPressureValveStatusEnum(Enum):
	Inactive = 0
	Closed = 1

class BoundaryPipeStatusEnum(Enum):
	PipeOpen = 0
	PipeClosed = 1

class BoundaryGPVStatusEnum(Enum):
	Active = 0
	Closed = 1

class BoundaryTCVStatusEnum(Enum):
	Closed = 0
	Inactive = 1

class BoundaryFCVStatusEnum(Enum):
	Closed = 0
	Inactive = 1

class BoundaryTankAttributeEnum(Enum):
	TankHGL = 0
	TankLevel = 1

class BoundaryPumpAttributeEnum(Enum):
	PumpSetting = 0
	PumpStatus = 1

class BoundaryPressureValveAttributeEnum(Enum):
	ValveSetting = 0
	ValveStatus = 6

class BoundaryTCVAttributeEnum(Enum):
	ValveSetting = 0
	ValveStatus = 1

class BoundaryFCVAttributeEnum(Enum):
	ValveSetting = 0
	ValveStatus = 1

class TargetNodeAttributeEnum(Enum):
	Hgl = 0
	Pressure = 1

class TargetDirectedNodeAttributeEnum(Enum):
	Flow = 0
	HglIn = 1
	HglOut = 2
	PressureIn = 3
	PressureOut = 4

class ObservedTargetElementTypeEnum(Enum):
	TargetNode = 1
	TargetDirectedNode = 2
	TargetPipe = 7

class BoundaryTargetElementTypeEnum(Enum):
	Tank = 0
	Pump = 2
	PressureValve = 3
	GPV = 4
	Pipe = 5
	TCV = 6
	FCV = 7

class InitialTransientPumpStatusEnum(Enum):
	PumpOn = 0
	PumpOff = 1

class RunDurationTypeEnum(Enum):
	TimeSteps = 0
	Times = 1

class ReportPointHistoryTypeEnum(Enum):
	All = 0
	OnlyIfOnPath = 1

class ShowExtremeHeadsAfterEnum(Enum):
	AfterTimeZero = 0
	AfterFirstMaxMin = 1

class TransientFrictionMethodEnum(Enum):
	Steady = 0
	QuasiSteady = 1
	Unsteady = 2
	UnsteadyVitkovsky = 3

class TurbineOperatingCaseEnum(Enum):
	InstantLoadRejection = 0
	LoadRejection = 1
	LoadAcceptance = 2
	LoadVariation = 3

class AirValveTypeEnum(Enum):
	SlowClosing = 0
	DoubleActing = 1
	TripleActing = 2
	VacuumBreaker = 3

class SAV_SRVTypeEnum(Enum):
	SAV = 0
	SRV = 1
	SAVAndSRV = 2

class SAVValveTypeEnum(Enum):
	Needle = 0
	CircularGate = 1
	Global = 2
	Ball = 3
	Butterfly = 4

class SRVControlTypeEnum(Enum):
	SpringLoaded = 0
	TimeBased = 1

class SRVValveTypeEnum(Enum):
	Needle = 0
	CircularGate = 1
	Globe = 2
	Ball = 3
	Butterfly = 4

class RuptureDiskOrificeDefinitionType(Enum):
	Simple = 0
	OrificeEquation = 1

class FlowHeadRelationshipEnum(Enum):
	Simple = 0
	BasicEmitter = 1
	OrificeEquation = 2

class DischargeToAtmosphereTypeEnum(Enum):
	Orifice = 0
	Valve = 1
	RatingCurve = 2

class ValveTypeInitialStatusEnum(Enum):
	Open = 1
	Closed = 2

class HammerPumpTypeEnum(Enum):
	Shutdown = 0
	ConstantSpeedNoPumpCurve = 1
	ConstantSpeedWithPumpCurve = 2
	VSP = 3
	PumpStartVSP = 4

class HammerPumpValveTypeEnum(Enum):
	CheckValve = 0
	ControlValve = 1

class VariableSpeedType_ControlVariableEnum(Enum):
	Speed = 0
	Torque = 1

class SpecificSpeedEnum(Enum):
	Si25_Us1280 = 0
	Si35_Us1800 = 1
	Si94_Us4850 = 2
	Si117_Us6040 = 3
	Si145_Us7500 = 4
	Si208_Us10740 = 5
	Si260_Us13500 = 6

class CheckValveFlowDirectionEnum(Enum):
	TowardsWye = 0
	AwayFromWye = 1

class CheckValveClosureTypeEnum(Enum):
	InstantaneousClosure = 0
	SlowClosure = 1
	DynamicCharacteristicsCurve = 2

class SurgeTankTypeEnum(Enum):
	Simple = 0
	Differential = 1

class TypeOfVolumeEnum(Enum):
	Air = 0
	Vapor = 1

class HammerValveType(Enum):
	Butterfly = 0
	Needle = 1
	CircularGate = 2
	Globe = 3
	Ball = 4
	UserDefined = 5

class TimestepAdjustmentAttribute(Enum):
	Length = 0
	WaveSpeed = 1

class TimestepAdjustmentType(Enum):
	Relative = 0
	Absolute = 1

class GPVTransientBehaviorEnum(Enum):
	Orifice = 0
	Valve = 1

class PeriodicHeadFlowBehaviorEnum(Enum):
	Head = 0
	Flow = 1

class HammerReportPointsEnum(Enum):
	NoPoints = 0
	AllPoints = 1
	SelectedPoints = 2

class HammerReportTimesEnum(Enum):
	Periodically = 0
	AtNoTimes = 1
	AtAllTimes = 2
	AtSpecificTimes = 3

class HammerLevelOfPrecision(Enum):
	Lowest = 0
	Low = 1
	Medium = 2
	High = 3
	Highest = 4

class SavClosureTriggerEnum(Enum):
	Time = 0
	Pressure = 1

class AirValveTransitionType(Enum):
	ByVolume = 0
	ByPressure = 1

class GasVesselLevelType(Enum):
	Fixed = 0
	Mean = 1
	Variable = 2

class HydroTankType(Enum):
	Sealed = 0
	Vented = 1
	DippingTube = 2

class AirFlowCalculationMethod(Enum):
	OrificeDiameter = 0
	AirFlowCurve = 1

class PressureZoneScopeType(Enum):
	EntireNetwork = 0
	NetworkSubset = 1

class FlushingStatus(Enum):
	Open = 0
	Closed = 1
	Target = 2
	Flowing = 3
	Reopen = 4
	Reclose = 5
	OpenPrior = 6
	ClosedPrior = 7

class WaterSCADAField(Enum):
	NullAttribute = 0
	ObservedRelativeClosure = -300
	ObservedConstituentConcentration = -299
	PressureNodeDemand = -297
	TankInitialHGLSetting = -296
	TCValveInitialSetting = -208
	GPValveInitialSetting = -207
	ValveInitialStatus = -201
	PumpInitialSetting = -200
	PumpInitialStatus = -199
	PressurePipeInitialStatus = -198
	VSPTargetHead = -191
	VSPControlNodeID = -189
	ObservedValveStatus = -58
	ObservedPumpStatus = -57
	ObservedPipeStatus = -56
	ObservedTankLevel = -55
	ObservedPressure = -54
	ObservedHydraulicGrade = -53
	ObservedPumpSetting = -52
	ObservedPressureValveSetting = -51
	ObservedTCValveSetting = -50
	ObservedFCValveSetting = -49
	ObservedPressureOut = -48
	ObservedPressureIn = -47
	ObservedHydraulicGradeOut = -46
	ObservedHydraulicGradeIn = -45
	ObservedDischarge = -44
	TankBaseElevation = -39
	Demand = -33
	InitialHGLSetting = -27
	FCValveInitialSetting = -26
	TankActiveVolume = -10
	GroundElevation = -4

class PumpDefinitionTypeEnum(Enum):
	ConstantPowerType = 0
	DesignPointType = 1
	StandardType = 2
	StandardExtendedType = 3
	CustomExtendedType = 4
	MultiplePointType = 5
	VolumeFlow = 6
	DepthFlow = 7
	DepthFlowVariableSpeed = 8

class PumpEfficiencyTypeEnum(Enum):
	ConstantEfficiencyType = 0
	BestEfficiencyPointType = 1
	MultipleEfficiencyPointsType = 2

class WallReactionOrderEnum(Enum):
	ZeroOrderType = 0
	FirstOrderType = 1

class ControlTypeEnum(Enum):
	LogicalType = 0
	SimpleType = 1

class ControlPriorityEnum(Enum):
	PriorityDefaultType = 0
	Priority1Type = 1
	Priority2Type = 2
	Priority3Type = 3
	Priority4Type = 4
	Priority5Type = 5

class ControlActionTypeEnum(Enum):
	SimpleActionType = 0
	CompositeActionType = 1

class ElementTypeEnum(Enum):
	ControlActionFCVType = 60
	ControlActionTCVType = 61
	ControlActionGPVType = 62
	ControlActionPressureValveType = 63
	ControlActionPumpType = 68
	ControlActionPipeType = 69

class PipeAttributeEnum(Enum):
	ActionPipeStatusType = 0

class ActionPipeStatusEnum(Enum):
	OpenType = 0
	OffType = 1

class PumpAttributeEnum(Enum):
	ActionPumpStatusType = 0
	ActionPumpSettingType = 1
	ActionPumpPressureSetting = 2
	ActionPumpHeadSetting = 3

class ActionPumpStatusEnum(Enum):
	OnType = 0
	OffType = 1

class TCVAttributeEnum(Enum):
	ActionTCVStatusType = 0
	ActionTCVSettingType = 1

class TCVStatusEnum(Enum):
	ClosedType = 0
	InactiveType = 1

class GPVAttributeEnum(Enum):
	ActionGPVStatusType = 0

class GPVStatusEnum(Enum):
	ClosedType = 0
	ActiveType = 1

class FCVAttributeEnum(Enum):
	ActionFCVSettingType = 0
	ActionFCVStatusType = 1

class FCVStatusEnum(Enum):
	ClosedType = 0
	InactiveType = 1

class PRVAttributeEnum(Enum):
	ActionPressureValveSettingType = 0
	ActionPressureValveStatusType = 1
	ActionPressureValveSettingPressure = 2

class ActionPressureValveStatusEnum(Enum):
	ClosedType = 0
	InactiveType = 1

class ConditionTypeEnum(Enum):
	SimpleConditionType = 0
	CompositeConditionType = 1

class SimpleConditionTypeEnum(Enum):
	ElementType = 0
	SystemDemandType = 1
	ClockTimeType = 2
	TimeFromStartType = 3

class ControlConditionPumpStatusEnum(Enum):
	OnType = 0
	OffType = 1

class ControlConditionPipeStatusEnum(Enum):
	OpenType = 0
	ClosedType = 1

class ControlConditionGPVStatusEnum(Enum):
	ClosedType = 0
	ActiveType = 1

class ControlConditionValveStatusEnum(Enum):
	ClosedType = 0
	InactiveType = 1

class ControlConditionElementTypeEnum(Enum):
	ControlConditionNodeType = 50
	ControlConditionTankType = 52
	ControlConditionFCVType = 60
	ControlConditionTCVType = 61
	ControlConditionGPVType = 62
	ControlConditionPressureValveType = 63
	ControlConditionPumpType = 68
	ControlConditionPipeType = 69
	ControlConditionHydroTankType = 302
	ControlConditionSurgeTankType = 308

class NodeAttributeEnum(Enum):
	NodeDemandType = 0
	NodeHydraulicGradeType = 1
	NodePressureType = 2

class TankAttributeEnum(Enum):
	TankDemandType = 0
	TankHydraulicGradeType = 1
	TankPressureType = 2
	TankLevelType = 3
	TankTimeToDrainType = 4
	TankTimeToFillType = 5
	TankPercentFullType = 6

class HydroTankAttributeEnum(Enum):
	HydroTankHydraulicGradeType = 1
	HydroTankPressureType = 2

class SuctionDataTypeEnum(Enum):
	Pressure = 0
	Level = 1

class DischargeDataTypeEnum(Enum):
	Pressure = 0
	Level = 1

class SurgeTankAttributeEnum(Enum):
	SurgeTankDemandType = 0
	SurgeTankHydraulicGradeType = 1
	SurgeTankPressureType = 2

class ControlConditionPumpAttributeEnum(Enum):
	PumpDischargeType = 0
	ConditionPumpSettingType = 1
	ConditionPumpStatusType = 2

class ConditionPipeAttributeEnum(Enum):
	PipeDischargeType = 0
	ConditionPipeStatusType = 1

class ControlConditionPressureValveAttributeEnum(Enum):
	PressureValveDischargeType = 0
	PressureValveSettingType = 1
	PressureValveStatusType = 2

class ControlConditionFCVAttributeEnum(Enum):
	FCVDischargeType = 0
	FCVSettingType = 1
	FCVStatusType = 2

class ControlConditionGPVAttributeEnum(Enum):
	GPVDischargeType = 0
	GPVStatusType = 1

class ControlConditionTCVAttributeEnum(Enum):
	TCVDischargeType = 0
	TCVSettingType = 1
	TCVStatusType = 2

class CompareOperatorEnum(Enum):
	EqualsType = 0
	GreaterThanType = 1
	GreaterThanEqualType = 2
	LessThanType = 3
	LessThanEqualType = 4
	NotEqualType = 5

class LogicalOperatorEnum(Enum):
	OperatorIfType = 0
	OperatorAndType = 1
	OperatorOrType = 2

class UnitDemandLoadTypeEnum(Enum):
	PopulationBasedType = 0
	AreaBasedType = 1
	CountUnitType = 3

class EquivalentPipeMethodEnum(Enum):
	ModifyDiameterType = 0
	ModifityRoughnessType = 1

class DominantPipeCriteriaEnum(Enum):
	DomBulkReactionRateType = 0
	DomDiameterType = 1
	DomInstallationYearType = 2
	DomLengthType = 3
	DomMinorLossCoefficientType = 4
	DomRoughnessType = 5
	DomWallReactionRateType = 6

class SkelebratorTypeEnum(Enum):
	SmartPipeRemovalType = 0
	BranchCollapsingType = 1
	SeriesPipeMergingType = 2
	ParallelPipeMergingType = 3
	InlineIsolatingValveReplacementType = 4

class BranchLoadDistributionStrategyEnum(Enum):
	MoveLoadType = 0
	DontMoveLoadType = 1

class SeriesLoadDistributionStrategyEnum(Enum):
	EquallyDistributedType = 0
	ProportionalToDominantCriteriaType = 1
	ProportionalToExistingLoadType = 2
	UserDefinedRatioType = 3

class MinorLossStrategyEnum(Enum):
	FiftyFiftySplityType = 0
	IgnoreMinorLossesType = 1
	SkipPipeMinorLossGreaterThanMaxType = 2

class MaterialConditionEnum(Enum):
	ConditionSameType = 0
	ConditionDifferentType = 1

class PipeConditionAttributeTypeEnum(Enum):
	ConditionBulkReactionRateType = 0
	ConditionDiameterType = 1
	ConditionHasCheckValveType = 2
	ConditionInstallationYearType = 3
	ConditionLengthType = 4
	ConditionMaterialType = 5
	ConditionMinorLossCoefficientType = 6
	ConditionRoughnessType = 7
	ConditionWallReactionRateType = 8
	ConditionWaveSpeed = 9

class PipeConditionOperatorTypeEnum(Enum):
	PipeConditionLessThanType = 0
	PipeConditionGreaterThanType = 1
	PipeConditionLessThanEqualType = 2
	PipeConditionGreaterThanEqualType = 3
	PipeConditionEqualType = 4
	PipeConditionNotEqualType = 5
	PipeConditionToleranceType = 6

class JunctionConditionAttributeTypeEnum(Enum):
	ConditionBaseFlowType = 0
	ConditionElevationType = 1
	ConditionEmitterCoefficientType = 2

class JunctionConditionOperatorEnum(Enum):
	JunctionConditionLessThanType = 0
	JunctionConditionGreaterThanType = 1
	JunctionConditionLessThanEqualType = 2
	JunctionConditionGreaterThanEqualType = 3
	JunctionConditionEqualType = 4
	JunctionConditionNotEqualType = 5
	JunctionConditionToleranceType = 6

class IdahoSupportElementTypes(Enum):
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

