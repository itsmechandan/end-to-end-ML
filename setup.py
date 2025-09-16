###This file is essential for making your project installable and distributable as a Python package.
#It contains metadata about your project, such as its name, version, and dependencies. When someone runs pip install . 
#in your project's directory, setup.py tells pip how to build and install the package.

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='chandan',
author_email='jakkavenkatchandan@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)