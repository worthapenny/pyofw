from pyOpenFlows import support
import pandas as pd
import unittest


class TestSetupOpenFlows(unittest.TestCase):

    # region Setup and Teardown

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # endregion

    # region Tests

    # region Test Lat / Lng
    def test_add_lat_lng(self):
        df = pd.DataFrame({
            "X": [3063456.483],
            "Y": [1235478.99]})

        support.add_lat_long(df=df, from_epsg=2231, x_col="X", y_col="Y")

        self.assertAlmostEqual(df["Lat"][0], 39.9795514636454, 4)
        self.assertAlmostEqual(df["Lng"][0], -105.27356160030409, 4)
    # endregion

    # endregion


if __name__ == '__main__':
    unittest.main()
