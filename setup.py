from setuptools import setup, find_packages
from typing import List

# Project details
PROJECT_NAME = 'Text Summarization'
VERSION = '0.0.0'
AUTHOR_NAME = 'Anas Malik'
AUTHOR_EMAIL = 'anasmalik081@gmail.com'

# get dependendcies
def get_requirements(file_path: str)->List[str]:
    """
    This function returns the list of requirements for this package

    Inputs: file path
    Output: list of required libraries or packages
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
        
    return requirements

# creating a setup
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)