## `NetworkInput` class (a pure python class)

In the `pyofw` module, there is a `NetworkInput` class under `pyOpenFlows.networkInput`. This class mostly uses the IDictionary<int, object> collection from IWaterModel.Network.[elements].Input.[property] and converts that into pandas `DataSeries` item, collection of which gives the `DataFrame` for that Network Element Type