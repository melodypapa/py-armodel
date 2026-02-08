from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DataFormatTailoring(ARObject):
    """
    This class collects all rules that tailor the AUTOSAR templates for a
    specific data exchange point.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::DataFormatTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 180, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of tailorings of Meta Classes.
        self._classTailoring: List["ClassTailoring"] = []

    @property
    def class_tailoring(self) -> List["ClassTailoring"]:
        """Get classTailoring (Pythonic accessor)."""
        return self._classTailoring
        # Specification of tailorings of Constraints that are not owned by any
        # Meta-Class.
        self._constraint: List["ConstraintTailoring"] = []

    @property
    def constraint(self) -> List["ConstraintTailoring"]:
        """Get constraint (Pythonic accessor)."""
        return self._constraint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClassTailoring(self) -> List["ClassTailoring"]:
        """
        AUTOSAR-compliant getter for classTailoring.

        Returns:
            The classTailoring value

        Note:
            Delegates to class_tailoring property (CODING_RULE_V2_00017)
        """
        return self.class_tailoring  # Delegates to property

    def getConstraint(self) -> List["ConstraintTailoring"]:
        """
        AUTOSAR-compliant getter for constraint.

        Returns:
            The constraint value

        Note:
            Delegates to constraint property (CODING_RULE_V2_00017)
        """
        return self.constraint  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
