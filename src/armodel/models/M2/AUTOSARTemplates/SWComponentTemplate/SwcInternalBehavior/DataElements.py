from ....AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from ....AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from ....AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from ....MSR.DataDictionary.DataDefProperties import SwDataDefProps

class ParameterAccess(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessedParameter = None   # type: AutosarParameterRef
        self.swDataDefProps = None      # type: SwDataDefProps

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

        self.accessedVariableRef = None                             # type: AutosarVariableRef
        self.scope = None                                           # type: ARLiteral

    def getAccessedVariableRef(self):
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value):
        self.accessedVariableRef = value
        return self

    def getScope(self):
        return self.scope

    def setScope(self, value):
        self.scope = value
        return self
