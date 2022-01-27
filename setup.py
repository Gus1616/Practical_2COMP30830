from setuptools import setup

setup(
    name="practical_two",
    version="1.0.0",
    description='Practical_2',
    packages=["Practical_2COMP30830"],
    entry_points={
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
    zip_safe=False)