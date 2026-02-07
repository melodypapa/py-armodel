from typing import Optional


class DiagnosticJ1939ExpandedFreezeFrame(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model an expanded J1939 Freeze
    Frame.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::J1939::DiagnosticJ1939ExpandedFreezeFrame

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 221, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the DiagnosticJ1939Node to which the freeze frame is
                # associated.
        # DiagnosticJ1939Spn * ref This represents the collection of SPNs that make the
                # Freeze Frame.
        self._node: Optional["DiagnosticJ1939Node"] = None

    @property
    def node(self) -> Optional["DiagnosticJ1939Node"]:
        """Get node (Pythonic accessor)."""
        return self._node

    @node.setter
    def node(self, value: Optional["DiagnosticJ1939Node"]) -> None:
        """
        Set node with validation.

        Args:
            value: The node to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._node = None
            return

        if not isinstance(value, DiagnosticJ1939Node):
            raise TypeError(
                f"node must be DiagnosticJ1939Node or None, got {type(value).__name__}"
            )
        self._node = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNode(self) -> "DiagnosticJ1939Node":
        """
        AUTOSAR-compliant getter for node.

        Returns:
            The node value

        Note:
            Delegates to node property (CODING_RULE_V2_00017)
        """
        return self.node  # Delegates to property

    def setNode(self, value: "DiagnosticJ1939Node") -> "DiagnosticJ1939ExpandedFreezeFrame":
        """
        AUTOSAR-compliant setter for node with method chaining.

        Args:
            value: The node to set

        Returns:
            self for method chaining

        Note:
            Delegates to node property setter (gets validation automatically)
        """
        self.node = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_node(self, value: Optional["DiagnosticJ1939Node"]) -> "DiagnosticJ1939ExpandedFreezeFrame":
        """
        Set node and return self for chaining.

        Args:
            value: The node to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_node("value")
        """
        self.node = value  # Use property setter (gets validation)
        return self
