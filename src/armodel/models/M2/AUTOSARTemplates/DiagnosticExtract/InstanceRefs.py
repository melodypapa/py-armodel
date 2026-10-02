# This module contains AUTOSAR Diagnostic Extract Template classes for instance references
# It defines the PModeInSystemInstanceRef used by DiagnosticEnvSwcModeElement

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class PModeInSystemInstanceRef(AtpInstanceRef):
    """
    Instance reference to a mode declaration of a concrete System context, reached
    through an optional RootSwCompositionPrototype context composition, a chain of
    SwComponentPrototypes and an optional provided port.
    Aggregated by DiagnosticEnvSwcModeElement.mode.
    """

    # PModeInSystemInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate (DiagnosticExtract::InstanceRefs), AUTOSAR_00052.xsd line 87429 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                         [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseRef                         [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextCompositionRef           [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextCompositionRef           [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextComponentRefs            [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextComponentRef             [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextPPortRef                 [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextPPortRef                 [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextModeDeclarationGroupRef  [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextModeDeclarationGroupRef  [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetModeRef                   [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetModeRef                   [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The System that is the base of this instance ref. Stereotypes: atpDerived (derived attribute, no XML element).
        self.baseRef: Optional[RefType] = None

        # This represents the context RootSwCompositionPrototype (xml.sequenceOffset=20).
        self.contextCompositionRef: Optional[RefType] = None

        # This represents the chain of context SwComponentPrototypes (xml.sequenceOffset=30, 0..*).
        self.contextComponentRefs: List[RefType] = []

        # This represents the context provided port prototype (xml.sequenceOffset=40).
        self.contextPPortRef: Optional[RefType] = None

        # This represents the context ModeDeclarationGroupPrototype (xml.sequenceOffset=50).
        self.contextModeDeclarationGroupRef: Optional[RefType] = None

        # This represents the target mode declaration (xml.sequenceOffset=60).
        self.targetModeRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        if value is not None:
            self.baseRef = value
        return self

    def getContextCompositionRef(self) -> Optional[RefType]:
        return self.contextCompositionRef

    def setContextCompositionRef(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        if value is not None:
            self.contextCompositionRef = value
        return self

    def getContextComponentRefs(self) -> List[RefType]:
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextPPortRef(self) -> Optional[RefType]:
        return self.contextPPortRef

    def setContextPPortRef(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        if value is not None:
            self.contextPPortRef = value
        return self

    def getContextModeDeclarationGroupRef(self) -> Optional[RefType]:
        return self.contextModeDeclarationGroupRef

    def setContextModeDeclarationGroupRef(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        if value is not None:
            self.contextModeDeclarationGroupRef = value
        return self

    def getTargetModeRef(self) -> Optional[RefType]:
        return self.targetModeRef

    def setTargetModeRef(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        if value is not None:
            self.targetModeRef = value
        return self
