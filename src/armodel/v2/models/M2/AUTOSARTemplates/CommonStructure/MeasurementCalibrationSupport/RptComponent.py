from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    RoleBasedMcData,
    RptExecutableEntity,
    RptImplPolicy,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RptComponent(Identifiable):
    """
    Description of component instance for which rapid prototyping support is
    implemented.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptComponent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 199, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to related McDataElement describing the implementation of "RP
        # global buffer", "RP global "RP enabler flag" and the "RP flag".
        self._mcData: List["RoleBasedMcData"] = []

    @property
    def mc_data(self) -> List["RoleBasedMcData"]:
        """Get mcData (Pythonic accessor)."""
        return self._mcData
        # Describes the implemented code preparation for rapid data accesses.
        self._rpImplPolicy: Optional["RptImplPolicy"] = None

    @property
    def rp_impl_policy(self) -> Optional["RptImplPolicy"]:
        """Get rpImplPolicy (Pythonic accessor)."""
        return self._rpImplPolicy

    @rp_impl_policy.setter
    def rp_impl_policy(self, value: Optional["RptImplPolicy"]) -> None:
        """
        Set rpImplPolicy with validation.

        Args:
            value: The rpImplPolicy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rpImplPolicy = None
            return

        if not isinstance(value, RptImplPolicy):
            raise TypeError(
                f"rpImplPolicy must be RptImplPolicy or None, got {type(value).__name__}"
            )
        self._rpImplPolicy = value
        # ExecutableEntity instance which can be bypassed.
        # atpSplitable; atpVariation.
        self._rptExecutable: List["RptExecutableEntity"] = []

    @property
    def rpt_executable(self) -> List["RptExecutableEntity"]:
        """Get rptExecutable (Pythonic accessor)."""
        return self._rptExecutable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMcData(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for mcData.

        Returns:
            The mcData value

        Note:
            Delegates to mc_data property (CODING_RULE_V2_00017)
        """
        return self.mc_data  # Delegates to property

    def getRpImplPolicy(self) -> "RptImplPolicy":
        """
        AUTOSAR-compliant getter for rpImplPolicy.

        Returns:
            The rpImplPolicy value

        Note:
            Delegates to rp_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.rp_impl_policy  # Delegates to property

    def setRpImplPolicy(self, value: "RptImplPolicy") -> "RptComponent":
        """
        AUTOSAR-compliant setter for rpImplPolicy with method chaining.

        Args:
            value: The rpImplPolicy to set

        Returns:
            self for method chaining

        Note:
            Delegates to rp_impl_policy property setter (gets validation automatically)
        """
        self.rp_impl_policy = value  # Delegates to property setter
        return self

    def getRptExecutable(self) -> List["RptExecutableEntity"]:
        """
        AUTOSAR-compliant getter for rptExecutable.

        Returns:
            The rptExecutable value

        Note:
            Delegates to rpt_executable property (CODING_RULE_V2_00017)
        """
        return self.rpt_executable  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rp_impl_policy(self, value: Optional["RptImplPolicy"]) -> "RptComponent":
        """
        Set rpImplPolicy and return self for chaining.

        Args:
            value: The rpImplPolicy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rp_impl_policy("value")
        """
        self.rp_impl_policy = value  # Use property setter (gets validation)
        return self
