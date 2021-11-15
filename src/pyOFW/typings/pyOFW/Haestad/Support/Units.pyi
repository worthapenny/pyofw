from Haestad.Support.Support import INamable, ILabeled
from typing import List, overload, Dict
from enum import Enum
from System import TypeCode, ICloneable
from datetime import datetime
from System.Runtime.Serialization import SerializationInfo, StreamingContext, ISerializable

class DimensionType(Enum):
	Dimensionless = 0
	Length = 1
	Area = 2
	Mass = 3
	Flow = 4
	Percentage = 5
	Time = 6
	ReactionRate = 7
	SurfaceReactionRate = 8
	Pressure = 9
	Concentration = 10
	Volume = 11
	Diffusivity = 12
	Temperature = 13
	Power = 14
	RainfallIntensity = 15
	Angle = 16
	InfiltrationRate = 17
	Velocity = 18
	Scale = 19
	NthOrderBulkReactionRate = 20
	ZeroOrderSurfaceReactionRate = 21
	CurrencyPerPower = 22
	CurrencyPerEnergy = 23
	Slope = 24
	FlowDensityPerArea = 25
	Currency = 26
	Population = 27
	Energy = 28
	MassRate = 29
	SpecificWeight = 30
	FlowPerCapita = 31
	PopulationDensityPerArea = 32
	EmitterCoeff = 33
	CurrencyPerLength = 34
	Unitless = 35
	ElectricalFrequency = 102
	RotationalFrequency = 103
	WeirCoefficient = 104
	DiameterLength = 105
	MassPerArea = 106
	Inertia = 108
	CostPerUnitVolume = 109
	EnergyPerUnitVolume = 110
	Torque = 111
	SpringConstant = 112
	Force = 113
	Density = 114
	DischargePerPressureDrop = 115
	VolumerPerLength = 116
	SideWeirCoefficient = 117
	InfiltrationPerUnitDepth = 118
	PressurePerLength = 119
	MassPerLength = 120
	PerLength = 121
	PerPressure = 122
	DynamicViscosity = 123
	CalorificValue = 124
	WeirCoefficientParameterized = 125
	SnowMeltCoefficient = 126
	BreakRate = 127
	MassPerEnergy = 128
	ValveOpenCloseRateCoefficient = 129
	EnergyPerPower = 130
	DrainCoefficient = 131
	NumberPerVolume = 132
	NumbersPerArea = 133
	MolesPerVolume = 134
	MolesPerArea = 135
	ValveOpenCloseRateCoefficientPerFlow = 136
	FlowPerUnitLength = 137
	Acceleration = 138

class EmitterCoefficientUnit(Enum):
	LitersPerDayPerMetersOfH2O = 1
	MegaLitersPerDayPerMetersOfH2O = 2
	LitersPerSecondPerMetersOfH2O = 3
	CubicMetersPerSecondPerMetersOfH2O = 4
	CubicMetersPerHourPerMetersOfH2O = 5
	CubicMetersPerDayPerMetersOfH2O = 6
	GallonsPerSecondPerPSI = 7
	GallonsPerDayPerPSI = 8
	ImperialGallonsPerSecondPerPSI = 9
	ImperialGallonsPerDayPerPSI = 10
	CubicFeetPerSecondPerPSI = 11
	CubicFeetPerDayPerPSI = 12
	LitersPerMinutePerMetersOfH2O = 13
	CubicMetersPerMinutePerMetersOfH2O = 14
	CFSPerPSI = 15
	CubicFeetPerMinutePerPSI = 16
	CFMPerPSI = 17
	GallonsPerMinutePerPSI = 18
	GPMPerPSI = 19
	ImperialGallonsPerMinutePerPSI = 20
	MGDPerPSI = 21
	MGDImperialPerPSI = 22

class LengthUnit(Enum):
	Meters = 1
	Kilometers = 2
	Centimeters = 3
	Millimeters = 4
	Feet = 5
	Mfeet = 6
	Millifeet = 7
	Inches = 8
	Yards = 9
	Miles = 10
	Decimeters = 11
	USSurveyFoot = 12

class AreaUnit(Enum):
	SquareMillimeters = 1
	SquareCentimeters = 2
	SquareMeters = 3
	Hectares = 4
	SquareKilometers = 5
	SquareInches = 6
	SquareFeet = 7
	ThousandSquareFeet = 8
	SquareYards = 9
	Acres = 10
	SquareMiles = 11

class MassUnit(Enum):
	Kilograms = 1
	Gram = 2
	Milligram = 3
	Pounds = 4
	Tons = 5

class FlowUnit(Enum):
	LitersPerDay = 1
	MegaLitersPerDay = 2
	LitersPerSecond = 3
	CubicMetersPerSecond = 4
	CubicMetersPerHour = 5
	CubicMetersPerDay = 6
	GallonsPerSecond = 7
	GallonsPerDay = 8
	ImperialGallonsPerSecond = 9
	ImperialGallonsPerDay = 10
	CubicFeetPerSecond = 11
	CubicFeetPerDay = 12
	AcreFeetPerMinute = 13
	LitersPerMinute = 14
	CubicMetersPerMinute = 15
	CFS = 16
	CubicFeetPerMinute = 17
	CFM = 18
	GallonsPerMinute = 19
	GPM = 20
	ImperialGallonsPerMinute = 21
	AcreInchPerMinute = 22
	AcreInchPerHour = 23
	AcreFeetPerHour = 24
	AcreFeetPerDay = 25
	MGD = 26
	MGDImperial = 27
	MillionLitersPerDay = 28
	GPD = 29
	LitersPerHour = 30

class PercentUnit(Enum):
	Percent = 1
	Unitless = 2

class TimeUnit(Enum):
	Seconds = 1
	Minutes = 2
	Hours = 3
	Days = 4
	Years = 5
	Milliseconds = 6

class ReactionRateUnit(Enum):
	PerSecond = 1
	PerDay = 2
	PerMinute = 3
	PerHour = 4

class SurfaceReactionRateUnit(Enum):
	MetersPerSecond = 1
	MetersPerDay = 2
	FeetPerDay = 3

class PressureUnit(Enum):
	NewtonsPerSquareMeter = 1
	MillimetersOfH2O = 2
	KiloPascals = 3
	MetersOfH2O = 4
	KilogramsPerSquareCentimeter = 5
	Bars = 6
	PoundsPerSquareFoot = 7
	FeetOfH2O = 8
	PoundsPerSquareInch = 9
	PSI = 10
	Atmospheres = 11
	KilogramsPerSquareMeter = 12
	Pascals = 13
	HektoPascals = 14
	MegaPascals = 15
	MilliBars = 16

class ConcentrationUnit(Enum):
	MicrogramsPerLiter = 1
	PartsPerBillion = 2
	MilliGramsPerLiter = 3
	PartsPerMillion = 4
	PoundsPerCubicFoot = 5
	PoundsPerMillionGallons = 6

class VolumeUnit(Enum):
	CubicCentimeters = 1
	Liters = 2
	CubicMeters = 3
	CubicInches = 4
	Gallons = 5
	ImpGallons = 6
	CubicFeet = 7
	CubicYards = 8
	AcreInches = 9
	AcreFeet = 10
	MillionGallons = 11
	ThousandGallons = 12
	ThousandLiters = 13
	MillionLiters = 14

class DollarsPerVolumeUnit(Enum):
	DollarsPerCubicCentimeters = 1
	DollarsPerLiters = 2
	DollarsPerCubicMeters = 3
	DollarsPerCubicInches = 4
	DollarsPerGallons = 5
	DollarsPerImpGallons = 6
	DollarsPerCubicFeet = 7
	DollarsPerCubicYards = 8
	DollarsPerAcreInches = 9
	DollarsPerAcreFeet = 10
	DollarsPerMillionGallons = 11
	DollarsPerThousandGallons = 12
	DollarsPerThousandLiters = 13
	DollarsPerMillionLiters = 14

class DiffusivityUnit(Enum):
	SquareMetersPerSecond = 1
	SquareFeetPerSecond = 2
	Stokes = 3
	Centistokes = 4

class TemperatureUnit(Enum):
	Celsius = 1
	Fahrenheit = 2
	Kelvin = 3

class PowerUnit(Enum):
	Watts = 1
	Kilowatts = 2
	HorsePower = 3
	MegaWatts = 4
	GigaWatts = 5

class EnergyUnit(Enum):
	Joules = 1
	KiloJoules = 2
	KiloWattHours = 3
	FootPoundals = 4
	MegaJoules = 5
	GigaJoules = 6
	WattSeconds = 7
	MegaWattHours = 8
	GigaWattHours = 9

class RainfallIntensityUnit(Enum):
	MillimetersPerMinute = 1
	CentimetersPerMinute = 2
	InchesPerDay = 3
	InchesPerHour = 4
	InchesPerMinute = 5
	MillimetersPerDay = 6
	CentimetersPerDay = 7
	MillimetersPerHour = 8
	CentimetersPerHour = 9
	MicrometersPerSecond = 10

class AngleUnit(Enum):
	Radians = 1
	Degrees = 2
	AngleMinutes = 3
	AngleSeconds = 4
	Quadrants = 5
	Revolutions = 6

