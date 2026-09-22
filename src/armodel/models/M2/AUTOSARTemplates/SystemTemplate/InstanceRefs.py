# This module contains AUTOSAR System Template classes for instance references
# It defines variable and component instance references used in system modeling

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class VariableDataPrototypeInSystemInstanceRef(AtpInstanceRef):
    """
    If the referenced VariableDataPrototype is part of a PortInterface of a SwComponentPrototype that is located within the RootSwCompositionPrototype then the contextComposition reference to the RootSwCompositionPrototype shall be provided. In this scenario we have a System Extract where the RootSwComposition may contain other compositions. If the referenced VariableDataPrototype is part of a PortInterface of the RootSwCompositionPrototype itself then the contextComposition reference to the RootSwCompositionPrototype shall be skipped and the RootSwCompositionPrototype shall be referenced as contextComponent. In this scenario we have an Ecu Extract where the RootSwComposition contains PortPrototypes that describe the external communication.

    Please note that the xml.sequenceOffset is not set for this InstanceRef and therefore the properties are serialized in an alphabetical order.
    """

    # VariableDataPrototypeInSystemInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table B.3, p.1004 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextComponentRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextComponentRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextCompositionRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextCompositionRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextPortRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPortRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetDataPrototypeRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetDataPrototypeRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        self.contextComponentRefs: List[RefType] = []

        self.contextCompositionRef: Optional[RefType] = None

        self.contextPortRef: Optional[RefType] = None

        self.targetDataPrototypeRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Stereotypes: atpDerived"""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInSystemInstanceRef":
        """Stereotypes: atpDerived
        A None value is a no-op and does not overwrite an existing baseRef."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextComponentRefs(self) -> List[RefType]:
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInSystemInstanceRef":
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextCompositionRef(self) -> Optional[RefType]:
        return self.contextCompositionRef

    def setContextCompositionRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInSystemInstanceRef":
        if value is not None:
            self.contextCompositionRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInSystemInstanceRef":
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInSystemInstanceRef":
        if value is not None:
            self.targetDataPrototypeRef = value
        return self


class ComponentInSystemInstanceRef(AtpInstanceRef):
    """
    Instance reference to a component in the context of a system model.
    """

    # ComponentInSystemInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextComponentRefs      [x] impl  [ ] docstring  [ ] test
    # [ ] addContextComponentRef       [x] impl  [ ] docstring  [ ] test
    # [ ] getContextCompositionRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setContextCompositionRef     [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetComponentRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetComponentRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextComponentRefs: List[RefType] = []
        self.contextCompositionRef: RefType = None
        self.targetComponentRef: RefType = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextComponentRefs(self):
        return self.contextComponentRefs

    def addContextComponentRef(self, value):
        self.contextComponentRefs.append(value)
        return self

    def getContextCompositionRef(self):
        return self.contextCompositionRef

    def setContextCompositionRef(self, value):
        self.contextCompositionRef = value
        return self

    def getTargetComponentRef(self):
        return self.targetComponentRef

    def setTargetComponentRef(self, value):
        self.targetComponentRef = value
        return self


class OperationInSystemInstanceRef(AtpInstanceRef):
    """
    If the referenced ClientServerOperation is part of a PortInterface of a SwComponentPrototype that is located within the RootSwCompositionPrototype then the contextComposition reference to the RootSwCompositionPrototype shall be provided. In this scenario we have a System Extract where the RootSwComposition may contain other compositions. If the referenced ClientServerOperation is part of a PortInterface of the RootSwCompositionPrototype itself then the contextComposition reference to the RootSwCompositionPrototype shall be skipped and the RootSwCompositionPrototype shall be referenced as contextComponent. In this scenario we have an Ecu Extract where the RootSwComposition contains PortPrototypes that describe the external communication.
    """

    # OperationInSystemInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table B.2, p.1002 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextComponentRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextComponentRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextCompositionRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextCompositionRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextPortRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPortRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetOperationRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetOperationRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.contextComponentRefs: List[RefType] = []

        # Tags: xml.sequenceOffset=20
        self.contextCompositionRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=40
        self.contextPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=50
        self.targetOperationRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10"""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "OperationInSystemInstanceRef":
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextComponentRefs(self) -> List[RefType]:
        """Tags: xml.sequenceOffset=30"""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "OperationInSystemInstanceRef":
        """Tags: xml.sequenceOffset=30
        A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextCompositionRef(self) -> Optional[RefType]:
        """Tags: xml.sequenceOffset=20"""
        return self.contextCompositionRef

    def setContextCompositionRef(self, value: Optional[RefType]) -> "OperationInSystemInstanceRef":
        """Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextCompositionRef."""
        if value is not None:
            self.contextCompositionRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """Tags: xml.sequenceOffset=40"""
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "OperationInSystemInstanceRef":
        """Tags: xml.sequenceOffset=40
        A None value is a no-op and does not overwrite an existing contextPortRef."""
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetOperationRef(self) -> Optional[RefType]:
        """Tags: xml.sequenceOffset=50"""
        return self.targetOperationRef

    def setTargetOperationRef(self, value: Optional[RefType]) -> "OperationInSystemInstanceRef":
        """Tags: xml.sequenceOffset=50
        A None value is a no-op and does not overwrite an existing targetOperationRef."""
        if value is not None:
            self.targetOperationRef = value
        return self


class PortGroupInSystemInstanceRef(AtpInstanceRef):
    """
    Instance reference to a PortGroup in the context of a system model.
    """

    # PortGroupInSystemInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table B.5, p.1007 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextComponentRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextComponentRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextCompositionRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextCompositionRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.contextComponentRefs: List[RefType] = []

        # Tags: xml.sequenceOffset=20
        self.contextCompositionRef: Optional[RefType] = None

        # Link to a PortGroup that is defined in a component which is part of this CompositionSwComponentType. Tags: xml.sequenceOffset=40
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10"""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "PortGroupInSystemInstanceRef":
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextComponentRefs(self) -> List[RefType]:
        """Tags: xml.sequenceOffset=30"""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "PortGroupInSystemInstanceRef":
        """Tags: xml.sequenceOffset=30
        A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextCompositionRef(self) -> Optional[RefType]:
        """Tags: xml.sequenceOffset=20"""
        return self.contextCompositionRef

    def setContextCompositionRef(self, value: Optional[RefType]) -> "PortGroupInSystemInstanceRef":
        """Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextCompositionRef."""
        if value is not None:
            self.contextCompositionRef = value
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """Link to a PortGroup that is defined in a component which is part of this CompositionSwComponentType. Tags: xml.sequenceOffset=40"""
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "PortGroupInSystemInstanceRef":
        """Link to a PortGroup that is defined in a component which is part of this CompositionSwComponentType. Tags: xml.sequenceOffset=40
        A None value is a no-op and does not overwrite an existing targetRef."""
        if value is not None:
            self.targetRef = value
        return self
