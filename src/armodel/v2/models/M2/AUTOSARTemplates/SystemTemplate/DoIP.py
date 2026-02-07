# This module contains AUTOSAR System Template classes for DoIP (Diagnostics over IP)
# It defines logic address properties and configurations for DoIP communication

from abc import ABC
from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class AbstractDoIpLogicAddressProps(Identifiable, ABC):
    """
    Abstract base class for DoIP (Diagnostics over IP) logic address properties.
    This class defines the common properties for DoIP address configurations,
    serving as the foundation for specific DoIP address types in the system.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is AbstractDoIpLogicAddressProps:
            raise TypeError("AbstractDoIpLogicAddressProps is an abstract class.")

        super().__init__(parent, short_name)


class DoIpLogicTargetAddressProps(AbstractDoIpLogicAddressProps):
    """
    Defines properties for DoIP (Diagnostics over IP) logic target addresses,
    specifying how diagnostic messages should be addressed to target ECUs
    in the IP-based diagnostic communication system.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """
    Defines properties for DoIP (Diagnostics over IP) logic tester addresses,
    specifying how diagnostic tools and testers are addressed in the IP-based
    diagnostic communication system, including routing activation references.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.doIpTesterRoutingActivationRef: Union[Union[RefType, None] , None] = None

    def getDoIpTesterRoutingActivationRef(self):
        return self.doIpTesterRoutingActivationRef

    def setDoIpTesterRoutingActivationRef(self, value):
        if value is not None:
            self.doIpTesterRoutingActivationRef = value
        return self


__all__ = [
    "AbstractDoIpLogicAddressProps",
    "DoIpLogicTargetAddressProps",
    "DoIpLogicTesterAddressProps",
]
