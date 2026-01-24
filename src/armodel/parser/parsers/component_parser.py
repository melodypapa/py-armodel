"""
Parser for AUTOSAR software component elements.

Handles:
- ApplicationSwComponentType
- CompositionSwComponentType
- SensorActuatorSwComponentType
- ServiceSwComponentType
- ComplexDeviceDriverSwComponentType
- EcuAbstractionSwComponentType
- ServiceProxySwComponentType
- NvBlockSwComponentType
- SwConnector (AssemblySwConnector, DelegationSwConnector)
"""
from ..base_arxml_parser import BaseARXMLParser


class ComponentParser(BaseARXMLParser):
    """
    Parser for AUTOSAR software component elements.

    Handles all software component types and their connectors,
    including atomic and composition components.
    """

    def __init__(self, options=None):
        """Initialize ComponentParser."""
        super().__init__(options)
