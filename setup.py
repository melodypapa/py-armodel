from setuptools import setup, find_packages
import sys
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='armodel',
    version='1.8.5',
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

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    python_requires=">=3.5",

    license='MIT',
    install_requires=['colorama', 'openpyxl', "lxml"],
    include_package_data=True,
    zip_safe=False,

    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'format-xml                 = armodel.cli.format_xml_cli:main',
            'arxml-dump                 = armodel.cli.arxml_dump_cli:cli_main',
            'arxml-format               = armodel.cli.arxml_format_cli:main',
            'connector2xlsx             = armodel.cli.connector2xlsx_cli:main',
            'connector-update           = armodel.cli.connector_update_cli:main',
            'armodel-component          = armodel.cli.swc_list_cli:main',
            'armodel-system-signal      = armodel.cli.system_signal_cli:main',
            'armodel-memory-section     = armodel.cli.memory_section_cli:main',
            'armodel-file-list          = armodel.cli.file_list_cli:main',
            'armodel-uuid-checker       = armodel.cli.uuid_checker_cli:main',
        ]
    }
)
