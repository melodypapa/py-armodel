"""
This module contains classes for representing identifiable elements in AUTOSAR models
in the GenericStructure module.
"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString, Identifier, String
from abc import ABC
from typing import Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph
    from armodel.models.M2.MSR.Documentation.Annotation import Annotation
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint


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

        self.parent = parent
        self.short_name = short_name

        # This specifies how the Referrable.shortName is composed of several shortNameFragments. Tags: xml.sequenceOffset=-90
        self.shortNameFragments: List["ShortNameFragment"] = []

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
        return self.parent.full_name + "/" + self.short_name

    def getFullName(self) -> str:
        """
        Gets the full name of this element, including the parent's full name.

        Returns:
            The full name of this element
        """
        return self.full_name

    def addShortNameFragment(self, value: Optional["ShortNameFragment"]) -> "Referrable":
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

    def getShortNameFragments(self) -> List["ShortNameFragment"]:
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
    # [ ] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getRole                      [x] impl  [x] docstring  [x] test
    # [ ] setRole                      [x] impl  [x] docstring  [x] test
    # [ ] getFragment                  [x] impl  [x] docstring  [x] test
    # [ ] setFragment                  [x] impl  [x] docstring  [x] test

    def __init__(self):
        super().__init__()

        # This specifies the role of fragment to define e.g. the order of the fragments. Tags: xml.sequenceOffset=10
        self.role: Optional[str] = None

        # This specifies a single shortName (fragment) which is part of the composed shortName. Tags: xml.sequenceOffset=20
        self.fragment: Optional[Identifier] = None

    def getRole(self) -> Optional[str]:
        """
        Gets the role of fragment to define e.g. the order of the fragments.

        Returns:
            The role string, or None if not set
        """
        return self.role

    def setRole(self, value: Optional[str]) -> "ShortNameFragment":
        """
        Sets the role of fragment to define e.g. the order of the fragments.
        A None value is a no-op and does not overwrite an existing role.

        Args:
            value: The role string to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self

    def getFragment(self) -> Optional[Identifier]:
        """
        Gets the single shortName (fragment) which is part of the composed shortName.

        Returns:
            Identifier representing the fragment, or None if not set
        """
        return self.fragment

    def setFragment(self, value: Optional[Identifier]) -> "ShortNameFragment":
        """
        Sets the single shortName (fragment) which is part of the composed shortName.
        A None value is a no-op and does not overwrite an existing fragment.

        Args:
            value: The fragment identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.fragment = value
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

    def setLongName(self, value: Optional["MultilanguageLongName"]) -> "MultilanguageReferrable":
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


class Identifiable(MultilanguageReferrable, ABC):
    """
    Instances of this class can be referred to by their identifier (within the namespace borders). In addition to this, Identifiables are objects which contribute significantly to the overall structure of an AUTOSAR description. In particular, Identifiables might contain Identifiables.
    """

    # Identifiable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.4, p.61
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
    # [x] getTotalElement    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] removeElement      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getElements        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addElement         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getElement         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] IsElementExists    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # Kept deviation member (VARIATION-POINT element; not a Table 4.4 attribute):
    # carried here as framework infra so readIdentifiable/writeIdentifiable round-trip
    # VARIATION-POINT for every identifiable element; the XSD (AUTOSAR_00052.xsd)
    # declares VARIATION-POINT individually on 335 atpVariation classes, not in the
    # IDENTIFIABLE group. Stamp withheld until the per-class placement is resolved.
    # [x] getVariationPoint  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVariationPoint  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

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

        # Structural variation point of this element (kept deviation: VARIATION-POINT element; not a Table 4.4 attribute).
        self.variationPoint: Optional[VariationPoint] = None

        # Element collection registry (shared infra; kept on Identifiable because some direct subclasses, e.g. Fibex PhysicalChannel, are not CollectableElement).
        self.elements: List[Referrable] = []
        self.element_mappings: Dict[str, List[Referrable]] = {}

    def getAdminData(self) -> Optional[AdminData]:
        """
        This represents the administrative data for the identifiable object.
        """
        return self.adminData

    def setAdminData(self, value: Optional[AdminData]) -> "Identifiable":
        """
        This represents the administrative data for the identifiable object. A None value is a no-op and does not overwrite an existing adminData.
        """
        if value is not None:
            self.adminData = value
        return self

    def removeAdminData(self) -> None:
        """
        Removes the administrative data for this identifiable element.
        """
        self.adminData = None

    def addAnnotation(self, annotation: Optional[Annotation]) -> "Identifiable":
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

    def setCategory(self, value: Union[CategoryString, str]) -> "Identifiable":
        """
        The category is a keyword that specializes the semantics of the Identifiable. It affects the expected existence of attributes and the applicability of constraints. A None value is a no-op and does not overwrite an existing category.
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

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "Identifiable":
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the object in question. More elaborate documentation, (in particular how the object is built or used) should go to "introduction". A None value is a no-op and does not overwrite an existing desc.
        """
        if value is not None:
            self.desc = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> "Identifiable":
        """
        This represents more information about how the object in question is built or is used. Therefore it is a DocumentationBlock. A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self

    def getUuid(self) -> Optional[String]:
        """
        The purpose of this attribute is to provide a globally unique identifier for an instance of a meta-class. The values of this attribute should be globally unique strings prefixed by the type of identifier. For example, to include a DCE UUID as defined by The Open Group, the UUID would be preceded by "DCE:". The values of this attribute may be used to support merging of different AUTOSAR models. The form of the UUID (Universally Unique Identifier) is taken from a standard defined by the Open Group (was Open Software Foundation). This standard is widely used, including by Microsoft for COM (GUIDs) and by many companies for DCE, which is based on CORBA. The method for generating these 128-bit IDs is published in the standard and the effectiveness and uniqueness of the IDs is not in practice disputed. If the id namespace is omitted, DCE is assumed. An example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid attribute has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        """
        return self.uuid

    def setUuid(self, value: Optional[String]) -> "Identifiable":
        """
        The purpose of this attribute is to provide a globally unique identifier for an instance of a meta-class. The values of this attribute should be globally unique strings prefixed by the type of identifier. For example, to include a DCE UUID as defined by The Open Group, the UUID would be preceded by "DCE:". The values of this attribute may be used to support merging of different AUTOSAR models. The form of the UUID (Universally Unique Identifier) is taken from a standard defined by the Open Group (was Open Software Foundation). This standard is widely used, including by Microsoft for COM (GUIDs) and by many companies for DCE, which is based on CORBA. The method for generating these 128-bit IDs is published in the standard and the effectiveness and uniqueness of the IDs is not in practice disputed. If the id namespace is omitted, DCE is assumed. An example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid attribute has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp. A None value is a no-op and does not overwrite an existing uuid.
        """
        if value is not None:
            self.uuid = value
        return self

    def getTotalElement(self) -> int:
        """
        Gets the total number of elements in this collection.

        Returns:
            The count of elements in the collection
        """
        return len(self.elements)

    def removeElement(self, short_name: str, type=None) -> None:
        """
        Removes an element from this collection.

        Args:
            short_name: The short name of the element to remove
            type: The type of element to remove (optional)
        """
        if short_name not in self.element_mappings:
            raise KeyError("Invalid key <%s> for removing element" % short_name)
        if type is None:
            item = self.element_mappings[short_name][0]
        else:
            item = next(filter(lambda a: isinstance(a, type), self.element_mappings[short_name]))
        if item is not None:
            self.elements.remove(item)
            self.element_mappings[short_name].remove(item)

    def getElements(self) -> List[Referrable]:
        """
        Gets the list of elements in this collection.

        Returns:
            List of Referrable instances
        """
        return self.elements

    def addElement(self, element: Referrable) -> None:
        """
        Adds an element to this collection.

        Args:
            element: The element to add
        """
        short_name = element.getShortName()
        if not self.IsElementExists(short_name, type(element)):
            self.elements.append(element)
            if short_name not in self.element_mappings:
                self.element_mappings[short_name] = []
            self.element_mappings[short_name].append(element)

    def getElement(self, short_name: str, type=None) -> Optional[Referrable]:
        """
        Gets an element from this collection by short name and type.

        Args:
            short_name: The short name of the element to find
            type: The type of element to find (optional)

        Returns:
            The found Referrable instance, or None if not found
        """
        if short_name not in self.element_mappings:
            return None
        if type is not None:
            result = list(filter(lambda a: isinstance(a, type), self.element_mappings[short_name]))
            if len(result) == 0:
                return None
            return result[0]
        return self.element_mappings[short_name][0]

    def IsElementExists(self, short_name: str, type=None) -> bool:
        """
        Checks if an element with the specified short name and type exists in this collection.

        Args:
            short_name: The short name of the element to check
            type: The type of element to check (optional)

        Returns:
            True if the element exists, False otherwise
        """
        if type is None:
            return short_name in self.element_mappings
        if short_name in self.element_mappings:
            return any(isinstance(a, type) for a in self.element_mappings[short_name])
        return False

    def getVariationPoint(self) -> Optional["VariationPoint"]:
        """
        Returns the structural variation point of this element, if any.
        """
        return self.variationPoint

    def setVariationPoint(self, value: Optional["VariationPoint"]) -> "Identifiable":
        """
        Sets the structural variation point of this element. A None value is a no-op
        and does not overwrite an existing variationPoint.
        """
        if value is not None:
            self.variationPoint = value
        return self


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
