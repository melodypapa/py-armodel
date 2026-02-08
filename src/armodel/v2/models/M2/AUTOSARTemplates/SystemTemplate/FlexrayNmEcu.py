from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    BusspecificNmEcu,
)


class FlexrayNmEcu(BusspecificNmEcu):
    """
    FlexRay specific attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 679, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Switch for enabling the processing of FlexRay Hardware NM-Votes.
        self._nmHwVote: Optional["Boolean"] = None

    @property
    def nm_hw_vote(self) -> Optional["Boolean"]:
        """Get nmHwVote (Pythonic accessor)."""
        return self._nmHwVote

    @nm_hw_vote.setter
    def nm_hw_vote(self, value: Optional["Boolean"]) -> None:
        """
        Set nmHwVote with validation.

        Args:
            value: The nmHwVote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmHwVote = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmHwVote must be Boolean or None, got {type(value).__name__}"
            )
        self._nmHwVote = value
        # Parameter describing if the execution of the FrNm_Main crosses theFlexRay
        # cycle boundary or not.
        self._nmMain: Optional["Boolean"] = None

    @property
    def nm_main(self) -> Optional["Boolean"]:
        """Get nmMain (Pythonic accessor)."""
        return self._nmMain

    @nm_main.setter
    def nm_main(self, value: Optional["Boolean"]) -> None:
        """
        Set nmMain with validation.

        Args:
            value: The nmMain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMain = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmMain must be Boolean or None, got {type(value).__name__}"
            )
        self._nmMain = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmHwVote(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmHwVote.

        Returns:
            The nmHwVote value

        Note:
            Delegates to nm_hw_vote property (CODING_RULE_V2_00017)
        """
        return self.nm_hw_vote  # Delegates to property

    def setNmHwVote(self, value: "Boolean") -> "FlexrayNmEcu":
        """
        AUTOSAR-compliant setter for nmHwVote with method chaining.

        Args:
            value: The nmHwVote to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_hw_vote property setter (gets validation automatically)
        """
        self.nm_hw_vote = value  # Delegates to property setter
        return self

    def getNmMain(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmMain.

        Returns:
            The nmMain value

        Note:
            Delegates to nm_main property (CODING_RULE_V2_00017)
        """
        return self.nm_main  # Delegates to property

    def setNmMain(self, value: "Boolean") -> "FlexrayNmEcu":
        """
        AUTOSAR-compliant setter for nmMain with method chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_main property setter (gets validation automatically)
        """
        self.nm_main = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_hw_vote(self, value: Optional["Boolean"]) -> "FlexrayNmEcu":
        """
        Set nmHwVote and return self for chaining.

        Args:
            value: The nmHwVote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_hw_vote("value")
        """
        self.nm_hw_vote = value  # Use property setter (gets validation)
        return self

    def with_nm_main(self, value: Optional["Boolean"]) -> "FlexrayNmEcu":
        """
        Set nmMain and return self for chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_main("value")
        """
        self.nm_main = value  # Use property setter (gets validation)
        return self
