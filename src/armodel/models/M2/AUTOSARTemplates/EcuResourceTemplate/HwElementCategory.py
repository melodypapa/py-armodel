"""
This module contains classes for representing AUTOSAR hardware element categories
in the EcuResourceTemplate module.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Numerical,
    RefType,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity
from armodel.models.M2.MSR.Documentation.Annotation import Annotation


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
    This metaclass represents the ability to assign a hardware attribute value. Note that v and vt are mutually exclusive.
    """

    # HwAttributeValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.2, p.16
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAnnotation         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAnnotation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHwAttributeDefRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHwAttributeDefRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getV                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setV                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVt                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVt                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVariationPoint     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVariationPoint     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Optional annotation that can be added to each HwAttributeValue.
        self.annotation: Optional[Annotation] = None

        # This association represents the definition of the particular hardware attribute value.
        self.hwAttributeDefRef: Optional[RefType] = None

        # This represents a numerical hardware attribute value. Stereotypes: atpVariation Tags: vh.latestBindingTime=systemDesignTime
        self.v: Optional[Numerical] = None

        # This represents a textual hardware attribute value.
        self.vt: Optional[VerbatimString] = None

    def getAnnotation(self) -> Optional[Annotation]:
        """
        Optional annotation that can be added to each HwAttributeValue.
        """
        return self.annotation

    def setAnnotation(self, value: Annotation) -> "HwAttributeValue":
        """
        Optional annotation that can be added to each HwAttributeValue.

        A None value is a no-op and does not overwrite an existing annotation.
        """
        if value is not None:
            self.annotation = value
        return self

    def getHwAttributeDefRef(self) -> Optional[RefType]:
        """
        This association represents the definition of the particular hardware attribute value.
        """
        return self.hwAttributeDefRef

    def setHwAttributeDefRef(self, value: RefType) -> "HwAttributeValue":
        """
        This association represents the definition of the particular hardware attribute value.

        A None value is a no-op and does not overwrite an existing hwAttributeDefRef.
        """
        if value is not None:
            self.hwAttributeDefRef = value
        return self

    def getV(self) -> Optional[Numerical]:
        """
        This represents a numerical hardware attribute value. Stereotypes: atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        return self.v

    def setV(self, value: Numerical) -> "HwAttributeValue":
        """
        This represents a numerical hardware attribute value. Stereotypes: atpVariation Tags: vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not overwrite an existing v.
        """
        if value is not None:
            self.v = value
        return self

    def getVt(self) -> Optional[VerbatimString]:
        """
        This represents a textual hardware attribute value.
        """
        return self.vt

    def setVt(self, value: VerbatimString) -> "HwAttributeValue":
        """
        This represents a textual hardware attribute value.

        A None value is a no-op and does not overwrite an existing vt.
        """
        if value is not None:
            self.vt = value
        return self


class HwAttributeLiteralDef(Identifiable):
    """
    One available EnumerationLiteral of the Enumeration definition. Only applicable if the category of the HwAttributeDef equals Enumeration.
    """

    # HwAttributeLiteralDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.14, p.26
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class HwAttributeDef(Identifiable):
    """
    This metaclass represents the ability to define a particular hardware attribute. The category of this element defines the type of the attributeValue. If the category is Enumeration the hwAttributeEnumerationLiterals specify the available literals.
    """

    # HwAttributeDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.13, p.26
    # Spec verified: R23-11
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

    def __init__(self, parent: ARObject, short_name: str):
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
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] createHwAttributeDef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addHwAttributeDef     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getHwAttributeDefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
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
