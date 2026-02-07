# This module contains AUTOSAR System Template classes for RTE event to OS task mapping
# It defines mappings between application and ECU task proxies for real-time execution

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Represents a mapping between application OS task proxies and ECU task proxies
    in the Runtime Environment (RTE), defining how application-level tasks are
    connected to ECU-level tasks for real-time execution coordination.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.appTaskProxyRef: Union[Union[RefType, None] , None] = None
        self.ecuTaskProxyRef: Union[Union[RefType, None] , None] = None
        self.offset: Union[Union[RefType, None] , None] = None

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
