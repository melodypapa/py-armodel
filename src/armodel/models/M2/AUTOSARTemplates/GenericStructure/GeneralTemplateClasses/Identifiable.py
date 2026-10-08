"""
This module contains classes for representing identifiable elements in AUTOSAR models
in the GenericStructure module.
"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    FMAttributeValue,
    DdsCpServiceInstanceEvent,
    DdsCpServiceInstanceOperation,
    DdsDeadline,
    DdsDestinationOrder,
    DdsDurability,
    DdsDurabilityService,
    DdsHistory,
    DdsLatencyBudget,
    DdsLifespan,
    DdsLiveliness,
    DdsOwnership,
    DdsOwnershipStrength,
    DdsReliability,
    DdsResourceLimits,
    DdsTopicData,
    DdsTransportPriority,
    DiagnosticAbstractParameter,
    DiagnosticParameter,
    RoleBasedResourceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyVersionString,
    Boolean,
    CategoryString,
    DiagnosticDebounceBehaviorEnum,
    FMFeatureSelectionState,
    Identifier,
    Limit,
    Numerical,
    PositiveInteger,
    RefType,
    String,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from abc import ABC
from typing import Dict, List, Optional, TYPE_CHECKING, Union, cast

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes, FMConditionByFeaturesAndSwSystemconsts
    from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph
    from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SingleLanguageLongName
    from armodel.models.M2.MSR.Documentation.Annotation import Annotation
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceAlgorithm, DiagEventDebounceCounterBased, DiagEventDebounceMonitorInternal, DiagEventDebounceTimeBased
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class Referrable(ARObject, ABC):
    """
    Instances of this class can be referred to by their identifier (while adhering to namespace borders).
    """

    # Referrable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.10, p.63
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] shortName              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] shortName              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getShortName           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getParent              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] full_name              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFullName            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addShortNameFragment   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortNameFragments  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Referrable:
            raise TypeError("Referrable is an abstract class.")

        ARObject.__init__(self)

        self.parent: ARObject = parent

        self.short_name: str = short_name

        # This specifies how the Referrable.shortName is composed of several shortNameFragments. Tags: xml.sequenceOffset=-90
        self.shortNameFragments: List[ShortNameFragment] = []

    @property
    def shortName(self) -> str:
        """str: The short name of this referrable element."""
        return self.short_name

    @shortName.setter
    def shortName(self, value: str):
        self.short_name = value

    def getShortName(self) -> str:
        """
        Gets the short name of this referrable element.

        Returns:
            The short name of this element
        """
        return self.short_name

    def getParent(self) -> ARObject:
        """
        Gets the parent of this referrable element.

        Returns:
            The parent ARObject
        """
        return self.parent

    @property
    def full_name(self) -> str:
        """
        str: The full name of this element, including the parent's full name.
        """
        return cast(Identifiable, self.parent).full_name + "/" + self.short_name

    def getFullName(self) -> str:
        """
        Gets the full name of this element, including the parent's full name.

        Returns:
            The full name of this element
        """
        return self.full_name

    def addShortNameFragment(self, value: Optional[ShortNameFragment]) -> Referrable:
        """
        Adds a short name fragment that specifies how the shortName is composed of several shortNameFragments.
        A None value is a no-op and does not append anything.

        Args:
            value: The ShortNameFragment to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortNameFragments.append(value)
        return self

    def getShortNameFragments(self) -> List[ShortNameFragment]:
        """
        Gets the short name fragments that specify how the shortName is composed of several shortNameFragments.

        Returns:
            List of ShortNameFragment instances
        """
        return self.shortNameFragments


class ShortNameFragment(ARObject):
    """
    This class describes how the Referrable.shortName is composed of several shortNameFragments.
    """

    # ShortNameFragment method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.13, p.64
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFragment     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFragment     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRole         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This specifies a single shortName (fragment) which is part of the composed shortName. Tags: xml.sequenceOffset=20
        self.fragment: Optional[Identifier] = None

        # This specifies the role of fragment to define e.g. the order of the fragments. Tags: xml.sequenceOffset=10
        self.role: Optional[String] = None

    def getFragment(self) -> Optional[Identifier]:
        """
        This specifies a single shortName (fragment) which is part of the composed shortName.
        """
        return self.fragment

    def setFragment(self, value: Optional[Identifier]) -> ShortNameFragment:
        """
        This specifies a single shortName (fragment) which is part of the composed shortName. A None value is a no-op and does not overwrite an existing fragment.
        """
        if value is not None:
            self.fragment = value
        return self

    def getRole(self) -> Optional[String]:
        """
        This specifies the role of fragment to define e.g. the order of the fragments.
        """
        return self.role

    def setRole(self, value: Optional[String]) -> ShortNameFragment:
        """
        This specifies the role of fragment to define e.g. the order of the fragments. A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self


class MultilanguageReferrable(Referrable, ABC):
    """
    Instances of this class can be referred to by their identifier (while adhering to namespace borders). They also may have a longName. But they are not considered to contribute substantially to the overall structure of an AUTOSAR description. In particular it does not contain other Referrables.
    """

    # MultilanguageReferrable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.11, p.64
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLongName   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLongName   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is MultilanguageReferrable:
            raise TypeError("MultilanguageReferrable is an abstract class.")

        super().__init__(parent, short_name)

        # This specifies the long name of the object. Long name is targeted to human readers and acts like a headline.
        self.longName: Optional[MultilanguageLongName] = None

    def getLongName(self) -> Optional[MultilanguageLongName]:
        """
        This specifies the long name of the object. Long name is targeted to human readers and acts like a headline.
        """
        return self.longName

    def setLongName(self, value: Optional[MultilanguageLongName]) -> MultilanguageReferrable:
        """
        This specifies the long name of the object. Long name is targeted to human readers and acts like a headline.
        A None value is a no-op and does not overwrite an existing longName.

        Args:
            value: The long name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.longName = value
        return self


class SingleLanguageReferrable(Referrable, ABC):
    """
    Instances of this class can be referred to by their identifier (while adhering to namespace borders). They also may have a longName but in one language only. Specializations of this class only occur as inline elements in one particular language. Therefore they aggregate But they are not considered to contribute substantially to the overall structure of an AUTOSAR description. In particular it does not contain other Referrables.
    """

    # SingleLanguageReferrable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.12, p.64
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLongName1   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLongName1   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is SingleLanguageReferrable:
            raise TypeError("SingleLanguageReferrable is an abstract class.")

        super().__init__(parent, short_name)

        # This specifies the long name of the object. The role is longName1 for compatibiilty to ASAM FSX
        self.longName1: Optional[SingleLanguageLongName] = None

    def getLongName1(self) -> Optional[SingleLanguageLongName]:
        """
        This specifies the long name of the object. The role is longName1 for compatibiilty to ASAM FSX
        """
        return self.longName1

    def setLongName1(self, value: Optional[SingleLanguageLongName]) -> SingleLanguageReferrable:
        """
        This specifies the long name of the object. The role is longName1 for compatibiilty to ASAM FSX. A None value is a no-op and does not overwrite an existing longName1.
        """
        if value is not None:
            self.longName1 = value
        return self


