from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import ValueSpecification


class CompositeValueSpecification(ValueSpecification, ABC):
    """
    This abstract meta-class acts a base class for ValueSpecifications that have
    a composite form.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::CompositeValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 434, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompositeValueSpecification:
            raise TypeError("CompositeValueSpecification is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
