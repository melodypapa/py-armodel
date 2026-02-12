"""
Ecu Resource Template package.

This module defines hardware description classes for AUTOSAR ECU resources.

Package: M2::AUTOSARTemplates::EcuResourceTemplate
"""

from typing import TYPE_CHECKING, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import (
        HwAttributeValue,
    )
    from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwCategory import (
        HwCategory,
    )
    from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwType import (
        HwType,
    )


class HwDescriptionEntity(Referrable):
    """
    This meta-class represents the ability to describe a hardware entity.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 15, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 990, Classic Platform R23-11)
    """

    def __init__(self) -> None:
        super().__init__()

        self.hw_attributes: List["HwAttributeValue"] = []
        self.hw_categories: List["HwCategory"] = []
        self.hw_type: Optional["HwType"] = None

    def getHwAttributes(self) -> List["HwAttributeValue"]:
        """Get hardware attributes."""
        return self.hw_attributes

    def setHwAttributes(self, value: List["HwAttributeValue"]) -> "HwDescriptionEntity":
        """Set hardware attributes."""
        self.hw_attributes = value
        return self

    def getHwCategories(self) -> List["HwCategory"]:
        """Get hardware categories."""
        return self.hw_categories

    def setHwCategories(self, value: List["HwCategory"]) -> "HwDescriptionEntity":
        """Set hardware categories."""
        self.hw_categories = value
        return self

    def getHwType(self) -> Optional["HwType"]:
        """Get hardware type."""
        return self.hw_type

    def setHwType(self, value: Optional["HwType"]) -> "HwDescriptionEntity":
        """Set hardware type."""
        self.hw_type = value
        return self


class HwElement(HwDescriptionEntity):
    """
    This represents the ability to describe Hardware Elements on an instance level.
    The particular types of hardware are distinguished by the category.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 296, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 18, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 991, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2026, Classic Platform R23-11)
    """

    def __init__(self) -> None:
        super().__init__()

        self.hw_elements: List["HwElementConnector"] = []
        self.hw_pin_groups: List["HwPinGroup"] = []
        self.nested_elements: List["HwElement"] = []

    def getHwElements(self) -> List["HwElementConnector"]:
        """Get hardware element connections."""
        return self.hw_elements

    def setHwElements(self, value: List["HwElementConnector"]) -> "HwElement":
        """Set hardware element connections."""
        self.hw_elements = value
        return self

    def getHwPinGroups(self) -> List["HwPinGroup"]:
        """Get hardware pin groups."""
        return self.hw_pin_groups

    def setHwPinGroups(self, value: List["HwPinGroup"]) -> "HwElement":
        """Set hardware pin groups."""
        self.hw_pin_groups = value
        return self

    def getNestedElements(self) -> List["HwElement"]:
        """Get nested elements."""
        return self.nested_elements

    def setNestedElements(self, value: List["HwElement"]) -> "HwElement":
        """Set nested elements."""
        self.nested_elements = value
        return self


class HwPinGroup(Identifiable):
    """
    This class represents a hardware pin group.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate
    """

    def __init__(self) -> None:
        super().__init__()

        self.hw_pin_group_contents: List["HwPinGroupContent"] = []

    def getHwPinGroupContents(self) -> List["HwPinGroupContent"]:
        """Get pin group contents."""
        return self.hw_pin_group_contents

    def setHwPinGroupContents(self, value: List["HwPinGroupContent"]) -> "HwPinGroup":
        """Set pin group contents."""
        self.hw_pin_group_contents = value
        return self


class HwPinGroupContent(ARObject):
    """
    This class represents content within a hardware pin group.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate
    """

    def __init__(self) -> None:
        super().__init__()

        self.hw_pin: Optional["HwPin"] = None

    def getHwPin(self) -> Optional["HwPin"]:
        """Get hardware pin."""
        return self.hw_pin

    def setHwPin(self, value: Optional["HwPin"]) -> "HwPinGroupContent":
        """Set hardware pin."""
        self.hw_pin = value
        return self


class HwPin(HwDescriptionEntity):
    """
    This class represents a hardware pin.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate
    """

    def __init__(self) -> None:
        super().__init__()


class HwElementConnector(ARObject):
    """
    This class represents a connection between hardware elements.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate
    """

    def __init__(self) -> None:
        super().__init__()

        self.source: Optional["HwElement"] = None
        self.target: Optional["HwElement"] = None

    def getSource(self) -> Optional["HwElement"]:
        """Get source element."""
        return self.source

    def setSource(self, value: Optional["HwElement"]) -> "HwElementConnector":
        """Set source element."""
        self.source = value
        return self

    def getTarget(self) -> Optional["HwElement"]:
        """Get target element."""
        return self.target

    def setTarget(self, value: Optional["HwElement"]) -> "HwElementConnector":
        """Set target element."""
        self.target = value
        return self


class HwPinGroupConnector(ARObject):
    """
    This class represents a connection between hardware pin groups.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate
    """

    def __init__(self) -> None:
        super().__init__()

        self.source: Optional["HwPinGroup"] = None
        self.target: Optional["HwPinGroup"] = None

    def getSource(self) -> Optional["HwPinGroup"]:
        """Get source pin group."""
        return self.source

    def setSource(self, value: Optional["HwPinGroup"]) -> "HwPinGroupConnector":
        """Set source pin group."""
        self.source = value
        return self

    def getTarget(self) -> Optional["HwPinGroup"]:
        """Get target pin group."""
        return self.target

    def setTarget(self, value: Optional["HwPinGroup"]) -> "HwPinGroupConnector":
        """Set target pin group."""
        self.target = value
        return self


class HwPinConnector(ARObject):
    """
    This class represents a connection between hardware pins.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate
    """

    def __init__(self) -> None:
        super().__init__()

        self.source: Optional["HwPin"] = None
        self.target: Optional["HwPin"] = None

    def getSource(self) -> Optional["HwPin"]:
        """Get source pin."""
        return self.source

    def setSource(self, value: Optional["HwPin"]) -> "HwPinConnector":
        """Set source pin."""
        self.source = value
        return self

    def getTarget(self) -> Optional["HwPin"]:
        """Get target pin."""
        return self.target

    def setTarget(self, value: Optional["HwPin"]) -> "HwPinConnector":
        """Set target pin."""
        self.target = value
        return self


__all__ = [
    "HwDescriptionEntity",
    "HwElement",
    "HwPinGroup",
    "HwPinGroupContent",
    "HwPin",
    "HwElementConnector",
    "HwPinGroupConnector",
    "HwPinConnector",
]
