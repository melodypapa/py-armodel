from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Frame,
    FramePort,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class FrameTriggering(Identifiable, ABC):
    """
    The FrameTriggering describes the instance of a frame sent on a channel and
    defines the manner of triggering (timing information) and identification of
    a frame on the channel, on which it is sent. For the same frame, if
    FrameTriggerings exist on more than one channel of the same cluster the
    fan-out/ in is handled by the Bus interface.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::FrameTriggering

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 295, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 418, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 224, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is FrameTriggering:
            raise TypeError("FrameTriggering is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # One frame can be triggered several times, e.
        # g.
        # on If a frame has no frame triggering, it sent at all.
        # A frame triggering has assigned frame, which it triggers.
        self._frame: Optional["Frame"] = None

    @property
    def frame(self) -> Optional["Frame"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["Frame"]) -> None:
        """
        Set frame with validation.

        Args:
            value: The frame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, Frame):
            raise TypeError(
                f"frame must be Frame or None, got {type(value).__name__}"
            )
        self._frame = value
        # References to the FramePort on every ECU of the system and/or receives the
                # frame.
        # both the sender and the receiver side included when the system is completely
                # defined.
        self._framePort: List["FramePort"] = []

    @property
    def frame_port(self) -> List["FramePort"]:
        """Get framePort (Pythonic accessor)."""
        return self._framePort
        # This reference provides the relationship to the Pdu are implemented by the
                # FrameTriggering.
        # is optional since no PduTriggering can be NmPdus and XCP Pdus.
        # atpVariation.
        self._pduTriggering: List[RefType] = []

    @property
    def pdu_triggering(self) -> List[RefType]:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrame(self) -> "Frame":
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "Frame") -> "FrameTriggering":
        """
        AUTOSAR-compliant setter for frame with method chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
        return self

    def getFramePort(self) -> List["FramePort"]:
        """
        AUTOSAR-compliant getter for framePort.

        Returns:
            The framePort value

        Note:
            Delegates to frame_port property (CODING_RULE_V2_00017)
        """
        return self.frame_port  # Delegates to property

    def getPduTriggering(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pduTriggering.

        Returns:
            The pduTriggering value

        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional["Frame"]) -> "FrameTriggering":
        """
        Set frame and return self for chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self
