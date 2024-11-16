from abc import ABCMeta
from typing import List

from ...M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from ...M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat

from ...fibex.lin_communication import LinFrameTriggering
from ...fibex.can_communication import CanFrameTriggering
from ...ar_ref import RefType
from ...general_structure import Identifiable
from ...ar_object import ARLiteral
from ...fibex.fibex_core.core_communication import FibexElement, FrameTriggering, ISignalTriggering, PduTriggering

class PhysicalChannel (Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == PhysicalChannel:
            raise NotImplementedError("PhysicalChannel is an abstract class.")
        
        super().__init__(parent, short_name)

        self.commConnectorRefs = []                     # type: List[RefType]
        self.managedPhysicalChannelRefs = []            # type: List[RefType]

    def getCommConnectorRefs(self):
        return self.commConnectorRefs

    def addCommConnectorRef(self, value):
        self.commConnectorRefs.append(value)
        return self

    def getFrameTriggerings(self) -> List[FrameTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, FrameTriggering), self.elements.values()), key= lambda o:o.short_name))

    def createCanFrameTriggering(self, short_name: str):
        if (short_name not in self.elements):
            channel = CanFrameTriggering(self, short_name)
            self.elements[short_name] = channel
        return self.elements[short_name]
    
    def createLinFrameTriggering(self, short_name: str):
        if (short_name not in self.elements):
            channel = LinFrameTriggering(self, short_name)
            self.elements[short_name] = channel
        return self.elements[short_name]

    def getISignalTriggerings(self) -> List[ISignalTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, ISignalTriggering), self.elements.values()), key= lambda o:o.short_name))

    def createISignalTriggering(self, short_name: str):
        if (short_name not in self.elements):
            channel = ISignalTriggering(self, short_name)
            self.elements[short_name] = channel
        return self.elements[short_name]
    

    def getManagedPhysicalChannelRefs(self):
        return self.managedPhysicalChannelRefs

    def addManagedPhysicalChannelRef(self, value):
        self.managedPhysicalChannelRefs.append(value)
        return self
    
    def getPduTriggerings(self) -> List[PduTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, PduTriggering), self.elements.values()), key= lambda o:o.short_name))

    def createPduTriggering(self, short_name: str):
        if (short_name not in self.elements):
            channel = PduTriggering(self, short_name)
            self.elements[short_name] = channel
        return self.elements[short_name]

class AbstractCanPhysicalChannel(PhysicalChannel, metaclass = ABCMeta):
    def __init__(self, parent, short_name):
        if type(self) == ARObject:
            raise NotImplementedError("AbstractCanPhysicalChannel is an abstract class.")
         
        super().__init__(parent, short_name)

class CanPhysicalChannel(AbstractCanPhysicalChannel):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name) 

class LinPhysicalChannel(PhysicalChannel):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name) 

class CommunicationCluster(FibexElement, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == CommunicationCluster:
            raise NotImplementedError("CommunicationCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.baudrate = None                # type: ARFloat
        self.protocolName = None            # type: ARLiteral
        self.protocolVersion = None         # type: ARLiteral

    def getBaudrate(self):
        return self.baudrate

    def setBaudrate(self, value):
        self.baudrate = value
        return self

    def getPhysicalChannels(self) -> List[PhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, PhysicalChannel), self.elements.values()), key= lambda o:o.short_name))
    
    def getCanPhysicalChannels(self) -> List[CanPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, CanPhysicalChannel), self.elements.values()), key= lambda o:o.short_name))
    
    def getLinPhysicalChannels(self) -> List[LinPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, LinPhysicalChannel), self.elements.values()), key= lambda o:o.short_name))
    
    def createCanPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = CanPhysicalChannel(self, short_name)
            self.elements[short_name] = channel
        return self.elements[short_name]
    
    def createLinPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = LinPhysicalChannel(self, short_name)
            self.elements[short_name] = channel
        return self.elements[short_name]

    def getProtocolName(self):
        return self.protocolName

    def setProtocolName(self, value):
        self.protocolName = value
        return self

    def getProtocolVersion(self):
        return self.protocolVersion

    def setProtocolVersion(self, value):
        self.protocolVersion = value
        return self      
    
class AbstractCanCluster(CommunicationCluster, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractCanCluster:
            raise NotImplementedError("AbstractCanCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.busOffRecovery = None
        self.canFdBaudrate = None
        self.canXlBaudrate = None

    def getBusOffRecovery(self):
        return self.busOffRecovery

    def setBusOffRecovery(self, value):
        self.busOffRecovery = value
        return self

    def getCanFdBaudrate(self):
        return self.canFdBaudrate

    def setCanFdBaudrate(self, value):
        self.canFdBaudrate = value
        return self

    def getCanXlBaudrate(self):
        return self.canXlBaudrate

    def setCanXlBaudrate(self, value):
        self.canXlBaudrate = value
        return self


class CanCluster(AbstractCanCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)         

class LinCluster(CommunicationCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)                 

class EcuInstance(FibexElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)    