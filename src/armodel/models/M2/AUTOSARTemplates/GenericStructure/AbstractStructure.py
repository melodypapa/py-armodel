
"""
This module contains abstract structure classes for AUTOSAR models
in the GenericStructure module.
"""

from abc import ABCMeta
from typing import List, Optional
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class AtpInstanceRef(ARObject, metaclass=ABCMeta):
    """
    Abstract class for AUTOSAR Template Parameter (ATP) instance references.
    This class defines the structure for referencing ATP instances.
    """
    
    def __init__(self):
        if type(self) == AtpInstanceRef:
            raise NotImplementedError("AtpInstanceRef is an abstract class.")

        super().__init__()

        self.atpBaseRef: Optional[RefType] = None
        self.atpContextElementRefs: List[RefType] = []
        self.atpTargetRef: Optional[RefType] = None

    def getAtpBaseRef(self) -> Optional[RefType]:
        """
        Gets the ATP base reference.
        
        Returns:
            RefType representing the base reference, or None if not set
        """
        return self.atpBaseRef

    def setAtpBaseRef(self, value: RefType):
        """
        Sets the ATP base reference.
        
        Args:
            value: The base reference to set
            
        Returns:
            self for method chaining
        """
        self.atpBaseRef = value
        return self

    def getAtpContextElementRefs(self) -> List[RefType]:
        """
        Gets the list of ATP context element references.
        
        Returns:
            List of RefType instances representing context element references
        """
        return self.atpContextElementRefs

    def addAtpContextElementRef(self, value: RefType):
        """
        Adds an ATP context element reference.
        
        Args:
            value: The context element reference to add
            
        Returns:
            self for method chaining
        """
        self.atpContextElementRefs.append(value)
        return self

    def getAtpTargetRef(self) -> Optional[RefType]:
        """
        Gets the ATP target reference.
        
        Returns:
            RefType representing the target reference, or None if not set
        """
        return self.atpTargetRef

    def setAtpTargetRef(self, value: RefType):
        """
        Sets the ATP target reference.
        
        Args:
            value: The target reference to set
            
        Returns:
            self for method chaining
        """
        self.atpTargetRef = value
        return self


class AnyInstanceRef(ARObject):
    """
    Represents a generic instance reference in AUTOSAR models.
    This class defines the structure for referencing any type of instance.
    """
    
    def __init__(self):
        super().__init__()

        self.baseRef: Optional[RefType] = None
        self.contextElementRefs: List[RefType] = []
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Gets the base reference.
        
        Returns:
            RefType representing the base reference, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: RefType):
        """
        Sets the base reference.
        
        Args:
            value: The base reference to set
            
        Returns:
            self for method chaining
        """
        self.baseRef = value
        return self

    def getContextElementRefs(self) -> List[RefType]:
        """
        Gets the list of context element references.
        
        Returns:
            List of RefType instances representing context element references
        """
        return self.contextElementRefs

    def addContextElementRef(self, value: RefType):
        """
        Adds a context element reference.
        
        Args:
            value: The context element reference to add
            
        Returns:
            self for method chaining
        """
        self.contextElementRefs.append(value)
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        Gets the target reference.
        
        Returns:
            RefType representing the target reference, or None if not set
        """
        return self.targetRef

    def setTargetRef(self, value: RefType):
        """
        Sets the target reference.
        
        Args:
            value: The target reference to set
            
        Returns:
            self for method chaining
        """
        self.targetRef = value
        return self


class AtpFeature(Identifiable, metaclass=ABCMeta):
    """
    Abstract class for AUTOSAR Template Parameter (ATP) features.
    This class defines the basic structure for ATP features.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpFeature:
            raise TypeError("AtpFeature is an abstract class.")
        super().__init__(parent, short_name)


class AtpStructureElement(AtpFeature, metaclass=ABCMeta):
    """
    Abstract class for AUTOSAR Template Parameter (ATP) structure elements.
    This class defines the basic structure for ATP structure elements.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpStructureElement:
            raise TypeError("AtpStructureElement is an abstract class.")
        super().__init__(parent, short_name)


class AtpType(ARElement, metaclass=ABCMeta):
    """
    Abstract class for AUTOSAR Template Parameter (ATP) types.
    This class defines the basic structure for ATP types.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpType:
            raise TypeError("AtpType is an abstract class.")

        super().__init__(parent, short_name)
