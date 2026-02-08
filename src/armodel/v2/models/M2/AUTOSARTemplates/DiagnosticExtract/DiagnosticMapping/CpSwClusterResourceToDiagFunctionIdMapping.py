from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import DiagnosticMapping


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
        # This reference identifies the mapped DiagnosticFunction Identifier.
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

    def setCpSoftware(self, value: "CpSoftwareCluster") -> "CpSwClusterResourceToDiagFunctionIdMapping":
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

    def setFunction(self, value: "DiagnosticFunction") -> "CpSwClusterResourceToDiagFunctionIdMapping":
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

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> "CpSwClusterResourceToDiagFunctionIdMapping":
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

    def with_function(self, value: Optional["DiagnosticFunction"]) -> "CpSwClusterResourceToDiagFunctionIdMapping":
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
