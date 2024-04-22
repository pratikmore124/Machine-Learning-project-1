from setuptools import setup
from typing import List

# Declaring variable for setup functions

PROJECT_NAME="housing-predictor",
VERSION="0.0.1",
AUTHOR="Pratik More"
DESCRIPTION="House price prediction model"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    It is going to return list of requirements mentioned in requirements.txt file
    return type is list of string 
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = PACKAGES,
    install_requires=get_requirements_list()
)