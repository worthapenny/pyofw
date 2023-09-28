from enum import Enum
from System import TypeCode

class CalculationResultStatus(Enum):
	Balanced = 0
	Unbalanced = 1
	CannotSolveHydraulicEquations = 2

class BoundaryConditionType(Enum):
	FreeOutfall = 0
	UserDefinedTailwater = 1
	BoundaryElevationFlowCurve = 2
	Crown = 10

class InflowType(Enum):
	FixedLoad = 0
	HydrographLoad = 1
	InflowPattern = 2

class LoadDefinition(Enum):
	SanitaryHydrograph = 0
	SanitaryUnitLoad = 1
	SanitaryPatternLoad = 2

class TCVCoefficientType(Enum):
	TCVCoefficientType_Headloss = 1
	TCVCoefficientType_Discharge = 2
	TCVCoefficientType_ValveCharactersticsCurve = 3

class ControlValveCoefficientType(Enum):
	ControlValveCoefficientType_MinorLoss = 1
	ControlValveCoefficientType_DischargeCoefficient = 2

class HammerValveType(Enum):
	HammerValveType_Butterfly = 0
	HammerValveType_Needle = 1
	HammerValveType_CircularGate = 2
	HammerValveType_Globe = 3
	HammerValveType_Ball = 4
	HammerValveType_UserDefined = 5

class DischargeElementType(Enum):
	DischargeElementTypeOrifice = 0
	DischargeElementTypeValve = 1
	DischargeElementTypeRatingCurve = 2

class ValveTypeInitialStatus(Enum):
	ValveTypeInitialStatus_Open = 1
	ValveTypeInitialStatus_Closed = 2

class TankCalculationModel(Enum):
	ConstantAreaApproximation = 0
	GasLawModel = 1

class FlushingElementType(Enum):
	ElementType_Hydrant = 54
	ElementType_Junction = 55
	ElementType_FCV = 60
	ElementType_TCV = 61
	ElementType_GPV = 62
	ElementType_PRV = 64
	ElementType_PSV = 65
	ElementType_PBV = 66
	ElementType_Pipe = 69
	ElementType_PressureIsolationValve = 71

class FlushingStatus(Enum):
	Open = 0
	Closed = 1
	PipeRun = 2
	Flowing = 3

class FlushingType(Enum):
	Conventional = 0
	Unidirectional = 1

class FlushingApplyFlushingFlowBy(Enum):
	AddingToBaselineDemand = 0
	ReplacingBaselineDemand = 1

class PeriodicHeadFlowTransientBehavior(Enum):
	TransientBehaviorHead = 0
	TransientBehaviorFlow = 1

class CheckValveFlowDirection(Enum):
	TowardsWye = 0
	AwayFromWye = 1

class OverrideReportingTimeStepType(Enum):
	All = 0
	Constant = 1
	Variable = 2

class ReportType(Enum):
	All = 0
	Constant = 1
	None = 2

class PatternCategory(Enum):
	PatternCategoryHydraulic = 0
	PatternCategoryConstituent = 1
	PatternCategoryReservoir = 2
	PatternCategoryPump = 3
	PatternCategoryOperationalValve = 4
	PatternCategoryOperationalPump = 5
	PatternCategoryOperationalTurbine = 6
	PatternCategoryValve = 7
	PatternCategoryValveRelativeClosure = 8
	PatternCategoryPowerUsage = 9

class IsolationValveInitialSetting(Enum):
	IsolationValveOpen = 0
	IsolationValveClosed = 1

class ApplyFireFlows(Enum):
	AddToBaseline = 0
	ReplaceBaseline = 1

class PressureValveSetting(Enum):
	ValvePressure = 0
	ValveHGL = 1

class TurbineStatus(Enum):
	Open = 0
	Closed = 1

class HydrantStatus(Enum):
	Open = 0
	Closed = 1

class PddFunctionType(Enum):
	PowerFunction = 0
	PieceLinear = 1

