from enum import Enum
from OpenFlows.Domain.IDataObjects import IModelAlternatives
from OpenFlows.Water.Domain.ModelingElements.INetworkElements import WaterNetworkElementType
from OpenFlows.Water.IUnits import INetworkElementUnits, IComponentElementUnits

class WaterAlternativeType(Enum):
	Physical = 4

class IWaterAlternatives(IModelAlternatives[WaterNetworkElementType, WaterAlternativeType, INetworkElementUnits, IComponentElementUnits]):

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

