"""
AUTOSAR Package - EcuResourceTemplate

Package: M2::AUTOSARTemplates::EcuResourceTemplate
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.__init__ import (
    HwDescriptionEntity,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Identifiable,
    Referrable,
)




class HwDescriptionEntity(Referrable, ABC):
    """
    This meta-class represents the ability to describe a hardware entity.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwDescriptionEntity
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 15, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 990, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is HwDescriptionEntity:
            raise TypeError("HwDescriptionEntity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents a particular hardware value.
        # atpVariation.
        self._hwAttribute: List["HwAttributeValue"] = []

    @property
    def hw_attribute(self) -> List["HwAttributeValue"]:
        """Get hwAttribute (Pythonic accessor)."""
        return self._hwAttribute
        # One of the associations representing one particular the hardware entity.
        self._hwCategory: List["HwCategory"] = []

    @property
    def hw_category(self) -> List["HwCategory"]:
        """Get hwCategory (Pythonic accessor)."""
        return self._hwCategory
        # This association is used to assign an optional HwType the common attribute
                # values for all this HwDescriptionEntity.
        # Note that Hw not be redefined and therefore shall not have a.
        self._hwType: Optional["HwType"] = None

    @property
    def hw_type(self) -> Optional["HwType"]:
        """Get hwType (Pythonic accessor)."""
        return self._hwType

    @hw_type.setter
    def hw_type(self, value: Optional["HwType"]) -> None:
        """
        Set hwType with validation.
        
        Args:
            value: The hwType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwType = None
            return

        if not isinstance(value, HwType):
            raise TypeError(
                f"hwType must be HwType or None, got {type(value).__name__}"
            )
        self._hwType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwAttribute(self) -> List["HwAttributeValue"]:
        """
        AUTOSAR-compliant getter for hwAttribute.
        
        Returns:
            The hwAttribute value
        
        Note:
            Delegates to hw_attribute property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute  # Delegates to property

    def getHwCategory(self) -> List["HwCategory"]:
        """
        AUTOSAR-compliant getter for hwCategory.
        
        Returns:
            The hwCategory value
        
        Note:
            Delegates to hw_category property (CODING_RULE_V2_00017)
        """
        return self.hw_category  # Delegates to property

    def getHwType(self) -> "HwType":
        """
        AUTOSAR-compliant getter for hwType.
        
        Returns:
            The hwType value
        
        Note:
            Delegates to hw_type property (CODING_RULE_V2_00017)
        """
        return self.hw_type  # Delegates to property

    def setHwType(self, value: "HwType") -> "HwDescriptionEntity":
        """
        AUTOSAR-compliant setter for hwType with method chaining.
        
        Args:
            value: The hwType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_type property setter (gets validation automatically)
        """
        self.hw_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_hw_type(self, value: Optional["HwType"]) -> "HwDescriptionEntity":
        """
        Set hwType and return self for chaining.
        
        Args:
            value: The hwType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_type("value")
        """
        self.hw_type = value  # Use property setter (gets validation)
        return self



class HwPinGroup(Identifiable):
    """
    This meta-class represents the ability to describe groups of pins which are
    used to connect hardware elements. This group acts as a bundle of pins.
    Thereby they allow to describe high level connections. Pin groups can even
    be nested.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPinGroup
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 19, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2027, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation describes the contained pins/pin groups.
        self._hwPinGroup: Optional["RefType"] = None

    @property
    def hw_pin_group(self) -> Optional["RefType"]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup

    @hw_pin_group.setter
    def hw_pin_group(self, value: Optional["RefType"]) -> None:
        """
        Set hwPinGroup with validation.
        
        Args:
            value: The hwPinGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwPinGroup = None
            return

        self._hwPinGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwPinGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    def setHwPinGroup(self, value: "RefType") -> "HwPinGroup":
        """
        AUTOSAR-compliant setter for hwPinGroup with method chaining.
        
        Args:
            value: The hwPinGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_pin_group property setter (gets validation automatically)
        """
        self.hw_pin_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_hw_pin_group(self, value: Optional[RefType]) -> "HwPinGroup":
        """
        Set hwPinGroup and return self for chaining.
        
        Args:
            value: The hwPinGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_pin_group("value")
        """
        self.hw_pin_group = value  # Use property setter (gets validation)
        return self



class HwPinGroupContent(ARObject):
    """
    This meta-class specifies a mixture of hwPins and hwPinGroups.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPinGroupContent
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 20, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents a hardware pin in a hardware atpVariation.
        self._hwPin: Optional["HwPin"] = None

    @property
    def hw_pin(self) -> Optional["HwPin"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin

    @hw_pin.setter
    def hw_pin(self, value: Optional["HwPin"]) -> None:
        """
        Set hwPin with validation.
        
        Args:
            value: The hwPin to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwPin = None
            return

        if not isinstance(value, HwPin):
            raise TypeError(
                f"hwPin must be HwPin or None, got {type(value).__name__}"
            )
        self._hwPin = value
        # This aggregation represents a nested hardware pin group.
        # atpVariation.
        self._hwPinGroup: Optional["RefType"] = None

    @property
    def hw_pin_group(self) -> Optional["RefType"]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup

    @hw_pin_group.setter
    def hw_pin_group(self, value: Optional["RefType"]) -> None:
        """
        Set hwPinGroup with validation.
        
        Args:
            value: The hwPinGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwPinGroup = None
            return

        self._hwPinGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwPin(self) -> "HwPin":
        """
        AUTOSAR-compliant getter for hwPin.
        
        Returns:
            The hwPin value
        
        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    def setHwPin(self, value: "HwPin") -> "HwPinGroupContent":
        """
        AUTOSAR-compliant setter for hwPin with method chaining.
        
        Args:
            value: The hwPin to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_pin property setter (gets validation automatically)
        """
        self.hw_pin = value  # Delegates to property setter
        return self

    def getHwPinGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    def setHwPinGroup(self, value: "RefType") -> "HwPinGroupContent":
        """
        AUTOSAR-compliant setter for hwPinGroup with method chaining.
        
        Args:
            value: The hwPinGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_pin_group property setter (gets validation automatically)
        """
        self.hw_pin_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_hw_pin(self, value: Optional["HwPin"]) -> "HwPinGroupContent":
        """
        Set hwPin and return self for chaining.
        
        Args:
            value: The hwPin to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_pin("value")
        """
        self.hw_pin = value  # Use property setter (gets validation)
        return self

    def with_hw_pin_group(self, value: Optional[RefType]) -> "HwPinGroupContent":
        """
        Set hwPinGroup and return self for chaining.
        
        Args:
            value: The hwPinGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_pin_group("value")
        """
        self.hw_pin_group = value  # Use property setter (gets validation)
        return self



class HwPin(Identifiable):
    """
    This meta-class represents the possibility to describe a hardware pin.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPin
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 20, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute describes the function of the pin (e.
        # g.
        # CLK.
        self._functionName: List["String"] = []

    @property
    def function_name(self) -> List["String"]:
        """Get functionName (Pythonic accessor)."""
        return self._functionName
        # This attribute contains the name of the pin according to packaging of the
                # hardware element (e.
        # g.
        # A03).
        self._packagingPin: Optional["String"] = None

    @property
    def packaging_pin(self) -> Optional["String"]:
        """Get packagingPin (Pythonic accessor)."""
        return self._packagingPin

    @packaging_pin.setter
    def packaging_pin(self, value: Optional["String"]) -> None:
        """
        Set packagingPin with validation.
        
        Args:
            value: The packagingPin to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._packagingPin = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"packagingPin must be String or str or None, got {type(value).__name__}"
            )
        self._packagingPin = value
        # This attribute contains the physical pin number.
        self._pinNumber: Optional["Integer"] = None

    @property
    def pin_number(self) -> Optional["Integer"]:
        """Get pinNumber (Pythonic accessor)."""
        return self._pinNumber

    @pin_number.setter
    def pin_number(self, value: Optional["Integer"]) -> None:
        """
        Set pinNumber with validation.
        
        Args:
            value: The pinNumber to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pinNumber = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"pinNumber must be Integer or int or None, got {type(value).__name__}"
            )
        self._pinNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionName(self) -> List["String"]:
        """
        AUTOSAR-compliant getter for functionName.
        
        Returns:
            The functionName value
        
        Note:
            Delegates to function_name property (CODING_RULE_V2_00017)
        """
        return self.function_name  # Delegates to property

    def getPackagingPin(self) -> "String":
        """
        AUTOSAR-compliant getter for packagingPin.
        
        Returns:
            The packagingPin value
        
        Note:
            Delegates to packaging_pin property (CODING_RULE_V2_00017)
        """
        return self.packaging_pin  # Delegates to property

    def setPackagingPin(self, value: "String") -> "HwPin":
        """
        AUTOSAR-compliant setter for packagingPin with method chaining.
        
        Args:
            value: The packagingPin to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to packaging_pin property setter (gets validation automatically)
        """
        self.packaging_pin = value  # Delegates to property setter
        return self

    def getPinNumber(self) -> "Integer":
        """
        AUTOSAR-compliant getter for pinNumber.
        
        Returns:
            The pinNumber value
        
        Note:
            Delegates to pin_number property (CODING_RULE_V2_00017)
        """
        return self.pin_number  # Delegates to property

    def setPinNumber(self, value: "Integer") -> "HwPin":
        """
        AUTOSAR-compliant setter for pinNumber with method chaining.
        
        Args:
            value: The pinNumber to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pin_number property setter (gets validation automatically)
        """
        self.pin_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_packaging_pin(self, value: Optional["String"]) -> "HwPin":
        """
        Set packagingPin and return self for chaining.
        
        Args:
            value: The packagingPin to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_packaging_pin("value")
        """
        self.packaging_pin = value  # Use property setter (gets validation)
        return self

    def with_pin_number(self, value: Optional["Integer"]) -> "HwPin":
        """
        Set pinNumber and return self for chaining.
        
        Args:
            value: The pinNumber to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pin_number("value")
        """
        self.pin_number = value  # Use property setter (gets validation)
        return self



class HwElementConnector(Describable):
    """
    This meta-class represents the ability to connect two hardware elements. The
    details of the connection can be refined by hwPinGroupConnection.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementConnector
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 21, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association connects two hardware elements.
        self._hwElement: List["HwElement"] = []

    @property
    def hw_element(self) -> List["HwElement"]:
        """Get hwElement (Pythonic accessor)."""
        return self._hwElement
        # This represents one particular connection between two pins.
        # This connection shall be used if to be described but no description
                # connection between the hierarchical composition of HwPinGroupConnector) is
                # required.
        # atpVariation.
        self._hwPin: List["HwPinConnector"] = []

    @property
    def hw_pin(self) -> List["HwPinConnector"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin
        # This represents one particular connection between two pin groups.
        # atpVariation.
        self._hwPinGroup: List["RefType"] = []

    @property
    def hw_pin_group(self) -> List["RefType"]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwElement(self) -> List["HwElement"]:
        """
        AUTOSAR-compliant getter for hwElement.
        
        Returns:
            The hwElement value
        
        Note:
            Delegates to hw_element property (CODING_RULE_V2_00017)
        """
        return self.hw_element  # Delegates to property

    def getHwPin(self) -> List["HwPinConnector"]:
        """
        AUTOSAR-compliant getter for hwPin.
        
        Returns:
            The hwPin value
        
        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    def getHwPinGroup(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class HwPinGroupConnector(Describable):
    """
    This meta-class represents the ability to connect two pin groups.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPinGroupConnector
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 22, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents one particular connection between two pins.
        # The connected pins shall match the by the parent hwPinGroup atpVariation.
        self._hwPin: List["HwPinConnector"] = []

    @property
    def hw_pin(self) -> List["HwPinConnector"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin
        # This association connects two hardware pin groups.
        self._hwPinGroup: List["RefType"] = []

    @property
    def hw_pin_group(self) -> List["RefType"]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwPin(self) -> List["HwPinConnector"]:
        """
        AUTOSAR-compliant getter for hwPin.
        
        Returns:
            The hwPin value
        
        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    def getHwPinGroup(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class HwPinConnector(Describable):
    """
    This meta-class represents the ability to connect two pins.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPinConnector
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 22, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association connects two hardware pins.
        self._hwPin: List["HwPin"] = []

    @property
    def hw_pin(self) -> List["HwPin"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwPin(self) -> List["HwPin"]:
        """
        AUTOSAR-compliant getter for hwPin.
        
        Returns:
            The hwPin value
        
        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class HwElement(HwDescriptionEntity):
    """
    This represents the ability to describe Hardware Elements on an instance
    level. The particular types of hardware are distinguished by the category.
    This category determines the applicable attributes. The possible categories
    and attributes are defined in HwCategory.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElement
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 296, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 18, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 991, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2026, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents one particular connection between two elements.
        # atpVariation.
        self._hwElement: List["HwElementConnector"] = []

    @property
    def hw_element(self) -> List["HwElementConnector"]:
        """Get hwElement (Pythonic accessor)."""
        return self._hwElement
        # This aggregation is used to describe the connection a hardware element.
        # Note that hardware no pins but only pingroups.
        # atpVariation.
        self._hwPinGroup: List["RefType"] = []

    @property
    def hw_pin_group(self) -> List["RefType"]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup
        # This association is used to establish hierarchies of hw that one particular
                # HwElement can be this association only once.
        # I.
        # e.
        # multiple the same HwElement is not supported (at level).
        # atpVariation.
        self._nestedElement: List["HwElement"] = []

    @property
    def nested_element(self) -> List["HwElement"]:
        """Get nestedElement (Pythonic accessor)."""
        return self._nestedElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwElement(self) -> List["HwElementConnector"]:
        """
        AUTOSAR-compliant getter for hwElement.
        
        Returns:
            The hwElement value
        
        Note:
            Delegates to hw_element property (CODING_RULE_V2_00017)
        """
        return self.hw_element  # Delegates to property

    def getHwPinGroup(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    def getNestedElement(self) -> List["HwElement"]:
        """
        AUTOSAR-compliant getter for nestedElement.
        
        Returns:
            The nestedElement value
        
        Note:
            Delegates to nested_element property (CODING_RULE_V2_00017)
        """
        return self.nested_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====