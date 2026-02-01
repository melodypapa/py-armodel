"""
This module contains classes for representing AUTOSAR element collections
in the GenericStructure module.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, NameToken, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import AutoCollectEnum


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
