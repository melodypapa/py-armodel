from typing import Optional


class DiagnosticJ1939Node(DiagnosticCommonElement):
    """
    This meta-class represents the diagnostic configuration of a J1939 Nm node,
    which in turn represents a "virtual Ecu" on the J1939 communication bus.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::J1939::DiagnosticJ1939Node

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 267, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the reference to the "virtual Ecu" to which
        # DiagnosticJ1939Node is associated.
        self._nmNode: Optional["J1939NmNode"] = None

    @property
    def nm_node(self) -> Optional["J1939NmNode"]:
        """Get nmNode (Pythonic accessor)."""
        return self._nmNode

    @nm_node.setter
    def nm_node(self, value: Optional["J1939NmNode"]) -> None:
        """
        Set nmNode with validation.

        Args:
            value: The nmNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNode = None
            return

        if not isinstance(value, J1939NmNode):
            raise TypeError(
                f"nmNode must be J1939NmNode or None, got {type(value).__name__}"
            )
        self._nmNode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmNode(self) -> "J1939NmNode":
        """
        AUTOSAR-compliant getter for nmNode.

        Returns:
            The nmNode value

        Note:
            Delegates to nm_node property (CODING_RULE_V2_00017)
        """
        return self.nm_node  # Delegates to property

    def setNmNode(self, value: "J1939NmNode") -> "DiagnosticJ1939Node":
        """
        AUTOSAR-compliant setter for nmNode with method chaining.

        Args:
            value: The nmNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_node property setter (gets validation automatically)
        """
        self.nm_node = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_node(self, value: Optional["J1939NmNode"]) -> "DiagnosticJ1939Node":
        """
        Set nmNode and return self for chaining.

        Args:
            value: The nmNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_node("value")
        """
        self.nm_node = value  # Use property setter (gets validation)
        return self
