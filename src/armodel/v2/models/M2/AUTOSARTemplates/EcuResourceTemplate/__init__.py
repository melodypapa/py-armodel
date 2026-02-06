"""
This module contains classes for representing AUTOSAR hardware element templates
in the EcuResourceTemplate module.

Hardware elements define the physical components of ECUs including pins, pin groups,
and connections between hardware elements.
"""

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import (
    HwElementConnector,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
    String,
)


class HwDescriptionEntity(ARElement):
    """
    Abstract base class for hardware description entities in AUTOSAR.
    This class defines common properties for hardware elements including attribute values and type references.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwDescriptionEntity with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware description entity
            short_name: The unique short name of this hardware description entity
        """
        super().__init__(parent, short_name)

        self.hwAttributeValues: List[HwAttributeValue] = []
        self.hwCategoryRefs: List[RefType] = []
        self.hwTypeRef: Optional[RefType] = None

    def getHwAttributeValues(self) -> List[HwAttributeValue]:
        """
        Gets the list of hardware attribute values for this entity.

        Returns:
            List of HwAttributeValue instances
        """
        return self.hwAttributeValues

    def setHwAttributeValues(self, value: List[HwAttributeValue]):
        """
        Sets the list of hardware attribute values for this entity.
        Only sets the value if it is not None.

        Args:
            value: The list of hardware attribute values to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwAttributeValues = value
        return self

    def getHwCategoryRefs(self) -> List[RefType]:
        """
        Gets the list of hardware category references for this entity.

        Returns:
            List of RefType instances representing hardware category references
        """
        return self.hwCategoryRefs

    def addHwCategoryRef(self, value: RefType):
        """
        Adds a hardware category reference to this entity.
        Only adds the value if it is not None.

        Args:
            value: The hardware category reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwCategoryRefs.append(value)
        return self

    def getHwTypeRef(self) -> Optional[RefType]:
        """
        Gets the hardware type reference for this entity.

        Returns:
            RefType representing the hardware type reference, or None if not set
        """
        return self.hwTypeRef

    def setHwTypeRef(self, value: RefType):
        """
        Sets the hardware type reference for this entity.
        Only sets the value if it is not None.

        Args:
            value: The hardware type reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwTypeRef = value
        return self


class HwPin(HwDescriptionEntity):
    """
    Represents a hardware pin in AUTOSAR hardware descriptions.
    This class defines the properties of individual hardware pins including function names and pin numbers.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwPin with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware pin
            short_name: The unique short name of this hardware pin
        """
        super().__init__(parent, short_name)

        self.functionName: Optional[String] = None
        self.packagingPinName: Optional[String] = None
        self.pinNumber: Optional[Integer] = None

    def getFunctionName(self) -> Optional[String]:
        """
        Gets the function name of this hardware pin.

        Returns:
            String representing the function name, or None if not set
        """
        return self.functionName

    def setFunctionName(self, value: String):
        """
        Sets the function name of this hardware pin.
        Only sets the value if it is not None.

        Args:
            value: The function name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.functionName = value
        return self

    def getPackagingPinName(self) -> Optional[String]:
        """
        Gets the packaging pin name of this hardware pin.

        Returns:
            String representing the packaging pin name, or None if not set
        """
        return self.packagingPinName

    def setPackagingPinName(self, value: String):
        """
        Sets the packaging pin name of this hardware pin.
        Only sets the value if it is not None.

        Args:
            value: The packaging pin name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.packagingPinName = value
        return self

    def getPinNumber(self) -> Optional[Integer]:
        """
        Gets the pin number of this hardware pin.

        Returns:
            Integer representing the pin number, or None if not set
        """
        return self.pinNumber

    def setPinNumber(self, value: Integer):
        """
        Sets the pin number of this hardware pin.
        Only sets the value if it is not None.

        Args:
            value: The pin number to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.pinNumber = value
        return self


