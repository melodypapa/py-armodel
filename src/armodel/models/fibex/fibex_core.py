from abc import ABCMeta
from typing import List

from armodel.models.ar_ref import RefType

from ..ar_object import ARFloat, ARLiteral, ARNumerical, ARObject, ARPositiveInteger
from ..general_structure import Identifiable


class FibexElement(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == FibexElement:
            raise NotImplementedError("FibexElement is an abstract class.")
        
        super().__init__(parent, short_name)

class PhysicalChannel (Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == PhysicalChannel:
            raise NotImplementedError("PhysicalChannel is an abstract class.")
        
        super().__init__(parent, short_name)


class CommunicationCluster(FibexElement):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == CommunicationCluster:
            raise NotImplementedError("CommunicationCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.baudrate = None                # type: ARFloat
        self.physical_channels = []         # type: List[PhysicalChannel]
        self.protocol_name = None           # type: ARLiteral
        self.protocol_version = None        # type: ARLiteral

    def addPhysicalChannel(self, channel: PhysicalChannel):
        self.physical_channels.append(channel)

    def getPhysicalChannels(self) -> List[PhysicalChannel]:
        return self.physical_channels
    
    @property
    def protocolName(self) -> ARLiteral:
        return self.protocol_name
    
    @protocolName.setter
    def protocolName(self, value: ARLiteral):
        self.protocol_name = value

    @property
    def protocolVersion(self) -> ARLiteral:
        return self.protocol_version

    @protocolVersion.setter
    def protocolVersion(self, value: ARLiteral):
        self.protocol_version = value

class Pdu(FibexElement):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Pdu:
            raise NotImplementedError("Pdu is an abstract class.")
        
        super().__init__(parent, short_name)

        self.length = None     # type: ARNumerical

class PduToFrameMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.packing_byte_order = None      # type: ARLiteral
        self.pdu_ref = None                 # type: RefType
        self.start_position = None          # type: ARNumerical

    @property
    def packingByteOrder(self) -> ARLiteral:
        return self.packing_byte_order

    @packingByteOrder.setter
    def packingByteOrder(self, value: ARLiteral):
        self.packing_byte_order = value

    @property
    def pduRef(self) -> RefType:
        return self.pdu_ref

    @pduRef.setter
    def pduRef(self, value: RefType):
        self.pdu_ref = value

    @property
    def startPosition(self) -> ARNumerical:
        return self.start_position

    @startPosition.setter
    def startPosition(self, value: ARNumerical):
        self.start_position = value

class Frame(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Frame:
            raise NotImplementedError("Frame is an abstract class.")
        
        super().__init__(parent, short_name)

        self.frame_length = None
        self.pdu_to_frame_mappings = []        # type: List[PduToFrameMapping]

    @property
    def frameLength(self) -> ARNumerical:
        return self.frame_length

    @frameLength.setter
    def frameLength(self, value: ARNumerical):
        self.frame_length = value

    def createPduToFrameMapping(self, short_name: str) -> PduToFrameMapping:
        if (short_name not in self.elements):
            mapping = PduToFrameMapping(self, short_name)
            self.elements[short_name] = mapping
            self.pdu_to_frame_mappings.append(mapping)
        return self.elements[short_name]

    def getPduToFrameMappings(self) -> List[PduToFrameMapping]:
        return list(sorted(filter(lambda a: isinstance(a, PduToFrameMapping), self.elements.values()), key= lambda o:o.short_name))
    
class ContainedIPduProps(ARObject):
    def __init__(self):
        super().__init__()

        self._collection_semantics = None                # type: ARLiteral
        self._header_id_long_header = None               # type: ARPositiveInteger
        self._header_id_short_header = None              # type: ARPositiveInteger
        self._offset = None                              # type: ARNumerical
        self._timeout = None                             # type: ARNumerical
        self._trigger = None                             # type: ARLiteral
        self._update_indication_bit_position = None      # type: ARNumerical
 
    @property
    def headerIdLongHeader(self) -> ARPositiveInteger:
        return self._header_id_long_header

    @headerIdLongHeader.setter
    def headerIdLongHeader(self, value: ARPositiveInteger):
        self._header_id_long_header = value

    @property
    def headerIdShortHeader(self) -> ARPositiveInteger:
        return self._header_id_short_header

    @headerIdShortHeader.setter
    def headerIdShortHeader(self, value: ARPositiveInteger):
        self._header_id_short_header = value

    @property
    def offset(self) -> ARNumerical:
        return self._offset

    @offset.setter
    def offset(self, value: ARNumerical):
        self._offset = value

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
        
    @property
    def collectionSemantics(self) -> ARLiteral:
        return self._collection_semantics

    @collectionSemantics.setter
    def collectionSemantics(self, value: ARLiteral):
        self._collection_semantics = value
    
    @property
    def trigger(self) -> ARLiteral:
        return self._trigger

    @trigger.setter
    def trigger(self, value: ARLiteral):
        self._trigger = value
       
    @property
    def updateIndicationBitPosition(self) -> ARNumerical:
        return self._update_indication_bit_position

    @updateIndicationBitPosition.setter
    def updateIndicationBitPosition(self, value: ARNumerical):
        self._update_indication_bit_position = value

class IPdu(Pdu):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == IPdu:
            raise NotImplementedError("IPdu is an abstract class.")
        
        super().__init__(parent, short_name)

        self._contained_ipdu_props = None       # type: ContainedIPduProps

    @property
    def containedIPduProps(self) -> ContainedIPduProps:
        return self._contained_ipdu_props

    @containedIPduProps.setter
    def containedIPduProps(self, value: ContainedIPduProps):
        self._contained_ipdu_props = value


class NmPdu(Pdu):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
    

class NPdu(IPdu):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class DcmIPdu(IPdu):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class FrameTriggering(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == FrameTriggering:
            raise NotImplementedError("FrameTriggering is an abstract class.")
        
        super().__init__(parent, short_name)

class ISignal(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._data_transformation_ref = None
        self._data_type_policy = None
        self._i_signal_props = None
        self._i_signal_type = None
        self._init_value = None
        self._length = None
        self._network_representation_props = None
        self._system_signal_ref = None                  # type: RefType
        self._timeout_substitution_value = None
        self._transformation_i_signal_props = []

    @property
    def dataTransformationRef(self):
        return self._data_transformation_ref

    @dataTransformationRef.setter
    def dataTransformationRef(self, value):
        self._data_transformation_ref = value

    @property
    def dataTypePolicy(self):
        return self._data_type_policy

    @dataTypePolicy.setter
    def dataTypePolicy(self, value):
        self._data_type_policy = value

    @property
    def iSignalProps(self):
        return self._i_signal_props

    @iSignalProps.setter
    def iSignalProps(self, value):
        self._i_signal_props = value

    @property
    def iSignalType(self):
        return self._i_signal_type

    @iSignalType.setter
    def iSignalType(self, value):
        self._i_signal_type = value

    @property
    def initValue(self):
        return self._init_value

    @initValue.setter
    def initValue(self, value):
        self._init_value = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def networkRepresentationProps(self):
        return self._network_representation_props

    @networkRepresentationProps.setter
    def networkRepresentationProps(self, value):
        self._network_representation_props = value

    @property
    def systemSignalRef(self):
        return self._system_signal_ref

    @systemSignalRef.setter
    def systemSignalRef(self, value):
        self._system_signal_ref = value

    @property
    def timeoutSubstitutionValue(self):
        return self._timeout_substitution_value

    @timeoutSubstitutionValue.setter
    def timeoutSubstitutionValue(self, value):
        self._timeout_substitution_value = value

    @property
    def transformationISignalProps(self):
        return self._transformation_i_signal_props

    @transformationISignalProps.setter
    def transformationISignalProps(self, value):
        self._transformation_i_signal_props = value
