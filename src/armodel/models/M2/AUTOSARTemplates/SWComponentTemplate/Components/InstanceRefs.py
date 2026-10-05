"""
This module contains classes for representing AUTOSAR instance references
in the SWComponentTemplate module. These classes are used for referencing
elements within atomic SWCs and compositions, particularly for mode groups
and data elements in instance contexts.
"""

from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class ModeGroupInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    # ModeGroupInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.24, p.961 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBaseRef          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextPortRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setContextPortRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTargetRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setTargetRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is ModeGroupInAtomicSwcInstanceRef:
            raise TypeError("ModeGroupInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        self.contextPortRef: Optional[RefType] = None

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "ModeGroupInAtomicSwcInstanceRef":
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        """
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "ModeGroupInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPortRef.
        """
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        """
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "ModeGroupInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetRef.
        """
        if value is not None:
            self.targetRef = value
        return self


class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    # PModeGroupInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.12, p.949 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextPPortRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPPortRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetModeGroupRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetModeGroupRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Tags: xml.sequenceOffset=20
        self.contextPPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetModeGroupRef: Optional[RefType] = None

    def getContextPPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextPPortRef

    def setContextPPortRef(self, value: Optional[RefType]) -> "PModeGroupInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPPortRef.
        """
        if value is not None:
            self.contextPPortRef = value
        return self

    def getTargetModeGroupRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetModeGroupRef

    def setTargetModeGroupRef(self, value: Optional[RefType]) -> "PModeGroupInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetModeGroupRef.
        """
        if value is not None:
            self.targetModeGroupRef = value
        return self


class RModeGroupInAtomicSWCInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    # RModeGroupInAtomicSWCInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.11, p.948 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRPortRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextRPortRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetModeGroupRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetModeGroupRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Tags: xml.sequenceOffset=20
        self.contextRPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetModeGroupRef: Optional[RefType] = None

    def getContextRPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextRPortRef

    def setContextRPortRef(self, value: Optional[RefType]) -> "RModeGroupInAtomicSWCInstanceRef":
        """
        Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextRPortRef.
        """
        if value is not None:
            self.contextRPortRef = value
        return self

    def getTargetModeGroupRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetModeGroupRef

    def setTargetModeGroupRef(self, value: Optional[RefType]) -> "RModeGroupInAtomicSWCInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetModeGroupRef.
        """
        if value is not None:
            self.targetModeGroupRef = value
        return self


class RModeInAtomicSwcInstanceRef(AtpInstanceRef):
    # RModeInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.3, p.943 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                    [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBaseRef                                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextModeDeclarationGroupPrototypeRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextModeDeclarationGroupPrototypeRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextPortRef                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPortRef                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetModeDeclarationRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetModeDeclarationRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.contextModeDeclarationGroupPrototypeRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=20
        self.contextPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=40
        self.targetModeDeclarationRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "RModeInAtomicSwcInstanceRef":
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextModeDeclarationGroupPrototypeRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.contextModeDeclarationGroupPrototypeRef

    def setContextModeDeclarationGroupPrototypeRef(self, value: Optional[RefType]) -> "RModeInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing contextModeDeclarationGroupPrototypeRef.
        """
        if value is not None:
            self.contextModeDeclarationGroupPrototypeRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "RModeInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPortRef.
        """
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetModeDeclarationRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=40
        """
        return self.targetModeDeclarationRef

    def setTargetModeDeclarationRef(self, value: Optional[RefType]) -> "RModeInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=40
        A None value is a no-op and does not overwrite an existing targetModeDeclarationRef.
        """
        if value is not None:
            self.targetModeDeclarationRef = value
        return self


class TriggerInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    # TriggerInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.5, p.945 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBaseRef          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextPortRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setContextPortRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTargetRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setTargetRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is TriggerInAtomicSwcInstanceRef:
            raise TypeError("TriggerInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        self.contextPortRef: Optional[RefType] = None

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        """
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPortRef.
        """
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        """
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetRef.
        """
        if value is not None:
            self.targetRef = value
        return self


class PTriggerInAtomicSwcTypeInstanceRef(TriggerInAtomicSwcInstanceRef):
    # PTriggerInAtomicSwcTypeInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.7, p.946 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextPPortRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPPortRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetTriggerRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetTriggerRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Tags: xml.sequenceOffset=20
        self.contextPPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetTriggerRef: Optional[RefType] = None

    def getContextPPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextPPortRef

    def setContextPPortRef(self, value: Optional[RefType]) -> "PTriggerInAtomicSwcTypeInstanceRef":
        """
        Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPPortRef.
        """
        if value is not None:
            self.contextPPortRef = value
        return self

    def getTargetTriggerRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetTriggerRef

    def setTargetTriggerRef(self, value: Optional[RefType]) -> "PTriggerInAtomicSwcTypeInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetTriggerRef.
        """
        if value is not None:
            self.targetTriggerRef = value
        return self


class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    # RTriggerInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.6, p.945
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRPortRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextRPortRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetTriggerRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetTriggerRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Tags: xml.sequenceOffset=20
        self.contextRPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetTriggerRef: Optional[RefType] = None

    def getContextRPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextRPortRef

    def setContextRPortRef(self, value: Optional[RefType]) -> "RTriggerInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=20

        A None value is a no-op and does not overwrite an existing contextRPortRef.
        """
        if value is not None:
            self.contextRPortRef = value
        return self

    def getTargetTriggerRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetTriggerRef

    def setTargetTriggerRef(self, value: Optional[RefType]) -> "RTriggerInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=30

        A None value is a no-op and does not overwrite an existing targetTriggerRef.
        """
        if value is not None:
            self.targetTriggerRef = value
        return self


class VariableInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    """"""

    # VariableInAtomicSwcInstanceRef method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.1, p.941 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAbstractTargetDataElementRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAbstractTargetDataElementRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseRef                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextPortRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPortRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is VariableInAtomicSwcInstanceRef:
            raise TypeError("VariableInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.abstractTargetDataElementRef: Optional[RefType] = None

        self.baseRef: Optional[RefType] = None

        self.contextPortRef: Optional[RefType] = None

    def getAbstractTargetDataElementRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        """
        return self.abstractTargetDataElementRef

    def setAbstractTargetDataElementRef(self, value: Optional[RefType]) -> "VariableInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing abstractTargetDataElementRef.
        """
        if value is not None:
            self.abstractTargetDataElementRef = value
        return self

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "VariableInAtomicSwcInstanceRef":
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        """
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "VariableInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPortRef.
        """
        if value is not None:
            self.contextPortRef = value
        return self


class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    # RVariableInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.2, p.943 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRPortRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextRPortRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetDataElementRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetDataElementRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Tags: xml.sequenceOffset=20
        self.contextRPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetDataElementRef: Optional[RefType] = None

    def getContextRPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextRPortRef

    def setContextRPortRef(self, value: Optional[RefType]) -> "RVariableInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextRPortRef.
        """
        if value is not None:
            self.contextRPortRef = value
        return self

    def getTargetDataElementRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetDataElementRef

    def setTargetDataElementRef(self, value: Optional[RefType]) -> "RVariableInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetDataElementRef.
        """
        if value is not None:
            self.targetDataElementRef = value
        return self


class InnerPortGroupInCompositionInstanceRef(AtpInstanceRef):
    # InnerPortGroupInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.4, p.943 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBaseRef      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRefs  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addContextRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getTargetRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setTargetRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=20
        self.contextRefs: List[RefType] = []

        # Links a PortGroup in a composition to another PortGroup, that is defined in a component which is part of this CompositionSwComponentType. There shall be at most one innerGroup per contained SwComponentPrototype. Tags: xml.sequenceOffset=30
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10"""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "InnerPortGroupInCompositionInstanceRef":
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10 Only sets the value if it is not None, and returns self for method chaining."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextRefs(self) -> List[RefType]:
        """Tags: xml.sequenceOffset=20"""
        return self.contextRefs

    def addContextRef(self, value: Optional[RefType]) -> "InnerPortGroupInCompositionInstanceRef":
        """Tags: xml.sequenceOffset=20 Only adds the value if it is not None, and returns self for method chaining."""
        if value is not None:
            self.contextRefs.append(value)
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """Links a PortGroup in a composition to another PortGroup, that is defined in a component which is part of this CompositionSwComponentType. There shall be at most one innerGroup per contained SwComponentPrototype. Tags: xml.sequenceOffset=30"""
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "InnerPortGroupInCompositionInstanceRef":
        """Links a PortGroup in a composition to another PortGroup, that is defined in a component which is part of this CompositionSwComponentType. There shall be at most one innerGroup per contained SwComponentPrototype. Tags: xml.sequenceOffset=30 Only sets the value if it is not None, and returns self for method chaining."""
        if value is not None:
            self.targetRef = value
        return self


class OperationInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    # OperationInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.8, p.946 (R23-11; body renders below the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBaseRef                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextPortRef         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setContextPortRef         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTargetOperationRef     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setTargetOperationRef     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is OperationInAtomicSwcInstanceRef:
            raise TypeError("OperationInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        self.contextPortRef: Optional[RefType] = None

        # Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        self.targetOperationRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "OperationInAtomicSwcInstanceRef":
        """
        Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        """
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "OperationInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPortRef.
        """
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetOperationRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        """
        return self.targetOperationRef

    def setTargetOperationRef(self, value: Optional[RefType]) -> "OperationInAtomicSwcInstanceRef":
        """
        Stereotypes: atpAbstract Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetOperationRef.
        """
        if value is not None:
            self.targetOperationRef = value
        return self


class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    # POperationInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.10, p.948 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextPPortRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPPortRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetProvidedOperationRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetProvidedOperationRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Tags: xml.sequenceOffset=20
        self.contextPPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetProvidedOperationRef: Optional[RefType] = None

    def getContextPPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextPPortRef

    def setContextPPortRef(self, value: Optional[RefType]) -> "POperationInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextPPortRef.
        """
        if value is not None:
            self.contextPPortRef = value
        return self

    def getTargetProvidedOperationRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetProvidedOperationRef

    def setTargetProvidedOperationRef(self, value: Optional[RefType]) -> "POperationInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetProvidedOperationRef.
        """
        if value is not None:
            self.targetProvidedOperationRef = value
        return self


class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    # ROperationInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.9, p.947 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRPortRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextRPortRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetRequiredOperationRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetRequiredOperationRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Tags: xml.sequenceOffset=20
        self.contextRPortRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetRequiredOperationRef: Optional[RefType] = None

    def getContextRPortRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=20
        """
        return self.contextRPortRef

    def setContextRPortRef(self, value: Optional[RefType]) -> "ROperationInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextRPortRef.
        """
        if value is not None:
            self.contextRPortRef = value
        return self

    def getTargetRequiredOperationRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetRequiredOperationRef

    def setTargetRequiredOperationRef(self, value: Optional[RefType]) -> "ROperationInAtomicSwcInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetRequiredOperationRef.
        """
        if value is not None:
            self.targetRequiredOperationRef = value
        return self
