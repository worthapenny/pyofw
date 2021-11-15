from enum import Enum
from System import TypeCode
from Haestad.Support.Support import IField, FieldDataType, INamable, ILabeled
from Haestad.Domain import DomainFieldType
from Haestad.Support.Units import Unit
from OpenFlows.Units import IUnit
from System.Collections.Generic import IReadOnlyCollection
from typing import List, Generic, TypeVar

TValueType = TypeVar("TValueType")
TNetworkElementTypeEnum = TypeVar("TNetworkElementTypeEnum", Enum)
TFieldType = TypeVar("TFieldType")
TNetworkElementType = TypeVar("TNetworkElementType", Enum)

class UserFieldDataType(Enum):
	Integer = 1
	Real = 2
	LongText = 4
	DateTime = 5
	Boolean = 6

class IFieldInfo(INamable, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, id: int) -> TValueType:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``TValueType`` : 
		"""
		pass

	def SetValue(self, id: int, value: TValueType) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id
			value (``TValueType``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Field(self) -> IField:
		"""The field associated with this FieldInfo

		Returns
		--------
			``IFieldInfo`` : 
		"""
		pass

	@property
	def FieldType(self) -> DomainFieldType:
		"""The type of field - domain, support, scenario, etc.

		Returns
		--------
			``IFieldInfo`` : 
		"""
		pass

	@property
	def FieldDataType(self) -> FieldDataType:
		"""The value type for this field when retrieved.

		Returns
		--------
			``IFieldInfo`` : 
		"""
		pass

	@property
	def StorageUnit(self) -> Unit:
		"""If unitized, the storage unit the value is stored in.

		Returns
		--------
			``IFieldInfo`` : 
		"""
		pass

	@property
	def Unit(self) -> IUnit:
		"""If unitized, the format information for the field.

		Returns
		--------
			``IFieldInfo`` : 
		"""
		pass

class INetworkFieldInfo(IFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeTypeName(self) -> str:
		"""The name of the alternative type this field belongs to.

		Returns
		--------
			``INetworkFieldInfo`` : 
		"""
		pass

	@property
	def DomainElementTypeName(self) -> str:
		"""The name of the domain element type that this field is assigned.

		Returns
		--------
			``INetworkFieldInfo`` : 
		"""
		pass

class IUserNetworkfieldInfo(INetworkFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Delete(self) -> None:
		"""Deletes the user defined field from all supported element types.

		Returns
		--------
			``None`` : 
		"""
		pass

class IResultFieldInfo(IFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ResultRecordTypeName(self) -> str:
		"""the result record that the field is part of.

		Returns
		--------
			``IResultFieldInfo`` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""The numerical engine that the field belongs to.

		Returns
		--------
			``IResultFieldInfo`` : 
		"""
		pass

class IComponentElementFieldInfo(IFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportElementTypeName(self) -> str:
		"""The name of the support element

		Returns
		--------
			``IComponentElementFieldInfo`` : 
		"""
		pass

class IFieldManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def FieldByName(self, name: str) -> IFieldInfo:
		"""Gets an IFieldInfo given the name.

		Args
		--------
			name (``str``) :  The name of the field to return.

		Returns
		--------
			``IFieldInfo`` : A non-null IFieldInfo implementation if the name is found, otherwise null.
		"""
		pass

	def FieldByLabel(self, label: str) -> IFieldInfo:
		"""Gets an IFieldINfo by label.

		Args
		--------
			label (``str``) :  The label of the field to search for.  Exact match is used.

		Returns
		--------
			``IFieldInfo`` : A non-null IFieldInfo if found, otherwise null
		"""
		pass

	@property
	def FieldInfo(self) -> IReadOnlyCollection[IFieldInfo]:
		"""A list of IFieldInfo objects providing information about individual fields including
            data type, name, etc.

		Returns
		--------
			``IFieldManager`` : 
		"""
		pass

class IUserFieldOptions(Generic[TFieldType, TNetworkElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FieldType(self) -> UserFieldDataType:
		"""The created field will use this type of data.

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""The name of the field.  Must be unique across all element types being used.

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@property
	def Label(self) -> str:
		"""The display label to show in the user interface (if applicable)

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@property
	def ElementType(self) -> TNetworkElementTypeEnum:
		"""The primary element type this field belongs to.

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@ElementType.setter
	def ElementType(self, elementtype: TNetworkElementTypeEnum) -> None:
		pass

	@property
	def SharedWith(self) -> List[TNetworkElementTypeEnum]:
		"""The list of element types to share this field with.  Should not include ElementType in this list.

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@property
	def DefaultValue(self) -> TFieldType:
		"""The default value for this field.

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@DefaultValue.setter
	def DefaultValue(self, defaultvalue: TFieldType) -> None:
		pass

	@property
	def Category(self) -> str:
		"""The category the field is placed in the property grid or quick attribute selection.

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@Category.setter
	def Category(self, category: str) -> None:
		pass

	@property
	def JustLikeField(self) -> IFieldInfo:
		"""The field to use for getting the storage unit for a unitized real field.  Ignored if FieldType is not Real.

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	@JustLikeField.setter
	def JustLikeField(self, justlikefield: IFieldInfo) -> None:
		pass

class IUserFieldManager(Generic[TNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def NewFieldOptions(self) -> IUserFieldOptions:
		"""No Description

		Returns
		--------
			``IUserFieldOptions`` : 
		"""
		pass

	def CreateField(self, options: IUserFieldOptions[TFieldType,TNetworkElementType]) -> IUserNetworkfieldInfo:
		"""No Description

		Args
		--------
			options (``IUserFieldOptions``) :  options

		Returns
		--------
			``IUserNetworkfieldInfo`` : 
		"""
		pass

