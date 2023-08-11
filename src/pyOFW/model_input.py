from typing import Any, Dict, List

import pandas as pd
import numpy as np


def scenario_df(water_model: Any) -> pd.DataFrame:
    from OpenFlows.Domain.ModelingElements import IScenario
    from OpenFlows.Water.Domain import IWaterModel

    wm: IWaterModel = water_model
    scenarios: List[Dict[str, Any]] = []

    scenario: IScenario
    for scenario in wm.Scenarios.Elements():
        scenario_dict: Dict[str, Any] = dict()
        scenario_dict["Id"] = scenario.Id
        scenario_dict["Label"] = scenario.Label
        scenario_dict["IsActive"] = wm.ActiveScenario.Id == scenario.Id
        scenario_dict["ParentId"] = np.nan
        scenario_dict["ParentLabel"] = np.nan
        if scenario.ParentScenario is not None:
            scenario_dict["ParentId"] = scenario.ParentScenario.Id
            scenario_dict["ParentLabel"] = scenario.ParentScenario.Label

        scenarios.append(scenario_dict)

    df = pd.DataFrame(scenarios)
    df["Id"] = df["Id"].astype('Int64')
    df["ParentId"] = df["ParentId"].astype('Int64')
    return df
