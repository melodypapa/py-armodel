from typing import List
from ....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class CanTpConfig(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class DoIpTpConfig(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.doIpLogicAddresses = []                                # type: List[DoIpLogicAddress]
        self.tpConnections = []                                     # typeL List[DoIpTpConnection]

    def getDoIpLogicAddresses(self):
        return self.doIpLogicAddresses

    def addDoIpLogicAddress(self, value):
        if value is not None:
            self.doIpLogicAddresses.append(value)
        return self

    def getTpConnections(self):
        return self.tpConnections

    def addTpConnection(self, value):
        if value is not None:
            self.tpConnections.append(value)
        return self
