from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticComControlSubNodeChannel(ARObject):
    """
    This represents the ability to add further attributes to the definition of a
    specific sub-node channel that is subject to the diagnostic service
    "communication control".

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 110, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the affected sub-node EthernetPhysical Channel.
        self._subNode: Optional["EthernetPhysical"] = None

    @property
    def sub_node(self) -> Optional["EthernetPhysical"]:
        """Get subNode (Pythonic accessor)."""
        return self._subNode

    @sub_node.setter
    def sub_node(self, value: Optional["EthernetPhysical"]) -> None:
        """
        Set subNode with validation.

        Args:
            value: The subNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subNode = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"subNode must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._subNode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSubNode(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for subNode.

        Returns:
            The subNode value

        Note:
            Delegates to sub_node property (CODING_RULE_V2_00017)
        """
        return self.sub_node  # Delegates to property

    def setSubNode(self, value: "EthernetPhysical") -> "DiagnosticComControlSubNodeChannel":
        """
        AUTOSAR-compliant setter for subNode with method chaining.

        Args:
            value: The subNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub_node property setter (gets validation automatically)
        """
        self.sub_node = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sub_node(self, value: Optional["EthernetPhysical"]) -> "DiagnosticComControlSubNodeChannel":
        """
        Set subNode and return self for chaining.

        Args:
            value: The subNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_node("value")
        """
        self.sub_node = value  # Use property setter (gets validation)
        return self
