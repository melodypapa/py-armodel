from typing import Optional


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """
    This meta-class represents the ability to map a piece of application
    software to a J1939DiagnosticNode. By this means the diagnostic
    configuration can be associated with the application software.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping::DiagnosticJ1939SwMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 268, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the mapped DiagnosticJ1939Node.
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
        # InstanceRef implemented by: ComponentIn.
        self._swComponentCompositionInstanceRef: Optional["SwComponent"] = None

    @property
    def sw_component_composition_instance_ref(self) -> Optional["SwComponent"]:
        """Get swComponentCompositionInstanceRef (Pythonic accessor)."""
        return self._swComponentCompositionInstanceRef

    @sw_component_composition_instance_ref.setter
    def sw_component_composition_instance_ref(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponentCompositionInstanceRef with validation.

        Args:
            value: The swComponentCompositionInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponentCompositionInstanceRef = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponentCompositionInstanceRef must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponentCompositionInstanceRef = value

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

    def setNode(self, value: "DiagnosticJ1939Node") -> "DiagnosticJ1939SwMapping":
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

    def getSwComponentCompositionInstanceRef(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponentCompositionInstanceRef.

        Returns:
            The swComponentCompositionInstanceRef value

        Note:
            Delegates to sw_component_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.sw_component_composition_instance_ref  # Delegates to property

    def setSwComponentCompositionInstanceRef(self, value: "SwComponent") -> "DiagnosticJ1939SwMapping":
        """
        AUTOSAR-compliant setter for swComponentCompositionInstanceRef with method chaining.

        Args:
            value: The swComponentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_component_composition_instance_ref property setter (gets validation automatically)
        """
        self.sw_component_composition_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_node(self, value: Optional["DiagnosticJ1939Node"]) -> "DiagnosticJ1939SwMapping":
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

    def with_sw_component_composition_instance_ref(self, value: Optional["SwComponent"]) -> "DiagnosticJ1939SwMapping":
        """
        Set swComponentCompositionInstanceRef and return self for chaining.

        Args:
            value: The swComponentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_component_composition_instance_ref("value")
        """
        self.sw_component_composition_instance_ref = value  # Use property setter (gets validation)
        return self
