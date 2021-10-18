import pandas as pd


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

    inProj = Proj(f'epsg:{from_epsg}')
    outProj = Proj('epsg:4326')

    df[["Lat", "Lng"]] = df.apply(
        lambda row: transform(inProj, outProj, row[x_col], row[y_col]),
        axis=1).tolist()

    return None
