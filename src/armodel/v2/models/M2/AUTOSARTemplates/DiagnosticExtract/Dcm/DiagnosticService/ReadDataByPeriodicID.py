"""
AUTOSAR Package - ReadDataByPeriodicID

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    PositiveInteger,
)


class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):
    """
    This represents an instance of the "Read Data by periodic Identifier"
    diagnostic service. (cid:53) 129 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID::DiagnosticReadDataByPeriodicID

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 129, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticReadDataBy the
                # given context.
        self._readDataClass: Optional["DiagnosticReadDataBy"] = None

    @property
    def read_data_class(self) -> Optional["DiagnosticReadDataBy"]:
        """Get readDataClass (Pythonic accessor)."""
        return self._readDataClass

    @read_data_class.setter
    def read_data_class(self, value: Optional["DiagnosticReadDataBy"]) -> None:
        """
        Set readDataClass with validation.

        Args:
            value: The readDataClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readDataClass = None
            return

        if not isinstance(value, DiagnosticReadDataBy):
            raise TypeError(
                f"readDataClass must be DiagnosticReadDataBy or None, got {type(value).__name__}"
            )
        self._readDataClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReadDataClass(self) -> "DiagnosticReadDataBy":
        """
        AUTOSAR-compliant getter for readDataClass.

        Returns:
            The readDataClass value

        Note:
            Delegates to read_data_class property (CODING_RULE_V2_00017)
        """
        return self.read_data_class  # Delegates to property

    def setReadDataClass(self, value: "DiagnosticReadDataBy") -> DiagnosticReadDataByPeriodicID:
        """
        AUTOSAR-compliant setter for readDataClass with method chaining.

        Args:
            value: The readDataClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to read_data_class property setter (gets validation automatically)
        """
        self.read_data_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_read_data_class(self, value: Optional["DiagnosticReadDataBy"]) -> DiagnosticReadDataByPeriodicID:
        """
        Set readDataClass and return self for chaining.

        Args:
            value: The readDataClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_read_data_class("value")
        """
        self.read_data_class = value  # Use property setter (gets validation)
        return self



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
        self._maxPeriodicDid: Optional[PositiveInteger] = None

    @property
    def max_periodic_did(self) -> Optional[PositiveInteger]:
        """Get maxPeriodicDid (Pythonic accessor)."""
        return self._maxPeriodicDid

    @max_periodic_did.setter
    def max_periodic_did(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxPeriodicDid must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxPeriodicDid = value
        # can be executed.
        self._periodicRate: List[DiagnosticPeriodicRate] = []

    @property
    def periodic_rate(self) -> List[DiagnosticPeriodicRate]:
        """Get periodicRate (Pythonic accessor)."""
        return self._periodicRate
        # This represents the maximum number of periodic data that can be scheduled in
        # parallel.
        self._schedulerMax: Optional[PositiveInteger] = None

    @property
    def scheduler_max(self) -> Optional[PositiveInteger]:
        """Get schedulerMax (Pythonic accessor)."""
        return self._schedulerMax

    @scheduler_max.setter
    def scheduler_max(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"schedulerMax must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._schedulerMax = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxPeriodicDid(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxPeriodicDid.

        Returns:
            The maxPeriodicDid value

        Note:
            Delegates to max_periodic_did property (CODING_RULE_V2_00017)
        """
        return self.max_periodic_did  # Delegates to property

    def setMaxPeriodicDid(self, value: PositiveInteger) -> DiagnosticReadDataByPeriodicIDClass:
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

    def getPeriodicRate(self) -> List[DiagnosticPeriodicRate]:
        """
        AUTOSAR-compliant getter for periodicRate.

        Returns:
            The periodicRate value

        Note:
            Delegates to periodic_rate property (CODING_RULE_V2_00017)
        """
        return self.periodic_rate  # Delegates to property

    def getSchedulerMax(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for schedulerMax.

        Returns:
            The schedulerMax value

        Note:
            Delegates to scheduler_max property (CODING_RULE_V2_00017)
        """
        return self.scheduler_max  # Delegates to property

    def setSchedulerMax(self, value: PositiveInteger) -> DiagnosticReadDataByPeriodicIDClass:
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

    def with_max_periodic_did(self, value: Optional[PositiveInteger]) -> DiagnosticReadDataByPeriodicIDClass:
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

    def with_scheduler_max(self, value: Optional[PositiveInteger]) -> DiagnosticReadDataByPeriodicIDClass:
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



class DiagnosticPeriodicRate(ARObject):
    """
    This represents the ability to define a periodic rate for the specification
    of the "read data by periodic ID" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID::DiagnosticPeriodicRate

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 131, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the period of the DiagnosticPeriodicRate.
        self._period: Optional["TimeValue"] = None

    @property
    def period(self) -> Optional["TimeValue"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["TimeValue"]) -> None:
        """
        Set period with validation.

        Args:
            value: The period to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"period must be TimeValue or None, got {type(value).__name__}"
            )
        self._period = value
        self._periodicRate: Optional[DiagnosticPeriodicRate] = None

    @property
    def periodic_rate(self) -> Optional[DiagnosticPeriodicRate]:
        """Get periodicRate (Pythonic accessor)."""
        return self._periodicRate

    @periodic_rate.setter
    def periodic_rate(self, value: Optional[DiagnosticPeriodicRate]) -> None:
        """
        Set periodicRate with validation.

        Args:
            value: The periodicRate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._periodicRate = None
            return

        if not isinstance(value, DiagnosticPeriodicRate):
            raise TypeError(
                f"periodicRate must be DiagnosticPeriodicRate or None, got {type(value).__name__}"
            )
        self._periodicRate = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "TimeValue") -> DiagnosticPeriodicRate:
        """
        AUTOSAR-compliant setter for period with method chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    def getPeriodicRate(self) -> DiagnosticPeriodicRate:
        """
        AUTOSAR-compliant getter for periodicRate.

        Returns:
            The periodicRate value

        Note:
            Delegates to periodic_rate property (CODING_RULE_V2_00017)
        """
        return self.periodic_rate  # Delegates to property

    def setPeriodicRate(self, value: DiagnosticPeriodicRate) -> DiagnosticPeriodicRate:
        """
        AUTOSAR-compliant setter for periodicRate with method chaining.

        Args:
            value: The periodicRate to set

        Returns:
            self for method chaining

        Note:
            Delegates to periodic_rate property setter (gets validation automatically)
        """
        self.periodic_rate = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_period(self, value: Optional["TimeValue"]) -> DiagnosticPeriodicRate:
        """
        Set period and return self for chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self

    def with_periodic_rate(self, value: Optional[DiagnosticPeriodicRate]) -> DiagnosticPeriodicRate:
        """
        Set periodicRate and return self for chaining.

        Args:
            value: The periodicRate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_periodic_rate("value")
        """
        self.periodic_rate = value  # Use property setter (gets validation)
        return self


class DiagnosticPeriodicRateCategoryEnum(AREnum):
    """
    DiagnosticPeriodicRateCategoryEnum enumeration

This meta-class provides possible values for the setting of the periodic rate. Aggregated by DiagnosticPeriodicRate.periodicRateCategory

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID
    """
    # This value represents a fast periodic rate.
    periodicRateFast = "0"

    # This value represents a medium periodic rate.
    periodicRateMedium = "1"

    # This value represents a slow periodic rate.
    periodicRateSlow = "2"
