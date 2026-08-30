"""
This module contains classes for representing identifiable elements in AUTOSAR models
in the GenericStructure module.
"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString, Identifier
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
    Abstract class for referrable elements that support multilingual text.
    This class extends Referrable with multilingual support functionality.
    """

    # MultilanguageReferrable method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getLongName                  [x] impl  [x] docstring  [ ] test
    # [ ] setLongName                  [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is MultilanguageReferrable:
            raise TypeError("MultilanguageReferrable is an abstract class.")

        super().__init__(parent, short_name)

        # self._parent = parent
        self.longName: Optional[MultilanguageLongName] = None

    def getLongName(self) -> Optional[MultilanguageLongName]:
        """
        Gets the long name of this multilingual referrable element.

        Returns:
            MultilanguageLongName representing the long name, or None if not set
        """
        return self.longName

    def setLongName(self, value: MultilanguageLongName):
        """
        Sets the long name of this multilingual referrable element.

        Args:
            value: The long name to set

        Returns:
            self for method chaining
        """
        self.longName = value
        return self


class Identifiable(MultilanguageReferrable, ABC):
    """
    Abstract class for identifiable elements in AUTOSAR models.
    This class combines multilingual referrable functionality with element collection capabilities.
    """

    # Identifiable method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTotalElement              [x] impl  [x] docstring  [ ] test
    # [ ] removeElement                [x] impl  [x] docstring  [ ] test
    # [ ] getElements                  [x] impl  [x] docstring  [ ] test
    # [ ] addElement                   [x] impl  [x] docstring  [ ] test
    # [ ] getElement                   [x] impl  [x] docstring  [ ] test
    # [ ] IsElementExists              [x] impl  [x] docstring  [ ] test
    # [ ] getAdminData                 [x] impl  [x] docstring  [ ] test
    # [ ] setAdminData                 [x] impl  [x] docstring  [ ] test
    # [x] removeAdminData              [x] impl  [x] docstring  [x] test
    # [ ] getDesc                      [x] impl  [x] docstring  [ ] test
    # [ ] setDesc                      [x] impl  [x] docstring  [ ] test
    # [ ] getCategory                  [x] impl  [x] docstring  [ ] test
    # [ ] setCategory                  [x] impl  [x] docstring  [ ] test
    # [ ] getIntroduction              [x] impl  [x] docstring  [ ] test
    # [ ] setIntroduction              [x] impl  [x] docstring  [ ] test
    # [ ] addAnnotation                [x] impl  [x] docstring  [ ] test
    # [ ] getAnnotations               [x] impl  [x] docstring  [ ] test
    # [x] getVariationPoint            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVariationPoint            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Identifiable:
            raise TypeError("Identifiable is an abstract class.")

        MultilanguageReferrable.__init__(self, parent, short_name)

        self.elements: List[Referrable] = []
        self.element_mappings: Dict[str, List[Referrable]] = {}

        self.annotations: List[Annotation] = []
        self.adminData: Optional[AdminData] = None
        self.category: Optional[CategoryString] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        # Structural variation point attached to this element (pattern: aggregation,
        # TPS_GST 7.6; XSD group AR:VARIATION-POINT, AUTOSAR_00046.xsd:99470).
        # Deviation: spec also allows variation points on non-Identifiable elements
        # (reference pattern, property set pattern); only the Identifiable
        # aggregation pattern is supported.
        self.variationPoint: Optional["VariationPoint"] = None

    def getTotalElement(self) -> int:
        """
        Gets the total number of elements in this collection.

        Returns:
            The count of elements in the collection
        """
        return len(self.elements)

    def removeElement(self, short_name: str, type=None):
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

    def addElement(self, element: Referrable):
        """
        Adds an element to this collection.

        Args:
            element: The element to add

        Returns:
            self for method chaining
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

    def getAdminData(self) -> Optional[AdminData]:
        """
        Gets the administrative data for this identifiable element.

        Returns:
            AdminData instance, or None if not set
        """
        return self.adminData

    def setAdminData(self, value: AdminData):
        """
        Sets the administrative data for this identifiable element.
        Only sets the value if it is not None.

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
        Removes the administrative data for this identifiable element.
        """
        self.adminData = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        Gets the description for this identifiable element.

        Returns:
            MultiLanguageOverviewParagraph instance, or None if not set
        """
        return self.desc

    def setDesc(self, value: MultiLanguageOverviewParagraph):
        """
        Sets the description for this identifiable element.

        Args:
            value: The description to set

        Returns:
            self for method chaining
        """
        self.desc = value
        return self

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

    def getCategory(self) -> Optional[CategoryString]:
        """
        Gets the category for this identifiable element.

        Returns:
            CategoryString instance, or None if not set
        """
        return self.category

    def setCategory(self, value: Union[CategoryString, str]):
        """
        Sets the category for this identifiable element.
        If the value is a string, it will be converted to a CategoryString.

        Args:
            value: The category to set

        Returns:
            self for method chaining
        """
        if isinstance(value, str):
            self.category = CategoryString().setValue(value)
        else:
            self.category = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        Gets the introduction documentation for this identifiable element.

        Returns:
            DocumentationBlock instance, or None if not set
        """
        return self.introduction

    def setIntroduction(self, value: DocumentationBlock):
        """
        Sets the introduction documentation for this identifiable element.

        Args:
            value: The introduction documentation to set

        Returns:
            self for method chaining
        """
        self.introduction = value
        return self

    def addAnnotation(self, annotation: Annotation):
        """
        Adds an annotation to this identifiable element.

        Args:
            annotation: The annotation to add

        Returns:
            self for method chaining
        """
        self.annotations.append(annotation)
        return self

    def getAnnotations(self) -> List[Annotation]:
        """
        Gets the list of annotations for this identifiable element.

        Returns:
            List of Annotation instances
        """
        return self.annotations


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
