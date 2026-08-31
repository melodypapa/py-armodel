"""
This module contains classes for representing AUTOSAR hardware element categories
in the EcuResourceTemplate module.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
    PackageableElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AtpDefinition,
)


class HwType(ARElement, HwDescriptionEntity):
    """
    Represents a hardware type in AUTOSAR hardware descriptions.
    This class defines the basic structure for hardware types.
    """

    # HwType method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwType with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware type
            short_name: The unique short name of this hardware type
        """
        super().__init__(parent, short_name)


class HwAttributeValue(ARObject):
    """
    Represents a hardware attribute value in AUTOSAR hardware descriptions.
    This class defines the actual values assigned to hardware attributes in the model.
    """

    # HwAttributeValue method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getHwAttributeDefRef         [x] impl  [x] docstring  [ ] test
    # [ ] setHwAttributeDefRef         [x] impl  [x] docstring  [ ] test
    # [ ] getValue                     [x] impl  [x] docstring  [ ] test
    # [ ] setValue                     [x] impl  [x] docstring  [ ] test

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


class HwAttributeLiteralDef(Identifiable):
    """
    Represents a hardware attribute literal definition in AUTOSAR hardware descriptions.
    This class defines the possible literal values for an enumerated hardware attribute.
    """

    # HwAttributeLiteralDef method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getValue                     [x] impl  [x] docstring  [ ] test
    # [ ] setValue                     [x] impl  [x] docstring  [ ] test

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


class HwAttributeDef(Identifiable):
    """
    This metaclass represents the ability to define a particular hardware attribute. The category of this element defines the type of the attributeValue. If the category is Enumeration the hw AttributeEnumerationLiterals specify the available literals.
    """

    # HwAttributeDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.13, p.26
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createHwAttributeLiteral     [x] impl  [x] docstring  [ ] test  [x] reader  [x] writer
    # [x] addHwAttributeLiteral        [x] impl  [x] docstring  [ ] test  [ ] reader  [ ] writer
    # [x] getHwAttributeLiterals       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setHwAttributeLiterals       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getIsRequired                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setIsRequired                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getUnitRef                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setUnitRef                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the Hw AttributeDef equals Enumeration.
        self.hwAttributeLiterals: List[HwAttributeLiteralDef] = []

        # This attribute specifies if the defined attribute value is required to be provided.
        self.isRequired: Optional[Boolean] = None

        # This association specifies the physical unit of the defined hardware attribute. This is optional due to the fact that there are textual attributes.
        self.unitRef: Optional[RefType] = None

    def getHwAttributeLiterals(self) -> List[HwAttributeLiteralDef]:
        """The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the Hw AttributeDef equals Enumeration."""
        return self.hwAttributeLiterals

    def setHwAttributeLiterals(self, value: List[HwAttributeLiteralDef]):
        """The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the Hw AttributeDef equals Enumeration. Only sets the value if it is not None."""
        if value is not None:
            self.hwAttributeLiterals = value
        return self

    def createHwAttributeLiteral(self, short_name: str) -> HwAttributeLiteralDef:
        """The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the Hw AttributeDef equals Enumeration."""
        if not self.IsElementExists(short_name, HwAttributeLiteralDef):
            literal_def = HwAttributeLiteralDef(self, short_name)
            self.addElement(literal_def)
            self.hwAttributeLiterals.append(literal_def)
        return self.getElement(short_name, HwAttributeLiteralDef)

    def addHwAttributeLiteral(self, literal_def: HwAttributeLiteralDef) -> "HwAttributeDef":
        """The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the Hw AttributeDef equals Enumeration."""
        if literal_def not in self.hwAttributeLiterals:
            self.hwAttributeLiterals.append(literal_def)
        return self

    def getIsRequired(self) -> Optional[Boolean]:
        """This attribute specifies if the defined attribute value is required to be provided."""
        return self.isRequired

    def setIsRequired(self, value: Boolean):
        """This attribute specifies if the defined attribute value is required to be provided. Only sets the value if it is not None."""
        if value is not None:
            self.isRequired = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """This association specifies the physical unit of the defined hardware attribute. This is optional due to the fact that there are textual attributes."""
        return self.unitRef

    def setUnitRef(self, value: RefType):
        """This association specifies the physical unit of the defined hardware attribute. This is optional due to the fact that there are textual attributes. Only sets the value if it is not None."""
        if value is not None:
            self.unitRef = value
        return self


class HwCategory(PackageableElement, AtpDefinition):
    """
    Represents a hardware category in AUTOSAR hardware descriptions.
    This class defines categories of hardware with associated attribute definitions.
    """

    # HwCategory method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getHwAttributeDefs           [x] impl  [x] docstring  [ ] test
    # [ ] createHwAttributeDef         [x] impl  [x] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwCategory with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware category
            short_name: The unique short name of this hardware category
        """
        PackageableElement.__init__(self, parent, short_name)
        AtpDefinition.__init__(self, parent, short_name)

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
        if not self.IsElementExists(short_name, HwAttributeDef):
            pin_group = HwAttributeDef(self, short_name)
            self.addElement(pin_group)
            self.hwAttributeDefs.append(pin_group)
        return self.getElement(short_name, HwAttributeDef)
