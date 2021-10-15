import setuptools
import os
import pathlib


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


stub_files = package_files(pathlib.Path(__file__).parent.joinpath("typings"))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyofw",
    version="0.0.2",
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
    package_data={"": stub_files},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "pythonnet"
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
)
