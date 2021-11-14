# https://github.com/pypa/sampleproject/blob/main/setup.py

import setuptools
import pathlib

# the name of the installer for user to install
# this name will be in pypi, user will do pip install this name
pypi_package_name = "pyofw"

# version number of the package
package_version = "0.0.4"

# the first letter of the namespace (aka package)
# name of the directory under the src directory
package_py_openflows = "pyOFW"

# the dependency of this package
install_requires = [
    "networkx",
    "pandas",
    "pythonnet",
    "numpy",
    "pyproj",
]

# the root directory of the package
# in ths case: pyofw
app_path = pathlib.Path(__file__).parent

# the src directory where the package (namespace) starts
src_path = app_path.joinpath("src")

# dynamically add the contents from README.md
# so that pypi wll show the exact same readme as of github
with open(app_path.joinpath("README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=pypi_package_name,
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

    # do no use other method on providing package_dir
    # the src dir under which packages are round
    package_dir={'': "src"},

    # A simple list of root packages that are going to be available
    # Say there will be three distinct packages
    # like OpenFlows, Haestad, System then
    # packages = ["OpenFlows", "Haestad", "System"]
    packages=[package_py_openflows],

    # do not use "include_package" and provide a dictionary. WILL NOT WORK
    # use MANIFEST.in and based on that it will auto generate the contents
    # to be included
    include_package_data=True,

    # minimum version of the python required
    python_requires=">=3.6",

    # other dependencies for this package
    install_requires=install_requires,

    # other dependencies for developers to build this package
    extras_require={
        "dev": [
            "pytest>=3.7",
            "wheel",
            "twine"
        ],
    },

    # Create an exe in the Scripts directory
    # So that user can call the commands
    # from given path
    # Format:
    #  commandNameThatUserWillType = name.space.to-the.command:public_method_for_this_command_in_the_py_fle
    entry_points={
        'console_scripts': [
            'newofw=pyOpenFlows.tools.cmd:newofw_command',
        ],
    },
)
