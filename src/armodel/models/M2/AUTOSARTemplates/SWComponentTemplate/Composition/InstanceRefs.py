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
    # PortInCompositionTypeInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.14, p.950 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAbstractContextComponentRef [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAbstractContextComponentRef [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBaseRef                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTargetPortRef               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setTargetPortRef               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is PortInCompositionTypeInstanceRef:
            raise TypeError("PortInCompositionTypeInstanceRef is an abstract class.")

        super().__init__()

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        self.abstractContextComponentRef: Optional[RefType] = None

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        self.targetPortRef: Optional[RefType] = None

    def getAbstractContextComponentRef(self) -> Optional[RefType]:
        """Stereotypes: atpAbstract Tags: xml.sequenceOffset=20"""
        return self.abstractContextComponentRef

    def setAbstractContextComponentRef(self, value: Optional[RefType]) -> "PortInCompositionTypeInstanceRef":
        """Stereotypes: atpAbstract Tags: xml.sequenceOffset=20"""
        if value is not None:
            self.abstractContextComponentRef = value
        return self

    def getBaseRef(self) -> Optional[RefType]:
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10"""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "PortInCompositionTypeInstanceRef":
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10"""
        if value is not None:
            self.baseRef = value
        return self

    def getTargetPortRef(self) -> Optional[RefType]:
        """Stereotypes: atpAbstract Tags: xml.sequenceOffset=30"""
        return self.targetPortRef

    def setTargetPortRef(self, value: Optional[RefType]) -> "PortInCompositionTypeInstanceRef":
        """Stereotypes: atpAbstract Tags: xml.sequenceOffset=30"""
        if value is not None:
            self.targetPortRef = value
        return self


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    # PPortInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.15, p.950 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextComponentRef  [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextComponentRef  [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetPPortRef       [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetPPortRef       [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        self.contextComponentRef: Optional[RefType] = None
        self.targetPPortRef: Optional[RefType] = None

    def getContextComponentRef(self) -> Optional[RefType]:
        return self.contextComponentRef

    def setContextComponentRef(self, value: Optional[RefType]) -> "PPortInCompositionInstanceRef":
        if value is not None:
            self.contextComponentRef = value
        return self

    def getTargetPPortRef(self) -> Optional[RefType]:
        return self.targetPPortRef

    def setTargetPPortRef(self, value: Optional[RefType]) -> "PPortInCompositionInstanceRef":
        if value is not None:
            self.targetPPortRef = value
        return self


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    # RPortInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.16, p.951 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextComponentRef  [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextComponentRef  [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetRPortRef       [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetRPortRef       [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        self.contextComponentRef: Optional[RefType] = None
        self.targetRPortRef: Optional[RefType] = None

    def getContextComponentRef(self) -> Optional[RefType]:
        return self.contextComponentRef

    def setContextComponentRef(self, value: Optional[RefType]) -> "RPortInCompositionInstanceRef":
        if value is not None:
            self.contextComponentRef = value
        return self

    def getTargetRPortRef(self) -> Optional[RefType]:
        return self.targetRPortRef

    def setTargetRPortRef(self, value: Optional[RefType]) -> "RPortInCompositionInstanceRef":
        if value is not None:
            self.targetRPortRef = value
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


class ComponentInCompositionInstanceRef(AtpInstanceRef):
    """
    The ComponentInCompositionInstanceRef points to a concrete SwComponentPrototype within a CompositionSwComponentType.
    """

    # ComponentInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.13, p.950 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextComponentRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextComponentRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetComponentRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetComponentRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # The context for the scope of this timing event. Tags: xml.sequenceOffset=20
        self.contextComponentRefs: List[RefType] = []

        # Tags: xml.sequenceOffset=30
        self.targetComponentRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10"""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "ComponentInCompositionInstanceRef":
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextComponentRefs(self) -> List[RefType]:
        """The context for the scope of this timing event. Tags: xml.sequenceOffset=20"""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "ComponentInCompositionInstanceRef":
        """The context for the scope of this timing event. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getTargetComponentRef(self) -> Optional[RefType]:
        """Tags: xml.sequenceOffset=30"""
        return self.targetComponentRef

    def setTargetComponentRef(self, value: Optional[RefType]) -> "ComponentInCompositionInstanceRef":
        """Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetComponentRef."""
        if value is not None:
            self.targetComponentRef = value
        return self
