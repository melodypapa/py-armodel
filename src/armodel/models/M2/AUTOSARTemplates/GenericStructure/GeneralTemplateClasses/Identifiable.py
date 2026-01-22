"""
This module contains classes for representing identifiable elements in AUTOSAR models
in the GenericStructure module.
"""

from .....M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from .....M2.MSR.AsamHdo.AdminData import AdminData
from .....M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from .....M2.MSR.Documentation.Annotation import Annotation
from .....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString
from abc import ABCMeta
from typing import Dict, List, Optional, Any


class Referrable(ARObject, metaclass=ABCMeta):
    """
    Abstract class for elements that can be referenced by other elements in AUTOSAR models.
    This class provides basic functionality for managing short names and parent-child relationships.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Referrable:
            raise TypeError("Referrable is an abstract class.")
        
        ARObject.__init__(self)

        self.parent = parent
        self.short_name = short_name

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


class MultilanguageReferrable(Referrable, metaclass=ABCMeta):
    """
    Abstract class for referrable elements that support multilingual text.
    This class extends Referrable with multilingual support functionality.
    """
    
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


class CollectableElement(ARObject, metaclass=ABCMeta):
    """
    Abstract class for elements that can collect other referrable elements.
    This class provides functionality for managing collections of elements with lookup capabilities.
    """
    
    def __init__(self):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")
        
        # super().__init__()
        
        self.elements: List[Referrable] = []
        self.element_mappings: Dict[str, List[Referrable]] = {}

    def getTotalElement(self) -> int:
        """
        Gets the total number of elements in this collection.
        
        Returns:
            The count of elements in the collection
        """
        # return len(list(filter(lambda a: not isinstance(a, ARPackage) , self.elements)))
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


class Identifiable(MultilanguageReferrable, CollectableElement, metaclass=ABCMeta):
    """
    Abstract class for identifiable elements in AUTOSAR models.
    This class combines multilingual referrable functionality with element collection capabilities.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Identifiable:
            raise TypeError("Identifiable is an abstract class.")
        
        MultilanguageReferrable.__init__(self, parent, short_name)
        CollectableElement.__init__(self)

        self.annotations: List[Annotation] = []
        self.adminData: Optional[AdminData] = None
        self.category: Optional[CategoryString] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

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

    def getCategory(self) -> Optional[CategoryString]:
        """
        Gets the category for this identifiable element.
        
        Returns:
            CategoryString instance, or None if not set
        """
        return self.category

    def setCategory(self, value: Any):
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


class PackageableElement(Identifiable, metaclass=ABCMeta):
    """
    Abstract class for elements that can be packaged in AUTOSAR models.
    This class extends Identifiable with packaging functionality.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PackageableElement:
            raise TypeError("PackageableElement is an abstract class.")
        super().__init__(parent, short_name)


class ARElement(PackageableElement, metaclass=ABCMeta):
    """
    Abstract class for AUTOSAR elements.
    This class represents the basic structure for all AUTOSAR model elements.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ARElement:
            raise TypeError("ARElement is an abstract class.")
        super().__init__(parent, short_name)


class Describable(ARObject, metaclass=ABCMeta):
    """
    Abstract class for elements that can be described in AUTOSAR models.
    This class provides basic description functionality for AUTOSAR elements.
    """
    
    def __init__(self):
        if type(self) is Describable:
            raise TypeError("Describable is an abstract class.")

        super().__init__()

        self.desc = None
        self.category = None
        self.adminData = None
        self.introduction = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        Gets the description for this describable element.
        
        Returns:
            MultiLanguageOverviewParagraph instance, or None if not set
        """
        return self.desc

    def setDesc(self, value: MultiLanguageOverviewParagraph):
        """
        Sets the description for this describable element.
        Only sets the value if it is not None.
        
        Args:
            value: The description to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.desc = value
        return self

    def getCategory(self) -> Optional[CategoryString]:
        """
        Gets the category for this describable element.
        
        Returns:
            CategoryString instance, or None if not set
        """
        return self.category

    def setCategory(self, value: CategoryString):
        """
        Sets the category for this describable element.
        Only sets the value if it is not None.
        
        Args:
            value: The category to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.category = value
        return self

    def getAdminData(self) -> Optional[AdminData]:
        """
        Gets the administrative data for this describable element.
        
        Returns:
            AdminData instance, or None if not set
        """
        return self.adminData

    def setAdminData(self, value: AdminData):
        """
        Sets the administrative data for this describable element.
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
        Removes the administrative data for this describable element.
        """
        self.adminData = None

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        Gets the introduction documentation for this describable element.
        
        Returns:
            DocumentationBlock instance, or None if not set
        """
        return self.introduction

    def setIntroduction(self, value: DocumentationBlock):
        """
        Sets the introduction documentation for this describable element.
        Only sets the value if it is not None.
        
        Args:
            value: The introduction documentation to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.introduction = value
        return self


    
