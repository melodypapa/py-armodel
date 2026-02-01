"""
py-armodel - Python library for AUTOSAR model support.

This library provides ARXML parser and writer functionality for automotive
ECU software development.
"""

__version__ = "1.9.1"

from armodel.models import AUTOSAR
from armodel.parser import ARXMLParser, FileListParser
from armodel.writer import ARXMLWriter

__all__ = [
    "AUTOSAR",
    "ARXMLParser",
    "FileListParser",
    "ARXMLWriter",
]