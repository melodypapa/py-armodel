from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, ARNumerical, Identifier, Integer
from armodel.models.M2.MSR.Documentation.Annotation import Annotation

from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import BlueprintGenerator


class PostBuildVariantCriterion(ARElement):
    """
    This class specifies one particular PostBuildVariantSelector.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARElement, ARObject, AtpDefinition, CollectableElement, Identifiable,
        MultilanguageReferrable, PackageableElement, Referrable
    Tags: atp.recommendedPackage=PostBuildVariantCriterions

    Attributes:
        compuMethodRef (CompuMethod): The compuMethod specifies the
            possible values for the variant criterion serving as an
            enumerator. (Multiplicity: 1)
    """

    # PostBuildVariantCriterion method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.63, p.614
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCompuMethodRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCompuMethodRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The compuMethod specifies the possible values for the variant criterion serving as an enumerator.
        self.compuMethodRef: RefType = None

    def getCompuMethodRef(self) -> RefType:
        """
        The compuMethod specifies the possible values for the variant criterion
        serving as an enumerator.
        """
        return self.compuMethodRef

    def setCompuMethodRef(self, value: RefType) -> "PostBuildVariantCriterion":
        """
        The compuMethod specifies the possible values for the variant criterion
        serving as an enumerator. A None value is a no-op and does not overwrite an
        existing compuMethodRef.
        """
        if value is not None:
            self.compuMethodRef = value
        return self


