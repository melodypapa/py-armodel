from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):
    """
    This element is used to define OBD-relevant DTCs.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 174, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute describes the affection of the event by the PTO handling.
        # event is affected by the Dem PTO handling.
        # event is not affected by the Dem PTO handling.
        self._considerPto: Optional["Boolean"] = None

    @property
    def consider_pto(self) -> Optional["Boolean"]:
        """Get considerPto (Pythonic accessor)."""
        return self._considerPto

    @consider_pto.setter
    def consider_pto(self, value: Optional["Boolean"]) -> None:
        """
        Set considerPto with validation.

        Args:
            value: The considerPto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._considerPto = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"considerPto must be Boolean or None, got {type(value).__name__}"
            )
        self._considerPto = value
        # Defined properties associated with the DemDTC.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._dtcPropsProps: Optional["DiagnosticTroubleCode"] = None

    @property
    def dtc_props_props(self) -> Optional["DiagnosticTroubleCode"]:
        """Get dtcPropsProps (Pythonic accessor)."""
        return self._dtcPropsProps

    @dtc_props_props.setter
    def dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set dtcPropsProps with validation.

        Args:
            value: The dtcPropsProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dtcPropsProps = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"dtcPropsProps must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._dtcPropsProps = value
        # This aggregation allows for the variant definition of the attribute
                # eventObdReadinessGroup.
        # atpVariation.
        self._eventReadiness: Optional["EventObdReadiness"] = None

    @property
    def event_readiness(self) -> Optional["EventObdReadiness"]:
        """Get eventReadiness (Pythonic accessor)."""
        return self._eventReadiness

    @event_readiness.setter
    def event_readiness(self, value: Optional["EventObdReadiness"]) -> None:
        """
        Set eventReadiness with validation.

        Args:
            value: The eventReadiness to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventReadiness = None
            return

        if not isinstance(value, EventObdReadiness):
            raise TypeError(
                f"eventReadiness must be EventObdReadiness or None, got {type(value).__name__}"
            )
        self._eventReadiness = value
        # Unique Diagnostic Trouble Code value for OBD.
        self._obdDTCValue: Optional["PositiveInteger"] = None

    @property
    def obd_dtc_value(self) -> Optional["PositiveInteger"]:
        """Get obdDTCValue (Pythonic accessor)."""
        return self._obdDTCValue

    @obd_dtc_value.setter
    def obd_dtc_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set obdDTCValue with validation.

        Args:
            value: The obdDTCValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdDTCValue = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"obdDTCValue must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._obdDTCValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsiderPto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for considerPto.

        Returns:
            The considerPto value

        Note:
            Delegates to consider_pto property (CODING_RULE_V2_00017)
        """
        return self.consider_pto  # Delegates to property

    def setConsiderPto(self, value: "Boolean") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for considerPto with method chaining.

        Args:
            value: The considerPto to set

        Returns:
            self for method chaining

        Note:
            Delegates to consider_pto property setter (gets validation automatically)
        """
        self.consider_pto = value  # Delegates to property setter
        return self

    def getDtcPropsProps(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for dtcPropsProps.

        Returns:
            The dtcPropsProps value

        Note:
            Delegates to dtc_props_props property (CODING_RULE_V2_00017)
        """
        return self.dtc_props_props  # Delegates to property

    def setDtcPropsProps(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for dtcPropsProps with method chaining.

        Args:
            value: The dtcPropsProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to dtc_props_props property setter (gets validation automatically)
        """
        self.dtc_props_props = value  # Delegates to property setter
        return self

    def getEventReadiness(self) -> "EventObdReadiness":
        """
        AUTOSAR-compliant getter for eventReadiness.

        Returns:
            The eventReadiness value

        Note:
            Delegates to event_readiness property (CODING_RULE_V2_00017)
        """
        return self.event_readiness  # Delegates to property

    def setEventReadiness(self, value: "EventObdReadiness") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for eventReadiness with method chaining.

        Args:
            value: The eventReadiness to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_readiness property setter (gets validation automatically)
        """
        self.event_readiness = value  # Delegates to property setter
        return self

    def getObdDTCValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for obdDTCValue.

        Returns:
            The obdDTCValue value

        Note:
            Delegates to obd_dtc_value property (CODING_RULE_V2_00017)
        """
        return self.obd_dtc_value  # Delegates to property

    def setObdDTCValue(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for obdDTCValue with method chaining.

        Args:
            value: The obdDTCValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to obd_dtc_value property setter (gets validation automatically)
        """
        self.obd_dtc_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_consider_pto(self, value: Optional["Boolean"]) -> "DiagnosticTroubleCodeObd":
        """
        Set considerPto and return self for chaining.

        Args:
            value: The considerPto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_consider_pto("value")
        """
        self.consider_pto = value  # Use property setter (gets validation)
        return self

    def with_dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeObd":
        """
        Set dtcPropsProps and return self for chaining.

        Args:
            value: The dtcPropsProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dtc_props_props("value")
        """
        self.dtc_props_props = value  # Use property setter (gets validation)
        return self

    def with_event_readiness(self, value: Optional["EventObdReadiness"]) -> "DiagnosticTroubleCodeObd":
        """
        Set eventReadiness and return self for chaining.

        Args:
            value: The eventReadiness to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_readiness("value")
        """
        self.event_readiness = value  # Use property setter (gets validation)
        return self

    def with_obd_dtc_value(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeObd":
        """
        Set obdDTCValue and return self for chaining.

        Args:
            value: The obdDTCValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_obd_dtc_value("value")
        """
        self.obd_dtc_value = value  # Use property setter (gets validation)
        return self
