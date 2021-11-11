# pyofw

Python package for OpenFlowsWater module from Bentley that mainly contains the stub (*.pyi) files and a few py files to get started.

[![Build Python Package](https://github.com/worthapenny/pyofw/actions/workflows/python-build.yml/badge.svg)](https://github.com/worthapenny/pyofw/actions/workflows/python-build.yml)

## Must Create python.exe.config File

Bentley's WaterObjects.NET API contains a mixed mode (managed/unmanaged)
assemblies as a result, a python configuration file has to placed where the python.exe is location (in your environment). The contents of the file can be copied from below or use from [here](/misc/python.exe.config).

>**Note:** Filename is important. For "python.exe" create "python.exe.config"

```xml
<?xml version="1.0"?>
<configuration>
  <startup useLegacyV2RuntimeActivationPolicy="true">
    <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>
  </startup>
</configuration>
````

## Installation

Run the following to install:

```python
pip install pyofw
```

> **Note:** The package itself will not add any value without the [Bentley's](https://www.bentley.com/en) OpenFlows application like [WaterGEMS](https://www.bentley.com/en/products/product-line/hydraulics-and-hydrology-software/watergems), [WaterCAD](https://www.bentley.com/en/products/product-line/hydraulics-and-hydrology-software/watercad), or WaterOPS. And the package assumes the application is installed at the default location. For WaterGEMS it is `C:\Program Files (x86)\Bentley\WaterGEMS\x64`.

## Usage

```python
from pyOpenFlows.openFlowsWaterConfig import OpenFlowsWaterConfig

# if logging is desired
import logging
logging.basicConfig(
    level=logging.DEBUG,
    # level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
    datefmt="%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# Default setup is for WaterGEMS,
ofw_config = OpenFlowsWaterConfig()
# Above class loads the OpenFlow* assemblies
# as well as opens up the session where licensing
# information are checked


# # example for WaterCAD,
# from SetupOpenFlows import AppType
# setup = SetupOpenFlowsWater(AppType.WaterCAD)


# NOTE:
# After above setup ONLY, do the OpenFlow.* imports
# if not, error is thrown at runtime
from OpenFlows.Water.Domain import IWaterModel

# Path of the model file to be opened
model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"
model: IWaterModel = setup.open_model(model_filepath)

message = f"Active scenario is: {model.ActiveScenario}"
print(message)
log.info(message)


# To close the model and and the session
setup.end()

# # To only close the model but not the session
# # Option 1:
# model.Close()

# # Option 2:
# setup.end(close_session=False)
```

## Developing pyofw

To install `pyofw`, along with the tools you need to develop and run test, run the following in your [virtual]evn:

```python
pip install -e .[dev]
```
