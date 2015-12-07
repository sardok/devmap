import devmap
from setuptools import setup, find_packages


setup(
    name='devmap',
    version=devmap.__version__,
    packages=find_packages(),
    py_modules=['devmap'],
    license='MIT',
)
