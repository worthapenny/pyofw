class IOpenFlowsWaterDefaults:

	def __new__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DefaultIsActive(self) -> bool:
		"""Set the default value for IsActive when creating new elements
            Applies to domain elements only.

		Note
		--------
			Default value is true

		Returns
		--------
			`bool` : 
		"""
		pass

	@DefaultIsActive.setter
	def DefaultIsActive(self, defaultisactive: bool) -> None:
		pass

	@property
	def UseElementLabeling(self) -> bool:
		"""Use the element label generator settings for setting the label
            of a new element.  Applies to domain elements only.

		Note
		--------
			Default value is true

		Returns
		--------
			`bool` : 
		"""
		pass

	@UseElementLabeling.setter
	def UseElementLabeling(self, useelementlabeling: bool) -> None:
		pass

