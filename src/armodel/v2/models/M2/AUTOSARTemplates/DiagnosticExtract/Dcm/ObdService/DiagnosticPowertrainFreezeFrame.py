from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticCommonElement,
    DiagnosticParameter,
)


class DiagnosticPowertrainFreezeFrame(DiagnosticCommonElement):
    """
    This meta-class represents a powertrain-related freeze-frame. In theory,
    this meta-class would need an additional id attribute. However, legal
    regulations requires only a single value for this attribute anyway.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x02_RequestPowertrainFreeze::DiagnosticPowertrainFreezeFrame

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 153, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the PID associated with this instance of OBD mode 0x02
        # service.
        self._pid: List["DiagnosticParameter"] = []

    @property
    def pid(self) -> List["DiagnosticParameter"]:
        """Get pid (Pythonic accessor)."""
        return self._pid

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPid(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for pid.

        Returns:
            The pid value

        Note:
            Delegates to pid property (CODING_RULE_V2_00017)
        """
        return self.pid  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
