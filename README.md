# pyofw

Python package for OpenFlowsWater module from Bentley that mainly contains the stub (*.pyi) files and a few py files to get started.

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

>**Failed to install?** One of the requirements package is `pythonnet` which might not get installed directly. In such case, follow the steps [below](##How-to-install-pythonnet?).
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

## How to install pythonnet?

> `pythonnet` may not get installed by `pip install pythonnet` as a result follow this alternative.

### Common Error message

> ERROR: Could not build wheels for pythonnet which use PEP 517 and cannot be installed directly

#### Steps to install pythonnet

1. Download the wheel file from <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pythonnet>
   1. For 3.9 version of python, on windows, download **`pythonnet-2.5.2-cp39-cp39-win_amd64.whl`**.
2. run `pip install "path\to\the\downloaded\pythonnet.whl"`
3. Test if pythonnet got installed. If `import clr` doesn't return any error then `pythonnet` is ready to use

   ```powershell
   c:\>python
    Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import clr
    >>>
   ```

## ERROR at Run Time?

During the run time, if you run into

```bat
AttributeError: module 'clr' has no attribute 'AddReference'
```

error that most likely due the installed package called `clr`. Simply uninstall this package and the error should go away.

```bat
pip uninstall clr
```
