from typing import List, Union

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

    def __init__(self) -> None:
        super().__init__()

        self.variationPointName: Union[Union[String, None] , None] = None
        self.isEnabled: Union[Union[Boolean, None] , None] = None
        self.variantCondition: Union[Union[String, None] , None] = None

    def getVariationPointName(self) -> Union[String, None]:
        return self.variationPointName

    def setVariationPointName(self, value: String) -> "VariationPoint":
        if value is not None:
            self.variationPointName = value
        return self

    def getIsEnabled(self) -> Union[Boolean, None]:
        return self.isEnabled

    def setIsEnabled(self, value: Boolean) -> "VariationPoint":
        if value is not None:
            self.isEnabled = value
        return self

    def getVariantCondition(self) -> Union[String, None]:
        return self.variantCondition

    def setVariantCondition(self, value: String) -> "VariationPoint":
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

    def __init__(self) -> None:
        super().__init__()

        self.criterionName: Union[Union[String, None] , None] = None
        self.criterionValue: Union[Union[String, None] , None] = None

    def getCriterionName(self) -> Union[String, None]:
        return self.criterionName

    def setCriterionName(self, value: String) -> "Criterion":
        if value is not None:
            self.criterionName = value
        return self

    def getCriterionValue(self) -> Union[String, None]:
        return self.criterionValue

    def setCriterionValue(self, value: String) -> "Criterion":
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

    def __init__(self) -> None:
        super().__init__()

        self.value: Union[Union[String, None] , None] = None

    def getValue(self) -> Union[String, None]:
        return self.value

    def setValue(self, value: String) -> "VariantCriterion":
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

    def __init__(self) -> None:
        super().__init__()

        self.variantName: Union[Union[String, None] , None] = None
        self.variantDescription: Union[Union[String, None] , None] = None

    def getVariantName(self) -> Union[String, None]:
        return self.variantName

    def setVariantName(self, value: String) -> "PredefinedVariant":
        if value is not None:
            self.variantName = value
        return self

    def getVariantDescription(self) -> Union[String, None]:
        return self.variantDescription

    def setVariantDescription(self, value: String) -> "PredefinedVariant":
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

    def __init__(self) -> None:
        super().__init__()

        self.constantName: Union[Union[String, None] , None] = None
        self.constantValues: List[String] = []
        self.constantRef: Union[Union[RefType, None] , None] = None

    def getConstantName(self) -> Union[String, None]:
        return self.constantName

    def setConstantName(self, value: String) -> "Decision":
        if value is not None:
            self.constantName = value
        return self

    def getConstantValues(self) -> List[String]:
        return self.constantValues

    def addConstantValue(self, value: String) -> "Decision":
        if value is not None:
            self.constantValues.append(value)
        return self

    def getConstantRef(self) -> Union[RefType, None]:
        return self.constantRef

    def setConstantRef(self, value: RefType) -> "Decision":
        if value is not None:
            self.constantRef = value
        return self


__all__ = []
