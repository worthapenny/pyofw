'''
Author: Akshaya Niraula
Create Time: 2021-11-15 02:02:34
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''

import os
import shutil
from typing import Tuple
import unittest
import logging
import pathlib

# from pyofw.tools import cmd
from src.pyofw.tools import cmd


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
        typings_path = pathlib.Path(__file__).parent.parent.joinpath("typings")
        if typings_path.exists():
            typings_path.rmdir()
        pass

    # endregion

    # region Tests
    def test_help(self):
        success = cmd.newofw(["?"])
        self.assertTrue(success)

    def test_copy_1036(self):
        self.__test_files_copy(
            source_dir_name = "pyofw1036",
            version = "10.3.6"
            )
        
    def test_copy_1040(self):
        self.__test_files_copy(
            source_dir_name = "pyofw1040",
            version = "10.4"
            )

    def __test_files_copy(self, source_dir_name: str, version: str):
        tests_path = pathlib.Path(__file__).parent
        
        # (clean up any leftover items)
        # # make sure example/getting_started notebook files are not there
        example_min_py_path = tests_path.parent.joinpath("example_minimal.py")
        example_with_comments_py_path = tests_path.parent.joinpath("example_with_comments.py")
        getting_started_nb_path = tests_path.parent.joinpath("Getting_Started.ipynb")

        if example_min_py_path.exists():
            os.remove(str(example_min_py_path))
            self.assertFalse(example_min_py_path.exists())
        
        if example_with_comments_py_path.exists():
            os.remove(str(example_with_comments_py_path))
            self.assertFalse(example_with_comments_py_path.exists())

        if getting_started_nb_path.exists():
            os.remove(str(getting_started_nb_path))
            self.assertFalse(getting_started_nb_path.exists())


        self.__check_typings_contents(
            tests_path, 
            source_dir_name, 
            version)

        self.__check_getting_started_contents(
            tests_path,
            example_min_py_path, 
            example_with_comments_py_path, 
            getting_started_nb_path, 
        )


    def __check_typings_contents(
            self,
            tests_path: pathlib.Path,
            source_dir_name: str,
            version_str: str):

        typings_path = tests_path.parent.joinpath("typings")
        if typings_path.exists():
            shutil.rmtree(str(typings_path))
            typings_path.mkdir(parents=True, exist_ok=True)

        # make sure source path exists
        src_path = tests_path.parent.joinpath("src")
        self.assertTrue(src_path.exists())

        # make sure stub path exists
        src_typings_pyofw_version_path = src_path.joinpath(
            "pyofw", "typings", source_dir_name)
        self.assertTrue(src_typings_pyofw_version_path.exists())

        try:
            success = cmd.newofw([version_str])
            self.assertTrue(success)

            cmd_typings_contents = self.__get_contents_count(typings_path)
            src_typings_pyofw_version_contents = self.__get_contents_count(
                src_typings_pyofw_version_path)

            # Make sure the number of dirs and number of files are same compared to src
            self.assertTupleEqual(
                src_typings_pyofw_version_contents, cmd_typings_contents)

        finally:
            if typings_path.exists():
                shutil.rmtree(typings_path)
            

    def __check_getting_started_contents(
            self,
            tests_path: pathlib.Path,
            example_min_py_path: pathlib.Path,
            example_with_comments_py_path: pathlib.Path,
            getting_started_nb_path: pathlib.Path,
    ):
        # expected files path
        example_min_py_path = tests_path.parent.joinpath(example_min_py_path.name)
        example_with_comments_py_path = tests_path.parent.joinpath(example_with_comments_py_path.name)
        getting_started_nb_path = tests_path.parent.joinpath(getting_started_nb_path.name)

        # make sure getting started template files exits    
        self.assertTrue(example_min_py_path.exists())
        self.assertTrue(example_with_comments_py_path.exists())
        self.assertTrue(getting_started_nb_path.exists())
    
        # now delete the files
        example_min_py_path.unlink(missing_ok=True)
        example_with_comments_py_path.unlink(missing_ok=True)
        getting_started_nb_path.unlink(missing_ok=True)

        # make sure getting started template files are delete    
        self.assertFalse(example_min_py_path.exists())
        self.assertFalse(example_with_comments_py_path.exists())
        self.assertFalse(getting_started_nb_path.exists())
        pass

    # endregion

    # region private functions

    def __get_contents_count(self, path: pathlib.Path) -> Tuple[int, int]:
        num_of_sub_dirs, num_of_files = 0, 0
        for f in path.rglob('*'):
            if f.is_dir():
                num_of_sub_dirs += 1
            if f.is_file():
                num_of_files += 1

        logging.info(
            f"Directory Count = {num_of_sub_dirs}, Files Count = {num_of_files}, Path: {path}")
        return (num_of_sub_dirs, num_of_files)
    # endregion


if __name__ == '__main__':
    unittest.main()
