from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwCalprmAxisSet(ARObject):
    """
    This element specifies the input parameter axes (abscissas) of parameters
    (and variables, if these are used adaptively).

    Package: M2::MSR::DataDictionary::CalibrationParameter

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 351, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # One axis belonging to this SwCalprmAxisSet.
        self._swCalprmAxis: List["SwCalprmAxis"] = []

    @property
    def sw_calprm_axis(self) -> List["SwCalprmAxis"]:
        """Get swCalprmAxis (Pythonic accessor)."""
        return self._swCalprmAxis

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwCalprmAxis(self) -> List["SwCalprmAxis"]:
        """
        AUTOSAR-compliant getter for swCalprmAxis.

        Returns:
            The swCalprmAxis value

        Note:
            Delegates to sw_calprm_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_axis  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
