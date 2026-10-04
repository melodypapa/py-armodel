"""
This module contains classes for representing identifiable elements in AUTOSAR models
in the GenericStructure module.
"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject, DiagnosticAbstractParameter, DiagnosticParameter, RoleBasedResourceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CategoryString,
    DiagnosticDebounceBehaviorEnum,
    Identifier,
    PositiveInteger,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from abc import ABC
from typing import Dict, List, Optional, TYPE_CHECKING, Union, cast

if TYPE_CHECKING:
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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.38, p.1002
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addShortNameFragment         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShortNameFragments        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getShortName                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getParent                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFullName                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

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

    def setCategory(self, value: Union[CategoryString, str]) -> Identifiable:
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
    pass


class FMFeatureMapAssertion(Identifiable):
    pass


class FMFeatureMapCondition(Identifiable):
    pass


class FMFeatureMapElement(Identifiable):
    pass


class FMFeatureRelation(Identifiable):
    pass


class FMFeatureRestriction(Identifiable):
    pass


class FMFeatureSelection(Identifiable):
    pass


class IdsmRateLimitation(Identifiable):
    pass


class PrimitiveAttributeTailoring(AttributeTailoring):
    pass


class ReferenceTailoring(AttributeTailoring):
    pass


class RptContainer(Identifiable):
    pass


class SdgTailoring(DataFormatElementScope):
    pass


class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    pass


class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    pass


class SoConIPduIdentifier(Referrable):
    pass


class SpecificationDocumentScope(SpecElementScope):
    pass


class TDCpSoftwareClusterMapping(Identifiable):
    pass


class TDCpSoftwareClusterResourceMapping(Identifiable):
    pass


class BinaryManifestItem(Identifiable):
    pass


class BinaryManifestItemDefinition(Identifiable):
    pass


class BinaryManifestMetaDataField(Identifiable):
    pass


class BinaryManifestProvideResource(Identifiable):
    pass


class BinaryManifestRequireResource(Identifiable):
    pass


class BinaryManifestResourceDefinition(Identifiable):
    pass


class CouplingElementAbstractDetails(Identifiable, ABC):
    pass


class CpSoftwareClusterResourceToApplicationPartitionMapping(Identifiable):
    pass


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    pass


class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    pass


class CpSoftwareClusterToResourceMapping(Identifiable):
    pass


class DdsCpDomain(Identifiable):
    pass


class DdsCpPartition(Identifiable):
    pass


class DdsCpServiceInstance(Identifiable, ABC):
    pass


class FlexrayArTpNode(Identifiable):
    pass


class FlexrayTpConnectionControl(Identifiable):
    pass


class FlexrayTpNode(Identifiable):
    pass


class FlexrayTpPduPool(Identifiable):
    pass


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


class IEEE1722TpAcfBus(Identifiable, ABC):
    pass


class IEEE1722TpAcfCanPart(Identifiable):
    pass


class IEEE1722TpAcfLinPart(Identifiable):
    pass


class J1939TpNode(Identifiable):
    pass


class PortElementToCommunicationResourceMapping(Identifiable):
    pass


class RteEventInCompositionSeparation(Identifiable):
    pass


class RteEventInSystemSeparation(Identifiable):
    pass


class SOMEIPTransformationProps(Identifiable):
    pass


class SomeipTpChannel(Identifiable):
    pass


class SwcToApplicationPartitionMapping(Identifiable):
    pass


class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    pass


class SwitchFlowMeteringEntry(Identifiable):
    pass


class SwitchStreamFilterActionDestPortModification(Identifiable):
    pass


class SwitchStreamFilterEntry(Identifiable):
    pass


class SwitchStreamFilterRule(Identifiable):
    pass


class SwitchStreamGateEntry(Identifiable):
    pass


class SwitchStreamIdentification(Identifiable):
    pass


class SystemSignalGroupToCommunicationResourceMapping(Identifiable):
    pass


class SystemSignalToCommunicationResourceMapping(Identifiable):
    pass


class UserDefinedGlobalTimeSlave(Identifiable):
    pass


class UserDefinedTransformationProps(Identifiable):
    pass


class CouplingElementSwitchDetails(CouplingElementAbstractDetails):
    pass


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    pass


class GlobalTimeCanMaster(GlobalTimeMaster):
    pass


class GlobalTimeEthMaster(GlobalTimeMaster):
    pass


class GlobalTimeFrMaster(GlobalTimeMaster):
    pass


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    pass


class UserDefinedGlobalTimeMaster(GlobalTimeMaster):
    pass
