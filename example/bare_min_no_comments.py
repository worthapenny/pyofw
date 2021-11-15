'''
 # @ Author: Akshaya Niraula
 # @ Create Time: 2021-11-14 07:10:24
 # @ Modified by: Akshaya Niraula
 # @ Modified time: 2021-11-15 15:15:17
 # @ Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
 '''

# -------------------- VERY FIRST STEP ---------------------
# | From command line run:
# | newofw 10.3.5
# | --------------------------------------------------------
# | Above command will add "typings folder" to the workspace
# | FAILURE to do above will result in NO IntelliSense
# | --------------------------------------------------------


from pyOFW.openFlowsWaterConfig import OpenFlowsWaterConfig

ofw_config = OpenFlowsWaterConfig()

from OpenFlows.Water.Domain import IWaterModel

model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
model: IWaterModel = ofw_config.open_model(model_filepath)

print(f"Active scenario is: {model.ActiveScenario}")
print(f"And there are '{model.Scenarios.Count}' scenarios in the model")

ofw_config.end_session()
