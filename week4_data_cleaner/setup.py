"""


"""

__author__ = "wangxukang"
__date__ = "2026/03/23"

from setuptools import setup, find_packages

setup(
    name="data-cleaner",
    version="0.0.1",
    description="Data Cleaner cli command",
    author="wangxukang",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
    ]
)