"""
This module contains the SwComponentType base class for AUTOSAR software components.
"""

from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwComponentType(AtpType, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is SwComponentType:
            raise TypeError("SwComponentType is an abstract class.")
        super().__init__(parent, short_name)

        self.ports = []
        self.portGroups = []

    def getPorts(self):
        return self.ports

    def createPPortPrototype(self, short_name: str):
        # Import here to avoid circular dependency
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PPortPrototype,
        )
        prototype = PPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype

    def createRPortPrototype(self, short_name):
        # Import here to avoid circular dependency
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            RPortPrototype,
        )
        prototype = RPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype

    def createPRPortPrototype(self, short_name):
        # Import here to avoid circular dependency
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PRPortPrototype,
        )
        prototype = PRPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype

    def getPPortPrototypes(self) -> List['PPortPrototype']:
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PPortPrototype,
        )
        return sorted(filter(lambda c: isinstance(c, PPortPrototype), self.ports), key=lambda o: o.short_name)

    def getRPortPrototypes(self) -> List['RPortPrototype']:
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            RPortPrototype,
        )
        return sorted(filter(lambda c: isinstance(c, RPortPrototype), self.ports), key=lambda o: o.short_name)

    def getPRPortPrototypes(self) -> List['PRPortPrototype']:
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PRPortPrototype,
        )
        return sorted(filter(lambda c: isinstance(c, PRPortPrototype), self.ports), key=lambda o: o.short_name)

    def getPortPrototypes(self) -> List['PortPrototype']:
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PortPrototype,
        )
        return sorted(filter(lambda c: isinstance(c, PortPrototype), self.ports), key=lambda o: o.short_name)

    def getPortGroups(self) -> List['PortGroup']:
        return self.portGroups

    def createPortGroup(self, short_name):
        # Import here to avoid circular dependency
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PortGroup,
        )
        port_group = PortGroup(self, short_name)
        self.addElement(port_group)
        self.portGroups.append(port_group)
        return port_group


__all__ = [
    'SwComponentType',
]
