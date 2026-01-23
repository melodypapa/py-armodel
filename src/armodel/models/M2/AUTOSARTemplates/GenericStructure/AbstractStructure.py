
"""
This module contains abstract structure classes for AUTOSAR models
in the GenericStructure module.
"""

from abc import ABC
from typing import List, Optional
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class AtpInstanceRef(ARObject, ABC):
    """
    Abstract class for AUTOSAR Template Parameter (ATP) instance references.
    This class defines the structure for referencing ATP instances.
    """
    
    def __init__(self):
        if type(self) == AtpInstanceRef:
            raise TypeError("AtpInstanceRef is an abstract class.")

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


class AtpBlueprintable(Identifiable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) blueprintable elements.
    
    AtpBlueprintable represents elements that can be used as blueprints in the AUTOSAR
    template system. These elements provide reusable definitions that can be instantiated
    or referenced in the model.
    
    This class extends Identifiable with blueprint-specific functionality for managing
    template-based elements in AUTOSAR models.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        Concrete implementations include BswModuleEntry, CompuMethod, DataConstr,
        and other blueprintable AUTOSAR elements.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpBlueprintable:
            raise TypeError("AtpBlueprintable is an abstract class.")
        super().__init__(parent, short_name)


class AtpClassifier(Identifiable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) classifier elements.
    
    AtpClassifier represents elements that classify or categorize other elements
    in the AUTOSAR system. It serves as a base for type definitions and classifiers
    that provide structural organization to AUTOSAR models.
    
    This class extends Identifiable with classifier-specific functionality.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpClassifier is the parent of AtpType, which in turn is the parent
        of various AUTOSAR type definitions like AutosarDataType, PortInterface,
        and SwComponentType.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpClassifier:
            raise TypeError("AtpClassifier is an abstract class.")
        super().__init__(parent, short_name)


class AtpType(AtpClassifier, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) type elements.
    
    AtpType represents type definitions in the AUTOSAR system. It provides
    the foundation for all AUTOSAR type classifications including data types,
    port interfaces, and component types.
    
    This class extends AtpClassifier with type-specific functionality.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpType is the parent of various AUTOSAR type definitions:
        - AutosarDataType (including ApplicationDataType and ImplementationDataType)
        - ModeDeclarationGroup
        - ModeDeclarationMappingSet
        - PortInterface (including ClientServerInterface, SenderReceiverInterface, etc.)
        - SwComponentType (including AtomicSwComponentType, CompositionSwComponentType, etc.)
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpType:
            raise TypeError("AtpType is an abstract class.")
        super().__init__(parent, short_name)


class AtpFeature(Identifiable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) feature elements.
    
    AtpFeature represents feature elements in the AUTOSAR system. Features
    are structural elements that provide specific functionality or characteristics
    to AUTOSAR models.
    
    This class extends Identifiable with feature-specific functionality.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpFeature is the parent of AtpPrototype, which in turn is the parent
        of various AUTOSAR prototype definitions like PortPrototype, DataPrototype,
        and SwComponentPrototype.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpFeature:
            raise TypeError("AtpFeature is an abstract class.")
        super().__init__(parent, short_name)


class AtpPrototype(AtpFeature, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) prototype elements.
    
    AtpPrototype represents prototype elements in the AUTOSAR system. Prototypes
    are instantiable elements that can be used to create instances or references
    in AUTOSAR models. They serve as templates for creating specific occurrences
    of elements.
    
    This class extends AtpFeature with prototype-specific functionality.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpPrototype is the parent of various AUTOSAR prototype definitions:
        - AbstractProvidedPortPrototype
        - AbstractRequiredPortPrototype
        - DataPrototype (including VariableDataPrototype, ParameterDataPrototype, etc.)
        - ModeDeclarationGroupPrototype
        - PortPrototype (including PPortPrototype, RPortPrototype, PRPortPrototype)
        - RootSwCompositionPrototype
        - SwComponentPrototype
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpPrototype:
            raise TypeError("AtpPrototype is an abstract class.")
        super().__init__(parent, short_name)


class AtpStructureElement(AtpFeature, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) structure elements.
    
    AtpStructureElement represents structural elements in the AUTOSAR system.
    These elements provide the fundamental structure for organizing and defining
    AUTOSAR models, including behaviors, operations, and other structural components.
    
    This class extends AtpFeature with structure-specific functionality.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpStructureElement is the parent of various AUTOSAR structural elements:
        - AbstractAccessPoint (including ServerCallPoint, VariableAccess, etc.)
        - AbstractImplementationDataTypeElement
        - BswModuleDescription
        - BulkNvDataDescriptor
        - ClientServerOperation
        - DataPrototypeGroup
        - IdentCaption
        - InternalBehavior (including SwcInternalBehavior, BswInternalBehavior)
        - ModeDeclaration
        - ModeDeclarationMapping
        - ModeTransition
        - NvBlockDescriptor
        - PerInstanceMemory
        - PortGroup
        - PortPrototypeBlueprint
        - RTEEvent (including InitEvent, TimingEvent, DataReceivedEvent, etc.)
        - RunnableEntityGroup
        - SwConnector
        - SwcBswMapping
        - System
        - Trigger
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpStructureElement:
            raise TypeError("AtpStructureElement is an abstract class.")
        super().__init__(parent, short_name)
