from enum import Enum
from System import TypeCode, ICloneable
from typing import overload, List, Dict, Iterator
from array import array

class DictionaryEntryExStringType(Enum):
	Key = 0
	Value = 1

class FieldDataType(Enum):
	Integer = 1
	Real = 2
	Text = 3
	LongText = 4
	DateTime = 5
	Boolean = 6
	LongBinary = 7
	Referenced = 8
	Collection = 9
	Enumerated = 10

class SystemType(Enum):
	Bool = 1
	Byte = 2
	Char = 3
	DateTime = 4
	Decimal = 5
	Delegate = 6
	Double = 7
	Int = 8
	Long = 9
	Object = 10
	SelectionSet = 11
	String = 12
	Guid = 13

class SymbolStyle(Enum):
	None = 0
	CAD = 1
	GIS = 2

class SetValuesOperation(Enum):
	Add = 1
	Divide = 2
	Multiply = 3
	Set = 4
	Subtract = 5

class ComparisonOperator(Enum):
	NoOperator = 0
	EqualTo = 1
	NotEqualTo = 2
	GreaterThan = 3
	GreaterThanOrEqualTo = 4
	LessThan = 5
	LessThanOrEqualTo = 6
	Contains = 7
	BeginsWith = 8

class SortOrder(Enum):
	Ascending = 1
	Descending = 2

class HmiProductBeta(Enum):
	None = 0
	Test = 1
	Maryland = 2
	Vegas = 3
	Delaware = 4
	Hammer = 5
	Idaho = 6
	UDX = 7
	Idaho_WaterCAD = 8
	Florida = 9
	Toronto = 10
	Alabama = 11
	Montana = 12
	GasAnalysis = 14
	Florida_UK = 15
	Washington = 16
	ControlRoom = 17
	SUE = 18
	DigitalWaterWorks = 19
	SewerOPS = 20
	WaterOPS = 21
	Shanghai = 22

class HmiProductRelease(Enum):
	None = 0
	Test = 1
	CivilStormDynamic = 2
	FlowMaster = 3
	SewerGEMS = 4
	Hammer = 5
	WaterGEMS = 6
	UserDataExtensions = 7
	WaterCAD = 8
	StormCAD = 9
	HAMMERXM = 10
	SewerCAD = 11
	PondPack = 12
	GasAnalysis = 14
	StormCAD_UK = 15
	SUDA = 16
	ControlRoom = 17
	SUE = 18
	DigitalWaterWorks = 19
	SewerOPS = 20
	WaterOPS = 21
	Shanghai = 22

class hmiProjectType(Enum):
	hmiAllProject = 0
	hmiWaterProject = 1
	hmiSewerProject = 2
	hmiStormProject = 3
	hmiPondProject = 4
	hmiDynProject = 5
	hmiPumpMasterProject = 6
	hmiGDBConnectProject = 7
	hmiHammerProject = 8
	hmiFlowMasterProject = 9
	hmiCulvertMasterProject = 10
	hmiHendersonProject = 11

class LockType(Enum):
	None = 0
	Optimistic = 1
	Pessimistic = 2

class HaestadDocumentSpecificationType(Enum):
	Local = 0
	ProjectWise = 1
	Multifile = 2
	Invalid = 3
	PWCS = 4

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

class CompareType(Enum):
	IncreasingX = 0
	IncreasingY = 1

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class Tag(Enum):
	Default = 0

