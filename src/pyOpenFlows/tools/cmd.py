
import pathlib
import sys
import os


def newofw_command() -> None:
    args = sys.argv[1:]
    print(f"You ran this from: {os.getcwd()}")

    def prepare_msg(ver: str) -> str:
        return f"Setting up for the {ver} version of WaterGEMS/WaterCAD/WaterOPS."

    if len(args) < 1:
        print(prepare_msg("UNRELEASED"))
    else:
        arg = args[0]
        if arg == "?" or arg == "help":
            __show_help()
        elif arg.startswith("10.3"):
            print(prepare_msg(arg))
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
