from typing import overload, List, Iterator
from array import array
from enum import Enum

class Assembly(_Assembly, IEvidenceFactory, ICustomAttributeProvider, ISerializable):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	@overload
	def LoadFrom(assemblyFile: str) -> Assembly:
		"""No Description

		Args:
			assemblyFile(str): assemblyFile

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def LoadFrom(assemblyFile: str, securityEvidence: Evidence) -> Assembly:
		"""No Description

		Args:
			assemblyFile(str): assemblyFile
			securityEvidence(Evidence): securityEvidence

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def LoadFrom(assemblyFile: str, securityEvidence: Evidence, hashValue: array(int), hashAlgorithm: AssemblyHashAlgorithm) -> Assembly:
		"""No Description

		Args:
			assemblyFile(str): assemblyFile
			securityEvidence(Evidence): securityEvidence
			hashValue(array(int)): hashValue
			hashAlgorithm(AssemblyHashAlgorithm): hashAlgorithm

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def LoadFrom(assemblyFile: str, hashValue: array(int), hashAlgorithm: AssemblyHashAlgorithm) -> Assembly:
		"""No Description

		Args:
			assemblyFile(str): assemblyFile
			hashValue(array(int)): hashValue
			hashAlgorithm(AssemblyHashAlgorithm): hashAlgorithm

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(assemblyString: str) -> Assembly:
		"""No Description

		Args:
			assemblyString(str): assemblyString

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def ReflectionOnlyLoad(assemblyString: str) -> Assembly:
		"""No Description

		Args:
			assemblyString(str): assemblyString

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(assemblyString: str, assemblySecurity: Evidence) -> Assembly:
		"""No Description

		Args:
			assemblyString(str): assemblyString
			assemblySecurity(Evidence): assemblySecurity

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(assemblyRef: AssemblyName) -> Assembly:
		"""No Description

		Args:
			assemblyRef(AssemblyName): assemblyRef

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
		"""No Description

		Args:
			assemblyRef(AssemblyName): assemblyRef
			assemblySecurity(Evidence): assemblySecurity

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def LoadWithPartialName(partialName: str) -> Assembly:
		"""No Description

		Args:
			partialName(str): partialName

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def LoadWithPartialName(partialName: str, securityEvidence: Evidence) -> Assembly:
		"""No Description

		Args:
			partialName(str): partialName
			securityEvidence(Evidence): securityEvidence

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(rawAssembly: array(int)) -> Assembly:
		"""No Description

		Args:
			rawAssembly(array(int)): rawAssembly

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def ReflectionOnlyLoad(rawAssembly: array(int)) -> Assembly:
		"""No Description

		Args:
			rawAssembly(array(int)): rawAssembly

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(rawAssembly: array(int), rawSymbolStore: array(int)) -> Assembly:
		"""No Description

		Args:
			rawAssembly(array(int)): rawAssembly
			rawSymbolStore(array(int)): rawSymbolStore

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(rawAssembly: array(int), rawSymbolStore: array(int), securityContextSource: SecurityContextSource) -> Assembly:
		"""No Description

		Args:
			rawAssembly(array(int)): rawAssembly
			rawSymbolStore(array(int)): rawSymbolStore
			securityContextSource(SecurityContextSource): securityContextSource

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def Load(rawAssembly: array(int), rawSymbolStore: array(int), securityEvidence: Evidence) -> Assembly:
		"""No Description

		Args:
			rawAssembly(array(int)): rawAssembly
			rawSymbolStore(array(int)): rawSymbolStore
			securityEvidence(Evidence): securityEvidence

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def LoadFile(path: str) -> Assembly:
		"""No Description

		Args:
			path(str): path

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	@overload
	def LoadFile(path: str, securityEvidence: Evidence) -> Assembly:
		"""No Description

		Args:
			path(str): path
			securityEvidence(Evidence): securityEvidence

		Returns:
			Assembly: 
		"""
		pass

	@overload
	def GetName(self) -> AssemblyName:
		"""No Description

		Returns:
			AssemblyName: 
		"""
		pass

	@overload
	def GetName(self, copiedName: bool) -> AssemblyName:
		"""No Description

		Args:
			copiedName(bool): copiedName

		Returns:
			AssemblyName: 
		"""
		pass

	@overload
	def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
		"""No Description

		Args:
			type(Type): type
			name(str): name

		Returns:
			Stream: 
		"""
		pass

	@overload
	def GetManifestResourceStream(self, name: str) -> Stream:
		"""No Description

		Args:
			name(str): name

		Returns:
			Stream: 
		"""
		pass

	@overload
	def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
		"""No Description

		Args:
			culture(CultureInfo): culture

		Returns:
			Assembly: 
		"""
		pass

	@overload
	def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
		"""No Description

		Args:
			culture(CultureInfo): culture
			version(Version): version

		Returns:
			Assembly: 
		"""
		pass

	@overload
	def GetCustomAttributes(self, inherit: bool) -> array(object):
		"""No Description

		Args:
			inherit(bool): inherit

		Returns:
			array(object): 
		"""
		pass

	@overload
	def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> array(object):
		"""No Description

		Args:
			attributeType(Type): attributeType
			inherit(bool): inherit

		Returns:
			array(object): 
		"""
		pass

	@overload
	def LoadModule(self, moduleName: str, rawModule: array(int)) -> Module:
		"""No Description

		Args:
			moduleName(str): moduleName
			rawModule(array(int)): rawModule

		Returns:
			Module: 
		"""
		pass

	@overload
	def LoadModule(self, moduleName: str, rawModule: array(int), rawSymbolStore: array(int)) -> Module:
		"""No Description

		Args:
			moduleName(str): moduleName
			rawModule(array(int)): rawModule
			rawSymbolStore(array(int)): rawSymbolStore

		Returns:
			Module: 
		"""
		pass

	@overload
	def CreateInstance(self, typeName: str) -> object:
		"""No Description

		Args:
			typeName(str): typeName

		Returns:
			object: 
		"""
		pass

	@overload
	def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
		"""No Description

		Args:
			typeName(str): typeName
			ignoreCase(bool): ignoreCase

		Returns:
			object: 
		"""
		pass

	@overload
	def CreateInstance(self, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: array(object), culture: CultureInfo, activationAttributes: array(object)) -> object:
		"""No Description

		Args:
			typeName(str): typeName
			ignoreCase(bool): ignoreCase
			bindingAttr(BindingFlags): bindingAttr
			binder(Binder): binder
			args(array(object)): args
			culture(CultureInfo): culture
			activationAttributes(array(object)): activationAttributes

		Returns:
			object: 
		"""
		pass

	@overload
	def GetLoadedModules(self) -> array(Module):
		"""No Description

		Returns:
			array(Module): 
		"""
		pass

	@overload
	def GetLoadedModules(self, getResourceModules: bool) -> array(Module):
		"""No Description

		Args:
			getResourceModules(bool): getResourceModules

		Returns:
			array(Module): 
		"""
		pass

	@overload
	def GetModules(self) -> array(Module):
		"""No Description

		Returns:
			array(Module): 
		"""
		pass

	@overload
	def GetModules(self, getResourceModules: bool) -> array(Module):
		"""No Description

		Args:
			getResourceModules(bool): getResourceModules

		Returns:
			array(Module): 
		"""
		pass

	@overload
	def GetFiles(self) -> array(FileStream):
		"""No Description

		Returns:
			array(FileStream): 
		"""
		pass

	@overload
	def GetFiles(self, getResourceModules: bool) -> array(FileStream):
		"""No Description

		Args:
			getResourceModules(bool): getResourceModules

		Returns:
			array(FileStream): 
		"""
		pass

	@staticmethod
	def GetAssembly(type: Type) -> Assembly:
		"""No Description

		Args:
			type(Type): type

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	def op_Equality(left: Assembly, right: Assembly) -> bool:
		"""No Description

		Args:
			left(Assembly): left
			right(Assembly): right

		Returns:
			bool: 
		"""
		pass

	@staticmethod
	def op_Inequality(left: Assembly, right: Assembly) -> bool:
		"""No Description

		Args:
			left(Assembly): left
			right(Assembly): right

		Returns:
			bool: 
		"""
		pass

	@staticmethod
	def ReflectionOnlyLoadFrom(assemblyFile: str) -> Assembly:
		"""No Description

		Args:
			assemblyFile(str): assemblyFile

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	def UnsafeLoadFrom(assemblyFile: str) -> Assembly:
		"""No Description

		Args:
			assemblyFile(str): assemblyFile

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	def GetExecutingAssembly() -> Assembly:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	def GetCallingAssembly() -> Assembly:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@staticmethod
	def GetEntryAssembly() -> Assembly:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	def add_ModuleResolve(self, value: ModuleResolveEventHandler) -> None:
		"""No Description

		Args:
			value(ModuleResolveEventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_ModuleResolve(self, value: ModuleResolveEventHandler) -> None:
		"""No Description

		Args:
			value(ModuleResolveEventHandler): value

		Returns:
			None: 
		"""
		pass

	def GetExportedTypes(self) -> array(Type):
		"""No Description

		Returns:
			array(Type): 
		"""
		pass

	def GetTypes(self) -> array(Type):
		"""No Description

		Returns:
			array(Type): 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args:
			info(SerializationInfo): info
			context(StreamingContext): context

		Returns:
			None: 
		"""
		pass

	def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
		"""No Description

		Args:
			attributeType(Type): attributeType
			inherit(bool): inherit

		Returns:
			bool: 
		"""
		pass

	def GetCustomAttributesData(self) -> List[CustomAttributeData]:
		"""No Description

		Returns:
			List[CustomAttributeData]: 
		"""
		pass

	def GetModule(self, name: str) -> Module:
		"""No Description

		Args:
			name(str): name

		Returns:
			Module: 
		"""
		pass

	def GetFile(self, name: str) -> FileStream:
		"""No Description

		Args:
			name(str): name

		Returns:
			FileStream: 
		"""
		pass

	def GetManifestResourceNames(self) -> array(str):
		"""No Description

		Returns:
			array(str): 
		"""
		pass

	def GetReferencedAssemblies(self) -> array(AssemblyName):
		"""No Description

		Returns:
			array(AssemblyName): 
		"""
		pass

	def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
		"""No Description

		Args:
			resourceName(str): resourceName

		Returns:
			ManifestResourceInfo: 
		"""
		pass

	@staticmethod
	def CreateQualifiedName(assemblyName: str, typeName: str) -> str:
		"""No Description

		Args:
			assemblyName(str): assemblyName
			typeName(str): typeName

		Returns:
			str: 
		"""
		pass

	@property
	def CodeBase(self) -> str:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def EscapedCodeBase(self) -> str:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def FullName(self) -> str:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def EntryPoint(self) -> MethodInfo:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def ExportedTypes(self) -> Iterator[Type]:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def DefinedTypes(self) -> Iterator[TypeInfo]:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def Evidence(self) -> Evidence:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def PermissionSet(self) -> PermissionSet:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def IsFullyTrusted(self) -> bool:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def SecurityRuleSet(self) -> SecurityRuleSet:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def ManifestModule(self) -> Module:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def CustomAttributes(self) -> Iterator[CustomAttributeData]:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def ReflectionOnly(self) -> bool:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def Modules(self) -> Iterator[Module]:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def Location(self) -> str:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def ImageRuntimeVersion(self) -> str:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def GlobalAssemblyCache(self) -> bool:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def HostContext(self) -> int:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

	@property
	def IsDynamic(self) -> bool:
		"""No Description

		Returns:
			Assembly: 
		"""
		pass

class LoadContext(Enum):
	DEFAULT = 0
	LOADFROM = 1
	UNKNOWN = 2
	HOSTED = 3

class AssemblyNameFlags(Enum):
	None = 0
	PublicKey = 1
	Retargetable = 256
	EnableJITcompileOptimizer = 16384
	EnableJITcompileTracking = 32768

class AssemblyContentType(Enum):
	Default = 0
	WindowsRuntime = 1

class ProcessorArchitecture(Enum):
	None = 0
	MSIL = 1
	X86 = 2
	IA64 = 3
	Amd64 = 4
	Arm = 5

class BindingFlags(Enum):
	Default = 0
	IgnoreCase = 1
	DeclaredOnly = 2
	Instance = 4
	Static = 8
	Public = 16
	NonPublic = 32
	FlattenHierarchy = 64
	InvokeMethod = 256
	CreateInstance = 512
	GetField = 1024
	SetField = 2048
	GetProperty = 4096
	SetProperty = 8192
	PutDispProperty = 16384
	PutRefDispProperty = 32768
	ExactBinding = 65536
	SuppressChangeType = 131072
	OptionalParamBinding = 262144
	IgnoreReturn = 16777216

class CallingConventions(Enum):
	Standard = 1
	VarArgs = 2
	Any = 3
	HasThis = 32
	ExplicitThis = 64

class CustomAttributeEncoding(Enum):
	Undefined = 0
	Boolean = 2
	Char = 3
	SByte = 4
	Byte = 5
	Int16 = 6
	UInt16 = 7
	Int32 = 8
	UInt32 = 9
	Int64 = 10
	UInt64 = 11
	Float = 12
	Double = 13
	String = 14
	Array = 29
	Type = 80
	Object = 81
	Field = 83
	Property = 84
	Enum = 85

class EventAttributes(Enum):
	None = 0
	SpecialName = 512
	ReservedMask = 1024
	RTSpecialName = 1024

class FieldAttributes(Enum):
	PrivateScope = 0
	Private = 1
	FamANDAssem = 2
	Assembly = 3
	Family = 4
	FamORAssem = 5
	Public = 6
	FieldAccessMask = 7
	Static = 16
	InitOnly = 32
	Literal = 64
	NotSerialized = 128
	HasFieldRVA = 256
	SpecialName = 512
	RTSpecialName = 1024
	HasFieldMarshal = 4096
	PinvokeImpl = 8192
	HasDefault = 32768
	ReservedMask = 38144

class GenericParameterAttributes(Enum):
	None = 0
	Covariant = 1
	Contravariant = 2
	VarianceMask = 3
	ReferenceTypeConstraint = 4
	NotNullableValueTypeConstraint = 8
	DefaultConstructorConstraint = 16
	SpecialConstraintMask = 28

class ResourceLocation(Enum):
	Embedded = 1
	ContainedInAnotherAssembly = 2
	ContainedInManifestFile = 4

class CorElementType(Enum):
	End = 0
	Void = 1
	Boolean = 2
	Char = 3
	I1 = 4
	U1 = 5
	I2 = 6
	U2 = 7
	I4 = 8
	U4 = 9
	I8 = 10
	U8 = 11
	R4 = 12
	R8 = 13
	String = 14
	Ptr = 15
	ByRef = 16
	ValueType = 17
	Class = 18
	Var = 19
	Array = 20
	GenericInst = 21
	TypedByRef = 22
	I = 24
	U = 25
	FnPtr = 27
	Object = 28
	SzArray = 29
	MVar = 30
	CModReqd = 31
	CModOpt = 32
	Internal = 33
	Max = 34
	Modifier = 64
	Sentinel = 65
	Pinned = 69

class MdSigCallingConvention(Enum):
	Default = 0
	C = 1
	StdCall = 2
	ThisCall = 3
	FastCall = 4
	Vararg = 5
	Field = 6
	LocalSig = 7
	Property = 8
	Unmgd = 9
	GenericInst = 10
	CallConvMask = 15
	Generic = 16
	HasThis = 32
	ExplicitThis = 64

class PInvokeAttributes(Enum):
	ThrowOnUnmappableCharUseAssem = 0
	CharSetNotSpec = 0
	BestFitUseAssem = 0
	NoMangle = 1
	CharSetAnsi = 2
	CharSetUnicode = 4
	CharSetAuto = 6
	CharSetMask = 6
	BestFitEnabled = 16
	BestFitDisabled = 32
	BestFitMask = 48
	SupportsLastError = 64
	CallConvWinapi = 256
	CallConvCdecl = 512
	CallConvStdcall = 768
	CallConvThiscall = 1024
	CallConvFastcall = 1280
	CallConvMask = 1792
	ThrowOnUnmappableCharEnabled = 4096
	ThrowOnUnmappableCharDisabled = 8192
	ThrowOnUnmappableCharMask = 12288
	MaxValue = 65535

class MethodSemanticsAttributes(Enum):
	Setter = 1
	Getter = 2
	Other = 4
	AddOn = 8
	RemoveOn = 16
	Fire = 32

class MetadataTokenType(Enum):
	Module = 0
	TypeRef = 16777216
	TypeDef = 33554432
	FieldDef = 67108864
	MethodDef = 100663296
	ParamDef = 134217728
	InterfaceImpl = 150994944
	MemberRef = 167772160
	CustomAttribute = 201326592
	Permission = 234881024
	Signature = 285212672
	Event = 335544320
	Property = 385875968
	ModuleRef = 436207616
	TypeSpec = 452984832
	Assembly = 536870912
	AssemblyRef = 587202560
	File = 637534208
	ExportedType = 654311424
	ManifestResource = 671088640
	GenericPar = 704643072
	MethodSpec = 721420288
	String = 1879048192
	Name = 1895825408
	BaseType = 1912602624
	Invalid = 2147483647

class MemberTypes(Enum):
	Constructor = 1
	Event = 2
	Field = 4
	Method = 8
	Property = 16
	TypeInfo = 32
	Custom = 64
	NestedType = 128
	All = 191

class MethodAttributes(Enum):
	ReuseSlot = 0
	PrivateScope = 0
	Private = 1
	FamANDAssem = 2
	Assembly = 3
	Family = 4
	FamORAssem = 5
	Public = 6
	MemberAccessMask = 7
	UnmanagedExport = 8
	Static = 16
	Final = 32
	Virtual = 64
	HideBySig = 128
	NewSlot = 256
	VtableLayoutMask = 256
	CheckAccessOnOverride = 512
	Abstract = 1024
	SpecialName = 2048
	RTSpecialName = 4096
	PinvokeImpl = 8192
	HasSecurity = 16384
	RequireSecObject = 32768
	ReservedMask = 53248

class INVOCATION_FLAGS(Enum):
	INVOCATION_FLAGS_UNKNOWN = 0
	INVOCATION_FLAGS_INITIALIZED = 1
	INVOCATION_FLAGS_NO_INVOKE = 2
	INVOCATION_FLAGS_NEED_SECURITY = 4
	INVOCATION_FLAGS_NO_CTOR_INVOKE = 8
	INVOCATION_FLAGS_IS_CTOR = 16
	INVOCATION_FLAGS_SPECIAL_FIELD = 16
	INVOCATION_FLAGS_RISKY_METHOD = 32
	INVOCATION_FLAGS_FIELD_SPECIAL_CAST = 32
	INVOCATION_FLAGS_NON_W8P_FX_API = 64
	INVOCATION_FLAGS_IS_DELEGATE_CTOR = 128
	INVOCATION_FLAGS_CONTAINS_STACK_POINTERS = 256
	INVOCATION_FLAGS_CONSTRUCTOR_INVOKE = 268435456

class MethodImplAttributes(Enum):
	IL = 0
	Managed = 0
	Native = 1
	OPTIL = 2
	Runtime = 3
	CodeTypeMask = 3
	Unmanaged = 4
	ManagedMask = 4
	NoInlining = 8
	ForwardRef = 16
	Synchronized = 32
	NoOptimization = 64
	PreserveSig = 128
	AggressiveInlining = 256
	SecurityMitigations = 1024
	InternalCall = 4096
	MaxMethodImplVal = 65535

class PortableExecutableKinds(Enum):
	NotAPortableExecutableImage = 0
	ILOnly = 1
	Required32Bit = 2
	PE32Plus = 4
	Unmanaged32Bit = 8
	Preferred32Bit = 16

class ImageFileMachine(Enum):
	I386 = 332
	ARM = 452
	IA64 = 512
	AMD64 = 34404

class ExceptionHandlingClauseOptions(Enum):
	Clause = 0
	Filter = 1
	Finally = 2
	Fault = 4

class ParameterAttributes(Enum):
	None = 0
	In = 1
	Out = 2
	Lcid = 4
	Retval = 8
	Optional = 16
	HasDefault = 4096
	HasFieldMarshal = 8192
	Reserved3 = 16384
	Reserved4 = 32768
	ReservedMask = 61440

class PropertyAttributes(Enum):
	None = 0
	SpecialName = 512
	RTSpecialName = 1024
	HasDefault = 4096
	Reserved2 = 8192
	Reserved3 = 16384
	Reserved4 = 32768
	ReservedMask = 62464

class ResourceAttributes(Enum):
	Public = 1
	Private = 2

class TypeAttributes(Enum):
	NotPublic = 0
	AutoLayout = 0
	AnsiClass = 0
	Class = 0
	Public = 1
	NestedPublic = 2
	NestedPrivate = 3
	NestedFamily = 4
	NestedAssembly = 5
	NestedFamANDAssem = 6
	NestedFamORAssem = 7
	VisibilityMask = 7
	SequentialLayout = 8
	ExplicitLayout = 16
	LayoutMask = 24
	Interface = 32
	ClassSemanticsMask = 32
	Abstract = 128
	Sealed = 256
	SpecialName = 1024
	RTSpecialName = 2048
	Import = 4096
	Serializable = 8192
	WindowsRuntime = 16384
	UnicodeClass = 65536
	AutoClass = 131072
	StringFormatMask = 196608
	CustomFormatClass = 196608
	HasSecurity = 262144
	ReservedMask = 264192
	BeforeFieldInit = 1048576
	CustomFormatMask = 12582912

class ASSEMBLY_FLAGS(Enum):
	ASSEMBLY_FLAGS_UNKNOWN = 0
	ASSEMBLY_FLAGS_TOKEN_MASK = 16777215
	ASSEMBLY_FLAGS_INITIALIZED = 16777216
	ASSEMBLY_FLAGS_FRAMEWORK = 33554432
	ASSEMBLY_FLAGS_SAFE_REFLECTION = 67108864

class Attributes(Enum):
	ComposedOfAllVirtualMethods = 1
	ComposedOfAllPrivateMethods = 2
	ComposedOfNoPublicMembers = 4
	ComposedOfNoStaticMembers = 8