class Identifiable(MultilanguageReferrable, ABC):
    """
    Instances of this class can be referred to by their identifier (within the namespace borders). In addition to this, Identifiables are objects which contribute significantly to the overall structure of an AUTOSAR description. In particular, Identifiables might contain Identifiables.
    """

    # Identifiable method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.4, p.61 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAdminData       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAdminData       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] removeAdminData    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAnnotation      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAnnotations     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getCategory        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCategory        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDesc            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDesc            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIntroduction    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUuid            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUuid            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Internal members (no spec counterpart — element-collection infra, cf. the CollectableElement
    # decision in docs/examples/method_deviation_by_class_v2.md). Owned here because some direct
    # subclasses, e.g. Fibex PhysicalChannel, are not CollectableElement:
    # [x] getTotalReferrableElement    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] removeReferrableElement      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReferrableElements        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addReferrableElement         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReferrableElement         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] IsReferrableElementExists    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # Deviation RESOLVED: variationPoint was never a Table 4.4 attribute of
    # Identifiable (the IDENTIFIABLE group carries no VARIATION-POINT in the XSD).
    # Capability now lives in the VariationPointCapable mixin, anchored on the
    # XSD atpVariation classes (see VariationPointCapable.py and
    # docs/superpowers/plans/vp_anchors.txt).

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Identifiable:
            raise TypeError("Identifiable is an abstract class.")

        super().__init__(parent, short_name)

        # This represents the administrative data for the identifiable object.
        self.adminData: Optional[AdminData] = None

        # Possibility to provide additional notes while defining a model element (e.g. the ECU Configuration Parameter Values). These are not intended as documentation but are mere design notes.
        self.annotations: List[Annotation] = []

        # The category is a keyword that specializes the semantics of the Identifiable. It affects the expected existence of attributes and the applicability of constraints.
        self.category: Optional[CategoryString] = None

        # This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the object in question. More elaborate documentation, (in particular how the object is built or used) should go to "introduction".
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

        # This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock.
        self.introduction: Optional[DocumentationBlock] = None

        # The purpose of this attribute is to provide a globally unique identifier for an instance of a meta-class. The values of this attribute should be globally unique strings prefixed by the type of identifier. For example, to include a DCE UUID as defined by The Open Group, the UUID would be preceded by "DCE:". The values of this attribute may be used to support merging of different AUTOSAR models. The form of the UUID (Universally Unique Identifier) is taken from a standard defined by the Open Group (was Open Software Foundation). This standard is widely used, including by Microsoft for COM (GUIDs) and by many companies for DCE, which is based on CORBA. The method for generating these 128-bit IDs is published in the standard and the effectiveness and uniqueness of the IDs is not in practice disputed. If the id namespace is omitted, DCE is assumed. An example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid attribute has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        self.uuid: Optional[String] = None

        # Element collection registry (shared infra; kept on Identifiable because some direct subclasses, e.g. Fibex PhysicalChannel, are not CollectableElement).
        self.referrableElements: List[Referrable] = []
        self.referrableElementMappings: Dict[str, List[Referrable]] = {}

    def getAdminData(self) -> Optional[AdminData]:
        """
        This represents the administrative data for the identifiable object.
        """
        return self.adminData

    def setAdminData(self, value: Optional[AdminData]) -> Identifiable:
        """
        This represents the administrative data for the identifiable object. Only sets the value if it is not None.
        """
        if value is not None:
            self.adminData = value
        return self

    def removeAdminData(self) -> None:
        """
        Removes the administrative data for this identifiable element.
        """
        self.adminData = None

    def addAnnotation(self, annotation: Optional[Annotation]) -> Identifiable:
        """
        Possibility to provide additional notes while defining a model element (e.g. the ECU Configuration Parameter Values). These are not intended as documentation but are mere design notes. A None value is a no-op and does not append anything.
        """
        if annotation is not None:
            self.annotations.append(annotation)
        return self

    def getAnnotations(self) -> List[Annotation]:
        """
        Possibility to provide additional notes while defining a model element (e.g. the ECU Configuration Parameter Values). These are not intended as documentation but are mere design notes.
        """
        return self.annotations

    def getCategory(self) -> Optional[CategoryString]:
        """
        The category is a keyword that specializes the semantics of the Identifiable. It affects the expected existence of attributes and the applicability of constraints.
        """
        return self.category

    def setCategory(self, value: Optional[Union[CategoryString, str]]) -> Identifiable:
        """
        The category is a keyword that specializes the semantics of the Identifiable. It affects the expected existence of attributes and the applicability of constraints. Only sets the value if it is not None.
        """
        if value is not None:
            if isinstance(value, str):
                self.category = CategoryString().setValue(value)
            else:
                self.category = value
        return self

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the object in question. More elaborate documentation, (in particular how the object is built or used) should go to "introduction".
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> Identifiable:
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the object in question. More elaborate documentation, (in particular how the object is built or used) should go to "introduction". Only sets the value if it is not None.
        """
        if value is not None:
            self.desc = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> Identifiable:
        """
        This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock. Only sets the value if it is not None.
        """
        if value is not None:
            self.introduction = value
        return self

    def getUuid(self) -> Optional[String]:
        """
        The purpose of this attribute is to provide a globally unique identifier for an instance of a meta-class. The values of this attribute should be globally unique strings prefixed by the type of identifier. For example, to include a DCE UUID as defined by The Open Group, the UUID would be preceded by "DCE:". The values of this attribute may be used to support merging of different AUTOSAR models. The form of the UUID (Universally Unique Identifier) is taken from a standard defined by the Open Group (was Open Software Foundation). This standard is widely used, including by Microsoft for COM (GUIDs) and by many companies for DCE, which is based on CORBA. The method for generating these 128-bit IDs is published in the standard and the effectiveness and uniqueness of the IDs is not in practice disputed. If the id namespace is omitted, DCE is assumed. An example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid attribute has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        """
        return self.uuid

    def setUuid(self, value: Optional[String]) -> Identifiable:
        """
        The purpose of this attribute is to provide a globally unique identifier for an instance of a meta-class. The values of this attribute should be globally unique strings prefixed by the type of identifier. For example, to include a DCE UUID as defined by The Open Group, the UUID would be preceded by "DCE:". The values of this attribute may be used to support merging of different AUTOSAR models. The form of the UUID (Universally Unique Identifier) is taken from a standard defined by the Open Group (was Open Software Foundation). This standard is widely used, including by Microsoft for COM (GUIDs) and by many companies for DCE, which is based on CORBA. The method for generating these 128-bit IDs is published in the standard and the effectiveness and uniqueness of the IDs is not in practice disputed. If the id namespace is omitted, DCE is assumed. An example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid attribute has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp. Only sets the value if it is not None.
        """
        if value is not None:
            self.uuid = value
        return self

    def getTotalReferrableElement(self) -> int:
        """
        Gets the total number of elements in this collection.

        Returns:
            The count of elements in the collection
        """
        return len(self.referrableElements)

    def removeReferrableElement(self, short_name: str, type=None) -> None:
        """
        Removes an element from this collection.

        Args:
            short_name: The short name of the element to remove
            type: The type of element to remove (optional)
        """
        if short_name not in self.referrableElementMappings:
            raise KeyError("Invalid key <%s> for removing element" % short_name)
        if type is None:
            item = self.referrableElementMappings[short_name][0]
        else:
            item = next(filter(lambda a: isinstance(a, type), self.referrableElementMappings[short_name]))
        if item is not None:
            self.referrableElements.remove(item)
            self.referrableElementMappings[short_name].remove(item)

    def getReferrableElements(self) -> List[Referrable]:
        """
        Gets the list of elements in this collection.

        Returns:
            List of Referrable instances
        """
        return self.referrableElements

    def addReferrableElement(self, element: Referrable) -> None:
        """
        Adds an element to this collection.

        Args:
            element: The element to add
        """
        short_name = element.getShortName()
        if not self.IsReferrableElementExists(short_name, type(element)):
            self.referrableElements.append(element)
            if short_name not in self.referrableElementMappings:
                self.referrableElementMappings[short_name] = []
            self.referrableElementMappings[short_name].append(element)

    def getReferrableElement(self, short_name: str, type=None) -> Optional[Referrable]:
        """
        Gets an element from this collection by short name and type.

        Args:
            short_name: The short name of the element to find
            type: The type of element to find (optional)

        Returns:
            The found Referrable instance, or None if not found
        """
        if short_name not in self.referrableElementMappings:
            return None
        if type is not None:
            result = list(filter(lambda a: isinstance(a, type), self.referrableElementMappings[short_name]))
            if len(result) == 0:
                return None
            return result[0]
        return self.referrableElementMappings[short_name][0]

    def IsReferrableElementExists(self, short_name: str, type=None) -> bool:
        """
        Checks if an element with the specified short name and type exists in this collection.

        Args:
            short_name: The short name of the element to check
            type: The type of element to check (optional)

        Returns:
            True if the element exists, False otherwise
        """
        if type is None:
            return short_name in self.referrableElementMappings
        if short_name in self.referrableElementMappings:
            return any(isinstance(a, type) for a in self.referrableElementMappings[short_name])
        return False


# Initialize the CommonStructure package before any import that transitively touches
# AbstractStructure: AbstractStructure's own import of AbstractBlueprintStructure requires
# the CommonStructure package to be present in sys.modules (Task 15 bootstrap-cycle fix).


class Describable(ARObject, ABC):
    """
    This meta-class represents the ability to add a descriptive documentation to non identifiable elements.
    """

    # Describable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.25, p.438
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAdminData                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAdminData                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] removeAdminData              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCategory                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCategory                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDesc                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIntroduction              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIntroduction              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is Describable:
            raise TypeError("Describable is an abstract class.")

        super().__init__()

        # This represents the administrative data for the describable object. Stereotypes: atpSplitable Tags: atp.Splitkey=adminData xml.sequenceOffset=-20
        self.adminData: Optional[AdminData] = None

        # The category is a keyword that specializes the semantics of the Describable. It affects the expected existence of attributes and the applicability of constraints. Tags: xml.sequenceOffset=-50
        self.category: Optional[CategoryString] = None

        # This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the object in question. More elaborate documentation, (in particular how the object is built or used) should go to "introduction". Tags: xml.sequenceOffset=-60
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

        # This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock. Tags: xml.sequenceOffset=-30
        self.introduction: Optional[DocumentationBlock] = None

    def getAdminData(self) -> Optional[AdminData]:
        """
        This represents the administrative data for the describable object. Stereotypes: atpSplitable Tags: atp.Splitkey=adminData xml.sequenceOffset=-20
        """
        return self.adminData

    def setAdminData(self, value: Optional[AdminData]):
        """
        This represents the administrative data for the describable object. Stereotypes: atpSplitable Tags: atp.Splitkey=adminData xml.sequenceOffset=-20

        Args:
            value: The administrative data to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.adminData = value
        return self

    def removeAdminData(self):
        """
        Removes the administrative data for this describable element.
        """
        self.adminData = None

    def getCategory(self) -> Optional[CategoryString]:
        """
        The category is a keyword that specializes the semantics of the Describable. It affects the expected existence of attributes and the applicability of constraints. Tags: xml.sequenceOffset=-50
        """
        return self.category

    def setCategory(self, value: Optional[CategoryString]):
        """
        The category is a keyword that specializes the semantics of the Describable. It affects the expected existence of attributes and the applicability of constraints. Tags: xml.sequenceOffset=-50

        Args:
            value: The category to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.category = value
        return self

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the object in question. More elaborate documentation, (in particular how the object is built or used) should go to "introduction". Tags: xml.sequenceOffset=-60
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]):
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the object in question. More elaborate documentation, (in particular how the object is built or used) should go to "introduction". Tags: xml.sequenceOffset=-60

        Args:
            value: The description to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.desc = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock. Tags: xml.sequenceOffset=-30
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]):
        """
        This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock. Tags: xml.sequenceOffset=-30

        Args:
            value: The introduction documentation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.introduction = value
        return self


class SpecElementReference(Identifiable, ABC):
    pass


class DataFormatElementReference(SpecElementReference, ABC):
    pass


class AbstractClassTailoring(DataFormatElementReference):
    pass


class AbstractSecurityEventFilter(Identifiable, ABC):
    pass


class DataFormatElementScope(DataFormatElementReference, ABC):
    pass


class AttributeTailoring(DataFormatElementScope, ABC):
    pass


class AggregationTailoring(AttributeTailoring):
    pass


class BlockState(Identifiable):
    pass


class ClassContentConditional(Identifiable):
    pass


class ConcreteClassTailoring(DataFormatElementScope):
    pass


class ConstraintTailoring(DataFormatElementScope):
    pass


