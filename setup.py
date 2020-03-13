
from setuptools import setup, find_packages
import pymms

setup(
    name='pymms',
    version=pymms.__version__,
    description='Simulation of the Minkowski metric  for Python',
    license='MIT',
    author='Vasyliy I. Gurianov',
    author_email='vg2007sns@rambler.ru',
    url='https://vgurianov.github.io/srt/mms/',    
    packages=find_packages(exclude=['experiments']),
    install_requires=[
        'matplotlib ==2.2.4'
    ],
    long_description=open('README.md').read(),
    zip_safe=False,
    test_suite='test',
    python_requires='==2.7',
)
