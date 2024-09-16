from typing import List

from ..ar_ref import RefType
from ..ar_object import ARObject, ARPositiveInteger
from .fibex_core import FibexElement

class FrameMapping(ARObject):
    def __init__(self):
        super().__init__()

        self._introduction = None             # type: DocumentationBlock
        self._source_frame_ref = None         # type: RefType
        self._target_frame_ref = None         # type: RefType

    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value

    @property
    def sourceFrameRef(self):
        return self._source_frame_ref

    @sourceFrameRef.setter
    def sourceFrameRef(self, value):
        self._source_frame_ref = value

    @property
    def targetFrameRef(self):
        return self._target_frame_ref

    @targetFrameRef.setter
    def targetFrameRef(self, value):
        self._target_frame_ref = value

class ISignalMapping(ARObject):
    def __init__(self):
        super().__init__()

        self._introduction = None           # type: DocumentationBlock
        self._source_signal_ref = None      # type: RefType
        self._target_signal_ref = None      # type: RefType

    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value

    @property
    def sourceSignalRef(self):
        return self._source_signal_ref

    @sourceSignalRef.setter
    def sourceSignalRef(self, value):
        self._source_signal_ref = value

    @property
    def targetSignalRef(self):
        return self._target_signal_ref

    @targetSignalRef.setter
    def targetSignalRef(self, value):
        self._target_signal_ref = value

class IPduMapping(ARObject):
    def __init__(self):
        super().__init__()

        self._introduction = None           # type: DocumentationBlock
        self._pdur_tp_chunk_size = None     # type: ARPositiveInteger
        self._source_ipdu_ref = None        # type: RefType
        self._target_ipdu_ref = None        # type: RefType

    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value

    @property
    def pdurTpChunkSize(self):
        return self._pdur_tp_chunk_size

    @pdurTpChunkSize.setter
    def pdurTpChunkSize(self, value):
        self._pdur_tp_chunk_size = value

    @property
    def sourceIPduRef(self):
        return self._source_ipdu_ref

    @sourceIPduRef.setter
    def sourceIPduRef(self, value):
        self._source_ipdu_ref = value

    @property
    def targetIPduRef(self):
        return self._target_ipdu_ref

    @targetIPduRef.setter
    def targetIPduRef(self, value):
        self._target_ipdu_ref = value

class Gateway(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._ecu_ref = None                # type: RefType
        self._frame_mappings = []           # type: List[FrameMapping]
        self._i_pdu_mappings = []           # type: List[IPduMapping]
        self._signal_mappings = []          # type: List[ISignalMapping]

    @property
    def ecuRef(self) -> RefType:
        return self._ecu_ref

    @ecuRef.setter
    def ecuRef(self, value: RefType):
        self._ecu_ref = value

    def getFrameMappings(self) -> List[FrameMapping]:
        return self._frame_mappings

    def addFrameMapping(self, mapping: FrameMapping):
        self._frame_mappings.append(mapping)

    def getIPduMappings(self) -> List[FrameMapping]:
        return self._i_pdu_mappings

    def addIPduMappings(self, mapping: FrameMapping):
        self._i_pdu_mappings.append(mapping)

    def getSignalMappings(self) -> List[FrameMapping]:
        return self._signal_mappings

    def addSignalMapping(self, mapping: FrameMapping):
        self._signal_mappings.append(mapping)
