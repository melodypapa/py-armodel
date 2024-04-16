from setuptools import setup, find_packages
import sys
import os

with open("README.md", "r") as fh:
    long_description = fh.read() 

setup(
    name='armodel',
    version='1.2.0',
    description='the python arxml parser',

    url='http://github.com/melodypapa/py-armodel',
    author='melodypapa',
    author_email='melodypapa@outlook.com',

    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='AUTOSAR ARXML', 

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    python_requires=">=3.5",

    license='MIT',
	install_requires=[],
    include_package_data=True,
    zip_safe=False,

    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'arxml-dump = armodel.cli.arxml_dump_cli:cli_main',
        ]
    }
)