"""
py-armodel - Python library for AUTOSAR model support.

This library provides ARXML parser and writer functionality for automotive
ECU software development.
"""

__version__ = "1.9.3"

from armodel import models as _models
from armodel.parser import ARXMLParser, FileListParser
from armodel.writer import ARXMLWriter

for _name in getattr(_models, "__all__", []):
    globals()[_name] = getattr(_models, _name)

_models_all = getattr(_models, "__all__", [])
__all__ = list(_models_all) + ["ARXMLParser", "FileListParser", "ARXMLWriter"]
