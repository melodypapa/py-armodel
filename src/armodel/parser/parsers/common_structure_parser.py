"""
Parser for AUTOSAR CommonStructure elements.

Handles:
- ARObject (base attributes)
- Identifiable (short-name, category, desc)
- AdminData
- Documentation
- ServiceNeeds
"""
from ..base_arxml_parser import BaseARXMLParser


class CommonStructureParser(BaseARXMLParser):
    """
    Parser for AUTOSAR CommonStructure elements.

    Handles base attributes and common structures shared across all
    AUTOSAR elements including ARObject, Identifiable, and AdminData.
    """

    def __init__(self, options=None):
        """Initialize CommonStructureParser."""
        super().__init__(options)
