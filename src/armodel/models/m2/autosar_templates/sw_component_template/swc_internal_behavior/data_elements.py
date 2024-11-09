

from .access_count import AbstractAccessPoint

from .....general_structure import Identifiable
from ....msr.data_dictionary.data_def_properties import SwDataDefProps
from .....ar_ref import AutosarParameterRef, AutosarVariableRef
from .....ar_object import ARObject

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

        #self.accessedVariableRef = AutosarVariableRef()         # type: AutosarVariableRef
        #self.accessedVariableRef.parent = self
        #self.localVariableRef = None                               # type: RefType

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
