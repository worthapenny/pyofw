class IOpenFlowsWaterDefaults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DefaultIsActive(self) -> bool:
		"""No Description

		Returns:
			IOpenFlowsWaterDefaults: 
		"""
		pass

	@DefaultIsActive.setter
	def DefaultIsActive(self, defaultisactive: bool) -> None:
		pass

	@property
	def UseElementLabeling(self) -> bool:
		"""No Description

		Returns:
			IOpenFlowsWaterDefaults: 
		"""
		pass

	@UseElementLabeling.setter
	def UseElementLabeling(self, useelementlabeling: bool) -> None:
		pass

