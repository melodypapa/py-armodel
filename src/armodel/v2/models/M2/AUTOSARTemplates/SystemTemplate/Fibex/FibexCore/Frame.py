from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

    RefType,
)


class Frame(FibexElement, ABC):
    """
    Data frame which is sent over a communication medium. This element describes
    the pure Layout of a frame sent on a channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 295, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 418, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 224, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is Frame:
            raise TypeError("Frame is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The used length (in bytes) of the referencing frame.
        # be confused with a static byte length reserved frame by some platforms (e.
        # g.
        # FlexRay).
        # of zero bytes is allowed.
        # also TPS_SYST_02255.
        self._frameLength: Optional["Integer"] = None

    @property
    def frame_length(self) -> Optional["Integer"]:
        """Get frameLength (Pythonic accessor)."""
        return self._frameLength

    @frame_length.setter
    def frame_length(self, value: Optional["Integer"]) -> None:
        """
        Set frameLength with validation.

        Args:
            value: The frameLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frameLength = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"frameLength must be Integer or None, got {type(value).__name__}"
            )
        self._frameLength = value
        # A frames layout as a sequence of Pdus.
        # The content of a frame can be variable.
        # atpVariation.
        self._pduToFrame: List[RefType] = []

    @property
    def pdu_to_frame(self) -> List[RefType]:
        """Get pduToFrame (Pythonic accessor)."""
        return self._pduToFrame

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrameLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for frameLength.

        Returns:
            The frameLength value

        Note:
            Delegates to frame_length property (CODING_RULE_V2_00017)
        """
        return self.frame_length  # Delegates to property

    def setFrameLength(self, value: "Integer") -> "Frame":
        """
        AUTOSAR-compliant setter for frameLength with method chaining.

        Args:
            value: The frameLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_length property setter (gets validation automatically)
        """
        self.frame_length = value  # Delegates to property setter
        return self

    def getPduToFrame(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pduToFrame.

        Returns:
            The pduToFrame value

        Note:
            Delegates to pdu_to_frame property (CODING_RULE_V2_00017)
        """
        return self.pdu_to_frame  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame_length(self, value: Optional["Integer"]) -> "Frame":
        """
        Set frameLength and return self for chaining.

        Args:
            value: The frameLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_length("value")
        """
        self.frame_length = value  # Use property setter (gets validation)
        return self
