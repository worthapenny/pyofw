from enum import Enum
from OpenFlows.Domain.IModelingElements import IElement, TElementTypeEnum, TUnitsType, IModelingElementBase, TElementManagerType, TElementType, IElementUnits, IElementInput, IElementResults, IElementsInput, IElementsResults, IModelingElementsBase, IGeometryUnits, IElements, IElementManager
from typing import Generic, List, overload, Dict, TypeVar
from OpenFlows.Domain.ModelingElements.ISupport import IFieldManager
from Haestad.Support.ISupport import GeometryPoint, IEditLabeled, ILabeled
from OpenFlows.IUnits import IUnit

TElementInputType = TypeVar("TElementInputType")
TElementResultsType = TypeVar("TElementResultsType")
TElementsInputType = TypeVar("TElementsInputType")
TElementsResultsType = TypeVar("TElementsResultsType")

class ElementStateType(Enum):
	All = 0
	Active = 1
	Inactive = 2

class IMorphable(Generic[TElementTypeEnum]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Morph(self, toElementType: TElementTypeEnum) -> IElement:
		"""No Description

		Args
		--------
			toElementType (`TElementTypeEnum`) :  toElementType

		Returns
		--------
			`IElement` : 
		"""
		pass

class INetworkElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], IModelingElementBase[TElementManagerType, TElementType, TElementTypeEnum], IMorphable[TElementTypeEnum]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GISIDs(self) -> str:
		"""A comma-delimited string representing the GIDs of the element.

		Returns
		--------
			`str` : 
		"""
		pass

	@GISIDs.setter
	def GISIDs(self, gisids: str) -> None:
		pass

	@property
	def Input(self) -> TElementInputType:
		"""Provides easy access to only input properties for this element.

		Returns
		--------
			`TElementInputType` : 
		"""
		pass

	@property
	def Results(self) -> TElementResultsType:
		"""Provides easy access to only result properties for this element.
            Null if there are no results available for the current scenario.

		Returns
		--------
			`TElementResultsType` : 
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""Provides easy access to this element's field formatters.

		Returns
		--------
			`TUnitsType` : 
		"""
		pass

class INetworkElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], IModelingElementsBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Elements(self, state: ElementStateType) -> List[TElementType]:
		"""Returns a list of elements of the given state.

		Args
		--------
			state (`ElementStateType`) :  Determines the state of the element to include

		Returns
		--------
			`List[TElementType]` : Returns a list of 
		"""
		pass

	@overload
	def Elements(self, label: str) -> List[TElementType]:
		"""No Description

		Args
		--------
			label (`str`) :  label

		Returns
		--------
			`List[TElementType]` : 
		"""
		pass

	@overload
	def Elements(self) -> List[TElementType]:
		"""No Description

		Returns
		--------
			`List[TElementType]` : 
		"""
		pass

	@property
	def Results(self) -> TElementsResultsType:
		"""Access to results for this element list.

		Returns
		--------
			`TElementsResultsType` : 
		"""
		pass

	@property
	def Input(self) -> TElementsInputType:
		"""Access to input for this elements list.

		Returns
		--------
			`TElementsInputType` : 
		"""
		pass

	@property
	def ResultFields(self) -> IFieldManager:
		"""Access to result fields for this manager

		Returns
		--------
			`IFieldManager` : 
		"""
		pass