class InfiltrationRateUnit(Enum):
	MillimetersPerMinute = 1
	CentimetersPerMinute = 2
	InchesPerDay = 3
	InchesPerHour = 4
	InchesPerMinute = 5
	MillimetersPerDay = 6
	CentimetersPerDay = 7
	MillimetersPerHour = 8
	CentimetersPerHour = 9

class VelocityUnit(Enum):
	CentimetersPerHour = 1
	CentimetersPerMinute = 2
	CentimetersPerSecond = 3
	MetersPerHour = 4
	MetersPerMinute = 5
	KilometersPerHour = 6
	MetersPerSecond = 7
	InchesPerHour = 8
	FeetPerHour = 9
	InchesPerMinute = 10
	FeetPerMinute = 11
	InchesPerSecond = 12
	FeetPerSecond = 13
	MilePerHour = 14
	KnotInternational = 15
	Knot = 16

class ScaleUnit(Enum):
	MetersPerCm = 1
	FeetPerInch = 2

class NthOrderBulkReactionRateUnit(Enum):
	MicrogramsPerLiterNPerSecond = 1
	MicrogramsPerLiterNPerDay = 2
	PartsPerBillionNPerSecond = 3
	PartsPerBillionNPerDay = 4
	MilliGramsPerLiterNPerSecond = 5
	MilliGramsPerLiterNPerDay = 6
	PartsPerMillionNPerSecond = 7
	PartsPerMillionNPerDay = 8
	PoundsPerCubicFootNPerSecond = 9
	PoundsPerCubicFootNPerDay = 10
	PoundsPerMillionGallonsNPerSecond = 11
	PoundsPerMillionGallonsNPerDay = 12

class ZeroOrderSurfaceReactionRateUnit(Enum):
	MicrogramsPerSquareMeterPerSecond = 1
	MicrogramsPerSquareMeterPerDay = 2
	MicrogramsPerSquareFeetPerDay = 3
	MilliGramsPerSquareMeterPerSecond = 4
	MilliGramsPerSquareMeterPerDay = 5
	MilliGramsPerSquareFeetPerDay = 6

class CurrencyPerEnergyUnit(Enum):
	DollarsPerKiloWattHour = 1

class CurrencyPerPowerUnit(Enum):
	DollarsPerKiloWatt = 1
	DollarsPerHorsePower = 2

class SlopeUnit(Enum):
	PercentSlope = 1
	OneOverS = 2
	CentimeterPerMeter = 3
	FeetPer1000Feet = 4
	FootPerFoot = 5
	FootPerFootVtoH = 6
	FootPerFootHtoV = 7
	FeetPerMile = 8
	HorizontalToVertical = 9
	VerticalToHorizontal = 10
	InchPerFoot = 11
	MeterPerKilometer = 12
	MeterPerMeter = 13
	MeterPerMeterVtoH = 14
	MeterPerMeterHtoV = 15
	MilliMeterPerMeter = 16
	MillimeterVerticalPerMeterHorizontal = 17
	MilliMeterPerMeterHtoV = 18

class FlowDensityPerAreaUnit(Enum):
	CFSPerSquareFeet = 1
	CFSPerAcres = 2
	CFSPerSquareMiles = 3
	GPMPerSquareFeet = 4
	GPMPerAcres = 5
	GPMPerSquareMile = 6
	GPDPerSquareFeet = 7
	GPDPerAcres = 8
	GPDPerSquareMile = 9
	LitersPerSquareMeterPerDay = 10
	LitersPerSquareKilometerPerDay = 11
	LitersPerHectaresPerDay = 12
	CubicMetersPerSquareMeterPerDay = 13
	CubicMetersPerSquareKilometerPerDay = 14
	CubicMetersPerHectaresPerDay = 15
	LitersPerHectaresPerSecond = 16

class PopulationDensityPerAreaUnit(Enum):
	PersonsPerSquareFeet = 1
	PersonsPerAcre = 2
	PersonsPerSquareMile = 3
	PersonsPerSquareMeter = 4
	PersonsPerSquareKilometer = 5
	PersonsPerHectares = 6

class FlowPerCapitaUnit(Enum):
	GPDPerCapita = 1
	LitersPerCapitaPerDay = 2

class CurrencyUnit(Enum):
	BaseCurrency = 1
	KiloCurrency = 2
	MegaCurrency = 3
	GigaCurrency = 4

class PopulationUnit(Enum):
	Capita = 1
	ThousandCapita = 2
	HundredCapita = 3
	Customer = 4
	Employee = 5
	Passenger = 6
	Person = 7
	Guest = 8
	Resident = 9
	Student = 10

class MassRateUnit(Enum):
	MicrogramsPerSecond = 1
	MilliGramsPerSecond = 2
	GramsPerSecond = 3
	KilogramsPerSecond = 4
	PoundsPerSecond = 5
	MicrogramsPerMinute = 6
	MilliGramsPerMinute = 7
	GramsPerMinute = 8
	KilogramsPerMinute = 9
	PoundsPerMinute = 10
	MicrogramsPerHour = 11
	MilliGramsPerHour = 12
	GramsPerHour = 13
	KilogramsPerHour = 14
	PoundsPerHour = 15
	MicrogramsPerDay = 16
	MilliGramsPerDay = 17
	GramsPerDay = 18
	KilogramsPerDay = 19
	PoundsPerDay = 20

class SpecificWeightUnit(Enum):
	NewtonsPerCubicMeter = 1
	KiloNewtonsPerCubicMeter = 2
	PoundsForcePerCubicFoot = 3

class ElectricalFrequencyUnit(Enum):
	Hertz = 1

class RotationalFrequencyUnit(Enum):
	RPM = 1

class WeirCoefficientUnit(Enum):
	SI = 1
	US = 2

class SideWeirCoefficientUnit(Enum):
	SI = 1
	US = 2

class DiameterLengthUnit(Enum):
	InchMiles = 1
	InchFeet = 2
	FootMiles = 3
	FootFeet = 4
	MillimeterMeters = 5
	MillimeterKilometers = 6
	MeterMeters = 7
	MeterKilometer = 8
	InchMeters = 9
	MillimeterMiles = 10

class MassPerAreaUnit(Enum):
	PoundsPerAcre = 1
	KilogramsPerHectare = 2
	MilligramsPerSquareFeet = 3
	MicrogramsPerSquareFeet = 4
	MilligramsPerSquareMeter = 5
	MicrogramsPerSquareMeter = 6
	MilligramsPerSquareCentimeter = 7
	MicrogramsPerSquareCentimeter = 8

class NumberPerVolumeUnit(Enum):
	NumbersPerLiter = 1
	ThousandNumbersPerLiter = 2
	MillionNumbersPerLiter = 3

class NumbersPerAreaUnit(Enum):
	NumbersPerSquareMeter = 1
	ThousandNumbersPerSquareMeter = 2
	MillionNumbersPerSquareMeter = 3
	NumbersPerSquareFeet = 4
	ThousandNumbersPerSquareFeet = 5
	MillionNumbersPerSquareFeet = 6
	NumbersPerSquareCentimeter = 7
	ThousandNumbersPerSquareCentimeter = 8
	MillionNumbersPerSquareCentimeter = 9

class MolesPerVolumeUnit(Enum):
	MolePerLiter = 1
	MilliMolePerLiter = 2

class MolesPerAreaUnit(Enum):
	MolePerSquareMeter = 1
	MilliMolePerSquareMeter = 2
	MolePerSquareFeet = 3
	MilliMolePerSquareFeet = 4
	MolePerSquareCentimeter = 5
	MilliMolePerSquareCentimeter = 6

class InertiaUnit(Enum):
	PoundSquareFeet = 1
	NewtonSquareMeters = 2
	KilogramSquareMeters = 3

class EnergyPerUnitVolume(Enum):
	KiloWattHourPerMillionGallons = 1
	KiloWattHourPerMillionLiters = 2
	KiloWattHourPerCubicMeters = 3
	KiloWattHourPerCubicFeet = 4

class TorqueUnit(Enum):
	NewtonMeters = 1
	PoundFeet = 2

class SpringConstantUnit(Enum):
	PoundPerInch = 1
	NewtonPerMillimeter = 2

class ForceUnit(Enum):
	PoundForce = 1
	KiloPoundForce = 2
	Newton = 3
	KiloNewton = 4

class DensityUnit(Enum):
	SlugPerCubicFoot = 1
	PoundPerCubicFoot = 2
	KilogramPerCubicMeter = 3

class DischargePerPressureDropUnit(Enum):
	CfsPerSquareRootFooH20 = 1
	CmsPerSquareRootMeterH20 = 2
	LPerSecPerSquareRootKpa = 3
	GpmPerSquareRootPsi = 4

class VolumerPerLength(Enum):
	CubicFeetPerFoot = 1
	CubicMetersPerMeter = 2

class InfiltrationPerUnitDepth(Enum):
	InchesPerHourPerFeetToKexp = 1
	CentimeterPerHourPerMeterToKexp = 2

class PressurePerLengthUnit(Enum):
	PascalsPerMeter = 1
	BarsPerKiloMeter = 2
	PSIPerFoot = 3
	PSIPerInch = 4

class MassPerLengthUnit(Enum):
	KilogramsPerMeter = 1
	PoundsPerFoot = 2

class PerLengthUnit(Enum):
	PerMeter = 1
	PerMillimeter = 2

