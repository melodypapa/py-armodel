from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, RefType, ARNumerical, Identifier, Integer
from armodel.models.M2.MSR.Documentation.Annotation import Annotation

from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import (
    MlFormula,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum
)


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


class PredefinedVariant(Identifiable):
    """
    This specifies one predefined variant.

    It is characterized by the union of all system constant values and
    post-build variant criterion values aggregated within all referenced
    system constant value sets and post-build variant criterion value sets,
    plus the value sets of the included variants.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARElement, ARObject, CollectableElement, Identifiable,
        MultilanguageReferrable, PackageableElement, Referrable
    Tags: atp.recommendedPackage=PredefinedVariants
    """

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.includedVariantRefs: List[RefType] = []
        self.postBuildVariantCriterionValueSetRefs: List[RefType] = []
        self.swSystemconstantValueSetRefs: List[RefType] = []

    def getIncludedVariantRefs(self) -> List[RefType]:
        return self.includedVariantRefs

    def addIncludedVariantRef(self, value: RefType):
        if value is not None:
            self.includedVariantRefs.append(value)
        return self

    def getPostBuildVariantCriterionValueSetRefs(self) -> List[RefType]:
        return self.postBuildVariantCriterionValueSetRefs

    def addPostBuildVariantCriterionValueSetRef(self, value: RefType):
        if value is not None:
            self.postBuildVariantCriterionValueSetRefs.append(value)
        return self

    def getSwSystemconstantValueSetRefs(self) -> List[RefType]:
        return self.swSystemconstantValueSetRefs

    def addSwSystemconstantValueSetRef(self, value: RefType):
        if value is not None:
            self.swSystemconstantValueSetRefs.append(value)
        return self


class SwSystemconstValue(ARObject):
    """
    This meta-class assigns a particular value to a system constant.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject

    Attributes:
        annotations (List[Annotation]):
            Provides the ability to add information why the value is set as
            it is.
            Tag: xml.sequenceOffset=30
        swSystemconstRef (RefType):
            Reference to the system constant to which the value applies.
            Tag: xml.sequenceOffset=10
        value (ARNumerical):
            The particular value of a system constant. Further restrictions
            may apply by the definition of the system constant. This defines
            the internal value of the SwSystemconst as processed in the
            Formula Language.
            Stereotype: atpVariation
            Tags: vh.latestBindingTime=preCompileTime,
                xml.sequenceOffset=20
    """

    def __init__(self):
        super().__init__()

        self.annotations: List[Annotation] = []
        self.swSystemconstRef: RefType = None
        self.value: ARNumerical = None

    def getAnnotations(self) -> List[Annotation]:
        return self.annotations

    def addAnnotation(self, value: Annotation):
        if value is not None:
            self.annotations.append(value)
        return self

    def getSwSystemconstRef(self) -> RefType:
        return self.swSystemconstRef

    def setSwSystemconstRef(self, value: RefType):
        if value is not None:
            self.swSystemconstRef = value
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

    def getSwSystemconstantValues(self) -> List[SwSystemconstValue]:
        """
        Returns the list of system constant values in the set.

        Returns:
            List[SwSystemconstValue]: The list of system constant values.
        """
        return self.swSystemconstantValues


