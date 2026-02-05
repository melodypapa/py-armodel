"""
This module contains classes for representing AUTOSAR hardware element categories
in the EcuResourceTemplate module.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.AtpDefinition import (
    AtpDefinition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class HwAttributeLiteralDef(Identifiable):
    """
    Represents a hardware attribute literal definition in AUTOSAR hardware descriptions.
    This class defines the possible literal values for an enumerated hardware attribute.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwAttributeLiteralDef with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware attribute literal definition
            short_name: The unique short name of this hardware attribute literal definition
        """
        super().__init__(parent, short_name)

        self.value: Optional[str] = None

    def getValue(self) -> Optional[str]:
        """
        Gets the literal value for this attribute literal definition.

        Returns:
            String representing the literal value, or None if not set
        """
        return self.value

    def setValue(self, value: str):
        """
        Sets the literal value for this attribute literal definition.
        Only sets the value if it is not None.

        Args:
            value: The literal value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


class HwAttributeValue(ARObject):
    """
    Represents a hardware attribute value in AUTOSAR hardware descriptions.
    This class defines the actual values assigned to hardware attributes in the model.
    """

    def __init__(self):
        """
        Initializes the HwAttributeValue.
        """
        super().__init__()

        self.hwAttributeDefRef: Optional[RefType] = None
        self.value: Optional[str] = None

    def getHwAttributeDefRef(self) -> Optional[RefType]:
        """
        Gets the reference to the hardware attribute definition for this value.

        Returns:
            RefType representing the attribute definition reference, or None if not set
        """
        return self.hwAttributeDefRef

    def setHwAttributeDefRef(self, value: RefType):
        """
        Sets the reference to the hardware attribute definition for this value.
        Only sets the value if it is not None.

        Args:
            value: The attribute definition reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwAttributeDefRef = value
        return self

    def getValue(self) -> Optional[str]:
        """
        Gets the actual value for this hardware attribute.

        Returns:
            String representing the attribute value, or None if not set
        """
        return self.value

    def setValue(self, value: str):
        """
        Sets the actual value for this hardware attribute.
        Only sets the value if it is not None.

        Args:
            value: The attribute value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


class HwType(ARElement):
    """
    Represents a hardware type in AUTOSAR hardware descriptions.
    This class defines the basic structure for hardware types.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwType with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware type
            short_name: The unique short name of this hardware type
        """
        super().__init__(parent, short_name)


class HwAttributeDef(Identifiable):
    """
    Represents a hardware attribute definition in AUTOSAR hardware descriptions.
    This class defines the attributes that can be assigned to hardware elements.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwAttributeDef with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware attribute definition
            short_name: The unique short name of this hardware attribute definition
        """
        super().__init__(parent, short_name)

        self.hwAttributeLiterals: List[HwAttributeLiteralDef] = []
        self.isRequired: Optional[Boolean] = None
        self.unitRef: Optional[RefType] = None

    def getHwAttributeLiterals(self) -> List[HwAttributeLiteralDef]:
        """
        Gets the list of hardware attribute literals for this definition.

        Returns:
            List of HwAttributeLiteralDef instances
        """
        return self.hwAttributeLiterals

    def setHwAttributeLiterals(self, value: List[HwAttributeLiteralDef]):
        """
        Sets the list of hardware attribute literals for this definition.
        Only sets the value if it is not None.

        Args:
            value: The list of hardware attribute literals to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwAttributeLiterals = value
        return self

    def getIsRequired(self) -> Optional[Boolean]:
        """
        Gets the required flag for this attribute definition.

        Returns:
            Boolean indicating if this attribute is required, or None if not set
        """
        return self.isRequired

    def setIsRequired(self, value: Boolean):
        """
        Sets the required flag for this attribute definition.
        Only sets the value if it is not None.

        Args:
            value: The required flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.isRequired = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """
        Gets the unit reference for this attribute definition.

        Returns:
            RefType representing the unit reference, or None if not set
        """
        return self.unitRef

    def setUnitRef(self, value: RefType):
        """
        Sets the unit reference for this attribute definition.
        Only sets the value if it is not None.

        Args:
            value: The unit reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.unitRef = value
        return self


class HwCategory(AtpDefinition):
    """
    Represents a hardware category in AUTOSAR hardware descriptions.
    This class defines categories of hardware with associated attribute definitions.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwCategory with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware category
            short_name: The unique short name of this hardware category
        """
        super().__init__(parent, short_name)

        self.hwAttributeDefs: List["HwAttributeDef"] = []

    def getHwAttributeDefs(self) -> List["HwAttributeDef"]:
        """
        Gets the list of hardware attribute definitions for this category.

        Returns:
            List of HwAttributeDef instances
        """
        return self.hwAttributeDefs

    def createHwAttributeDef(self, short_name: str) -> "HwAttributeDef":
        """
        Creates and adds a new hardware attribute definition to this category.

        Args:
            short_name: The short name for the new hardware attribute definition

        Returns:
            The created HwAttributeDef instance
        """
        if not self.IsElementExists(short_name):
            pin_group = HwAttributeDef(self, short_name)
            self.addElement(pin_group)
            self.hwAttributeDefs.append(pin_group)
        return self.getElement(short_name)
