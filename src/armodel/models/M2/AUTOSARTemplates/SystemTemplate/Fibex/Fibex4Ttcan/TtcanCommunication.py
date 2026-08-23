# This module contains AUTOSAR System Template classes for TTCAN communication
# It defines TTCAN-specific absolutely scheduled timing elements

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCycle


class TtcanTriggerType(AREnum):
    """
    This type lists all trigger types for a time window.
    """

    # TtcanTriggerType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.116, p.450
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods)

    ENUM_RX_TRIGGER = "RX-TRIGGER"
    ENUM_TX_REF_TRIGGER = "TX-REF-TRIGGER"
    ENUM_TX_REF_TRIGGER_GAP = "TX-REF-TRIGGER-GAP"
    ENUM_TX_TRIGGER_MERGED = "TX-TRIGGER-MERGED"
    ENUM_TX_TRIGGER_SINGLE = "TX-TRIGGER-SINGLE"
    ENUM_WATCH_TRIGGER = "WATCH-TRIGGER"
    ENUM_WATCH_TRIGGER_GAP = "WATCH-TRIGGER-GAP"

    def __init__(self):
        super().__init__(
            [
                TtcanTriggerType.ENUM_RX_TRIGGER,
                TtcanTriggerType.ENUM_TX_REF_TRIGGER,
                TtcanTriggerType.ENUM_TX_REF_TRIGGER_GAP,
                TtcanTriggerType.ENUM_TX_TRIGGER_MERGED,
                TtcanTriggerType.ENUM_TX_TRIGGER_SINGLE,
                TtcanTriggerType.ENUM_WATCH_TRIGGER,
                TtcanTriggerType.ENUM_WATCH_TRIGGER_GAP,
            ]
        )


class TtcanAbsolutelyScheduledTiming(ARObject):
    """
    Each frame in TTCAN is identified by its slot id and communication cycle. A description is provided by the usage of AbsolutelyScheduledTiming. A frame can be sent multiple times within one communication cycle. For describing this case multiple AbsolutelyScheduledTimings have to be used. The main use case would be that a frame is sent twice within one communication cycle.
    """

    # TtcanAbsolutelyScheduledTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.115, p.450
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCommunicationCycle           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setCommunicationCycle           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeMark                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeMark                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTrigger                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTrigger                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The communication cycle where the frame is sent.
        self.communicationCycle: Optional[CommunicationCycle] = None

        # Where FlexRay counts the slots in the static segment, TTCAN requires explicit Tx and Rx time marks.
        self.timeMark: Optional[Integer] = None

        # Trigger type for this time window.
        self.trigger: Optional[TtcanTriggerType] = None

    def getCommunicationCycle(self) -> Optional[CommunicationCycle]:
        """
        The communication cycle where the frame is sent.
        """
        return self.communicationCycle

    def setCommunicationCycle(self, value: Optional[CommunicationCycle]) -> "TtcanAbsolutelyScheduledTiming":
        """
        The communication cycle where the frame is sent.
        A None value is a no-op and does not overwrite an existing communicationCycle.
        """
        if value is not None:
            self.communicationCycle = value
        return self

    def getTimeMark(self) -> Optional[Integer]:
        """
        Where FlexRay counts the slots in the static segment, TTCAN requires explicit Tx and Rx time marks.
        """
        return self.timeMark

    def setTimeMark(self, value: Optional[Integer]) -> "TtcanAbsolutelyScheduledTiming":
        """
        Where FlexRay counts the slots in the static segment, TTCAN requires explicit Tx and Rx time marks.
        A None value is a no-op and does not overwrite an existing timeMark.
        """
        if value is not None:
            self.timeMark = value
        return self

    def getTrigger(self) -> Optional[TtcanTriggerType]:
        """
        Trigger type for this time window.
        """
        return self.trigger

    def setTrigger(self, value: Optional[TtcanTriggerType]) -> "TtcanAbsolutelyScheduledTiming":
        """
        Trigger type for this time window.
        A None value is a no-op and does not overwrite an existing trigger.
        """
        if value is not None:
            self.trigger = value
        return self