class PumpDefinitionType(Enum):
	ConstantPower = 0
	DesignPoint = 1
	Standard = 2
	StandardExtended = 3
	CustomExtended = 4
	MultiplePoint = 5
	VolumeFlow = 6
	DepthFlow = 7
	DepthFlowVariableSpeed = 8

class PatternFormat(Enum):
	Stepwise = 0
	Continuous = 1

class CalculationType(Enum):
	FireFlow = 0
	Flushing = 1
	AgeAnalysis = 2
	ConstituentAnalysis = 3
	TraceAnalysis = 4
	HydraulicsOnly = 5
	MSXAnalysis = 6
	SCADA = 7
	AllQualities = 8

class ScadaCalculationType(Enum):
	HydraulicsOnly = 0
	ConstituentAnalysis = 1
	AgeAnalysis = 2
	TraceAnalysis = 3
	QualityAnalysis = 4

class SCADASimulationMode(Enum):
	Baseline = 0
	Historical = 1
	Live = 2
	LiveAuto = 3
	HistoricalLiveTraining = 4

class TimeAnalysisType(Enum):
	SteadyState = 0
	EPS = 1

class EngineCompatibilityType(Enum):
	V8iSS2 = 0
	V8iSS1 = 1
	EPANET2_12 = 2
	EPANET2_10 = 3

class ConstituentSourceType(Enum):
	Concentration = 0
	FlowPacedBooster = 1
	SetpointBooster = 2
	MassBooster = 3

class WallReactionOrder(Enum):
	ZeroOrder = 0
	FirstOrder = 1

class TankMixingModel(Enum):
	TwoCompartment = 0
	CompletelyMixed = 1
	FIFO = 2
	LIFO = 3

class VSPType(Enum):
	PatternBased = 0
	FixedHead = 1
	FixedFlow = 2

class VSPBType(Enum):
	FixedHead = 1
	FixedFlow = 2

class FrictionMethod(Enum):
	DarcyWeisbach = 0
	HazenWilliams = 1
	Mannings = 2
	ModifiedHazenWilliams = 3

class AlabamaFrictionMethod(Enum):
	Mannings = 0
	HazenWilliams = 1
	DarcyWeisbach = 2
	Kutters = 3

class OperatingRangeType(Enum):
	Elevations = 0
	Levels = 1

class HydroTankOperatingRangeType(Enum):
	HydroTankOperatingRangeElevation = 0
	HydroTankOperatingRangeLevel = 1

class TankSection(Enum):
	CircularTankSection = 0
	NonCircularTankSection = 1
	VariableAreaTankSection = 2

class ControlType(Enum):
	Logical = 0
	Simple = 1

class SurgeTankType(Enum):
	SimpleSurgeTank = 0
	DifferentialSurgeTank = 1

class ControlPriority(Enum):
	PriorityDefault = 0
	Priority1 = 1
	Priority2 = 2
	Priority3 = 3
	Priority4 = 4
	Priority5 = 5

class ControlActionType(Enum):
	SimpleAction = 0
	CompositeAction = 1

class SimpleActionType(Enum):
	ControlActionFCV = 60
	ControlActionTCV = 61
	ControlActionGPV = 62
	ControlActionPressureValve = 63
	ControlActionPump = 68
	ControlActionPipe = 69

class ControlActionPipeAttribute(Enum):
	PipeStatus = 0

class ControlActionPipeStatus(Enum):
	Open = 0
	Closed = 1

class ControlActionPumpAttribute(Enum):
	PumpStatus = 0
	PumpSetting = 1
	PumpPressureSetting = 2
	PumpHeadSetting = 3

class ControlActionPumpStatus(Enum):
	On = 0
	Off = 1

class ControlActionTCVAttribute(Enum):
	TCVStatus = 0
	TCVSetting = 1

class ControlActionTCVStatus(Enum):
	Closed = 0
	Inactive = 1

class ControlActionGPVAttribute(Enum):
	GPVStatus = 0

