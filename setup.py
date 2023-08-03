from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[requirement.replace('\n','') for requirement in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    
setup(
    name='ML Project',
    version='0.0.1',
    description='Student Performance in Exams - ML Project',
    author='Nikhil Patil',
    author_email='patilnikhil3586@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)