class FieldCollection(List, ICloneable):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FieldCollection``) :  c
			a (``List[IField]``) :  a
		"""
		pass

	@overload
	def __init__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FieldCollection``) :  c
			a (``List[IField]``) :  a
		"""
		pass

	@overload
	def __init__(self, c: FieldCollection) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FieldCollection``) :  c
			a (``List[IField]``) :  a
		"""
		pass

	@overload
	def __init__(self, a: List[IField]) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FieldCollection``) :  c
			a (``List[IField]``) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: FieldCollection) -> FieldCollection:
		"""No Description

		Args
		--------
			list (``FieldCollection``) :  list

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: FieldCollection) -> FieldCollection:
		"""No Description

		Args
		--------
			list (``FieldCollection``) :  list

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IField]) -> None:
		"""No Description

		Args
		--------
			array (``List[IField]``) :  array

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IField], start: int) -> None:
		"""No Description

		Args
		--------
			array (``List[IField]``) :  array
			start (``int``) :  start

		Returns
		--------
			``None`` : 
		"""
		pass

	def Add(self, item: IField) -> int:
		"""No Description

		Args
		--------
			item (``IField``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

	def Contains(self, item: IField) -> bool:
		"""No Description

		Args
		--------
			item (``IField``) :  item

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IndexOf(self, item: IField) -> int:
		"""No Description

		Args
		--------
			item (``IField``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Insert(self, index: int, item: IField) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index
			item (``IField``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def Remove(self, item: IField) -> None:
		"""No Description

		Args
		--------
			item (``IField``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetEnumerator(self) -> IFieldCollectionEnumerator:
		"""No Description

		Returns
		--------
			``IFieldCollectionEnumerator`` : 
		"""
		pass

	@overload
	def AddRange(self, x: FieldCollection) -> int:
		"""No Description

		Args
		--------
			x (``FieldCollection``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IField]) -> int:
		"""No Description

		Args
		--------
			x (``List[IField]``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def Item(self) -> IField:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IField) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class FilterContextCollection(List, ICloneable):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FilterContextCollection``) :  c
			a (``List[IFilterContext]``) :  a
		"""
		pass

	@overload
	def __init__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FilterContextCollection``) :  c
			a (``List[IFilterContext]``) :  a
		"""
		pass

	@overload
	def __init__(self, c: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FilterContextCollection``) :  c
			a (``List[IFilterContext]``) :  a
		"""
		pass

	@overload
	def __init__(self, a: List[IFilterContext]) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``FilterContextCollection``) :  c
			a (``List[IFilterContext]``) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: FilterContextCollection) -> FilterContextCollection:
		"""No Description

		Args
		--------
			list (``FilterContextCollection``) :  list

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: FilterContextCollection) -> FilterContextCollection:
		"""No Description

		Args
		--------
			list (``FilterContextCollection``) :  list

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFilterContext]) -> None:
		"""No Description

		Args
		--------
			array (``List[IFilterContext]``) :  array

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[IFilterContext], start: int) -> None:
		"""No Description

		Args
		--------
			array (``List[IFilterContext]``) :  array
			start (``int``) :  start

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def Add(self, item: IFilterContext) -> int:
		"""No Description

		Args
		--------
			item (``IFilterContext``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def Add(self, field: IField, comparisonOperator: ComparisonOperator, value: object) -> int:
		"""No Description

		Args
		--------
			field (``IField``) :  field
			comparisonOperator (``ComparisonOperator``) :  comparisonOperator
			value (``object``) :  value

		Returns
		--------
			``int`` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

	def Contains(self, item: IFilterContext) -> bool:
		"""No Description

		Args
		--------
			item (``IFilterContext``) :  item

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IndexOf(self, item: IFilterContext) -> int:
		"""No Description

		Args
		--------
			item (``IFilterContext``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Insert(self, index: int, item: IFilterContext) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index
			item (``IFilterContext``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def Remove(self, item: IFilterContext) -> None:
		"""No Description

		Args
		--------
			item (``IFilterContext``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetEnumerator(self) -> IFilterContextCollectionEnumerator:
		"""No Description

		Returns
		--------
			``IFilterContextCollectionEnumerator`` : 
		"""
		pass

	@overload
	def AddRange(self, x: FilterContextCollection) -> int:
		"""No Description

		Args
		--------
			x (``FilterContextCollection``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[IFilterContext]) -> int:
		"""No Description

		Args
		--------
			x (``List[IFilterContext]``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def AdditionalFilterSQL(self) -> str:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@AdditionalFilterSQL.setter
	def AdditionalFilterSQL(self, additionalfiltersql: str) -> None:
		pass

	@property
	def AdditionalFilterStringToFieldsMap(self) -> Dict:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@AdditionalFilterStringToFieldsMap.setter
	def AdditionalFilterStringToFieldsMap(self, additionalfilterstringtofieldsmap: Dict) -> None:
		pass

	@property
	def IdsToFilter(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@IdsToFilter.setter
	def IdsToFilter(self, idstofilter: HmIDCollection) -> None:
		pass

	@property
	def UseSmartLabels(self) -> bool:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@UseSmartLabels.setter
	def UseSmartLabels(self, usesmartlabels: bool) -> None:
		pass

	@property
	def IsEmpty(self) -> bool:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@property
	def SelectNOTElementIDs(self) -> bool:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@SelectNOTElementIDs.setter
	def SelectNOTElementIDs(self, selectnotelementids: bool) -> None:
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@property
	def Item(self) -> IFilterContext:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@Item.setter
	def Item(self, item: IFilterContext) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			``FilterContextCollection`` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class GeometryPoint:

	def __init__(self, x: float, y: float) -> None:
		"""No Description

		Args
		--------
			x (``float``) :  x
			y (``float``) :  y
		"""
		pass

	def MoveBy(self, x: float, y: float) -> None:
		"""No Description

		Args
		--------
			x (``float``) :  x
			y (``float``) :  y

		Returns
		--------
			``None`` : 
		"""
		pass

	@staticmethod
	def op_Equality(point1: GeometryPoint, point2: GeometryPoint) -> bool:
		"""No Description

		Args
		--------
			point1 (``GeometryPoint``) :  point1
			point2 (``GeometryPoint``) :  point2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def op_Inequality(point1: GeometryPoint, point2: GeometryPoint) -> bool:
		"""No Description

		Args
		--------
			point1 (``GeometryPoint``) :  point1
			point2 (``GeometryPoint``) :  point2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def op_Addition(left: GeometryPoint, right: GeometryPoint) -> GeometryPoint:
		"""No Description

		Args
		--------
			left (``GeometryPoint``) :  left
			right (``GeometryPoint``) :  right

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	@staticmethod
	def op_Subtraction(left: GeometryPoint, right: GeometryPoint) -> GeometryPoint:
		"""No Description

		Args
		--------
			left (``GeometryPoint``) :  left
			right (``GeometryPoint``) :  right

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	@staticmethod
	def op_UnaryPlus(point: GeometryPoint) -> GeometryPoint:
		"""No Description

		Args
		--------
			point (``GeometryPoint``) :  point

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	@staticmethod
	def op_UnaryNegation(point: GeometryPoint) -> GeometryPoint:
		"""No Description

		Args
		--------
			point (``GeometryPoint``) :  point

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	@staticmethod
	def op_Addition(left: GeometryPoint, right: GeometryPoint) -> GeometryPoint:
		"""No Description

		Args
		--------
			left (``GeometryPoint``) :  left
			right (``GeometryPoint``) :  right

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	@staticmethod
	def op_Equality(point1: GeometryPoint, point2: GeometryPoint) -> bool:
		"""No Description

		Args
		--------
			point1 (``GeometryPoint``) :  point1
			point2 (``GeometryPoint``) :  point2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def op_Inequality(point1: GeometryPoint, point2: GeometryPoint) -> bool:
		"""No Description

		Args
		--------
			point1 (``GeometryPoint``) :  point1
			point2 (``GeometryPoint``) :  point2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def op_Subtraction(left: GeometryPoint, right: GeometryPoint) -> GeometryPoint:
		"""No Description

		Args
		--------
			left (``GeometryPoint``) :  left
			right (``GeometryPoint``) :  right

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	@property
	def X(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryPoint`` : 
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
			``GeometryPoint`` : 
		"""
		pass

	@Y.setter
	def Y(self, y: float) -> None:
		pass

	@property
	def IsEmpty(self) -> bool:
		"""No Description

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	@staticmethod
	@property
	def Empty() -> GeometryPoint:
		"""No Description

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

class GeometryRectangle:

	def __init__(self, x: float, y: float, width: float, height: float) -> None:
		"""No Description

		Args
		--------
			x (``float``) :  x
			y (``float``) :  y
			width (``float``) :  width
			height (``float``) :  height
		"""
		pass

	@overload
	def Contains(self, point: GeometryPoint) -> bool:
		"""No Description

		Args
		--------
			point (``GeometryPoint``) :  point

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def Contains(self, x: float, y: float) -> bool:
		"""No Description

		Args
		--------
			x (``float``) :  x
			y (``float``) :  y

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def Contains(self, rectangle: GeometryRectangle) -> bool:
		"""No Description

		Args
		--------
			rectangle (``GeometryRectangle``) :  rectangle

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Inflate(self, x: float, y: float) -> None:
		"""No Description

		Args
		--------
			x (``float``) :  x
			y (``float``) :  y

		Returns
		--------
			``None`` : 
		"""
		pass

	def Offset(self, x: float, y: float) -> None:
		"""No Description

		Args
		--------
			x (``float``) :  x
			y (``float``) :  y

		Returns
		--------
			``None`` : 
		"""
		pass

	def CreatePositiveCopy(self) -> GeometryRectangle:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@staticmethod
	def FromLTRB(left: float, top: float, right: float, bottom: float) -> GeometryRectangle:
		"""No Description

		Args
		--------
			left (``float``) :  left
			top (``float``) :  top
			right (``float``) :  right
			bottom (``float``) :  bottom

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@staticmethod
	def Union(rectangle1: GeometryRectangle, rectangle2: GeometryRectangle) -> GeometryRectangle:
		"""No Description

		Args
		--------
			rectangle1 (``GeometryRectangle``) :  rectangle1
			rectangle2 (``GeometryRectangle``) :  rectangle2

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@staticmethod
	def op_Equality(rectangle1: GeometryRectangle, rectangle2: GeometryRectangle) -> bool:
		"""No Description

		Args
		--------
			rectangle1 (``GeometryRectangle``) :  rectangle1
			rectangle2 (``GeometryRectangle``) :  rectangle2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def op_Inequality(rectangle1: GeometryRectangle, rectangle2: GeometryRectangle) -> bool:
		"""No Description

		Args
		--------
			rectangle1 (``GeometryRectangle``) :  rectangle1
			rectangle2 (``GeometryRectangle``) :  rectangle2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def op_Equality(rectangle1: GeometryRectangle, rectangle2: GeometryRectangle) -> bool:
		"""No Description

		Args
		--------
			rectangle1 (``GeometryRectangle``) :  rectangle1
			rectangle2 (``GeometryRectangle``) :  rectangle2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@staticmethod
	def op_Inequality(rectangle1: GeometryRectangle, rectangle2: GeometryRectangle) -> bool:
		"""No Description

		Args
		--------
			rectangle1 (``GeometryRectangle``) :  rectangle1
			rectangle2 (``GeometryRectangle``) :  rectangle2

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def X(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
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
			``GeometryRectangle`` : 
		"""
		pass

	@Y.setter
	def Y(self, y: float) -> None:
		pass

	@property
	def Width(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@Width.setter
	def Width(self, width: float) -> None:
		pass

	@property
	def Height(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@Height.setter
	def Height(self, height: float) -> None:
		pass

	@property
	def Left(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@property
	def Right(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@property
	def Top(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@property
	def Bottom(self) -> float:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@property
	def IsEmpty(self) -> bool:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@property
	def Center(self) -> GeometryPoint:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

	@staticmethod
	@property
	def Empty() -> GeometryRectangle:
		"""No Description

		Returns
		--------
			``GeometryRectangle`` : 
		"""
		pass

class HmIDCollection(List, ICloneable):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``HmIDCollection``) :  c
			a (``array[int]``) :  a
		"""
		pass

	@overload
	def __init__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``HmIDCollection``) :  c
			a (``array[int]``) :  a
		"""
		pass

	@overload
	def __init__(self, c: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``HmIDCollection``) :  c
			a (``array[int]``) :  a
		"""
		pass

	@overload
	def __init__(self, a: array[int]) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``HmIDCollection``) :  c
			a (``array[int]``) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			list (``HmIDCollection``) :  list

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			list (``HmIDCollection``) :  list

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int]) -> None:
		"""No Description

		Args
		--------
			array (``array[int]``) :  array

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], start: int) -> None:
		"""No Description

		Args
		--------
			array (``array[int]``) :  array
			start (``int``) :  start

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: array[int], startInTarget: int, startInSource: int, length: int) -> None:
		"""No Description

		Args
		--------
			array (``array[int]``) :  array
			startInTarget (``int``) :  startInTarget
			startInSource (``int``) :  startInSource
			length (``int``) :  length

		Returns
		--------
			``None`` : 
		"""
		pass

	def Add(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

	def Contains(self, item: int) -> bool:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IndexOf(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Insert(self, index: int, item: int) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index
			item (``int``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def Remove(self, item: int) -> None:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetEnumerator(self) -> IHmIDCollectionEnumerator:
		"""No Description

		Returns
		--------
			``IHmIDCollectionEnumerator`` : 
		"""
		pass

	@overload
	def AddRange(self, x: HmIDCollection) -> int:
		"""No Description

		Args
		--------
			x (``HmIDCollection``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def AddRange(self, x: array[int]) -> int:
		"""No Description

		Args
		--------
			x (``array[int]``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Sort(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def ReverseInPlace(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def ToArray(self) -> array[int]:
		"""No Description

		Returns
		--------
			``array[int]`` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def Item(self) -> int:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
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
			``HmIDCollection`` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

class IField:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, id: int) -> object:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``object`` : 
		"""
		pass

	@overload
	def GetValues(self) -> Dict:
		"""No Description

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetValues(self, ids: HmIDCollection) -> Dict:
		"""No Description

		Args
		--------
			ids (``HmIDCollection``) :  ids

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns
		--------
			``IField`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``IField`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``IField`` : 
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
			``IField`` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def Category(self) -> str:
		"""No Description

		Returns
		--------
			``IField`` : 
		"""
		pass

	@Category.setter
	def Category(self, category: str) -> None:
		pass

	@property
	def FieldDataType(self) -> FieldDataType:
		"""No Description

		Returns
		--------
			``IField`` : 
		"""
		pass

class IEditField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetValue(self, id: int, value: object) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetValues(self, operation: SetValuesOperation, value: object) -> None:
		"""No Description

		Args
		--------
			operation (``SetValuesOperation``) :  operation
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def DefaultValue(self) -> object:
		"""No Description

		Returns
		--------
			``IEditField`` : 
		"""
		pass

class IFilterContext:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Field(self) -> IField:
		"""No Description

		Returns
		--------
			``IFilterContext`` : 
		"""
		pass

	@Field.setter
	def Field(self, field: IField) -> None:
		pass

	@property
	def ComparisonOperator(self) -> ComparisonOperator:
		"""No Description

		Returns
		--------
			``IFilterContext`` : 
		"""
		pass

	@ComparisonOperator.setter
	def ComparisonOperator(self, comparisonoperator: ComparisonOperator) -> None:
		pass

	@property
	def Value(self) -> object:
		"""No Description

		Returns
		--------
			``IFilterContext`` : 
		"""
		pass

	@Value.setter
	def Value(self, value: object) -> None:
		pass

	@property
	def AlternativeID(self) -> int:
		"""No Description

		Returns
		--------
			``IFilterContext`` : 
		"""
		pass

	@AlternativeID.setter
	def AlternativeID(self, alternativeid: int) -> None:
		pass

class ISortContext:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Field(self) -> IField:
		"""No Description

		Returns
		--------
			``ISortContext`` : 
		"""
		pass

	@Field.setter
	def Field(self, field: IField) -> None:
		pass

	@property
	def SortOrder(self) -> SortOrder:
		"""No Description

		Returns
		--------
			``ISortContext`` : 
		"""
		pass

	@SortOrder.setter
	def SortOrder(self, sortorder: SortOrder) -> None:
		pass

	@property
	def AlternativeID(self) -> int:
		"""No Description

		Returns
		--------
			``ISortContext`` : 
		"""
		pass

	@AlternativeID.setter
	def AlternativeID(self, alternativeid: int) -> None:
		pass

class IEditLabeled(ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``IEditLabeled`` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

class ILabeled:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``ILabeled`` : 
		"""
		pass

class INamable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``INamable`` : 
		"""
		pass

class SortContextCollection(List, ICloneable):

	@overload
	def __init__(self) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``SortContextCollection``) :  c
			a (``List[ISortContext]``) :  a
		"""
		pass

	@overload
	def __init__(self, capacity: int) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``SortContextCollection``) :  c
			a (``List[ISortContext]``) :  a
		"""
		pass

	@overload
	def __init__(self, c: SortContextCollection) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``SortContextCollection``) :  c
			a (``List[ISortContext]``) :  a
		"""
		pass

	@overload
	def __init__(self, a: List[ISortContext]) -> None:
		"""No Description

		Args
		--------
			capacity (``int``) :  capacity
			c (``SortContextCollection``) :  c
			a (``List[ISortContext]``) :  a
		"""
		pass

	@staticmethod
	def Synchronized(list: SortContextCollection) -> SortContextCollection:
		"""No Description

		Args
		--------
			list (``SortContextCollection``) :  list

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@staticmethod
	def ReadOnly(list: SortContextCollection) -> SortContextCollection:
		"""No Description

		Args
		--------
			list (``SortContextCollection``) :  list

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISortContext]) -> None:
		"""No Description

		Args
		--------
			array (``List[ISortContext]``) :  array

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def CopyTo(self, array: List[ISortContext], start: int) -> None:
		"""No Description

		Args
		--------
			array (``List[ISortContext]``) :  array
			start (``int``) :  start

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def Add(self, item: ISortContext) -> int:
		"""No Description

		Args
		--------
			item (``ISortContext``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def Add(self, field: IField, sortOrder: SortOrder) -> int:
		"""No Description

		Args
		--------
			field (``IField``) :  field
			sortOrder (``SortOrder``) :  sortOrder

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def Add(self, field: IField, sortOrder: SortOrder, enumLabels: array[str], enumValues: array[int]) -> int:
		"""No Description

		Args
		--------
			field (``IField``) :  field
			sortOrder (``SortOrder``) :  sortOrder
			enumLabels (``array[str]``) :  enumLabels
			enumValues (``array[int]``) :  enumValues

		Returns
		--------
			``int`` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

	def Contains(self, item: ISortContext) -> bool:
		"""No Description

		Args
		--------
			item (``ISortContext``) :  item

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IndexOf(self, item: ISortContext) -> int:
		"""No Description

		Args
		--------
			item (``ISortContext``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Insert(self, index: int, item: ISortContext) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index
			item (``ISortContext``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def Remove(self, item: ISortContext) -> None:
		"""No Description

		Args
		--------
			item (``ISortContext``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetEnumerator(self) -> ISortContextCollectionEnumerator:
		"""No Description

		Returns
		--------
			``ISortContextCollectionEnumerator`` : 
		"""
		pass

	@overload
	def AddRange(self, x: SortContextCollection) -> int:
		"""No Description

		Args
		--------
			x (``SortContextCollection``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def AddRange(self, x: List[ISortContext]) -> int:
		"""No Description

		Args
		--------
			x (``List[ISortContext]``) :  x

		Returns
		--------
			``int`` : 
		"""
		pass

	def TrimToSize(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def UseSmartLabels(self) -> bool:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@UseSmartLabels.setter
	def UseSmartLabels(self, usesmartlabels: bool) -> None:
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@property
	def IsSynchronized(self) -> bool:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@property
	def SyncRoot(self) -> object:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@property
	def Item(self) -> ISortContext:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@Item.setter
	def Item(self, item: ISortContext) -> None:
		pass

	@property
	def IsFixedSize(self) -> bool:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@property
	def Capacity(self) -> int:
		"""No Description

		Returns
		--------
			``SortContextCollection`` : 
		"""
		pass

	@Capacity.setter
	def Capacity(self, capacity: int) -> None:
		pass