class CpSoftwareClusterResource(Identifiable):
    """Represents a single resource required or provided by a CP Software Cluster. Tags: atp.recommendedPackage=Resources"""

    # CpSoftwareClusterResource method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.44, p.271
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDependentResource      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDependentResources     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getGlobalResourceId       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGlobalResourceId       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIsMandatory            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIsMandatory            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Link to a resource which depends on this resource to implement them.
        self.dependentResources: List[RoleBasedResourceDependency] = []

        # A unique identifiers per resource used for the connection process. The identifier is required to be unique in the scope of a single machine. If software clusters are designed to be reused on multiple machines the uniqueness requirements applies for all the intended machines.
        self.globalResourceId: Optional[PositiveInteger] = None

        # This attribute indicates, that the resource is mandatory to operate the Software Cluster. If the resource is not provided on the machine the connection process of any Software Cluster requiring this resource gets aborted.
        self.isMandatory: Optional[Boolean] = None

    def addDependentResource(self, value: Optional[RoleBasedResourceDependency]) -> CpSoftwareClusterResource:
        """
        Link to a resource which depends on this resource to implement them.
        A None value is a no-op and does not append a dependentResource.
        """
        if value is not None:
            self.dependentResources.append(value)
        return self

    def getDependentResources(self) -> List[RoleBasedResourceDependency]:
        """
        Link to a resource which depends on this resource to implement them.
        """
        return self.dependentResources

    def getGlobalResourceId(self) -> Optional[PositiveInteger]:
        """
        A unique identifiers per resource used for the connection process. The identifier is required to be unique in the scope of a single machine. If software clusters are designed to be reused on multiple machines the uniqueness requirements applies for all the intended machines.
        """
        return self.globalResourceId

    def setGlobalResourceId(self, value: Optional[PositiveInteger]) -> CpSoftwareClusterResource:
        """
        A unique identifiers per resource used for the connection process. The identifier is required to be unique in the scope of a single machine. If software clusters are designed to be reused on multiple machines the uniqueness requirements applies for all the intended machines.
        A None value is a no-op and does not overwrite an existing globalResourceId.
        """
        if value is not None:
            self.globalResourceId = value
        return self

    def getIsMandatory(self) -> Optional[Boolean]:
        """
        This attribute indicates, that the resource is mandatory to operate the Software Cluster. If the resource is not provided on the machine the connection process of any Software Cluster requiring this resource gets aborted.
        """
        return self.isMandatory

    def setIsMandatory(self, value: Optional[Boolean]) -> CpSoftwareClusterResource:
        """
        This attribute indicates, that the resource is mandatory to operate the Software Cluster. If the resource is not provided on the machine the connection process of any Software Cluster requiring this resource gets aborted.
        A None value is a no-op and does not overwrite an existing isMandatory.
        """
        if value is not None:
            self.isMandatory = value
        return self


class CpSoftwareClusterCommunicationResource(CpSoftwareClusterResource):
    pass


class CpSoftwareClusterServiceResource(CpSoftwareClusterResource):
    pass


class DiagnosticAuthTransmitCertificateEvaluation(Identifiable):
    """This meta-class represents the ability to configure a certificate evaluation in the context of a diagnostic authentication."""

    # DiagnosticAuthTransmitCertificateEvaluation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.59, p.101
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEvaluationId    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEvaluationId    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFunction        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFunction        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attributes represents the ID of the certificate evaluation.
        self.evaluationId: Optional[PositiveInteger] = None

        # This attribute represents the description of the actual semantics of the corresponding evaluation ID.
        self.function: Optional[String] = None

    def getEvaluationId(self) -> Optional[PositiveInteger]:
        """
        This attributes represents the ID of the certificate evaluation.
        """
        return self.evaluationId

    def setEvaluationId(self, value: Optional[PositiveInteger]) -> DiagnosticAuthTransmitCertificateEvaluation:
        """
        This attributes represents the ID of the certificate evaluation.

        A None value is a no-op and does not overwrite an existing evaluationId.
        """
        if value is not None:
            self.evaluationId = value
        return self

    def getFunction(self) -> Optional[String]:
        """
        This attribute represents the description of the actual semantics of the corresponding evaluation ID.
        """
        return self.function

    def setFunction(self, value: Optional[String]) -> DiagnosticAuthTransmitCertificateEvaluation:
        """
        This attribute represents the description of the actual semantics of the corresponding evaluation ID.

        A None value is a no-op and does not overwrite an existing function.
        """
        if value is not None:
            self.function = value
        return self


class DiagnosticDataElement(Identifiable, VariationPointCapable):
    """
    This meta-class represents the ability to describe a concrete piece of data to be taken into account for diagnostic purposes.

    [constr_1394] Value of DiagnosticDataElement.maxNumberOfElements depending on its existence: If the attribute DiagnosticDataElement.maxNumberOfElements exists then its value shall be greater than 0 at the time when the DEXT is complete.
    """

    # DiagnosticDataElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.9, p.41
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArraySizeSemantics     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArraySizeSemantics     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumberOfElements    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumberOfElements    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getScalingInfoSize        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setScalingInfoSize        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwDataDefProps         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwDataDefProps         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)
    #
    # VP-capable per Rule 0020: XSD group DIAGNOSTIC-DATA-ELEMENT (AUTOSAR_00052.xsd
    # l.34124) carries VARIATION-POINT with "Applicable for:
    # DiagnosticAbstractParameter.dataElement", sequenceOffset=10000 → last.
    # swDataDefProps is a plain ARObject child (no Referrable) → set/get pair per
    # Rule 0001.6, serialized through the shared SW-DATA-DEF-PROPS helpers.
    # ArraySizeSemanticsEnum / SwDataDefProps are cross-package types imported back
    # into this package — TYPE_CHECKING annotation names per the file-wide pattern
    # (AdminData, Annotation, …); a bottom-of-module runtime import explodes the
    # CommonStructure hub mid-bootstrap (Rule 0005 deviation recorded), so nothing
    # pins those two annotations at runtime.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute controls the meaning of the value of the array size.
        self.arraySizeSemantics: Optional[ArraySizeSemanticsEnum] = None

        # The existence of this attribute turns the data instance into an array of data. The attribute determines the size of the array in terms of how many elements the array can take.
        self.maxNumberOfElements: Optional[PositiveInteger] = None

        # Size in bytes of scaling information for the DiagnosticData Element if used with DiagnosticReadScalingDataBy Identifier
        self.scalingInfoSize: Optional[PositiveInteger] = None

        # This property allows to specify data definition properties in order to support the definition of e.g. computation formulae and data constraints.
        self.swDataDefProps: Optional[SwDataDefProps] = None

    def getArraySizeSemantics(self) -> Optional[ArraySizeSemanticsEnum]:
        """
        This attribute controls the meaning of the value of the array size.
        """
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value: Optional[ArraySizeSemanticsEnum]) -> DiagnosticDataElement:
        """
        This attribute controls the meaning of the value of the array size.
        A None value is a no-op and does not overwrite an existing arraySizeSemantics.
        """
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getMaxNumberOfElements(self) -> Optional[PositiveInteger]:
        """
        The existence of this attribute turns the data instance into an array of data. The attribute determines the size of the array in terms of how many elements the array can take.
        """
        return self.maxNumberOfElements

    def setMaxNumberOfElements(self, value: Optional[PositiveInteger]) -> DiagnosticDataElement:
        """
        The existence of this attribute turns the data instance into an array of data. The attribute determines the size of the array in terms of how many elements the array can take.
        A None value is a no-op and does not overwrite an existing maxNumberOfElements.
        """
        if value is not None:
            self.maxNumberOfElements = value
        return self

    def getScalingInfoSize(self) -> Optional[PositiveInteger]:
        """
        Size in bytes of scaling information for the DiagnosticData Element if used with DiagnosticReadScalingDataBy Identifier
        """
        return self.scalingInfoSize

    def setScalingInfoSize(self, value: Optional[PositiveInteger]) -> DiagnosticDataElement:
        """
        Size in bytes of scaling information for the DiagnosticData Element if used with DiagnosticReadScalingDataBy Identifier
        A None value is a no-op and does not overwrite an existing scalingInfoSize.
        """
        if value is not None:
            self.scalingInfoSize = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        This property allows to specify data definition properties in order to support the definition of e.g. computation formulae and data constraints.
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> DiagnosticDataElement:
        """
        This property allows to specify data definition properties in order to support the definition of e.g. computation formulae and data constraints.
        A None value is a no-op and does not overwrite an existing swDataDefProps.
        """
        if value is not None:
            self.swDataDefProps = value
        return self


