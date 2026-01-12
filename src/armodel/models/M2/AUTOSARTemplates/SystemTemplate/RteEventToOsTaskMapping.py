# This module contains AUTOSAR System Template classes for RTE event to OS task mapping
# It defines mappings between application and ECU task proxies for real-time execution

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """
    Represents a mapping between application OS task proxies and ECU task proxies
    in the Runtime Environment (RTE), defining how application-level tasks are
    connected to ECU-level tasks for real-time execution coordination.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.appTaskProxyRef: RefType = None
        self.ecuTaskProxyRef: RefType = None
        self.offset: RefType = None

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