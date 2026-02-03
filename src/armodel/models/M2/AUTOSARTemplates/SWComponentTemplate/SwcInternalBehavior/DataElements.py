"""
This module contains classes for representing AUTOSAR data elements
in software component internal behavior templates.
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


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
