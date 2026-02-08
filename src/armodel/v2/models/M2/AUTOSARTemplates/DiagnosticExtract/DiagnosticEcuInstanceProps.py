from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticEcuInstanceProps(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model properties that are specific
    for a given EcuInstance but on the other hand represent purely
    diagnostic-related information. In the spirit of decentralized configuration
    it is therefore possible to specify the diagnostic-related information
    related to a given EcuInstance even if the EcuInstance does not yet exist.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution::DiagnosticEcuInstanceProps

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 207, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the actual EcuInstance to which the in the
        # DiagnosticEcuInstance.
        self._ecuInstance: List["EcuInstance"] = []

    @property
    def ecu_instance(self) -> List["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance
        # This attribute is used to specify the role (if applicable) in the
        # DiagnosticEcuInstance supports OBD.
        self._obdSupport: Optional["DiagnosticObdSupport"] = None

    @property
    def obd_support(self) -> Optional["DiagnosticObdSupport"]:
        """Get obdSupport (Pythonic accessor)."""
        return self._obdSupport

    @obd_support.setter
    def obd_support(self, value: Optional["DiagnosticObdSupport"]) -> None:
        """
        Set obdSupport with validation.

        Args:
            value: The obdSupport to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdSupport = None
            return

        if not isinstance(value, DiagnosticObdSupport):
            raise TypeError(
                f"obdSupport must be DiagnosticObdSupport or None, got {type(value).__name__}"
            )
        self._obdSupport = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuInstance(self) -> List["EcuInstance"]:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def getObdSupport(self) -> "DiagnosticObdSupport":
        """
        AUTOSAR-compliant getter for obdSupport.

        Returns:
            The obdSupport value

        Note:
            Delegates to obd_support property (CODING_RULE_V2_00017)
        """
        return self.obd_support  # Delegates to property

    def setObdSupport(self, value: "DiagnosticObdSupport") -> "DiagnosticEcuInstanceProps":
        """
        AUTOSAR-compliant setter for obdSupport with method chaining.

        Args:
            value: The obdSupport to set

        Returns:
            self for method chaining

        Note:
            Delegates to obd_support property setter (gets validation automatically)
        """
        self.obd_support = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_obd_support(self, value: Optional["DiagnosticObdSupport"]) -> "DiagnosticEcuInstanceProps":
        """
        Set obdSupport and return self for chaining.

        Args:
            value: The obdSupport to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_obd_support("value")
        """
        self.obd_support = value  # Use property setter (gets validation)
        return self
