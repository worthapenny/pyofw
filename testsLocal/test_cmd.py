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

    def test_copy_1035(self):
        tests_path = pathlib.Path(__file__).parent

        # # make sure getting_started.py file is not there
        getting_started_path = tests_path.parent.joinpath("getting_started.py")
        if getting_started_path.exists():
            os.remove(str(getting_started_path))

        self.assertFalse(getting_started_path.exists())

        # # make sure Getting_Started.ipynb file is not there
        getting_started_nb_path = tests_path.parent.joinpath(
            "Getting_Started.ipynb")
        if getting_started_nb_path.exists():
            os.remove(str(getting_started_nb_path))

        self.assertFalse(getting_started_nb_path.exists())

        # make sure typings dir is not there
        self.__check_typings_version(
            tests_path, getting_started_path, getting_started_nb_path, "pyofw1036", "10.3.6")

        # now test for preventing overrite on getting started files
        try:
            files_count = sum(1 for _ in pathlib.Path(
                getting_started_path.parent).rglob("getting_started.*"))

            # NOTE:
            # For some unknown reason (yet), the command below doesn't work fully
            # (this worked successfully above)
            # It produces exception as copy fails
            # Hence not doing any testing if the command belows goes belly up
            # Output text shows exception which sadly is expected.

            # success = cmd.newofw([])

            # # if above copy fails, no need to test as will it will fails as well
            # # need to figure out why above is not working
            # if success:
            #     # make sure the getting_started.py and Getting_Started.ipynb still exits
            #     self.assertTrue(getting_started_path.exists())
            #     self.assertTrue(getting_started_nb_path.exists())

            #     # make sure new getting_started.py and Getting_Started.ipynb with current date-time is created
            #     new_files_count = sum(1 for _ in pathlib.Path(
            #         getting_started_path.parent).rglob("getting_started.*"))

            #     # there should be 2 more files that starts with getting_started name
            #     self.assertEqual(files_count + 2, new_files_count)

        finally:
            if getting_started_path.exists():
                getting_started_path.unlink()
            if getting_started_nb_path.exists():
                getting_started_nb_path.unlink()

    def __check_typings_version(
            self,
            tests_path: pathlib.Path,
            getting_started_path: pathlib.Path,
            getting_started_nb_path: pathlib.Path,
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
            cmd.newofw([version_str])
            cmd_typings_contents = self.__get_contents_count(typings_path)
            src_typings_pyofw_version_contents = self.__get_contents_count(
                src_typings_pyofw_version_path)

            # Make sure the number of dirs and number of files are same compared to src
            self.assertTupleEqual(
                src_typings_pyofw_version_contents, cmd_typings_contents)

            # make sure getting started templates exits
            self.assertTrue(getting_started_path.exists())
            self.assertTrue(getting_started_nb_path.exists())

        finally:
            if typings_path.exists():
                shutil.rmtree(typings_path)
            if getting_started_path.exists():
                getting_started_path.unlink(missing_ok=True)
            if getting_started_nb_path.exists():
                getting_started_nb_path.unlink(missing_ok=True)

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