class HwPinGroupContent(ARObject):
    """
    Represents the content of a hardware pin group in AUTOSAR.
    This class links individual pins and pin groups together to form complex pin structures.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        """
        Initializes the HwPinGroupContent with default values.
        """
        super().__init__()

        self.hwPin: Optional['HwPin'] = None
        self.hwPinGroup: Optional['HwPinGroup'] = None

    def getHwPin(self) -> Optional['HwPin']:
        """
        Gets the hardware pin in this pin group content.

        Returns:
            HwPin instance, or None if not set
        """
        return self.hwPin

    def createHwPin(self, short_name: str) -> 'HwPin':
        """
        Creates a new hardware pin in this pin group content.

        Args:
            short_name: The short name for the new hardware pin

        Returns:
            The created HwPin instance
        """
        pin = HwPin(self, short_name)
        self.hwPin = pin
        return pin

    def getHwPinGroup(self) -> Optional['HwPinGroup']:
        """
        Gets the hardware pin group in this pin group content.

        Returns:
            HwPinGroup instance, or None if not set
        """
        return self.hwPinGroup

    def setHwPinGroup(self, value: 'HwPinGroup'):
        """
        Sets the hardware pin group in this pin group content.
        Only sets the value if it is not None.

        Args:
            value: The hardware pin group to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwPinGroup = value
        return self


class HwPinGroup(HwDescriptionEntity):
    """
    Represents a group of hardware pins in AUTOSAR hardware descriptions.
    This class defines collections of related hardware pins with associated content.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwPinGroup with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware pin group
            short_name: The unique short name of this hardware pin group
        """
        super().__init__(parent, short_name)

        self.hwPinGroupContent: Optional[HwPinGroupContent] = None

    def getHwPinGroupContent(self) -> Optional[HwPinGroupContent]:
        """
        Gets the pin group content for this hardware pin group.

        Returns:
            HwPinGroupContent instance, or None if not set
        """
        return self.hwPinGroupContent

    def setHwPinGroupContent(self, value: HwPinGroupContent):
        """
        Sets the pin group content for this hardware pin group.
        Only sets the value if it is not None.

        Args:
            value: The pin group content to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwPinGroupContent = value
        return self


class HwElement(HwDescriptionEntity):
    """
    Represents a hardware element in AUTOSAR hardware descriptions.
    This class defines complete hardware components with connections, pin groups, and nested elements.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwElement with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware element
            short_name: The unique short name of this hardware element
        """
        super().__init__(parent, short_name)

        self.hwElementConnections: List[HwElementConnector] = []
        self.hwPinGroups: List[HwPinGroup] = []
        self.nestedElementRefs: List[RefType] = []

    def getHwElementConnections(self) -> List[HwElementConnector]:
        """
        Gets the list of hardware element connections for this element.

        Returns:
            List of HwElementConnector instances
        """
        return self.hwElementConnections

    def setHwElementConnections(self, value: List[HwElementConnector]):
        """
        Sets the list of hardware element connections for this element.
        Only sets the value if it is not None.

        Args:
            value: The list of hardware element connections to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwElementConnections = value
        return self

    def getHwPinGroups(self) -> List[HwPinGroup]:
        """
        Gets the list of hardware pin groups for this element.

        Returns:
            List of HwPinGroup instances
        """
        return self.hwPinGroups

    def createHwPinGroup(self, short_name: str) -> HwPinGroup:
        """
        Creates and adds a new hardware pin group to this element.

        Args:
            short_name: The short name for the new hardware pin group

        Returns:
            The created HwPinGroup instance
        """
        if (not self.IsElementExists(short_name)):
            pin_group = HwPinGroup(self, short_name)
            self.addElement(pin_group)
            self.hwPinGroups.append(pin_group)
        return self.getElement(short_name)

    def getNestedElementRefs(self) -> List[RefType]:
        """
        Gets the list of nested element references for this element.

        Returns:
            List of RefType instances representing nested element references
        """
        return self.nestedElementRefs

    def setNestedElementRefs(self, value: List[RefType]):
        """
        Sets the list of nested element references for this element.
        Only sets the value if it is not None.

        Args:
            value: The list of nested element references to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nestedElementRefs = value
        return self


__all__ = []
