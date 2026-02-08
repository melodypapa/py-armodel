from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import InterpolationRoutine
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class InterpolationRoutineMappingSet(ARElement):
    """
    This meta-class specifies a set of interpolation routine mappings. (cid:53)
    429 of 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate
    Software Component Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine::InterpolationRoutineMappingSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 429, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 46, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies one particular mapping of recordlayout and its matching
        # interpolationRoutines.
        self._interpolation: List["InterpolationRoutine"] = []

    @property
    def interpolation(self) -> List["InterpolationRoutine"]:
        """Get interpolation (Pythonic accessor)."""
        return self._interpolation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInterpolation(self) -> List["InterpolationRoutine"]:
        """
        AUTOSAR-compliant getter for interpolation.

        Returns:
            The interpolation value

        Note:
            Delegates to interpolation property (CODING_RULE_V2_00017)
        """
        return self.interpolation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