class PostBuildVariantCriterionValue(ARObject):
    """
    This class specifies a the value which must be assigned to a particular variant
    criterion in order to bind the variation point. If multiple criterion/value pairs
    are specified, they all must must match to bind the variation point.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject

    Attributes:
        annotations (List[Annotation]): This provides the ability to add
            information why the value is set like it is. (Multiplicity: *)
        value (Integer): This is the particular value of the post-build
            variant criterion. (Multiplicity: 1)
        variantCriterionRef (PostBuildVariantCriterion): This association
            selects the variant criterion whose value is specified.
            (Multiplicity: 1)
    """

    # PostBuildVariantCriterionValue method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.27, p.259
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAnnotations          [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer
    # [x] addAnnotation           [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer
    # [x] getValue                [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer
    # [x] setValue                [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer
    # [x] getVariantCriterionRef  [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer
    # [x] setVariantCriterionRef  [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This provides the ability to add information why the value is set like it is.
        self.annotations: List[Annotation] = []

        # This is the particular value of the post-build variant criterion.
        self.value: Optional[Integer] = None

        # This association selects the variant criterion whose value is specified.
        self.variantCriterionRef: RefType = None

    def getAnnotations(self) -> List[Annotation]:
        """
        This provides the ability to add information why the value is set like it is.
        """
        return self.annotations

    def addAnnotation(self, value: Annotation) -> "PostBuildVariantCriterionValue":
        """
        This provides the ability to add information why the value is set like it is. A
        None value is a no-op and is not appended.
        """
        if value is not None:
            self.annotations.append(value)
        return self

    def getValue(self) -> Optional[Integer]:
        """
        This is the particular value of the post-build variant criterion.
        """
        return self.value

    def setValue(self, value: Optional[Integer]) -> "PostBuildVariantCriterionValue":
        """
        This is the particular value of the post-build variant criterion. A None value
        is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self

    def getVariantCriterionRef(self) -> RefType:
        """
        This association selects the variant criterion whose value is specified.
        """
        return self.variantCriterionRef

    def setVariantCriterionRef(self, value: RefType) -> "PostBuildVariantCriterionValue":
        """
        This association selects the variant criterion whose value is specified. A None
        value is a no-op and does not overwrite an existing variantCriterionRef.
        """
        if value is not None:
            self.variantCriterionRef = value
        return self


class PredefinedVariant(ARElement):
    """
    This specifies one predefined variant. It is characterized by the union of all system constant values and post-build variant criterion values aggregated within all referenced system constant value sets and post build variant criterion value sets plus the value sets of the included variants. Tags: atp.recommendedPackage=PredefinedVariants
    """

    # PredefinedVariant method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.24, p.258
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIncludedVariantRefs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addIncludedVariantRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantCriterionValueSetRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPostBuildVariantCriterionValueSetRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwSystemconstantValueSetRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSwSystemconstantValueSetRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The associated variants are considered part of this PredefinedVariant. This means the settings of the included variants are included in the settings of the referencing PredefinedVariant. Nevertheless the included variants might be included in several predefined variants.
        self.includedVariantRefs: List[RefType] = []

        # This is the postBuildVariantCriterionValueSet contributing to the predefinded variant.
        self.postBuildVariantCriterionValueSetRefs: List[RefType] = []

        # This ist the set of Systemconstant Values contributing to the predefined variant.
        self.swSystemconstantValueSetRefs: List[RefType] = []

    def getIncludedVariantRefs(self) -> List[RefType]:
        """
        The associated variants are considered part of this PredefinedVariant. This means the settings of the included variants are included in the settings of the referencing PredefinedVariant. Nevertheless the included variants might be included in several predefined variants.
        """
        return self.includedVariantRefs

    def addIncludedVariantRef(self, value: Optional[RefType]) -> "PredefinedVariant":
        """
        The associated variants are considered part of this PredefinedVariant. This means the settings of the included variants are included in the settings of the referencing PredefinedVariant. Nevertheless the included variants might be included in several predefined variants.
        """
        if value is not None:
            self.includedVariantRefs.append(value)
        return self

    def getPostBuildVariantCriterionValueSetRefs(self) -> List[RefType]:
        """
        This is the postBuildVariantCriterionValueSet contributing to the predefinded variant.
        """
        return self.postBuildVariantCriterionValueSetRefs

    def addPostBuildVariantCriterionValueSetRef(self, value: Optional[RefType]) -> "PredefinedVariant":
        """
        This is the postBuildVariantCriterionValueSet contributing to the predefinded variant.
        """
        if value is not None:
            self.postBuildVariantCriterionValueSetRefs.append(value)
        return self

    def getSwSystemconstantValueSetRefs(self) -> List[RefType]:
        """
        This ist the set of Systemconstant Values contributing to the predefined variant.
        """
        return self.swSystemconstantValueSetRefs

    def addSwSystemconstantValueSetRef(self, value: Optional[RefType]) -> "PredefinedVariant":
        """
        This ist the set of Systemconstant Values contributing to the predefined variant.
        """
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

    # SwSystemconstValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAnnotations               [x] impl  [ ] docstring  [ ] test
    # [ ] addAnnotation                [x] impl  [ ] docstring  [ ] test
    # [ ] getSwSystemconstRef          [x] impl  [ ] docstring  [ ] test
    # [ ] setSwSystemconstRef          [x] impl  [ ] docstring  [ ] test
    # [ ] getValue                     [x] impl  [ ] docstring  [ ] test
    # [ ] setValue                     [x] impl  [ ] docstring  [ ] test

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


class SwSystemconstantValueSet(ARElement):
    """
    This meta-class represents the ability to specify a set of system constant values. Tags: atp.recommendedPackage=SwSystemconstantValueSets
    """

    # SwSystemconstantValueSet method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.25, p.258
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addSwSystemconstantValue    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwSystemconstantValues   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This is one particular value of a system constant.
        self.swSystemconstantValues: List[SwSystemconstValue] = []

    def addSwSystemconstantValue(self, value: Optional[SwSystemconstValue]) -> "SwSystemconstantValueSet":
        """
        This is one particular value of a system constant.
        """
        if value is not None:
            self.swSystemconstantValues.append(value)
        return self

    def getSwSystemconstantValues(self) -> List[SwSystemconstValue]:
        """
        This is one particular value of a system constant.
        """
        return self.swSystemconstantValues


class PostBuildVariantCondition(ARObject):
    """
    This class specifies the value which shall be assigned to a particular variant
    criterion in order to bind the variation point. If multiple criterion/value pairs
    are specified, they shall all match to bind the variation point. In other words
    binding can be represented by (criterion1 == value1) && (condition2 == value2) ...

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject
    Stereotypes: atpVariation
    Tags: vh.latestBindingTime=preCompileTime

    Attributes:
        matchingCriterionRef (PostBuildVariantCriterion): This is the
            criterion which needs to match the value in order to make the
            PostbuildVariantCondition to be true. (Multiplicity: 1)
        value (Integer): This is the particular value of the post-build
            variant criterion. (Multiplicity: 1)
    """

    # PostBuildVariantCondition method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.6, p.232
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMatchingCriterionRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMatchingCriterionRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValue                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is the criterion which needs to match the value in order to make the PostbuildVariantCondition to be true.
        self.matchingCriterionRef: RefType = None

        # This is the particular value of the post-build variant criterion.
        self.value: Optional[Integer] = None

    def getMatchingCriterionRef(self) -> RefType:
        """
        This is the criterion which needs to match the value in order to make the
        PostbuildVariantCondition to be true.
        """
        return self.matchingCriterionRef

    def setMatchingCriterionRef(self, value: RefType) -> "PostBuildVariantCondition":
        """
        This is the criterion which needs to match the value in order to make the
        PostbuildVariantCondition to be true. A None value is a no-op and does not
        overwrite an existing matchingCriterionRef.
        """
        if value is not None:
            self.matchingCriterionRef = value
        return self

    def getValue(self) -> Optional[Integer]:
        """
        This is the particular value of the post-build variant criterion.
        """
        return self.value

    def setValue(self, value: Optional[Integer]) -> "PostBuildVariantCondition":
        """
        This is the particular value of the post-build variant criterion. A None value
        is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class ConditionByFormula(ARObject):
    """
    This class represents a condition which is computed based on system constants
    according to the specified expression. The expected result is considered as boolean
    value. The result of the expression is interpreted as a condition. • "0" represents
    "false"; • a value other than zero is considered "true"

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString

    Attributes:
        bindingTime (BindingTimeEnum): This attribute specifies the point in time when
            condition may be evaluated at earliest. At this point in time all referenced
            system constants shall have a value. (Multiplicity: 1)
    """

    # ConditionByFormula method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.5, p.231
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBindingTime    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBindingTime    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute specifies the point in time when condition may be evaluated at earliest. At this point in time all referenced system constants shall have a value.
        self.bindingTime: Optional["BindingTimeEnum"] = None

    def getBindingTime(self) -> Optional["BindingTimeEnum"]:
        """
        This attribute specifies the point in time when condition may be evaluated at
        earliest. At this point in time all referenced system constants shall have a
        value.
        """
        return self.bindingTime

    def setBindingTime(self, value: Optional["BindingTimeEnum"]) -> "ConditionByFormula":
        """
        This attribute specifies the point in time when condition may be evaluated at
        earliest. At this point in time all referenced system constants shall have a
        value. A None value is a no-op and does not overwrite an existing bindingTime.
        """
        if value is not None:
            self.bindingTime = value
        return self


class VariationPoint(ARObject):
    """
    This meta-class represents the ability to express a "structural variation point".
    The container of the variation point is part of the selected variant if swSyscond
    evaluates to true and each postBuildVariantCriterion is fulfilled.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    Base: ARObject

    Attributes:
        blueprintCondition (DocumentationBlock): This represents a description
            that documents how the variation point shall be resolved when deriving
            objects from the blueprint. Note that variationPoints are not allowed
            within a blueprintCondition. (Multiplicity: 0..1)
        desc (MultiLanguageOverviewParagraph): This allows to describe shortly the
            purpose of the variation point. (Multiplicity: 0..1)
        formalBlueprintGenerator (BlueprintGenerator): This represents a description
            that documents how the variation point shall be resolved when deriving
            objects from the blueprint by using ARMQL. Note that variationPoints are
            not allowed within a formal BlueprintGenerator. (Multiplicity: 0..1)
        postBuildVariantConditions (List[PostBuildVariantCondition]): This is the
            set of post build variant conditions which all shall be fulfilled in
            order to (postbuild) bind the variation point. (Multiplicity: *)
        sdg (Sdg): An optional special data group is attached to every variation
            point. These data can be used by external software systems to attach
            application specific data. For example, a variant management system
            might add an identifier, an URL or a specific classifier.
            (Multiplicity: 0..1)
        shortLabel (Identifier): This provides a name to the particular variation
            point to support the RTE generator. It is necessary for supporting
            splitable aggregations and if binding time is later than
            codeGenerationTime, as well as some RTE conditions. It needs to be
            unique with in the enclosing Identifiables with the same ShortName.
            (Multiplicity: 0..1)
        swSyscond (ConditionByFormula): This condition acts as Binding Function for
            the Variation Point. Note that the multiplicity is 0..1 in order to
            support pure postBuild variants. (Multiplicity: 0..1)
    """

    # VariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.4, p.226
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBlueprintCondition             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBlueprintCondition             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDesc                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFormalBlueprintGenerator       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFormalBlueprintGenerator       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantConditions     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPostBuildVariantCondition      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSdg                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdg                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShortLabel                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setShortLabel                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwSyscond                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwSyscond                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents a description that documents how the variation point shall be resolved when deriving objects from the blueprint. Note that variationPoints are not allowed within a blueprintCondition.
        self.blueprintCondition: Optional[DocumentationBlock] = None

        # This allows to describe shortly the purpose of the variation point.
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

        # This represents a description that documents how the variation point shall be resolved when deriving objects from the blueprint by using ARMQL. Note that variationPoints are not allowed within a formal BlueprintGenerator.
        self.formalBlueprintGenerator: Optional[BlueprintGenerator] = None

        # This is the set of post build variant conditions which all shall be fulfilled in order to (postbuild) bind the variation point.
        self.postBuildVariantConditions: List["PostBuildVariantCondition"] = []

        # An optional special data group is attached to every variation point. These data can be used by external software systems to attach application specific data. For example, a variant management system might add an identifier, an URL or a specific classifier.
        self.sdg: Optional[Sdg] = None

        # This provides a name to the particular variation point to support the RTE generator. It is necessary for supporting splitable aggregations and if binding time is later than codeGenerationTime, as well as some RTE conditions. It needs to be unique with in the enclosing Identifiables with the same ShortName.
        self.shortLabel: Optional[Identifier] = None

        # This condition acts as Binding Function for the Variation Point. Note that the multiplicity is 0..1 in order to support pure postBuild variants.
        self.swSyscond: Optional["ConditionByFormula"] = None

    def getBlueprintCondition(self) -> Optional[DocumentationBlock]:
        """
        This represents a description that documents how the variation point shall be
        resolved when deriving objects from the blueprint. Note that variationPoints
        are not allowed within a blueprintCondition.
        """
        return self.blueprintCondition

    def setBlueprintCondition(self, value: Optional[DocumentationBlock]) -> "VariationPoint":
        """
        This represents a description that documents how the variation point shall be
        resolved when deriving objects from the blueprint. Note that variationPoints
        are not allowed within a blueprintCondition. A None value is a no-op and does
        not overwrite an existing blueprintCondition.
        """
        if value is not None:
            self.blueprintCondition = value
        return self

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This allows to describe shortly the purpose of the variation point.
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "VariationPoint":
        """
        This allows to describe shortly the purpose of the variation point. A None value
        is a no-op and does not overwrite an existing desc.
        """
        if value is not None:
            self.desc = value
        return self

    def getFormalBlueprintGenerator(self) -> Optional[BlueprintGenerator]:
        """
        This represents a description that documents how the variation point shall be
        resolved when deriving objects from the blueprint by using ARMQL. Note that
        variationPoints are not allowed within a formal BlueprintGenerator.
        """
        return self.formalBlueprintGenerator

    def setFormalBlueprintGenerator(self, value: Optional[BlueprintGenerator]) -> "VariationPoint":
        """
        This represents a description that documents how the variation point shall be
        resolved when deriving objects from the blueprint by using ARMQL. Note that
        variationPoints are not allowed within a formal BlueprintGenerator. A None value
        is a no-op and does not overwrite an existing formalBlueprintGenerator.
        """
        if value is not None:
            self.formalBlueprintGenerator = value
        return self

    def getPostBuildVariantConditions(self) -> List["PostBuildVariantCondition"]:
        """
        This is the set of post build variant conditions which all shall be fulfilled in
        order to (postbuild) bind the variation point.
        """
        return self.postBuildVariantConditions

    def addPostBuildVariantCondition(self, value: "PostBuildVariantCondition") -> "VariationPoint":
        """
        This is the set of post build variant conditions which all shall be fulfilled in
        order to (postbuild) bind the variation point. A None value is a no-op and is
        not appended.
        """
        if value is not None:
            self.postBuildVariantConditions.append(value)
        return self

    def getSdg(self) -> Optional[Sdg]:
        """
        An optional special data group is attached to every variation point. These data
        can be used by external software systems to attach application specific data.
        For example, a variant management system might add an identifier, an URL or a
        specific classifier.
        """
        return self.sdg

    def setSdg(self, value: Optional[Sdg]) -> "VariationPoint":
        """
        An optional special data group is attached to every variation point. These data
        can be used by external software systems to attach application specific data.
        For example, a variant management system might add an identifier, an URL or a
        specific classifier. A None value is a no-op and does not overwrite an existing
        sdg.
        """
        if value is not None:
            self.sdg = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This provides a name to the particular variation point to support the RTE
        generator. It is necessary for supporting splitable aggregations and if binding
        time is later than codeGenerationTime, as well as some RTE conditions. It needs
        to be unique with in the enclosing Identifiables with the same ShortName.
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "VariationPoint":
        """
        This provides a name to the particular variation point to support the RTE
        generator. It is necessary for supporting splitable aggregations and if binding
        time is later than codeGenerationTime, as well as some RTE conditions. It needs
        to be unique with in the enclosing Identifiables with the same ShortName. A None
        value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self

    def getSwSyscond(self) -> Optional["ConditionByFormula"]:
        """
        This condition acts as Binding Function for the Variation Point. Note that the
        multiplicity is 0..1 in order to support pure postBuild variants.
        """
        return self.swSyscond

    def setSwSyscond(self, value: Optional["ConditionByFormula"]) -> "VariationPoint":
        """
        This condition acts as Binding Function for the Variation Point. Note that the
        multiplicity is 0..1 in order to support pure postBuild variants. A None value is
        a no-op and does not overwrite an existing swSyscond.
        """
        if value is not None:
            self.swSyscond = value
        return self
