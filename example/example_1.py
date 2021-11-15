# -------------------- VERY FIRST STEP ---------------------
# | From command line run:
# | newofw 10.x.x
# | --------------------------------------------------------
# | Above command will add "typings folder" to the workspace
# | The version (10.x.x) depends on the install OpenFlows Application
# | For WaterGEMS version 10.03.05.xx, newofw 10.3.5
# | FAILURE to do above will result in NO IntelliSense
# | --------------------------------------------------------


from pyOFW.openFlowsWaterConfig import AppType, OpenFlowsWaterConfig

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
# Example for WaterCAD
ofw_config = OpenFlowsWaterConfig(
    app_type=AppType.WaterCAD,
    dlls_dir=OpenFlowsWaterConfig.wtrc_install_dir)
# Above class loads the OpenFlow* assemblies
# as well as opens up the session where licensing
# information are checked


# NOTE:
# AFTER creating an instance of OpenFlowsWaterConfig ONLY,
# do the OpenFlow.* imports
# if not, error is thrown at runtime
from OpenFlows.Water.Domain import IWaterModel

# Path of the model file to be opened
model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
model: IWaterModel = ofw_config.open_model(model_filepath)

message = f"Active scenario is: {model.ActiveScenario}"
print(message)
log.info(message)


# To close the model and and the session
ofw_config.end_session()

# # To only close the model but not the session
# # Option 1:
# model.Close()

# # Option 2:
# ofw_config.end_session(end_session=False)
