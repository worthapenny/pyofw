# pyofw

![GitHub release (latest by date)](https://img.shields.io/github/v/release/worthapenny/pyofw)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyofw)

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

**Failed to install?** One of the requirements package is `pythonnet` which might not get installed directly. In such case, follow the steps [below](##How-to-install-pythonnet?).


 **Note:** The package itself will not add any value without the [Bentley's](https://www.bentley.com/en) OpenFlows application like [WaterGEMS](https://www.bentley.com/en/products/product-line/hydraulics-and-hydrology-software/watergems), [WaterCAD](https://www.bentley.com/en/products/product-line/hydraulics-and-hydrology-software/watercad), or WaterOPS. And the package assumes the application is installed at the default location. For WaterGEMS it is `C:\Program Files (x86)\Bentley\WaterGEMS\x64`.

## Usage

```python
# -------------------- VERY FIRST STEP ---------------------
# | From command line run:
# | newofw 10.3.6
# | --------------------------------------------------------
# | Above command will add "typings folder" to the workspace
# | FAILURE to do above will result in NO IntelliSense
# | --------------------------------------------------------


from pyOFW.ofwConfig import OpenFlowsWaterConfig

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

# close the model and the session
ofw_config.end_session()
```

## IntelliSense not working?

For IntelliSense to work properly, we have to make sure certain settings are configured properly. 

### VSCode IDE

If VSCode is the IDE of choice,

* Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and type in `Settings`. 
* Select `Preferences: Open User[/Workspace] Settings`, which will open up the Settings.
* In the search type, `stub`
* Either on User or Workspace tab, select `pylance`
* Under `Python ??? Analysis: Stub Path`, make sure `typings` is selected

![vscode_pylance_stub](misc/pylance_stub_typings.png)


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

### clr ERROR

>`AttributeError: module 'clr' has no attribute 'AddReference'`
> error that most likely due the installed package called `clr`. Simply uninstall this package and the error should go away.
>`pip uninstall clr`

### No module named 'OpenFlows'

>`ModuleNotFoundError: No module named 'OpenFlows'`
>Make sure the OpenFlows*.dll files are in the x64 directory of the Water products
>You could also pass in the custom location `ofw_config = OpenFlowsWaterConfig(dlls_dir="C:\Path\To\WaterGEMS\x64")`

## Get Started from Scratch (w/o pyOFW.openFlowsWaterConfig.py)

```python
import sys
import clr
import numpy as np

# specify where the OpenFlows.dll, OpenFlows.Water.dll are
install_dlls_dir = r"C:\Program Files (x86)\Bentley\WaterCAD\x64"
sys.path.append(install_dlls_dir)

# Load the dlls
loaded = clr.AddReference('OpenFlows.Water')
# when it fails to load, inspect loaded to learn more

# NOTE:
# AFTER performing the above load ONLY,
# do the OpenFlow.* imports
# if not, error is thrown at runtime
from OpenFlows.Water import OpenFlowsWater, WaterProductLicenseType

print("Initializing session of OpenFlows.Water...")
OpenFlowsWater.StartSession(WaterProductLicenseType.WaterGEMS)

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
```

## Developing pyofw

To install `pyofw`, along with the tools you need to develop and run test, run the following in your [virtual]evn:

```python
pip install -e .[dev]
```