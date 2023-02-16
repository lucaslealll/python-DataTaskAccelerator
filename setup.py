import io

from setuptools import find_packages, setup

with io.open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Lucas Omar Andrade Leal",
    author_email="lucasomarandradeleal@gmail.com",
    description="My first Python library",
    install_requires=[],
    keywords="data task accelerator functions gspread datetime gsheets email selenium cookies sleep wait",
    license="MIT",
    long_description=long_description,
    name="data_task_accelerator",
    # namespace_packages=("scripts",),
    # packages=find_packages(include=["data_task_accelerator"]),
    packages=find_packages(exclude=("tests*", "system_tests*")),
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*",
    setup_requires=["pytest-runner"],
    test_suite="tests",
    tests_require=["pytest==7.2.1"],
    url="https://github.com/lucasoal/data-task-accelerator",
    version="1.0.0",
)
