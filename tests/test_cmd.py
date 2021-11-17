'''
 # @ Author: Akshaya Niraula
 # @ Create Time: 2021-11-15 02:02:34
 # @ Modified by: Akshaya Niraula
 # @ Modified time: 2021-11-15 02:03:02
 # @ Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
 '''


from os import path
import shutil
from typing import Tuple
import unittest
import logging
from importlib_metadata import pathlib

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
    def test_help(self):
        cmd.newofw(["?"])
        self.assertTrue(True)

    def test_copy_1035(self):
        tests_path = pathlib.Path(__file__).parent
        typings_path = tests_path.parent.joinpath("typings")
        if typings_path.exists():
            shutil.rmtree(typings_path)

        self.assertFalse(typings_path.exists())

        src_path = tests_path.parent.joinpath("src")
        self.assertTrue(src_path.exists())

        src_typings_pyofw_1035_path = src_path.joinpath(
            "pyOFW", "typings", "pyOFW1035")
        self.assertTrue(src_typings_pyofw_1035_path.exists())

        try:
            cmd.newofw(["10.3.5"])
            cmd_typings_contents = self.__get_contents_count(typings_path)
            src_typings_pyofw_1035_contents = self.__get_contents_count(
                src_typings_pyofw_1035_path)

            # Make sure the number of dirs and number of files are same compared to src
            self.assertTupleEqual(
                src_typings_pyofw_1035_contents, cmd_typings_contents)

        finally:
            if typings_path.exists():
                shutil.rmtree(typings_path)
    # endregion

    # region private functions

    def __get_contents_count(self, path: pathlib.Path) -> Tuple[int, int]:
        num_of_sub_dirs, num_of_files = 0, 0
        for f in path.rglob('*'):
            if f.is_dir():
                num_of_sub_dirs += 1
            if f.is_file():
                num_of_files += 1

        return (num_of_sub_dirs, num_of_files)
    # endregion


if __name__ == '__main__':
    unittest.main()
