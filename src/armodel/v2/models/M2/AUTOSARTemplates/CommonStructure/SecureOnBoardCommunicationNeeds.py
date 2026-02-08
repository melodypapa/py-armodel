from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds


class SecureOnBoardCommunicationNeeds(ServiceNeeds):
    """
    Specifies the need for the existence of the SecOc module on the respective
    ECU. This class currently contains no attributes. An instance of this class
    is used to find out which ports of a software-component deal with the
    administration of secure communication in order to group the request and
    response ports.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::SecureOnBoardCommunicationNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 824, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute provides the ability to control the mode in which the
        # application software is notified about the result authentication attempts.
        self._verification: Optional["VerificationStatus"] = None

    @property
    def verification(self) -> Optional["VerificationStatus"]:
        """Get verification (Pythonic accessor)."""
        return self._verification

    @verification.setter
    def verification(self, value: Optional["VerificationStatus"]) -> None:
        """
        Set verification with validation.

        Args:
            value: The verification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._verification = None
            return

        if not isinstance(value, VerificationStatus):
            raise TypeError(
                f"verification must be VerificationStatus or None, got {type(value).__name__}"
            )
        self._verification = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVerification(self) -> "VerificationStatus":
        """
        AUTOSAR-compliant getter for verification.

        Returns:
            The verification value

        Note:
            Delegates to verification property (CODING_RULE_V2_00017)
        """
        return self.verification  # Delegates to property

    def setVerification(self, value: "VerificationStatus") -> "SecureOnBoardCommunicationNeeds":
        """
        AUTOSAR-compliant setter for verification with method chaining.

        Args:
            value: The verification to set

        Returns:
            self for method chaining

        Note:
            Delegates to verification property setter (gets validation automatically)
        """
        self.verification = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_verification(self, value: Optional["VerificationStatus"]) -> "SecureOnBoardCommunicationNeeds":
        """
        Set verification and return self for chaining.

        Args:
            value: The verification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_verification("value")
        """
        self.verification = value  # Use property setter (gets validation)
        return self
