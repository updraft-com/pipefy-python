import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pipefypython",
    version="1.0.0",
    description="Python API for the Pipefy",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/updraft-com/pipefy-python",
    author="Uriel Mehamed",
    author_email="urielmehamed@gmail.com",
    install_requires=["requests"],
    license="MIT",
    packages=find_packages(),
    include_package_data=True)
