from enum import Enum
from Haestad.Support.ISupport import IField, FieldDataType, INamable, ILabeled
from Haestad.IDomain import DomainFieldType
from Haestad.Support.IUnits import Unit
from OpenFlows.IUnits import IUnit
from System.Collections.Generic import IReadOnlyCollection
from typing import List, Generic, overload, TypeVar
from OpenFlows.Domain.IModelingElements import TNetworkElementType

TValueType = TypeVar("TValueType")
TNetworkElementTypeEnum = TypeVar("TNetworkElementTypeEnum")
TFieldType = TypeVar("TFieldType")

class UserFieldDataType(Enum):
	Integer = 1
	Real = 2
	LongText = 4
	DateTime = 5
	Boolean = 6

class IFieldInfo(INamable, ILabeled):

	def __new__(self) -> None:
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
			id (`int`) :  id

		Returns
		--------
			`TValueType` : 
		"""
		pass

	def SetValue(self, id: int, value: TValueType) -> None:
		"""No Description

		Args
		--------
			id (`int`) :  id
			value (`TValueType`) :  value

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def Field(self) -> IField:
		"""The field associated with this FieldInfo

		Returns
		--------
			`IField` : 
		"""
		pass

	@property
	def FieldType(self) -> DomainFieldType:
		"""The type of field - domain, support, scenario, etc.

		Returns
		--------
			`DomainFieldType` : 
		"""
		pass

	@property
	def FieldDataType(self) -> FieldDataType:
		"""The value type for this field when retrieved.

		Returns
		--------
			`FieldDataType` : 
		"""
		pass

	@property
	def StorageUnit(self) -> Unit:
		"""If unitized, the storage unit the value is stored in.

		Returns
		--------
			`Unit` : 
		"""
		pass

	@property
	def Unit(self) -> IUnit:
		"""If unitized, the format information for the field.

		Returns
		--------
			`IUnit` : 
		"""
		pass

class INetworkFieldInfo(IFieldInfo):

	def __new__(self) -> None:
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
			`str` : 
		"""
		pass

	@property
	def DomainElementTypeName(self) -> str:
		"""The name of the domain element type that this field is assigned.

		Returns
		--------
			`str` : 
		"""
		pass

class IUserNetworkfieldInfo(INetworkFieldInfo):

	def __new__(self) -> None:
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
			`None` : 
		"""
		pass

class IResultFieldInfo(IFieldInfo):

	def __new__(self) -> None:
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
			`str` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""The numerical engine that the field belongs to.

		Returns
		--------
			`str` : 
		"""
		pass

class IComponentElementFieldInfo(IFieldInfo):

	def __new__(self) -> None:
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
			`str` : 
		"""
		pass

class IFieldManager:

	def __new__(self) -> None:
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
			name (`str`) :  The name of the field to return.

		Returns
		--------
			`IFieldInfo` : A non-null IFieldInfo implementation if the name is found, otherwise null.
		"""
		pass

	def FieldByLabel(self, label: str) -> IFieldInfo:
		"""Gets an IFieldINfo by label.

		Args
		--------
			label (`str`) :  The label of the field to search for.  Exact match is used.

		Returns
		--------
			`IFieldInfo` : A non-null IFieldInfo if found, otherwise null
		"""
		pass

	@property
	def FieldInfo(self) -> IReadOnlyCollection[IFieldInfo]:
		"""A list of IFieldInfo objects providing information about individual fields including
            data type, name, etc.

		Returns
		--------
			`IReadOnlyCollection` : 
		"""
		pass

class IUserFieldOptions(Generic[TFieldType, TNetworkElementTypeEnum]):

	def __new__(self) -> None:
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
			`UserFieldDataType` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""The name of the field.  Must be unique across all element types being used.

		Returns
		--------
			`str` : 
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
			`str` : 
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
			`TNetworkElementTypeEnum` : 
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
			`List[TNetworkElementTypeEnum]` : 
		"""
		pass

	@property
	def DefaultValue(self) -> TFieldType:
		"""The default value for this field.

		Returns
		--------
			`TFieldType` : 
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
			`str` : 
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
			`IFieldInfo` : 
		"""
		pass

	@JustLikeField.setter
	def JustLikeField(self, justlikefield: IFieldInfo) -> None:
		pass

class IUserFieldManager(Generic[TNetworkElementType]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def NewFieldOptions(self) -> IUserFieldOptions[TFieldType,TNetworkElementType]:
		"""No Description

		Returns
		--------
			`IUserFieldOptions` : 
		"""
		pass

	def CreateField(self, options: IUserFieldOptions[TFieldType,TNetworkElementType]) -> IUserNetworkfieldInfo:
		"""No Description

		Args
		--------
			options (`IUserFieldOptions`) :  options

		Returns
		--------
			`IUserNetworkfieldInfo` : 
		"""
		pass

	@overload
	def UserDefinedFields(self) -> ReadOnlyCollection[IUserNetworkfieldInfo]:
		"""Returns all user defined fields across all element types.

		Returns
		--------
			`ReadOnlyCollection` : A read-only list containing all user defined fields across all element types
		"""
		pass

	@overload
	def UserDefinedFields(self, elementType: TNetworkElementType) -> ReadOnlyCollection[IUserNetworkfieldInfo]:
		"""Returns all user defined fields across all element types.

		Args
		--------
			elementType (`TNetworkElementType`) :  elementType

		Returns
		--------
			`ReadOnlyCollection` : A read-only list containing all user defined fields across all element types
		"""
		pass

