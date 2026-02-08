from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import RptAccessEnum
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class RptSwPrototypingAccess(ARObject):
    """
    Describes the accessibility of data and modes by the rapid prototyping
    tooling.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptSwPrototypingAccess

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 199, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 856, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The related data element can be modified using a tool.
        # An ENABLED VariableData implicitly READABLE/WRITABLE.
        self._rptHookAccess: Optional["RptAccessEnum"] = None

    @property
    def rpt_hook_access(self) -> Optional["RptAccessEnum"]:
        """Get rptHookAccess (Pythonic accessor)."""
        return self._rptHookAccess

    @rpt_hook_access.setter
    def rpt_hook_access(self, value: Optional["RptAccessEnum"]) -> None:
        """
        Set rptHookAccess with validation.

        Args:
            value: The rptHookAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptHookAccess = None
            return

        if not isinstance(value, RptAccessEnum):
            raise TypeError(
                f"rptHookAccess must be RptAccessEnum or None, got {type(value).__name__}"
            )
        self._rptHookAccess = value
        # The related data element can be used as input for bypass RP tool.
        # If rptImplPolicy is not specified generation shall ensure at least suitable
                # MC are created.
        self._rptReadAccess: Optional["RptAccessEnum"] = None

    @property
    def rpt_read_access(self) -> Optional["RptAccessEnum"]:
        """Get rptReadAccess (Pythonic accessor)."""
        return self._rptReadAccess

    @rpt_read_access.setter
    def rpt_read_access(self, value: Optional["RptAccessEnum"]) -> None:
        """
        Set rptReadAccess with validation.

        Args:
            value: The rptReadAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptReadAccess = None
            return

        if not isinstance(value, RptAccessEnum):
            raise TypeError(
                f"rptReadAccess must be RptAccessEnum or None, got {type(value).__name__}"
            )
        self._rptReadAccess = value
        # The related data element can be used as output for by RP tool.
        # The data element shall to rptLevel2 and related write service points.
        self._rptWriteAccess: Optional["RptAccessEnum"] = None

    @property
    def rpt_write_access(self) -> Optional["RptAccessEnum"]:
        """Get rptWriteAccess (Pythonic accessor)."""
        return self._rptWriteAccess

    @rpt_write_access.setter
    def rpt_write_access(self, value: Optional["RptAccessEnum"]) -> None:
        """
        Set rptWriteAccess with validation.

        Args:
            value: The rptWriteAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptWriteAccess = None
            return

        if not isinstance(value, RptAccessEnum):
            raise TypeError(
                f"rptWriteAccess must be RptAccessEnum or None, got {type(value).__name__}"
            )
        self._rptWriteAccess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRptHookAccess(self) -> "RptAccessEnum":
        """
        AUTOSAR-compliant getter for rptHookAccess.

        Returns:
            The rptHookAccess value

        Note:
            Delegates to rpt_hook_access property (CODING_RULE_V2_00017)
        """
        return self.rpt_hook_access  # Delegates to property

    def setRptHookAccess(self, value: "RptAccessEnum") -> "RptSwPrototypingAccess":
        """
        AUTOSAR-compliant setter for rptHookAccess with method chaining.

        Args:
            value: The rptHookAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_hook_access property setter (gets validation automatically)
        """
        self.rpt_hook_access = value  # Delegates to property setter
        return self

    def getRptReadAccess(self) -> "RptAccessEnum":
        """
        AUTOSAR-compliant getter for rptReadAccess.

        Returns:
            The rptReadAccess value

        Note:
            Delegates to rpt_read_access property (CODING_RULE_V2_00017)
        """
        return self.rpt_read_access  # Delegates to property

    def setRptReadAccess(self, value: "RptAccessEnum") -> "RptSwPrototypingAccess":
        """
        AUTOSAR-compliant setter for rptReadAccess with method chaining.

        Args:
            value: The rptReadAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_read_access property setter (gets validation automatically)
        """
        self.rpt_read_access = value  # Delegates to property setter
        return self

    def getRptWriteAccess(self) -> "RptAccessEnum":
        """
        AUTOSAR-compliant getter for rptWriteAccess.

        Returns:
            The rptWriteAccess value

        Note:
            Delegates to rpt_write_access property (CODING_RULE_V2_00017)
        """
        return self.rpt_write_access  # Delegates to property

    def setRptWriteAccess(self, value: "RptAccessEnum") -> "RptSwPrototypingAccess":
        """
        AUTOSAR-compliant setter for rptWriteAccess with method chaining.

        Args:
            value: The rptWriteAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_write_access property setter (gets validation automatically)
        """
        self.rpt_write_access = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_hook_access(self, value: Optional["RptAccessEnum"]) -> "RptSwPrototypingAccess":
        """
        Set rptHookAccess and return self for chaining.

        Args:
            value: The rptHookAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_hook_access("value")
        """
        self.rpt_hook_access = value  # Use property setter (gets validation)
        return self

    def with_rpt_read_access(self, value: Optional["RptAccessEnum"]) -> "RptSwPrototypingAccess":
        """
        Set rptReadAccess and return self for chaining.

        Args:
            value: The rptReadAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_read_access("value")
        """
        self.rpt_read_access = value  # Use property setter (gets validation)
        return self

    def with_rpt_write_access(self, value: Optional["RptAccessEnum"]) -> "RptSwPrototypingAccess":
        """
        Set rptWriteAccess and return self for chaining.

        Args:
            value: The rptWriteAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_write_access("value")
        """
        self.rpt_write_access = value  # Use property setter (gets validation)
        return self