class ControlActionGPVStatus(Enum):
	Closed = 0
	Active = 1

class ControlActionFCVAttribute(Enum):
	FCVSetting = 0
	FCVStatus = 1

class ControlActionFCVStatus(Enum):
	Closed = 0
	Inactive = 1

class ControlActionPressureValveAttribute(Enum):
	PressureValveSettingHydraulicGrade = 0
	PressureValveStatus = 1
	PressureValveSettingPressure = 2

class ControlActionPressureValveStatus(Enum):
	Closed = 0
	Inactive = 1

class ControlConditionType(Enum):
	SimpleCondition = 0
	CompositeCondition = 1

class SimpleConditionType(Enum):
	Element = 0
	SystemDemand = 1
	ClockTime = 2
	TimeFromStart = 3

class SimpleConditionElementType(Enum):
	ControlConditionPumpStatus = 129
	ControlConditionPipeStatus = 130
	ControlConditionGPVStatus = 131
	ControlConditionValveStatus = 132
	ControlConditionElementType = 133

class ControlConditionPumpStatus(Enum):
	On = 0
	Off = 1

class ControlConditionPipeStatus(Enum):
	Open = 0
	Closed = 1

class ControlConditionGPVStatus(Enum):
	Closed = 0
	Active = 1

class ControlConditionValveStatus(Enum):
	Closed = 0
	Inactive = 1

class ControlConditionElementType(Enum):
	ControlConditionNode = 50
	ControlConditionTank = 52
	ControlConditionFCV = 60
	ControlConditionTCV = 61
	ControlConditionGPV = 62
	ControlConditionPressureValve = 63
	ControlConditionPump = 68
	ControlConditionPipe = 69
	ControlConditionHydroTank = 302
	ControlConditionSurgeTank = 308

class ControlConditionNodeAttribute(Enum):
	NodeDemand = 0
	NodeHydraulicGrade = 1
	NodePressure = 2

class ControlConditionTankAttribute(Enum):
	TankDemand = 0
	TankHydraulicGrade = 1
	TankPressure = 2
	TankLevel = 3
	TankTimeToDrain = 4
	TankTimeToFill = 5
	TankPercentFull = 6

class ControlConditionPumpAttribute(Enum):
	PumpDischarge = 0
	ConditionPumpSetting = 1
	ConditionPumpStatus = 2

class ControlConditionPipeAttribute(Enum):
	PipeDischarge = 0
	ConditionPipeStatus = 1

class ControlConditionPressureValveAttribute(Enum):
	PressureValveDischarge = 0
	PressureValveSetting = 1
	PressureValveStatus = 2

class ControlConditionFCVAttribute(Enum):
	FCVDischarge = 0
	FCVSetting = 1
	FCVStatus = 2

class ControlConditionGPVAttribute(Enum):
	GPVDischarge = 0
	GPVStatus = 1

class ControlConditionTCVAttribute(Enum):
	TCVDischarge = 0
	TCVSetting = 1
	TCVStatus = 2

class ControlConditionHydroTankAttribute(Enum):
	HydroTankHydraulicGrade = 1
	HydroTankPressure = 2

class ControlConditionSurgeTankAttribute(Enum):
	SurgeTankDemand = 0
	SurgeTankHydraulicGrade = 1
	SurgeTankPressure = 2

class CompareOperator(Enum):
	Equals = 0
	GreaterThan = 1
	GreaterThanEqual = 2
	LessThan = 3
	LessThanEqual = 4
	NotEqual = 5

class LogicalOperator(Enum):
	OperatorIf = 0
	OperatorAnd = 1
	OperatorOr = 2

