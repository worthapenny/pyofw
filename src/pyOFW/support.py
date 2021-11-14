import pandas as pd
import logging


def add_lat_long(df: pd.DataFrame, from_epsg: int, x_col: str = "X", y_col: str = "Y") -> None:
    """Adds Lat and Lng column with lat, lng value generated based on given epsg code

    Args
    ---------
        df (`pd.DataFrame`): Dataframe with X and Y columns
        from_epsg (`int`): EPSG code of current project
        x_col (`str`, optional): X Column. Defaults to "X".
        y_col (`str`, optional): Y Column. Defaults to "Y".

    Returns
    ---------
        `None`: Lat, and Lng, columns will be added/update on the given dataframe. 
    """

    from pyproj import Proj, transform
    to_epsg = 4326
    inProj = Proj(f'epsg:{from_epsg}')
    outProj = Proj(f'epsg:{to_epsg}')

    logging.debug(
        f"About to generate Lat, and Lng to the df based on EPSG:{from_epsg} -> EPSG:{to_epsg}")

    df[["Lat", "Lng"]] = df.apply(
        lambda row: transform(inProj, outProj, row[x_col], row[y_col]),
        axis=1).tolist()

    logging.info(
        f"Generated Lat, and Lng to the df based on EPSG:{from_epsg} -> EPSG:{to_epsg}")
    return None
