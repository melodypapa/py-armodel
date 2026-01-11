"""
This module contains classes for representing AUTOSAR variable references
in software component internal behavior templates.
"""

from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import ArVariableInImplementationDataInstanceRef
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef


class AutosarVariableRef(ARObject):
    def __init__(self):
        super().__init__()

        self.autosarVariableIRef: VariableInAtomicSWCTypeInstanceRef = None
        self.autosarVariableInImplDatatype: ArVariableInImplementationDataInstanceRef = None
        self.localVariableRef: 'VariableInAtomicSWCTypeInstanceRef' = None

    def getAutosarVariableIRef(self) -> VariableInAtomicSWCTypeInstanceRef:
        return self.autosarVariableIRef

    def setAutosarVariableIRef(self, value):
        self.autosarVariableIRef = value
        return self

    def getAutosarVariableInImplDatatype(self) -> ArVariableInImplementationDataInstanceRef:
        """Get the autosarVariableInImplDatatype attribute."""
        return self.autosarVariableInImplDatatype

    def setAutosarVariableInImplDatatype(self, value):
        self.autosarVariableInImplDatatype = value
        return self

    def getLocalVariableRef(self):
        return self.localVariableRef

    def setLocalVariableRef(self, value):
        self.localVariableRef = value
        return self
