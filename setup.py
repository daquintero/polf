#!/usr/bin/env python
import setuptools

# # read the contents of your README file
# from pathlib import Path
# this_directory = Path(__file__).parent
# long_description = (this_directory / "README_RAW.md").read_text()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpt_parser",
    version="0.0.1",
    description="Report RPT file parser for Openlane OpenROAD Static Timing Analysis output files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daquintero/rpt_parser",
    author="Dario Quintero",
    author_email="darioaquintero@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    # install_requires=[
    #     "ipython",
    #     "numpy",
    #     "pandas",
    #     "sympy",
    #     # "scipy",
    #     "cython",
    #     "tabulate",
    # ],
    # TODO sort out requirements outside of Anaconda3
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
