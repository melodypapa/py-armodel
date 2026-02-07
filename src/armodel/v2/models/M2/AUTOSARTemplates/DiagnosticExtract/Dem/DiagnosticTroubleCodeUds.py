from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticTroubleCodeUds(DiagnosticTroubleCode):
    """
    This element is used to describe non OBD-relevant DTCs.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeUds
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 173, Classic Platform
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
        # This attribute specifies the Event OBD Readiness group for PID $01 and PID
                # $41 computation.
        # This attribute is for emission-related ECUs.
        # atpVariation 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
                # Template R23-11.
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
        # This attribute specifies a 1-byte value which identifies the vehicle / system
                # function which DTC.
        # This parameter is necessary for the severity information.
        self._functionalUnit: Optional["PositiveInteger"] = None

    @property
    def functional_unit(self) -> Optional["PositiveInteger"]:
        """Get functionalUnit (Pythonic accessor)."""
        return self._functionalUnit

    @functional_unit.setter
    def functional_unit(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set functionalUnit with validation.
        
        Args:
            value: The functionalUnit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionalUnit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"functionalUnit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._functionalUnit = value
        # 3 Byte OBD DTC value based on the definition from SAE The existence of this
        # attribute is only required if and OBD DTC values are used for SAE this
        # attribute does not exist, then UDS DTC used with J1979-2.
        self._obdDtc: Optional["PositiveInteger"] = None

    @property
    def obd_dtc(self) -> Optional["PositiveInteger"]:
        """Get obdDtc (Pythonic accessor)."""
        return self._obdDtc

    @obd_dtc.setter
    def obd_dtc(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set obdDtc with validation.
        
        Args:
            value: The obdDtc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdDtc = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"obdDtc must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._obdDtc = value
        # DTC severity according to ISO 14229-1.
        # atpVariation.
        self._severity: Optional["DiagnosticUdsSeverity"] = None

    @property
    def severity(self) -> Optional["DiagnosticUdsSeverity"]:
        """Get severity (Pythonic accessor)."""
        return self._severity

    @severity.setter
    def severity(self, value: Optional["DiagnosticUdsSeverity"]) -> None:
        """
        Set severity with validation.
        
        Args:
            value: The severity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._severity = None
            return

        if not isinstance(value, DiagnosticUdsSeverity):
            raise TypeError(
                f"severity must be DiagnosticUdsSeverity or None, got {type(value).__name__}"
            )
        self._severity = value
        # Unique Diagnostic Trouble Code value for UDS.
        self._udsDtcValue: Optional["PositiveInteger"] = None

    @property
    def uds_dtc_value(self) -> Optional["PositiveInteger"]:
        """Get udsDtcValue (Pythonic accessor)."""
        return self._udsDtcValue

    @uds_dtc_value.setter
    def uds_dtc_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set udsDtcValue with validation.
        
        Args:
            value: The udsDtcValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udsDtcValue = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"udsDtcValue must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._udsDtcValue = value
        # This attribute is used to identify (if applicable) the.
        self._wwhObdDtc: Optional["DiagnosticWwhObdDtc"] = None

    @property
    def wwh_obd_dtc(self) -> Optional["DiagnosticWwhObdDtc"]:
        """Get wwhObdDtc (Pythonic accessor)."""
        return self._wwhObdDtc

    @wwh_obd_dtc.setter
    def wwh_obd_dtc(self, value: Optional["DiagnosticWwhObdDtc"]) -> None:
        """
        Set wwhObdDtc with validation.
        
        Args:
            value: The wwhObdDtc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wwhObdDtc = None
            return

        if not isinstance(value, DiagnosticWwhObdDtc):
            raise TypeError(
                f"wwhObdDtc must be DiagnosticWwhObdDtc or None, got {type(value).__name__}"
            )
        self._wwhObdDtc = value

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

    def setConsiderPto(self, value: "Boolean") -> "DiagnosticTroubleCodeUds":
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

    def setDtcPropsProps(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeUds":
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

    def setEventReadiness(self, value: "EventObdReadiness") -> "DiagnosticTroubleCodeUds":
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

    def getFunctionalUnit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for functionalUnit.
        
        Returns:
            The functionalUnit value
        
        Note:
            Delegates to functional_unit property (CODING_RULE_V2_00017)
        """
        return self.functional_unit  # Delegates to property

    def setFunctionalUnit(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for functionalUnit with method chaining.
        
        Args:
            value: The functionalUnit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to functional_unit property setter (gets validation automatically)
        """
        self.functional_unit = value  # Delegates to property setter
        return self

    def getObdDtc(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for obdDtc.
        
        Returns:
            The obdDtc value
        
        Note:
            Delegates to obd_dtc property (CODING_RULE_V2_00017)
        """
        return self.obd_dtc  # Delegates to property

    def setObdDtc(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for obdDtc with method chaining.
        
        Args:
            value: The obdDtc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to obd_dtc property setter (gets validation automatically)
        """
        self.obd_dtc = value  # Delegates to property setter
        return self

    def getSeverity(self) -> "DiagnosticUdsSeverity":
        """
        AUTOSAR-compliant getter for severity.
        
        Returns:
            The severity value
        
        Note:
            Delegates to severity property (CODING_RULE_V2_00017)
        """
        return self.severity  # Delegates to property

    def setSeverity(self, value: "DiagnosticUdsSeverity") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for severity with method chaining.
        
        Args:
            value: The severity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to severity property setter (gets validation automatically)
        """
        self.severity = value  # Delegates to property setter
        return self

    def getUdsDtcValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for udsDtcValue.
        
        Returns:
            The udsDtcValue value
        
        Note:
            Delegates to uds_dtc_value property (CODING_RULE_V2_00017)
        """
        return self.uds_dtc_value  # Delegates to property

    def setUdsDtcValue(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for udsDtcValue with method chaining.
        
        Args:
            value: The udsDtcValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to uds_dtc_value property setter (gets validation automatically)
        """
        self.uds_dtc_value = value  # Delegates to property setter
        return self

    def getWwhObdDtc(self) -> "DiagnosticWwhObdDtc":
        """
        AUTOSAR-compliant getter for wwhObdDtc.
        
        Returns:
            The wwhObdDtc value
        
        Note:
            Delegates to wwh_obd_dtc property (CODING_RULE_V2_00017)
        """
        return self.wwh_obd_dtc  # Delegates to property

    def setWwhObdDtc(self, value: "DiagnosticWwhObdDtc") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for wwhObdDtc with method chaining.
        
        Args:
            value: The wwhObdDtc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to wwh_obd_dtc property setter (gets validation automatically)
        """
        self.wwh_obd_dtc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_consider_pto(self, value: Optional["Boolean"]) -> "DiagnosticTroubleCodeUds":
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

    def with_dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeUds":
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

    def with_event_readiness(self, value: Optional["EventObdReadiness"]) -> "DiagnosticTroubleCodeUds":
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

    def with_functional_unit(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeUds":
        """
        Set functionalUnit and return self for chaining.
        
        Args:
            value: The functionalUnit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_functional_unit("value")
        """
        self.functional_unit = value  # Use property setter (gets validation)
        return self

    def with_obd_dtc(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeUds":
        """
        Set obdDtc and return self for chaining.
        
        Args:
            value: The obdDtc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_obd_dtc("value")
        """
        self.obd_dtc = value  # Use property setter (gets validation)
        return self

    def with_severity(self, value: Optional["DiagnosticUdsSeverity"]) -> "DiagnosticTroubleCodeUds":
        """
        Set severity and return self for chaining.
        
        Args:
            value: The severity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_severity("value")
        """
        self.severity = value  # Use property setter (gets validation)
        return self

    def with_uds_dtc_value(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeUds":
        """
        Set udsDtcValue and return self for chaining.
        
        Args:
            value: The udsDtcValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_uds_dtc_value("value")
        """
        self.uds_dtc_value = value  # Use property setter (gets validation)
        return self

    def with_wwh_obd_dtc(self, value: Optional["DiagnosticWwhObdDtc"]) -> "DiagnosticTroubleCodeUds":
        """
        Set wwhObdDtc and return self for chaining.
        
        Args:
            value: The wwhObdDtc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_wwh_obd_dtc("value")
        """
        self.wwh_obd_dtc = value  # Use property setter (gets validation)
        return self