"""
AUTOSAR Package - DiagnosticTestResult

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult
"""


from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import (
    DiagnosticEvent,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    PositiveInteger,
)


class DiagnosticTestResult(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define diagnostic test results.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult::DiagnosticTestResult

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 204, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 804, Classic Platform
      R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the diagnostic event that is the diagnostic test
                # result.
        # atpVariation.
        self._diagnosticEvent: Optional[DiagnosticEvent] = None

    @property
    def diagnostic_event(self) -> Optional[DiagnosticEvent]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional[DiagnosticEvent]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        self._monitored: Optional["Diagnostic"] = None  # noqa: F821

    @property
    def monitored(self) -> Optional["Diagnostic"]:  # noqa: F821
        """Get monitored (Pythonic accessor)."""
        return self._monitored

    @monitored.setter
    def monitored(self, value: Optional["Diagnostic"]) -> None:  # noqa: F821
        """
        Set monitored with validation.

        Args:
            value: The monitored to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._monitored = None
            return

        if not isinstance(value, Diagnostic):  # noqa: F821
            raise TypeError(
                f"monitored must be Diagnostic or None, got {type(value).__name__}"
            )
        self._monitored = value
        self._testIdentifier: Optional["DiagnosticTestIdentifier"] = None

    @property
    def test_identifier(self) -> Optional["DiagnosticTestIdentifier"]:
        """Get testIdentifier (Pythonic accessor)."""
        return self._testIdentifier

    @test_identifier.setter
    def test_identifier(self, value: Optional["DiagnosticTestIdentifier"]) -> None:
        """
        Set testIdentifier with validation.

        Args:
            value: The testIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._testIdentifier = None
            return

        if not isinstance(value, DiagnosticTestIdentifier):
            raise TypeError(
                f"testIdentifier must be DiagnosticTestIdentifier or None, got {type(value).__name__}"
            )
        self._testIdentifier = value
        self._updateKind: Optional["DiagnosticTestResult"] = None

    @property
    def update_kind(self) -> Optional["DiagnosticTestResult"]:
        """Get updateKind (Pythonic accessor)."""
        return self._updateKind

    @update_kind.setter
    def update_kind(self, value: Optional["DiagnosticTestResult"]) -> None:
        """
        Set updateKind with validation.

        Args:
            value: The updateKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._updateKind = None
            return

        if not isinstance(value, DiagnosticTestResult):
            raise TypeError(
                f"updateKind must be DiagnosticTestResult or None, got {type(value).__name__}"
            )
        self._updateKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> Optional[DiagnosticEvent]:
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: DiagnosticEvent) -> "DiagnosticTestResult":
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getMonitored(self) -> Optional["Diagnostic"]:  # noqa: F821
        """
        AUTOSAR-compliant getter for monitored.

        Returns:
            The monitored value

        Note:
            Delegates to monitored property (CODING_RULE_V2_00017)
        """
        return self.monitored  # Delegates to property

    def setMonitored(self, value: "Diagnostic") -> "DiagnosticTestResult":  # noqa: F821
        """
        AUTOSAR-compliant setter for monitored with method chaining.

        Args:
            value: The monitored to set

        Returns:
            self for method chaining

        Note:
            Delegates to monitored property setter (gets validation automatically)
        """
        self.monitored = value  # Delegates to property setter
        return self

    def getTestIdentifier(self) -> Optional["DiagnosticTestIdentifier"]:
        """
        AUTOSAR-compliant getter for testIdentifier.

        Returns:
            The testIdentifier value

        Note:
            Delegates to test_identifier property (CODING_RULE_V2_00017)
        """
        return self.test_identifier  # Delegates to property

    def setTestIdentifier(self, value: "DiagnosticTestIdentifier") -> "DiagnosticTestResult":
        """
        AUTOSAR-compliant setter for testIdentifier with method chaining.

        Args:
            value: The testIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to test_identifier property setter (gets validation automatically)
        """
        self.test_identifier = value  # Delegates to property setter
        return self

    def getUpdateKind(self) -> Optional["DiagnosticTestResult"]:
        """
        AUTOSAR-compliant getter for updateKind.

        Returns:
            The updateKind value

        Note:
            Delegates to update_kind property (CODING_RULE_V2_00017)
        """
        return self.update_kind  # Delegates to property

    def setUpdateKind(self, value: "DiagnosticTestResult") -> "DiagnosticTestResult":
        """
        AUTOSAR-compliant setter for updateKind with method chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to update_kind property setter (gets validation automatically)
        """
        self.update_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticTestResult":
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_monitored(self, value: Optional["Diagnostic"]) -> "DiagnosticTestResult":  # noqa: F821
        """
        Set monitored and return self for chaining.

        Args:
            value: The monitored to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_monitored("value")
        """
        self.monitored = value  # Use property setter (gets validation)
        return self

    def with_test_identifier(self, value: Optional["DiagnosticTestIdentifier"]) -> "DiagnosticTestResult":
        """
        Set testIdentifier and return self for chaining.

        Args:
            value: The testIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_test_identifier("value")
        """
        self.test_identifier = value  # Use property setter (gets validation)
        return self

    def with_update_kind(self, value: Optional["DiagnosticTestResult"]) -> "DiagnosticTestResult":
        """
        Set updateKind and return self for chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_update_kind("value")
        """
        self.update_kind = value  # Use property setter (gets validation)
        return self



class DiagnosticTestIdentifier(ARObject):
    """
    This meta-class represents the ability to create a diagnostic test
    identifier.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult::DiagnosticTestIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 205, Classic Platform
      R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the numerical id associated with the identifier.
        self._id: Optional[PositiveInteger] = None

    @property
    def id(self) -> Optional[PositiveInteger]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value
        self._uasId: Optional[PositiveInteger] = None

    @property
    def uas_id(self) -> Optional[PositiveInteger]:
        """Get uasId (Pythonic accessor)."""
        return self._uasId

    @uas_id.setter
    def uas_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set uasId with validation.

        Args:
            value: The uasId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._uasId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"uasId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._uasId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: PositiveInteger) -> "DiagnosticTestIdentifier":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getUasId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for uasId.

        Returns:
            The uasId value

        Note:
            Delegates to uas_id property (CODING_RULE_V2_00017)
        """
        return self.uas_id  # Delegates to property

    def setUasId(self, value: PositiveInteger) -> "DiagnosticTestIdentifier":
        """
        AUTOSAR-compliant setter for uasId with method chaining.

        Args:
            value: The uasId to set

        Returns:
            self for method chaining

        Note:
            Delegates to uas_id property setter (gets validation automatically)
        """
        self.uas_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional[PositiveInteger]) -> "DiagnosticTestIdentifier":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_uas_id(self, value: Optional[PositiveInteger]) -> "DiagnosticTestIdentifier":
        """
        Set uasId and return self for chaining.

        Args:
            value: The uasId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uas_id("value")
        """
        self.uas_id = value  # Use property setter (gets validation)
        return self



class DiagnosticMeasurementIdentifier(DiagnosticCommonElement):
    """
    This meta-class represents the ability to describe a measurement identifier.
    (cid:53) 205 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult::DiagnosticMeasurementIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 205, Classic Platform
      R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the numerical measurement Id.
        self._obdMid: Optional[PositiveInteger] = None

    @property
    def obd_mid(self) -> Optional[PositiveInteger]:
        """Get obdMid (Pythonic accessor)."""
        return self._obdMid

    @obd_mid.setter
    def obd_mid(self, value: Optional[PositiveInteger]) -> None:
        """
        Set obdMid with validation.

        Args:
            value: The obdMid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdMid = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"obdMid must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._obdMid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getObdMid(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for obdMid.

        Returns:
            The obdMid value

        Note:
            Delegates to obd_mid property (CODING_RULE_V2_00017)
        """
        return self.obd_mid  # Delegates to property

    def setObdMid(self, value: PositiveInteger) -> "DiagnosticMeasurementIdentifier":
        """
        AUTOSAR-compliant setter for obdMid with method chaining.

        Args:
            value: The obdMid to set

        Returns:
            self for method chaining

        Note:
            Delegates to obd_mid property setter (gets validation automatically)
        """
        self.obd_mid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_obd_mid(self, value: Optional[PositiveInteger]) -> "DiagnosticMeasurementIdentifier":
        """
        Set obdMid and return self for chaining.

        Args:
            value: The obdMid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_obd_mid("value")
        """
        self.obd_mid = value  # Use property setter (gets validation)
        return self


class DiagnosticTestResultUpdateEnum(AREnum):
    """
    DiagnosticTestResultUpdateEnum enumeration

This meta-class represents the ability to define the update behavior of a DiagnosticTestResult. Aggregated by DiagnosticTestResult.updateKind

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult
    """
    # Any DTR result reported by the monitor is used by the Dem.
    always = "0"

    # The Dem accepts reported DTRs only when the configured debouncing mechanism is stable at the FAIL or PASS limit.
    steady = "1"