class PerPressureUnit(Enum):
	PerPascals = 1
	PerBars = 2
	PerPSI = 3

class DynamicViscosityUnit(Enum):
	KilogramsPerMeterPerSecond = 1
	PoundSecondPerSquareFoot = 2

class CalorificValueUnit(Enum):
	JoulesPerCubicMeters = 1
	KiloJoulesPerCubicMeters = 2
	MegaJoulesPerCubicMeters = 3
	KiloWattHoursPerCubicMeters = 4

class DateTimeFormats(Enum):
	ElapsedTimeShort = 0
	ElapsedTimeLong = 1
	ShortTime = 2
	LongTime = 3
	ShortDate = 4
	LongDate = 5
	ShortDateAndShortTime = 6
	ShortDateAndLongTime = 7
	LongDateAndShortTime = 8
	LongDateAndLongTime = 9
	SortableDateTime = 10
	UniversalSortableDateTime = 11
	UniversalFullDateAndTime = 12

class WeirCoefficientParameterizedUnit(Enum):
	SI = 1
	US = 2

class SnowMeltCoefficientUnit(Enum):
	MillimetersPerHourPerDegreeCelsius = 1
	InchesPerHourPerDegreeFahrenheit = 2

class BreakRateUnit(Enum):
	BreaksPerYrPerKm = 1
	BreaksPerYrPerMi = 2
	BreaksPerYrPer1000Ft = 3
	BreaksPerYrPer100Mi = 4

class ValveOpenCloseRateCoefficientUnit(Enum):
	percentPerSecondPerMeterH2O = 1
	percentPerSecondPerFtH2O = 2
	percentPerSecondPerKiloPascal = 3
	percentPerSecondPerPSI = 4

class AccelerationUnit(Enum):
	MetersPerSquareSecond = 1
	FeetPerSquareSecond = 2

class DrainCoefficientUnit(Enum):
	DrainCoeffInchesPerHour = 1
	DrainCoeffMMPerHour = 2

class ValveOpenCloseRateCoefficientUnitPerFlow(Enum):
	PercentPerSecondPerCubicFeetPerSecond = 1
	PercentPerSecondPerCubicFeetPerMinute = 2
	PercentPerSecondPerCubicMeterPerSecond = 3
	PercentPerSecondPerCubicMeterPerMinute = 4
	PercentPerSecondPerLiterPerSecond = 5
	PercentPerSecondPerLiterPerMinute = 6
	PercentPerSecondPerGalPerSecond = 7
	PercentPerSecondPerGalPerMinute = 8

class FlowPerUnitLengthUnit(Enum):
	CubicFeetPerMilePerSecond = 0
	LitersPerKilometerPerSecond = 1
	QuadFeetPerSecond = 2
	GallonsPerFootPerMinute = 3
	GallonsPerMilePerMinute = 4
	QuadMeterPerSecond = 5
	CubicMetersPerKilometerPerSecond = 6
	LitersPerMeterPerSecond = 7

class DimensionIndex(Enum):
	None = 0
	Angle = 1
	Area = 2
	Concentration = 3
	Currency = 4
	CurrencyPerEnergy = 5
	CurrencyPerLength = 6
	Diffusivity = 7
	ElectricalFrequency = 8
	EmitterCoefficient = 9
	Energy = 10
	Flow = 11
	FlowDensityPerArea = 12
	FlowDensityPerCapita = 13
	InfiltrationRate = 14
	Length = 15
	Mass = 16
	MassRate = 17
	NthOrderBulkReactionRate = 18
	Percent = 19
	Population = 20
	PopulationDensityPerArea = 21
	Power = 22
	Pressure = 23
	RainfallIntensity = 24
	ReactionRate = 25
	RotationalFrequency = 26
	Scale = 27
	Slope = 28
	SpecificWeight = 29
	SurfaceReactionRate = 30
	Temperature = 31
	Time = 32
	Unitless = 33
	Velocity = 34
	Volume = 35
	WeirCoefficient = 36
	ZeroOrderSurfaceReactionRate = 37
	DiameterLength = 38
	MassPerArea = 39
	Inertia = 40
	CurrencyPerPower = 41
	CostPerUnitVolume = 42
	EnergyPerUnitVolume = 43
	Torque = 44
	SpringConstant = 45
	Force = 46
	Density = 47
	DischargePerPressureDrop = 48
	VolumePerLength = 49
	SideWeirCoefficient = 50
	InfiltrationPerUnitDepth = 51
	PressurePerLength = 52
	MassPerLength = 53
	PerLength = 54
	PerPressure = 55
	DynamicViscosity = 56
	CalorificValue = 57
	WeirCoefficientParameterized = 58
	SnowMeltCoefficient = 59
	BreakRate = 60
	MassPerEnergy = 61
	ValveOpenCloseRateCoefficient = 62
	EnergyPerPower = 63
	DrainCoefficientUnit = 64
	NumberPerVolume = 65
	NumberPerArea = 66
	MolesPerVolume = 67
	MolesPerArea = 68
	ValveOpenCloseRateCoefficientPerFlow = 69
	FlowPerUnitLength = 70
	Acceleration = 71

