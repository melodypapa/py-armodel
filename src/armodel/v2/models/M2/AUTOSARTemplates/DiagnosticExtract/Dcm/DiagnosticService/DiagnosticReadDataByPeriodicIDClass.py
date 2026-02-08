from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import DiagnosticServiceClass


class DiagnosticReadDataByPeriodicIDClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Read
    Data by periodic Identifier" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID::DiagnosticReadDataByPeriodicIDClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 130, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the maximum number of data identifiers can be included in one
        # request.
        self._maxPeriodicDid: Optional["PositiveInteger"] = None

    @property
    def max_periodic_did(self) -> Optional["PositiveInteger"]:
        """Get maxPeriodicDid (Pythonic accessor)."""
        return self._maxPeriodicDid

    @max_periodic_did.setter
    def max_periodic_did(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxPeriodicDid with validation.

        Args:
            value: The maxPeriodicDid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxPeriodicDid = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxPeriodicDid must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxPeriodicDid = value
        # This represents the description of a collection of periodic which the service
        # can be executed.
        self._periodicRate: List["DiagnosticPeriodicRate"] = []

    @property
    def periodic_rate(self) -> List["DiagnosticPeriodicRate"]:
        """Get periodicRate (Pythonic accessor)."""
        return self._periodicRate
        # This represents the maximum number of periodic data that can be scheduled in
        # parallel.
        self._schedulerMax: Optional["PositiveInteger"] = None

    @property
    def scheduler_max(self) -> Optional["PositiveInteger"]:
        """Get schedulerMax (Pythonic accessor)."""
        return self._schedulerMax

    @scheduler_max.setter
    def scheduler_max(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set schedulerMax with validation.

        Args:
            value: The schedulerMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._schedulerMax = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"schedulerMax must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._schedulerMax = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxPeriodicDid(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxPeriodicDid.

        Returns:
            The maxPeriodicDid value

        Note:
            Delegates to max_periodic_did property (CODING_RULE_V2_00017)
        """
        return self.max_periodic_did  # Delegates to property

    def setMaxPeriodicDid(self, value: "PositiveInteger") -> "DiagnosticReadDataByPeriodicIDClass":
        """
        AUTOSAR-compliant setter for maxPeriodicDid with method chaining.

        Args:
            value: The maxPeriodicDid to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_periodic_did property setter (gets validation automatically)
        """
        self.max_periodic_did = value  # Delegates to property setter
        return self

    def getPeriodicRate(self) -> List["DiagnosticPeriodicRate"]:
        """
        AUTOSAR-compliant getter for periodicRate.

        Returns:
            The periodicRate value

        Note:
            Delegates to periodic_rate property (CODING_RULE_V2_00017)
        """
        return self.periodic_rate  # Delegates to property

    def getSchedulerMax(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for schedulerMax.

        Returns:
            The schedulerMax value

        Note:
            Delegates to scheduler_max property (CODING_RULE_V2_00017)
        """
        return self.scheduler_max  # Delegates to property

    def setSchedulerMax(self, value: "PositiveInteger") -> "DiagnosticReadDataByPeriodicIDClass":
        """
        AUTOSAR-compliant setter for schedulerMax with method chaining.

        Args:
            value: The schedulerMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to scheduler_max property setter (gets validation automatically)
        """
        self.scheduler_max = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_periodic_did(self, value: Optional["PositiveInteger"]) -> "DiagnosticReadDataByPeriodicIDClass":
        """
        Set maxPeriodicDid and return self for chaining.

        Args:
            value: The maxPeriodicDid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_periodic_did("value")
        """
        self.max_periodic_did = value  # Use property setter (gets validation)
        return self

    def with_scheduler_max(self, value: Optional["PositiveInteger"]) -> "DiagnosticReadDataByPeriodicIDClass":
        """
        Set schedulerMax and return self for chaining.

        Args:
            value: The schedulerMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scheduler_max("value")
        """
        self.scheduler_max = value  # Use property setter (gets validation)
        return self
