import glob
import subprocess
from setuptools import setup, find_packages, Extension


def build_libs():
    subprocess.call(['cmake', '.'])
    subprocess.call(['make'])
    

build_libs()


setup(
    name='pyamze',
    version='1.0.2',
    description='An open-source robot based on NVIDIA Jetson Nano',
    packages=find_packages(),
#    install_requires=[
#        'tkinter',   # install using sudo apt install python3-tk
#    ],
#    dependency_links = ['http://github.com/mtai/python-gearman/tarball/master#egg=gearman-2.0.0beta']

)
