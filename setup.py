from setuptools import setup

setup(
    name="practical_two",
    version="1.0.0",
    description='Practical_2',
    packages=["systeminfo"],
    scripts=['bin/comp303830_systeminfo'],
    entry_points={
        'console_scripts':['comp30380_systeminfo=systeminfo.main:main']
        }
    )