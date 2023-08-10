from pyofw.config import AppType, OFWConfig

# if logging is desired
import logging
logging.basicConfig(
    level=logging.DEBUG,
    # level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
    datefmt="%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# Prepare for WaterGEMS
ofw = OFWConfig(
    app_type=AppType.WaterGEMS, # the default is WaterGEMS, this line can be commented
    dlls_dir=OFWConfig.WTRG_INSTALL_DIR # the default is for WaterGEMS, this line can be commented
)
# Above class loads the OpenFlow* assemblies
# as well as opens up the session


# NOTE:
# ONLY AFTER creating an instance of OFWConfig,
# do the OpenFlow.* imports
# if not, error is thrown at runtime
from OpenFlows.Water.Domain import IWaterModel  # type: ignore

# Path of the model file to be opened
model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"

logging.info("Opening model...")
model: IWaterModel = ofw.open_model(model_filepath)
logging.info(f"Opened '{model}' model got opened...")


# Change pipe size
pipes = model.Network.Pipes.Elements()
pipe = pipes[10]
new_pipe_dia = 100
logging.info(f"Current Diameter of {pipe} is: {pipe.Input.Diameter}. It will be updated to {new_pipe_dia}")
pipe.Input.Diameter = new_pipe_dia
logging.info(f"New Diameter of {pipe} is: {pipe.Input.Diameter}")


# Components > Patterns
patterns = model.Components.Patterns.Elements()
logging.info(f"The first pattern is: {patterns[0].Label}")


# Scenario Information
logging.info(f"Active scenario is: {model.ActiveScenario}")
logging.info(f"And there are '{model.Scenarios.Count}' scenarios in the model")


# Find scenario by label, and run it
scenario_label = "Variable Speed Pumping"
scenario = model.Scenarios.Element(scenario_label)
logging.info(f"Found scenario: {scenario}")

logging.info(f"Running simulation... Has Results: {scenario.HasResults}")
scenario.Run()
logging.info(f"Ran the simulation... Has Results: {scenario.HasResults}")


# To close the model and and the session
ofw.end_session()

# # To only close the model but not the session
# model.Close()