class UnitIndex(Enum):
	None = 0
	AcreFeet = 1
	AcreFeetPerDay = 2
	AcreFeetPerHour = 3
	AcreFeetPerMinute = 4
	AcreInches = 5
	AcreInchPerHour = 6
	AcreInchPerMinute = 7
	Acres = 8
	AngleDegrees = 9
	AngleMinutes = 10
	AngleQuadrants = 11
	AngleRadians = 12
	AngleRevolutions = 13
	AngleSeconds = 14
	Atmospheres = 15
	Bars = 16
	Capita = 17
	Celsius = 18
	CentimeterPerMeter = 19
	Centimeters = 20
	CentimetersPerDay = 21
	CentimetersPerHour = 22
	CentimetersPerMinute = 23
	Centistokes = 24
	CFM = 25
	CFMPerPSI = 26
	CFS = 27
	CFSPerPSI = 28
	CFSPerAcres = 29
	CFSPerSquareFeet = 30
	CFSPerSquareMiles = 31
	CubicCentimeters = 32
	CubicFeet = 33
	CubicFeetPerDay = 34
	CubicFeetPerDayPerPSI = 35
	CubicFeetPerMinute = 36
	CubicFeetPerMinutePerPSI = 37
	CubicFeetPerSecond = 38
	CubicFeetPerSecondPerPSI = 39
	CubicInches = 40
	CubicMeters = 41
	CubicMetersPerDay = 42
	CubicMetersPerDayPerMetersOfH2O = 43
	CubicMetersPerHour = 44
	CubicMetersPerHourPerMetersOfH2O = 45
	CubicMetersPerMinute = 46
	CubicMetersPerMinutePerMetersOfH2O = 47
	CubicMetersPerSecond = 48
	CubicMetersPerSecondPerMetersOfH2O = 49
	CubicMetersPerHectaresPerDay = 50
	CubicMetersPerSquareKilometerPerDay = 51
	CubicMetersPerSquareMeterPerDay = 52
	CubicYards = 53
	Customer = 54
	Days = 55
	Decimeters = 56
	Dollars = 57
	DollarsPerFoot = 58
	DollarsPerMeter = 59
	DollarsPerKiloWattHour = 60
	Employee = 61
	Fahrenheit = 62
	Feet = 63
	FeetOfH2O = 64
	FeetPerDay = 65
	FeetPerInch = 66
	FootHorizontalPerFootVertical = 67
	FootPer1000Feet = 68
	FootPerFoot = 69
	FootPerMile = 70
	FootPoundals = 71
	FootVerticalPerFootHorizontal = 72
	Gallons = 73
	GallonsPerDay = 74
	GallonsPerDayPerPSI = 75
	GallonsPerMinute = 76
	GallonsPerMinutePerPSI = 77
	GallonsPerSecond = 78
	GallonsPerSecondPerPSI = 79
	GPDPerAcres = 80
	GPDPerCapita = 81
	GPDPerSquareFeet = 82
	GPDPerSquareMile = 83
	GPM = 84
	GPMPerAcres = 85
	GPMPerPSI = 86
	GPMPerSquareFeet = 87
	GPMPerSquareMile = 88
	Gram = 89
	GramsPerDay = 90
	GramsPerHour = 91
	GramsPerMinute = 92
	GramsPerSecond = 93
	Guest = 94
	Hectares = 95
	Hertz = 96
	HorizontalPerVertical = 97
	Horsepower = 98
	Hours = 99
	HundredCapita = 100
	ImperialGallonsPerDay = 101
	ImperialGallonsPerMinute = 102
	ImperialGallonsPerSecond = 103
	ImpGallons = 104
	ImperialGallonsPerDayPerPSI = 105
	ImperialGallonsPerMinutePerPSI = 106
	ImperialGallonsPerSecondPerPSI = 107
	Inches = 108
	InchesPerDay = 109
	InchesPerHour = 110
	InchesPerMinute = 111
	InchPerFoot = 112
	InfiltrationRateCentimetersPerDay = 113
	InfiltrationRateCentimetersPerHour = 114
	InfiltrationRateCentimetersPerMinute = 115
	InfiltrationRateInchesPerDay = 116
	InfiltrationRateInchesPerHour = 117
	InfiltrationRateInchesPerMinute = 118
	InfiltrationRateMillimetersPerDay = 119
	InfiltrationRateMillimetersPerHour = 120
	InfiltrationRateMillimetersPerMinute = 121
	Joules = 122
	Kilograms = 123
	KilogramsPerDay = 124
	KilogramsPerHour = 125
	KilogramsPerMinute = 126
	KilogramsPerSecond = 127
	KilogramsPerSquareCentimeter = 128
	KiloJoules = 129
	Kilometers = 130
	KiloNewtonsPerCubicMeter = 131
	KiloPascals = 132
	KiloWattHours = 133
	Kilowatts = 134
	Liters = 135
	LitersPerCapitaPerDay = 136
	LitersPerDay = 137
	LitersPerDayPerMetersOfH2O = 138
	LitersPerMinute = 139
	LitersPerMinutePerMetersOfH2O = 140
	LitersPerSecond = 141
	LitersPerSecondPerMetersOfH2O = 142
	LitersPerHectaresPerDay = 143
	LitersPerSquareKilometerPerDay = 144
	LitersPerSquareMeterPerDay = 145
	MegaLitersPerDay = 146
	MegaLitersPerDayPerMetersOfH2O = 147
	MeterHorizontalPerMeterVertical = 148
	MeterPerKilometer = 149
	MeterPerMeter = 150
	Meters = 151
	MetersOfH2O = 152
	MetersPerCm = 153
	MetersPerDay = 154
	MetersPerSecond = 155
	MeterVerticalPerMeterHorizontal = 156
	Mfeet = 157
	MGD = 158
	MGDPerPSI = 159
	MGDImperial = 160
	MGDImperialPerPSI = 161
	MicrogramsPerDay = 162
	MicrogramsPerHour = 163
	MicrogramsPerLiter = 164
	MicrogramsPerLiterNPerDay = 165
	MicrogramsPerLiterNPerSecond = 166
	MicrogramsPerMinute = 167
	MicrogramsPerSecond = 168
	MicrogramsPerSquareFeetPerDay = 169
	MicrogramsPerSquareMeterPerDay = 170
	MicrogramsPerSquareMeterPerSecond = 171
	Miles = 172
	Millifeet = 173
	Milligram = 174
	MilliGramsPerDay = 175
	MilliGramsPerHour = 176
	MilligramsPerLiter = 177
	MilligramsPerLiterNPerDay = 178
	MilligramsPerLiterNPerSecond = 179
	MilliGramsPerMinute = 180
	MilliGramsPerSecond = 181
	MilliGramsPerSquareFeetPerDay = 182
	MilliGramsPerSquareMeterPerDay = 183
	MilliGramsPerSquareMeterPerSecond = 184
	MillimeterHorizontalPerMeterVertical = 185
	MillimeterPerMeter = 186
	Millimeters = 187
	MillimetersOfH2O = 188
	MilliMetersPerDay = 189
	MilliMetersPerHour = 190
	MillimetersPerMinute = 191
	MillimeterVerticalPerMeterHorizontal = 192
	MillionGallons = 193
	MillionLiters = 194
	Minutes = 195
	NewtonsPerCubicMeter = 196
	NewtonsPerSquareMeter = 197
	OneOverSlope = 198
	PartsPerBillion = 199
	PartsPerBillionNPerDay = 200
	PartsPerBillionNPerSecond = 201
	PartsPerMillion = 202
	PartsPerMillionNPerDay = 203
	PartsPerMillionNPerSecond = 204
	Passenger = 205
	PerDay = 206
	PercentPercent = 207
	PercentSlope = 208
	PerSecond = 209
	Person = 210
	PersonsPerAcre = 211
	PersonsPerSquareFeet = 212
	PersonsPerSquareKilometer = 213
	PersonsPerHectares = 214
	PersonsPerSquareMeter = 215
	PersonsPerSquareMile = 216
	Pounds = 217
	PoundsForcePerCubicFoot = 218
	PoundsPerCubicFoot = 219
	PoundsPerCubicFootNPerDay = 220
	PoundsPerCubicFootNPerSecond = 221
	PoundsPerDay = 222
	PoundsPerHour = 223
	PoundsPerMillionGallons = 224
	PoundsPerMillionGallonsNPerDay = 225
	PoundsPerMillionGallonsNPerSecond = 226
	PoundsPerMinute = 227
	PoundsPerSecond = 228
	PoundsPerSquareFoot = 229
	PoundsPerSquareInch = 230
	PSI = 231
	Resident = 232
	RPM = 233
	Seconds = 234
	SquareCentimeters = 235
	SquareFeet = 236
	SquareFeetPerSecond = 237
	SquareInches = 238
	SquareKilometers = 239
	SquareMeters = 240
	SquareMetersPerSecond = 241
	SquareMiles = 242
	SquareMillimeters = 243
	SquareYards = 244
	Stokes = 245
	Student = 246
	ThousandCapita = 247
	ThousandGallons = 248
	ThousandLiters = 249
	ThousandSquareFeet = 250
	UnitlessPercent = 251
	UnitlessUnit = 252
	VelocityCentimetersPerHour = 253
	VelocityCentimetersPerMinute = 254
	VelocityCentimetersPerSecond = 255
	VelocityFeetPerHour = 256
	VelocityFeetPerMinute = 257
	VelocityFeetPerSecond = 258
	VelocityInchesPerHour = 259
	VelocityInchesPerMinute = 260
	VelocityInchesPerSecond = 261
	VelocityKilometersPerHour = 262
	VelocityKnot = 263
	VelocityKnotInternational = 264
	VelocityMetersPerHour = 265
	VelocityMetersPerMinute = 266
	VelocityMetersPerSecond = 267
	VelocityMilePerHour = 268
	VerticalPerHorizontal = 269
	Watts = 270
	WeirCoefficientSi = 271
	WeirCoefficientUs = 272
	Yards = 273
	Years = 274
	MillionLitersPerDay = 275
	PerMinute = 276
	InchMiles = 277
	InchFeet = 278
	FootMiles = 279
	FootFeet = 280
	MillimeterMeters = 281
	MillimeterKilometers = 282
	MeterMeters = 283
	MeterKilometers = 284
	InchMeters = 285
	MillimeterMiles = 286
	PoundsPerAcre = 287
	KilogramsPerHectare = 288
	DollarsPerKiloWatt = 289
	PoundSquareFeet = 290
	NewtonSquareMeters = 291
	DollarsPerHorsepower = 292
	DollarsPerCubicCentimeters = 293
	DollarsPerLiters = 294
	DollarsPerCubicMeters = 295
	DollarsPerCubicInches = 296
	DollarsPerGallons = 297
	DollarsPerImpGallons = 298
	DollarsPerCubicFeet = 299
	DollarsPerCubicYards = 300
	DollarsPerAcreInches = 301
	DollarsPerAcreFeet = 302
	DollarsPerMillionGallons = 303
	DollarsPerThousandGallons = 304
	DollarsPerThousandLiters = 305
	DollarsPerMillionLiters = 306
	KilogramsPerSquareMeter = 307
	KiloWattHourPerMillionGallons = 308
	KiloWattHourPerMillionLiters = 309
	KiloWattHourPerCubicMeters = 310
	KiloWattHourPerCubicFeet = 311
	PerHour = 312
	NewtonMeters = 313
	PoundFeet = 314
	PoundPerInch = 315
	NewtonPerMillimeter = 316
	PoundForce = 317
	KiloPoundForce = 318
	Newton = 319
	KiloNewton = 320
	SlugPerCubicFoot = 321
	PoundPerCubicFoot = 322
	KilogramPerCubicMeter = 323
	CfsPerSquareRootFooH20 = 324
	CmsPerSquareRootMeterH20 = 325
	LPerSecPerSquareRootKpa = 326
	GpmPerSquareRootPsi = 327
	Milliseconds = 328
	KilogramSquareMeters = 329
	Pascals = 330
	GPD = 331
	SideWeirCoefficientSi = 332
	SideWeirCoefficientUs = 333
	CubicFeetPerFoot = 334
	CubicMetersPerMeter = 335
	InchesPerHourPerFeetToKexp = 336
	CentimeterPerHourPerMeterToKexp = 337
	HektoPascals = 338
	MegaPascals = 339
	MilliBars = 340
	Kelvin = 341
	LitersPerHour = 342
	Tons = 343
	MegaWatts = 344
	GigaWatts = 345
	MegaJoules = 346
	GigaJoules = 347
	WattSeconds = 348
	MegaWattHours = 349
	GigaWattHours = 350
	KilogramsPerMeterPerSecond = 351
	PerPascals = 352
	PerBars = 353
	PerMeter = 354
	PerMillimeter = 355
	KilogramsPerMeter = 356
	PascalsPerMeter = 357
	BarsPerKilometer = 358
	JoulesPerCubicMeters = 359
	KiloJoulesPerCubicMeters = 360
	MegaJoulesPerCubicMeters = 361
	KiloWattHoursPerCubicMeters = 362
	WeirCoefficientParameterizedUS = 363
	WeirCoefficientParameterizedSI = 364
	MillimetersPerHourPerDegreeCelsius = 365
	InchesPerHourPerDegreeFahrenheit = 366
	BreaksPerYrPerKm = 367
	BreaksPerYrPerMi = 368
	BreaksPerYrPer1000Ft = 369
	USSurveyFoot = 370
	PoundSecondPerSquareFoot = 371
	PoundsPerFoot = 372
	PSIPerFoot = 373
	PSIPerInch = 374
	PerPSI = 375
	BreaksPerYrPer100Mi = 376
	PoundsPerKilowattHour = 377
	KilogramsPerKilowattHour = 378
	TonnesPerMegaJoule = 379
	TonnesPerYear = 380
	PercentPerSecondPerMeterH2O = 381
	PercentPerSecondPerFtH2O = 382
	PercentPerSecondPerKiloPascal = 383
	PercentPerSecondPerPsi = 384
	KilowattHoursPerKilowatt = 385
	DrainCoeffInchesPerHour = 386
	DrainCoeffMMPerHour = 387
	MilligramsPerSquareFeet = 388
	MicrogramsPerSquareFeet = 389
	MilligramsPerSquareMeter = 390
	MicrogramsPerSquareMeter = 391
	MilligramsPerSquareCentimeter = 392
	MicrogramsPerSquareCentimeter = 393
	NumbersPerLiter = 394
	ThousandNumbersPerLiter = 395
	MillionNumbersPerLiter = 396
	NumbersPerSquareMeter = 397
	ThousandNumbersPerSquareMeter = 398
	MillionNumbersPerSquareMeter = 399
	NumbersPerSquareFeet = 400
	ThousandNumbersPerSquareFeet = 401
	MillionNumbersPerSquareFeet = 402
	NumbersPerSquareCentimeter = 403
	ThousandNumbersPerSquareCentimeter = 404
	MillionNumbersPerSquareCentimeter = 405
	MolesPerLiter = 406
	MilliMolesPerLiter = 407
	MolesPerSquareMeter = 408
	MilliMolesPerSquareMeter = 409
	MolesPerSquareFeet = 410
	MilliMolesPerSquareFeet = 411
	MolesPerSquareCentimeter = 412
	MilliMolesPerSquareCentimeter = 413
	PercentPerSecondPerCubicFeetPerSecond = 414
	PercentPerSecondPerCubicFeetPerMinute = 415
	PercentPerSecondPerCubicMeterPerSecond = 416
	PercentPerSecondPerCubicMeterPerMinute = 417
	PercentPerSecondPerLiterPerSecond = 418
	PercentPerSecondPerLiterPerMinute = 419
	PercentPerSecondPerGalPerSecond = 420
	PercentPerSecondPerGalPerMinute = 421
	MicrometersPerSecond = 422
	CubicFeetPerMilePerSecond = 423
	LitersPerKiliometersPerSecond = 424
	QuadFootPerSecond = 425
	GallonsPerFootPerMinute = 426
	GallonsPerMilePerMinute = 427
	QuadMetersPerSecond = 428
	CubicMetersPerKiliometerPerSecond = 429
	LitersPerMeterPerSecond = 430
	LitersPerHectaresPerSecond = 431
	MetersPerSquareSecond = 432
	FeetPerSquareSecond = 433

