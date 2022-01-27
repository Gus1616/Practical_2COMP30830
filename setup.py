from setuptools import setup

setup(
    name="practical_two",
    version="1.0.0",
    description='Practical_2',
    url='https://github.com/Gus1616/Practical_2COMP30830',
    packages=["systeminfo"],
    scripts=['bin/comp303830_systeminfo'],
    entry_points={
        'console_scripts':['comp30380_systeminfo=systeminfo.main:main']
        }
    )
