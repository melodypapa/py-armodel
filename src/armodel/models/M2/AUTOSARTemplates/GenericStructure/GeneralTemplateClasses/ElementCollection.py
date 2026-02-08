"""
This module contains classes for representing AUTOSAR element collections
in the GenericStructure module.
"""

from abc import ABC
from typing import Dict, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    AutoCollectEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
    RefType,
)


class CollectableElement(ARObject, ABC):
    """
    Abstract class for elements that can collect other referrable elements.
    This class provides functionality for managing collections of elements with lookup capabilities.
    """

    def __init__(self):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")

        super().__init__()

        self.elements: List[Referrable] = []
        self.element_mappings: Dict[str, List[Referrable]] = {}

    def getTotalElement(self) -> int:
        """
        Gets the total number of elements in this collection.

        Returns:
            The count of elements in this collection
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
        if (short_name not in self.element_mappings):
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


class Collection(ARElement):
    """
    Represents a collection of elements in AUTOSAR models.
    This class defines the structure for organizing and managing collections of AUTOSAR elements.
    """

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.autoCollect: Optional[AutoCollectEnum] = None
        self.collectedInstances: List[AnyInstanceRef] = []
        self.collectionSemantics: Optional[NameToken] = None
        self.elementRefs: List[RefType] = []
        self.elementRole: Optional[Identifier] = None
        self.sourceElementRefs: List[RefType] = []
        self.sourceInstances: List[AnyInstanceRef] = []

    def getAutoCollect(self) -> Optional[AutoCollectEnum]:
        """
        Gets the auto-collect setting for this collection.

        Returns:
            AutoCollectEnum representing the auto-collect setting, or None if not set
        """
        return self.autoCollect

    def setAutoCollect(self, value: AutoCollectEnum):
        """
        Sets the auto-collect setting for this collection.
        Only sets the value if it is not None.

        Args:
            value: The auto-collect setting to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.autoCollect = value
        return self

    def getCollectedInstances(self) -> List[AnyInstanceRef]:
        """
        Gets the list of collected instances in this collection.

        Returns:
            List of AnyInstanceRef instances
        """
        return self.collectedInstances

    def setCollectedInstances(self, value: List[AnyInstanceRef]):
        """
        Sets the list of collected instances in this collection.
        Only sets the value if it is not None.

        Args:
            value: The list of collected instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.collectedInstances = value
        return self

    def getCollectionSemantics(self) -> Optional[NameToken]:
        """
        Gets the collection semantics for this collection.

        Returns:
            NameToken representing the collection semantics, or None if not set
        """
        return self.collectionSemantics

    def setCollectionSemantics(self, value: NameToken):
        """
        Sets the collection semantics for this collection.
        Only sets the value if it is not None.

        Args:
            value: The collection semantics to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.collectionSemantics = value
        return self

    def getElementRefs(self) -> List[RefType]:
        """
        Gets the list of element references in this collection.

        Returns:
            List of RefType instances representing element references
        """
        return self.elementRefs

    def addElementRef(self, value: RefType):
        """
        Adds an element reference to this collection.
        Only adds the value if it is not None.

        Args:
            value: The element reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.elementRefs.append(value)
        return self

    def getElementRole(self) -> Optional[Identifier]:
        """
        Gets the element role for this collection.

        Returns:
            Identifier representing the element role, or None if not set
        """
        return self.elementRole

    def setElementRole(self, value: Identifier):
        """
        Sets the element role for this collection.
        Only sets the value if it is not None.

        Args:
            value: The element role to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.elementRole = value
        return self

    def getSourceElementRefs(self) -> List[RefType]:
        """
        Gets the list of source element references in this collection.

        Returns:
            List of RefType instances representing source element references
        """
        return self.sourceElementRefs

    def addSourceElementRef(self, value: RefType):
        """
        Adds a source element reference to this collection.
        Only adds the value if it is not None.

        Args:
            value: The source element reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sourceElementRefs.append(value)
        return self

    def getSourceInstances(self) -> List[AnyInstanceRef]:
        """
        Gets the list of source instances in this collection.

        Returns:
            List of AnyInstanceRef instances
        """
        return self.sourceInstances

    def setSourceInstances(self, value: List[AnyInstanceRef]):
        """
        Sets the list of source instances in this collection.
        Only sets the value if it is not None.

        Args:
            value: The list of source instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sourceInstances = value
        return self
