from setuptools import find_packages,setup
from typing import List

Hypen_E_Dot='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this  funtion will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]
            if Hypen_E_Dot in requirements:
                  requirements.remove(Hypen_E_Dot)


setup(
    name='MLProject',version='0.0.1',description='End to end ML',author='Sathish Kasinathan',
    author_email='sathishtechkasi@gmail.com',packages=find_packages(),
    install_requires=get_requirements('requirements.txt')



)