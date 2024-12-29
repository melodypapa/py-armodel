from abc import ABCMeta
from typing import List

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TpConfig(FibexElement, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ARObject:
            raise NotImplementedError("ARObject is an abstract class.")
        
        super().__init__(parent, short_name)

        self.communicationClusterRef = None                                 # type: RefType

    def getCommunicationClusterRef(self):
        return self.communicationClusterRef

    def setCommunicationClusterRef(self, value):
        if value is not None:
            self.communicationClusterRef = value
        return self


class CanTpConfig(TpConfig):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class DoIpTpConfig(TpConfig):
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

class LinTpConfig(TpConfig):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.tpAddresses = []                                       # type: List[TpAddress]
        self.tpConnections = []                                     # type: List[LinTpConnection]
        self.tpNodes = []                                           # type: List[LinTpNode]

    def getTpAddresses(self):
        return self.tpAddresses

    def addTpAddress(self, value):
        if value is not None:
            self.tpAddresses.append(value)
        return self

    def getTpConnections(self):
        return self.tpConnections

    def addTpConnection(self, value):
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpNodes(self):
        return self.tpNodes

    def setTpNode(self, value):
        if value is not None:
            self.tpNodes.append(value)
        return self
