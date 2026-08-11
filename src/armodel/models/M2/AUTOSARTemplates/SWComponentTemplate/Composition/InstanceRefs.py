"""
This module contains classes for representing AUTOSAR instance references
in composition contexts. These classes are used for referencing ports and
operations within compositions and atomic SWC instances.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class PortInCompositionTypeInstanceRef(AtpInstanceRef, ABC):
    """
    Abstract base class for port instance references within a composition
    software component type.
    """

    # PortInCompositionTypeInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAbstractContextComponentRef [x] impl  [ ] docstring  [ ] test
    # [ ] setAbstractContextComponentRef [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetPortRef             [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is PortInCompositionTypeInstanceRef:
            raise TypeError("PortInCompositionTypeInstanceRef is an abstract class.")

        super().__init__()

        self.abstractContextComponentRef: RefType = None
        self.baseRef: RefType = None
        self.targetPortRef: RefType = None

    def getAbstractContextComponentRef(self):
        return self.abstractContextComponentRef

    def setAbstractContextComponentRef(self, value):
        self.abstractContextComponentRef = value
        return self

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getTargetPortRef(self):
        return self.targetPortRef

    def setTargetPortRef(self, value):
        self.targetPortRef = value
        return self


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """
    Instance reference to a PPortPrototype within a composition software
    component type.
    """

    # PPortInCompositionInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextComponentRef       [x] impl  [ ] docstring  [ ] test
    # [ ] setContextComponentRef       [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetPPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetPPortRef            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextComponentRef: RefType = None
        self.targetPPortRef: RefType = None

    def getContextComponentRef(self):
        return self.contextComponentRef

    def setContextComponentRef(self, value):
        self.contextComponentRef = value
        return self

    def getTargetPPortRef(self):
        return self.targetPPortRef

    def setTargetPPortRef(self, value):
        self.targetPPortRef = value
        return self


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """
    Instance reference to an RPortPrototype within a composition software
    component type.
    """

    # RPortInCompositionInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextComponentRef       [x] impl  [ ] docstring  [ ] test
    # [ ] setContextComponentRef       [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetRPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetRPortRef            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextComponentRef: RefType = None
        self.targetRPortRef: RefType = None

    def getContextComponentRef(self):
        return self.contextComponentRef

    def setContextComponentRef(self, value):
        self.contextComponentRef = value
        return self

    def getTargetRPortRef(self):
        return self.targetRPortRef

    def setTargetRPortRef(self, value):
        self.targetRPortRef = value
        return self


class OperationInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    """
    Abstract base class for operation instance references within an atomic
    software component type.
    """

    # OperationInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetOperationRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetOperationRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is OperationInAtomicSwcInstanceRef:
            raise TypeError("OperationInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.baseRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetOperationRef: RefType = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextPortRef(self):
        return self.contextPortRef

    def setContextPortRef(self, value):
        self.contextPortRef = value
        return self

    def getTargetOperationRef(self):
        return self.targetOperationRef

    def setTargetOperationRef(self, value):
        self.targetOperationRef = value
        return self


class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """
    Instance reference to a provided operation in an atomic software
    component through a PPortPrototype.
    """

    # POperationInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetProvidedOperationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetProvidedOperationRef [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextPPortRef: RefType = None
        self.targetProvidedOperationRef: RefType = None

    def getContextPPortRef(self):
        return self.contextPPortRef

    def setContextPPortRef(self, value):
        self.contextPPortRef = value
        return self

    def getTargetProvidedOperationRef(self):
        return self.targetProvidedOperationRef

    def setTargetProvidedOperationRef(self, value):
        self.targetProvidedOperationRef = value
        return self


class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """
    Instance reference to a required operation in an atomic software
    component through an RPortPrototype.
    """

    # ROperationInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetRequiredOperationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetRequiredOperationRef [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextRPortRef: RefType = None
        self.targetRequiredOperationRef: RefType = None

    def getContextRPortRef(self):
        return self.contextRPortRef

    def setContextRPortRef(self, value):
        self.contextRPortRef = value
        return self

    def getTargetRequiredOperationRef(self):
        return self.targetRequiredOperationRef

    def setTargetRequiredOperationRef(self, value):
        self.targetRequiredOperationRef = value
        return self


class InstanceEventInCompositionInstanceRef(AtpInstanceRef):
    """
    Instance reference to an RTEEvent in the context of a CompositionSwComponentType.
    Aggregated by InstantiationRTEEventProps.refinedEventIRef.
    """

    # InstanceEventInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.23, p.959
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addContextComponentPrototypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextComponentPrototypeRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetEventRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetEventRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # The CompositionSwComponentType that is the base of this instance ref.
        # Stereotypes: atpDerived (derived attribute, no XML element).
        self.baseRef: Optional[RefType] = None

        # This represents the nested structure of SwComponentPrototypes.
        self.contextComponentPrototypeRefs: List[RefType] = []

        # This represents the target RTEEvent.
        self.targetEventRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Gets the reference to the base CompositionSwComponentType.
        Derived attribute (atpDerived), so it has no XML element.

        Returns:
            RefType referencing the CompositionSwComponentType, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "InstanceEventInCompositionInstanceRef":
        """
        Sets the reference to the base CompositionSwComponentType.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The base CompositionSwComponentType reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def addContextComponentPrototypeRef(self, value: Optional[RefType]) -> "InstanceEventInCompositionInstanceRef":
        """
        Adds a reference to a context SwComponentPrototype.
        A None value is a no-op and does not append anything.

        Args:
            value: The context SwComponentPrototype reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextComponentPrototypeRefs.append(value)
        return self

    def getContextComponentPrototypeRefs(self) -> List[RefType]:
        """
        Gets the references to the context SwComponentPrototypes.

        Returns:
            List of RefType instances
        """
        return self.contextComponentPrototypeRefs

    def setTargetEventRef(self, value: Optional[RefType]) -> "InstanceEventInCompositionInstanceRef":
        """
        Sets the reference to the target RTEEvent.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The target RTEEvent reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetEventRef = value
        return self

    def getTargetEventRef(self) -> Optional[RefType]:
        """
        Gets the reference to the target RTEEvent.

        Returns:
            RefType referencing the RTEEvent, or None if not set
        """
        return self.targetEventRef
