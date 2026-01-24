"""
Parser for AUTOSAR port interface elements.

Handles:
- SenderReceiverInterface
- ClientServerInterface
- ModeSwitchInterface
- ParameterInterface
- NvDataInterface
- TriggerInterface
- ServiceInterface
- DiagnosticInterface variants
"""
from ..base_arxml_parser import BaseARXMLParser


class PortInterfaceParser(BaseARXMLParser):
    """
    Parser for AUTOSAR port interface elements.

    Handles all port interface types that define communication patterns
    between software components.
    """

    def __init__(self, options=None):
        """Initialize PortInterfaceParser."""
        super().__init__(options)
