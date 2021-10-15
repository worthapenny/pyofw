from enum import Enum
from typing import Generic, overload, TypeVar
from Haestad.Support.Units import Unit, Dimension

TNetworkUnitsType = TypeVar("TNetworkUnitsType", INetworkUnits)
TComponentUnitsType = TypeVar("TComponentUnitsType", IComponentUnits)

class FormatCode(Enum):
	Fixed = 0
	General = 1
	ScientificNotation = 2
	Number = 3

class UnitSystemType(Enum):
	USCustomary = 0
	SI = 1

class IModelUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> IUnits:
		"""No Description

		Returns:
			IModelUnits: 
		"""
		pass

class INetworkUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def FormatValue(self, value: float, unit: IUnit) -> str:
		"""No Description

		Args:
			value(float): value
			unit(IUnit): unit

		Returns:
			str: 
		"""
		pass

	@overload
	def FormatValue(self, value: float, unit: IUnit, format: FormatCode, signficantDigits: int) -> str:
		"""No Description

		Args:
			value(float): value
			unit(IUnit): unit
			format(FormatCode): format
			signficantDigits(int): signficantDigits

		Returns:
			str: 
		"""
		pass

	def ConvertValue(self, value: float, fromUnit: Unit, toUnit: Unit) -> float:
		"""No Description

		Args:
			value(float): value
			fromUnit(Unit): fromUnit
			toUnit(Unit): toUnit

		Returns:
			float: 
		"""
		pass

	def Reset(self, unitSystem: UnitSystemType) -> None:
		"""No Description

		Args:
			unitSystem(UnitSystemType): unitSystem

		Returns:
			None: 
		"""
		pass

	@property
	def NetworkUnits(self) -> TNetworkUnitsType:
		"""No Description

		Returns:
			IUnits: 
		"""
		pass

	@property
	def ComponentUnits(self) -> TComponentUnitsType:
		"""No Description

		Returns:
			IUnits: 
		"""
		pass

class IUnit:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def FormatValue(self, value: float) -> str:
		"""No Description

		Args:
			value(float): value

		Returns:
			str: 
		"""
		pass

	@overload
	def FormatValue(self, value: float, format: FormatCode, significantDigits: int) -> str:
		"""No Description

		Args:
			value(float): value
			format(FormatCode): format
			significantDigits(int): significantDigits

		Returns:
			str: 
		"""
		pass

	def SetUnit(self, unit: Unit) -> None:
		"""No Description

		Args:
			unit(Unit): unit

		Returns:
			None: 
		"""
		pass

	def GetUnit(self) -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	def ConvertTo(self, value: float, unit: Unit) -> float:
		"""No Description

		Args:
			value(float): value
			unit(Unit): unit

		Returns:
			float: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@property
	def FormatCode(self) -> FormatCode:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: FormatCode) -> None:
		pass

	@property
	def SignificantDigits(self) -> int:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@SignificantDigits.setter
	def SignificantDigits(self, significantdigits: int) -> None:
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

