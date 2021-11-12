from typing import Dict, List
import setuptools
import os
import pathlib

package_version = "0.0.4"

package_py_openflows = "pyopenflows"
package_haestad = "haestad"
package_openflows = "openflows"
package_system = "system"

package_data: Dict[str, List[str]] = dict()
app_path = pathlib.Path(__file__).parent
src_path = app_path.joinpath("src")


def build_package_files(root_path: pathlib.Path, paths: List[str]) -> None:
    for (path, _, filenames) in os.walk(str(root_path)):
        for filename in filenames:
            full_path = os.path.join('..', path, filename)
            paths.append(full_path)
            # paths.append(str(pathlib.Path(full_path).relative_to(root_path)))
    return None


packages = [
    package_py_openflows,
    package_haestad,
    package_openflows,
    package_system,
]

package_data[package_py_openflows] = []
package_data[package_haestad] = []
package_data[package_openflows] = []
package_data[package_system] = []

build_package_files(src_path.joinpath(package_py_openflows),
                    package_data[package_py_openflows])
build_package_files(src_path.joinpath(package_haestad),
                    package_data[package_haestad])
build_package_files(src_path.joinpath(package_openflows),
                    package_data[package_openflows])
build_package_files(src_path.joinpath(package_system),
                    package_data[package_system])


# with open(app_path.joinpath("requirements.txt"), "r", encoding="utf-8") as fr:
#     install_requires = fr.read().splitlines()
# For some odd reasons I guess, the requirements.txt is not seen during the build
install_requires = [
    "networkx",
    "pandas",
    "pythonnet",
    "numpy",
    "pyproj",
]


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
    package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=packages,
    package_data=package_data,
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
)
