from typing import List


class DataConstr(ARElement):
    """
    This meta-class represents the ability to specify constraints on data.

    Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints::DataConstr

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 405, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 44, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 179, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular rule within the data constraints.
        self._dataConstrRule: List["DataConstrRule"] = []

    @property
    def data_constr_rule(self) -> List["DataConstrRule"]:
        """Get dataConstrRule (Pythonic accessor)."""
        return self._dataConstrRule

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataConstrRule(self) -> List["DataConstrRule"]:
        """
        AUTOSAR-compliant getter for dataConstrRule.

        Returns:
            The dataConstrRule value

        Note:
            Delegates to data_constr_rule property (CODING_RULE_V2_00017)
        """
        return self.data_constr_rule  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
