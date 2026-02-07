"""
V2 Models - Extensible AUTOSAR model classes.

V2 Implementation:
- Extensible design for V2 modules (CODING_RULE_V2_00014)
- Module integration contract (CODING_RULE_V2_00015)
- Modern Python patterns with type hints
- Extended attributes for custom V2 module properties

Exports:
- ARObject: Base class for all AUTOSAR objects (extensible)
- AUTOSAR: Root element with singleton pattern
- Identifiable: Base class for identifiable objects
- ARPackage: AUTOSAR package container

Usage:
    from armodel.v2.models import AUTOSAR, ARPackage

    # Get singleton instance
    autosar = AUTOSAR.getInstance()

    # Create package using extensible design
    pkg = ARPackage()
    pkg.setShortName("MyPackage")

    # Use extended attributes for custom properties
    pkg.setExtendedAttribute("vendor", "MyCompany")
    vendor = pkg.getExtendedAttribute("vendor")
"""
from .ar_object import ARObject
from .models import (
    AUTOSAR,
    ARPackage,
    Identifiable,
)

__version__ = "2.0.0"

__all__ = [
    "ARObject",
    "AUTOSAR",
    "ARPackage",
    "Identifiable",
    "__version__",
]
