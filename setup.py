import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "LCD_ORANGEPI",
    version = "0.0.1",
    author = "Hamed Torky",
    author_email = "hamedtorky2@gmail.com",
    description = ("LCD 16x[1,2,3,4] i2c connect "),
    license = "AVA",
    keywords = "LCD 16x2 i2c",
    url = "",
    packages=['LCD_ORANGEPI', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: AVA License",
    ],
)
