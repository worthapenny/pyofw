import pathlib
import shutil
import logging
from distutils.dir_util import copy_tree
from typing import Tuple

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s [%(filename)s]:\t%(message)s",
    datefmt="%d %H:%M:%S",
)
logging.info("-" * 60)
logging.info("Copying local package to site-package dir")
logging.info("-" * 60)


package_name = "pyOFW"
src_path = pathlib.Path(r"src").resolve()
src_package_path = src_path.joinpath(package_name)

# create dir in site-packages
site_packages_path = pathlib.Path(
    r"D:\Development\Python\Python39-64\Lib\site-packages"
)
tgt_package_path = site_packages_path.joinpath(package_name)


def __copy_dir(source_path: pathlib.Path, destination_path: pathlib.Path) -> bool:
    success = True

    try:
        if destination_path.exists():
            shutil.rmtree(destination_path)

        destination_path.mkdir(parents=True, exist_ok=True)
        copy_tree(str(source_path), str(destination_path))

        logging.info(f"Copied")
        __get_contents_count(source_path)
        __get_contents_count(destination_path)

    except:
        logging.exception(f"ERROR.")

    return success


def __get_contents_count(path: pathlib.Path) -> Tuple[int, int]:
    num_of_sub_dirs, num_of_files = 0, 0
    for f in path.rglob('*'):
        if f.is_dir():
            num_of_sub_dirs += 1
        if f.is_file():
            num_of_files += 1

    logging.info(
        f"Directory Count = {num_of_sub_dirs}, Files Count = {num_of_files}, Path: {path}")
    return (num_of_sub_dirs, num_of_files)


logging.info(f"Copying '{src_package_path}' to '{tgt_package_path}' ...")
__copy_dir(src_package_path, tgt_package_path)

logging.info("-" * 60)
