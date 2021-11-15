from enum import Enum

class ExceptionArgument(Enum):
	obj = 0
	dictionary = 1
	dictionaryCreationThreshold = 2
	array = 3
	info = 4
	key = 5
	collection = 6
	list = 7
	match = 8
	converter = 9
	queue = 10
	stack = 11
	capacity = 12
	index = 13
	startIndex = 14
	value = 15
	count = 16
	arrayIndex = 17
	name = 18
	mode = 19
	item = 20
	options = 21
	view = 22
	sourceBytesToCopy = 23

class ExceptionResource(Enum):
	Argument_ImplementIComparable = 0
	Argument_InvalidType = 1
	Argument_InvalidArgumentForComparison = 2
	Argument_InvalidRegistryKeyPermissionCheck = 3
	ArgumentOutOfRange_NeedNonNegNum = 4
	Arg_ArrayPlusOffTooSmall = 5
	Arg_NonZeroLowerBound = 6
	Arg_RankMultiDimNotSupported = 7
	Arg_RegKeyDelHive = 8
	Arg_RegKeyStrLenBug = 9
	Arg_RegSetStrArrNull = 10
	Arg_RegSetMismatchedKind = 11
	Arg_RegSubKeyAbsent = 12
	Arg_RegSubKeyValueAbsent = 13
	Argument_AddingDuplicate = 14
	Serialization_InvalidOnDeser = 15
	Serialization_MissingKeys = 16
	Serialization_NullKey = 17
	Argument_InvalidArrayType = 18
	NotSupported_KeyCollectionSet = 19
	NotSupported_ValueCollectionSet = 20
	ArgumentOutOfRange_SmallCapacity = 21
	ArgumentOutOfRange_Index = 22
	Argument_InvalidOffLen = 23
	Argument_ItemNotExist = 24
	ArgumentOutOfRange_Count = 25
	ArgumentOutOfRange_InvalidThreshold = 26
	ArgumentOutOfRange_ListInsert = 27
	NotSupported_ReadOnlyCollection = 28
	InvalidOperation_CannotRemoveFromStackOrQueue = 29
	InvalidOperation_EmptyQueue = 30
	InvalidOperation_EnumOpCantHappen = 31
	InvalidOperation_EnumFailedVersion = 32
	InvalidOperation_EmptyStack = 33
	ArgumentOutOfRange_BiggerThanCollection = 34
	InvalidOperation_EnumNotStarted = 35
	InvalidOperation_EnumEnded = 36
	NotSupported_SortedListNestedWrite = 37
	InvalidOperation_NoValue = 38
	InvalidOperation_RegRemoveSubKey = 39
	Security_RegistryPermission = 40
	UnauthorizedAccess_RegistryNoWrite = 41
	ObjectDisposed_RegKeyClosed = 42
	NotSupported_InComparableType = 43
	Argument_InvalidRegistryOptionsCheck = 44
	Argument_InvalidRegistryViewCheck = 45

class StringSplitOptions(Enum):
	None = 0
	RemoveEmptyEntries = 1

class StringComparison(Enum):
	CurrentCulture = 0
	CurrentCultureIgnoreCase = 1
	InvariantCulture = 2
	InvariantCultureIgnoreCase = 3
	Ordinal = 4
	OrdinalIgnoreCase = 5

class DateTimeKind(Enum):
	Unspecified = 0
	Utc = 1
	Local = 2

class DelegateBindingFlags(Enum):
	StaticMethodOnly = 1
	InstanceMethodOnly = 2
	OpenDelegateOnly = 4
	ClosedDelegateOnly = 8
	NeverCloseOverNull = 16
	CaselessMatching = 32
	SkipSecurityChecks = 64
	RelaxedSignature = 128

class LogLevel(Enum):
	Trace = 0
	Status = 20
	Warning = 40
	Error = 50
	Panic = 100

class AppDomainManagerInitializationOptions(Enum):
	None = 0
	RegisterWithHost = 1

class LoaderOptimization(Enum):
	NotSpecified = 0
	SingleDomain = 1
	MultiDomain = 2
	MultiDomainHost = 3
	DomainMask = 3
	DisallowBindings = 4

class AttributeTargets(Enum):
	Assembly = 1
	Module = 2
	Class = 4
	Struct = 8
	Enum = 16
	Constructor = 32
	Method = 64
	Property = 128
	Field = 256
	Event = 512
	Interface = 1024
	Parameter = 2048
	Delegate = 4096
	ReturnValue = 8192
	GenericParameter = 16384
	All = 32767

