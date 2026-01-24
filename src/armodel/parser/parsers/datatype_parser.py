"""
Parser for AUTOSAR data type elements.

Handles:
- ApplicationDataType
- ImplementationDataType
- ApplicationRecordElement
- ApplicationArrayElement
- CompuMethod
- DataConstr
- Unit
- UnitGroup
- SwTextProps
- SwSystemconst
"""
from ..base_arxml_parser import BaseARXMLParser


class DataTypeParser(BaseARXMLParser):
    """
    Parser for AUTOSAR data type elements.

    Handles all data type definitions and related elements including
    application and implementation data types, compu-methods, units,
    and constraints.
    """

    def __init__(self, options=None):
        """Initialize DataTypeParser."""
        super().__init__(options)
