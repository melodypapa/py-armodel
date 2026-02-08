from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class NmPdu(Pdu):
    """
    Network Management Pdu

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::NmPdu

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 302, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 342, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This optional aggregation is used to describe NmUser that is transmitted in
                # the NmPdu.
        # The counting of starts at the beginning of the NmPdu Cbv or Nid are used.
        self._iSignalToIPdu: List[RefType] = []

    @property
    def i_signal_to_i_pdu(self) -> List[RefType]:
        """Get iSignalToIPdu (Pythonic accessor)."""
        return self._iSignalToIPdu
        # Defines if the Pdu contains NM Data.
        # If the NmPdu does aggregate any ISignalToIPduMappings it still may that is
                # set via Nm_SetUserData().
        # If the then the nmDataInformation be ignored.
        self._nmData: Optional["Boolean"] = None

    @property
    def nm_data(self) -> Optional["Boolean"]:
        """Get nmData (Pythonic accessor)."""
        return self._nmData

    @nm_data.setter
    def nm_data(self, value: Optional["Boolean"]) -> None:
        """
        Set nmData with validation.

        Args:
            value: The nmData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmData = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmData must be Boolean or None, got {type(value).__name__}"
            )
        self._nmData = value
        # Defines if the Pdu contains NM Vote information.
        self._nmVoteInformation: Optional["Boolean"] = None

    @property
    def nm_vote_information(self) -> Optional["Boolean"]:
        """Get nmVoteInformation (Pythonic accessor)."""
        return self._nmVoteInformation

    @nm_vote_information.setter
    def nm_vote_information(self, value: Optional["Boolean"]) -> None:
        """
        Set nmVoteInformation with validation.

        Args:
            value: The nmVoteInformation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmVoteInformation = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmVoteInformation must be Boolean or None, got {type(value).__name__}"
            )
        self._nmVoteInformation = value
        # AUTOSAR COM is filling not used areas of an Pdu with bit-pattern.
        # This attribute can only be used if the nm is set to true.
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

    def getISignalToIPdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for iSignalToIPdu.

        Returns:
            The iSignalToIPdu value

        Note:
            Delegates to i_signal_to_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_to_i_pdu  # Delegates to property

    def getNmData(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmData.

        Returns:
            The nmData value

        Note:
            Delegates to nm_data property (CODING_RULE_V2_00017)
        """
        return self.nm_data  # Delegates to property

    def setNmData(self, value: "Boolean") -> "NmPdu":
        """
        AUTOSAR-compliant setter for nmData with method chaining.

        Args:
            value: The nmData to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_data property setter (gets validation automatically)
        """
        self.nm_data = value  # Delegates to property setter
        return self

    def getNmVoteInformation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmVoteInformation.

        Returns:
            The nmVoteInformation value

        Note:
            Delegates to nm_vote_information property (CODING_RULE_V2_00017)
        """
        return self.nm_vote_information  # Delegates to property

    def setNmVoteInformation(self, value: "Boolean") -> "NmPdu":
        """
        AUTOSAR-compliant setter for nmVoteInformation with method chaining.

        Args:
            value: The nmVoteInformation to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_vote_information property setter (gets validation automatically)
        """
        self.nm_vote_information = value  # Delegates to property setter
        return self

    def getUnusedBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for unusedBit.

        Returns:
            The unusedBit value

        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "Integer") -> "NmPdu":
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

    def with_nm_data(self, value: Optional["Boolean"]) -> "NmPdu":
        """
        Set nmData and return self for chaining.

        Args:
            value: The nmData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_data("value")
        """
        self.nm_data = value  # Use property setter (gets validation)
        return self

    def with_nm_vote_information(self, value: Optional["Boolean"]) -> "NmPdu":
        """
        Set nmVoteInformation and return self for chaining.

        Args:
            value: The nmVoteInformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_vote_information("value")
        """
        self.nm_vote_information = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["Integer"]) -> "NmPdu":
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
