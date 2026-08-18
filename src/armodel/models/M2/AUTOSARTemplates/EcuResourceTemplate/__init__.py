"""
This module contains classes for representing AUTOSAR hardware element templates
in the EcuResourceTemplate module.

Hardware elements define the physical components of ECUs including pins, pin groups,
and connections between hardware elements.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import HwElementConnector
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinConnector import HwPinConnector as HwPinConnector
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinGroupConnector import HwPinGroupConnector as HwPinGroupConnector


class HwDescriptionEntity(Referrable):
    """
    This meta-class represents the ability to describe a hardware entity.
    """

    # HwDescriptionEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.1, p.15
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addHwAttributeValue          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHwAttributeValues         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addHwCategoryRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHwCategoryRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getHwTypeRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHwTypeRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        if type(self) is HwDescriptionEntity:
            raise TypeError("HwDescriptionEntity is an abstract class.")
        super().__init__(parent, short_name)

        # This aggregation represents a particular hardware attribute value.
        self.hwAttributeValues: List[HwAttributeValue] = []

        # One of the associations representing one particular category of the hardware entity.
        self.hwCategoryRefs: List[RefType] = []

        # This association is used to assign an optional HwType which contains the common attribute values for all occurences of this HwDescriptionEntity. Note that Hw Types can not be redefined and therefore shall not have a hwType reference.
        self.hwTypeRef: Optional[RefType] = None

    def addHwAttributeValue(self, value: HwAttributeValue):
        """
        This aggregation represents a particular hardware attribute value.

        A None value is a no-op and does not add an hwAttributeValue.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwAttributeValues.append(value)
        return self

    def getHwAttributeValues(self) -> List[HwAttributeValue]:
        """
        This aggregation represents a particular hardware attribute value.

        Returns:
            The list of hwAttributeValues, or an empty list if none are set
        """
        return self.hwAttributeValues

    def addHwCategoryRef(self, value: RefType):
        """
        One of the associations representing one particular category of the hardware entity.

        A None value is a no-op and does not add an hwCategoryRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwCategoryRefs.append(value)
        return self

    def getHwCategoryRefs(self) -> List[RefType]:
        """
        One of the associations representing one particular category of the hardware entity.

        Returns:
            The list of hwCategoryRefs, or an empty list if none are set
        """
        return self.hwCategoryRefs

    def getHwTypeRef(self) -> Optional[RefType]:
        """
        This association is used to assign an optional HwType which contains the common attribute values for all occurences of this HwDescriptionEntity. Note that Hw Types can not be redefined and therefore shall not have a hwType reference.

        Returns:
            The hwTypeRef, or None if not set
        """
        return self.hwTypeRef

    def setHwTypeRef(self, value: Optional[RefType]):
        """
        This association is used to assign an optional HwType which contains the common attribute values for all occurences of this HwDescriptionEntity. Note that Hw Types can not be redefined and therefore shall not have a hwType reference.

        A None value is a no-op and does not overwrite an existing hwTypeRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwTypeRef = value
        return self


class HwPin(HwDescriptionEntity):
    """
    This meta-class represents the possibility to describe a hardware pin.
    """

    # HwPin method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.7, p.20
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createFunctionName           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addFunctionName              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getFunctionNames             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setFunctionNames             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPackagingPinName          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPackagingPinName          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPinNumber                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPinNumber                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This attribute describes the function of the pin (e.g. CLK for Clock).
        self.functionNames: List[String] = []

        # This attribute contains the name of the pin according to the packaging of the hardware element (e.g. A03).
        self.packagingPinName: Optional[String] = None

        # This attribute contains the physical pin number.
        self.pinNumber: Optional[Integer] = None

    def createFunctionName(self, value: String) -> String:
        """This attribute describes the function of the pin (e.g. CLK for Clock)."""
        if value not in self.functionNames:
            self.functionNames.append(value)
        return value

    def addFunctionName(self, value: String) -> "HwPin":
        """This attribute describes the function of the pin (e.g. CLK for Clock)."""
        if value not in self.functionNames:
            self.functionNames.append(value)
        return self

    def getFunctionNames(self) -> List[String]:
        """This attribute describes the function of the pin (e.g. CLK for Clock)."""
        return self.functionNames

    def setFunctionNames(self, value: List[String]):
        """This attribute describes the function of the pin (e.g. CLK for Clock). Only sets the value if it is not None."""
        if value is not None:
            self.functionNames = value
        return self

    def getPackagingPinName(self) -> Optional[String]:
        """This attribute contains the name of the pin according to the packaging of the hardware element (e.g. A03)."""
        return self.packagingPinName

    def setPackagingPinName(self, value: String):
        """This attribute contains the name of the pin according to the packaging of the hardware element (e.g. A03). Only sets the value if it is not None."""
        if value is not None:
            self.packagingPinName = value
        return self

    def getPinNumber(self) -> Optional[Integer]:
        """This attribute contains the physical pin number."""
        return self.pinNumber

    def setPinNumber(self, value: Integer):
        """This attribute contains the physical pin number. Only sets the value if it is not None."""
        if value is not None:
            self.pinNumber = value
        return self


