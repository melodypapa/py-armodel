# This module contains AUTOSAR System Template classes for transport protocols
# It defines CAN, DoIP, and LIN transport protocol configurations and connections

from abc import ABCMeta
from typing import List

from ....M2.AUTOSARTemplates.SystemTemplate.DoIp import AbstractDoIpLogicAddressProps
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType, TimeValue
from ....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TpConfig(FibexElement, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == TpConfig:
            raise NotImplementedError("TpConfig is an abstract class.")
        
        super().__init__(parent, short_name)

        self.communicationClusterRef: RefType = None

    def getCommunicationClusterRef(self):
        return self.communicationClusterRef

    def setCommunicationClusterRef(self, value):
        if value is not None:
            self.communicationClusterRef = value
        return self
    
class CanTpAddress(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.tpAddress: Integer = None
        self.tpAddressExtensionValue: Integer = None

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

        self.channelId: PositiveInteger = None
        self.channelMode: CanTpChannelModeType = None

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

class TpConnectionIdent(Referrable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)    

class TpConnection(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == TpConnection:
            raise NotImplementedError("TpConnection is an abstract class.")
        
        super().__init__()

        self.ident: TpConnectionIdent = None

    def getIdent(self):
        return self.ident

    def createTpConnectionIdent(self, short_name: str):
        ident = TpConnectionIdent(self, short_name)
        self.ident = ident
        return ident

class CanTpConnection(TpConnection):
    def __init__(self):
        super().__init__()

        self.addressingFormat: CanTpAddressingFormatType = None
        self.cancellation: Boolean = None
        self.canTpChannelRef: RefType = None
        self.dataPduRef: RefType = None
        self.flowControlPduRef: RefType = None
        self.maxBlockSize: Integer = None
        self.multicastRef: RefType = None
        self.paddingActivation: Boolean = None
        self.receiverRefs: List[RefType] = []
        self.taType: NetworkTargetAddressType = None
        self.timeoutBr: TimeValue = None
        self.timeoutBs: TimeValue = None
        self.timeoutCr: TimeValue = None
        self.timeoutCs: TimeValue = None
        self.tpSduRef: RefType = None
        self.transmitterRef: RefType = None

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

    def getReceiverRefs(self):
        return self.receiverRefs

    def addReceiverRef(self, value):
        if value is not None:
            self.receiverRefs.append(value) 
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

class CanTpEcu(ARObject):
    def __init__(self):
        super().__init__()

        self.cycleTimeMainFunction: TimeValue = None
        self.ecuInstanceRef: RefType = None

    def getCycleTimeMainFunction(self):
        return self.cycleTimeMainFunction

    def setCycleTimeMainFunction(self, value):
        if value is not None:
            self.cycleTimeMainFunction = value
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        if value is not None:
            self.ecuInstanceRef = value
        return self
    
class CanTpNode(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.connectorRef: RefType = None
        self.maxFcWait: Integer = None
        self.stMin: TimeValue = None
        self.timeoutAr: TimeValue = None
        self.timeoutAs: TimeValue = None
        self.tpAddressRef: RefType = None

    def getConnectorRef(self):
        return self.connectorRef

    def setConnectorRef(self, value):
        if value is not None:
            self.connectorRef = value
        return self

    def getMaxFcWait(self):
        return self.maxFcWait

    def setMaxFcWait(self, value):
        if value is not None:
            self.maxFcWait = value
        return self

    def getStMin(self):
        return self.stMin

    def setStMin(self, value):
        if value is not None:
            self.stMin = value
        return self

    def getTimeoutAr(self):
        return self.timeoutAr

    def setTimeoutAr(self, value):
        if value is not None:
            self.timeoutAr = value
        return self
    
    def getTimeoutAs(self):
        return self.timeoutAs

    def setTimeoutAs(self, value):
        if value is not None:
            self.timeoutAs = value
        return self
    
    def getTpAddressRef(self):
        return self.tpAddressRef

    def setTpAddressRef(self, value):
        if value is not None:
            self.tpAddressRef = value
        return self



class CanTpConfig(TpConfig):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.tpAddresses: List[CanTpAddress] = []
        self.tpChannels: List[CanTpChannel] = []
        self.tpConnections:List[CanTpConnection] = []
        self.tpEcus: List[CanTpEcu] = []
        self.tpNodes: List[CanTpNode] = []

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
    
    def addTpConnection(self, value):
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpEcus(self):
        return self.tpEcus

    def addTpEcu(self, value):
        if value is not None:
            self.tpEcus.append(value)
        return self

    def getTpNodes(self):
        return self.tpNodes

    def createCanTpNode(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            address = CanTpNode(self, short_name)
            self.addElement(address)
            self.tpNodes.append(address)
        return self.getElement(short_name)
    
class DoIpLogicAddress(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.address: Integer = None
        self.doIpLogicAddressProps: AbstractDoIpLogicAddressProps = None

    def getAddress(self):
        return self.address

    def setAddress(self, value):
        if value is not None:
            self.address = value
        return self

    def getDoIpLogicAddressProps(self):
        return self.doIpLogicAddressProps

    def setDoIpLogicAddressProps(self, value):
        if value is not None:
            self.doIpLogicAddressProps = value
        return self

class DoIpTpConnection(TpConnection):
    def __init__(self):
        super().__init__()

        self.doIpSourceAddressRef: RefType = None
        self.doIpTargetAddressRef: RefType = None
        self.tpSduRef: RefType = None

    def getDoIpSourceAddressRef(self):
        return self.doIpSourceAddressRef

    def setDoIpSourceAddressRef(self, value):
        if value is not None:
            self.doIpSourceAddressRef = value
        return self

    def getDoIpTargetAddressRef(self):
        return self.doIpTargetAddressRef

    def setDoIpTargetAddressRef(self, value):
        if value is not None:
            self.doIpTargetAddressRef = value
        return self

    def getTpSduRef(self):
        return self.tpSduRef

    def setTpSduRef(self, value):
        if value is not None:
            self.tpSduRef = value
        return self


class DoIpTpConfig(TpConfig):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.doIpLogicAddresses: List[DoIpLogicAddress] = []
        self.tpConnections: List[DoIpTpConnection] = []

    def getDoIpLogicAddresses(self):
        return self.doIpLogicAddresses

    def createDoIpLogicAddress(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            address = DoIpLogicAddress(self, short_name)
            self.addElement(address)
            self.doIpLogicAddresses.append(address)
        return self.getElement(short_name)

    def getTpConnections(self):
        return self.tpConnections

    def addTpConnection(self, value):
        if value is not None:
            self.tpConnections.append(value)
        return self
        
class TpAddress(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.tpAddress: Integer = None

    def getTpAddress(self):
        return self.tpAddress

    def setTpAddress(self, value):
        if value is not None:
            self.tpAddress = value
        return self
    
class LinTpConnection(TpConnection):
    def __init__(self):
        super().__init__()

        self.dataPduRef: RefType = None
        self.flowControlRef: RefType = None
        self.linTpNSduRef: RefType = None
        self.multicastRef: RefType = None
        self.receiverRefs: List[RefType] = []
        self.timeoutAs: TimeValue = None
        self.timeoutCr: TimeValue = None
        self.timeoutCs: TimeValue = None
        self.transmitterRef: RefType = None

    def getDataPduRef(self):
        return self.dataPduRef

    def setDataPduRef(self, value):
        if value is not None:
            self.dataPduRef = value
        return self

    def getFlowControlRef(self):
        return self.flowControlRef

    def setFlowControlRef(self, value):
        if value is not None:
            self.flowControlRef = value
        return self

    def getLinTpNSduRef(self):
        return self.linTpNSduRef

    def setLinTpNSduRef(self, value):
        if value is not None:
            self.linTpNSduRef = value
        return self

    def getMulticastRef(self):
        return self.multicastRef

    def setMulticastRef(self, value):
        if value is not None:
            self.multicastRef = value
        return self

    def getReceiverRefs(self):
        return self.receiverRefs

    def addReceiverRef(self, value):
        if value is not None:
            self.receiverRefs.append(value)
        return self

    def getTimeoutAs(self):
        return self.timeoutAs

    def setTimeoutAs(self, value):
        if value is not None:
            self.timeoutAs = value
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

    def getTransmitterRef(self):
        return self.transmitterRef

    def setTransmitterRef(self, value):
        if value is not None:
            self.transmitterRef = value
        return self

class LinTpNode(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.connectorRef: RefType = None
        self.dropNotRequestedNad: Boolean = None
        self.maxNumberOfRespPendingFrames: Integer = None
        self.p2Max: TimeValue = None
        self.p2Timing: TimeValue = None
        self.tpAddressRef: RefType = None

    def getConnectorRef(self):
        return self.connectorRef

    def setConnectorRef(self, value):
        if value is not None:
            self.connectorRef = value
        return self

    def getDropNotRequestedNad(self):
        return self.dropNotRequestedNad

    def setDropNotRequestedNad(self, value):
        if value is not None:
            self.dropNotRequestedNad = value
        return self

    def getMaxNumberOfRespPendingFrames(self):
        return self.maxNumberOfRespPendingFrames

    def setMaxNumberOfRespPendingFrames(self, value):
        if value is not None:
            self.maxNumberOfRespPendingFrames = value
        return self

    def getP2Max(self):
        return self.p2Max

    def setP2Max(self, value):
        if value is not None:
            self.p2Max = value
        return self

    def getP2Timing(self):
        return self.p2Timing

    def setP2Timing(self, value):
        if value is not None:
            self.p2Timing = value
        return self

    def getTpAddressRef(self):
        return self.tpAddressRef

    def setTpAddressRef(self, value):
        if value is not None:
            self.tpAddressRef = value
        return self

 
class LinTpConfig(TpConfig):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.tpAddresses: List[TpAddress] = []
        self.tpConnections: List[LinTpConnection] = []
        self.tpNodes: List[LinTpNode] = []

    def getTpAddresses(self):
        return self.tpAddresses

    def createTpAddress(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            address = TpAddress(self, short_name)
            self.addElement(address)
            self.tpAddresses.append(address)
        return self.getElement(short_name)

    def getTpConnections(self):
        return self.tpConnections

    def addTpConnection(self, value):
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpNodes(self):
        return self.tpNodes
    
    def createLinTpNode(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            address = LinTpNode(self, short_name)
            self.addElement(address)
            self.tpNodes.append(address)
        return self.getElement(short_name)