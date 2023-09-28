from typing import overload
from datetime import datetime
from enum import Enum
from System import TypeCode

class StreamingContextStates(Enum):
	CrossProcess = 1
	CrossMachine = 2
	File = 4
	Persistence = 8
	Remoting = 16
	Other = 32
	Clone = 64
	CrossAppDomain = 128
	All = 255

class ISerializable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
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

class SerializationInfo:

	@overload
	def __init__(self, type: Type, converter: IFormatterConverter) -> None:
		"""No Description

		Args
		--------
			type (``Type``) :  type
			converter (``IFormatterConverter``) :  converter
			type (``Type``) :  type
			converter (``IFormatterConverter``) :  converter
			requireSameTokenInPartialTrust (``bool``) :  requireSameTokenInPartialTrust
		"""
		pass

	@overload
	def __init__(self, type: Type, converter: IFormatterConverter, requireSameTokenInPartialTrust: bool) -> None:
		"""No Description

		Args
		--------
			type (``Type``) :  type
			converter (``IFormatterConverter``) :  converter
			type (``Type``) :  type
			converter (``IFormatterConverter``) :  converter
			requireSameTokenInPartialTrust (``bool``) :  requireSameTokenInPartialTrust
		"""
		pass

	def SetType(self, type: Type) -> None:
		"""No Description

		Args
		--------
			type (``Type``) :  type

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetEnumerator(self) -> SerializationInfoEnumerator:
		"""No Description

		Returns
		--------
			``SerializationInfoEnumerator`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: object, type: Type) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``object``) :  value
			type (``Type``) :  type

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: object) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: bool) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``bool``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``str``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: int) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``int``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: float) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``float``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: float) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``float``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: float) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``float``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddValue(self, name: str, value: datetime) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name
			value (``datetime``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetValue(self, name: str, type: Type) -> object:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``Type``) :  type

		Returns
		--------
			``object`` : 
		"""
		pass

	def GetBoolean(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetChar(self, name: str) -> str:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetSByte(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetByte(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetInt16(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetUInt16(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetInt32(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetUInt32(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetInt64(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetUInt64(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetSingle(self, name: str) -> float:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``float`` : 
		"""
		pass

	def GetDouble(self, name: str) -> float:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``float`` : 
		"""
		pass

	def GetDecimal(self, name: str) -> float:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``float`` : 
		"""
		pass

	def GetDateTime(self, name: str) -> datetime:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def GetString(self, name: str) -> str:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def FullTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``SerializationInfo`` : 
		"""
		pass

	@FullTypeName.setter
	def FullTypeName(self, fulltypename: str) -> None:
		pass

	@property
	def AssemblyName(self) -> str:
		"""No Description

		Returns
		--------
			``SerializationInfo`` : 
		"""
		pass

	@AssemblyName.setter
	def AssemblyName(self, assemblyname: str) -> None:
		pass

	@property
	def MemberCount(self) -> int:
		"""No Description

		Returns
		--------
			``SerializationInfo`` : 
		"""
		pass

	@property
	def ObjectType(self) -> Type:
		"""No Description

		Returns
		--------
			``SerializationInfo`` : 
		"""
		pass

	@property
	def IsFullTypeNameSetExplicit(self) -> bool:
		"""No Description

		Returns
		--------
			``SerializationInfo`` : 
		"""
		pass

	@property
	def IsAssemblyNameSetExplicit(self) -> bool:
		"""No Description

		Returns
		--------
			``SerializationInfo`` : 
		"""
		pass

class StreamingContext:

	@overload
	def __init__(self, state: StreamingContextStates) -> None:
		"""No Description

		Args
		--------
			state (``StreamingContextStates``) :  state
			state (``StreamingContextStates``) :  state
			additional (``object``) :  additional
		"""
		pass

	@overload
	def __init__(self, state: StreamingContextStates, additional: object) -> None:
		"""No Description

		Args
		--------
			state (``StreamingContextStates``) :  state
			state (``StreamingContextStates``) :  state
			additional (``object``) :  additional
		"""
		pass

	@property
	def Context(self) -> object:
		"""No Description

		Returns
		--------
			``StreamingContext`` : 
		"""
		pass

	@property
	def State(self) -> StreamingContextStates:
		"""No Description

		Returns
		--------
			``StreamingContext`` : 
		"""
		pass

