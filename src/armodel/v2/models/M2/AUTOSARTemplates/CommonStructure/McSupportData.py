from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    McDataInstance,
    McSwEmulationMethod,
    RptSupportData,
    SwSystemconstant,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class McSupportData(ARObject):
    """
    Root element for all measurement and calibration support data related to one
    Implementation artifact on an ECU. There shall be one such element related
    to the RTE implementation (if it owns MC data) and a separate one for each
    module or component, which owns private MC data.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McSupportData

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 172, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 999, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes the calibration method used by the RTE.
        # This information is not needed for A2L generation, but to setup in the ECU.
        # atpVariation.
        self._emulation: List["McSwEmulationMethod"] = []

    @property
    def emulation(self) -> List["McSwEmulationMethod"]:
        """Get emulation (Pythonic accessor)."""
        return self._emulation
        # A data instance to be used for calibration.
        # atpSplitable; atpVariation.
        self._mcParameter: List["McDataInstance"] = []

    @property
    def mc_parameter(self) -> List["McDataInstance"]:
        """Get mcParameter (Pythonic accessor)."""
        return self._mcParameter
        # A data instance to be used for measurement.
        # atpSplitable; atpVariation.
        self._mcVariable: List["McDataInstance"] = []

    @property
    def mc_variable(self) -> List["McDataInstance"]:
        """Get mcVariable (Pythonic accessor)."""
        return self._mcVariable
        # Sets of system constant values to be transferred to the MCD system, because
        # the system constants have been with "swCalibrationAccess" = readonly.
        self._measurable: List["SwSystemconstant"] = []

    @property
    def measurable(self) -> List["SwSystemconstant"]:
        """Get measurable (Pythonic accessor)."""
        return self._measurable
        # The rapid prototyping support data belonging to this aggregtion is
        # <<atpSplitable>> case of an already exisiting BSW this description will be
        # added later process, namely at code generation time.
        self._rptSupportData: Optional["RptSupportData"] = None

    @property
    def rpt_support_data(self) -> Optional["RptSupportData"]:
        """Get rptSupportData (Pythonic accessor)."""
        return self._rptSupportData

    @rpt_support_data.setter
    def rpt_support_data(self, value: Optional["RptSupportData"]) -> None:
        """
        Set rptSupportData with validation.

        Args:
            value: The rptSupportData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptSupportData = None
            return

        if not isinstance(value, RptSupportData):
            raise TypeError(
                f"rptSupportData must be RptSupportData or None, got {type(value).__name__}"
            )
        self._rptSupportData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEmulation(self) -> List["McSwEmulationMethod"]:
        """
        AUTOSAR-compliant getter for emulation.

        Returns:
            The emulation value

        Note:
            Delegates to emulation property (CODING_RULE_V2_00017)
        """
        return self.emulation  # Delegates to property

    def getMcParameter(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for mcParameter.

        Returns:
            The mcParameter value

        Note:
            Delegates to mc_parameter property (CODING_RULE_V2_00017)
        """
        return self.mc_parameter  # Delegates to property

    def getMcVariable(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for mcVariable.

        Returns:
            The mcVariable value

        Note:
            Delegates to mc_variable property (CODING_RULE_V2_00017)
        """
        return self.mc_variable  # Delegates to property

    def getMeasurable(self) -> List["SwSystemconstant"]:
        """
        AUTOSAR-compliant getter for measurable.

        Returns:
            The measurable value

        Note:
            Delegates to measurable property (CODING_RULE_V2_00017)
        """
        return self.measurable  # Delegates to property

    def getRptSupportData(self) -> "RptSupportData":
        """
        AUTOSAR-compliant getter for rptSupportData.

        Returns:
            The rptSupportData value

        Note:
            Delegates to rpt_support_data property (CODING_RULE_V2_00017)
        """
        return self.rpt_support_data  # Delegates to property

    def setRptSupportData(self, value: "RptSupportData") -> "McSupportData":
        """
        AUTOSAR-compliant setter for rptSupportData with method chaining.

        Args:
            value: The rptSupportData to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_support_data property setter (gets validation automatically)
        """
        self.rpt_support_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_support_data(self, value: Optional["RptSupportData"]) -> "McSupportData":
        """
        Set rptSupportData and return self for chaining.

        Args:
            value: The rptSupportData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_support_data("value")
        """
        self.rpt_support_data = value  # Use property setter (gets validation)
        return self
