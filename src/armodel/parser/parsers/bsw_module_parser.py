"""
Parser for AUTOSAR BSW module elements.

Handles:
- BswModuleDescription
- BswInternalBehavior
- BswModuleEntity
- BswCalledEntity
- BswSchedulableEntity
- BswInterruptEntity
- BswImplementation
- BswModuleEntry
- BswModuleClientServerEntry
- BswModuleDependency
- BSW Events
- BSW Call Points (BswDirectCallPoint, BswSynchronousServerCallPoint,
  BswAsynchronousServerCallPoint, BswAsynchronousServerCallResultPoint)
"""
from ..base_arxml_parser import BaseARXMLParser


class BswModuleParser(BaseARXMLParser):
    """
    Parser for AUTOSAR BSW module elements.

    Handles basic software module descriptions, behaviors,
    implementations, and their interfaces.
    """

    def __init__(self, options=None):
        """Initialize BswModuleParser."""
        super().__init__(options)