class EngineCalculationFlags(Enum):
	None = 0
	PumpExceedsMaximumOperatingPoint = 1
	NegativePressures = 2
	TankEmpty = 4
	TankLowLevelAlarm = 8
	TankHighLevelAlarm = 16
	TankFull = 32
	ContainsInfoFlagMask = 255
	Unstable = 256
	Disconnected = 512
	PumpCannotDeliverFlowOrHead = 1024
	ValveCannotDeliverFlow = 2048
	ValveCannotSupplyPressure = 4096
	Disconnecting = 8192
	PumpFixedFlowTargetIsTooLow = 16384
	ValveHeadLossSmallerThanWhenFullyOpen = 32768
	ControlActionExecutedOnValveWithPattern = 65536
	PumpCannotDeliverHead = 131072
	PumpFailsNPSHR = 262144
	FF_NodeBelowMinimumPressure = 524288
	FF_PipeExceedsMaximumVelocity = 1048576
	FF_FFNodeFailsResidualPressure = 2097152
	UnsupportedStartAndEndNodeConfiguration = 8388608
	ContainsWarningFlagMask = 16776960
	Unbalanced = 16777216
	IllConditioned = 33554432
	UnableToComputeOmegaForVSPump = 67108864
	InconsistentPumpBatteryResults = 268435456
	DemandDisconnected = 536870912
	UnexpectedReverseFlow = 1073741824
	ContainsErrorFlagMask = 30

class PatternValidationFailureType(Enum):
	NotEnoughPoints = 0
	DuplicateTimes = 1
	FirstTimeIsZero = 2
	LastMultiplierMustMatchStartMultiplier = 3
	PatternPointsOutOfOrder = 4
	NegativeMultiplierInPumpPattern = 5
	LastClosureMustMatchStartClosure = 6
	RelativeClosureOutsideAllowableRange = 7
	TimeStepOrStartTimeMismatch = 8

class FlushingElementCategory(Enum):
	FlowingNode = 1
	StatusElement = 2

class PressureEngineNodeType(Enum):
	NodeTypeJunction = 0
	NodeTypeReservoir = 1
	NodeTypeTank = 2
	NodeTypeVSPCN = 3

class PressureEngineLinkType(Enum):
	LinkTypeCVPipe = 0
	LinkTypePipe = 1
	LinkTypePump = 2
	LinkTypePRV = 3
	LinkTypePSV = 4
	LinkTypePBV = 5
	LinkTypeFCV = 6
	LinkTypeTCV = 7
	LinkTypeGPV = 8

class PressureEngineLinkStatus(Enum):
	LinkStatusClosed = 0
	LinkStatusOpen = 1

class PressureEngineSourceType(Enum):
	SourceTypeConcentrationBooster = 0
	SourceTypeMassBooster = 1
	SourceTypeSetpointBooster = 2
	SourceTypeFlowPacedBooster = 3

class PressureEngineMixingModelType(Enum):
	Mix1 = 0
	Mix2 = 1
	Fifo = 2
	Lifo = 3

class PressureEngineFlowUnit(Enum):
	FlowUnitCFS = 0
	FlowUnitGPM = 1
	FlowUnitMGD = 2
	FlowUnitIMGD = 3
	FlowUnitAFD = 4
	FlowUnitLPS = 5
	FlowUnitLPM = 6
	FlowUnitMLD = 7
	FlowUnitCMH = 8
	FlowUnitCMD = 9

class PressureEngineReportFlag(Enum):
	ReportFlagNoStatusReport = 0
	ReportFlagNormalStatusReport = 1
	ReportFlagFullStatusReport = 2

class PressureEngineControlType(Enum):
	LowLevelControl = 0
	HighLevelControl = 1
	TimerControl = 2
	TimeOfDayControl = 3

class PressureEngineQualityAnalysisType(Enum):
	QualityAnalysisNone = 0
	QualityAnalysisChemical = 1
	QualityAnalysisAge = 2
	QualityAnalysisTrace = 3

class PressureEngineTimeStatisticsFlag(Enum):
	TimeStatisticsNone = 0
	TimeStatisticsAverage = 1
	TimeStatisticsMinimum = 2
	TimeStatisticsMaximum = 3
	TimeStatisticsRange = 4

