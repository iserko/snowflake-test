from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="snowflake-test",
    version="0.1.0",
    description="Package to test Snowflake python connector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["snowflake-connector-python", "environs"],
    entry_points={"console_scripts": ["query=snowflake_test.query:query"]},
)
