from __future__ import annotations
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class DdsCpISignalToDdsTopicMapping(ARObject):
    """
    Mapping of an ISignal to a DdsTopic. Tags: atp.Status=candidate
    """

    # DdsCpISignalToDdsTopicMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.53, p.293 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDdsTopicRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsTopicRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getISignalRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setISignalRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the DdsTopic. Tags: atp.Status=candidate
        self.ddsTopicRef: Optional[RefType] = None

        # Reference to the ISignal. Tags: atp.Status=candidate
        self.iSignalRef: Optional[RefType] = None

    def getDdsTopicRef(self) -> Optional[RefType]:
        """
        Reference to the DdsTopic. Tags: atp.Status=candidate
        """
        return self.ddsTopicRef

    def setDdsTopicRef(self, value: Optional[RefType]) -> DdsCpISignalToDdsTopicMapping:
        """
        Reference to the DdsTopic. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing ddsTopicRef.
        """
        if value is not None:
            self.ddsTopicRef = value
        return self

    def getISignalRef(self) -> Optional[RefType]:
        """
        Reference to the ISignal. Tags: atp.Status=candidate
        """
        return self.iSignalRef

    def setISignalRef(self, value: Optional[RefType]) -> DdsCpISignalToDdsTopicMapping:
        """
        Reference to the ISignal. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing iSignalRef.
        """
        if value is not None:
            self.iSignalRef = value
        return self