class HwPinGroupContent(ARObject):
    """
    Represents the content of a hardware pin group in AUTOSAR.
    This class links individual pins and pin groups together to form complex pin structures.

    Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.6, p.20
    Spec verified: R23-11
    Note: XSD defines atpMixed choice (HW-PIN-GROUP | HW-PIN), not a sequence. Multiplicity 0..1 for both fields.
    """

    # HwPinGroupContent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.6, p.20
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHwPin                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createHwPin                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHwPinGroup                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setHwPinGroup                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        """
        Initializes the HwPinGroupContent with default values.
        """
        super().__init__()

        self.hwPin: Optional["HwPin"] = None
        self.hwPinGroup: Optional["HwPinGroup"] = None

    def getHwPin(self) -> Optional["HwPin"]:
        """
        Gets the hardware pin in this pin group content.

        Returns:
            HwPin instance, or None if not set
        """
        return self.hwPin

    def createHwPin(self, short_name: str) -> "HwPin":
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

    def getHwPinGroup(self) -> Optional["HwPinGroup"]:
        """
        Gets the hardware pin group in this pin group content.

        Returns:
            HwPinGroup instance, or None if not set
        """
        return self.hwPinGroup

    def setHwPinGroup(self, value: "HwPinGroup"):
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

    Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.5, p.19
    Spec verified: R23-11
    Note: Represents a grouping of pins with optional content (HwPin or HwPinGroup).
    """

    # HwPinGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.5, p.19
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHwPinGroupContent         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setHwPinGroupContent         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

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

    # HwElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.4, p.18
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addHwElementConnection       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHwElementConnections      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createHwPinGroup             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHwPinGroups               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addNestedElementRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNestedElementRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This represents one particular connection between two hardware elements.
        self.hwElementConnections: List[HwElementConnector] = []

        # This aggregation is used to describe the connection facilities of a hardware element. Note that hardware element has no pins but only pingroups.
        self.hwPinGroups: List[HwPinGroup] = []

        # This association is used to establish hierarchies of hw elements. Note that one particular HwElement can be target of this association only once. I.e. multiple instantiation of the same HwElement is not supported (at any hierarchy level).
        self.nestedElementRefs: List[RefType] = []

    def getHwElementConnections(self) -> List[HwElementConnector]:
        """
        This represents one particular connection between two hardware elements.

        Returns:
            The list of hwElementConnections, or an empty list if none are set
        """
        return self.hwElementConnections

    def addHwElementConnection(self, value: HwElementConnector):
        """
        This represents one particular connection between two hardware elements.

        A None value is a no-op and does not add an hwElementConnection.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwElementConnections.append(value)
        return self

    def getHwPinGroups(self) -> List[HwPinGroup]:
        """
        This aggregation is used to describe the connection facilities of a hardware element. Note that hardware element has no pins but only pingroups.

        Returns:
            The list of hwPinGroups, or an empty list if none are set
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
        if not any(pin_group.getShortName() == short_name for pin_group in self.hwPinGroups):
            pin_group = HwPinGroup(self, short_name)
            self.hwPinGroups.append(pin_group)
        return next(pin_group for pin_group in self.hwPinGroups if pin_group.getShortName() == short_name)

    def getNestedElementRefs(self) -> List[RefType]:
        """
        This association is used to establish hierarchies of hw elements. Note that one particular HwElement can be target of this association only once. I.e. multiple instantiation of the same HwElement is not supported (at any hierarchy level).

        Returns:
            The list of nestedElementRefs, or an empty list if none are set
        """
        return self.nestedElementRefs

    def addNestedElementRef(self, value: RefType):
        """
        This association is used to establish hierarchies of hw elements. Note that one particular HwElement can be target of this association only once. I.e. multiple instantiation of the same HwElement is not supported (at any hierarchy level).

        A None value is a no-op and does not add a nestedElementRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nestedElementRefs.append(value)
        return self