class PostBuildVariantCondition(ARObject):
    """
    Specifies a post-build variant condition criterion/value pair.

    This class specifies the value which must be assigned to a particular
    variant criterion in order to bind the variation point. If multiple
    criterion/value pairs are specified, they shall all match to bind the
    variation point. In other words, binding can be represented by:
    (criterion1 == value1) && (criterion2 == value2) ...

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject
    Stereotypes: atpVariation
    Tags: vh.latestBindingTime=preCompileTime

    Attributes:
        matchingCriterion (PostBuildVariantCriterion): The criterion
            which needs to match the value in order to make the
            PostBuildVariantCondition true. (Multiplicity: 1)
        value (Integer): The particular value of the post-build variant
            criterion. (Multiplicity: 1)
    """

    def __init__(self):
        super().__init__()

        self.matchingCriterion: PostBuildVariantCriterion = None
        self.value: Integer = None

    def getMatchingCriterion(self) -> PostBuildVariantCriterion:
        """
        Gets the matching criterion for this condition.

        Returns:
            PostBuildVariantCriterion: The criterion to match
        """
        return self.matchingCriterion

    def setMatchingCriterion(
        self, value: PostBuildVariantCriterion
    ) -> "PostBuildVariantCondition":
        """
        Sets the matching criterion for this condition.

        Args:
            value: The criterion to match

        Returns:
            self for method chaining
        """
        if value is not None:
            self.matchingCriterion = value
        return self

    def getValue(self) -> Integer:
        """
        Gets the criterion value for this condition.

        Returns:
            Integer: The value to match
        """
        return self.value

    def setValue(self, value: Integer) -> "PostBuildVariantCondition":
        """
        Sets the criterion value for this condition.

        Args:
            value: The value to match

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


class ConditionByFormula(ARObject):
    """
    Represents a system condition computed based on system constants.

    This class represents a condition which is computed based on system
    constants according to a specified expression. The expected result is
    interpreted as a boolean value where:
    - "0" represents false
    - Any non-zero value is considered true

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject
    Stereotypes: atpMixedString

    Attributes:
        bindingTime (BindingTimeEnum): Specifies the point in time when
           the condition may be evaluated at earliest. At this point in
           time, all referenced system constants shall have a value.
           (Multiplicity: 1)
    """

    def __init__(self):
        super().__init__()

        self.bindingTime: Optional["BindingTimeEnum"] = None

    def getBindingTime(self) -> Optional["BindingTimeEnum"]:
        """
        Gets the binding time for this condition.

        Returns:
           BindingTimeEnum: When this condition may be evaluated, or None
        """
        return self.bindingTime

    def setBindingTime(
        self, value: "BindingTimeEnum"
    ) -> "ConditionByFormula":
        """
        Sets the binding time for this condition.

        Args:
           value: When this condition may be evaluated

        Returns:
           self for method chaining
        """
        if value is not None:
            self.bindingTime = value
        return self


class VariationPoint(ARObject):
    """
    Represents a structural variation point in the AUTOSAR model.

    This class represents the ability to express a "structural variation
    point". The container of the variation point is part of the selected
    variant if swSyscond evaluates to true and each postBuildVariantCriterion
    is fulfilled.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject

    Attributes:
        desc (MultiLanguageOverviewParagraph): Allows to describe shortly
            the purpose of the variation point. (Multiplicity: 0..1)
        blueprintCondition (DocumentationBlock): Represents a description
            that documents how the variation point shall be resolved when
            deriving objects from the blueprint. Note that variationPoints
            are not allowed within a blueprintCondition.
            (Multiplicity: 0..1)
        formalBlueprintCondition (MlFormula): Denotes a formal blueprint
            condition. This shall not be in contradiction with
            blueprintCondition. It is recommended to use only one of the
            two. (Multiplicity: 0..1)
        postBuildVariantCondition (List[PostBuildVariantCondition]): The
            set of post-build variant conditions which all shall be
            fulfilled in order to bind the variation point.
            (Multiplicity: *)
        sdg (Sdg): An optional special data group attached to every
            variation point. These data can be used by external software
            systems to attach application specific data. For example, a
            variant management system might add an identifier, an URL or
            a specific classifier. (Multiplicity: 0..1)
        shortLabel (Identifier): Provides a name to the particular variation
            point to support the RTE generator. It is necessary for
            supporting splitable aggregations and if binding time is
            later than codeGenerationTime, as well as some RTE
            conditions. It needs to be unique within the enclosing
            Identifiables with the same ShortName. (Multiplicity: 0..1)
        swSyscond (ConditionByFormula): This condition acts as Binding
            Function for the VariationPoint. Note that the multiplicity
            is 0..1 in order to support pure postBuild variants.
            (Multiplicity: 0..1)
    """

    def __init__(self):
        super().__init__()

        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.blueprintCondition: Optional[DocumentationBlock] = None
        self.formalBlueprintCondition: Optional[MlFormula] = None
        self.postBuildVariantConditions: List["PostBuildVariantCondition"] = []
        self.sdg: Optional[Sdg] = None
        self.shortLabel: Optional[Identifier] = None
        self.swSyscond: Optional["ConditionByFormula"] = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        Gets the description of this variation point.

        Returns:
            MultiLanguageOverviewParagraph: The description, or None
        """
        return self.desc

    def setDesc(
        self, value: MultiLanguageOverviewParagraph
    ) -> "VariationPoint":
        """
        Sets the description of this variation point.

        Args:
            value: The description to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.desc = value
        return self

    def getBlueprintCondition(self) -> Optional[DocumentationBlock]:
        """
        Gets the blueprint condition documentation for this variation
        point.

        Returns:
            DocumentationBlock: The condition documentation, or None
        """
        return self.blueprintCondition

    def setBlueprintCondition(
        self, value: DocumentationBlock
    ) -> "VariationPoint":
        """
        Sets the blueprint condition documentation for this variation
        point.

        Args:
            value: The condition documentation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.blueprintCondition = value
        return self

    def getFormalBlueprintCondition(self) -> Optional[MlFormula]:
        """
        Gets the formal blueprint condition for this variation point.

        Returns:
            MlFormula: The formal condition, or None
        """
        return self.formalBlueprintCondition

    def setFormalBlueprintCondition(
        self, value: MlFormula
    ) -> "VariationPoint":
        """
        Sets the formal blueprint condition for this variation point.

        Args:
            value: The formal condition to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.formalBlueprintCondition = value
        return self

    def getPostBuildVariantConditions(
        self
    ) -> List["PostBuildVariantCondition"]:
        """
        Gets the post-build variant conditions for this variation point.

        Returns:
            List[PostBuildVariantCondition]: The list of conditions
        """
        return self.postBuildVariantConditions

    def addPostBuildVariantCondition(
        self, value: "PostBuildVariantCondition"
    ) -> "VariationPoint":
        """
        Adds a post-build variant condition to this variation point.

        Args:
            value: The condition to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.postBuildVariantConditions.append(value)
        return self

    def getSdg(self) -> Optional[Sdg]:
        """
        Gets the special data group for this variation point.

        Returns:
            Sdg: The special data group, or None
        """
        return self.sdg

    def setSdg(self, value: Sdg) -> "VariationPoint":
        """
        Sets the special data group for this variation point.

        Args:
            value: The special data group to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sdg = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        Gets the short label for this variation point.

        Returns:
            Identifier: The short label for RTE generator, or None
        """
        return self.shortLabel

    def setShortLabel(self, value: Identifier) -> "VariationPoint":
        """
        Sets the short label for this variation point.

        Args:
            value: The short label for RTE generator support

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortLabel = value
        return self

    def getSwSyscond(self) -> Optional["ConditionByFormula"]:
        """
        Gets the system condition for this variation point.

        Returns:
            ConditionByFormula: The system condition, or None
        """
        return self.swSyscond

    def setSwSyscond(self, value: "ConditionByFormula") -> "VariationPoint":
        """
        Sets the system condition for this variation point.

        Args:
            value: The system condition to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swSyscond = value
        return self
