'''
Author: Akshaya Niraula
Create Time: 2021-11-15 15:10:11
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''


# -------------------- VERY FIRST STEP ---------------------
# | From command line run:
# | newofw
# | --------------------------------------------------------
# | Above command will add "typings folder" to the workspace
# | This will enable the intellisense!
# | --------------------------------------------------------
# | NOTE:
# | This example doesn't take advantage of pyofw module on purpose
# | as it is trying to show the similarity between .NET and python
# | on how a model can be opened
# | --------------------------------------------------------


# To Open Model with just 3 lines
# ...look at the example/readme.md (It has Jupyter Notebook example too)

import sys
import clr # from pip install pythonnet, (NOT: pip install clr)

from pathlib import Path

# specify where the OpenFlows.dll, OpenFlows.Water.dll are
install_dlls_dir = r"C:\Program Files (x86)\Bentley\WaterGEMS\x64"
assert Path(install_dlls_dir).exists()

sys.path.append(install_dlls_dir)

# Load the dlls
loaded = clr.AddReference('OpenFlows.Water')
# when it fails to load, inspect loaded to learn more
assert loaded is not None

# NOTE:
# AFTER performing the above load ONLY,
# do the OpenFlow.* imports
# if not, error is thrown at runtime
from OpenFlows.Water import OpenFlowsWater, WaterProductLicenseType

print("Initializing session of OpenFlows.Water...")
status = OpenFlowsWater.StartSession(WaterProductLicenseType.WaterGEMS)
assert f"{status}" == "OK"

# Path of the model file to be opened
print("Opening model...")
model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
assert Path(model_filepath).exists()

model = OpenFlowsWater.Open(model_filepath)
assert model is not None
print(f"Opened the '{model}' model")

# Pipe Count
print(f"There are '{model.Network.Pipes.Count}' pipes.")


# Change pipe size
pipes = model.Network.Pipes.Elements()
pipe = pipes[10]
new_pipe_dia = 100
print(f"Current Diameter of {pipe} is: {pipe.Input.Diameter}. It will be updated to {new_pipe_dia}")
pipe.Input.Diameter = new_pipe_dia
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

print(f"Running simulation... Has Results: {scenario.HasResults}")
scenario.Run()
print(f"Ran the simulation... Has Results: {scenario.HasResults}")


# Close the model, don't save anything
OpenFlowsWater.EndSession()
