# https://github.com/pypa/sampleproject/blob/main/setup.py

import setuptools
import pathlib

package_version = "0.0.4"
package_py_openflows = "pyOpenFlows"

install_requires = [
    "networkx",
    "pandas",
    "pythonnet",
    "numpy",
    "pyproj",
]


app_path = pathlib.Path(__file__).parent
src_path = app_path.joinpath("src")

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
    packages=[package_py_openflows],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    entry_points={
        'console_scripts': [
            'prepareofw=pyOpenFlows.tools.cmd:prepareofw_command',
        ],
    },
)
