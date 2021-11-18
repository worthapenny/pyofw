'''
 # @ Author: Akshaya Niraula
 # @ Create Time: 2021-10-14 19:32:26
 # @ Modified by: Akshaya Niraula
 # @ Modified time: 2021-11-15 15:15:24
 # @ Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
 '''

# -------------------- VERY FIRST STEP ---------------------
# | From command line run:
# | newofw 10.x.x
# | --------------------------------------------------------
# | Above command will add "typings folder" to the workspace
# | The version (10.x.x) depends on the install OpenFlows Application
# | For WaterGEMS version 10.03.05.xx, newofw 10.3.5
# | FAILURE to do above will result in NO IntelliSense
# | --------------------------------------------------------

import numpy as np
from pyOFW.ofwConfig import AppType, OFWConfig

# if logging is desired
import logging
logging.basicConfig(
    level=logging.DEBUG,
    # level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
    datefmt="%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# Default setup is for WaterGEMS where no arguments are needed
ofw_config = OFWConfig()
# Above class loads the OpenFlow* assemblies
# as well as opens up the session where licensing
# information are checked

# Example for WaterCAD
# ofw_config = OpenFlowsWaterConfig(
#     app_type=AppType.WaterCAD,
#     dlls_dir=OpenFlowsWaterConfig.wtrc_install_dir)


# NOTE:
# AFTER creating an instance of OpenFlowsWaterConfig ONLY,
# do the OpenFlow.* imports
# if not, error is thrown at runtime
from OpenFlows.Water.Domain import IWaterModel

# Path of the model file to be opened
# Path of the model file to be opened
print("Opening model...")
model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
model = OpenFlowsWater.Open(model_filepath)


# Network elements (Pipes), Unit, Format value with given unit
print(f"There are '{model.Network.Pipes.Count}' pipes.")
lengths = model.Network.Pipes.Input.Lengths()
# Note: if you do type(lengths)
# you will see it is an object of System.Collections.Generic
# so follow .NET approach to some level
lengths_array = [l for l in lengths.Values]  # notice ".Values"
sum = np.sum(lengths_array)
length_unit = model.Units.NetworkUnits.Pipe.LengthUnit
formatted_sum = model.Units.FormatValue(sum, length_unit)
print(f"The total pipe length is {formatted_sum} {length_unit.ShortLabel}")

# Change pipe size
pipes = model.Network.Pipes.Elements()
pipe = pipes[10]
print(f"Current Diameter of {pipe} is: {pipe.Input.Diameter}")
pipe.Input.Diameter = 100
print(f"New Diameter of {pipe} is: {pipe.Input.Diameter}")


# Components > Patterns
patterns = model.Components.Patterns.Elements()
print(f"The first pattern is: {patterns[0].Label}")


# Scenario Information
print(f"Active scenario is: {model.ActiveScenario}")
print(f"And there are '{model.Scenarios.Count}' scenarios in the model")


# Find scenario by label, and run it
scenario_label = "Variable Speed Pumping"
scenario = model.Scenarios.Element(scenario_label)
print(f"Found scenario: {scenario}")

print("Running simulation...")
scenario.Run()

# Close the model, don't save anything
OpenFlowsWater.EndSession()


# To close the model and and the session
ofw_config.end_session()

# # To only close the model but not the session
# # Option 1:
# model.Close()

# # Option 2:
# ofw_config.end_session(end_session=False)
