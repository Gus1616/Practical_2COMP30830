from setuptools import setup

setup(
    name="practical_two",
    version="1.0.0",
    description='Practical_2',
    packages=["systeminfo"],
    scripts=['bin/comp30670'],
    entry_points={
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
    )