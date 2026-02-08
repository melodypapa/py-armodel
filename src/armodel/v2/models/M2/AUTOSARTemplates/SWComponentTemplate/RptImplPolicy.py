from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    RptEnablerImplType,
    RptPreparationEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class RptImplPolicy(ARObject):
    """
    Describes the code preparation for rapid prototyping at data accesses.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RptImplPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 202, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 854, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # For Level 2 or Level3 this property determines how the RTE implements the
        # additional "RP enabler" flag.
        self._rptEnablerImpl: Optional["RptEnablerImplType"] = None

    @property
    def rpt_enabler_impl(self) -> Optional["RptEnablerImplType"]:
        """Get rptEnablerImpl (Pythonic accessor)."""
        return self._rptEnablerImpl

    @rpt_enabler_impl.setter
    def rpt_enabler_impl(self, value: Optional["RptEnablerImplType"]) -> None:
        """
        Set rptEnablerImpl with validation.

        Args:
            value: The rptEnablerImpl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptEnablerImpl = None
            return

        if not isinstance(value, RptEnablerImplType):
            raise TypeError(
                f"rptEnablerImpl must be RptEnablerImplType or None, got {type(value).__name__}"
            )
        self._rptEnablerImpl = value
        # Mandates RP preparation level for access to VariableData within generated RTE
        # implementation.
        self._rptPreparation: Optional["RptPreparationEnum"] = None

    @property
    def rpt_preparation(self) -> Optional["RptPreparationEnum"]:
        """Get rptPreparation (Pythonic accessor)."""
        return self._rptPreparation

    @rpt_preparation.setter
    def rpt_preparation(self, value: Optional["RptPreparationEnum"]) -> None:
        """
        Set rptPreparation with validation.

        Args:
            value: The rptPreparation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptPreparation = None
            return

        if not isinstance(value, RptPreparationEnum):
            raise TypeError(
                f"rptPreparation must be RptPreparationEnum or None, got {type(value).__name__}"
            )
        self._rptPreparation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRptEnablerImpl(self) -> "RptEnablerImplType":
        """
        AUTOSAR-compliant getter for rptEnablerImpl.

        Returns:
            The rptEnablerImpl value

        Note:
            Delegates to rpt_enabler_impl property (CODING_RULE_V2_00017)
        """
        return self.rpt_enabler_impl  # Delegates to property

    def setRptEnablerImpl(self, value: "RptEnablerImplType") -> "RptImplPolicy":
        """
        AUTOSAR-compliant setter for rptEnablerImpl with method chaining.

        Args:
            value: The rptEnablerImpl to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_enabler_impl property setter (gets validation automatically)
        """
        self.rpt_enabler_impl = value  # Delegates to property setter
        return self

    def getRptPreparation(self) -> "RptPreparationEnum":
        """
        AUTOSAR-compliant getter for rptPreparation.

        Returns:
            The rptPreparation value

        Note:
            Delegates to rpt_preparation property (CODING_RULE_V2_00017)
        """
        return self.rpt_preparation  # Delegates to property

    def setRptPreparation(self, value: "RptPreparationEnum") -> "RptImplPolicy":
        """
        AUTOSAR-compliant setter for rptPreparation with method chaining.

        Args:
            value: The rptPreparation to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_preparation property setter (gets validation automatically)
        """
        self.rpt_preparation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_enabler_impl(self, value: Optional["RptEnablerImplType"]) -> "RptImplPolicy":
        """
        Set rptEnablerImpl and return self for chaining.

        Args:
            value: The rptEnablerImpl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_enabler_impl("value")
        """
        self.rpt_enabler_impl = value  # Use property setter (gets validation)
        return self

    def with_rpt_preparation(self, value: Optional["RptPreparationEnum"]) -> "RptImplPolicy":
        """
        Set rptPreparation and return self for chaining.

        Args:
            value: The rptPreparation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_preparation("value")
        """
        self.rpt_preparation = value  # Use property setter (gets validation)
        return self
