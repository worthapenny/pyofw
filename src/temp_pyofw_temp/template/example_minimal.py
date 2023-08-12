from pyofw.config import OFWConfig

ofw = OFWConfig()

from OpenFlows.Water.Domain import IWaterModel # type: ignore

model_filepath = r"C:\Program Files (x86)\Bentley\WaterGEMS\Samples\Example5.wtg"

print("Opening model...")
model: IWaterModel = ofw.open_model(model_filepath)
print(f"Model '{model}' is now opened.")

print(f"Active scenario is: {model.ActiveScenario.Label} is in the {model}")
print(f"And there are '{model.Scenarios.Count}' scenarios in the model")

print(f"About to close the model")
ofw.end_session()
print(f"Closed the model and also ended the session")