class ConfigEvents(Enum):
	StartDocument = 0
	StartDTD = 1
	EndDTD = 2
	StartDTDSubset = 3
	EndDTDSubset = 4
	EndProlog = 5
	StartEntity = 6
	EndEntity = 7
	EndDocument = 8
	DataAvailable = 9
	LastEvent = 9

class ConfigNodeType(Enum):
	Element = 1
	Attribute = 2
	Pi = 3
	XmlDecl = 4
	DocType = 5
	DTDAttribute = 6
	EntityDecl = 7
	ElementDecl = 8
	AttlistDecl = 9
	Notation = 10
	Group = 11
	IncludeSect = 12
	PCData = 13
	CData = 14
	IgnoreSect = 15
	Comment = 16
	EntityRef = 17
	Whitespace = 18
	Name = 19
	NMToken = 20
	String = 21
	Peref = 22
	Model = 23
	ATTDef = 24
	ATTType = 25
	ATTPresence = 26
	DTDSubset = 27
	LastNodeType = 28

class ConfigNodeSubType(Enum):
	Version = 28
	Encoding = 29
	Standalone = 30
	NS = 31
	XMLSpace = 32
	XMLLang = 33
	System = 34
	Public = 35
	NData = 36
	AtCData = 37
	AtId = 38
	AtIdref = 39
	AtIdrefs = 40
	AtEntity = 41
	AtEntities = 42
	AtNmToken = 43
	AtNmTokens = 44
	AtNotation = 45
	AtRequired = 46
	AtImplied = 47
	AtFixed = 48
	PentityDecl = 49
	Empty = 50
	Any = 51
	Mixed = 52
	Sequence = 53
	Choice = 54
	Star = 55
	Plus = 56
	Questionmark = 57
	LastSubNodeType = 58

class ConsoleColor(Enum):
	Black = 0
	DarkBlue = 1
	DarkGreen = 2
	DarkCyan = 3
	DarkRed = 4
	DarkMagenta = 5
	DarkYellow = 6
	Gray = 7
	DarkGray = 8
	Blue = 9
	Green = 10
	Cyan = 11
	Red = 12
	Magenta = 13
	Yellow = 14
	White = 15

class ConsoleKey(Enum):
	Backspace = 8
	Tab = 9
	Clear = 12
	Enter = 13
	Pause = 19
	Escape = 27
	Spacebar = 32
	PageUp = 33
	PageDown = 34
	End = 35
	Home = 36
	LeftArrow = 37
	UpArrow = 38
	RightArrow = 39
	DownArrow = 40
	Select = 41
	Print = 42
	Execute = 43
	PrintScreen = 44
	Insert = 45
	Delete = 46
	Help = 47
	D0 = 48
	D1 = 49
	D2 = 50
	D3 = 51
	D4 = 52
	D5 = 53
	D6 = 54
	D7 = 55
	D8 = 56
	D9 = 57
	A = 65
	B = 66
	C = 67
	D = 68
	E = 69
	F = 70
	G = 71
	H = 72
	I = 73
	J = 74
	K = 75
	L = 76
	M = 77
	N = 78
	O = 79
	P = 80
	Q = 81
	R = 82
	S = 83
	T = 84
	U = 85
	V = 86
	W = 87
	X = 88
	Y = 89
	Z = 90
	LeftWindows = 91
	RightWindows = 92
	Applications = 93
	Sleep = 95
	NumPad0 = 96
	NumPad1 = 97
	NumPad2 = 98
	NumPad3 = 99
	NumPad4 = 100
	NumPad5 = 101
	NumPad6 = 102
	NumPad7 = 103
	NumPad8 = 104
	NumPad9 = 105
	Multiply = 106
	Add = 107
	Separator = 108
	Subtract = 109
	Decimal = 110
	Divide = 111
	F1 = 112
	F2 = 113
	F3 = 114
	F4 = 115
	F5 = 116
	F6 = 117
	F7 = 118
	F8 = 119
	F9 = 120
	F10 = 121
	F11 = 122
	F12 = 123
	F13 = 124
	F14 = 125
	F15 = 126
	F16 = 127
	F17 = 128
	F18 = 129
	F19 = 130
	F20 = 131
	F21 = 132
	F22 = 133
	F23 = 134
	F24 = 135
	BrowserBack = 166
	BrowserForward = 167
	BrowserRefresh = 168
	BrowserStop = 169
	BrowserSearch = 170
	BrowserFavorites = 171
	BrowserHome = 172
	VolumeMute = 173
	VolumeDown = 174
	VolumeUp = 175
	MediaNext = 176
	MediaPrevious = 177
	MediaStop = 178
	MediaPlay = 179
	LaunchMail = 180
	LaunchMediaSelect = 181
	LaunchApp1 = 182
	LaunchApp2 = 183
	Oem1 = 186
	OemPlus = 187
	OemComma = 188
	OemMinus = 189
	OemPeriod = 190
	Oem2 = 191
	Oem3 = 192
	Oem4 = 219
	Oem5 = 220
	Oem6 = 221
	Oem7 = 222
	Oem8 = 223
	Oem102 = 226
	Process = 229
	Packet = 231
	Attention = 246
	CrSel = 247
	ExSel = 248
	EraseEndOfFile = 249
	Play = 250
	Zoom = 251
	NoName = 252
	Pa1 = 253
	OemClear = 254

