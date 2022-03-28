'''
Author: Akshaya Niraula
Create Time: 2021-11-13 19:48:34
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''

import pathlib
import sys
import os
import shutil
import logging
from typing import List
from distutils.dir_util import copy_tree
from datetime import datetime

# region Constants
__unreleased_stub_dir = "pyOFW"
__1035_stub_dir = "pyOFW1035"
__1036_stub_dir = "pyOFW1036"
__typings_dir_name = "typings"
# endregion

# region Public Methods


def newofw_command() -> None:
    args = sys.argv[1:]
    return newofw(args)


def newofw(args: List[str]) -> bool:
    typings_path = pathlib.Path(os.getcwd()).joinpath(__typings_dir_name)
    success: bool = True

    # NOTE:
    # Make sure to update this section with every release of Water Product
    # So that "newofw" will always get the latest released version
    if args == None or len(args) < 1:
        print(__setting_up_msg("10.3"))
        success = __copy_stub_1036(typings_path)  # // latest on 103
    else:
        arg = args[0]
        if arg == "?" or arg == "help":
            success = __show_help()

        elif arg.startswith("10.3.5"):
            print(__setting_up_msg(arg))
            success = __copy_stub_1035(typings_path)

        elif arg.startswith("10.3.6"):
            print(__setting_up_msg(arg))
            success = __copy_stub_1036(typings_path)

        elif arg.startswith("UNRELEASED"):
            print(__setting_up_msg(arg))
            success = __copy_stub_unreleased(typings_path)

        else:
            print(f"ERROR: '{arg}' is unsupported keyword.")
            print()
            success = __show_help()

    return success


# endregion

# region Help Command


def __show_help() -> bool:
    print(
        f"To get started with OpenFlows[Water], type in 'newofw targetVersion' such as:")
    print(f"newofw 10.3")
    print(f"newofw 10.3.6")
    print(f"If only newofw is executed, it will setup for the latest version of Water products")
    print(f"To show this help message, 'newofw ?' or 'newofw help'")

    return True
# endregion


# region Copy Stubs from package dir to user's working directory
def __copy_stub_1035(to_path: pathlib.Path) -> bool:
    return __copy_stub_files(__1035_stub_dir, to_path)


def __copy_stub_1036(to_path: pathlib.Path) -> bool:
    return __copy_stub_files(__1036_stub_dir, to_path)


def __copy_stub_unreleased(to_path: pathlib.Path) -> bool:
    return __copy_stub_files(__unreleased_stub_dir, to_path)


def __copy_stub_files(stub_dir_name: str, to_path: pathlib.Path) -> bool:
    success = True
    try:
        package_path = pathlib.Path(__file__).parent.parent
        stub_files_path = package_path.joinpath(
            __typings_dir_name, stub_dir_name)
        success = __copy_dir(stub_files_path, to_path)

        if success:
            template_filenames = __copy_template_getting_started()
            if template_filenames:
                names = ", ".join([f.name for f in template_filenames])
                print(
                    f"Setup complete (typings directory, {names} added)")
            else:
                print("Setup complete (typings directory added).")
        else:
            print("Setup was unsuccessful, see previous errors.")
    except Exception as ex:
        print(f"ERROR: Failed to setup.\n {ex}")
        logging.exception(("...while setting up"))
        success = False

    return success


def __copy_dir(source_path: pathlib.Path, destination_path: pathlib.Path) -> bool:
    success = True

    # delete the 'typings' folder if exits to clear the leftover
    if destination_path.exists():
        shutil.rmtree(destination_path)

    # create a new 'typings' dir
    destination_path.mkdir(parents=True, exist_ok=True)

    try:
        copy_tree(str(source_path), str(destination_path))

    except Exception as ex:
        success = False
        print(f"ERROR: {ex}")
        logging.exception("...while coping files/folders.")

    return success

# endregion - Copy stubs

# region Copy Template


def __copy_template_getting_started() -> List[str]:
    template_dir_name = "template"
    template_files = ["getting_started.py", "Getting_Started.ipynb", ]

    # source files
    src_template_paths = [
        pathlib.Path(__file__).parent.parent.joinpath(
            template_dir_name, f) for f in template_files
    ]

    # target files
    target_tempate_paths = [
        pathlib.Path(os.getcwd()).joinpath(f) for f in template_files
    ]

    # Prevent overwriting users file
    updated_target_file_paths: List[pathlib.Path] = []
    for f in target_tempate_paths:
        if f.exists():
            suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f.name.replace(f.name, f"{f.stem}_{suffix}{f.suffix}")
            updated_target_file_paths.append(f.with_name(name))
        else:
            updated_target_file_paths.append(f)

    # copy files
    copied_file_paths: List[pathlib.Path] = []
    for i in range(0, len(src_template_paths)):
        try:
            src_file = src_template_paths[i]
            target_file = updated_target_file_paths[i]
            copied_file_paths.append(
                pathlib.Path(
                    shutil.copyfile(str(src_file), str(target_file))
                )
            )

        except Exception as ex:
            print(
                f"ERROR: Failed to copy {updated_target_file_paths[i].name} file.\r{ex}")
            logging.exception("...while copying getting started files.")

    return copied_file_paths
# endregion


def __setting_up_msg(ver: str) -> str:
    return f"Setting up for the {ver} version of Water[GEMS/CAD/OPS]."

# endregion private methods
