from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RptExecutableEntity(Identifiable):
    """
    This describes a ExecutableEntity instance which can be bypassed.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 200, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ExecutableEntity event instance activation the owning Rpt ExecutableEntity.
        # atpVariation.
        self._rptExecutable: List["RptExecutableEntity"] = []

    @property
    def rpt_executable(self) -> List["RptExecutableEntity"]:
        """Get rptExecutable (Pythonic accessor)."""
        return self._rptExecutable
        # read access to a variable atpSplitable; atpVariation.
        self._rptRead: List["RoleBasedMcData"] = []

    @property
    def rpt_read(self) -> List["RoleBasedMcData"]:
        """Get rptRead (Pythonic accessor)."""
        return self._rptRead
        # write access to a variable atpSplitable; atpVariation.
        self._rptWrite: List["RoleBasedMcData"] = []

    @property
    def rpt_write(self) -> List["RoleBasedMcData"]:
        """Get rptWrite (Pythonic accessor)."""
        return self._rptWrite
        # The symbol describing this ExecutableEntity’s entry point.
        self._symbol: Optional["CIdentifier"] = None

    @property
    def symbol(self) -> Optional["CIdentifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["CIdentifier"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"symbol must be CIdentifier or None, got {type(value).__name__}"
            )
        self._symbol = value

    def with_rpt_executable(self, value):
        """
        Set rpt_executable and return self for chaining.

        Args:
            value: The rpt_executable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_executable("value")
        """
        self.rpt_executable = value  # Use property setter (gets validation)
        return self

    def with_rpt_read(self, value):
        """
        Set rpt_read and return self for chaining.

        Args:
            value: The rpt_read to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_read("value")
        """
        self.rpt_read = value  # Use property setter (gets validation)
        return self

    def with_rpt_write(self, value):
        """
        Set rpt_write and return self for chaining.

        Args:
            value: The rpt_write to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_write("value")
        """
        self.rpt_write = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRptExecutable(self) -> List["RptExecutableEntity"]:
        """
        AUTOSAR-compliant getter for rptExecutable.

        Returns:
            The rptExecutable value

        Note:
            Delegates to rpt_executable property (CODING_RULE_V2_00017)
        """
        return self.rpt_executable  # Delegates to property

    def getRptRead(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for rptRead.

        Returns:
            The rptRead value

        Note:
            Delegates to rpt_read property (CODING_RULE_V2_00017)
        """
        return self.rpt_read  # Delegates to property

    def getRptWrite(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for rptWrite.

        Returns:
            The rptWrite value

        Note:
            Delegates to rpt_write property (CODING_RULE_V2_00017)
        """
        return self.rpt_write  # Delegates to property

    def getSymbol(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "CIdentifier") -> "RptExecutableEntity":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_symbol(self, value: Optional["CIdentifier"]) -> "RptExecutableEntity":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self
