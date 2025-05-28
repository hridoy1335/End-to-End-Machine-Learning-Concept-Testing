from typing import List
from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."
def get_install_requires() -> List[str]:
    with open('requirements.txt','r') as f:
        require_list = [line.strip() for line in f.readlines()]
        if HYPEN_E_DOT in require_list:
            require_list.remove(HYPEN_E_DOT)
            
            return require_list
setup(
    name="sensor",
    version="0.0.1",
    description="this is demo",
    author="hridoy khan",
    author_email="rkhridoyinfo@gmail.com",
    packages=find_packages(),
    install_requires=get_install_requires()
)