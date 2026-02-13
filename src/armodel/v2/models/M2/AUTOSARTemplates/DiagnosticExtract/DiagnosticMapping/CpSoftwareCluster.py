"""
AUTOSAR Package - CpSoftwareCluster

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster
"""


from __future__ import annotations

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.__init__ import (
    DiagnosticMapping,
)


class CpSwClusterToDiagEventMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CpSoftwareClusterResource with a Diagnostic Event. This allows for
    indicating that the CpSoftwareClusterResource is used to convey the
    reporting or status query of the mapped DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster::CpSwClusterToDiagEventMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 272, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the mapped CpSoftwareCluster Resource.
        # atp.
        # Status=draft.
        self._cpSoftware: Optional["CpSoftwareCluster"] = None

    @property
    def cp_software(self) -> Optional["CpSoftwareCluster"]:
        """Get cpSoftware (Pythonic accessor)."""
        return self._cpSoftware

    @cp_software.setter
    def cp_software(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set cpSoftware with validation.

        Args:
            value: The cpSoftware to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cpSoftware = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"cpSoftware must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._cpSoftware = value
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCpSoftware(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for cpSoftware.

        Returns:
            The cpSoftware value

        Note:
            Delegates to cp_software property (CODING_RULE_V2_00017)
        """
        return self.cp_software  # Delegates to property

    def setCpSoftware(self, value: "CpSoftwareCluster") -> CpSwClusterToDiagEventMapping:
        """
        AUTOSAR-compliant setter for cpSoftware with method chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Note:
            Delegates to cp_software property setter (gets validation automatically)
        """
        self.cp_software = value  # Delegates to property setter
        return self

    def getDiagnosticEvent(self) -> DiagnosticEvent:
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: DiagnosticEvent) -> CpSwClusterToDiagEventMapping:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> CpSwClusterToDiagEventMapping:
        """
        Set cpSoftware and return self for chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cp_software("value")
        """
        self.cp_software = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_event(self, value: Optional[DiagnosticEvent]) -> CpSwClusterToDiagEventMapping:
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



class CpSwClusterResourceToDiagDataElemMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CpSoftwareClusterResource with a DiagnosticData Element. This allows for
    indicating that the CpSoftwareClusterResource is used to convey the
    Diagnostic DataElement.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster::CpSwClusterResourceToDiagDataElemMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 273, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the affected CpSoftwareClusterResource.
        # Tags: atp.
        # Status=draft Resource.
        self._cpSoftware: Optional["CpSoftwareCluster"] = None

    @property
    def cp_software(self) -> Optional["CpSoftwareCluster"]:
        """Get cpSoftware (Pythonic accessor)."""
        return self._cpSoftware

    @cp_software.setter
    def cp_software(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set cpSoftware with validation.

        Args:
            value: The cpSoftware to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cpSoftware = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"cpSoftware must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._cpSoftware = value
        self._diagnosticData: Optional["DiagnosticDataElement"] = None

    @property
    def diagnostic_data(self) -> Optional["DiagnosticDataElement"]:
        """Get diagnosticData (Pythonic accessor)."""
        return self._diagnosticData

    @diagnostic_data.setter
    def diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set diagnosticData with validation.

        Args:
            value: The diagnosticData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticData = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"diagnosticData must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._diagnosticData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCpSoftware(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for cpSoftware.

        Returns:
            The cpSoftware value

        Note:
            Delegates to cp_software property (CODING_RULE_V2_00017)
        """
        return self.cp_software  # Delegates to property

    def setCpSoftware(self, value: "CpSoftwareCluster") -> CpSwClusterResourceToDiagDataElemMapping:
        """
        AUTOSAR-compliant setter for cpSoftware with method chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Note:
            Delegates to cp_software property setter (gets validation automatically)
        """
        self.cp_software = value  # Delegates to property setter
        return self

    def getDiagnosticData(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for diagnosticData.

        Returns:
            The diagnosticData value

        Note:
            Delegates to diagnostic_data property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_data  # Delegates to property

    def setDiagnosticData(self, value: "DiagnosticDataElement") -> CpSwClusterResourceToDiagDataElemMapping:
        """
        AUTOSAR-compliant setter for diagnosticData with method chaining.

        Args:
            value: The diagnosticData to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_data property setter (gets validation automatically)
        """
        self.diagnostic_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> CpSwClusterResourceToDiagDataElemMapping:
        """
        Set cpSoftware and return self for chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cp_software("value")
        """
        self.cp_software = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> CpSwClusterResourceToDiagDataElemMapping:
        """
        Set diagnosticData and return self for chaining.

        Args:
            value: The diagnosticData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_data("value")
        """
        self.diagnostic_data = value  # Use property setter (gets validation)
        return self



class CpSwClusterToDiagRoutineSubfunctionMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CpSoftwareClusterResource with a subfunction of a DiagnosticRoutine. This
    allows for indicating that the CpSoftwareClusterResource is used to convey
    the calling or result return of the mapped DiagnosticRoutine.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster::CpSwClusterToDiagRoutineSubfunctionMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 274, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the mapped CpSoftwareCluster Resource.
        # atp.
        # Status=draft.
        self._cpSoftware: Optional["CpSoftwareCluster"] = None

    @property
    def cp_software(self) -> Optional["CpSoftwareCluster"]:
        """Get cpSoftware (Pythonic accessor)."""
        return self._cpSoftware

    @cp_software.setter
    def cp_software(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set cpSoftware with validation.

        Args:
            value: The cpSoftware to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cpSoftware = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"cpSoftware must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._cpSoftware = value
        self._routine: Optional["DiagnosticRoutine"] = None

    @property
    def routine(self) -> Optional["DiagnosticRoutine"]:
        """Get routine (Pythonic accessor)."""
        return self._routine

    @routine.setter
    def routine(self, value: Optional["DiagnosticRoutine"]) -> None:
        """
        Set routine with validation.

        Args:
            value: The routine to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routine = None
            return

        if not isinstance(value, DiagnosticRoutine):
            raise TypeError(
                f"routine must be DiagnosticRoutine or None, got {type(value).__name__}"
            )
        self._routine = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCpSoftware(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for cpSoftware.

        Returns:
            The cpSoftware value

        Note:
            Delegates to cp_software property (CODING_RULE_V2_00017)
        """
        return self.cp_software  # Delegates to property

    def setCpSoftware(self, value: "CpSoftwareCluster") -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """
        AUTOSAR-compliant setter for cpSoftware with method chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Note:
            Delegates to cp_software property setter (gets validation automatically)
        """
        self.cp_software = value  # Delegates to property setter
        return self

    def getRoutine(self) -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant getter for routine.

        Returns:
            The routine value

        Note:
            Delegates to routine property (CODING_RULE_V2_00017)
        """
        return self.routine  # Delegates to property

    def setRoutine(self, value: "DiagnosticRoutine") -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """
        AUTOSAR-compliant setter for routine with method chaining.

        Args:
            value: The routine to set

        Returns:
            self for method chaining

        Note:
            Delegates to routine property setter (gets validation automatically)
        """
        self.routine = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """
        Set cpSoftware and return self for chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cp_software("value")
        """
        self.cp_software = value  # Use property setter (gets validation)
        return self

    def with_routine(self, value: Optional["DiagnosticRoutine"]) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """
        Set routine and return self for chaining.

        Args:
            value: The routine to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routine("value")
        """
        self.routine = value  # Use property setter (gets validation)
        return self



class CpSwClusterResourceToDiagFunctionIdMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CpSoftwareClusterResource with a subfunction of a
    DiagnosticFunctionIdentifier. This allows for indicating that the
    CpSoftwareClusterResource is used to convey the execution permission
    associated with the mapped function identifier.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster::CpSwClusterResourceToDiagFunctionIdMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 275, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the mapped CpSoftwareCluster Resource.
        # atp.
        # Status=draft.
        self._cpSoftware: Optional["CpSoftwareCluster"] = None

    @property
    def cp_software(self) -> Optional["CpSoftwareCluster"]:
        """Get cpSoftware (Pythonic accessor)."""
        return self._cpSoftware

    @cp_software.setter
    def cp_software(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set cpSoftware with validation.

        Args:
            value: The cpSoftware to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cpSoftware = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"cpSoftware must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._cpSoftware = value
        self._function: Optional["DiagnosticFunction"] = None

    @property
    def function(self) -> Optional["DiagnosticFunction"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"function must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._function = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCpSoftware(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for cpSoftware.

        Returns:
            The cpSoftware value

        Note:
            Delegates to cp_software property (CODING_RULE_V2_00017)
        """
        return self.cp_software  # Delegates to property

    def setCpSoftware(self, value: "CpSoftwareCluster") -> CpSwClusterResourceToDiagFunctionIdMapping:
        """
        AUTOSAR-compliant setter for cpSoftware with method chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Note:
            Delegates to cp_software property setter (gets validation automatically)
        """
        self.cp_software = value  # Delegates to property setter
        return self

    def getFunction(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: "DiagnosticFunction") -> CpSwClusterResourceToDiagFunctionIdMapping:
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> CpSwClusterResourceToDiagFunctionIdMapping:
        """
        Set cpSoftware and return self for chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cp_software("value")
        """
        self.cp_software = value  # Use property setter (gets validation)
        return self

    def with_function(self, value: Optional["DiagnosticFunction"]) -> CpSwClusterResourceToDiagFunctionIdMapping:
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self
