from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....general_structure import Identifiable
from .....ar_object import ARLiteral
from ....MSR.data_dictionary.data_def_properties import SwDataDefProps
from ..swc_internal_behavior.instance_refs_usage import AutosarParameterRef, AutosarVariableRef
from .access_count import AbstractAccessPoint
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