class UnitSystemIndex(Enum):
	None = 0
	Si = 1
	UsCustomary = 2
	Both = 3

class CurrencyBasedUnit(INamable):

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			``CurrencyBasedUnit`` : 
		"""
		pass

class WeirCoefficientParameterized(INamable):

	@overload
	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: WeirCoefficientParameterizedUnitConverter, enumVal: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``WeirCoefficientParameterizedUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``WeirCoefficientParameterizedUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: WeirCoefficientParameterizedUnitConverter, enumVal: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``WeirCoefficientParameterizedUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``WeirCoefficientParameterizedUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			bentleyName (``str``) :  bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterized`` : 
		"""
		pass

class WeirCoefficientParameterizedUnitConverter(IUnitConverter):

	def __init__(self, unitSystem: UnitSystemIndex) -> None:
		"""No Description

		Args
		--------
			unitSystem (``UnitSystemIndex``) :  unitSystem
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns
		--------
			``WeirCoefficientParameterizedUnitConverter`` : 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

class InfiltrationPerUnitDepthUnit(INamable):

	@overload
	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: InfiltrationPerUnitDepthConverter, enumVal: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``InfiltrationPerUnitDepthConverter``) :  converter
			enumVal (``int``) :  enumVal
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``InfiltrationPerUnitDepthConverter``) :  converter
			enumVal (``int``) :  enumVal
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: InfiltrationPerUnitDepthConverter, enumVal: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``InfiltrationPerUnitDepthConverter``) :  converter
			enumVal (``int``) :  enumVal
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``InfiltrationPerUnitDepthConverter``) :  converter
			enumVal (``int``) :  enumVal
			bentleyName (``str``) :  bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthUnit`` : 
		"""
		pass

class InfiltrationPerUnitDepthConverter(IUnitConverter):

	def __init__(self, infiltrationUnit: UnitIndex, depthUnit: UnitIndex) -> None:
		"""No Description

		Args
		--------
			infiltrationUnit (``UnitIndex``) :  infiltrationUnit
			depthUnit (``UnitIndex``) :  depthUnit
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthConverter`` : 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

	@property
	def BaseInfiltrationUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthConverter`` : 
		"""
		pass

	@property
	def BaseDepthUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthConverter`` : 
		"""
		pass

	@property
	def DepthUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthConverter`` : 
		"""
		pass

	@property
	def InfiltrationUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``InfiltrationPerUnitDepthConverter`` : 
		"""
		pass

class DrainageCoefficientUnit(INamable):

	@overload
	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: DrainageCoefficientUnitConverter, enumVal: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``DrainageCoefficientUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``DrainageCoefficientUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: DrainageCoefficientUnitConverter, enumVal: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``DrainageCoefficientUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			name (``str``) :  name
			dimension (``Dimension``) :  dimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			converter (``DrainageCoefficientUnitConverter``) :  converter
			enumVal (``int``) :  enumVal
			bentleyName (``str``) :  bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnit`` : 
		"""
		pass

class DrainageCoefficientUnitConverter(IUnitConverter):

	def __init__(self, infiltrationUnit: UnitIndex) -> None:
		"""No Description

		Args
		--------
			infiltrationUnit (``UnitIndex``) :  infiltrationUnit
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnitConverter`` : 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

	@property
	def BaseInfiltrationUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnitConverter`` : 
		"""
		pass

	@property
	def InfiltrationUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``DrainageCoefficientUnitConverter`` : 
		"""
		pass

class Dimension(INamable):

	@overload
	def __init__(self, astringName: str, aintEnumValue: int) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, astringName: str, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@staticmethod
	def FromIndex(aindex: DimensionIndex) -> Dimension:
		"""No Description

		Args
		--------
			aindex (``DimensionIndex``) :  aindex

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@overload
	def FromEnum(aint: int) -> Dimension:
		"""No Description

		Args
		--------
			aint (``int``) :  aint

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@overload
	def FromEnum(dimension: DimensionType) -> Dimension:
		"""No Description

		Args
		--------
			dimension (``DimensionType``) :  dimension

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	def FromName(asNameDimension: str) -> Dimension:
		"""No Description

		Args
		--------
			asNameDimension (``str``) :  asNameDimension

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@overload
	def Convert(adouble: float, dimensionType: DimensionType, aintFromUnit: int, aintToUnit: int) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			dimensionType (``DimensionType``) :  dimensionType
			aintFromUnit (``int``) :  aintFromUnit
			aintToUnit (``int``) :  aintToUnit

		Returns
		--------
			``float`` : 
		"""
		pass

	def AvailableUnitsSortedEx(self, currentUnit: int) -> List:
		"""No Description

		Args
		--------
			currentUnit (``int``) :  currentUnit

		Returns
		--------
			``List`` : 
		"""
		pass

	@overload
	def Convert(self, adouble: float, aintFromUnit: int, aintToUnit: int) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aintFromUnit (``int``) :  aintFromUnit
			aintToUnit (``int``) :  aintToUnit

		Returns
		--------
			``float`` : 
		"""
		pass

	def UnitFromEnum(self, aiEnumValue: int) -> Unit:
		"""No Description

		Args
		--------
			aiEnumValue (``int``) :  aiEnumValue

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Angle() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Area() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Concentration() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Currency() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def CurrencyPerEnergy() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def CurrencyPerLength() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Diffusivity() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def ElectricalFrequency() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def EmitterCoefficient() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Energy() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def EnergyPerPower() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Flow() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def FlowDensityPerArea() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def FlowDensityPerCapita() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRate() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Length() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Mass() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def MassPerEnergy() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def MassRate() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def _None() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def NthOrderBulkReactionRate() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Percent() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Population() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def PopulationDensityPerArea() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Pressure() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Power() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def RainfallIntensity() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def ReactionRate() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def RotationalFrequency() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Scale() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Slope() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def SpecificWeight() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def SurfaceReactionRate() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Temperature() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Time() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Unitless() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Velocity() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Volume() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def WeirCoefficient() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def ZeroOrderSurfaceReactionRate() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def DiameterLength() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def MassPerArea() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Inertia() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def CurrencyPerPower() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def CostPerUnitVolume() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def EnergyPerUnitVolume() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Torque() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def SpringConstant() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Force() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Density() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def DischargePerPressureDrop() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def VolumePerLength() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def SideWeirCoefficient() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationPerUnitDepth() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def PressurePerLength() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def MassPerLength() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def PerLength() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def PerPressure() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def DynamicViscosity() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def CalorificValue() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def WeirCoefficientParameterized() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def SnowMeltCoefficient() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def BreakRate() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def ValveOpenCloseRateCoefficient() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def DrainCoefficientUnit() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def NumberPerVolumeUnit() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def NumberPerAreaUnit() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def MolesPerVolumeUnit() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def MolesPerAreaUnit() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def ValveOpenCloseRateCoefficientPerFlow() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def FlowPerUnitLength() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@staticmethod
	@property
	def Acceleration() -> Dimension:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def AvailableUnitsSorted(self) -> List:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	@property
	def Units(self) -> ISet:
		"""No Description

		Returns
		--------
			``Dimension`` : 
		"""
		pass

