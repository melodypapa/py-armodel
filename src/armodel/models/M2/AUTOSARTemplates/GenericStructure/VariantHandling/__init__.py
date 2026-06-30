from typing import List
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, Boolean, RefType, ARNumerical
from armodel.models.M2.MSR.Documentation.Annotation import Annotation


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


class SwSystemconstValue(ARObject):
    """
    Assigns a particular value to a system constant.
    """

    def __init__(self):
        super().__init__()

        self.annotations: List[Annotation] = []
        self.swSystemconstRef: RefType = None
        self.swSystemconst: RefType = None
        self.value: ARNumerical = None

    def getAnnotations(self) -> List[Annotation]:
        return self.annotations

    def addAnnotation(self, value: Annotation):
        if value is not None:
            self.annotations.append(value)
        return self

    def getSwSystemconst(self) -> RefType:
        return self.swSystemconstRef

    def setSwSystemconst(self, value: RefType):
        return self.setSwSystemconstRef(value)

    def getSwSystemconstRef(self) -> RefType:
        return self.swSystemconstRef

    def setSwSystemconstRef(self, value: RefType):
        if value is not None:
            self.swSystemconstRef = value
            self.swSystemconst = value
        return self

    def getValue(self) -> ARNumerical:
        return self.value

    def setValue(self, value: ARNumerical):
        if value is not None:
            self.value = value
        return self


class SwSystemconstantValueSet(Identifiable):
    """
        This meta-class represents the ability to specify a set of system constant values.
        Tags: atp.recommendedPackage=SwSystemconstantValueSets
    """

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.swSystemconstantValues: List[SwSystemconstValue] = []

    def addSwSystemconstantValue(self, value: SwSystemconstValue):
        """
        Adds a system constant value to the set.

        Args:
            value (SwSystemconstValue): The system constant value to add.
        """
        if value is not None:
            self.swSystemconstantValues.append(value)
        return self
    
    def getSwSystemconstantValues(self) -> List['SwSystemconstValue']:
        """
        Returns the list of system constant values in the set.

        Returns:
            List[SwSystemconstValue]: The list of system constant values.
        """
        return self.swSystemconstantValues
