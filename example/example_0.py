# -------------------- VERY FIRST STEP ---------------------
# | From command line run:
# | newofw 10.3.5
# | --------------------------------------------------------
# | Above command will add "typings folder" to the workspace
# | FAILURE to do above will result in NO IntelliSense
# | --------------------------------------------------------


from pyOFW.openFlowsWaterConfig import OpenFlowsWaterConfig

ofw_config = OpenFlowsWaterConfig()

# NOTE:
# AFTER creating an instance of OpenFlowsWaterConfig ONLY,
# do the OpenFlow.* imports
# if not, error is thrown at runtime
from OpenFlows.Water.Domain import IWaterModel

model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
model: IWaterModel = ofw_config.open_model(model_filepath)

print(f"Active scenario is: {model.ActiveScenario}")
print(f"And there are '{model.Scenarios.Count}' scenarios in the model")

ofw_config.end_session()
