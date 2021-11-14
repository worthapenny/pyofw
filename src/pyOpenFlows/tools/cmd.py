import pathlib
import sys
import os
import shutil
from distutils.dir_util import copy_tree


def newofw_command() -> None:
    args = sys.argv[1:]
    typings_dir_name = "typings"
    typings_path = pathlib.Path(os.getcwd()).joinpath(typings_dir_name)

    if len(args) < 1:
        print(__setting_up_msg("UNRELEASED"))
        __copy_stub_unreleased(typings_path)
    else:
        arg = args[0]
        if arg == "?" or arg == "help":
            __show_help()
        elif arg.startswith("10.3"):
            print(__setting_up_msg(arg))
            __copy_stub_103(typings_path)

        else:
            print(f"ERROR: '{arg}' is unsupported keyword.")
            print()
            __show_help()

    return None


def __show_help() -> None:
    print(
        f"To get started with OpenFlows[Water], type in 'newofw targetVersion' such as:")
    print(f"newofw 10.3")
    print(f"newofw 10.3.5")
    print(f"If only newofw is executed, it will setup for UNRELEASED version of Water products")
    print(f"To show this help message, 'newofw ?' or 'newofw help'")

    return None


def __setting_up_msg(ver: str) -> str:
    return f"Setting up for the {ver} version of WaterGEMS/WaterCAD/WaterOPS."


def __copy_stub_files(stub_dir_name: str, to_path: pathlib.Path) -> bool:
    success = True
    try:
        package_path = pathlib.Path(__file__).parent.parent
        stub_files_path = package_path.joinpath(stub_dir_name)
        success = __copy_dir(stub_files_path, to_path)
        print("Setup complete (typings directory added).")

    except Exception as ex:
        print(f"ERROR: Failed to setup.\n {ex}")
        success = False

    return success


def __copy_stub_103(to_path: pathlib.Path) -> bool:
    print("Not supported! (yet)")
    return True


def __copy_stub_unreleased(to_path: pathlib.Path) -> bool:
    unreleased_stub_dir = "pyOpenFlowsWaterTypings"
    return __copy_stub_files(unreleased_stub_dir, to_path)


def __copy_dir(source_path: pathlib.Path, destination_path: pathlib.Path) -> bool:
    success = True
    destination_path.mkdir(parents=True, exist_ok=True)

    for path in source_path.rglob("**"):
        final_destination_path = destination_path.joinpath(path.name)
        if final_destination_path.exists():
            shutil.rmtree(final_destination_path)

        try:
            # copy_tree(str(path), str(final_destination_path))
            shutil.copytree(str(path), str(final_destination_path),
                            copy_function=shutil.copy2, dirs_exist_ok=True)

        except Exception as ex:
            success = False
            print(f"ERROR: {ex}")
        success = False

    return success
