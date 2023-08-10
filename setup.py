from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    This function wll return the list of requirements
    '''
    HYPHEN_E_DOT = '-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
           
    return requirements        
setup(
 name='MLProject',
 version='0.0.1',
 author='DhaneshRamesh',
 author_email='dhaneshrameshofficial@gmail.com',
 packages=find_packages(),
 install_requires=get_requirements('requirements.txt')  
)