from OpenFlows.Water.Domain.ModelingElements.Components import IMinorLossCoefficient, IPattern, IPumpDefinition, IValveCharacteristic, IGPVHeadlossCurve, ISCADASignal, TElementManagerType, TElementType, TUnitsType, IZone, IUnitDemandLoad, IAirFlowCurve
from OpenFlows.Domain.ModelingElements.Collections import ICollectionElement, ICollection, ICollectionElements
from typing import overload, Dict, List, Generic
from OpenFlows.Domain.ModelingElements import IElementUnits, IElementsResults, IElementResults, IElement, IGeometryUnits, TElementManagerType, TElementType, TUnitsType
from array import array
from OpenFlows.Units import IUnit
from enum import Enum
from OpenFlows.Water.Domain import ValveSettingType, TCVCoefficientType, PressureValvesettingType, ConstituentSourceType, PipeStatusType, TankSectionType
from Haestad.Support.Support import GeometryPoint
from OpenFlows.Domain.ModelingElements.NetworkElements import INetworkElements, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType, IActiveElementInput, IActiveElementsInput, INetworkElement, IBaseLinksResults, IBaseLinkResults, IBaseLinkInput, IBaseLinksInput, IBaseLinkUnits, IPointNodeInput, IPointNodesInput, IBasePolygonsInput, IBasePolygonsResults, IBasePolygonResults, IBasePolygonInput
from OpenFlows.Domain.DataObjects import INetwork


class VSPBFixedHeadType(Enum):
	HydraulicGrade = 0
	Pressure = 1

class WaterNetworkElementType(Enum):
	SCADAElement = 23
	Lateral = 24
	Tap = 26
	Tank = 52
	Hydrant = 54
	Junction = 55
	Reservoir = 56
	FCV = 60
	TCV = 61
	GPV = 62
	PRV = 64
	PSV = 65
	PBV = 66
	Pump = 68
	Pipe = 69
	SpotElevation = 70
	IsolationValve = 71
	VSPB = 72
	CustomerMeter = 73
	Turbine = 300
	AirValve = 301
	HydropneumaticTank = 302
	SurgeValve = 303
	DischargeToAtmosphere = 305
	RuptureDisk = 306
	OrificeBetweenTwoPipes = 307
	SurgeTank = 308
	CheckValve = 309
	ValveWithLinearAreaChange = 310
	PeriodicHeadFlow = 321
	PumpStation = 700

class SCADATargetAttribute(Enum):
	UnAssigned = 0
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

class TransientParameterType(Enum):
	Head = 0
	Flow = 1

