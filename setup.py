# https://github.com/pypa/sampleproject/blob/main/setup.py

from typing import List
import setuptools
import os
import pathlib

package_version = "0.0.4"
package_py_openflows = "pyOpenFlows"
stub_dir_name = "typings"

install_requires = [
    "networkx",
    "pandas",
    "pythonnet",
    "numpy",
    "pyproj",
]


app_path = pathlib.Path(__file__).parent
src_path = app_path.joinpath("src")


def build_package_files(root_path: pathlib.Path) -> List[str]:
    paths: List[str] = []
    for (path, _, filenames) in os.walk(str(root_path)):
        for filename in filenames:
            full_path = os.path.join('..', path, filename)
            paths.append(full_path)
    return paths


stub_files = build_package_files(src_path.joinpath(stub_dir_name))

package_data = {package_py_openflows: stub_files}
packages = [package_py_openflows]

with open(app_path.joinpath("README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyofw",
    version=package_version,
    author="Akshaya Niraula",
    author_email="Akshaya.Niraula@gmail.com",
    description="Bentley OpenFlows API stub files plus a few py files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/worthapenny/pyofw",
    project_urls={
        "Bug Tracker": "https://github.com/worthapenny/pyofw/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 4 - Beta",
    ],
    package_dir={'': "src"},
    packages=packages,
    package_data=package_data,
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
