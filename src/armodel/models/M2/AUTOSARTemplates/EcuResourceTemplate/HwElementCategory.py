"""
This module contains classes for representing AUTOSAR hardware element categories
in the EcuResourceTemplate module.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

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
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity


class HwType(ARElement, HwDescriptionEntity):
    """
    This represents the ability to describe Hardware types on an abstract level. The particular types of hardware are distinguished by the category. This category determines the applicable attributes. The possible categories and attributes are defined in HwCategory.
    """

    # HwType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.3, p.17
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)


class HwAttributeValue(ARObject, VariationPointCapable):
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
    This metaclass represents the ability to define a particular hardware attribute. The category of this element defines the type of the attributeValue. If the category is Enumeration the hwAttributeEnumerationLiterals specify the available literals.
    """

    # HwAttributeDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.13, p.26
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] createHwAttributeLiteral  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addHwAttributeLiteral     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getHwAttributeLiterals    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHwAttributeLiterals    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIsRequired             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setIsRequired             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getUnitRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setUnitRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the HwAttributeDef equals Enumeration.
        self.hwAttributeLiterals: List[HwAttributeLiteralDef] = []

        # This attribute specifies if the defined attribute value is required to be provided.
        self.isRequired: Optional[Boolean] = None

        # This association specifies the physical unit of the defined hardware attribute. This is optional due to the fact that there are textual attributes.
        self.unitRef: Optional[RefType] = None

    def getHwAttributeLiterals(self) -> List[HwAttributeLiteralDef]:
        """
        The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the HwAttributeDef equals Enumeration.
        """
        return self.hwAttributeLiterals

    def setHwAttributeLiterals(self, value: List[HwAttributeLiteralDef]) -> "HwAttributeDef":
        """
        The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the HwAttributeDef equals Enumeration.

        A None value is a no-op and does not overwrite an existing hwAttributeLiterals list.
        """
        if value is not None:
            self.hwAttributeLiterals = value
        return self

    def createHwAttributeLiteral(self, short_name: str) -> HwAttributeLiteralDef:
        """
        The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the HwAttributeDef equals Enumeration.
        """
        if not self.IsElementExists(short_name, HwAttributeLiteralDef):
            literal_def = HwAttributeLiteralDef(self, short_name)
            self.addElement(literal_def)
            self.hwAttributeLiterals.append(literal_def)
        return self.getElement(short_name, HwAttributeLiteralDef)

    def addHwAttributeLiteral(self, literal_def: HwAttributeLiteralDef) -> "HwAttributeDef":
        """
        The available EnumerationLiterals of the Enumeration definition. Only applicable if the category of the HwAttributeDef equals Enumeration.

        A None value is a no-op and does not extend the hwAttributeLiterals list.
        """
        if literal_def is not None and literal_def not in self.hwAttributeLiterals:
            self.hwAttributeLiterals.append(literal_def)
        return self

    def getIsRequired(self) -> Optional[Boolean]:
        """
        This attribute specifies if the defined attribute value is required to be provided.
        """
        return self.isRequired

    def setIsRequired(self, value: Boolean) -> "HwAttributeDef":
        """
        This attribute specifies if the defined attribute value is required to be provided.

        A None value is a no-op and does not overwrite an existing isRequired.
        """
        if value is not None:
            self.isRequired = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """
        This association specifies the physical unit of the defined hardware attribute. This is optional due to the fact that there are textual attributes.
        """
        return self.unitRef

    def setUnitRef(self, value: RefType) -> "HwAttributeDef":
        """
        This association specifies the physical unit of the defined hardware attribute. This is optional due to the fact that there are textual attributes.

        A None value is a no-op and does not overwrite an existing unitRef.
        """
        if value is not None:
            self.unitRef = value
        return self


class HwCategory(ARElement):
    """
    This metaclass represents the ability to declare hardware categories and its particular attributes. Tags: atp.recommendedPackage=HwCategorys
    """

    # HwCategory method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.11, p.24
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] createHwAttributeDef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addHwAttributeDef     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getHwAttributeDefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation describes particular hardware attribute definition.
        self.hwAttributeDefs: List[HwAttributeDef] = []

    def getHwAttributeDefs(self) -> List[HwAttributeDef]:
        """
        This aggregation describes particular hardware attribute definition.
        """
        return self.hwAttributeDefs

    def createHwAttributeDef(self, short_name: str) -> HwAttributeDef:
        """
        This aggregation describes particular hardware attribute definition.
        """
        if not self.IsElementExists(short_name, HwAttributeDef):
            attribute_def = HwAttributeDef(self, short_name)
            self.addElement(attribute_def)
            self.hwAttributeDefs.append(attribute_def)
        return self.getElement(short_name, HwAttributeDef)

    def addHwAttributeDef(self, attribute_def: HwAttributeDef) -> "HwCategory":
        """
        This aggregation describes particular hardware attribute definition.

        A None value is a no-op and does not extend the hwAttributeDefs list.
        """
        if attribute_def is not None and attribute_def not in self.hwAttributeDefs:
            self.hwAttributeDefs.append(attribute_def)
        return self
