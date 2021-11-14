import shutil
import pathlib
from typing import Union
from distutils.dir_util import copy_tree

copy_typings_from_assembly_crawler_dir = True

assembly_crawler_stubs_path = pathlib.Path(
    r"D:\Development\Python\assembly-crawler\typings")

local_src_path = pathlib.Path(r"typings").resolve()
local_src_path = pathlib.Path(r"src").resolve()
assert local_src_path.exists()

# region Utils


def copy_dir(source: Union[str, pathlib.Path], destination: Union[str, pathlib.Path]):
    destination_path: pathlib.Path

    if isinstance(source, str):
        source_path = pathlib.Path(source)
    elif isinstance(source, pathlib.Path):
        source_path = source

    if isinstance(destination, str):
        destination_path = pathlib.Path(destination)
    elif isinstance(destination, pathlib.Path):
        destination_path = destination

    destination_path.mkdir(parents=True, exist_ok=True)

    final_destination_path = destination_path.joinpath(source_path.name)
    if final_destination_path.exists():
        shutil.rmtree(final_destination_path)

    # shutil.copytree(str(source_path), str(final_destination_path))
    copy_tree(str(source_path), str(final_destination_path))

# endregion


# 1) Make sure the typings directory is up to date from assembly-crawler.sln
#     Make sure assembly-crawler project is in sync with https://github.com/MrMontana1889/assembly-crawler
if copy_typings_from_assembly_crawler_dir:
    open_flows_path = assembly_crawler_stubs_path.joinpath("OpenFlows")
    haestad_path = assembly_crawler_stubs_path.joinpath("Haestad")
    system_path = assembly_crawler_stubs_path.joinpath("System")

    assert open_flows_path.exists()
    assert haestad_path.exists()
    assert system_path.exists()

    copy_dir(open_flows_path, local_src_path)
    copy_dir(haestad_path, local_src_path)
    copy_dir(system_path, local_src_path)


# 2 update the MANIFEST.in file
# ..\pyofw> check-manifest --create (to create the MANIFEST.in file)


# Publish to pypi
# https://www.youtube.com/watch?v=GIF3LaRqgXo&t=798s

# 3) Prepare the installer
# CD to root directory i.e. pyofw
# ..\pyofw> python setup.py bdist_wheel sdist
# above will produce *.whl file and *.tar.gz file inside dist folder


# 4) Push to PyPI
# if needed: pip install twine
# twine upload dist/*
