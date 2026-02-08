"""
V2 ARXML Reader - deserializes ARXML to model objects.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- Reflection-based element handling (CODING_RULE_V2_00015)
- XSD-driven schema mappings (CODING_RULE_V2_00004)
"""
from armodel.v2.reader.base_reader import ARXMLReader
from armodel.v2.reader.element_handler import ElementHandler
from armodel.v2.reader.schema_registry import SchemaRegistry

__version__ = "2.0.0"
__all__ = ["ARXMLReader", "SchemaRegistry", "ElementHandler"]
