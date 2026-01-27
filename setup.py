''' The setup.py is an essential part of packaging and distributing python projects. 
It is used by setup tools(or distutils  in older python version) to define the configuration of project,
such as metadeta, dependencies and all'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() ->List[str]:
    ''' This function will return list of requirements'''
    requirement_list:List[str] =[]
    try:
        with open('requirements.txt','r')as file:
            # Read lines from the file
            lines = file.readlines()
            #Process each line 
            for line in lines:
                requirement=line.strip()
                # ignore empty linesn and -e.
                if requirement and requirement != '-e.':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("Requirements.txt not found")

    return requirement_list

setup(
    name = "Network Security against phising using ML",
    version = "0.0.1",
    author="Rishabh",
    author_email="rishabhchamoli0120@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()

)