"""
Shared utilities for armodel modules.

This module provides utilities that can be used by both V1 and V2.
"""
from armodel.utils.context import DeserializationContext
from armodel.utils.errors import ReadError

# Note: UUIDMgr uses V2 ARObject, import it directly:
# from armodel.utils.uuid_mgr import UUIDMgr

__all__ = ["ReadError", "DeserializationContext"]