class IUnitConverter:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

class NumericConversionHandler:

	def __init__(self, aunitStorage: Unit, anf: NumericFormatter) -> None:
		"""No Description

		Args
		--------
			aunitStorage (``Unit``) :  aunitStorage
			anf (``NumericFormatter``) :  anf
		"""
		pass

	def DependsOn(self, anf: NumericFormatter) -> bool:
		"""No Description

		Args
		--------
			anf (``NumericFormatter``) :  anf

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StorageDoubleFromViewDouble(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def StorageDoubleFromViewString(self, astring: str) -> float:
		"""No Description

		Args
		--------
			astring (``str``) :  astring

		Returns
		--------
			``float`` : 
		"""
		pass

	def StorageToViewFactor(self) -> float:
		"""No Description

		Returns
		--------
			``float`` : 
		"""
		pass

	def ViewDoubleFromStorageDouble(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ViewStringFromStorageDouble(self, adouble: float) -> str:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def Formatter(self) -> NumericFormatter:
		"""No Description

		Returns
		--------
			``NumericConversionHandler`` : 
		"""
		pass

	@property
	def StorageUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``NumericConversionHandler`` : 
		"""
		pass

class BaseDateTimeDelegate(ICloneable, ISerializable):

	def __init__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args
		--------
			object (``object``) :  object
			method (``IntPtr``) :  method
		"""
		pass

	def Invoke(self) -> datetime:
		"""No Description

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def BeginInvoke(self, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args
		--------
			callback (``AsyncCallback``) :  callback
			object (``object``) :  object

		Returns
		--------
			``IAsyncResult`` : 
		"""
		pass

	def EndInvoke(self, result: IAsyncResult) -> datetime:
		"""No Description

		Args
		--------
			result (``IAsyncResult``) :  result

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (``SerializationInfo``) :  info
			context (``StreamingContext``) :  context

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetInvocationList(self) -> List[Delegate]:
		"""No Description

		Returns
		--------
			``List[Delegate]`` : 
		"""
		pass

	def DynamicInvoke(self, args: List[object]) -> object:
		"""No Description

		Args
		--------
			args (``List[object]``) :  args

		Returns
		--------
			``object`` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

	@property
	def Method(self) -> MethodInfo:
		"""No Description

		Returns
		--------
			``BaseDateTimeDelegate`` : 
		"""
		pass

	@property
	def Target(self) -> object:
		"""No Description

		Returns
		--------
			``BaseDateTimeDelegate`` : 
		"""
		pass

class NumberFormatInfoLibrary:

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	@property
	def CurrentNumberFormatInfo(self) -> NumberFormatInfo:
		"""No Description

		Returns
		--------
			``NumberFormatInfoLibrary`` : 
		"""
		pass

	@property
	def CurrentCultureInfo(self) -> CultureInfo:
		"""No Description

		Returns
		--------
			``NumberFormatInfoLibrary`` : 
		"""
		pass

	@staticmethod
	@property
	def Current() -> NumberFormatInfoLibrary:
		"""No Description

		Returns
		--------
			``NumberFormatInfoLibrary`` : 
		"""
		pass

class NumericFormatter(INamable, IMementoable, ILabeled):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aboolIsStandardFormatter: bool, astringLabel: str) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, aboolIsStandardFormatter: bool, astringLabel: str) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, aboolIsStandardFormatter: bool, astringLabel: str) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aboolIsStandardFormatter (``bool``) :  aboolIsStandardFormatter
			astringLabel (``str``) :  astringLabel
		"""
		pass

	def add_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def CreateMemento(self) -> IMemento:
		"""No Description

		Returns
		--------
			``IMemento`` : 
		"""
		pass

	def DoubleFromDoubleUnit(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def DoubleUnitFromDouble(self, aunit: Unit, adouble: float) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def DoubleUnitFromString(self, aunit: Unit, astring: str) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit
			astring (``str``) :  astring

		Returns
		--------
			``float`` : 
		"""
		pass

	def InitializeDefaultsFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args
		--------
			anf (``NumericFormatter``) :  anf

		Returns
		--------
			``None`` : 
		"""
		pass

	def InitializeFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args
		--------
			anf (``NumericFormatter``) :  anf

		Returns
		--------
			``None`` : 
		"""
		pass

	def ResetDefault(self, aunitsystem: UnitSystem) -> None:
		"""No Description

		Args
		--------
			aunitsystem (``UnitSystem``) :  aunitsystem

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetMemento(self, aimemento: IMemento) -> bool:
		"""No Description

		Args
		--------
			aimemento (``IMemento``) :  aimemento

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StringFromDoubleUnit(self, adouble: float, aunit: Unit) -> str:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def DecimalDigits(self) -> int:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@DecimalDigits.setter
	def DecimalDigits(self, decimaldigits: int) -> None:
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@property
	def DisplayUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@DisplayUnit.setter
	def DisplayUnit(self, displayunit: Unit) -> None:
		pass

	@property
	def DisplayUnitLabel(self) -> str:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@property
	def FormatCode(self) -> str:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: str) -> None:
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@property
	def NumericFormatterId(self) -> int:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@NumericFormatterId.setter
	def NumericFormatterId(self, numericformatterid: int) -> None:
		pass

	@property
	def IsStandardFormatter(self) -> bool:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@property
	def Places(self) -> int:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@Places.setter
	def Places(self, places: int) -> None:
		pass

	@property
	def DateTimeFormatForBinding(self) -> int:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@DateTimeFormatForBinding.setter
	def DateTimeFormatForBinding(self, datetimeformatforbinding: int) -> None:
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@property
	def XmlDisplayUnit(self) -> str:
		"""No Description

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	@XmlDisplayUnit.setter
	def XmlDisplayUnit(self, xmldisplayunit: str) -> None:
		pass

class StationFormatter(INamable, IMementoable, ILabeled):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
		"""
		pass

	def DoubleUnitFromString(self, aunit: Unit, astring: str) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit
			astring (``str``) :  astring

		Returns
		--------
			``float`` : 
		"""
		pass

	def InitializeFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args
		--------
			anf (``NumericFormatter``) :  anf

		Returns
		--------
			``None`` : 
		"""
		pass

	def StringFromDoubleUnit(self, adouble: float, aunit: Unit) -> str:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``str`` : 
		"""
		pass

	def add_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def CreateMemento(self) -> IMemento:
		"""No Description

		Returns
		--------
			``IMemento`` : 
		"""
		pass

	def DoubleFromDoubleUnit(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def DoubleUnitFromDouble(self, aunit: Unit, adouble: float) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def InitializeDefaultsFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args
		--------
			anf (``NumericFormatter``) :  anf

		Returns
		--------
			``None`` : 
		"""
		pass

	def ResetDefault(self, aunitsystem: UnitSystem) -> None:
		"""No Description

		Args
		--------
			aunitsystem (``UnitSystem``) :  aunitsystem

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetMemento(self, aimemento: IMemento) -> bool:
		"""No Description

		Args
		--------
			aimemento (``IMemento``) :  aimemento

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def Places(self) -> int:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@Places.setter
	def Places(self, places: int) -> None:
		pass

	@property
	def DecimalDigits(self) -> int:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@DecimalDigits.setter
	def DecimalDigits(self, decimaldigits: int) -> None:
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@property
	def DisplayUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@DisplayUnit.setter
	def DisplayUnit(self, displayunit: Unit) -> None:
		pass

	@property
	def DisplayUnitLabel(self) -> str:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@property
	def FormatCode(self) -> str:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: str) -> None:
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@property
	def NumericFormatterId(self) -> int:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@NumericFormatterId.setter
	def NumericFormatterId(self, numericformatterid: int) -> None:
		pass

	@property
	def IsStandardFormatter(self) -> bool:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@property
	def DateTimeFormatForBinding(self) -> int:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@DateTimeFormatForBinding.setter
	def DateTimeFormatForBinding(self, datetimeformatforbinding: int) -> None:
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@property
	def XmlDisplayUnit(self) -> str:
		"""No Description

		Returns
		--------
			``StationFormatter`` : 
		"""
		pass

	@XmlDisplayUnit.setter
	def XmlDisplayUnit(self, xmldisplayunit: str) -> None:
		pass

class DateTimeFormatter(INamable, IMementoable, ILabeled):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, baseDateTimeDelegate: BaseDateTimeDelegate) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, baseDateTimeDelegate: BaseDateTimeDelegate) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
		"""
		pass

	@overload
	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, baseDateTimeDelegate: BaseDateTimeDelegate) -> None:
		"""No Description

		Args
		--------
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
			aintId (``int``) :  aintId
			asName (``str``) :  asName
			aunit (``Unit``) :  aunit
			asFormatCode (``str``) :  asFormatCode
			aintDecimalDigits (``int``) :  aintDecimalDigits
			aunitDisplayDefaultSi (``Unit``) :  aunitDisplayDefaultSi
			aunitDisplayDefaultUs (``Unit``) :  aunitDisplayDefaultUs
			baseDateTimeDelegate (``BaseDateTimeDelegate``) :  baseDateTimeDelegate
		"""
		pass

	def DoubleUnitFromString(self, aunit: Unit, astring: str) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit
			astring (``str``) :  astring

		Returns
		--------
			``float`` : 
		"""
		pass

	def InitializeFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args
		--------
			anf (``NumericFormatter``) :  anf

		Returns
		--------
			``None`` : 
		"""
		pass

	def StringFromDoubleUnit(self, adouble: float, aunit: Unit) -> str:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``str`` : 
		"""
		pass

	def SetDateTimeFormat(self, dateTimeFormat: DateTimeFormats) -> None:
		"""No Description

		Args
		--------
			dateTimeFormat (``DateTimeFormats``) :  dateTimeFormat

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetDateTimeFormatString(self, formatString: str, formatIncludesDate: bool, formatIncludesTime: bool) -> None:
		"""No Description

		Args
		--------
			formatString (``str``) :  formatString
			formatIncludesDate (``bool``) :  formatIncludesDate
			formatIncludesTime (``bool``) :  formatIncludesTime

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def CreateMemento(self) -> IMemento:
		"""No Description

		Returns
		--------
			``IMemento`` : 
		"""
		pass

	def DoubleFromDoubleUnit(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def DoubleUnitFromDouble(self, aunit: Unit, adouble: float) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def InitializeDefaultsFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args
		--------
			anf (``NumericFormatter``) :  anf

		Returns
		--------
			``None`` : 
		"""
		pass

	def ResetDefault(self, aunitsystem: UnitSystem) -> None:
		"""No Description

		Args
		--------
			aunitsystem (``UnitSystem``) :  aunitsystem

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetMemento(self, aimemento: IMemento) -> bool:
		"""No Description

		Args
		--------
			aimemento (``IMemento``) :  aimemento

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def DateTimeFormatString(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def FullDateTimeFormatString(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def DateTimeFormatForBinding(self) -> int:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@DateTimeFormatForBinding.setter
	def DateTimeFormatForBinding(self, datetimeformatforbinding: int) -> None:
		pass

	@property
	def DateTimeFormat(self) -> DateTimeFormats:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@DateTimeFormat.setter
	def DateTimeFormat(self, datetimeformat: DateTimeFormats) -> None:
		pass

	@property
	def HasUnitToDisplay(self) -> bool:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def FormatCode(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: str) -> None:
		pass

	@property
	def DecimalDigits(self) -> int:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@DecimalDigits.setter
	def DecimalDigits(self, decimaldigits: int) -> None:
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def DisplayUnit(self) -> Unit:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@DisplayUnit.setter
	def DisplayUnit(self, displayunit: Unit) -> None:
		pass

	@property
	def DisplayUnitLabel(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@property
	def NumericFormatterId(self) -> int:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@NumericFormatterId.setter
	def NumericFormatterId(self, numericformatterid: int) -> None:
		pass

	@property
	def IsStandardFormatter(self) -> bool:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def Places(self) -> int:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@Places.setter
	def Places(self, places: int) -> None:
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@property
	def XmlDisplayUnit(self) -> str:
		"""No Description

		Returns
		--------
			``DateTimeFormatter`` : 
		"""
		pass

	@XmlDisplayUnit.setter
	def XmlDisplayUnit(self, xmldisplayunit: str) -> None:
		pass

class Unit(INamable):

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@overload
	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			adouble (``float``) :  adouble
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			astringName (``str``) :  astringName
			adimension (``Dimension``) :  adimension
			aunitsystem (``UnitSystem``) :  aunitsystem
			aiunitconverter (``IUnitConverter``) :  aiunitconverter
			aintEnumValue (``int``) :  aintEnumValue
			bentleyName (``str``) :  bentleyName
		"""
		pass

	@staticmethod
	def FromDimensionEnum(adimension: Dimension, aint: int) -> Unit:
		"""No Description

		Args
		--------
			adimension (``Dimension``) :  adimension
			aint (``int``) :  aint

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	def FromDimensionName(adimension: Dimension, asNameUnit: str) -> Unit:
		"""No Description

		Args
		--------
			adimension (``Dimension``) :  adimension
			asNameUnit (``str``) :  asNameUnit

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	def FromLabel(adimension: Dimension, aUnitLabel: str) -> Unit:
		"""No Description

		Args
		--------
			adimension (``Dimension``) :  adimension
			aUnitLabel (``str``) :  aUnitLabel

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	def FromIndex(aindex: UnitIndex) -> Unit:
		"""No Description

		Args
		--------
			aindex (``UnitIndex``) :  aindex

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	def FromSerializedString(astring: str) -> Unit:
		"""No Description

		Args
		--------
			astring (``str``) :  astring

		Returns
		--------
			``Unit`` : 
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args
		--------
			aunit (``Unit``) :  aunit

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	@staticmethod
	@property
	def AcreFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AcreFeetPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AcreFeetPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AcreFeetPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AcreInches() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AcreInchPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AcreInchPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Acres() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AngleDegrees() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AngleMinutes() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AngleQuadrants() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AngleRadians() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AngleRevolutions() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def AngleSeconds() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Atmospheres() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Bars() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Capita() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Celsius() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CentimeterPerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Centimeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CentimetersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CentimetersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CentimetersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Centistokes() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CFM() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CFMPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CFS() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CFSPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CFSPerAcres() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CFSPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CFSPerSquareMiles() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicCentimeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerDayPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerMinutePerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerSecondPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicInches() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerDayPerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerHourPerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerMinutePerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerSecondPerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerHectaresPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerSquareKilometerPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicYards() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Customer() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Days() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Decimeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Dollars() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerKiloWattHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Employee() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Fahrenheit() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Feet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FeetOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FeetPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FeetPerInch() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootHorizontalPerFootVertical() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootPer1000Feet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootPerFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootPerMile() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootPoundals() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootVerticalPerFootHorizontal() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Gallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerDayPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerMinutePerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerSecondPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPD() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPDPerAcres() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPDPerCapita() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPDPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPDPerSquareMile() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPM() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPMPerAcres() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPMPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPMPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GPMPerSquareMile() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Gram() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GramsPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GramsPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GramsPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GramsPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Guest() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Hectares() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Hertz() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def HorizontalPerVertical() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Horsepower() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Hours() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def HundredCapita() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ImperialGallonsPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ImperialGallonsPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ImperialGallonsPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ImpGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ImperialGallonsPerDayPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ImperialGallonsPerMinutePerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ImperialGallonsPerSecondPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Inches() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchesPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchesPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchesPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchPerFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateCentimetersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateCentimetersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateCentimetersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateInchesPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateInchesPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateInchesPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateMillimetersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateMillimetersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InfiltrationRateMillimetersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Joules() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Kilograms() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerKilowattHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloJoules() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Kilometers() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloNewtonsPerCubicMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloPascals() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloWattHours() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilowattHoursPerKilowatt() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Kilowatts() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Liters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerCapitaPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerDayPerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerMinutePerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerSecondPerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerHectaresPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerHectaresPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerSquareKilometerPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MegaLitersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MegaLitersPerDayPerMetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MeterHorizontalPerMeterVertical() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MeterPerKilometer() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MeterPerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Meters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MetersPerCm() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MetersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MetersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MeterVerticalPerMeterHorizontal() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Mfeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MGD() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MGDPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MGDImperial() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MGDImperialPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerLiter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerLiterNPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerLiterNPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerSquareFeetPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerSquareMeterPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Miles() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Millifeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Milligram() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliGramsPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliGramsPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilligramsPerLiter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilligramsPerLiterNPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilligramsPerLiterNPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliGramsPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliGramsPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliGramsPerSquareFeetPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliGramsPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliGramsPerSquareMeterPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimeterHorizontalPerMeterVertical() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimeterPerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Millimeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimetersOfH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliMetersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliMetersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimetersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimeterVerticalPerMeterHorizontal() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillionGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillionLiters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillionLitersPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Milliseconds() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Minutes() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NewtonsPerCubicMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NewtonsPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def OneOverSlope() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def _None() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PartsPerBillion() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PartsPerBillionNPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PartsPerBillionNPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PartsPerMillion() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PartsPerMillionNPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PartsPerMillionNPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Passenger() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPercent() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentSlope() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Person() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PersonsPerAcre() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PersonsPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PersonsPerSquareKilometer() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PersonsPerHectares() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PersonsPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PersonsPerSquareMile() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Pounds() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsForcePerCubicFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerCubicFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerCubicFootNPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerCubicFootNPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerKilowattHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerMillionGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerMillionGallonsNPerDay() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerMillionGallonsNPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerSquareFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerSquareInch() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Resident() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def RPM() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Seconds() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareCentimeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareFeetPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareInches() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareKilometers() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareMetersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareMiles() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareMillimeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SquareYards() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Stokes() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Student() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandCapita() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandLiters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def TonnesPerMegaJoule() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def TonnesPerYear() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def UnitlessPercent() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def UnitlessUnit() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def USSurveyFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityCentimetersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityCentimetersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityCentimetersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityFeetPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityFeetPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityFeetPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityInchesPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityInchesPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityInchesPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityKilometersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityKnot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityKnotInternational() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityMetersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityMetersPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityMetersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VelocityMilePerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def VerticalPerHorizontal() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Watts() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def WeirCoefficientSi() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def WeirCoefficientUs() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Yards() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Years() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchMiles() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootMiles() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FootFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimeterMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimeterKilometers() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MeterMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MeterKilometers() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimeterMiles() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerAcre() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerHectare() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerKiloWatt() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerHorsepower() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerCubicCentimeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerLiters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerCubicMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerCubicInches() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerImpGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerCubicFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerCubicYards() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerAcreInches() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerAcreFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerMillionGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerThousandGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerThousandLiters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DollarsPerMillionLiters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NewtonSquareMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramSquareMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloWattHourPerMillionGallons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloWattHourPerMillionLiters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloWattHourPerCubicMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloWattHourPerCubicFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NewtonMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundPerInch() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NewtonPerMillimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundForce() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloPoundForce() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Newton() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloNewton() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SlugPerCubicFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundPerCubicFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramPerCubicMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CfsPerSquareRootFooH20() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CmsPerSquareRootMeterH20() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LPerSecPerSquareRootKpa() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GpmPerSquareRootPsi() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Pascals() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def HektoPascals() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MegaPascals() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliBars() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SideWeirCoefficientSi() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def SideWeirCoefficientUs() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchesPerHourPerFeetToKexp() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CentimeterPerHourPerMeterToKexp() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Kelvin() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def Tons() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MegaWatts() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GigaWatts() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MegaJoules() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GigaJoules() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def WattSeconds() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MegaWattHours() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GigaWattHours() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PascalsPerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def BarsPerKilometer() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PSIPerFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PSIPerInch() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundsPerFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerMillimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerPascals() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerBars() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KilogramsPerMeterPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PoundSecondPerSquareFoot() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def JoulesPerCubicMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloJoulesPerCubicMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MegaJoulesPerCubicMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def KiloWattHoursPerCubicMeters() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def WeirCoefficientParameterizedSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def WeirCoefficientParameterizedUS() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillimetersPerHourPerDegreeCelsius() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def InchesPerHourPerDegreeFahrenheit() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def BreaksPerYrPerKm() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def BreaksPerYrPerMi() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def BreaksPerYrPer1000Ft() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def BreaksPerYrPer100Mi() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerMeterH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerFtH2O() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerKiloPascal() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerPSI() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerCubicFeetPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerCubicFeetPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerCubicMeterPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerCubicMeterPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerLiterPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerLiterPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerGalPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def PercentPerSecondPerGalPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MetersPerSquareSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def FeetPerSquareSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DrainCoeffInchesPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def DrainCoeffMMPerHour() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilligramsPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilligramsPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilligramsPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MicrogramsPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MolesPerLiter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliMolesPerLiter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NumbersPerLiter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandNumbersPerLiter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillionNumbersPerLiter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MolesPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MolesPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MolesPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliMolesPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliMolesPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MilliMolesPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NumbersPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NumbersPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def NumbersPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandNumbersPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandNumbersPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def ThousandNumbersPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillionNumbersPerSquareMeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillionNumbersPerSquareCentimeter() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def MillionNumbersPerSquareFeet() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicFeetPerMilePerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerKilometerPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def QuadFootPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerFootPerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def GallonsPerMilePerMinute() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def QuadMetersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def CubicMetersPerKilometerPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@staticmethod
	@property
	def LitersPerMetersPerSecond() -> Unit:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			``Unit`` : 
		"""
		pass

class UnitConversionManager:

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def AvailableDimensions(self) -> List:
		"""No Description

		Returns
		--------
			``List`` : 
		"""
		pass

	def DimensionAt(self, adimensionindex: DimensionIndex) -> Dimension:
		"""No Description

		Args
		--------
			adimensionindex (``DimensionIndex``) :  adimensionindex

		Returns
		--------
			``Dimension`` : 
		"""
		pass

	def UnitIndexFor(self, unit: Unit) -> UnitIndex:
		"""No Description

		Args
		--------
			unit (``Unit``) :  unit

		Returns
		--------
			``UnitIndex`` : 
		"""
		pass

	def UnitAt(self, aunitindex: UnitIndex) -> Unit:
		"""No Description

		Args
		--------
			aunitindex (``UnitIndex``) :  aunitindex

		Returns
		--------
			``Unit`` : 
		"""
		pass

	def UnitSystemAt(self, aunitsystemindex: UnitSystemIndex) -> UnitSystem:
		"""No Description

		Args
		--------
			aunitsystemindex (``UnitSystemIndex``) :  aunitsystemindex

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@staticmethod
	@property
	def Current() -> UnitConversionManager:
		"""No Description

		Returns
		--------
			``UnitConversionManager`` : 
		"""
		pass

	@staticmethod
	@property
	def EmitterExponent() -> float:
		"""No Description

		Returns
		--------
			``UnitConversionManager`` : 
		"""
		pass

	@EmitterExponent.setter
	@staticmethod
	def EmitterExponent(self, emitterexponent: float) -> None:
		pass

class UnitSystem(INamable):

	def __init__(self, astringName: str) -> None:
		"""No Description

		Args
		--------
			astringName (``str``) :  astringName
		"""
		pass

	@staticmethod
	def FromSerializedString(astring: str) -> UnitSystem:
		"""No Description

		Args
		--------
			astring (``str``) :  astring

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	@staticmethod
	@property
	def _None() -> UnitSystem:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@staticmethod
	@property
	def Si() -> UnitSystem:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@staticmethod
	@property
	def UsCustomary() -> UnitSystem:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@staticmethod
	@property
	def Both() -> UnitSystem:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns
		--------
			``UnitSystem`` : 
		"""
		pass

class ConversionException(ISerializable, _Exception):

	def __init__(self, asMessage: str) -> None:
		"""No Description

		Args
		--------
			asMessage (``str``) :  asMessage
		"""
		pass

	def GetBaseException(self) -> Exception:
		"""No Description

		Returns
		--------
			``Exception`` : 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args
		--------
			info (``SerializationInfo``) :  info
			context (``StreamingContext``) :  context

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Message(self) -> str:
		"""No Description

		Returns
		--------
			``ConversionException`` : 
		"""
		pass

	@property
	def Data(self) -> Dict:
		"""No Description

		Returns
		--------
			``ConversionException`` : 
		"""
		pass

	@property
	def InnerException(self) -> Exception:
		"""No Description

		Returns
		--------
			``ConversionException`` : 
		"""
		pass

	@property
	def TargetSite(self) -> MethodBase:
		"""No Description

		Returns
		--------
			``ConversionException`` : 
		"""
		pass

	@property
	def StackTrace(self) -> str:
		"""No Description

		Returns
		--------
			``ConversionException`` : 
		"""
		pass

	@property
	def HelpLink(self) -> str:
		"""No Description

		Returns
		--------
			``ConversionException`` : 
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
			``ConversionException`` : 
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
			``ConversionException`` : 
		"""
		pass

	@HResult.setter
	def HResult(self, hresult: int) -> None:
		pass

class FactorConverter(IUnitConverter):

	def __init__(self, adouble: float) -> None:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

class BaseUnitConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

class DegreesFahrenheitConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def FromBaseUnit(self, adoubleCelsius: float) -> float:
		"""No Description

		Args
		--------
			adoubleCelsius (``float``) :  adoubleCelsius

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, adoubleFahrenheit: float) -> float:
		"""No Description

		Args
		--------
			adoubleFahrenheit (``float``) :  adoubleFahrenheit

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

class KelvinConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	@overload
	def FromBaseUnit(self, adoubleCelsius: float) -> float:
		"""No Description

		Args
		--------
			adoubleCelsius (``float``) :  adoubleCelsius

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, adoubleKelvin: float) -> float:
		"""No Description

		Args
		--------
			adoubleKelvin (``float``) :  adoubleKelvin

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

class SlopeConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

class EmitterCoefficientConverterUS(IUnitConverter):

	def __init__(self, aTargetUnitFlowFactor: float) -> None:
		"""No Description

		Args
		--------
			aTargetUnitFlowFactor (``float``) :  aTargetUnitFlowFactor
		"""
		pass

	@overload
	def FromBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args
		--------
			aDouble (``float``) :  aDouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args
		--------
			aDouble (``float``) :  aDouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

class EmitterCoefficientConverterSI(IUnitConverter):

	def __init__(self, aTargetUnitFlowFactor: float) -> None:
		"""No Description

		Args
		--------
			aTargetUnitFlowFactor (``float``) :  aTargetUnitFlowFactor
		"""
		pass

	@overload
	def FromBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args
		--------
			aDouble (``float``) :  aDouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args
		--------
			aDouble (``float``) :  aDouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

	@overload
	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args
		--------
			adouble (``float``) :  adouble

		Returns
		--------
			``float`` : 
		"""
		pass

