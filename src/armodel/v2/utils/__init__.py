"""
V2 Utilities - shared utilities for V2 modules.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- Custom error types (ReadError, WriteError)
- Context management for reading/writing operations
"""
from armodel.v2.utils.context import DeserializationContext
from armodel.v2.utils.errors import ReadError

__version__ = "2.0.0"
__all__ = ["ReadError", "DeserializationContext"]
