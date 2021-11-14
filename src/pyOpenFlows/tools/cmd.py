import pathlib
import sys


def prepareofw_command():
    args = sys.argv[1:]
    if len(args) < 1:
        print("Prepared with no args")
    else:
        print(f"Prepared with > args {','.join(args)}")
    pass
