"""
This module contains the SwComponentType base class for AUTOSAR software components.
"""

from abc import ABC
from typing import List, TYPE_CHECKING
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

if TYPE_CHECKING:
    from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype, RPortPrototype, PRPortPrototype, PortPrototype, PortGroup


class SwComponentType(AtpType, ABC):
    """
    Abstract base class for all software component types in AUTOSAR.
    Provides port and port group management.
    """

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is SwComponentType:
            raise TypeError("SwComponentType is an abstract class.")
        super().__init__(parent, short_name)

        self.ports = []
        self.portGroups = []

    def getPorts(self):
        """
        Gets the list of all ports.

        Returns:
            The list of ports
        """
        return self.ports

    def createPPortPrototype(self, short_name: str):
        """
        Creates and adds a PPortPrototype.

        Args:
            short_name: The short name for the port prototype

        Returns:
            PPortPrototype: The created port prototype
        """
        # Import here to avoid circular dependency
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
        prototype = PPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype

    def createRPortPrototype(self, short_name):
        """
        Creates and adds an RPortPrototype.

        Args:
            short_name: The short name for the port prototype

        Returns:
            RPortPrototype: The created port prototype
        """
        # Import here to avoid circular dependency
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import RPortPrototype
        prototype = RPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype

    def createPRPortPrototype(self, short_name):
        """
        Creates and adds a PRPortPrototype.

        Args:
            short_name: The short name for the port prototype

        Returns:
            PRPortPrototype: The created port prototype
        """
        # Import here to avoid circular dependency
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype
        prototype = PRPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype

    def getPPortPrototypes(self) -> List['PPortPrototype']:
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
        return list(sorted(filter(lambda c: isinstance(c, PPortPrototype), self.ports), key=lambda o: o.short_name))

    def getRPortPrototypes(self) -> List['RPortPrototype']:
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import RPortPrototype
        return list(sorted(filter(lambda c: isinstance(c, RPortPrototype), self.ports), key=lambda o: o.short_name))

    def getPRPortPrototypes(self) -> List['PRPortPrototype']:
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype
        return list(sorted(filter(lambda c: isinstance(c, PRPortPrototype), self.ports), key=lambda o: o.short_name))

    def getPortPrototypes(self) -> List['PortPrototype']:
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype
        return list(sorted(filter(lambda c: isinstance(c, PortPrototype), self.ports), key=lambda o: o.short_name))

    def getPortGroups(self) -> List['PortGroup']:
        """
        Gets the list of port groups.

        Returns:
            List[PortGroup]: The list of port groups
        """
        return self.portGroups

    def createPortGroup(self, short_name):
        """
        Creates and adds a PortGroup.

        Args:
            short_name: The short name for the port group

        Returns:
            PortGroup: The created port group
        """
        # Import here to avoid circular dependency
        from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import PortGroup
        port_group = PortGroup(self, short_name)
        self.addElement(port_group)
        self.portGroups.append(port_group)
        return port_group
