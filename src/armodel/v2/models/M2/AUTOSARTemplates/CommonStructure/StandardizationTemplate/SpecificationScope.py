from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import SpecificationDocument
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SpecificationScope(ARObject):
    """
    Specification of the relevant subset of Autosar specifications.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange::SpecificationScope

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 96, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Autosar or custom specifications that contain that are considered in this
        # Data Exchange Point.
        self._specification: List["SpecificationDocument"] = []

    @property
    def specification(self) -> List["SpecificationDocument"]:
        """Get specification (Pythonic accessor)."""
        return self._specification

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSpecification(self) -> List["SpecificationDocument"]:
        """
        AUTOSAR-compliant getter for specification.

        Returns:
            The specification value

        Note:
            Delegates to specification property (CODING_RULE_V2_00017)
        """
        return self.specification  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
