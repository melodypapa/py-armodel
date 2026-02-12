"""
AUTOSAR Package - GeneralPurposeConnection

Package: M2::AUTOSARTemplates::SystemTemplate::GeneralPurposeConnection
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class GeneralPurposeConnection(ARElement):
    """
    This meta-class allows to describe the relationship between several
    PduTriggerings that are defined on the same PhysicalChannel, e.g. to create
    a link between Rx and Tx Pdu that are used for request/ response.

    Package: M2::AUTOSARTemplates::SystemTemplate::GeneralPurposeConnection::GeneralPurposeConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 388, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to PduTriggerings that are connected to each a
        # GeneralPurposeConnection.
        self._pduTriggering: List["RefType"] = []

    @property
    def pdu_triggering(self) -> List["RefType"]:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    def with_pdu_triggering(self, value):
        """
        Set pdu_triggering and return self for chaining.

        Args:
            value: The pdu_triggering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu_triggering("value")
        """
        self.pdu_triggering = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPduTriggering(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for pduTriggering.

        Returns:
            The pduTriggering value

        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
