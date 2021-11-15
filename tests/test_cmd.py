'''
 # @ Author: Akshaya Niraula
 # @ Create Time: 2021-11-15 02:02:34
 # @ Modified by: Akshaya Niraula
 # @ Modified time: 2021-11-15 02:03:02
 # @ Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
 '''


import unittest
import logging

from sqlalchemy import true
from pyOFW.tools import cmd


class TestCMD(unittest.TestCase):

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

    # region Test Help Args
    def test_help(self):
        cmd.newofw(["?"])
        self.assertTrue(True)

    def test_copy(self):
        cmd.newofw(["10.3.5"])
    # endregion

    # endregion


if __name__ == '__main__':
    unittest.main()