class ConsoleModifiers(Enum):
	Alt = 1
	Shift = 2
	Control = 4

class ConsoleSpecialKey(Enum):
	ControlC = 0
	ControlBreak = 1

class Base64FormattingOptions(Enum):
	None = 0
	InsertLineBreaks = 1

class DayOfWeek(Enum):
	Sunday = 0
	Monday = 1
	Tuesday = 2
	Wednesday = 3
	Thursday = 4
	Friday = 5
	Saturday = 6

class EnvironmentVariableTarget(Enum):
	Process = 0
	User = 1
	Machine = 2

class GCCollectionMode(Enum):
	Default = 0
	Forced = 1
	Optimized = 2

class InternalGCCollectionMode(Enum):
	NonBlocking = 1
	Blocking = 2
	Optimized = 4
	Compacting = 8

class GCNotificationStatus(Enum):
	Succeeded = 0
	Failed = 1
	Canceled = 2
	Timeout = 3
	NotApplicable = 4

class MidpointRounding(Enum):
	ToEven = 0
	AwayFromZero = 1

class PlatformID(Enum):
	Win32S = 0
	Win32Windows = 1
	Win32NT = 2
	WinCE = 3
	Unix = 4
	Xbox = 5
	MacOSX = 6

class TypeNameFormatFlags(Enum):
	FormatBasic = 0
	FormatNamespace = 1
	FormatFullInst = 2
	FormatAssembly = 4
	FormatSignature = 8
	FormatNoVersion = 16
	FormatAngleBrackets = 64
	FormatStubInfo = 128
	FormatGenericParam = 256
	FormatSerialization = 259

class TypeNameKind(Enum):
	Name = 0
	ToString = 1
	SerializationName = 2
	FullName = 3

class TimeZoneInfoOptions(Enum):
	None = 1
	NoThrowOnInvalidTime = 2

class TypeCode(Enum):
	Empty = 0
	Object = 1
	DBNull = 2
	Boolean = 3
	Char = 4
	SByte = 5
	Byte = 6
	Int16 = 7
	UInt16 = 8
	Int32 = 9
	UInt32 = 10
	Int64 = 11
	UInt64 = 12
	Single = 13
	Double = 14
	Decimal = 15
	DateTime = 16
	String = 18

class DTSubStringType(Enum):
	Unknown = 0
	Invalid = 1
	Number = 2
	End = 3
	Other = 4

class ParseFailureKind(Enum):
	None = 0
	ArgumentNull = 1
	Format = 2
	FormatWithParameter = 3
	FormatBadDateTimeCalendar = 4

class ParseFlags(Enum):
	HaveYear = 1
	HaveMonth = 2
	HaveDay = 4
	HaveHour = 8
	HaveMinute = 16
	HaveSecond = 32
	HaveTime = 64
	HaveDate = 128
	TimeZoneUsed = 256
	TimeZoneUtc = 512
	ParsedMonthName = 1024
	CaptureOffset = 2048
	YearDefault = 4096
	Rfc1123Pattern = 8192
	UtcSortPattern = 16384

