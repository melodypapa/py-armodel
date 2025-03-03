from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.appTaskProxyRef = None                         # type: RefType
        self.ecuTaskProxyRef = None                         # type: RefType
        self.offset = None                                  # type: RefType

    def getAppTaskProxyRef(self):
        return self.appTaskProxyRef

    def setAppTaskProxyRef(self, value):
        if value is not None:
            self.appTaskProxyRef = value
        return self

    def getEcuTaskProxyRef(self):
        return self.ecuTaskProxyRef

    def setEcuTaskProxyRef(self, value):
        if value is not None:
            self.ecuTaskProxyRef = value
        return self

    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        if value is not None:
            self.offset = value
        return self
