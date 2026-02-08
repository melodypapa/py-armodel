from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class CalibrationParameterValueSet(ARElement):
    """
    Specification of a constant that can be part of a package, i.e. it can be
    defined stand-alone.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::CalibrationParameter::CalibrationParameterValueSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 477, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents single CalibrationParameterValues in the
                # CalibrationParameterValueSet.
        # atpVariation.
        self._calibration: List["CalibrationParameter"] = []

    @property
    def calibration(self) -> List["CalibrationParameter"]:
        """Get calibration (Pythonic accessor)."""
        return self._calibration

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalibration(self) -> List["CalibrationParameter"]:
        """
        AUTOSAR-compliant getter for calibration.

        Returns:
            The calibration value

        Note:
            Delegates to calibration property (CODING_RULE_V2_00017)
        """
        return self.calibration  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
