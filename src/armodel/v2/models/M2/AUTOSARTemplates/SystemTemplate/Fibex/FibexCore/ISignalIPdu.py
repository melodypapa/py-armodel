from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import IPdu

    RefType,
)


class ISignalIPdu(IPdu):
    """
    Represents the IPdus handled by Com. The ISignalIPdu assembled and
    disassembled in AUTOSAR COM consists of one or more signals. In case no
    multiplexing is performed this IPdu is routed to/from the Interface Layer. A
    maximum of one dynamic length signal per IPdu is allowed.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalIPdu

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 994, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 342, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Timing specification for Com IPdus (Transmission This information is
                # mandatory for the sender in a This information may be omitted on a System
                # Extract.
        # timing of a Pdu can vary.
        # atpVariation 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate
                # Template R23-11.
        self._iPduTiming: Optional["IPduTiming"] = None

    @property
    def i_pdu_timing(self) -> Optional["IPduTiming"]:
        """Get iPduTiming (Pythonic accessor)."""
        return self._iPduTiming

    @i_pdu_timing.setter
    def i_pdu_timing(self, value: Optional["IPduTiming"]) -> None:
        """
        Set iPduTiming with validation.

        Args:
            value: The iPduTiming to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPduTiming = None
            return

        if not isinstance(value, IPduTiming):
            raise TypeError(
                f"iPduTiming must be IPduTiming or None, got {type(value).__name__}"
            )
        self._iPduTiming = value
        # Definition of SignalToIPduMappings included in the Signal content of a PDU
                # can be variable.
        # atpVariation.
        self._iSignalToPdu: List[RefType] = []

    @property
    def i_signal_to_pdu(self) -> List[RefType]:
        """Get iSignalToPdu (Pythonic accessor)."""
        return self._iSignalToPdu
        # AUTOSAR COM and AUTOSAR IPDUM are filling not areas of an IPDU with this
                # bit-pattern.
        # This attribute to avoid undefined behavior.
        # This be repeated throughout the IPdu.
        self._unusedBit: Optional["Integer"] = None

    @property
    def unused_bit(self) -> Optional["Integer"]:
        """Get unusedBit (Pythonic accessor)."""
        return self._unusedBit

    @unused_bit.setter
    def unused_bit(self, value: Optional["Integer"]) -> None:
        """
        Set unusedBit with validation.

        Args:
            value: The unusedBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unusedBit = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"unusedBit must be Integer or None, got {type(value).__name__}"
            )
        self._unusedBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduTiming(self) -> "IPduTiming":
        """
        AUTOSAR-compliant getter for iPduTiming.

        Returns:
            The iPduTiming value

        Note:
            Delegates to i_pdu_timing property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_timing  # Delegates to property

    def setIPduTiming(self, value: "IPduTiming") -> "ISignalIPdu":
        """
        AUTOSAR-compliant setter for iPduTiming with method chaining.

        Args:
            value: The iPduTiming to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_pdu_timing property setter (gets validation automatically)
        """
        self.i_pdu_timing = value  # Delegates to property setter
        return self

    def getISignalToPdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for iSignalToPdu.

        Returns:
            The iSignalToPdu value

        Note:
            Delegates to i_signal_to_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_to_pdu  # Delegates to property

    def getUnusedBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for unusedBit.

        Returns:
            The unusedBit value

        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "Integer") -> "ISignalIPdu":
        """
        AUTOSAR-compliant setter for unusedBit with method chaining.

        Args:
            value: The unusedBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to unused_bit property setter (gets validation automatically)
        """
        self.unused_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu_timing(self, value: Optional["IPduTiming"]) -> "ISignalIPdu":
        """
        Set iPduTiming and return self for chaining.

        Args:
            value: The iPduTiming to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu_timing("value")
        """
        self.i_pdu_timing = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["Integer"]) -> "ISignalIPdu":
        """
        Set unusedBit and return self for chaining.

        Args:
            value: The unusedBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unused_bit("value")
        """
        self.unused_bit = value  # Use property setter (gets validation)
        return self
