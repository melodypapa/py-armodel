from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)


class DiagnosticControlDTCSetting(DiagnosticServiceInstance):
    """
    This represents an instance of the "Control DTC Setting" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ControlDTCSetting

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 110, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all
                # DiagnosticControlDTCSetting given context.
        self._dtcSettingClass: Optional["DiagnosticControlDTC"] = None

    @property
    def dtc_setting_class(self) -> Optional["DiagnosticControlDTC"]:
        """Get dtcSettingClass (Pythonic accessor)."""
        return self._dtcSettingClass

    @dtc_setting_class.setter
    def dtc_setting_class(self, value: Optional["DiagnosticControlDTC"]) -> None:
        """
        Set dtcSettingClass with validation.

        Args:
            value: The dtcSettingClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dtcSettingClass = None
            return

        if not isinstance(value, DiagnosticControlDTC):
            raise TypeError(
                f"dtcSettingClass must be DiagnosticControlDTC or None, got {type(value).__name__}"
            )
        self._dtcSettingClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDtcSettingClass(self) -> "DiagnosticControlDTC":
        """
        AUTOSAR-compliant getter for dtcSettingClass.

        Returns:
            The dtcSettingClass value

        Note:
            Delegates to dtc_setting_class property (CODING_RULE_V2_00017)
        """
        return self.dtc_setting_class  # Delegates to property

    def setDtcSettingClass(self, value: "DiagnosticControlDTC") -> "DiagnosticControlDTCSetting":
        """
        AUTOSAR-compliant setter for dtcSettingClass with method chaining.

        Args:
            value: The dtcSettingClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to dtc_setting_class property setter (gets validation automatically)
        """
        self.dtc_setting_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dtc_setting_class(self, value: Optional["DiagnosticControlDTC"]) -> "DiagnosticControlDTCSetting":
        """
        Set dtcSettingClass and return self for chaining.

        Args:
            value: The dtcSettingClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dtc_setting_class("value")
        """
        self.dtc_setting_class = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
)


class DiagnosticControlDTCSettingClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Control
    DTC Setting" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ControlDTCSetting

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 111, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the decision whether the DTCSetting (see ISO 14229-1) is in
        # general the request message.
        self._controlOption: Optional["Boolean"] = None

    @property
    def control_option(self) -> Optional["Boolean"]:
        """Get controlOption (Pythonic accessor)."""
        return self._controlOption

    @control_option.setter
    def control_option(self, value: Optional["Boolean"]) -> None:
        """
        Set controlOption with validation.

        Args:
            value: The controlOption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._controlOption = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"controlOption must be Boolean or None, got {type(value).__name__}"
            )
        self._controlOption = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getControlOption(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for controlOption.

        Returns:
            The controlOption value

        Note:
            Delegates to control_option property (CODING_RULE_V2_00017)
        """
        return self.control_option  # Delegates to property

    def setControlOption(self, value: "Boolean") -> "DiagnosticControlDTCSettingClass":
        """
        AUTOSAR-compliant setter for controlOption with method chaining.

        Args:
            value: The controlOption to set

        Returns:
            self for method chaining

        Note:
            Delegates to control_option property setter (gets validation automatically)
        """
        self.control_option = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_control_option(self, value: Optional["Boolean"]) -> "DiagnosticControlDTCSettingClass":
        """
        Set controlOption and return self for chaining.

        Args:
            value: The controlOption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_control_option("value")
        """
        self.control_option = value  # Use property setter (gets validation)
        return self
