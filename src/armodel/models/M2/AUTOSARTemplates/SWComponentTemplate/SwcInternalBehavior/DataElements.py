"""
This module contains classes for representing AUTOSAR data elements
in software component internal behavior templates.
"""

from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import AutosarVariableRef
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from .....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


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


class VariableAccess(Identifiable):
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