class IMinorLoss(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Quantity(self) -> int:
		"""No Description

		Returns:
			IMinorLoss: 
		"""
		pass

	@Quantity.setter
	def Quantity(self, quantity: int) -> None:
		pass

	@property
	def MinorLossCoefficient(self) -> IMinorLossCoefficient:
		"""No Description

		Returns:
			IMinorLoss: 
		"""
		pass

	@MinorLossCoefficient.setter
	def MinorLossCoefficient(self, minorlosscoefficient: IMinorLossCoefficient) -> None:
		pass

class IMinorLosses(ICollection[IMinorLoss]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, quantity: int, minorLoss: IMinorLossCoefficient) -> IMinorLoss:
		"""No Description

		Args:
			quantity(int): quantity
			minorLoss(IMinorLossCoefficient): minorLoss

		Returns:
			IMinorLoss: 
		"""
		pass

	@overload
	def Add(self) -> IMinorLoss:
		"""No Description

		Returns:
			IMinorLoss: 
		"""
		pass

class IMinorLossCoefficientCollection(ICollectionElements[IMinorLosses, IMinorLoss, IMinorLossCollectionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IMinorLossCollectionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseDirectedNodesResults(IElementsResults, IWaterQualityElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CannotDeliverFlowsOrHead(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CannotDeliverFlowsOrHead(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CannotDeliverFlowsOrHead(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsOpen(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsOpen(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsOpen(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseDirectedNodeResults(IElementResults, IWaterQualityResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CannotDeliverFlowOrHead(self) -> Union[bool, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CannotDeliverFlowOrHead(self, timeStepIndex: int) -> Union[bool, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CannotDeliverFlowsOrHeads(self) -> array(Union[bool, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def IsOpen(self) -> Union[bool, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IsOpen(self, timeStepIndex: int) -> Union[bool, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def IsOpens(self) -> array(Union[bool, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IBaseDirectedNodeInput(IPhysicalNodeElementInput, IWaterZoneableNetworkElementInput, IWaterQualityElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DownstreamLink(self) -> IElement:
		"""No Description

		Returns:
			IBaseDirectedNodeInput: 
		"""
		pass

	@DownstreamLink.setter
	def DownstreamLink(self, downstreamlink: IElement) -> None:
		pass

	@property
	def InstallationYear(self) -> int:
		"""No Description

		Returns:
			IBaseDirectedNodeInput: 
		"""
		pass

	@InstallationYear.setter
	def InstallationYear(self, installationyear: int) -> None:
		pass

class IBaseDirectedNodesInput(IWaterZoneableNetworkElementsInput, IWaterQualityElementsInput, IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def InstallationYears(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InstallationYears(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseDirectedNodeUnits(IElementResults, IWaterQualityResultsUnits, IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseDirectedNodeUnits: 
		"""
		pass

class ICheckValveElementInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LocatedAtWye(self) -> bool:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@LocatedAtWye.setter
	def LocatedAtWye(self, locatedatwye: bool) -> None:
		pass

	@property
	def CheckValvePipeWithWye(self) -> IPipe:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@CheckValvePipeWithWye.setter
	def CheckValvePipeWithWye(self, checkvalvepipewithwye: IPipe) -> None:
		pass

	@property
	def FlowDirection(self) -> CheckValveFlowDirectionEnum:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@FlowDirection.setter
	def FlowDirection(self, flowdirection: CheckValveFlowDirectionEnum) -> None:
		pass

	@property
	def InitialTypicalFlow(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@InitialTypicalFlow.setter
	def InitialTypicalFlow(self, initialtypicalflow: float) -> None:
		pass

	@property
	def ThresholdPressure(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@ThresholdPressure.setter
	def ThresholdPressure(self, thresholdpressure: float) -> None:
		pass

	@property
	def ClosureTime(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@ClosureTime.setter
	def ClosureTime(self, closuretime: float) -> None:
		pass

	@property
	def OpenTime(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@OpenTime.setter
	def OpenTime(self, opentime: float) -> None:
		pass

	@property
	def AllowDisruptionOfOperation(self) -> bool:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@AllowDisruptionOfOperation.setter
	def AllowDisruptionOfOperation(self, allowdisruptionofoperation: bool) -> None:
		pass

class ICheckValveElementsInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def LocatedAtWyes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def LocatedAtWyes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FlowDirections(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FlowDirections(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialTypicalFlows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialTypicalFlows(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ThresholdPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ThresholdPressures(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ClosureTimes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ClosureTimes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def OpenTimes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def OpenTimes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AllowDisruptionOfOperations(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AllowDisruptionOfOperations(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICheckValveElementResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def AbsoluteFlow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def AbsoluteFlow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Pressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Pressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def HydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def HydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class ICheckValveElementsResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, ids: List[int], timeSTepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeSTepIndex(int): timeSTepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICheckValveUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICheckValveUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICheckValveUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICheckValveUnits: 
		"""
		pass

class ICheckValves(IWaterNetworkElements[ICheckValves, ICheckValve, ICheckValveUnits, ICheckValveElementInput, ICheckValveElementResults, ICheckValveElementsInput, ICheckValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICheckValve(IWaterNetworkElement[ICheckValves, ICheckValve, ICheckValveUnits, ICheckValveElementInput, ICheckValveElementResults, ICheckValveElementsInput, ICheckValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IOrificeBetweenTwoPipesInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TypicalPressureDrop(self) -> float:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesInput: 
		"""
		pass

	@TypicalPressureDrop.setter
	def TypicalPressureDrop(self, typicalpressuredrop: float) -> None:
		pass

	@property
	def TypicalFlow(self) -> float:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesInput: 
		"""
		pass

	@TypicalFlow.setter
	def TypicalFlow(self, typicalflow: float) -> None:
		pass

class IOrificesBetweenTwoPipesInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TypicalPressureDrops(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TypicalFlows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IOrificeBetweenTwoPipesResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Headloss(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Headloss(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def FromHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def FromHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def ToHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ToHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def FromPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def FromPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def ToPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ToPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def AbsoluteFlow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def AbsoluteFlow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IOrificesBetweenTwoPipesResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headloss(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headloss(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headloss(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrade(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrade(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrade(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrade(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrade(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrade(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressure(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressure(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressure(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressure(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressure(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressure(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AbsolueFlow(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlow(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlow(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IOrificeBetweenTwoPipesUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

class IOrificeBetweenTwoPipes(IWaterNetworkElement[IOrificesBetweenTwoPipes, IOrificeBetweenTwoPipes, IOrificeBetweenTwoPipesUnits, IOrificeBetweenTwoPipesInput, IOrificeBetweenTwoPipesResults, IOrificesBetweenTwoPipesInput, IOrificesBetweenTwoPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IOrificesBetweenTwoPipes(IWaterNetworkElements[IOrificesBetweenTwoPipes, IOrificeBetweenTwoPipes, IOrificeBetweenTwoPipesUnits, IOrificeBetweenTwoPipesInput, IOrificeBetweenTwoPipesResults, IOrificesBetweenTwoPipesInput, IOrificesBetweenTwoPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITurbineCurveCollection(ICollectionElements[ITurbineFlowHeads, ITurbineFlowHead, ITurbineCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITurbineFlowHeads(ICollection[ITurbineFlowHead]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, head: float) -> ITurbineFlowHead:
		"""No Description

		Args:
			flow(float): flow
			head(float): head

		Returns:
			ITurbineFlowHead: 
		"""
		pass

	@overload
	def Add(self) -> ITurbineFlowHead:
		"""No Description

		Returns:
			ITurbineFlowHead: 
		"""
		pass

class ITurbineFlowHead(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			ITurbineFlowHead: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@property
	def Head(self) -> float:
		"""No Description

		Returns:
			ITurbineFlowHead: 
		"""
		pass

	@Head.setter
	def Head(self, head: float) -> None:
		pass

class ITurbineCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineCurveUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineCurveUnits: 
		"""
		pass

class IElectricalTorqueCollection(ICollectionElements[IElectricalTorques, IElectricalTorque, IElectricalTorqueUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElectricalTorques(ICollection[IElectricalTorque]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, time: float, torque: float) -> IElectricalTorque:
		"""No Description

		Args:
			time(float): time
			torque(float): torque

		Returns:
			IElectricalTorque: 
		"""
		pass

	@overload
	def Add(self) -> IElectricalTorque:
		"""No Description

		Returns:
			IElectricalTorque: 
		"""
		pass

class IElectricalTorque(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> float:
		"""No Description

		Returns:
			IElectricalTorque: 
		"""
		pass

	@Time.setter
	def Time(self, time: float) -> None:
		pass

	@property
	def Torque(self) -> float:
		"""No Description

		Returns:
			IElectricalTorque: 
		"""
		pass

	@Torque.setter
	def Torque(self, torque: float) -> None:
		pass

class IElectricalTorqueUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IElectricalTorqueUnits: 
		"""
		pass

	@property
	def TorqueUnit(self) -> IUnit:
		"""No Description

		Returns:
			IElectricalTorqueUnits: 
		"""
		pass

class ITurbineInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeDelayUntilValveOperates(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@TimeDelayUntilValveOperates.setter
	def TimeDelayUntilValveOperates(self, timedelayuntilvalveoperates: float) -> None:
		pass

	@property
	def TimeForValveToOperate(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@TimeForValveToOperate.setter
	def TimeForValveToOperate(self, timeforvalvetooperate: float) -> None:
		pass

	@property
	def SphericalValveDiameter(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@SphericalValveDiameter.setter
	def SphericalValveDiameter(self, sphericalvalvediameter: float) -> None:
		pass

	@property
	def TurbineEfficiency(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@TurbineEfficiency.setter
	def TurbineEfficiency(self, turbineefficiency: float) -> None:
		pass

	@property
	def MomentOfInertia(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@MomentOfInertia.setter
	def MomentOfInertia(self, momentofinertia: float) -> None:
		pass

	@property
	def RotationalSpeed(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@RotationalSpeed.setter
	def RotationalSpeed(self, rotationalspeed: float) -> None:
		pass

	@property
	def GateOpeningPattern(self) -> IPattern:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@GateOpeningPattern.setter
	def GateOpeningPattern(self, gateopeningpattern: IPattern) -> None:
		pass

	@property
	def SpecificSpeed(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@SpecificSpeed.setter
	def SpecificSpeed(self, specificspeed: float) -> None:
		pass

	@property
	def TurbineInitialFlow(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@TurbineInitialFlow.setter
	def TurbineInitialFlow(self, turbineinitialflow: float) -> None:
		pass

	@property
	def TurbineInitialHead(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@TurbineInitialHead.setter
	def TurbineInitialHead(self, turbineinitialhead: float) -> None:
		pass

	@property
	def OperatingCase(self) -> TurbineOperatingCaseEnum:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@OperatingCase.setter
	def OperatingCase(self, operatingcase: TurbineOperatingCaseEnum) -> None:
		pass

	@property
	def ReportPeriod(self) -> int:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@ReportPeriod.setter
	def ReportPeriod(self, reportperiod: int) -> None:
		pass

	@property
	def TurbineInitialStatus(self) -> TurbineStatusEnum:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@TurbineInitialStatus.setter
	def TurbineInitialStatus(self, turbineinitialstatus: TurbineStatusEnum) -> None:
		pass

	@property
	def TurbineCurveCollection(self) -> ITurbineCurveCollection:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def ElectricalTorqueCollection(self) -> IElectricalTorqueCollection:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

class ITurbinesInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TimeDelayUntilValveOperates(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForValveToOperate(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SphericalValveDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineEfficiency(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MomentOfInertia(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RotationalSpeed(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GateOpeningPattern(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecificSpeed(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialFlow(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialHead(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OperatingCase(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriod(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialStatus(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITurbineResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Headloss(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Headloss(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def FromHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def FromHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def ToHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ToHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def FromPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def FromPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def ToPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ToPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def AbsoluteFlow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def AbsoluteFlow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	def MaximumTransientSpeed(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientSpeed(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

class ITurbinesResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AbsoluteFlows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientSpeeds(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientSpeeds(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITurbineUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def InertiaUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def RotationUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

class ITurbine(IWaterNetworkElement[ITurbines, ITurbine, ITurbineUnits, ITurbineInput, ITurbineResults, ITurbinesInput, ITurbinesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITurbines(IWaterNetworkElements[ITurbines, ITurbine, ITurbineUnits, ITurbineInput, ITurbineResults, ITurbinesInput, ITurbinesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBasePumpsResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedRelativeSpeedFactors(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedRelativeSpeedFactors(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedRelativeSpeedFactors(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def SuctionHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def SuctionHydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def SuctionHydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargeHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargeHydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargeHydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def SuctionPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def SuctionPressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def SuctionPressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargePressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargePressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargePressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpHeads(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpHeads(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpHeads(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AvailableNPSHs(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AvailableNPSHs(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AvailableNPSHs(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def RequiredNPSHs(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def RequiredNPSHs(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def RequiredNPSHs(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpExceedsOperatingRanges(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpExceedsOperatingRanges(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpExceedsOperatingRanges(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpStatuses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpStatuses(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PumpStatuses(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def WirePower(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def WirePower(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def WirePower(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBasePumpResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedRelativeSpeedFactor(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedRelativeSpeedFactor(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedRelativeSpeedFactors(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def SuctionHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def SuctionHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def SuctionHyraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def DischargeHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def DischargeHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def DischargeHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def SuctionPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def SuctionPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def SuctionPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def DischargePressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def DischargePressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def DischargePressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def PumpHead(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def PumpHead(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def PumpHeads(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def AvailableNPSH(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def AvailableNPSH(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def AvailableNPSHs(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def RequiredNPSH(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def RequiredNPSH(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def RequiredNPSHs(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def PumpExceedsOperatingRange(self) -> Union[bool, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def PumpExceedsOperatingRange(self, timeStepIndex: int) -> Union[bool, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def PumpExceedsOperatingRanges(self) -> array(Union[bool, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def CalculatedPumpStatus(self) -> Union[PumpStatusEnum, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedPumpStatus(self, timeStepIndex: int) -> Union[PumpStatusEnum, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedPumpStatuses(self) -> array(Union[PumpStatusEnum, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def WirePower(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def WirePower(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def WirePowers(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IBasePumpInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialRelativeSpeedFactor(self) -> float:
		"""No Description

		Returns:
			IBasePumpInput: 
		"""
		pass

	@InitialRelativeSpeedFactor.setter
	def InitialRelativeSpeedFactor(self, initialrelativespeedfactor: float) -> None:
		pass

	@property
	def InitialStatus(self) -> int:
		"""No Description

		Returns:
			IBasePumpInput: 
		"""
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: int) -> None:
		pass

class IBasePumpsInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def InitialRelativeSpeedFactors(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialRelativeSpeedFactors(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialStatus(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialStatus(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBasePumpUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeSpeedFactorUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def NPSHUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def PowerUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

class IPumps(IWaterNetworkElements[IPumps, IPump, IPumpUnits, IPumpInput, IPumpResults, IPumpsInput, IPumpsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPump(IWaterNetworkElement[IPumps, IPump, IPumpUnits, IPumpInput, IPumpResults, IPumpsInput, IPumpsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpsInput(IBasePumpsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpsResults(IBasePumpsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpResults(IBasePumpResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpInput(IBasePumpInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinition:
		"""No Description

		Returns:
			IPumpInput: 
		"""
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

class IPumpUnits(IBasePumpUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IVariableSpeedPumpBatterys(IWaterNetworkElements[IVariableSpeedPumpBatterys, IVariableSpeedPumpBattery, IVariableSpeedPumpBatteryUnits, IVSPBInput, IVSPBResults, IVSPBsInput, IVSPBsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IVariableSpeedPumpBattery(IWaterNetworkElement[IVariableSpeedPumpBatterys, IVariableSpeedPumpBattery, IVariableSpeedPumpBatteryUnits, IVSPBInput, IVSPBResults, IVSPBsInput, IVSPBsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IVSPBsInput(IBasePumpsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def PumpDefinitions(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ControlNodes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumRelativeSpeedFactors(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def NumberOfLagPumps(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ControlNodeOnSuctionSide(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetFlows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VSPBTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VSPBFixedHeadTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IVSPBInput(IBasePumpInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinition:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

	@property
	def ControlNode(self) -> IWaterElement:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@ControlNode.setter
	def ControlNode(self, controlnode: IWaterElement) -> None:
		pass

	@property
	def TargetHydraulicGrade(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@TargetHydraulicGrade.setter
	def TargetHydraulicGrade(self, targethydraulicgrade: float) -> None:
		pass

	@property
	def MaximumRelativeSpeedFactor(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@MaximumRelativeSpeedFactor.setter
	def MaximumRelativeSpeedFactor(self, maximumrelativespeedfactor: float) -> None:
		pass

	@property
	def NumberOfLagPumps(self) -> int:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@NumberOfLagPumps.setter
	def NumberOfLagPumps(self, numberoflagpumps: int) -> None:
		pass

	@property
	def ControlNodeOnSuctionSide(self) -> bool:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@ControlNodeOnSuctionSide.setter
	def ControlNodeOnSuctionSide(self, controlnodeonsuctionside: bool) -> None:
		pass

	@property
	def TargetFlow(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@TargetFlow.setter
	def TargetFlow(self, targetflow: float) -> None:
		pass

	@property
	def TargetPressure(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@TargetPressure.setter
	def TargetPressure(self, targetpressure: float) -> None:
		pass

	@property
	def VSPBType(self) -> VSPBType:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@VSPBType.setter
	def VSPBType(self, vspbtype: VSPBType) -> None:
		pass

	@property
	def VSPBFixedHeadType(self) -> VSPBFixedHeadType:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@VSPBFixedHeadType.setter
	def VSPBFixedHeadType(self, vspbfixedheadtype: VSPBFixedHeadType) -> None:
		pass

class IVSPBsResults(IBasePumpsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def LeadPumpFlows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def LeadPumpFlows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def LeadPumpFlows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def NumberOfRunningLagPumps(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def NumberOfRunningLagPumps(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def NumberOfRunningLagPumps(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IVSPBResults(IBasePumpResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def LeadPumpFlow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def LeadPumpFlow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def LoadPumpFlows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def NumberOfRunningLagPumps(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def NumberOfRunningLagPumps(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def NumberRunningLagPumps(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IVariableSpeedPumpBatteryUnits(IBasePumpUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseValvesResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PressureLosses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PressureLosses(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PressureLosses(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromHydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToHydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FromPressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ToPressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Status(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Status(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Status(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseValveResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Velocity(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Velocity(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Headloss(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Headloss(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def PressureLoss(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def PressureLoss(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def PressureLosses(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def FromHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def FromHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def ToHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ToHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def FromPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def FromPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def ToPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ToPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def CalculatedStatus(self) -> Union[int, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedStatus(self, timeStepIndex: int) -> Union[int, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedStatuses(self) -> array(Union[int, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IBaseValveInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialStatus(self) -> ValveSettingType:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: ValveSettingType) -> None:
		pass

	@property
	def ValveDiameter(self) -> float:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@ValveDiameter.setter
	def ValveDiameter(self, valvediameter: float) -> None:
		pass

	@property
	def MinorLossCoefficientCollection(self) -> IMinorLossCoefficientCollection:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@property
	def LocalMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@LocalMinorLossCoefficient.setter
	def LocalMinorLossCoefficient(self, localminorlosscoefficient: float) -> None:
		pass

	@property
	def SpecifyLocalMinorLoss(self) -> bool:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@SpecifyLocalMinorLoss.setter
	def SpecifyLocalMinorLoss(self, specifylocalminorloss: bool) -> None:
		pass

	@property
	def DerivedMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

class IBaseValvesInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def InitialStatus(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialStatus(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Diameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Diameters(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LocalMinorLossCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecifyLocalMinorLoss(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DerivedMinorLossCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseValveUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveDiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def PressureLossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

class IFlowControlValves(IWaterNetworkElements[IFlowControlValves, IFlowControlValve, IFlowControlValveUnits, IFlowControlValveInput, IFlowControlValveResults, IFlowControlValvesInput, IFlowControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFlowControlValve(IWaterNetworkElement[IFlowControlValves, IFlowControlValve, IFlowControlValveUnits, IFlowControlValveInput, IFlowControlValveResults, IFlowControlValvesInput, IFlowControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFlowControlValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedFlowSettings(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedFlowSettings(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedFlowSettings(self, ids: List[int], timeStepInde: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepInde(int): timeStepInde

		Returns:
			Dict[int,int]: 
		"""
		pass

class IFlowControlValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedFlowSetting(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedFlowSetting(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedFlowSettings(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IFlowControlValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def InitialFlowSettings(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialFlowSettings(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IFlowControlValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialFlowSetting(self) -> float:
		"""No Description

		Returns:
			IFlowControlValveInput: 
		"""
		pass

	@InitialFlowSetting.setter
	def InitialFlowSetting(self, initialflowsetting: float) -> None:
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IFlowControlValveInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IFlowControlValveInput: 
		"""
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IFlowControlValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialFlowSettingUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowControlValveUnits: 
		"""
		pass

class IThrottleControlValves(IWaterNetworkElements[IThrottleControlValves, IThrottleControlValve, IThrottleControlValveUnits, IThrottleControlValveInput, IThrottleControlValveResults, IThrottleControlValvesInput, IThrottleControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IThrottleControlValve(IWaterNetworkElement[IThrottleControlValves, IThrottleControlValve, IThrottleControlValveUnits, IThrottleControlValveInput, IThrottleControlValveResults, IThrottleControlValvesInput, IThrottleControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IThrottleControlValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Settings(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Settings(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Settings(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IThrottleControlValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedSetting(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedSetting(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedSettings(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IThrottleControlValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TCVCoefficientType(self) -> TCVCoefficientType:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@TCVCoefficientType.setter
	def TCVCoefficientType(self, tcvcoefficienttype: TCVCoefficientType) -> None:
		pass

	@property
	def InitialCoefficient(self) -> float:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@InitialCoefficient.setter
	def InitialCoefficient(self, initialcoefficient: float) -> None:
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IThrottleControlValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def TCVCoefficientTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TCVCoefficientTypes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialCoefficients(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialCoefficients(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IThrottleControlValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IThrottleControlValveUnits: 
		"""
		pass

class IGeneralPurposeValves(IWaterNetworkElements[IGeneralPurposeValves, IGeneralPurposeValve, IGeneralPurposeValveUnits, IGeneralPurposeValveInput, IGeneralPurposeValveResults, IGeneralPurposeValvesInput, IGeneralPurposeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValve(IWaterNetworkElement[IGeneralPurposeValves, IGeneralPurposeValve, IGeneralPurposeValveUnits, IGeneralPurposeValveInput, IGeneralPurposeValveResults, IGeneralPurposeValvesInput, IGeneralPurposeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GPVHeadlossCurves(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IGeneralPurposeValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVHeadlossCurve(self) -> IGPVHeadlossCurve:
		"""No Description

		Returns:
			IGeneralPurposeValveInput: 
		"""
		pass

	@GPVHeadlossCurve.setter
	def GPVHeadlossCurve(self, gpvheadlosscurve: IGPVHeadlossCurve) -> None:
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IGeneralPurposeValveInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IGeneralPurposeValveInput: 
		"""
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IGeneralPurposeValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedSettings(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedSettings(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedSettings(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedSetting(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedSetting(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedSettings(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IPressureValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureValveSetting(self) -> PressureValvesettingType:
		"""No Description

		Returns:
			IPressureValveInput: 
		"""
		pass

	@PressureValveSetting.setter
	def PressureValveSetting(self, pressurevalvesetting: PressureValvesettingType) -> None:
		pass

	@property
	def InitialSetting(self) -> float:
		"""No Description

		Returns:
			IPressureValveInput: 
		"""
		pass

	@InitialSetting.setter
	def InitialSetting(self, initialsetting: float) -> None:
		pass

class IPressureValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def PressureValveSettings(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PressureValveSettings(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialSettings(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialSettings(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SettingUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPressureValveUnits: 
		"""
		pass

class IPressureBreakingValves(IWaterNetworkElements[IPressureBreakingValves, IPressureBreakingValve, IPressureBreakingValveUnits, IPressureBreakingValveInput, IPressureBreakingValveResults, IPressureBreakingValvesInput, IPressureBreakingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValve(IWaterNetworkElement[IPressureBreakingValves, IPressureBreakingValve, IPressureBreakingValveUnits, IPressureBreakingValveInput, IPressureBreakingValveResults, IPressureBreakingValvesInput, IPressureBreakingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValvesInput(IPressureValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValvesResults(IPressureValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValveResults(IPressureValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValveInput(IPressureValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValveUnits(IPressureValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValves(IWaterNetworkElements[IPressureSustainingValves, IPressureSustainingValve, IPressureSustainingValveUnits, IPressureSustainingValveInput, IPressureSustainingValveResults, IPressureSustainingValvesInput, IPressureSustainingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValve(IWaterNetworkElement[IPressureSustainingValves, IPressureSustainingValve, IPressureSustainingValveUnits, IPressureSustainingValveInput, IPressureSustainingValveResults, IPressureSustainingValvesInput, IPressureSustainingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValvesInput(IPressureValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureSustainingValvesResults(IPressureValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValveResults(IPressureValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValveInput(IPressureValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IPressureSustainingValveInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IPressureSustainingValveInput: 
		"""
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IPressureSustainingValveUnits(IPressureValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValves(IWaterNetworkElements[IPressureReducingValves, IPressureReducingValve, IPressureReducingValveUnits, IPressureReducingValveInput, IPressureReducingValveResults, IPressureReducingValvesInput, IPressureReducingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValve(IWaterNetworkElement[IPressureReducingValves, IPressureReducingValve, IPressureReducingValveUnits, IPressureReducingValveInput, IPressureReducingValveResults, IPressureReducingValvesInput, IPressureReducingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValvesInput(IPressureValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureReducingValvesResults(IPressureValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValveResults(IPressureValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValveInput(IPressureValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IPressureReducingValveInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IPressureReducingValveInput: 
		"""
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IPressureReducingValveUnits(IPressureValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveLinearAreaChangeResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValvesLinearAreaChangeResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveLinearAreaChangeInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeToClose(self) -> float:
		"""No Description

		Returns:
			IValveLinearAreaChangeInput: 
		"""
		pass

	@TimeToClose.setter
	def TimeToClose(self, timetoclose: float) -> None:
		pass

	@property
	def DischargeCoefficient(self) -> float:
		"""No Description

		Returns:
			IValveLinearAreaChangeInput: 
		"""
		pass

	@DischargeCoefficient.setter
	def DischargeCoefficient(self, dischargecoefficient: float) -> None:
		pass

class IValvesLinearAreaChangeInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def TimeToClose(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TimeToClose(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargeCoefficients(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DischargeCoefficients(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IValveWithLinearAreaChange(IWaterNetworkElement[IValvesWithLinearAreaChange, IValveWithLinearAreaChange, IValveWithLinearAreaChangeUnits, IValveLinearAreaChangeInput, IValveLinearAreaChangeResults, IValvesLinearAreaChangeInput, IValvesLinearAreaChangeResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValvesWithLinearAreaChange(IWaterNetworkElements[IValvesWithLinearAreaChange, IValveWithLinearAreaChange, IValveWithLinearAreaChangeUnits, IValveLinearAreaChangeInput, IValveLinearAreaChangeResults, IValvesLinearAreaChangeInput, IValvesLinearAreaChangeResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveWithLinearAreaChangeUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DischargeCoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IValveWithLinearAreaChangeUnits: 
		"""
		pass

	@property
	def TimeToCloseUnit(self) -> IUnit:
		"""No Description

		Returns:
			IValveWithLinearAreaChangeUnits: 
		"""
		pass

class DomainElementExtensions:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	@overload
	def Create(pipes: IPipes, label: str, startNode: IElement, stopNode: IElement, points: List[GeometryPoint]) -> IPipe:
		"""No Description

		Args:
			pipes(IPipes): pipes
			label(str): label
			startNode(IElement): startNode
			stopNode(IElement): stopNode
			points(List[GeometryPoint]): points

		Returns:
			IPipe: 
		"""
		pass

	@staticmethod
	@overload
	def Create(laterals: ILaterals, label: str, startNode: IElement, stopNode: IElement, points: List[GeometryPoint]) -> ILateral:
		"""No Description

		Args:
			laterals(ILaterals): laterals
			label(str): label
			startNode(IElement): startNode
			stopNode(IElement): stopNode
			points(List[GeometryPoint]): points

		Returns:
			ILateral: 
		"""
		pass

	@staticmethod
	@overload
	def Create(junctions: IJunctions, label: str, point: GeometryPoint) -> IJunction:
		"""No Description

		Args:
			junctions(IJunctions): junctions
			label(str): label
			point(GeometryPoint): point

		Returns:
			IJunction: 
		"""
		pass

	@staticmethod
	@overload
	def Create(hydrants: IHydrants, label: str, point: GeometryPoint) -> IHydrant:
		"""No Description

		Args:
			hydrants(IHydrants): hydrants
			label(str): label
			point(GeometryPoint): point

		Returns:
			IHydrant: 
		"""
		pass

	@staticmethod
	@overload
	def Create(tanks: ITanks, label: str, point: GeometryPoint) -> ITank:
		"""No Description

		Args:
			tanks(ITanks): tanks
			label(str): label
			point(GeometryPoint): point

		Returns:
			ITank: 
		"""
		pass

	@staticmethod
	@overload
	def Create(reservoirs: IReservoirs, label: str, point: GeometryPoint) -> IReservoir:
		"""No Description

		Args:
			reservoirs(IReservoirs): reservoirs
			label(str): label
			point(GeometryPoint): point

		Returns:
			IReservoir: 
		"""
		pass

	@staticmethod
	@overload
	def Create(taps: ITaps, label: str, point: GeometryPoint, associatedElement: IPipe) -> ITap:
		"""No Description

		Args:
			taps(ITaps): taps
			label(str): label
			point(GeometryPoint): point
			associatedElement(IPipe): associatedElement

		Returns:
			ITap: 
		"""
		pass

	@staticmethod
	@overload
	def Create(pumps: IPumps, label: str, point: GeometryPoint, downstreamLink: IElement) -> IPump:
		"""No Description

		Args:
			pumps(IPumps): pumps
			label(str): label
			point(GeometryPoint): point
			downstreamLink(IElement): downstreamLink

		Returns:
			IPump: 
		"""
		pass

	@staticmethod
	@overload
	def Create(pumpStations: IPumpStations, label: str, rings: array(array(GeometryPoint))) -> IPumpStation:
		"""No Description

		Args:
			pumpStations(IPumpStations): pumpStations
			label(str): label
			rings(array(array(GeometryPoint))): rings

		Returns:
			IPumpStation: 
		"""
		pass

	@staticmethod
	@overload
	def Create(valves: IFlowControlValves, label: str, point: GeometryPoint, downstreamLink: IElement) -> IFlowControlValve:
		"""No Description

		Args:
			valves(IFlowControlValves): valves
			label(str): label
			point(GeometryPoint): point
			downstreamLink(IElement): downstreamLink

		Returns:
			IFlowControlValve: 
		"""
		pass

	@staticmethod
	@overload
	def Create(valves: IGeneralPurposeValves, label: str, point: GeometryPoint, downstreamLink: IElement) -> IGeneralPurposeValve:
		"""No Description

		Args:
			valves(IGeneralPurposeValves): valves
			label(str): label
			point(GeometryPoint): point
			downstreamLink(IElement): downstreamLink

		Returns:
			IGeneralPurposeValve: 
		"""
		pass

	@staticmethod
	@overload
	def Create(valves: IPressureBreakingValves, label: str, point: GeometryPoint, downstreamLink: IElement) -> IPressureBreakingValve:
		"""No Description

		Args:
			valves(IPressureBreakingValves): valves
			label(str): label
			point(GeometryPoint): point
			downstreamLink(IElement): downstreamLink

		Returns:
			IPressureBreakingValve: 
		"""
		pass

	@staticmethod
	@overload
	def Create(valves: IPressureReducingValves, label: str, point: GeometryPoint, downstreamLink: IElement) -> IPressureReducingValve:
		"""No Description

		Args:
			valves(IPressureReducingValves): valves
			label(str): label
			point(GeometryPoint): point
			downstreamLink(IElement): downstreamLink

		Returns:
			IPressureReducingValve: 
		"""
		pass

	@staticmethod
	@overload
	def Create(valves: IPressureSustainingValves, label: str, point: GeometryPoint, downstreamLink: IElement) -> IPressureSustainingValve:
		"""No Description

		Args:
			valves(IPressureSustainingValves): valves
			label(str): label
			point(GeometryPoint): point
			downstreamLink(IElement): downstreamLink

		Returns:
			IPressureSustainingValve: 
		"""
		pass

	@staticmethod
	@overload
	def Create(valves: IThrottleControlValves, label: str, point: GeometryPoint, downstreamLink: IElement) -> IThrottleControlValve:
		"""No Description

		Args:
			valves(IThrottleControlValves): valves
			label(str): label
			point(GeometryPoint): point
			downstreamLink(IElement): downstreamLink

		Returns:
			IThrottleControlValve: 
		"""
		pass

	@staticmethod
	@overload
	def Create(scadaElements: ISCADAElements, label: str, point: GeometryPoint, targetElement: IWaterElement = None, scadaTargetAttribute: SCADATargetAttribute = SCADATargetAttribute.UnAssigned, realTimeSignal: ISCADASignal = None, historicalSignal: ISCADASignal = None) -> ISCADAElement:
		"""No Description

		Args:
			scadaElements(ISCADAElements): scadaElements
			label(str): label
			point(GeometryPoint): point
			targetElement(IWaterElement): targetElement
			scadaTargetAttribute(SCADATargetAttribute): scadaTargetAttribute
			realTimeSignal(ISCADASignal): realTimeSignal
			historicalSignal(ISCADASignal): historicalSignal

		Returns:
			ISCADAElement: 
		"""
		pass

	@staticmethod
	@overload
	def Create(valves: IIsolationValves, label: str, point: GeometryPoint, pipe: IPipe) -> IIsolationValve:
		"""No Description

		Args:
			valves(IIsolationValves): valves
			label(str): label
			point(GeometryPoint): point
			pipe(IPipe): pipe

		Returns:
			IIsolationValve: 
		"""
		pass

class IWaterElement(IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def WaterElementType(self) -> WaterNetworkElementType:
		"""No Description

		Returns:
			IWaterElement: 
		"""
		pass

class IWaterNetworkElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], INetworkElements[TElementManagerType, TElementType, TUnitsType, WaterNetworkElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterNetworkElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], INetworkElement[TElementManagerType, TElementType, TUnitsType, WaterNetworkElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], IWaterElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterZoneableNetworkElementInput(IActiveElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Zone(self) -> IZone:
		"""No Description

		Returns:
			IWaterZoneableNetworkElementInput: 
		"""
		pass

	@Zone.setter
	def Zone(self, zone: IZone) -> None:
		pass

class IWaterZoneableNetworkElementsInput(IActiveElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Zones(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Zones(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IWaterTraceableInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MakeActiveTraceElement(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

class IWaterQualityResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Age(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Age(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Ages(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Trace(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Trace(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Traces(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Concentration(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Concentration(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Concentrations(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IWaterQualityElementsInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def InitialAge(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialAge(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialTrace(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialTrace(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialConcentration(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialConcentration(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IWaterQualityElementInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialAge(self) -> float:
		"""No Description

		Returns:
			IWaterQualityElementInput: 
		"""
		pass

	@InitialAge.setter
	def InitialAge(self, initialage: float) -> None:
		pass

	@property
	def InitialConcentration(self) -> float:
		"""No Description

		Returns:
			IWaterQualityElementInput: 
		"""
		pass

	@InitialConcentration.setter
	def InitialConcentration(self, initialconcentration: float) -> None:
		pass

	@property
	def InitialTrace(self) -> float:
		"""No Description

		Returns:
			IWaterQualityElementInput: 
		"""
		pass

	@InitialTrace.setter
	def InitialTrace(self, initialtrace: float) -> None:
		pass

class IWaterQualityNodeInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsConstituentSource(self) -> bool:
		"""No Description

		Returns:
			IWaterQualityNodeInput: 
		"""
		pass

	@IsConstituentSource.setter
	def IsConstituentSource(self, isconstituentsource: bool) -> None:
		pass

	@property
	def ConstituentSourceType(self) -> ConstituentSourceType:
		"""No Description

		Returns:
			IWaterQualityNodeInput: 
		"""
		pass

	@ConstituentSourceType.setter
	def ConstituentSourceType(self, constituentsourcetype: ConstituentSourceType) -> None:
		pass

	@property
	def BaseConstituent(self) -> float:
		"""No Description

		Returns:
			IWaterQualityNodeInput: 
		"""
		pass

	@BaseConstituent.setter
	def BaseConstituent(self, baseconstituent: float) -> None:
		pass

class IWaterQualityNodesInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterQualityElementsResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Ages(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Ages(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Ages(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Traces(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Traces(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Traces(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Concentrations(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Concentrations(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Concentrations(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IWaterQualityResultsUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AgeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterQualityResultsUnits: 
		"""
		pass

	@property
	def TraceUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterQualityResultsUnits: 
		"""
		pass

	@property
	def ConcentrationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterQualityResultsUnits: 
		"""
		pass

class IWaterNetwork(INetwork[IWaterElement, WaterNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pipes(self) -> IPipes:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Laterals(self) -> ILaterals:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Junctions(self) -> IJunctions:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Hydrants(self) -> IHydrants:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Tanks(self) -> ITanks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Reservoirs(self) -> IReservoirs:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Taps(self) -> ITaps:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def CustomerMeters(self) -> ICustomerMeters:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Pumps(self) -> IPumps:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def VSPBs(self) -> IVariableSpeedPumpBatterys:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PumpStations(self) -> IPumpStations:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SCADAElements(self) -> ISCADAElements:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PRVs(self) -> IPressureReducingValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PBVs(self) -> IPressureBreakingValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PSVs(self) -> IPressureSustainingValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def TCVs(self) -> IThrottleControlValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def FCVs(self) -> IFlowControlValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def GPVs(self) -> IGeneralPurposeValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def IsolationValves(self) -> IIsolationValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def CheckValves(self) -> ICheckValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SpotElevations(self) -> ISpotElevations:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def ValvesWithLinearAreaChange(self) -> IValvesWithLinearAreaChange:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PeriodicHeadFlows(self) -> IPeriodicHeadFlows:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def AirValves(self) -> IAirValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def OrificesBetweenTwoPipes(self) -> IOrificesBetweenTwoPipes:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SurgeValves(self) -> ISurgeValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def DischargeToAtmospheres(self) -> IDischargeToAtmospheres:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def RuptureDisks(self) -> IRuptureDisks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Turbines(self) -> ITurbines:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SurgeTanks(self) -> ISurgeTanks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def HydropneumaticTanks(self) -> IHydropneumaticTanks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

class IPipes(IWaterNetworkElements[IPipes, IPipe, IPipeUnits, IPipeInput, IPipeResults, IPipesInput, IPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPipe(IWaterNetworkElement[IPipes, IPipe, IPipeUnits, IPipeInput, IPipeResults, IPipesInput, IPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerPipesResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def MaximumHeads(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def MaximumHeads(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPipesResults(IBaseLinksResults, IWaterQualityElementsResults, IHammerPipesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Headlosses(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HeadlossGradients(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HeadlossGradients(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HeadlossGradients(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Statuses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Statuses(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Statuses(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHammerPipeResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MaximumHead(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

class IPipeResults(IBaseLinkResults, IWaterQualityResults, IHammerPipeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Velocity(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Velocity(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Headloss(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Headloss(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def HeadlossGradient(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def HeadlossGradient(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HeadlossGradients(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def CalculatedStatus(self) -> Union[int, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedStatus(self, timeStepIndex: int) -> Union[int, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedStatuses(self) -> array(Union[int, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IPipeInput(IBaseLinkInput, IWaterZoneableNetworkElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InstallationYear(self) -> int:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@InstallationYear.setter
	def InstallationYear(self, installationyear: int) -> None:
		pass

	@property
	def InitialStatus(self) -> PipeStatusType:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: PipeStatusType) -> None:
		pass

	@property
	def Diameter(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@Diameter.setter
	def Diameter(self, diameter: float) -> None:
		pass

	@property
	def Material(self) -> str:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@Material.setter
	def Material(self, material: str) -> None:
		pass

	@property
	def FrictionCoefficient(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@FrictionCoefficient.setter
	def FrictionCoefficient(self, frictioncoefficient: float) -> None:
		pass

	@property
	def MinorLossCoefficientCollection(self) -> IMinorLossCoefficientCollection:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def LocalMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@LocalMinorLossCoefficient.setter
	def LocalMinorLossCoefficient(self, localminorlosscoefficient: float) -> None:
		pass

	@property
	def SpecifyLocalMinorLoss(self) -> bool:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@SpecifyLocalMinorLoss.setter
	def SpecifyLocalMinorLoss(self, specifylocalminorloss: bool) -> None:
		pass

	@property
	def DerivedMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

class IPipesInput(IBaseLinksInput, IWaterZoneableNetworkElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def InstallationYears(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InstallationYears(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PipeStatuses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PipeStatuses(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Diameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Diameters(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Materials(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Materials(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FrictionCoefficients(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FrictionCoefficients(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LocalMinorLossCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecifyLocalMinorLoss(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DerivedMinorLossCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPipeUnits(IBaseLinkUnits, IWaterQualityResultsUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def HeadlossGradientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

class ILateral(IWaterNetworkElement[ILaterals, ILateral, IBaseLinkUnits, ILateralInput, IBaseLinkResults, ILateralsInput, IBaseLinksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILaterals(IWaterNetworkElements[ILaterals, ILateral, IBaseLinkUnits, ILateralInput, IBaseLinkResults, ILateralsInput, IBaseLinksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILateralInput(IBaseLinkInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILateralsInput(IBaseLinksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFireFlowNodesResults(IDemandNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Demands(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Demands(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Demands(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IFireFlowNodeResults(IDemandNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Demand(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Demand(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Demands(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Pressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Pressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IFireFlowNodeInput(IDemandNodeInput, IWaterTraceableInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFireFlowNodesInput(IDemandNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFireFlowNodeUnits(IDemandNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFireFlowNodeUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFireFlowNodeUnits: 
		"""
		pass

class IJunctions(IWaterNetworkElements[IJunctions, IJunction, IJunctionUnits, IJunctionInput, IJunctionResults, IJunctionsInput, IJunctionsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunction(IWaterNetworkElement[IJunctions, IJunction, IJunctionUnits, IJunctionInput, IJunctionResults, IJunctionsInput, IJunctionsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionsResults(IFireFlowNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionsInput(IFireFlowNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionInput(IFireFlowNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionResults(IFireFlowNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionUnits(IFireFlowNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrants(IWaterNetworkElements[IHydrants, IHydrant, IHydrantUnits, IHydrantInput, IHydrantResults, IHydrantsInput, IHydrantsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrant(IWaterNetworkElement[IHydrants, IHydrant, IHydrantUnits, IHydrantInput, IHydrantResults, IHydrantsInput, IHydrantsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantsResults(IFireFlowNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantResults(IFireFlowNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantsInput(IFireFlowNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantInput(IFireFlowNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantUnits(IFireFlowNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodeInput(IBaseNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandCollection(self) -> IDemandCollection:
		"""No Description

		Returns:
			IDemandNodeInput: 
		"""
		pass

	@property
	def UnitDemandLoadCollection(self) -> IUnitLoadDemandCollection:
		"""No Description

		Returns:
			IDemandNodeInput: 
		"""
		pass

class IDemandNodesInput(IBaseNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodesResults(IBaseNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodeResults(IBaseNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodeUnits(IBaseNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandCollection(ICollectionElements[IDemands, IDemand, IDemandUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemands(ICollection[IDemand]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, flow: float, pattern: IPattern) -> IDemand:
		"""No Description

		Args:
			flow(float): flow
			pattern(IPattern): pattern

		Returns:
			IDemand: 
		"""
		pass

	@overload
	def Add(self) -> IDemand:
		"""No Description

		Returns:
			IDemand: 
		"""
		pass

class IDemand(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def BaseFlow(self) -> float:
		"""No Description

		Returns:
			IDemand: 
		"""
		pass

	@BaseFlow.setter
	def BaseFlow(self, baseflow: float) -> None:
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			IDemand: 
		"""
		pass

	@DemandPattern.setter
	def DemandPattern(self, demandpattern: IPattern) -> None:
		pass

class IDemandUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def BaseFlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDemandUnits: 
		"""
		pass

class IUnitLoadDemandCollection(ICollectionElements[IUnitLoadDemands, IUnitLoadDemand, IUnitLoadDemandUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitLoadDemands(ICollection[IUnitLoadDemand]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, unitDemandLoad: IUnitDemandLoad, numberOfLoadingUnits: float, unitDemandBaseFlow: float, unitDemandPattern: IPattern) -> IUnitLoadDemand:
		"""No Description

		Args:
			unitDemandLoad(IUnitDemandLoad): unitDemandLoad
			numberOfLoadingUnits(float): numberOfLoadingUnits
			unitDemandBaseFlow(float): unitDemandBaseFlow
			unitDemandPattern(IPattern): unitDemandPattern

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@overload
	def Add(self) -> IUnitLoadDemand:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

class IUnitLoadDemand(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UnitDemandLoad(self) -> IUnitDemandLoad:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@UnitDemandLoad.setter
	def UnitDemandLoad(self, unitdemandload: IUnitDemandLoad) -> None:
		pass

	@property
	def NumberOfLoadingUnits(self) -> float:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@NumberOfLoadingUnits.setter
	def NumberOfLoadingUnits(self, numberofloadingunits: float) -> None:
		pass

	@property
	def UnitDemandBaseFlow(self) -> float:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@UnitDemandBaseFlow.setter
	def UnitDemandBaseFlow(self, unitdemandbaseflow: float) -> None:
		pass

	@property
	def UnitDemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@UnitDemandPattern.setter
	def UnitDemandPattern(self, unitdemandpattern: IPattern) -> None:
		pass

class IUnitLoadDemandUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UnitDemandBaseFlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IUnitLoadDemandUnits: 
		"""
		pass

class IConventionalTanksResults(IBaseTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def VolumeFulls(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Levels(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Levels(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Levels(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Volumes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Volumes(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Volumes(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PercentFulls(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PercentFulls(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PercentFulls(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TankStatuses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TankStatuses(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TankStatuses(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IConventionalTankResults(IBaseTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def VolumeFull(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Level(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Level(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Levels(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Volume(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Volume(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Volumes(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def PercentFull(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def PercentFull(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def PercentFulls(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def TankStatus(self) -> Union[int, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def TankStatus(self, timeStepIndex: int) -> Union[int, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def TankStatuses(self) -> array(Union[int, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IConventionalTanksInput(IBaseTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def TankSection(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TankSection(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ActiveVolumeFull(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ActiveVolumeFull(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Diameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Diameter(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AverageArea(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AverageArea(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def BaseElevation(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def BaseElevation(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def MinimumLevel(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def MinimumLevel(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialLevel(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialLevel(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def MaximumLevel(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def MaximumLevel(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UseHighAlarm(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UseHighAlarm(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HighAlarmLevel(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HighAlarmLevel(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UseLowAlarm(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UseLowAlarm(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def LowAlarmLevel(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def LowAlarmLevel(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InactiveVolume(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InactiveVolume(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IConventionalTankInput(IBaseTankInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TankSection(self) -> TankSectionType:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@TankSection.setter
	def TankSection(self, tanksection: TankSectionType) -> None:
		pass

	@property
	def ActiveVolumeFull(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@ActiveVolumeFull.setter
	def ActiveVolumeFull(self, activevolumefull: float) -> None:
		pass

	@property
	def CrossSectionCurve(self) -> ICrossSectionCurveCollection:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def Diameter(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@Diameter.setter
	def Diameter(self, diameter: float) -> None:
		pass

	@property
	def AverageArea(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@AverageArea.setter
	def AverageArea(self, averagearea: float) -> None:
		pass

	@property
	def BaseElevation(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@BaseElevation.setter
	def BaseElevation(self, baseelevation: float) -> None:
		pass

	@property
	def MinimumLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@MinimumLevel.setter
	def MinimumLevel(self, minimumlevel: float) -> None:
		pass

	@property
	def InitialLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@InitialLevel.setter
	def InitialLevel(self, initiallevel: float) -> None:
		pass

	@property
	def MaximumLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@MaximumLevel.setter
	def MaximumLevel(self, maximumlevel: float) -> None:
		pass

	@property
	def UseHighAlarm(self) -> bool:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@UseHighAlarm.setter
	def UseHighAlarm(self, usehighalarm: bool) -> None:
		pass

	@property
	def HighAlarmLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@HighAlarmLevel.setter
	def HighAlarmLevel(self, highalarmlevel: float) -> None:
		pass

	@property
	def UseLowAlarm(self) -> bool:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@UseLowAlarm.setter
	def UseLowAlarm(self, uselowalarm: bool) -> None:
		pass

	@property
	def LowAlarmLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@LowAlarmLevel.setter
	def LowAlarmLevel(self, lowalarmlevel: float) -> None:
		pass

	@property
	def InactiveVolume(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@InactiveVolume.setter
	def InactiveVolume(self, inactivevolume: float) -> None:
		pass

class IConventionalTankUnits(IBaseTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LevelUnit(self) -> IUnit:
		"""No Description

		Returns:
			IConventionalTankUnits: 
		"""
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IConventionalTankUnits: 
		"""
		pass

	@property
	def PercentFullUnit(self) -> IUnit:
		"""No Description

		Returns:
			IConventionalTankUnits: 
		"""
		pass

class ICrossSectionCurveCollection(ICollectionElements[ICrossSectionCurve, ICrossSectionCurveElement, ICrossSectionCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICrossSectionCurve(ICollection[ICrossSectionCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, depthRatio: float, volumeRatio: float) -> ICrossSectionCurveElement:
		"""No Description

		Args:
			depthRatio(float): depthRatio
			volumeRatio(float): volumeRatio

		Returns:
			ICrossSectionCurveElement: 
		"""
		pass

	@overload
	def Add(self) -> ICrossSectionCurveElement:
		"""No Description

		Returns:
			ICrossSectionCurveElement: 
		"""
		pass

class ICrossSectionCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DepthRatio(self) -> float:
		"""No Description

		Returns:
			ICrossSectionCurveElement: 
		"""
		pass

	@DepthRatio.setter
	def DepthRatio(self, depthratio: float) -> None:
		pass

	@property
	def VolumeRatio(self) -> float:
		"""No Description

		Returns:
			ICrossSectionCurveElement: 
		"""
		pass

	@VolumeRatio.setter
	def VolumeRatio(self, volumeratio: float) -> None:
		pass

class ICrossSectionCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RatioUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICrossSectionCurveUnits: 
		"""
		pass

class ITanks(IWaterNetworkElements[ITanks, ITank, ITankUnits, ITankInput, ITankResults, ITanksInput, ITanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITank(IWaterNetworkElement[ITanks, ITank, ITankUnits, ITankInput, ITankResults, ITanksInput, ITanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITanksResults(IConventionalTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITankResults(IConventionalTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITanksInput(IConventionalTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITankInput(IConventionalTankInput, IWaterTraceableInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			ITankInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			ITankInput: 
		"""
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class ITankUnits(IConventionalTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTankInput(IConventionalTankInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TankOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@TankOrificeDiameter.setter
	def TankOrificeDiameter(self, tankorificediameter: float) -> None:
		pass

	@property
	def RatioOfLosses(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@RatioOfLosses.setter
	def RatioOfLosses(self, ratiooflosses: float) -> None:
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@property
	def SurgeTankType(self) -> SurgeTankTypeEnum:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@SurgeTankType.setter
	def SurgeTankType(self, surgetanktype: SurgeTankTypeEnum) -> None:
		pass

	@property
	def HasCheckValve(self) -> bool:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@HasCheckValve.setter
	def HasCheckValve(self, hascheckvalve: bool) -> None:
		pass

	@property
	def WeirCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@WeirCoefficient.setter
	def WeirCoefficient(self, weircoefficient: float) -> None:
		pass

	@property
	def WeirLength(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@WeirLength.setter
	def WeirLength(self, weirlength: float) -> None:
		pass

	@property
	def InternalRiserDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@InternalRiserDiameter.setter
	def InternalRiserDiameter(self, internalriserdiameter: float) -> None:
		pass

	@property
	def InternalRiserTopElevation(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@InternalRiserTopElevation.setter
	def InternalRiserTopElevation(self, internalrisertopelevation: float) -> None:
		pass

	@property
	def JunctionElevation(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@JunctionElevation.setter
	def JunctionElevation(self, junctionelevation: float) -> None:
		pass

	@property
	def DiameterExternalRiser(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@DiameterExternalRiser.setter
	def DiameterExternalRiser(self, diameterexternalriser: float) -> None:
		pass

	@property
	def ElevationOrificeFromInternalRiserInTank(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@ElevationOrificeFromInternalRiserInTank.setter
	def ElevationOrificeFromInternalRiserInTank(self, elevationorificefrominternalriserintank: float) -> None:
		pass

	@property
	def ElevationTopOfTankBase(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@ElevationTopOfTankBase.setter
	def ElevationTopOfTankBase(self, elevationtopoftankbase: float) -> None:
		pass

class ISurgeTanksInput(IConventionalTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TankOrificeDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RatioOfLosses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HeadlossCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SurgeTankType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HasCheckValve(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def WeirCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def WeirLength(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InternalRiserDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InternalRiserTopElevation(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def JunctionElevation(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DiameterExternalRiser(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ElevationOrificeFromInternalRiserInTank(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ElevationTopOfTankBase(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISurgeTankResults(IConventionalTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTanksResults(IConventionalTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTankUnits(IConventionalTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

	@property
	def RatioUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

	@property
	def WeirCoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

class ISurgeTanks(IWaterNetworkElements[ISurgeTanks, ISurgeTank, ISurgeTankUnits, ISurgeTankInput, ISurgeTankResults, ISurgeTanksInput, ISurgeTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTank(IWaterNetworkElement[ISurgeTanks, ISurgeTank, ISurgeTankUnits, ISurgeTankInput, ISurgeTankResults, ISurgeTanksInput, ISurgeTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseTanksResults(IDemandNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseTankResults(IDemandNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IBaseTankInput(IDemandNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseTanksInput(IDemandNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseTankUnits(IDemandNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseTankUnits: 
		"""
		pass

class IVariableLevelCurveCollection(ICollectionElements[ILevelDiameters, ILevelDiameter, IVariableLevelCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILevelDiameters(ICollection[ILevelDiameter]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, liquidLevel: float, diameter: float) -> ILevelDiameter:
		"""No Description

		Args:
			liquidLevel(float): liquidLevel
			diameter(float): diameter

		Returns:
			ILevelDiameter: 
		"""
		pass

	@overload
	def Add(self) -> ILevelDiameter:
		"""No Description

		Returns:
			ILevelDiameter: 
		"""
		pass

class ILevelDiameter(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LiquidLevel(self) -> float:
		"""No Description

		Returns:
			ILevelDiameter: 
		"""
		pass

	@LiquidLevel.setter
	def LiquidLevel(self, liquidlevel: float) -> None:
		pass

	@property
	def EquivalentDiameter(self) -> float:
		"""No Description

		Returns:
			ILevelDiameter: 
		"""
		pass

	@EquivalentDiameter.setter
	def EquivalentDiameter(self, equivalentdiameter: float) -> None:
		pass

class IVariableLevelCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LevelUnit(self) -> IUnit:
		"""No Description

		Returns:
			IVariableLevelCurveUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IVariableLevelCurveUnits: 
		"""
		pass

class IHydroTankInput(IBaseTankInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialVolumeOfGas(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@InitialVolumeOfGas.setter
	def InitialVolumeOfGas(self, initialvolumeofgas: float) -> None:
		pass

	@property
	def TankInletOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TankInletOrificeDiameter.setter
	def TankInletOrificeDiameter(self, tankinletorificediameter: float) -> None:
		pass

	@property
	def RatioOfLosses(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@RatioOfLosses.setter
	def RatioOfLosses(self, ratiooflosses: float) -> None:
		pass

	@property
	def GasLawExponent(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@GasLawExponent.setter
	def GasLawExponent(self, gaslawexponent: float) -> None:
		pass

	@property
	def HasBladder(self) -> bool:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@HasBladder.setter
	def HasBladder(self, hasbladder: bool) -> None:
		pass

	@property
	def GasPresetPressure(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@GasPresetPressure.setter
	def GasPresetPressure(self, gaspresetpressure: float) -> None:
		pass

	@property
	def MeanLiquidElevation(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@MeanLiquidElevation.setter
	def MeanLiquidElevation(self, meanliquidelevation: float) -> None:
		pass

	@property
	def AirInflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@AirInflowOrificeDiameter.setter
	def AirInflowOrificeDiameter(self, airinfloworificediameter: float) -> None:
		pass

	@property
	def AirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@AirOutflowOrificeDiameter.setter
	def AirOutflowOrificeDiameter(self, airoutfloworificediameter: float) -> None:
		pass

	@property
	def DippingTubeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@DippingTubeDiameter.setter
	def DippingTubeDiameter(self, dippingtubediameter: float) -> None:
		pass

	@property
	def CompressionChamberVolume(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@CompressionChamberVolume.setter
	def CompressionChamberVolume(self, compressionchambervolume: float) -> None:
		pass

	@property
	def TopElevationDippingTube(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TopElevationDippingTube.setter
	def TopElevationDippingTube(self, topelevationdippingtube: float) -> None:
		pass

	@property
	def BottomElevationDippingTube(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@BottomElevationDippingTube.setter
	def BottomElevationDippingTube(self, bottomelevationdippingtube: float) -> None:
		pass

	@property
	def LevelType(self) -> GasVesselLevelType:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@LevelType.setter
	def LevelType(self, leveltype: GasVesselLevelType) -> None:
		pass

	@property
	def HydroTankType(self) -> HydroTankType:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@HydroTankType.setter
	def HydroTankType(self, hydrotanktype: HydroTankType) -> None:
		pass

	@property
	def VariableLevelCurve(self) -> IVariableLevelCurveCollection:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankVolume(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TankVolume.setter
	def TankVolume(self, tankvolume: float) -> None:
		pass

	@property
	def InflowMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@InflowMinorLossCoefficient.setter
	def InflowMinorLossCoefficient(self, inflowminorlosscoefficient: float) -> None:
		pass

	@property
	def TankBaseElevation(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TankBaseElevation.setter
	def TankBaseElevation(self, tankbaseelevation: float) -> None:
		pass

	@property
	def TreatAsJunction(self) -> bool:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TreatAsJunction.setter
	def TreatAsJunction(self, treatasjunction: bool) -> None:
		pass

	@property
	def OperatingRangeType(self) -> OperatingRangeTypeEnum:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@OperatingRangeType.setter
	def OperatingRangeType(self, operatingrangetype: OperatingRangeTypeEnum) -> None:
		pass

	@property
	def TankCalculationModel(self) -> TankCalculationModel:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TankCalculationModel.setter
	def TankCalculationModel(self, tankcalculationmodel: TankCalculationModel) -> None:
		pass

	@property
	def TankInitialElevation(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TankInitialElevation.setter
	def TankInitialElevation(self, tankinitialelevation: float) -> None:
		pass

	@property
	def TankInitialLevel(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TankInitialLevel.setter
	def TankInitialLevel(self, tankinitiallevel: float) -> None:
		pass

	@property
	def TankInitialLiquidVolume(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@TankInitialLiquidVolume.setter
	def TankInitialLiquidVolume(self, tankinitialliquidvolume: float) -> None:
		pass

	@property
	def AirInflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@AirInflowOrificeAirFlowCurve.setter
	def AirInflowOrificeAirFlowCurve(self, airinfloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@property
	def AirOutflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@AirOutflowOrificeAirFlowCurve.setter
	def AirOutflowOrificeAirFlowCurve(self, airoutfloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@property
	def AirFlowCalculationMethod(self) -> AirFlowCalculationMethod:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@AirFlowCalculationMethod.setter
	def AirFlowCalculationMethod(self, airflowcalculationmethod: AirFlowCalculationMethod) -> None:
		pass

class IHydroTanksInput(IBaseTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def InitialVolumeOfGas(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInletOrificeDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RatioOfLosses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GasLawExponent(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HasBladder(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GasPresetPressure(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MeanLiquidElevation(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DippingTubeDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def CompressionChamberVolume(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TopElevationDippingTube(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def BottomElevationDippingTube(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LevelType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HydroTankType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankVolume(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InflowMinorLossCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankBaseElevation(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TreatAsJunction(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OperatingRangeType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankCalculationModel(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialElevation(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialLevel(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialLiquidVolume(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeAirFlowCurve(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeAirFlowCurve(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirFlowCalculationMethod(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHydroTankResults(IBaseTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedGasVolume(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedGasVolume(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedGasVolumes(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def CalculatedPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def CalculatedLiquidVolume(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedLiquidVolume(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedLiquidVolumes(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def CalculatedPercentFull(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedPercentFull(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedPercentFulls(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	def MaximumTransientGasPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientGasPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	def MaximumTransientGasVolume(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientGasVolume(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	def MaximumTransientWaterLevel(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientWaterLevel(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

class IHydroTanksResults(IBaseTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedGasVolumes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedGasVolumes(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedGasVolumes(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedPressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedPressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedLiquidVolumes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedLiquidVolumes(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedLiquidVolumes(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedPercentFulls(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedPercentFulls(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedPercentFulls(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientGasPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientGasPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientGasVolumes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientGasVolumes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientWaterLevels(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientWaterLevels(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHydropneumaticTankUnits(IBaseTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def GasExponentUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def PercentUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

class IHydropneumaticTank(IWaterNetworkElement[IHydropneumaticTanks, IHydropneumaticTank, IHydropneumaticTankUnits, IHydroTankInput, IHydroTankResults, IHydroTanksInput, IHydroTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydropneumaticTanks(IWaterNetworkElements[IHydropneumaticTanks, IHydropneumaticTank, IHydropneumaticTankUnits, IHydroTankInput, IHydroTankResults, IHydroTanksInput, IHydroTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerNodeInput(IBaseNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerNodesInput(IBaseNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerNodeResults(IBaseNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Pressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Pressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def PressureHead(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def PressureHead(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def PressureHeads(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IHammerNodesResults(IBaseNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Pressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PressureHeads(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PressureHeads(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def PressureHeads(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHammerNodeUnits(IBaseNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHammerNodeUnits: 
		"""
		pass

	@property
	def PressureHeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHammerNodeUnits: 
		"""
		pass

class IFlowPatternCollection(ICollectionElements[IFlowPatterns, IFlowPattern, IFlowPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFlowPatterns(ICollection[IFlowPattern]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, time: float, flow: float) -> IFlowPattern:
		"""No Description

		Args:
			time(float): time
			flow(float): flow

		Returns:
			IFlowPattern: 
		"""
		pass

	@overload
	def Add(self) -> IFlowPattern:
		"""No Description

		Returns:
			IFlowPattern: 
		"""
		pass

class IFlowPattern(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> float:
		"""No Description

		Returns:
			IFlowPattern: 
		"""
		pass

	@Time.setter
	def Time(self, time: float) -> None:
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IFlowPattern: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

class IFlowPatternUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowPatternUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowPatternUnits: 
		"""
		pass

class IHeadPatternCollection(ICollectionElements[IHeadPatterns, IHeadPattern, IHeadPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHeadPatterns(ICollection[IHeadPattern]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, time: float, head: float) -> IHeadPattern:
		"""No Description

		Args:
			time(float): time
			head(float): head

		Returns:
			IHeadPattern: 
		"""
		pass

	@overload
	def Add(self) -> IHeadPattern:
		"""No Description

		Returns:
			IHeadPattern: 
		"""
		pass

class IHeadPattern(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> float:
		"""No Description

		Returns:
			IHeadPattern: 
		"""
		pass

	@Time.setter
	def Time(self, time: float) -> None:
		pass

	@property
	def Head(self) -> float:
		"""No Description

		Returns:
			IHeadPattern: 
		"""
		pass

	@Head.setter
	def Head(self, head: float) -> None:
		pass

class IHeadPatternUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHeadPatternUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHeadPatternUnits: 
		"""
		pass

class IPeriodicHeadFlowInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Sinusoidal(self) -> bool:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@Sinusoidal.setter
	def Sinusoidal(self, sinusoidal: bool) -> None:
		pass

	@property
	def HeadMeanValue(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@HeadMeanValue.setter
	def HeadMeanValue(self, headmeanvalue: float) -> None:
		pass

	@property
	def HeadAmplitude(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@HeadAmplitude.setter
	def HeadAmplitude(self, headamplitude: float) -> None:
		pass

	@property
	def Phase(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@Phase.setter
	def Phase(self, phase: float) -> None:
		pass

	@property
	def Period(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@Period.setter
	def Period(self, period: float) -> None:
		pass

	@property
	def FlowMeanValue(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@FlowMeanValue.setter
	def FlowMeanValue(self, flowmeanvalue: float) -> None:
		pass

	@property
	def FlowAmplitude(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@FlowAmplitude.setter
	def FlowAmplitude(self, flowamplitude: float) -> None:
		pass

	@property
	def TransientParameter(self) -> TransientParameterType:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@TransientParameter.setter
	def TransientParameter(self, transientparameter: TransientParameterType) -> None:
		pass

	@property
	def FlowPatternCollection(self) -> IFlowPatternCollection:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def HeadPatternCollection(self) -> IHeadPatternCollection:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

class IPeriodicHeadFlowsInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Sinusoidals(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Sinusoidals(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HeadMeanValues(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HeadMeanValues(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HeadAmplitudes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HeadAmplitudes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Phases(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Phases(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Periods(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Periods(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FlowMeanValues(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FlowMeanValues(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FlowAmplitudes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def FlowAmplitudes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TransientParameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TransientParameters(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPeriodicHeadFlowResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedDischarge(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedDischarge(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedDischarges(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IPeriodicHeadFlowsResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedDischarges(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedDischarges(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedDischarges(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPeriodicHeadFlowUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

	@property
	def AngleUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

	@property
	def PeriodUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

class IPeriodicHeadFlows(IWaterNetworkElements[IPeriodicHeadFlows, IPeriodicHeadFlow, IPeriodicHeadFlowUnits, IPeriodicHeadFlowInput, IPeriodicHeadFlowResults, IPeriodicHeadFlowsInput, IPeriodicHeadFlowsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPeriodicHeadFlow(IWaterNetworkElement[IPeriodicHeadFlows, IPeriodicHeadFlow, IPeriodicHeadFlowUnits, IPeriodicHeadFlowInput, IPeriodicHeadFlowResults, IPeriodicHeadFlowsInput, IPeriodicHeadFlowsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValveInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialAirvolume(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@InitialAirvolume.setter
	def InitialAirvolume(self, initialairvolume: float) -> None:
		pass

	@property
	def SmallAirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@SmallAirOutflowOrificeDiameter.setter
	def SmallAirOutflowOrificeDiameter(self, smallairoutfloworificediameter: float) -> None:
		pass

	@property
	def TransitionVolume(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@TransitionVolume.setter
	def TransitionVolume(self, transitionvolume: float) -> None:
		pass

	@property
	def LargeAirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@LargeAirOutflowOrificeDiameter.setter
	def LargeAirOutflowOrificeDiameter(self, largeairoutfloworificediameter: float) -> None:
		pass

	@property
	def AirInflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@AirInflowOrificeDiameter.setter
	def AirInflowOrificeDiameter(self, airinfloworificediameter: float) -> None:
		pass

	@property
	def AirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@AirOutflowOrificeDiameter.setter
	def AirOutflowOrificeDiameter(self, airoutfloworificediameter: float) -> None:
		pass

	@property
	def TransitionPressure(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@TransitionPressure.setter
	def TransitionPressure(self, transitionpressure: float) -> None:
		pass

	@property
	def SmallAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@SmallAirFlowCurve.setter
	def SmallAirFlowCurve(self, smallairflowcurve: IAirFlowCurve) -> None:
		pass

	@property
	def LargeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@LargeAirFlowCurve.setter
	def LargeAirFlowCurve(self, largeairflowcurve: IAirFlowCurve) -> None:
		pass

	@property
	def AirValveType(self) -> AirValveTypeEnum:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@AirValveType.setter
	def AirValveType(self, airvalvetype: AirValveTypeEnum) -> None:
		pass

	@property
	def AirValveTransitionType(self) -> AirValveTransitionType:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@AirValveTransitionType.setter
	def AirValveTransitionType(self, airvalvetransitiontype: AirValveTransitionType) -> None:
		pass

	@property
	def TimeToClose(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@TimeToClose.setter
	def TimeToClose(self, timetoclose: float) -> None:
		pass

	@property
	def ReportPeriod(self) -> int:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@ReportPeriod.setter
	def ReportPeriod(self, reportperiod: int) -> None:
		pass

	@property
	def TreatAirValveAsJunction(self) -> bool:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@TreatAirValveAsJunction.setter
	def TreatAirValveAsJunction(self, treatairvalveasjunction: bool) -> None:
		pass

	@property
	def InflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@InflowOrificeAirFlowCurve.setter
	def InflowOrificeAirFlowCurve(self, infloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@property
	def OutflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@OutflowOrificeAirFlowCurve.setter
	def OutflowOrificeAirFlowCurve(self, outfloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@property
	def AirFlowCalculationMethod(self) -> AirFlowCalculationMethod:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@AirFlowCalculationMethod.setter
	def AirFlowCalculationMethod(self, airflowcalculationmethod: AirFlowCalculationMethod) -> None:
		pass

class IAirValvesInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def InitialAirVolumes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SmallAirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TransitionVolumes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LargeAirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeDiameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TransitionPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SmallAirflowCurves(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LargeAirFlowCurves(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirValveTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirValveTransitionTypes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToClose(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriods(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TreatAirValvesAsJunctions(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InflowOrificeAirFlowCurves(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OutflowOrificeAirFlowCurves(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirFlowCalculationMethods(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IAirValveResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValvesResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValveUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirValveUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirValveUnits: 
		"""
		pass

	@property
	def TimeTocloseUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirValveUnits: 
		"""
		pass

class IAirValve(IWaterNetworkElement[IAirValves, IAirValve, IAirValveUnits, IAirValveInput, IAirValveResults, IAirValvesInput, IAirValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValves(IWaterNetworkElements[IAirValves, IAirValve, IAirValveUnits, IAirValveInput, IAirValveResults, IAirValvesInput, IAirValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValveInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SavDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SavDiameter.setter
	def SavDiameter(self, savdiameter: float) -> None:
		pass

	@property
	def SavThresholdPressure(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SavThresholdPressure.setter
	def SavThresholdPressure(self, savthresholdpressure: float) -> None:
		pass

	@property
	def TimeForSAVToOpen(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@TimeForSAVToOpen.setter
	def TimeForSAVToOpen(self, timeforsavtoopen: float) -> None:
		pass

	@property
	def TimeSAVStaysFullyOpen(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@TimeSAVStaysFullyOpen.setter
	def TimeSAVStaysFullyOpen(self, timesavstaysfullyopen: float) -> None:
		pass

	@property
	def TimeForSAVToClose(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@TimeForSAVToClose.setter
	def TimeForSAVToClose(self, timeforsavtoclose: float) -> None:
		pass

	@property
	def SavDischargeCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SavDischargeCoefficient.setter
	def SavDischargeCoefficient(self, savdischargecoefficient: float) -> None:
		pass

	@property
	def SrvDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SrvDiameter.setter
	def SrvDiameter(self, srvdiameter: float) -> None:
		pass

	@property
	def SrvThresholdPressure(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SrvThresholdPressure.setter
	def SrvThresholdPressure(self, srvthresholdpressure: float) -> None:
		pass

	@property
	def SrvSpringConstant(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SrvSpringConstant.setter
	def SrvSpringConstant(self, srvspringconstant: float) -> None:
		pass

	@property
	def TimeForSRVToOpen(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@TimeForSRVToOpen.setter
	def TimeForSRVToOpen(self, timeforsrvtoopen: float) -> None:
		pass

	@property
	def TimeForSRVToClose(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@TimeForSRVToClose.setter
	def TimeForSRVToClose(self, timeforsrvtoclose: float) -> None:
		pass

	@property
	def SrvDischargeCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SrvDischargeCoefficient.setter
	def SrvDischargeCoefficient(self, srvdischargecoefficient: float) -> None:
		pass

	@property
	def SavSrvType(self) -> SAV_SRVTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SavSrvType.setter
	def SavSrvType(self, savsrvtype: SAV_SRVTypeEnum) -> None:
		pass

	@property
	def SavType(self) -> SAVValveTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SavType.setter
	def SavType(self, savtype: SAVValveTypeEnum) -> None:
		pass

	@property
	def SavClosureTriggerType(self) -> SavClosureTriggerEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SavClosureTriggerType.setter
	def SavClosureTriggerType(self, savclosuretriggertype: SavClosureTriggerEnum) -> None:
		pass

	@property
	def SrvControlType(self) -> SRVControlTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SrvControlType.setter
	def SrvControlType(self, srvcontroltype: SRVControlTypeEnum) -> None:
		pass

	@property
	def SrvValveType(self) -> SRVValveTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SrvValveType.setter
	def SrvValveType(self, srvvalvetype: SRVValveTypeEnum) -> None:
		pass

class ISurgeValvesInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SavDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavThresholdPressure(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSAVToOpen(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeSAVStaysFullyOpen(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSAVToClose(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavDischargeCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvDiameter(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvThresholdPressure(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvSpringConstant(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSRVToOpen(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSRVToClose(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvDischargeCoefficient(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavSrvType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavClosureTriggerType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvControlType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SRVValveType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISurgeValveResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValvesResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValveUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

	@property
	def TimeOpenUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

	@property
	def DischargeCoefficient(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

	@property
	def SpringConstantUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

class ISurgeValve(IWaterNetworkElement[ISurgeValves, ISurgeValve, ISurgeValveUnits, ISurgeValveInput, ISurgeValveResults, ISurgeValvesInput, ISurgeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValves(IWaterNetworkElements[ISurgeValves, ISurgeValve, ISurgeValveUnits, ISurgeValveInput, ISurgeValveResults, ISurgeValvesInput, ISurgeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseOrificeNodeInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def OrificePressureDrop(self) -> float:
		"""No Description

		Returns:
			IBaseOrificeNodeInput: 
		"""
		pass

	@OrificePressureDrop.setter
	def OrificePressureDrop(self, orificepressuredrop: float) -> None:
		pass

	@property
	def OrificeFlow(self) -> float:
		"""No Description

		Returns:
			IBaseOrificeNodeInput: 
		"""
		pass

	@OrificeFlow.setter
	def OrificeFlow(self, orificeflow: float) -> None:
		pass

class IBaseOrificeNodesInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def OrificePressureDrop(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OrificeFlow(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseOrificeNodeResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseOrificeNodesResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseOrificeNodeUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseOrificeNodeUnits: 
		"""
		pass

class IPressureHeadFlowCollection(ICollectionElements[IPressureHeadFlows, IPressureHeadFlow, IPressureHeadFlowUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureHeadFlows(ICollection[IPressureHeadFlow]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, pressureHead: float, flow: float) -> IPressureHeadFlow:
		"""No Description

		Args:
			pressureHead(float): pressureHead
			flow(float): flow

		Returns:
			IPressureHeadFlow: 
		"""
		pass

	@overload
	def Add(self) -> IPressureHeadFlow:
		"""No Description

		Returns:
			IPressureHeadFlow: 
		"""
		pass

class IPressureHeadFlow(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureHead(self) -> float:
		"""No Description

		Returns:
			IPressureHeadFlow: 
		"""
		pass

	@PressureHead.setter
	def PressureHead(self, pressurehead: float) -> None:
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IPressureHeadFlow: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

class IPressureHeadFlowUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureHeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPressureHeadFlowUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPressureHeadFlowUnits: 
		"""
		pass

class IDischargeToAtmosphereNodeInput(IBaseOrificeNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DischargeElementType(self) -> DischargeToAtmosphereTypeEnum:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@DischargeElementType.setter
	def DischargeElementType(self, dischargeelementtype: DischargeToAtmosphereTypeEnum) -> None:
		pass

	@property
	def InitialGaseVolume(self) -> float:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@InitialGaseVolume.setter
	def InitialGaseVolume(self, initialgasevolume: float) -> None:
		pass

	@property
	def TimeToStartOperating(self) -> float:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@TimeToStartOperating.setter
	def TimeToStartOperating(self, timetostartoperating: float) -> None:
		pass

	@property
	def TimeToFullyOpenOrClose(self) -> float:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@TimeToFullyOpenOrClose.setter
	def TimeToFullyOpenOrClose(self, timetofullyopenorclose: float) -> None:
		pass

	@property
	def PressureHeadFlowCollection(self) -> IPressureHeadFlowCollection:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@property
	def InitialStatus(self) -> ValveTypeInitialStatusEnum:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: ValveTypeInitialStatusEnum) -> None:
		pass

	@property
	def ReportPeriod(self) -> int:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@ReportPeriod.setter
	def ReportPeriod(self, reportperiod: int) -> None:
		pass

class IDischargeToAtmosphereNodesInput(IBaseOrificeNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DischargeElementType(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InitialGasVolume(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToStartOpening(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToFullyOpenOrClose(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InitialStatus(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriod(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IDischargeToAtmosphereNodeResults(IBaseOrificeNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedDischarge(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def CalculatedDischarge(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedDischarges(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IDischargeToAtmosphereNodesResults(IBaseOrificeNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def CalculatedDischarge(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedDischarge(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def CalculatedDischarge(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IDischargeToAtmosphereUnits(IBaseOrificeNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDischargeToAtmosphereUnits: 
		"""
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDischargeToAtmosphereUnits: 
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDischargeToAtmosphereUnits: 
		"""
		pass

class IDischargeToAtmosphere(IWaterNetworkElement[IDischargeToAtmospheres, IDischargeToAtmosphere, IDischargeToAtmosphereUnits, IDischargeToAtmosphereNodeInput, IDischargeToAtmosphereNodeResults, IDischargeToAtmosphereNodesInput, IDischargeToAtmosphereNodesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDischargeToAtmospheres(IWaterNetworkElements[IDischargeToAtmospheres, IDischargeToAtmosphere, IDischargeToAtmosphereUnits, IDischargeToAtmosphereNodeInput, IDischargeToAtmosphereNodeResults, IDischargeToAtmosphereNodesInput, IDischargeToAtmosphereNodesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDiskInput(IBaseOrificeNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureThreshold(self) -> float:
		"""No Description

		Returns:
			IRuptureDiskInput: 
		"""
		pass

	@PressureThreshold.setter
	def PressureThreshold(self, pressurethreshold: float) -> None:
		pass

class IRuptureDisksInput(IBaseOrificeNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def PressureThreshold(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

class IRuptureDiskResults(IBaseOrificeNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDisksResults(IBaseOrificeNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDiskUnits(IBaseOrificeNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDisk(IWaterNetworkElement[IRuptureDisks, IRuptureDisk, IRuptureDiskUnits, IRuptureDiskInput, IRuptureDiskResults, IRuptureDisksInput, IRuptureDisksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDisks(IWaterNetworkElements[IRuptureDisks, IRuptureDisk, IRuptureDiskUnits, IRuptureDiskInput, IRuptureDiskResults, IRuptureDisksInput, IRuptureDisksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseNodesResults(IElementsResults, IWaterQualityElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def HydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPhysicalNodeElementInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Elevation(self) -> float:
		"""No Description

		Returns:
			IPhysicalNodeElementInput: 
		"""
		pass

	@Elevation.setter
	def Elevation(self, elevation: float) -> None:
		pass

class IPhysicalNodeElementsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Elevations(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Elevations(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseNodeInput(IPhysicalNodeElementInput, IWaterZoneableNetworkElementInput, IWaterQualityElementInput, IWaterQualityNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseNodesInput(IWaterZoneableNetworkElementsInput, IWaterQualityElementsInput, IWaterQualityNodesInput, IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseNodeResults(IElementResults, IWaterQualityResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def HydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def HydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IBaseNodeUnits(IGeometryUnits, IWaterQualityResultsUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def InitialAgeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def InitialConcentrationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def InitialTraceUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def BaseConcentrationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

class IReservoirs(IWaterNetworkElements[IReservoirs, IReservoir, IReservoirUnits, IReservoirInput, IReservoirResults, IReservoirsInput, IReservoirsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoir(IWaterNetworkElement[IReservoirs, IReservoir, IReservoirUnits, IReservoirInput, IReservoirResults, IReservoirsInput, IReservoirsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoirsResults(IBaseNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IReservoirResults(IBaseNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IReservoirInput(IBaseNodeInput, IWaterTraceableInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoirsInput(IBaseNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoirUnits(IBaseNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IReservoirUnits: 
		"""
		pass

class ITapInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AssociatedElement(self) -> IPipe:
		"""No Description

		Returns:
			ITapInput: 
		"""
		pass

	@AssociatedElement.setter
	def AssociatedElement(self, associatedelement: IPipe) -> None:
		pass

class ITapsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def AssociatedElements(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AssociatedElements(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITap(IWaterNetworkElement[ITaps, ITap, IGeometryUnits, ITapInput, IElementResults, ITapsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITaps(IWaterNetworkElements[ITaps, ITap, IGeometryUnits, ITapInput, IElementResults, ITapsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IIsolationValveElementInput(IPhysicalNodeElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ReferencedPipe(self) -> IPipe:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@ReferencedPipe.setter
	def ReferencedPipe(self, referencedpipe: IPipe) -> None:
		pass

	@property
	def ValveDiameter(self) -> float:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@ValveDiameter.setter
	def ValveDiameter(self, valvediameter: float) -> None:
		pass

	@property
	def MinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@MinorLossCoefficient.setter
	def MinorLossCoefficient(self, minorlosscoefficient: float) -> None:
		pass

	@property
	def IsOperable(self) -> bool:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@IsOperable.setter
	def IsOperable(self, isoperable: bool) -> None:
		pass

	@property
	def InitialStatus(self) -> IsolationValveInitialSetting:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: IsolationValveInitialSetting) -> None:
		pass

	@property
	def InstallationYear(self) -> int:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@InstallationYear.setter
	def InstallationYear(self, installationyear: int) -> None:
		pass

class IIsolationValveElementsInput(IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ReferencedPipes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ReferencedPipes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ValveDiameters(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ValveDiameters(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def MinorLossCoefficients(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def MinorLossCoefficients(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsOperables(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsOperables(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialStatuses(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InitialStatuses(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InstallationYears(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def InstallationYears(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IIsolatioNValveElementResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def HydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def HydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Pressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Pressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Flow(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Flow(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Velocity(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Velocity(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	def DistanceFromEndPoint(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IsClosed(self) -> Union[bool, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IsClosed(self, timeStepIndex: int) -> Union[bool, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def IsCloseds(self) -> array(Union[bool, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class IIsolationValveElementsResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def HydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Flows(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Velocities(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DistanceFromEndPoints(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DistanceFromEndPoints(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsCloseds(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsCloseds(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsCloseds(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IIsolationValveUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

class IIsolationValves(IWaterNetworkElements[IIsolationValves, IIsolationValve, IIsolationValveUnits, IIsolationValveElementInput, IIsolatioNValveElementResults, IIsolationValveElementsInput, IIsolationValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IIsolationValve(IWaterNetworkElement[IIsolationValves, IIsolationValve, IIsolationValveUnits, IIsolationValveElementInput, IIsolatioNValveElementResults, IIsolationValveElementsInput, IIsolationValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISpotElevationInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Elevation(self) -> float:
		"""No Description

		Returns:
			ISpotElevationInput: 
		"""
		pass

	@Elevation.setter
	def Elevation(self, elevation: float) -> None:
		pass

class ISpotElevationsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Elevations(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Elevations(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISpotElevationResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def EnhancedHydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def EnhancedHydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def EnhancedHydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def EnhancedPressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def EnhancedPressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def EnhancedPressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class ISpotElevationsResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def EnhancedHydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def EnhancedHydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def EnhancedHydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def EnhancedPressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def EnhancedPressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def EnhancedPressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISpotElevationUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpotElevationUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpotElevationUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpotElevationUnits: 
		"""
		pass

class ISpotElevation(IWaterNetworkElement[ISpotElevations, ISpotElevation, ISpotElevationUnits, ISpotElevationInput, ISpotElevationResults, ISpotElevationsInput, ISpotElevationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISpotElevations(IWaterNetworkElements[ISpotElevations, ISpotElevation, ISpotElevationUnits, ISpotElevationInput, ISpotElevationResults, ISpotElevationsInput, ISpotElevationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICustomerMeterInput(IPhysicalNodeElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@DemandPattern.setter
	def DemandPattern(self, demandpattern: IPattern) -> None:
		pass

	@property
	def BaseDemand(self) -> float:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@BaseDemand.setter
	def BaseDemand(self, basedemand: float) -> None:
		pass

	@property
	def StartDemandDistribution(self) -> float:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@StartDemandDistribution.setter
	def StartDemandDistribution(self, startdemanddistribution: float) -> None:
		pass

	@property
	def AssociatedElement(self) -> IWaterElement:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@AssociatedElement.setter
	def AssociatedElement(self, associatedelement: IWaterElement) -> None:
		pass

	@property
	def UnitDemand(self) -> IUnitDemandLoad:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@UnitDemand.setter
	def UnitDemand(self, unitdemand: IUnitDemandLoad) -> None:
		pass

	@property
	def UnitDemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@UnitDemandPattern.setter
	def UnitDemandPattern(self, unitdemandpattern: IPattern) -> None:
		pass

	@property
	def NumberOfUnitDemands(self) -> float:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@NumberOfUnitDemands.setter
	def NumberOfUnitDemands(self, numberofunitdemands: float) -> None:
		pass

class ICustomerMetersInput(IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def DemandPatterns(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def DemandPatterns(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def BaseDemands(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def BaseDemands(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def StartDemandDistributions(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def StartDemandDistributions(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AssociatedElements(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def AssociatedElements(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UnitDemands(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UnitDemands(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UnitDemandPatterns(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def UnitDemandPatterns(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def NumberOfUnitDemands(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def NumberOfUnitDemands(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICustomerMeterResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def HydraulicGrade(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def HydraulicGrade(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

	@overload
	def Pressure(self) -> Union[float, None]:
		"""No Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def Pressure(self, timeStepIndex: int) -> Union[float, None]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""No Description

		Returns:
			array(Nullable): 
		"""
		pass

class ICustomerMetersResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def HydraulicGrades(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HydraulicGrades(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Pressures(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICustomerMeterUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICustomerMeterUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICustomerMeterUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICustomerMeterUnits: 
		"""
		pass

class ICustomerMeter(IWaterNetworkElement[ICustomerMeters, ICustomerMeter, ICustomerMeterUnits, ICustomerMeterInput, ICustomerMeterResults, ICustomerMetersInput, ICustomerMetersResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICustomerMeters(IWaterNetworkElements[ICustomerMeters, ICustomerMeter, ICustomerMeterUnits, ICustomerMeterInput, ICustomerMeterResults, ICustomerMetersInput, ICustomerMetersResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISCADAElementInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TargetElement(self) -> IWaterElement:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@TargetElement.setter
	def TargetElement(self, targetelement: IWaterElement) -> None:
		pass

	@property
	def RealtimeSignal(self) -> ISCADASignal:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@RealtimeSignal.setter
	def RealtimeSignal(self, realtimesignal: ISCADASignal) -> None:
		pass

	@property
	def HistoricalSignal(self) -> ISCADASignal:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@HistoricalSignal.setter
	def HistoricalSignal(self, historicalsignal: ISCADASignal) -> None:
		pass

	@property
	def TargetAttribute(self) -> SCADATargetAttribute:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@TargetAttribute.setter
	def TargetAttribute(self, targetattribute: SCADATargetAttribute) -> None:
		pass

class ISCADAElementsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def TargetElements(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def TargetElements(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def RealtimeSignals(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def RealtimeSignals(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HistoricalSignals(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def HistoricalSignals(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISCADAElement(IWaterNetworkElement[ISCADAElements, ISCADAElement, IGeometryUnits, ISCADAElementInput, IElementResults, ISCADAElementsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISCADAElements(IWaterNetworkElements[ISCADAElements, ISCADAElement, IGeometryUnits, ISCADAElementInput, IElementResults, ISCADAElementsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStations(IWaterNetworkElements[IPumpStations, IPumpStation, IPumpStationUnits, IPumpStationInput, IPumpStationResults, IPumpStationsInput, IPumpStationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStation(IWaterNetworkElement[IPumpStations, IPumpStation, IPumpStationUnits, IPumpStationInput, IPumpStationResults, IPumpStationsInput, IPumpStationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationsInput(IBasePolygonsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationsResults(IBasePolygonsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationResults(IBasePolygonResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationInput(IBasePolygonInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pumps(self) -> IPumpStationPumpIDsCollection:
		"""No Description

		Returns:
			IPumpStationInput: 
		"""
		pass

class IPumpStationPumpIDsCollection(ICollectionElements[IPumpStationPumpIDs, IPumpStationPumpID, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationPumpIDs(ICollection[IPumpStationPumpID]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Add(self, pump: IPump, pumpDefinition: IPumpDefinition) -> IPumpStationPumpID:
		"""No Description

		Args:
			pump(IPump): pump
			pumpDefinition(IPumpDefinition): pumpDefinition

		Returns:
			IPumpStationPumpID: 
		"""
		pass

	@overload
	def Add(self) -> IPumpStationPumpID:
		"""No Description

		Returns:
			IPumpStationPumpID: 
		"""
		pass

class IPumpStationPumpID(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pump(self) -> IElement:
		"""No Description

		Returns:
			IPumpStationPumpID: 
		"""
		pass

	@Pump.setter
	def Pump(self, pump: IElement) -> None:
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinition:
		"""No Description

		Returns:
			IPumpStationPumpID: 
		"""
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

