'''
 # @ Author: Akshaya Niraula
 # @ Create Time: 2021-10-18 06:57:08
 # @ Modified by: Akshaya Niraula
 # @ Modified time: 2021-11-15 02:02:47
 # @ Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
 '''

from pyofw import support
import pandas as pd
import unittest
import logging


class TestSupport(unittest.TestCase):

    # region Setup and Teardown

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s.%(msecs)03d %(levelname)s [%(filename)s]:\t%(message)s",
            datefmt="%d %H:%M:%S",
        )
        logging.info("")
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
