from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestVehicleInfo(DiagnosticServiceInstance):
    """
    This meta-class represents the ability to model an instance of the OBD mode
    0x09 service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x09_RequestVehicleInformation

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 160, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the info type associated with the mode.
        self._infoType: Optional["DiagnosticInfoType"] = None

    @property
    def info_type(self) -> Optional["DiagnosticInfoType"]:
        """Get infoType (Pythonic accessor)."""
        return self._infoType

    @info_type.setter
    def info_type(self, value: Optional["DiagnosticInfoType"]) -> None:
        """
        Set infoType with validation.

        Args:
            value: The infoType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._infoType = None
            return

        if not isinstance(value, DiagnosticInfoType):
            raise TypeError(
                f"infoType must be DiagnosticInfoType or None, got {type(value).__name__}"
            )
        self._infoType = value
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # among all DiagnosticRequesVehicleInfo given context.
        self._requestVehicle: Optional["DiagnosticRequest"] = None

    @property
    def request_vehicle(self) -> Optional["DiagnosticRequest"]:
        """Get requestVehicle (Pythonic accessor)."""
        return self._requestVehicle

    @request_vehicle.setter
    def request_vehicle(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set requestVehicle with validation.

        Args:
            value: The requestVehicle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestVehicle = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"requestVehicle must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._requestVehicle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInfoType(self) -> "DiagnosticInfoType":
        """
        AUTOSAR-compliant getter for infoType.

        Returns:
            The infoType value

        Note:
            Delegates to info_type property (CODING_RULE_V2_00017)
        """
        return self.info_type  # Delegates to property

    def setInfoType(self, value: "DiagnosticInfoType") -> "DiagnosticRequestVehicleInfo":
        """
        AUTOSAR-compliant setter for infoType with method chaining.

        Args:
            value: The infoType to set

        Returns:
            self for method chaining

        Note:
            Delegates to info_type property setter (gets validation automatically)
        """
        self.info_type = value  # Delegates to property setter
        return self

    def getRequestVehicle(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for requestVehicle.

        Returns:
            The requestVehicle value

        Note:
            Delegates to request_vehicle property (CODING_RULE_V2_00017)
        """
        return self.request_vehicle  # Delegates to property

    def setRequestVehicle(self, value: "DiagnosticRequest") -> "DiagnosticRequestVehicleInfo":
        """
        AUTOSAR-compliant setter for requestVehicle with method chaining.

        Args:
            value: The requestVehicle to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_vehicle property setter (gets validation automatically)
        """
        self.request_vehicle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_info_type(self, value: Optional["DiagnosticInfoType"]) -> "DiagnosticRequestVehicleInfo":
        """
        Set infoType and return self for chaining.

        Args:
            value: The infoType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_info_type("value")
        """
        self.info_type = value  # Use property setter (gets validation)
        return self

    def with_request_vehicle(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestVehicleInfo":
        """
        Set requestVehicle and return self for chaining.

        Args:
            value: The requestVehicle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_vehicle("value")
        """
        self.request_vehicle = value  # Use property setter (gets validation)
        return self

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
)


class DiagnosticRequestVehicleInfoClass(DiagnosticServiceClass):
    """
    This meta-class represents the ability to define common properties for all
    instances of the "Request Vehicle Info" OBD diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x09_RequestVehicleInformation

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 160, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
