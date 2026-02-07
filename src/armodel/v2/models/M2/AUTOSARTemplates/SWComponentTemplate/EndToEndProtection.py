from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class EndToEndProtection(Identifiable):
    """
    This meta-class represents the ability to describe a particular end to end
    protection.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection::EndToEndProtection

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 214, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 384, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines to which VariableDataPrototypes in the roles of one sender and one or
                # more receivers this EndTo applies.
        # shall be possible to aggregate several EndToEnd case additional are
                # introduced subsequently.
        # case one particular PortPrototype is split into and connectors, all
                # representing data entity.
        # E2E wrapper approach involves are not subjected to the AUTOSAR is superseded
                # by the superior E2E (which is fully standardized by new projects (without
                # legacy to carry-over parts) shall use the fully transformer approach.
        # atpVariation.
        self._endToEnd: List["EndToEndProtection"] = []

    @property
    def end_to_end(self) -> List["EndToEndProtection"]:
        """Get endToEnd (Pythonic accessor)."""
        return self._endToEnd

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEndToEnd(self) -> List["EndToEndProtection"]:
        """
        AUTOSAR-compliant getter for endToEnd.

        Returns:
            The endToEnd value

        Note:
            Delegates to end_to_end property (CODING_RULE_V2_00017)
        """
        return self.end_to_end  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
