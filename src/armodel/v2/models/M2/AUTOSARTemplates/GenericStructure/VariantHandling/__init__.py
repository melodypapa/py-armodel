from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
    String,
)


class VariationPoint(ARObject):
    """
    Represents a variation point in the AUTOSAR model.

    This class is used to define variation points that allow for different
    configurations based on variant conditions.

    Attributes:
        variationPointName (String): The name of the variation point.
        isEnabled (Boolean): Whether the variation point is enabled.
        variantCondition (String): The condition for the variant.
    """
    def __init__(self):
        super().__init__()

        self.variationPointName: String = None
        self.isEnabled: Boolean = None
        self.variantCondition: String = None

    def getVariationPointName(self) -> String:
        return self.variationPointName

    def setVariationPointName(self, value: String):
        if value is not None:
            self.variationPointName = value
        return self

    def getIsEnabled(self) -> Boolean:
        return self.isEnabled

    def setIsEnabled(self, value: Boolean):
        if value is not None:
            self.isEnabled = value
        return self

    def getVariantCondition(self) -> String:
        return self.variantCondition

    def setVariantCondition(self, value: String):
        if value is not None:
            self.variantCondition = value
        return self


class PostBuildVariantCriterion(ARObject):
    """
    Represents a post-build variant criterion in the AUTOSAR model.

    This class is used to define criteria for post-build variants,
    allowing for configuration after build time.

    Attributes:
        criterionName (String): The name of the criterion.
        criterionValue (String): The value of the criterion.
    """
    def __init__(self):
        super().__init__()

        self.criterionName: String = None
        self.criterionValue: String = None

    def getCriterionName(self) -> String:
        return self.criterionName

    def setCriterionName(self, value: String):
        if value is not None:
            self.criterionName = value
        return self

    def getCriterionValue(self) -> String:
        return self.criterionValue

    def setCriterionValue(self, value: String):
        if value is not None:
            self.criterionValue = value
        return self


class PostBuildVariantCriterionValue(ARObject):
    """
    Represents a post-build variant criterion value in the AUTOSAR model.

    This class is used to define values for post-build variant criteria.

    Attributes:
        value (String): The criterion value.
    """
    def __init__(self):
        super().__init__()

        self.value: String = None

    def getValue(self) -> String:
        return self.value

    def setValue(self, value: String):
        if value is not None:
            self.value = value
        return self


class PredefinedVariant(ARObject):
    """
    Represents a predefined variant in the AUTOSAR model.

    This class is used to define predefined variants that can be selected
    during configuration.

    Attributes:
        variantName (String): The name of the predefined variant.
        variantDescription (String): The description of the predefined variant.
    """
    def __init__(self):
        super().__init__()

        self.variantName: String = None
        self.variantDescription: String = None

    def getVariantName(self) -> String:
        return self.variantName

    def setVariantName(self, value: String):
        if value is not None:
            self.variantName = value
        return self

    def getVariantDescription(self) -> String:
        return self.variantDescription

    def setVariantDescription(self, value: String):
        if value is not None:
            self.variantDescription = value
        return self


class SwSystemconstantValueSet(ARObject):
    """
    Represents a system constant value set in the AUTOSAR model.

    This class is used to define sets of system constant values that can be
    used in variant handling.

    Attributes:
        constantName (String): The name of the constant.
        constantValues (List[String]): A list of constant values.
        constantRef (RefType): A reference to the constant definition.
    """
    def __init__(self):
        super().__init__()

        self.constantName: String = None
        self.constantValues: List[String] = []
        self.constantRef: RefType = None

    def getConstantName(self) -> String:
        return self.constantName

    def setConstantName(self, value: String):
        if value is not None:
            self.constantName = value
        return self

    def getConstantValues(self) -> List[String]:
        return self.constantValues

    def addConstantValue(self, value: String):
        if value is not None:
            self.constantValues.append(value)
        return self

    def getConstantRef(self) -> RefType:
        return self.constantRef

    def setConstantRef(self, value: RefType):
        if value is not None:
            self.constantRef = value
        return self


__all__ = []
