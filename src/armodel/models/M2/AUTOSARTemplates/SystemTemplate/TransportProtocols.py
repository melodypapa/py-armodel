from abc import ABCMeta
from typing import List

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType, TimeValue
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
    
class CanTpAddress(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.tpAddress = None                                           # type: Integer
        self.tpAddressExtensionValue = None                             # type: Integer

    def getTpAddress(self):
        return self.tpAddress

    def setTpAddress(self, value):
        if value is not None:
            self.tpAddress = value
        return self

    def getTpAddressExtensionValue(self):
        return self.tpAddressExtensionValue

    def setTpAddressExtensionValue(self, value):
        if value is not None:
            self.tpAddressExtensionValue = value
        return self
    
class CanTpChannel(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.channelId = None                                       # type: PositiveInteger
        self.channelMode = None                                     # type: CanTpChannelModeType

    def getChannelId(self):
        return self.channelId

    def setChannelId(self, value):
        if value is not None:
            self.channelId = value
        return self

    def getChannelMode(self):
        return self.channelMode

    def setChannelMode(self, value):
        if value is not None:
            self.channelMode = value
        return self

    

class TpConnection(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == TpConnection:
            raise NotImplementedError("TpConnection is an abstract class.")
        
        super().__init__()

        self.ident = None                                               # type: TpConnectionIdent

    def getIdent(self):
        return self.ident

    def setIdent(self, value):
        if value is not None:
            self.ident = value
        return self


class CanTpConnection(TpConnection):
    def __init__(self):
        super().__init__()

        self.addressingFormat = None                                    # type: CanTpAddressingFormatType
        self.cancellation = None                                        # type: Boolean
        self.canTpChannelRef = None                                     # type: RefType
        self.dataPduRef = None                                          # type: RefType
        self.flowControlPduRef = None                                   # type: RefType
        self.maxBlockSize = None                                        # type: Integer
        self.multicastRef = None                                        # type: RefType
        self.paddingActivation = None                                   # type: Boolean
        self.receiverRef = None                                         # type: RefType
        self.taType = None                                              # type: NetworkTargetAddressType
        self.timeoutBr = None                                           # type: TimeValue
        self.timeoutBs = None                                           # type: TimeValue
        self.timeoutCr = None                                           # type: TimeValue
        self.timeoutCs = None                                           # type: TimeValue
        self.tpSduRef = None                                            # type: RefType
        self.transmitterRef = None                                      # type: RefType

    def getAddressingFormat(self):
        return self.addressingFormat

    def setAddressingFormat(self, value):
        if value is not None:
            self.addressingFormat = value
        return self

    def getCancellation(self):
        return self.cancellation

    def setCancellation(self, value):
        if value is not None:
            self.cancellation = value
        return self

    def getCanTpChannelRef(self):
        return self.canTpChannelRef

    def setCanTpChannelRef(self, value):
        if value is not None:
            self.canTpChannelRef = value
        return self

    def getDataPduRef(self):
        return self.dataPduRef

    def setDataPduRef(self, value):
        if value is not None:
            self.dataPduRef = value
        return self

    def getFlowControlPduRef(self):
        return self.flowControlPduRef

    def setFlowControlPduRef(self, value):
        if value is not None:
            self.flowControlPduRef = value
        return self

    def getMaxBlockSize(self):
        return self.maxBlockSize

    def setMaxBlockSize(self, value):
        if value is not None:
            self.maxBlockSize = value
        return self

    def getMulticastRef(self):
        return self.multicastRef

    def setMulticastRef(self, value):
        if value is not None:
            self.multicastRef = value
        return self

    def getPaddingActivation(self):
        return self.paddingActivation

    def setPaddingActivation(self, value):
        if value is not None:
            self.paddingActivation = value
        return self

    def getReceiverRef(self):
        return self.receiverRef

    def setReceiverRef(self, value):
        if value is not None:
            self.receiverRef = value
        return self

    def getTaType(self):
        return self.taType

    def setTaType(self, value):
        if value is not None:
            self.taType = value
        return self

    def getTimeoutBr(self):
        return self.timeoutBr

    def setTimeoutBr(self, value):
        if value is not None:
            self.timeoutBr = value
        return self

    def getTimeoutBs(self):
        return self.timeoutBs

    def setTimeoutBs(self, value):
        if value is not None:
            self.timeoutBs = value
        return self

    def getTimeoutCr(self):
        return self.timeoutCr

    def setTimeoutCr(self, value):
        if value is not None:
            self.timeoutCr = value
        return self

    def getTimeoutCs(self):
        return self.timeoutCs

    def setTimeoutCs(self, value):
        if value is not None:
            self.timeoutCs = value
        return self

    def getTpSduRef(self):
        return self.tpSduRef

    def setTpSduRef(self, value):
        if value is not None:
            self.tpSduRef = value
        return self

    def getTransmitterRef(self):
        return self.transmitterRef

    def setTransmitterRef(self, value):
        if value is not None:
            self.transmitterRef = value
        return self


class CanTpConfig(TpConfig):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.tpAddresses = []                                           # type: List[CanTpAddress]
        self.tpChannels = []                                            # type: List[CanTpChannel]
        self.tpConnections =[]                                          # type: List[CanTpConnection]
        self.tpEcus = []                                                # type: List[CanTpEcu]
        self.tpNodes = []                                               # type: List[CanTpNode]

    def getTpAddresses(self):
        return self.tpAddresses

    def createCanTpAddress(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            address = CanTpAddress(self, short_name)
            self.addElement(address)
            self.tpAddresses.append(address)
        return self.getElement(short_name)

    def getTpChannels(self):
        return self.tpChannels

    def createCanTpChannel(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            address = CanTpChannel(self, short_name)
            self.addElement(address)
            self.tpChannels.append(address)
        return self.getElement(short_name)

    def getTpConnections(self):
        return self.tpConnections

    def setTpConnections(self, value):
        if value is not None:
            self.tpConnections = value
        return self

    def getTpEcus(self):
        return self.tpEcus

    def setTpEcus(self, value):
        if value is not None:
            self.tpEcus = value
        return self

    def getTpNodes(self):
        return self.tpNodes

    def setTpNodes(self, value):
        if value is not None:
            self.tpNodes = value
        return self

        

    


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