class DiagnosticDebounceAlgorithmProps(Identifiable):
    """Defines properties for the debounce algorithm class."""

    # DiagnosticDebounceAlgorithmProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.187, p.196
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDebounceAlgorithm                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDiagEventDebounceCounterBased    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagEventDebounceMonitorInternal [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagEventDebounceTimeBased       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDebounceBehavior                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDebounceBehavior                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDebounceCounterStorage              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDebounceCounterStorage              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the actual debounce algorithm.
        self.debounceAlgorithm: Optional[DiagEventDebounceAlgorithm] = None

        # This attribute defines how the event debounce algorithm will behave, if a related enable condition is not fulfilled or ControlDTCSetting of the related event is disabled. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.debounceBehavior: Optional[DiagnosticDebounceBehaviorEnum] = None

        # Switch to store the debounce counter value non-volatile or not. true: debounce counter value shall be stored non-volatile false: debounce counter value is volatile Please note that this attribute is not relevant for the adaptive platform.
        self.debounceCounterStorage: Optional[Boolean] = None

    def getDebounceAlgorithm(self) -> Optional[DiagEventDebounceAlgorithm]:
        """
        This represents the actual debounce algorithm.
        """
        return self.debounceAlgorithm

    def createDiagEventDebounceCounterBased(self, short_name: str) -> DiagEventDebounceCounterBased:
        """
        Creates and adds a counter-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new counter-based debounce algorithm

        Returns:
            The created DiagEventDebounceCounterBased instance
        """
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceCounterBased

        if not self.IsReferrableElementExists(short_name, DiagEventDebounceCounterBased):
            algorithm = DiagEventDebounceCounterBased(self, short_name)
            self.addReferrableElement(algorithm)
            self.debounceAlgorithm = algorithm
        return cast(DiagEventDebounceCounterBased, self.getReferrableElement(short_name, DiagEventDebounceCounterBased))

    def createDiagEventDebounceMonitorInternal(self, short_name: str) -> DiagEventDebounceMonitorInternal:
        """
        Creates and adds an internal monitor-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new internal monitor debounce algorithm

        Returns:
            The created DiagEventDebounceMonitorInternal instance
        """
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceMonitorInternal

        if not self.IsReferrableElementExists(short_name, DiagEventDebounceMonitorInternal):
            algorithm = DiagEventDebounceMonitorInternal(self, short_name)
            self.addReferrableElement(algorithm)
            self.debounceAlgorithm = algorithm
        return cast(DiagEventDebounceMonitorInternal, self.getReferrableElement(short_name, DiagEventDebounceMonitorInternal))

    def createDiagEventDebounceTimeBased(self, short_name: str) -> DiagEventDebounceTimeBased:
        """
        Creates and adds a time-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new time-based debounce algorithm

        Returns:
            The created DiagEventDebounceTimeBased instance
        """
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceTimeBased

        if not self.IsReferrableElementExists(short_name, DiagEventDebounceTimeBased):
            algorithm = DiagEventDebounceTimeBased(self, short_name)
            self.addReferrableElement(algorithm)
            self.debounceAlgorithm = algorithm
        return cast(DiagEventDebounceTimeBased, self.getReferrableElement(short_name, DiagEventDebounceTimeBased))

    def getDebounceBehavior(self) -> Optional[DiagnosticDebounceBehaviorEnum]:
        """
        This attribute defines how the event debounce algorithm will behave, if a related enable condition is not fulfilled or ControlDTCSetting of the related event is disabled.
        """
        return self.debounceBehavior

    def setDebounceBehavior(self, value: Optional[DiagnosticDebounceBehaviorEnum]) -> DiagnosticDebounceAlgorithmProps:
        """
        This attribute defines how the event debounce algorithm will behave, if a related enable condition is not fulfilled or ControlDTCSetting of the related event is disabled.
        A None value is a no-op and does not overwrite an existing debounceBehavior.
        """
        if value is not None:
            self.debounceBehavior = value
        return self

    def getDebounceCounterStorage(self) -> Optional[Boolean]:
        """
        Switch to store the debounce counter value non-volatile or not. true: debounce counter value shall be stored non-volatile false: debounce counter value is volatile Please note that this attribute is not relevant for the adaptive platform.
        """
        return self.debounceCounterStorage

    def setDebounceCounterStorage(self, value: Optional[Boolean]) -> DiagnosticDebounceAlgorithmProps:
        """
        Switch to store the debounce counter value non-volatile or not. true: debounce counter value shall be stored non-volatile false: debounce counter value is volatile Please note that this attribute is not relevant for the adaptive platform.
        A None value is a no-op and does not overwrite an existing debounceCounterStorage.
        """
        if value is not None:
            self.debounceCounterStorage = value
        return self


class DiagnosticFunctionInhibitSource(Identifiable):
    """This meta-class represents the ability to define an inhibition source in the context of the Fim configuration."""

    # DiagnosticFunctionInhibitSource method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.216, p.216
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setEventRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventGroupRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setEventGroupRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — the XSD carries DIAGNOSTIC-FUNCTION-INHIBIT-SOURCE
    # only via the INHIBIT-SOURCES wrapper of DIAGNOSTIC-FUNCTION-IDENTIFIER-INHIBIT
    # (AUTOSAR_00052.xsd l.37933-37944), whose parent is itself reachable only via the not-yet-wired
    # AR-PACKAGE/ELEMENTS choice (cf. DiagnosticFunctionIdentifierInhibit, commit 27e01b079);
    # reader/writer coverage lands with the consumer pass.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the alias event applicable for the referencing inhibition source.
        self.eventRef: Optional[RefType] = None

        # This represents the event group applicable for the referencing inhibition source.
        self.eventGroupRef: Optional[RefType] = None

    def getEventRef(self) -> Optional[RefType]:
        """
        This represents the alias event applicable for the referencing inhibition source.
        """
        return self.eventRef

    def setEventRef(self, value: Optional[RefType]) -> DiagnosticFunctionInhibitSource:
        """
        This represents the alias event applicable for the referencing inhibition source.
        A None value is a no-op and does not overwrite an existing eventRef.
        """
        if value is not None:
            self.eventRef = value
        return self

    def getEventGroupRef(self) -> Optional[RefType]:
        """
        This represents the event group applicable for the referencing inhibition source.
        """
        return self.eventGroupRef

    def setEventGroupRef(self, value: Optional[RefType]) -> DiagnosticFunctionInhibitSource:
        """
        This represents the event group applicable for the referencing inhibition source.
        A None value is a no-op and does not overwrite an existing eventGroupRef.
        """
        if value is not None:
            self.eventGroupRef = value
        return self


class DiagnosticParameterElement(DiagnosticAbstractParameter, Identifiable):
    """
    This meta-class represents an element of a DiagnosticParameter if the DiagnosticParameter represents a structure.

    [constr_10369] Existence of attributes of DiagnosticParameterElement depending on the value of attribute category: LEAF — arraySize No, subElement No, dataElement Yes; ARRAY — arraySize Yes, subElement Yes (if dataElement does not exist), dataElement Yes (if subElement does not exist); STRUCTURE — arraySize No, subElement Yes, dataElement No. This rule shall be imposed at the time when the DEXT is complete.
    """

    # DiagnosticParameterElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.6, p.36
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArraySize      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArraySize      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSubElement  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubElements    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    #
    # Inherited DiagnosticAbstractParameter attributes (bitOffset, dataElement,
    # parameterSize — Table 4.8) live on the base class queued within this batch.

    def __init__(self, parent: ARObject, short_name: str):
        DiagnosticAbstractParameter.__init__(self)
        Identifiable.__init__(self, parent, short_name)

        # This attribute indicates that the enclosing Diagnostic ParameterElement represents an array and configures the array size in terms of the number of elements of the array.
        self.arraySize: Optional[PositiveInteger] = None

        # This collection represents the sub-elements on the next lower level.
        self.subElements: List[DiagnosticParameterElement] = []

    def getArraySize(self) -> Optional[PositiveInteger]:
        """
        This attribute indicates that the enclosing Diagnostic ParameterElement represents an array and configures the array size in terms of the number of elements of the array.
        """
        return self.arraySize

    def setArraySize(self, value: Optional[PositiveInteger]) -> DiagnosticParameterElement:
        """
        This attribute indicates that the enclosing Diagnostic ParameterElement represents an array and configures the array size in terms of the number of elements of the array.
        A None value is a no-op and does not overwrite an existing arraySize.
        """
        if value is not None:
            self.arraySize = value
        return self

    def createSubElement(self, short_name: str) -> DiagnosticParameterElement:
        """
        This collection represents the sub-elements on the next lower level.
        The existing sub element is returned when the short name already exists (no duplicate creation).
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticParameterElement):
            sub_element = DiagnosticParameterElement(self, short_name)
            self.addReferrableElement(sub_element)
            self.subElements.append(sub_element)
        return cast(DiagnosticParameterElement, self.getReferrableElement(short_name, DiagnosticParameterElement))

    def getSubElements(self) -> List[DiagnosticParameterElement]:
        """
        This collection represents the sub-elements on the next lower level.
        """
        return self.subElements


class DiagnosticRoutineSubfunction(Identifiable, ABC):
    """This meta-class acts as an abstract base class to routine subfunctions."""

    # DiagnosticRoutineSubfunction method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.84, p.121
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAccessPermission  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAccessPermission  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticRoutineSubfunction:
            raise TypeError("DiagnosticRoutineSubfunction is an abstract class.")

        super().__init__(parent, short_name)

        # This reference represents the access permission of the owning routine subfunction.
        self.accessPermission: Optional[RefType] = None

    def getAccessPermission(self) -> Optional[RefType]:
        """
        This reference represents the access permission of the owning routine subfunction.
        """
        return self.accessPermission

    def setAccessPermission(self, value: Optional[RefType]) -> DiagnosticRoutineSubfunction:
        """
        This reference represents the access permission of the owning routine subfunction.

        A None value is a no-op and does not overwrite an existing accessPermission.
        """
        if value is not None:
            self.accessPermission = value
        return self


class DiagnosticRequestRoutineResults(DiagnosticRoutineSubfunction):
    """This meta-class represents the ability to define the result of a diagnostic routine execution."""

    # DiagnosticRequestRoutineResults method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.88, p.125
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRequest    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequest    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addResponse   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponse   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the request parameters.
        self.request: List[DiagnosticParameter] = []

        # This represents the response parameters.
        self.response: List[DiagnosticParameter] = []

    def addRequest(self, value: Optional[DiagnosticParameter]) -> DiagnosticRequestRoutineResults:
        """
        This represents the request parameters.
        A None value is a no-op and does not append a request.
        """
        if value is not None:
            self.request.append(value)
        return self

    def getRequest(self) -> List[DiagnosticParameter]:
        """
        This represents the request parameters.
        """
        return self.request

    def addResponse(self, value: Optional[DiagnosticParameter]) -> DiagnosticRequestRoutineResults:
        """
        This represents the response parameters.
        A None value is a no-op and does not append a response.
        """
        if value is not None:
            self.response.append(value)
        return self

    def getResponse(self) -> List[DiagnosticParameter]:
        """
        This represents the response parameters.
        """
        return self.response


class DiagnosticStartRoutine(DiagnosticRoutineSubfunction):
    """This represents the ability to start a diagnostic routine."""

    # DiagnosticStartRoutine method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.86, p.124
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRequest    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequest    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addResponse   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponse   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the request parameters.
        self.request: List[DiagnosticParameter] = []

        # This represents the response parameters.
        self.response: List[DiagnosticParameter] = []

    def addRequest(self, value: Optional[DiagnosticParameter]) -> DiagnosticStartRoutine:
        """
        This represents the request parameters.
        A None value is a no-op and does not append a request.
        """
        if value is not None:
            self.request.append(value)
        return self

    def getRequest(self) -> List[DiagnosticParameter]:
        """
        This represents the request parameters.
        """
        return self.request

    def addResponse(self, value: Optional[DiagnosticParameter]) -> DiagnosticStartRoutine:
        """
        This represents the response parameters.
        A None value is a no-op and does not append a response.
        """
        if value is not None:
            self.response.append(value)
        return self

    def getResponse(self) -> List[DiagnosticParameter]:
        """
        This represents the response parameters.
        """
        return self.response


class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):
    """This represents the ability to stop a diagnostic routine."""

    # DiagnosticStopRoutine method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.87, p.125
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRequest    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequest    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addResponse   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponse   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the request parameters.
        self.request: List[DiagnosticParameter] = []

        # This represents the response parameters.
        self.response: List[DiagnosticParameter] = []

    def addRequest(self, value: Optional[DiagnosticParameter]) -> DiagnosticStopRoutine:
        """
        This represents the request parameters.
        A None value is a no-op and does not append a request.
        """
        if value is not None:
            self.request.append(value)
        return self

    def getRequest(self) -> List[DiagnosticParameter]:
        """
        This represents the request parameters.
        """
        return self.request

    def addResponse(self, value: Optional[DiagnosticParameter]) -> DiagnosticStopRoutine:
        """
        This represents the response parameters.
        A None value is a no-op and does not append a response.
        """
        if value is not None:
            self.response.append(value)
        return self

    def getResponse(self) -> List[DiagnosticParameter]:
        """
        This represents the response parameters.
        """
        return self.response


class SpecElementScope(SpecElementReference, ABC):
    pass


class DocumentElementScope(SpecElementScope):
    pass


class FMAttributeDef(Identifiable):
    """
    This metaclass represents the ability to define attributes for a feature.
    """

    # FMAttributeDef method parity checklist:
    # Spec: AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 4.3, p.26
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDefaultValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMax              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMax              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMin              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMin              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the default value of the attribute.
        self.defaultValue: Optional[Numerical] = None

        # Maximum possible value for the value of this attribute
        self.max: Optional[Limit] = None

        # Minimum possible value for the value of this attribute
        self.min: Optional[Limit] = None

    def getDefaultValue(self) -> Optional[Numerical]:
        """
        This represents the default value of the attribute.
        """
        return self.defaultValue

    def setDefaultValue(self, value: Optional[Numerical]) -> FMAttributeDef:
        """
        This represents the default value of the attribute.

        A None value is a no-op and does not overwrite an existing defaultValue.
        """
        if value is not None:
            self.defaultValue = value
        return self

    def getMax(self) -> Optional[Limit]:
        """
        Maximum possible value for the value of this attribute
        """
        return self.max

    def setMax(self, value: Optional[Limit]) -> FMAttributeDef:
        """
        Maximum possible value for the value of this attribute

        A None value is a no-op and does not overwrite an existing max.
        """
        if value is not None:
            self.max = value
        return self

    def getMin(self) -> Optional[Limit]:
        """
        Minimum possible value for the value of this attribute
        """
        return self.min

    def setMin(self, value: Optional[Limit]) -> FMAttributeDef:
        """
        Minimum possible value for the value of this attribute

        A None value is a no-op and does not overwrite an existing min.
        """
        if value is not None:
            self.min = value
        return self


class FMFeatureMapAssertion(Identifiable):
    """
    Defines a boolean expression which shall evaluate to true for this mapping to become active. The expression is a formula that is based on features and system constants, and is defined by fmSyscond.
    """

    # FMFeatureMapAssertion method parity checklist:
    # Spec: AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 6.4, p.56
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFmSyscond   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFmSyscond   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The formula that implements the assertion.
        self.fmSyscond: Optional[FMConditionByFeaturesAndSwSystemconsts] = None

    def getFmSyscond(self) -> Optional[FMConditionByFeaturesAndSwSystemconsts]:
        """
        The formula that implements the assertion.
        """
        return self.fmSyscond

    def setFmSyscond(self, value: Optional[FMConditionByFeaturesAndSwSystemconsts]) -> FMFeatureMapAssertion:
        """
        The formula that implements the assertion.

        A None value is a no-op and does not overwrite an existing fmSyscond.
        """
        if value is not None:
            self.fmSyscond = value
        return self


class FMFeatureMapCondition(Identifiable):
    """
    Defines a condition which needs to be fulfilled for this mapping to become active. The condition is implemented as formula that is based on features and attributes and is defined by fmCond.
    """

    # FMFeatureMapCondition method parity checklist:
    # Spec: AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 6.3, p.55
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFmCond     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFmCond     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The formula that implements the condition.
        self.fmCond: Optional[FMConditionByFeaturesAndAttributes] = None

    def getFmCond(self) -> Optional[FMConditionByFeaturesAndAttributes]:
        """
        The formula that implements the condition.
        """
        return self.fmCond

    def setFmCond(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> FMFeatureMapCondition:
        """
        The formula that implements the condition.

        A None value is a no-op and does not overwrite an existing fmCond.
        """
        if value is not None:
            self.fmCond = value
        return self


class FMFeatureMapElement(Identifiable):
    pass


class FMFeatureRelation(Identifiable):
    """
    Defines relations for FMFeatures, for example dependencies on other FMFeatures, or conflicts with other FMFeatures. A FMFeature can only be part of a FMFeatureSelectionSet if all its relations are fulfilled.
    """

    # FMFeatureRelation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 4.6, p.34
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addFeatureRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFeatureRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRestriction    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRestriction    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The FMFeature that is targeted by this FMFeature Relation.
        self.featureRefs: List[RefType] = []

        # If given, the condition shall evaluate to true, in order for the FMFeatureRelation to be active.
        self.restriction: Optional[FMConditionByFeaturesAndAttributes] = None

    def addFeatureRef(self, ref: RefType) -> FMFeatureRelation:
        """
        The FMFeature that is targeted by this FMFeature Relation.
        """
        self.featureRefs.append(ref)
        return self

    def getFeatureRefs(self) -> List[RefType]:
        """
        The FMFeature that is targeted by this FMFeature Relation.
        """
        return self.featureRefs

    def getRestriction(self) -> Optional[FMConditionByFeaturesAndAttributes]:
        """
        If given, the condition shall evaluate to true, in order for the FMFeatureRelation to be active.
        """
        return self.restriction

    def setRestriction(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> FMFeatureRelation:
        """
        If given, the condition shall evaluate to true, in order for the FMFeatureRelation to be active.

        A None value is a no-op and does not overwrite an existing restriction.
        """
        if value is not None:
            self.restriction = value
        return self


class FMFeatureRestriction(Identifiable):
    """
    Defines restrictions for FMFeatures. A FMFeature can only be part of a FMFeatureSelectionSet if at least one of its restrictions evaluate to true.
    """

    # FMFeatureRestriction method parity checklist:
    # Spec: AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 4.5, p.32
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRestriction    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRestriction    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # A formula that contains the actual restriction.
        self.restriction: Optional[FMConditionByFeaturesAndAttributes] = None

    def getRestriction(self) -> Optional[FMConditionByFeaturesAndAttributes]:
        """
        A formula that contains the actual restriction.
        """
        return self.restriction

    def setRestriction(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> FMFeatureRestriction:
        """
        A formula that contains the actual restriction.

        A None value is a no-op and does not overwrite an existing restriction.
        """
        if value is not None:
            self.restriction = value
        return self


class FMFeatureSelection(Identifiable):
    """
    A FMFeatureSelection represents the state of a particular FMFeature within a FMFeatureSelectionSet.
    """

    # FMFeatureSelection method parity checklist:
    # Spec: AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 5.2, p.40
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAttributeValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAttributeValues             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getFeatureRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFeatureRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaximumSelectedBindingTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumSelectedBindingTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinimumSelectedBindingTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinimumSelectedBindingTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getState                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setState                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This defines a value for the attribute that is referred to in the role definition. Note that a FMFeatureSelection cannot include two FMAttributeValues that refer to the same FMAttributeDef in the role definition. Tags: xml.sequenceOffset=50
        self.attributeValues: List[FMAttributeValue] = []

        # The FMFeature whose state is defined by this FMFeature Selection. Tags: xml.sequenceOffset=10
        self.featureRef: Optional[RefType] = None

        # Defines an upper bound for the binding time of the variation points that are associated with the FMFeature, and refines its maximumIntendedBindingTime. This attribute is meant as a hint for the development process. Tags: xml.sequenceOffset=40
        self.maximumSelectedBindingTime: Optional[BindingTimeEnum] = None

        # Defines a lower bound for the binding time of the variation points that are associated with the FMFeature, and refines its minimumIntendedBindingTime. This attribute is meant as a hint for the development process. Tags: xml.sequenceOffset=30
        self.minimumSelectedBindingTime: Optional[BindingTimeEnum] = None

        # Defines how the FMFeature that is described by this FMFeatureSelection contributes to the FMFeature SelectionSet. A FMFeature may have the state selected, deselected or undecided. Tags: xml.sequenceOffset=20
        self.state: Optional[FMFeatureSelectionState] = None

    def addAttributeValue(self, value: FMAttributeValue) -> FMFeatureSelection:
        """
        This defines a value for the attribute that is referred to in the role definition. Note that a FMFeatureSelection cannot include two FMAttributeValues that refer to the same FMAttributeDef in the role definition. Tags: xml.sequenceOffset=50
        """
        self.attributeValues.append(value)
        return self

    def getAttributeValues(self) -> List[FMAttributeValue]:
        """
        This defines a value for the attribute that is referred to in the role definition. Note that a FMFeatureSelection cannot include two FMAttributeValues that refer to the same FMAttributeDef in the role definition. Tags: xml.sequenceOffset=50
        """
        return self.attributeValues

    def getFeatureRef(self) -> Optional[RefType]:
        """
        The FMFeature whose state is defined by this FMFeature Selection. Tags: xml.sequenceOffset=10
        """
        return self.featureRef

    def setFeatureRef(self, value: Optional[RefType]) -> FMFeatureSelection:
        """
        The FMFeature whose state is defined by this FMFeature Selection. Tags: xml.sequenceOffset=10

        A None value is a no-op and does not overwrite an existing featureRef.
        """
        if value is not None:
            self.featureRef = value
        return self

    def getMaximumSelectedBindingTime(self) -> Optional[BindingTimeEnum]:
        """
        Defines an upper bound for the binding time of the variation points that are associated with the FMFeature, and refines its maximumIntendedBindingTime. This attribute is meant as a hint for the development process. Tags: xml.sequenceOffset=40
        """
        return self.maximumSelectedBindingTime

    def setMaximumSelectedBindingTime(self, value: Optional[BindingTimeEnum]) -> FMFeatureSelection:
        """
        Defines an upper bound for the binding time of the variation points that are associated with the FMFeature, and refines its maximumIntendedBindingTime. This attribute is meant as a hint for the development process. Tags: xml.sequenceOffset=40

        A None value is a no-op and does not overwrite an existing maximumSelectedBindingTime.
        """
        if value is not None:
            self.maximumSelectedBindingTime = value
        return self

    def getMinimumSelectedBindingTime(self) -> Optional[BindingTimeEnum]:
        """
        Defines a lower bound for the binding time of the variation points that are associated with the FMFeature, and refines its minimumIntendedBindingTime. This attribute is meant as a hint for the development process. Tags: xml.sequenceOffset=30
        """
        return self.minimumSelectedBindingTime

    def setMinimumSelectedBindingTime(self, value: Optional[BindingTimeEnum]) -> FMFeatureSelection:
        """
        Defines a lower bound for the binding time of the variation points that are associated with the FMFeature, and refines its minimumIntendedBindingTime. This attribute is meant as a hint for the development process. Tags: xml.sequenceOffset=30

        A None value is a no-op and does not overwrite an existing minimumSelectedBindingTime.
        """
        if value is not None:
            self.minimumSelectedBindingTime = value
        return self

    def getState(self) -> Optional[FMFeatureSelectionState]:
        """
        Defines how the FMFeature that is described by this FMFeatureSelection contributes to the FMFeature SelectionSet. A FMFeature may have the state selected, deselected or undecided. Tags: xml.sequenceOffset=20
        """
        return self.state

    def setState(self, value: Optional[FMFeatureSelectionState]) -> FMFeatureSelection:
        """
        Defines how the FMFeature that is described by this FMFeatureSelection contributes to the FMFeature SelectionSet. A FMFeature may have the state selected, deselected or undecided. Tags: xml.sequenceOffset=20

        A None value is a no-op and does not overwrite an existing state.
        """
        if value is not None:
            self.state = value
        return self


class IdsmRateLimitation(Identifiable):
    pass


class PrimitiveAttributeTailoring(AttributeTailoring):
    pass


class ReferenceTailoring(AttributeTailoring):
    pass


class SdgTailoring(DataFormatElementScope):
    pass


class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    pass


class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    pass


class SpecificationDocumentScope(SpecElementScope):
    pass


class BinaryManifestItem(Identifiable):
    pass


class BinaryManifestItemDefinition(Identifiable):
    pass


class BinaryManifestAddressableObject(Identifiable, ABC):
    pass


class BinaryManifestMetaDataField(BinaryManifestAddressableObject):
    """
    This meta-class provides the ability to define a meta-data field for the binary manifest descriptor.
    """

    # BinaryManifestMetaDataField method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.28, p.923
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSize     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSize     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValue    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The value of this attribute represents the size of the meta-data field in bytes.
        self.size: Optional[PositiveInteger] = None

        # This attribute specifies the value of the meta-data field.
        self.value: Optional[VerbatimString] = None

    def getSize(self) -> Optional[PositiveInteger]:
        """
        The value of this attribute represents the size of the meta-data field in bytes.
        """
        return self.size

    def setSize(self, value: Optional[PositiveInteger]) -> BinaryManifestMetaDataField:
        """
        The value of this attribute represents the size of the meta-data field in bytes.

        A None value is a no-op and does not overwrite an existing size.
        """
        if value is not None:
            self.size = value
        return self

    def getValue(self) -> Optional[VerbatimString]:
        """
        This attribute specifies the value of the meta-data field.
        """
        return self.value

    def setValue(self, value: Optional[VerbatimString]) -> BinaryManifestMetaDataField:
        """
        This attribute specifies the value of the meta-data field.

        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class BinaryManifestProvideResource(Identifiable):
    pass


class BinaryManifestRequireResource(Identifiable):
    pass


class BinaryManifestResourceDefinition(Identifiable):
    pass


class CpSoftwareClusterToResourceMapping(Identifiable):
    pass


class DdsCpDomain(Identifiable):
    """
    Definition of a DDS Domain. Tags: atp.Status=candidate
    """

    # DdsCpDomain method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.176, p.526
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createDdsPartition   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsPartitions     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDdsTopic       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsTopics         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDomainId          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDomainId          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Identity-only child serialization debt (Rule 0001.7): ddsPartition aggregated the then-unsynced
    # DdsCpPartition stub — RESOLVED by the DdsCpPartition sync (Table 6.178), which replaced the
    # identity-only reader/writer placeholder with real read/writeDdsCpPartition calls and upgraded the
    # round-trip tests to assert partition field values. ddsTopic is fully serialized via the synced
    # read/writeDdsCpTopic (Table 6.177).

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of DDS Partition definitions. Tags: atp.Status=candidate
        self.ddsPartitions: List[DdsCpPartition] = []

        # Collection of DDS Topics. Tags: atp.Status=candidate
        self.ddsTopics: List[DdsCpTopic] = []

        # Definition of the DDS Domain Id. Tags: atp.Status=candidate
        self.domainId: Optional[PositiveInteger] = None

    def createDdsPartition(self, short_name: str) -> DdsCpPartition:
        """
        Collection of DDS Partition definitions. Tags: atp.Status=candidate
        """
        if not self.IsReferrableElementExists(short_name, DdsCpPartition):
            partition = DdsCpPartition(self, short_name)
            self.addReferrableElement(partition)
            self.ddsPartitions.append(partition)
        return cast(DdsCpPartition, self.getReferrableElement(short_name, DdsCpPartition))

    def getDdsPartitions(self) -> List[DdsCpPartition]:
        """
        Collection of DDS Partition definitions. Tags: atp.Status=candidate
        """
        return self.ddsPartitions

    def createDdsTopic(self, short_name: str) -> DdsCpTopic:
        """
        Collection of DDS Topics. Tags: atp.Status=candidate
        """
        if not self.IsReferrableElementExists(short_name, DdsCpTopic):
            topic = DdsCpTopic(self, short_name)
            self.addReferrableElement(topic)
            self.ddsTopics.append(topic)
        return cast(DdsCpTopic, self.getReferrableElement(short_name, DdsCpTopic))

    def getDdsTopics(self) -> List[DdsCpTopic]:
        """
        Collection of DDS Topics. Tags: atp.Status=candidate
        """
        return self.ddsTopics

    def getDomainId(self) -> Optional[PositiveInteger]:
        """
        Definition of the DDS Domain Id. Tags: atp.Status=candidate
        """
        return self.domainId

    def setDomainId(self, value: Optional[PositiveInteger]) -> DdsCpDomain:
        """
        Definition of the DDS Domain Id. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing domainId.
        """
        if value is not None:
            self.domainId = value
        return self


class DdsCpPartition(Identifiable):
    """
    Definition of a DDS Partition. Tags: atp.Status=candidate
    """

    # DdsCpPartition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.178, p.527
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPartitionName     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPartitionName     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Definition of the DDS Partition Name. '*' may be used to define the default partition. Tags: atp.Status=candidate
        self.partitionName: Optional[String] = None

    def getPartitionName(self) -> Optional[String]:
        """
        Definition of the DDS Partition Name. '*' may be used to define the default partition. Tags: atp.Status=candidate
        """
        return self.partitionName

    def setPartitionName(self, value: Optional[String]) -> DdsCpPartition:
        """
        Definition of the DDS Partition Name. '*' may be used to define the default partition. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing partitionName.
        """
        if value is not None:
            self.partitionName = value
        return self


class DdsCpServiceInstance(Identifiable, ABC):
    """
    Provided and Consumed Dds Service Instances that are available at the ApplicationEndpoint. Tags: atp.Status=candidate
    """

    # DdsCpServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.152, p.472
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDdsFieldReplyTopicRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsFieldReplyTopicRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsFieldRequestTopicRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsFieldRequestTopicRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsMethodReplyTopicRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsMethodReplyTopicRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsMethodRequestTopicRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setDdsMethodRequestTopicRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsServiceQosProfileRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsServiceQosProfileRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceInstanceId         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceInstanceId         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceInterfaceId        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceInterfaceId        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DdsCpServiceInstance:
            raise TypeError("DdsCpServiceInstance is an abstract class.")

        super().__init__(parent, short_name)

        # Reference to the DdsTopic used as fragment for the topic name of field setters. Tags: atp.Status=candidate
        self.ddsFieldReplyTopicRef: Optional[RefType] = None

        # Reference to the DdsTopic used as fragment for the topic name of field getters. Tags: atp.Status=candidate
        self.ddsFieldRequestTopicRef: Optional[RefType] = None

        # Reference to the DdsTopic used as fragment for the topic name of method replies. Tags: atp.Status=candidate
        self.ddsMethodReplyTopicRef: Optional[RefType] = None

        # Reference to the DdsTopic used as fragment for the topic name of method requests. Tags: atp.Status=candidate
        self.ddsMethodRequestTopicRef: Optional[RefType] = None

        # Reference to the QOS Profile used for the service. Tags: atp.Status=candidate
        self.ddsServiceQosProfileRef: Optional[RefType] = None

        # Identification number that is used by DDS to identify DomainParticipants associated with an instance of the service. Tags: atp.Status=candidate
        self.serviceInstanceId: Optional[PositiveInteger] = None

        # Unique Identifier that identifies the ServiceInterface in DDS. This Identifier is encoded in the USER_DATA QoS of the DomainParticipant associated with the Service Instance and its value is propagated by DDS Discovery messages. Tags: atp.Status=candidate
        self.serviceInterfaceId: Optional[String] = None

    def getDdsFieldReplyTopicRef(self) -> Optional[RefType]:
        """
        Reference to the DdsTopic used as fragment for the topic name of field setters. Tags: atp.Status=candidate
        """
        return self.ddsFieldReplyTopicRef

    def setDdsFieldReplyTopicRef(self, value: Optional[RefType]) -> DdsCpServiceInstance:
        """
        Reference to the DdsTopic used as fragment for the topic name of field setters. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsFieldReplyTopicRef.
        """
        if value is not None:
            self.ddsFieldReplyTopicRef = value
        return self

    def getDdsFieldRequestTopicRef(self) -> Optional[RefType]:
        """
        Reference to the DdsTopic used as fragment for the topic name of field getters. Tags: atp.Status=candidate
        """
        return self.ddsFieldRequestTopicRef

    def setDdsFieldRequestTopicRef(self, value: Optional[RefType]) -> DdsCpServiceInstance:
        """
        Reference to the DdsTopic used as fragment for the topic name of field getters. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsFieldRequestTopicRef.
        """
        if value is not None:
            self.ddsFieldRequestTopicRef = value
        return self

    def getDdsMethodReplyTopicRef(self) -> Optional[RefType]:
        """
        Reference to the DdsTopic used as fragment for the topic name of method replies. Tags: atp.Status=candidate
        """
        return self.ddsMethodReplyTopicRef

    def setDdsMethodReplyTopicRef(self, value: Optional[RefType]) -> DdsCpServiceInstance:
        """
        Reference to the DdsTopic used as fragment for the topic name of method replies. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsMethodReplyTopicRef.
        """
        if value is not None:
            self.ddsMethodReplyTopicRef = value
        return self

    def getDdsMethodRequestTopicRef(self) -> Optional[RefType]:
        """
        Reference to the DdsTopic used as fragment for the topic name of method requests. Tags: atp.Status=candidate
        """
        return self.ddsMethodRequestTopicRef

    def setDdsMethodRequestTopicRef(self, value: Optional[RefType]) -> DdsCpServiceInstance:
        """
        Reference to the DdsTopic used as fragment for the topic name of method requests. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsMethodRequestTopicRef.
        """
        if value is not None:
            self.ddsMethodRequestTopicRef = value
        return self

    def getDdsServiceQosProfileRef(self) -> Optional[RefType]:
        """
        Reference to the QOS Profile used for the service. Tags: atp.Status=candidate
        """
        return self.ddsServiceQosProfileRef

    def setDdsServiceQosProfileRef(self, value: Optional[RefType]) -> DdsCpServiceInstance:
        """
        Reference to the QOS Profile used for the service. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsServiceQosProfileRef.
        """
        if value is not None:
            self.ddsServiceQosProfileRef = value
        return self

    def getServiceInstanceId(self) -> Optional[PositiveInteger]:
        """
        Identification number that is used by DDS to identify DomainParticipants associated with an instance of the service. Tags: atp.Status=candidate
        """
        return self.serviceInstanceId

    def setServiceInstanceId(self, value: Optional[PositiveInteger]) -> DdsCpServiceInstance:
        """
        Identification number that is used by DDS to identify DomainParticipants associated with an instance of the service. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing serviceInstanceId.
        """
        if value is not None:
            self.serviceInstanceId = value
        return self

    def getServiceInterfaceId(self) -> Optional[String]:
        """
        Unique Identifier that identifies the ServiceInterface in DDS. This Identifier is encoded in the USER_DATA QoS of the DomainParticipant associated with the Service Instance and its value is propagated by DDS Discovery messages. Tags: atp.Status=candidate
        """
        return self.serviceInterfaceId

    def setServiceInterfaceId(self, value: Optional[String]) -> DdsCpServiceInstance:
        """
        Unique Identifier that identifies the ServiceInterface in DDS. This Identifier is encoded in the USER_DATA QoS of the DomainParticipant associated with the Service Instance and its value is propagated by DDS Discovery messages. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing serviceInterfaceId.
        """
        if value is not None:
            self.serviceInterfaceId = value
        return self


class DdsCpTopic(Identifiable):
    """
    Definition of a DDS Partition. Tags: atp.Status=candidate
    """

    # DdsCpTopic method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.177, p.527
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDdsPartitionRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsPartitionRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTopicName          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTopicName          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the DDS Partition this topic is communicated. Tags: atp.Status=candidate
        self.ddsPartitionRef: Optional[RefType] = None

        # Definition of the DDS Topic Name. Tags: atp.Status=candidate
        self.topicName: Optional[String] = None

    def getDdsPartitionRef(self) -> Optional[RefType]:
        """
        Reference to the DDS Partition this topic is communicated. Tags: atp.Status=candidate
        """
        return self.ddsPartitionRef

    def setDdsPartitionRef(self, value: Optional[RefType]) -> DdsCpTopic:
        """
        Reference to the DDS Partition this topic is communicated. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsPartitionRef.
        """
        if value is not None:
            self.ddsPartitionRef = value
        return self

    def getTopicName(self) -> Optional[String]:
        """
        Definition of the DDS Topic Name. Tags: atp.Status=candidate
        """
        return self.topicName

    def setTopicName(self, value: Optional[String]) -> DdsCpTopic:
        """
        Definition of the DDS Topic Name. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing topicName.
        """
        if value is not None:
            self.topicName = value
        return self


class DdsCpQosProfile(Identifiable):
    """
    Definition of a DDS QOS Profile. Tags: atp.Status=candidate
    """

    # DdsCpQosProfile method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.179, p.529
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDeadline               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDeadline               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDestinationOrder       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationOrder       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDurability             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurability             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDurabilityService      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityService      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHistory                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHistory                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLatencyBudget          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLatencyBudget          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLifespan               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLifespan               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLiveliness             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLiveliness             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOwnership              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOwnership              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOwnershipStrength      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOwnershipStrength      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReliability            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReliability            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResourceLimits         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResourceLimits         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTopicData              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTopicData              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransportPriority      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransportPriority      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Identity-only child serialization debt (Rule 0001.7): RESOLVED — destinationOrder, history,
    # lifespan, reliability, resourceLimits and transportPriority originally aggregated still-unsynced
    # Dds* QoS policy classes; every child's own sync (Tables 6.180-6.200, last: DdsResourceLimits
    # Table 6.200) replaced the identity-only reader/writer placeholder with real read/write calls, so
    # all 14 children now serialize fully with their field values.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the DDS DEADLINE QoS policy. Tags: atp.Status=candidate
        self.deadline: Optional[DdsDeadline] = None

        # Defines the DDS DESTINATION_ORDER QoS policy.
        self.destinationOrder: Optional[DdsDestinationOrder] = None

        # Defines the DDS DURABILITY QoS policy. Tags: atp.Status=candidate
        self.durability: Optional[DdsDurability] = None

        # Defines the DDS DURABILITY_SERVICE QoS policy. Tags: atp.Status=candidate
        self.durabilityService: Optional[DdsDurabilityService] = None

        # Defines the DDS HISTORY QoS policy.
        self.history: Optional[DdsHistory] = None

        # Defines the DDS LATENCY_BUDGET QoS policy. Tags: atp.Status=candidate
        self.latencyBudget: Optional[DdsLatencyBudget] = None

        # Defines the DDS LIFESPAN QoS policy.
        self.lifespan: Optional[DdsLifespan] = None

        # Defines the DDS LIVELINESS QoS policy. Tags: atp.Status=candidate
        self.liveliness: Optional[DdsLiveliness] = None

        # Defines the DDS OWNERSHIP QoS policy. Tags: atp.Status=candidate
        self.ownership: Optional[DdsOwnership] = None

        # Defines the DDS OWNERSHIP_STRENGTH QoS policy. Tags: atp.Status=candidate
        self.ownershipStrength: Optional[DdsOwnershipStrength] = None

        # Defines the DDS RELIABILITY QoS policy.
        self.reliability: Optional[DdsReliability] = None

        # Defines the DDS RESOURCE_LIMITS QoS policy.
        self.resourceLimits: Optional[DdsResourceLimits] = None

        # Defines the DDS TOPIC_DATA QoS policy.
        self.topicData: Optional[DdsTopicData] = None

        # Defines the DDS TRANSPORT_PRIORITY QoS policy.
        self.transportPriority: Optional[DdsTransportPriority] = None

    def getDeadline(self) -> Optional[DdsDeadline]:
        """
        Defines the DDS DEADLINE QoS policy. Tags: atp.Status=candidate
        """
        return self.deadline

    def setDeadline(self, value: Optional[DdsDeadline]) -> DdsCpQosProfile:
        """
        Defines the DDS DEADLINE QoS policy. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing deadline.
        """
        if value is not None:
            self.deadline = value
        return self

    def getDestinationOrder(self) -> Optional[DdsDestinationOrder]:
        """
        Defines the DDS DESTINATION_ORDER QoS policy.
        """
        return self.destinationOrder

    def setDestinationOrder(self, value: Optional[DdsDestinationOrder]) -> DdsCpQosProfile:
        """
        Defines the DDS DESTINATION_ORDER QoS policy.

        A None value is a no-op and does not overwrite an existing destinationOrder.
        """
        if value is not None:
            self.destinationOrder = value
        return self

    def getDurability(self) -> Optional[DdsDurability]:
        """
        Defines the DDS DURABILITY QoS policy. Tags: atp.Status=candidate
        """
        return self.durability

    def setDurability(self, value: Optional[DdsDurability]) -> DdsCpQosProfile:
        """
        Defines the DDS DURABILITY QoS policy. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durability.
        """
        if value is not None:
            self.durability = value
        return self

    def getDurabilityService(self) -> Optional[DdsDurabilityService]:
        """
        Defines the DDS DURABILITY_SERVICE QoS policy. Tags: atp.Status=candidate
        """
        return self.durabilityService

    def setDurabilityService(self, value: Optional[DdsDurabilityService]) -> DdsCpQosProfile:
        """
        Defines the DDS DURABILITY_SERVICE QoS policy. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityService.
        """
        if value is not None:
            self.durabilityService = value
        return self

    def getHistory(self) -> Optional[DdsHistory]:
        """
        Defines the DDS HISTORY QoS policy.
        """
        return self.history

    def setHistory(self, value: Optional[DdsHistory]) -> DdsCpQosProfile:
        """
        Defines the DDS HISTORY QoS policy.

        A None value is a no-op and does not overwrite an existing history.
        """
        if value is not None:
            self.history = value
        return self

    def getLatencyBudget(self) -> Optional[DdsLatencyBudget]:
        """
        Defines the DDS LATENCY_BUDGET QoS policy. Tags: atp.Status=candidate
        """
        return self.latencyBudget

    def setLatencyBudget(self, value: Optional[DdsLatencyBudget]) -> DdsCpQosProfile:
        """
        Defines the DDS LATENCY_BUDGET QoS policy. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing latencyBudget.
        """
        if value is not None:
            self.latencyBudget = value
        return self

    def getLifespan(self) -> Optional[DdsLifespan]:
        """
        Defines the DDS LIFESPAN QoS policy.
        """
        return self.lifespan

    def setLifespan(self, value: Optional[DdsLifespan]) -> DdsCpQosProfile:
        """
        Defines the DDS LIFESPAN QoS policy.

        A None value is a no-op and does not overwrite an existing lifespan.
        """
        if value is not None:
            self.lifespan = value
        return self

    def getLiveliness(self) -> Optional[DdsLiveliness]:
        """
        Defines the DDS LIVELINESS QoS policy. Tags: atp.Status=candidate
        """
        return self.liveliness

    def setLiveliness(self, value: Optional[DdsLiveliness]) -> DdsCpQosProfile:
        """
        Defines the DDS LIVELINESS QoS policy. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing liveliness.
        """
        if value is not None:
            self.liveliness = value
        return self

    def getOwnership(self) -> Optional[DdsOwnership]:
        """
        Defines the DDS OWNERSHIP QoS policy. Tags: atp.Status=candidate
        """
        return self.ownership

    def setOwnership(self, value: Optional[DdsOwnership]) -> DdsCpQosProfile:
        """
        Defines the DDS OWNERSHIP QoS policy. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ownership.
        """
        if value is not None:
            self.ownership = value
        return self

    def getOwnershipStrength(self) -> Optional[DdsOwnershipStrength]:
        """
        Defines the DDS OWNERSHIP_STRENGTH QoS policy. Tags: atp.Status=candidate
        """
        return self.ownershipStrength

    def setOwnershipStrength(self, value: Optional[DdsOwnershipStrength]) -> DdsCpQosProfile:
        """
        Defines the DDS OWNERSHIP_STRENGTH QoS policy. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ownershipStrength.
        """
        if value is not None:
            self.ownershipStrength = value
        return self

    def getReliability(self) -> Optional[DdsReliability]:
        """
        Defines the DDS RELIABILITY QoS policy.
        """
        return self.reliability

    def setReliability(self, value: Optional[DdsReliability]) -> DdsCpQosProfile:
        """
        Defines the DDS RELIABILITY QoS policy.

        A None value is a no-op and does not overwrite an existing reliability.
        """
        if value is not None:
            self.reliability = value
        return self

    def getResourceLimits(self) -> Optional[DdsResourceLimits]:
        """
        Defines the DDS RESOURCE_LIMITS QoS policy.
        """
        return self.resourceLimits

    def setResourceLimits(self, value: Optional[DdsResourceLimits]) -> DdsCpQosProfile:
        """
        Defines the DDS RESOURCE_LIMITS QoS policy.

        A None value is a no-op and does not overwrite an existing resourceLimits.
        """
        if value is not None:
            self.resourceLimits = value
        return self

    def getTopicData(self) -> Optional[DdsTopicData]:
        """
        Defines the DDS TOPIC_DATA QoS policy.
        """
        return self.topicData

    def setTopicData(self, value: Optional[DdsTopicData]) -> DdsCpQosProfile:
        """
        Defines the DDS TOPIC_DATA QoS policy.

        A None value is a no-op and does not overwrite an existing topicData.
        """
        if value is not None:
            self.topicData = value
        return self

    def getTransportPriority(self) -> Optional[DdsTransportPriority]:
        """
        Defines the DDS TRANSPORT_PRIORITY QoS policy.
        """
        return self.transportPriority

    def setTransportPriority(self, value: Optional[DdsTransportPriority]) -> DdsCpQosProfile:
        """
        Defines the DDS TRANSPORT_PRIORITY QoS policy.

        A None value is a no-op and does not overwrite an existing transportPriority.
        """
        if value is not None:
            self.transportPriority = value
        return self


class GlobalTimeCanSlave(Identifiable):
    pass


class GlobalTimeEthSlave(Identifiable):
    pass


class GlobalTimeFrSlave(Identifiable):
    pass


class GlobalTimeGateway(Identifiable):
    pass


class GlobalTimeMaster(Identifiable, ABC):
    pass


class PortElementToCommunicationResourceMapping(Identifiable):
    pass


class SOMEIPTransformationProps(Identifiable):
    pass


class UserDefinedGlobalTimeSlave(Identifiable):
    pass


class UserDefinedTransformationProps(Identifiable):
    pass


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """
    This meta-class represents the ability to describe the existence and configuration of a consumed (required) service instance in a concrete implementation on top of DDS. Tags: atp.Status=candidate
    """

    # DdsCpConsumedServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.154, p.475
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addConsumedDdsOperation             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConsumedDdsOperations            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addConsumedDdsServiceEvent          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConsumedDdsServiceEvents         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getLocalUnicastAddressRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLocalUnicastAddressRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinorVersion                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinorVersion                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStaticRemoteMulticastAddressRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStaticRemoteMulticastAddressRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStaticRemoteUnicastAddressRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStaticRemoteUnicastAddressRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of consumed operations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsOperation, consumedDds Operation.variationPoint.shortLabel atp.Status=candidate
        self.consumedDdsOperations: List[DdsCpServiceInstanceOperation] = []

        # Collection of consumed events. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsServiceEvent, consumedDds ServiceEvent.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        self.consumedDdsServiceEvents: List[DdsCpServiceInstanceEvent] = []

        # The local address over which the Service is consumed. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES
        self.localUnicastAddressRef: Optional[RefType] = None

        # Minor Version of the ServiceInterface. Value can be set to a number that represents the Minor Version of the searched service or to ANY.
        self.minorVersion: Optional[AnyVersionString] = None

        # This reference defines the remote multicast address of the Service provider. This reference shall ONLY be used if the remote multicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES
        self.staticRemoteMulticastAddressRef: Optional[RefType] = None

        # This reference defines the remote unicast address of the Service provider. This reference shall ONLY be used if the remote unicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteUnicastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES
        self.staticRemoteUnicastAddressRef: Optional[RefType] = None

    def addConsumedDdsOperation(self, value: Optional[DdsCpServiceInstanceOperation]) -> DdsCpConsumedServiceInstance:
        """
        Collection of consumed operations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsOperation, consumedDds Operation.variationPoint.shortLabel atp.Status=candidate

        A None value is a no-op and does not extend the consumedDdsOperations list.
        """
        if value is not None:
            self.consumedDdsOperations.append(value)
        return self

    def getConsumedDdsOperations(self) -> List[DdsCpServiceInstanceOperation]:
        """
        Collection of consumed operations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsOperation, consumedDds Operation.variationPoint.shortLabel atp.Status=candidate
        """
        return self.consumedDdsOperations

    def addConsumedDdsServiceEvent(self, value: Optional[DdsCpServiceInstanceEvent]) -> DdsCpConsumedServiceInstance:
        """
        Collection of consumed events. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsServiceEvent, consumedDds ServiceEvent.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not extend the consumedDdsServiceEvents list.
        """
        if value is not None:
            self.consumedDdsServiceEvents.append(value)
        return self

    def getConsumedDdsServiceEvents(self) -> List[DdsCpServiceInstanceEvent]:
        """
        Collection of consumed events. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsServiceEvent, consumedDds ServiceEvent.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        """
        return self.consumedDdsServiceEvents

    def getLocalUnicastAddressRef(self) -> Optional[RefType]:
        """
        The local address over which the Service is consumed. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES
        """
        return self.localUnicastAddressRef

    def setLocalUnicastAddressRef(self, value: Optional[RefType]) -> DdsCpConsumedServiceInstance:
        """
        The local address over which the Service is consumed. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES

        A None value is a no-op and does not overwrite an existing localUnicastAddressRef.
        """
        if value is not None:
            self.localUnicastAddressRef = value
        return self

    def getMinorVersion(self) -> Optional[AnyVersionString]:
        """
        Minor Version of the ServiceInterface. Value can be set to a number that represents the Minor Version of the searched service or to ANY.
        """
        return self.minorVersion

    def setMinorVersion(self, value: Optional[AnyVersionString]) -> DdsCpConsumedServiceInstance:
        """
        Minor Version of the ServiceInterface. Value can be set to a number that represents the Minor Version of the searched service or to ANY.

        A None value is a no-op and does not overwrite an existing minorVersion.
        """
        if value is not None:
            self.minorVersion = value
        return self

    def getStaticRemoteMulticastAddressRef(self) -> Optional[RefType]:
        """
        This reference defines the remote multicast address of the Service provider. This reference shall ONLY be used if the remote multicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES
        """
        return self.staticRemoteMulticastAddressRef

    def setStaticRemoteMulticastAddressRef(self, value: Optional[RefType]) -> DdsCpConsumedServiceInstance:
        """
        This reference defines the remote multicast address of the Service provider. This reference shall ONLY be used if the remote multicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES

        A None value is a no-op and does not overwrite an existing staticRemoteMulticastAddressRef.
        """
        if value is not None:
            self.staticRemoteMulticastAddressRef = value
        return self

    def getStaticRemoteUnicastAddressRef(self) -> Optional[RefType]:
        """
        This reference defines the remote unicast address of the Service provider. This reference shall ONLY be used if the remote unicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteUnicastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES
        """
        return self.staticRemoteUnicastAddressRef

    def setStaticRemoteUnicastAddressRef(self, value: Optional[RefType]) -> DdsCpConsumedServiceInstance:
        """
        This reference defines the remote unicast address of the Service provider. This reference shall ONLY be used if the remote unicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteUnicastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES

        A None value is a no-op and does not overwrite an existing staticRemoteUnicastAddressRef.
        """
        if value is not None:
            self.staticRemoteUnicastAddressRef = value
        return self


class GlobalTimeCanMaster(GlobalTimeMaster):
    pass


class GlobalTimeEthMaster(GlobalTimeMaster):
    pass


class GlobalTimeFrMaster(GlobalTimeMaster):
    pass


class UserDefinedGlobalTimeMaster(GlobalTimeMaster):
    pass
