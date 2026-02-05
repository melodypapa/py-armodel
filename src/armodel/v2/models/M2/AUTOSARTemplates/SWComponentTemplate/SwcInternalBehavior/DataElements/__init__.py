"""
This module contains classes for representing AUTOSAR data elements
in software component internal behavior templates.
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefs import (
    ParameterInAtomicSWCTypeInstanceRef,
    VariableInAtomicSWCTypeInstanceRef,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
)


class AutosarVariableRef(ARObject):
    def __init__(self):
        super().__init__()

        self.autosarVariableIRef: 'VariableInAtomicSWCTypeInstanceRef' = None
        self.autosarVariableInImplDatatype: 'ArVariableInImplementationDataInstanceRef' = None
        self.localVariableRef: 'VariableInAtomicSWCTypeInstanceRef' = None

    def getAutosarVariableIRef(self) -> 'VariableInAtomicSWCTypeInstanceRef':
        return self.autosarVariableIRef

    def setAutosarVariableIRef(self, value):
        self.autosarVariableIRef = value
        return self

    def getAutosarVariableInImplDatatype(self) -> 'ArVariableInImplementationDataInstanceRef':
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


class AutosarParameterRef(ARObject):
    def __init__(self):
        super().__init__()

        self.autosarParameterIRef: 'ParameterInAtomicSWCTypeInstanceRef' = None
        self.localParameterRef: 'RefType' = None

    def getAutosarParameterIRef(self):
        return self.autosarParameterIRef

    def setAutosarParameterIRef(self, value):
        self.autosarParameterIRef = value
        return self

    def getLocalParameterRef(self):
        return self.localParameterRef

    def setLocalParameterRef(self, value):
        self.localParameterRef = value
        return self


class ParameterAccess(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessedParameter: 'AutosarParameterRef' = None
        self.swDataDefProps: 'SwDataDefProps' = None

    def getAccessedParameter(self):
        return self.accessedParameter

    def setAccessedParameter(self, value):
        self.accessedParameter = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self


class VariableAccess(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name):
        super().__init__(parent, short_name)

        self.accessedVariableRef: 'AutosarVariableRef' = None
        self.scope: ARLiteral = None

    def getAccessedVariableRef(self) -> 'AutosarVariableRef':
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value: 'AutosarVariableRef'):
        if value is not None:
            self.accessedVariableRef = value
        return self

    def getScope(self):
        return self.scope

    def setScope(self, value):
        self.scope = value
        return self


class ArVariableInImplementationDataInstanceRef(ARObject):
    def __init__(self):
        super().__init__()

        self.contextDataPrototypeRefs: List[RefType] = []
        self.portPrototypeRef: RefType = None
        self.rootVariableDataPrototypeRef: RefType = None
        self.targetDataPrototypeRef: RefType = None

    def getContextDataPrototypeRefs(self):
        return self.contextDataPrototypeRefs

    def setContextDataPrototypeRefs(self, value):
        self.contextDataPrototypeRefs = value
        return self

    def getPortPrototypeRef(self):
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self):
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value):
        self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        self.targetDataPrototypeRef = value
        return self


__all__ = [
    'AutosarVariableRef',
    'AutosarParameterRef',
    'ParameterAccess',
    'VariableAccess',
    'ArVariableInImplementationDataInstanceRef',
]
