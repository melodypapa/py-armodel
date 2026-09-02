"""
This module contains abstract structure classes for AUTOSAR models
in the GenericStructure module.
"""

from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable


class AtpInstanceRef(ARObject, ABC):
    """
    An M0 instance of a classifier may be represented as a tree rooted at that instance, where under each node come the sub-trees representing the instances which act as features under that node. An instance ref specifies a navigation path from any M0 tree-instance of the base (which is a classifier) to a leaf (which is an instance of the target).
    """

    # AtpInstanceRef method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.3, p.174
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAtpBaseRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAtpBaseRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAtpContextElementRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addAtpContextElementRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAtpTargetRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAtpTargetRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is AtpInstanceRef:
            raise TypeError("AtpInstanceRef is an abstract class.")

        super().__init__()

        # This is the base from which the navigaion path starts. Stereotypes: atpAbstract; atpDerived
        self.atpBaseRef: Optional[RefType] = None

        # This is one particular step in the navigation path. Stereotypes: atpAbstract
        self.atpContextElementRefs: List[RefType] = []

        # This is the target of the instance ref. In other words it is the terminal of the navigation path. Stereotypes: atpAbstract
        self.atpTargetRef: Optional[RefType] = None

    def getAtpBaseRef(self) -> Optional[RefType]:
        """
        This is the base from which the navigaion path starts. Stereotypes: atpAbstract; atpDerived
        """
        return self.atpBaseRef

    def setAtpBaseRef(self, value: Optional[RefType]) -> "AtpInstanceRef":
        """
        This is the base from which the navigaion path starts. Stereotypes: atpAbstract; atpDerived
        A None value is a no-op and does not overwrite an existing atpBaseRef.
        """
        if value is not None:
            self.atpBaseRef = value
        return self

    def getAtpContextElementRefs(self) -> List[RefType]:
        """
        This is one particular step in the navigation path. Stereotypes: atpAbstract
        """
        return self.atpContextElementRefs

    def addAtpContextElementRef(self, value: Optional[RefType]) -> "AtpInstanceRef":
        """
        This is one particular step in the navigation path. Stereotypes: atpAbstract
        """
        if value is not None:
            self.atpContextElementRefs.append(value)
        return self

    def getAtpTargetRef(self) -> Optional[RefType]:
        """
        This is the target of the instance ref. In other words it is the terminal of the navigation path. Stereotypes: atpAbstract
        """
        return self.atpTargetRef

    def setAtpTargetRef(self, value: Optional[RefType]) -> "AtpInstanceRef":
        """
        This is the target of the instance ref. In other words it is the terminal of the navigation path. Stereotypes: atpAbstract
        A None value is a no-op and does not overwrite an existing atpTargetRef.
        """
        if value is not None:
            self.atpTargetRef = value
        return self


class AtpFeature(Identifiable, ABC):
    """
    Features are properties via which a classifier classifies instances. Or: a classifier has features and every M0 instance of it will have those features.
    """

    # AtpFeature method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.2, p.174
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpFeature:
            raise TypeError("AtpFeature is an abstract class.")
        super().__init__(parent, short_name)


class AtpClassifier(Identifiable, ABC):
    """
    A classifier classifies M0 instances according to their features. Or: a classifier is something that has instances - an M1 classifier has M0 instances.
    """

    # AtpClassifier method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.1, p.173
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAtpFeatures               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addAtpFeature                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpClassifier:
            raise TypeError("AtpClassifier is an abstract class.")
        super().__init__(parent, short_name)

        # This is a feature of the classifier. Stereotypes: atpDerived
        self.atpFeatures: List[AtpFeature] = []

    def getAtpFeatures(self) -> List[AtpFeature]:
        """
        This is a feature of the classifier. Stereotypes: atpDerived
        """
        return self.atpFeatures

    def addAtpFeature(self, value: Optional[AtpFeature]) -> "AtpClassifier":
        """
        This is a feature of the classifier. Stereotypes: atpDerived
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.atpFeatures.append(value)
        return self


class AtpType(AtpClassifier, ABC):
    """A type is a classifier that may serve to type prototypes. It is a reusable classifier."""

    # AtpType method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.6, p.175
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpType:
            raise TypeError("AtpType is an abstract class.")
        super().__init__(parent, short_name)


class AtpPrototype(AtpBlueprintable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) prototype elements.

    AtpPrototype represents prototype elements in the AUTOSAR system. Prototypes
    are instantiable elements that can be used to create instances or references
    in AUTOSAR models. They serve as templates for creating specific occurrences
    of elements.

    This class extends AtpBlueprintable with prototype-specific functionality.

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

    # AtpPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpPrototype:
            raise TypeError("AtpPrototype is an abstract class.")
        super().__init__(parent, short_name)


class AtpStructureElement(AtpBlueprintable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) structure elements.

    AtpStructureElement represents structural elements in the AUTOSAR system.
    These elements provide the fundamental structure for organizing and defining
    AUTOSAR models, including behaviors, operations, and other structural components.

    This class extends AtpBlueprintable with structure-specific functionality.

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

    # AtpStructureElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpStructureElement:
            raise TypeError("AtpStructureElement is an abstract class.")
        super().__init__(parent, short_name)
