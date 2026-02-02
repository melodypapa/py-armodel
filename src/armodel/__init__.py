"""
py-armodel - Python library for AUTOSAR model support.

This library provides ARXML parser and writer functionality for automotive
ECU software development.
"""

__version__ = "1.9.2"

# Import all model classes for direct access
from armodel.models import *
from armodel.parser import ARXMLParser, FileListParser
from armodel.writer import ARXMLWriter

# Export all model classes plus parser/writer
import armodel.models
_models_all = getattr(armodel.models, '__all__', [])
__all__ = list(_models_all) + ["ARXMLParser", "FileListParser", "ARXMLWriter"]