class IActiveElementInput(IElementInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsActive(self) -> bool:
		"""Specifies whether this element is active in the current scenario.

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsActive.setter
	def IsActive(self, isactive: bool) -> None:
		pass

class IActiveElementsInput(IElementsInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IsActives(self) -> Dict[int,int][int,bool]:
		"""Gets all IsActive values for all elements of this type.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def IsActives(self, ids: List[int]) -> Dict[int,int][int,bool]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

class IPointNodeInput(IActiveElementInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoint(self) -> GeometryPoint:
		"""Gets the geometry of the node.

		Returns
		--------
			`GeometryPoint` : 
		"""
		pass

	def SetPoint(self, point: GeometryPoint) -> None:
		"""Sets the geometry of the node.

		Args
		--------
			point (`GeometryPoint`) :  The point location of the node.

		Returns
		--------
			`None` : 
		"""
		pass

class IPointNodesInput(IActiveElementsInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Geometries(self) -> Dict[int,int][int,GeometryPoint]:
		"""Gets the geometry of all nodes of this type.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def Geometries(self, ids: List[int]) -> Dict[int,int][int,GeometryPoint]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

class IBaseLinkInput(IActiveElementInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self) -> List[GeometryPoint]:
		"""Gets the list of geometry for the link.  The first point is the geometry of the start node.  The last point
            is the geometry of the stop node.

		Returns
		--------
			`List[GeometryPoint]` : 
		"""
		pass

	def SetPoints(self, points: List[GeometryPoint]) -> None:
		"""No Description

		Args
		--------
			points (`List[GeometryPoint]`) :  points

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def StartNode(self) -> IElement:
		"""The ID of the start node of the link.

		Returns
		--------
			`IElement` : 
		"""
		pass

	@StartNode.setter
	def StartNode(self, startnode: IElement) -> None:
		pass

	@property
	def StopNode(self) -> IElement:
		"""The ID of the stop node of the link.

		Returns
		--------
			`IElement` : 
		"""
		pass

	@StopNode.setter
	def StopNode(self, stopnode: IElement) -> None:
		pass

	@property
	def IsUserDefinedLength(self) -> bool:
		"""Determines if the length is defined by the user.

		Returns
		--------
			`bool` : 
		"""
		pass

	@IsUserDefinedLength.setter
	def IsUserDefinedLength(self, isuserdefinedlength: bool) -> None:
		pass

	@property
	def Length(self) -> float:
		"""Returns the unified length - user defined, scaled or 3D in display units.
            If the value is set, Is User Defined Length is automatically set to true.

		Returns
		--------
			`float` : 
		"""
		pass

	@Length.setter
	def Length(self, length: float) -> None:
		pass

class IBaseLinksInput(IActiveElementsInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Geometries(self) -> Dict[int,int][int,List[GeometryPoint]]:
		"""Gets the polyline geometries for all base links.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def Geometries(self, ids: List[int]) -> Dict[int,int][int,List[GeometryPoint]]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def StartNodes(self) -> Dict[int,int][int,IElement]:
		"""Gets start nodes for all base links.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def StartNodes(self, ids: List[int]) -> Dict[int,int][int,IElement]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def StopNodes(self) -> Dict[int,int][int,IElement]:
		"""Gets stop nodes for all base links.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def StopNodes(self, ids: List[int]) -> Dict[int,int][int,IElement]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def IsUserDefinedLengths(self) -> Dict[int,int][int,bool]:
		"""Gets user defined lengths for all base links.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def IsUserDefinedLengths(self, ids: List[int]) -> Dict[int,int][int,bool]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def Lengths(self) -> Dict[int,int][int,float]:
		"""Gets lengths for all base links.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def Lengths(self, ids: List[int]) -> Dict[int,int][int,float]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

class IBaseLinksResults(IElementsResults):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseLinkResults(IElementResults):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseLinkUnits(IGeometryUnits):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""The formatter name for length.

		Returns
		--------
			`IUnit` : 
		"""
		pass

class IBasePolygonInput(IActiveElementInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetRings(self) -> List[List[GeometryPoint]]:
		"""Gets the rings of the polygon.

		Returns
		--------
			`List[List[GeometryPoint]]` : 
		"""
		pass

	def SetRings(self, rings: List[List[GeometryPoint]]) -> None:
		"""Sets the rings of the polygon.

		Args
		--------
			rings (`List[List[GeometryPoint]]`) :  rings

		Returns
		--------
			`None` : 
		"""
		pass

	@property
	def ScaledArea(self) -> float:
		"""The scaled area of the polygon based on the polygon geometry

		Returns
		--------
			`float` : 
		"""
		pass

class IBasePolygonsInput(IActiveElementsInput):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Geometries(self) -> Dict[int,int][int,List[List[GeometryPoint]]]:
		"""Gets ring geometry for all polygons.

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

	@overload
	def Geometries(self, ids: List[int]) -> Dict[int,int][int,List[List[GeometryPoint]]]:
		"""No Description

		Args
		--------
			ids (`List[int]`) :  ids

		Returns
		--------
			`Dict[int,int]` : 
		"""
		pass

class IBasePolygonsResults(IElementsResults):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBasePolygonResults(IElementResults):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

