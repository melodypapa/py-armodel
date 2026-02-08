"""
V2 ARXML Writer - serializes model objects to ARXML files.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- Reflection-based serialization (CODING_RULE_V2_00015)
- Model integration contract compliance (CODING_RULE_V2_00015)
"""
from armodel.v2.writer.base_writer import ARXMLWriter

__version__ = "2.0.0"
__all__ = ["ARXMLWriter"]
