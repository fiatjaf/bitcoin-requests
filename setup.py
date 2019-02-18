import pathlib
from setuptools import setup

import bitcoin

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="bitcoin-requests",
    version=bitcoin.__version__,
    description="Simplest Bitcoin Core RPC interface.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fiatjaf/bitcoin-requests",
    author="fiatjaf",
    author_email="fiatjaf@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["bitcoin"],
    include_package_data=True,
    install_requires=["requests"],
)
