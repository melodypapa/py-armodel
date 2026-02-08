from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

    RefType,
)


class PdurIPduGroup(FibexElement):
    """
    The AUTOSAR PduR will enable and disable the sending of configurable groups
    of IPdus during runtime according to the AUTOSAR PduR specification.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 352, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the use-case for this PduRIPdu For example, in a
                # diagnostic mode all IPdus - not involved in diagnostic - are disabled.
        # The are not limited to a fixed enumeration and can as a string.
        self._communication: Optional["String"] = None

    @property
    def communication(self) -> Optional["String"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["String"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"communication must be String or None, got {type(value).__name__}"
            )
        self._communication = value
        # Reference to a set of IPdus, which are contained in the Group.
        # If an IPdu is routed by the PduR to (PduR fan-out) than an Pdu each
                # destination is created in the System enable/disable a specific destination
                # the to the PduTriggering.
        # content of a PduR I-Pdu group can vary atpVariation.
        self._iPdu: List[RefType] = []

    @property
    def i_pdu(self) -> List[RefType]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "String":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "String") -> "PdurIPduGroup":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getIPdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for iPdu.

        Returns:
            The iPdu value

        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["String"]) -> "PdurIPduGroup":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self
