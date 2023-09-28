from enum import Enum
from System import TypeCode

class TargetAttribute(Enum):
	NullAttribute = 0
	SS_Depth = 1
	SS_DepthIn = 2
	SS_DepthOut = 3
	SS_VelocityIn = 4
	SS_VelocityOut = 5
	TankStatus = -301
	RelativeClosure = -300
	ConstituentConcentration = -299
	PressureNodeDemand = -297
	ValveStatus = -58
	PumpStatus = -57
	PipeStatus = -56
	TankLevel = -55
	Pressure = -54
	HydraulicGrade = -53
	PumpSetting = -52
	PressureValveSetting = -51
	TCValveSetting = -50
	FCValveSetting = -49
	PressureOut = -48
	PressureIn = -47
	HydraulicGradeOut = -46
	HydraulicGradeIn = -45
	Discharge = -44
	WirePower = -43
	SS_SurfaceElevation = -7

class ActiveAlarmsEnum(Enum):
	None = 0
	Low = 1
	High = 2
	LowHigh = 3
	All = 4