class TokenType(Enum):
	NumberToken = 1
	YearNumberToken = 2
	Am = 3
	Pm = 4
	MonthToken = 5
	EndOfString = 6
	DayOfWeekToken = 7
	TimeZoneToken = 8
	EraToken = 9
	DateWordToken = 10
	UnknownToken = 11
	HebrewNumber = 12
	JapaneseEraToken = 13
	TEraToken = 14
	IgnorableSymbol = 15
	RegularTokenMask = 255
	SEP_Unk = 256
	SEP_End = 512
	SEP_Space = 768
	SEP_Am = 1024
	SEP_Pm = 1280
	SEP_Date = 1536
	SEP_Time = 1792
	SEP_YearSuff = 2048
	SEP_MonthSuff = 2304
	SEP_DaySuff = 2560
	SEP_HourSuff = 2816
	SEP_MinuteSuff = 3072
	SEP_SecondSuff = 3328
	SEP_LocalTimeMark = 3584
	SEP_DateOrOffset = 3840
	SeparatorTokenMask = 65280

class CompatibilityFlag(Enum):
	SwallowUnhandledExceptions = 0
	NullReferenceExceptionOnAV = 1
	EagerlyGenerateRandomAsymmKeys = 2
	FullTrustListAssembliesInGac = 3
	DateTimeParseIgnorePunctuation = 4
	OnlyGACDomainNeutral = 5
	DisableReplacementCustomCulture = 6

class SwitchValueState(Enum):
	HasFalseValue = 1
	HasTrueValue = 2
	HasLookedForOverride = 4
	UnknownValue = 8

class ExceptionMessageKind(Enum):
	ThreadAbort = 1
	ThreadInterrupted = 2
	OutOfMemory = 3

class APPX_FLAGS(Enum):
	APPX_FLAGS_INITIALIZED = 1
	APPX_FLAGS_APPX_MODEL = 2
	APPX_FLAGS_APPX_DESIGN_MODE = 4
	APPX_FLAGS_APPX_NGEN = 8
	APPX_FLAGS_APPX_MASK = 14
	APPX_FLAGS_API_CHECK = 16

class LoaderInformation(Enum):
	ApplicationBaseValue = 0
	ConfigurationFileValue = 1
	DynamicBaseValue = 2
	DevPathValue = 3
	ApplicationNameValue = 4
	PrivateBinPathValue = 5
	PrivateBinPathProbeValue = 6
	ShadowCopyDirectoriesValue = 7
	ShadowCopyFilesValue = 8
	CachePathValue = 9
	LicenseFileValue = 10
	DisallowPublisherPolicyValue = 11
	DisallowCodeDownloadValue = 12
	DisallowBindingRedirectsValue = 13
	DisallowAppBaseProbingValue = 14
	ConfigurationBytesValue = 15
	LoaderMaximum = 18

class ContextForm(Enum):
	Loose = 0
	StoreBounded = 1

class ApplicationState(Enum):
	Undefined = 0
	Starting = 1
	Running = 2

class ApplicationStateDisposition(Enum):
	Undefined = 0
	Starting = 1
	Running = 2
	StartingMigrated = 65537
	RunningFirstTime = 131074

class ControlKeyState(Enum):
	RightAltPressed = 1
	LeftAltPressed = 2
	RightCtrlPressed = 4
	LeftCtrlPressed = 8
	ShiftPressed = 16
	NumLockOn = 32
	ScrollLockOn = 64
	CapsLockOn = 128
	EnhancedKey = 256

class ParseFailureKind(Enum):
	None = 0
	Argument = 1
	ArgumentNull = 2
	ArgumentWithParameter = 3
	UnhandledException = 4

class SpecialFolderOption(Enum):
	None = 0
	DoNotVerify = 16384
	Create = 32768

class SpecialFolder(Enum):
	Desktop = 0
	Programs = 2
	MyDocuments = 5
	Personal = 5
	Favorites = 6
	Startup = 7
	Recent = 8
	SendTo = 9
	StartMenu = 11
	MyMusic = 13
	MyVideos = 14
	DesktopDirectory = 16
	MyComputer = 17
	NetworkShortcuts = 19
	Fonts = 20
	Templates = 21
	CommonStartMenu = 22
	CommonPrograms = 23
	CommonStartup = 24
	CommonDesktopDirectory = 25
	ApplicationData = 26
	PrinterShortcuts = 27
	LocalApplicationData = 28
	InternetCache = 32
	Cookies = 33
	History = 34
	CommonApplicationData = 35
	Windows = 36
	System = 37
	ProgramFiles = 38
	MyPictures = 39
	UserProfile = 40
	SystemX86 = 41
	ProgramFilesX86 = 42
	CommonProgramFiles = 43
	CommonProgramFilesX86 = 44
	CommonTemplates = 45
	CommonDocuments = 46
	CommonAdminTools = 47
	AdminTools = 48
	CommonMusic = 53
	CommonPictures = 54
	CommonVideos = 55
	Resources = 56
	LocalizedResources = 57
	CommonOemLinks = 58
	CDBurning = 59

