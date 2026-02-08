from abc import ABC
from typing import Optional


class DiagnosticMapping(DiagnosticCommonElement, ABC):
    """
    Abstract element for different kinds of diagnostic mappings.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 223, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticMapping:
            raise TypeError("DiagnosticMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference can be used in an early design phase to an element of a
        # diagnostic extract with an CPSoftwareCluster.
        self._provider: Optional["CpSoftwareCluster"] = None

    @property
    def provider(self) -> Optional["CpSoftwareCluster"]:
        """Get provider (Pythonic accessor)."""
        return self._provider

    @provider.setter
    def provider(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set provider with validation.

        Args:
            value: The provider to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provider = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"provider must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._provider = value
        # This reference can be used in an early design phase to an element of a
        # diagnostic extract with an CPSoftwareCluster.
        self._requester: Optional["CpSoftwareCluster"] = None

    @property
    def requester(self) -> Optional["CpSoftwareCluster"]:
        """Get requester (Pythonic accessor)."""
        return self._requester

    @requester.setter
    def requester(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set requester with validation.

        Args:
            value: The requester to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requester = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"requester must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._requester = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvider(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for provider.

        Returns:
            The provider value

        Note:
            Delegates to provider property (CODING_RULE_V2_00017)
        """
        return self.provider  # Delegates to property

    def setProvider(self, value: "CpSoftwareCluster") -> "DiagnosticMapping":
        """
        AUTOSAR-compliant setter for provider with method chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Note:
            Delegates to provider property setter (gets validation automatically)
        """
        self.provider = value  # Delegates to property setter
        return self

    def getRequester(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for requester.

        Returns:
            The requester value

        Note:
            Delegates to requester property (CODING_RULE_V2_00017)
        """
        return self.requester  # Delegates to property

    def setRequester(self, value: "CpSoftwareCluster") -> "DiagnosticMapping":
        """
        AUTOSAR-compliant setter for requester with method chaining.

        Args:
            value: The requester to set

        Returns:
            self for method chaining

        Note:
            Delegates to requester property setter (gets validation automatically)
        """
        self.requester = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provider(self, value: Optional["CpSoftwareCluster"]) -> "DiagnosticMapping":
        """
        Set provider and return self for chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provider("value")
        """
        self.provider = value  # Use property setter (gets validation)
        return self

    def with_requester(self, value: Optional["CpSoftwareCluster"]) -> "DiagnosticMapping":
        """
        Set requester and return self for chaining.

        Args:
            value: The requester to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requester("value")
        """
        self.requester = value  # Use property setter (gets validation)
        return self