class StartNoGCRegionStatus(Enum):
	Succeeded = 0
	NotEnoughMemory = 1
	AmountTooLarge = 2
	AlreadyInProgress = 3

class EndNoGCRegionStatus(Enum):
	Succeeded = 0
	NotInProgress = 1
	GCInduced = 2
	AllocationExceeded = 3

class GuidStyles(Enum):
	NumberFormat = 0
	None = 0
	AllowParenthesis = 1
	AllowBraces = 2
	AllowDashes = 4
	AllowHexPrefix = 8
	Any = 15
	RequireParenthesis = 16
	RequireBraces = 32
	RequireDashes = 64
	DigitFormat = 64
	ParenthesisFormat = 80
	BraceFormat = 96
	RequireHexPrefix = 128
	HexFormat = 160

class GuidParseThrowStyle(Enum):
	None = 0
	All = 1
	AllButOverflow = 2

class ParseFailureKind(Enum):
	None = 0
	ArgumentNull = 1
	Format = 2
	FormatWithParameter = 3
	NativeException = 4
	FormatWithInnerException = 5

class MemberListType(Enum):
	All = 0
	CaseSensitive = 1
	CaseInsensitive = 2
	HandleToInfo = 3

class DispatchWrapperType(Enum):
	Unknown = 1
	Dispatch = 2
	Record = 4
	Error = 8
	Currency = 16
	BStr = 32
	SafeArray = 65536

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
	Max = 11
	CallConvMask = 15
	Generics = 16
	HasThis = 32
	ExplicitThis = 64

class TimeZoneInfoResult(Enum):
	Success = 0
	TimeZoneNotFoundException = 1
	InvalidTimeZoneException = 2
	SecurityException = 3

class ParseFailureKind(Enum):
	ArgumentNullException = 0
	ArgumentException = 1
	ArgumentOutOfRangeException = 2
	FormatException = 3

class DTT(Enum):
	End = 0
	NumEnd = 1
	NumAmpm = 2
	NumSpace = 3
	NumDatesep = 4
	NumTimesep = 5
	MonthEnd = 6
	MonthSpace = 7
	MonthDatesep = 8
	NumDatesuff = 9
	NumTimesuff = 10
	DayOfWeek = 11
	YearSpace = 12
	YearDateSep = 13
	YearEnd = 14
	TimeZone = 15
	Era = 16
	NumUTCTimeMark = 17
	Unk = 18
	NumLocalTimeMark = 19
	Max = 20

class TM(Enum):
	AM = 0
	PM = 1
	NotSet = -1

class DS(Enum):
	BEGIN = 0
	N = 1
	NN = 2
	D_Nd = 3
	D_NN = 4
	D_NNd = 5
	D_M = 6
	D_MN = 7
	D_NM = 8
	D_MNd = 9
	D_NDS = 10
	D_Y = 11
	D_YN = 12
	D_YNd = 13
	D_YM = 14
	D_YMd = 15
	D_S = 16
	T_S = 17
	T_Nt = 18
	T_NNt = 19
	ERROR = 20
	DX_NN = 21
	DX_NNN = 22
	DX_MN = 23
	DX_NM = 24
	DX_MNN = 25
	DX_DS = 26
	DX_DSN = 27
	DX_NDS = 28
	DX_NNDS = 29
	DX_YNN = 30
	DX_YMN = 31
	DX_YN = 32
	DX_YM = 33
	TX_N = 34
	TX_NN = 35
	TX_NNN = 36
	TX_TS = 37
	DX_NNY = 38

class CacheType(Enum):
	Method = 0
	Constructor = 1
	Field = 2
	Property = 3
	Event = 4
	Interface = 5
	NestedType = 6

class State(Enum):
	Escaped = 0
	NotEscaped = 1
	StartOfToken = 2
	EndOfLine = 3

class ICloneable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Clone(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

class EventArgs:

	def __init__(self) -> None:
		"""No Description
		"""
		pass

