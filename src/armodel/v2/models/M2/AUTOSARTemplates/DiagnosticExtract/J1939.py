"""
AUTOSAR Package - J1939

Package: M2::AUTOSARTemplates::DiagnosticExtract::J1939
"""


from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a J1939 Suspect Parameter
    Number (SPN).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::J1939::DiagnosticJ1939Spn

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 219, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the concrete numerical the enclosing SPN.
        self._spn: Optional["PositiveInteger"] = None

    @property
    def spn(self) -> Optional["PositiveInteger"]:
        """Get spn (Pythonic accessor)."""
        return self._spn

    @spn.setter
    def spn(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set spn with validation.

        Args:
            value: The spn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._spn = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"spn must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._spn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSpn(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for spn.

        Returns:
            The spn value

        Note:
            Delegates to spn property (CODING_RULE_V2_00017)
        """
        return self.spn  # Delegates to property

    def setSpn(self, value: "PositiveInteger") -> DiagnosticJ1939Spn:
        """
        AUTOSAR-compliant setter for spn with method chaining.

        Args:
            value: The spn to set

        Returns:
            self for method chaining

        Note:
            Delegates to spn property setter (gets validation automatically)
        """
        self.spn = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_spn(self, value: Optional["PositiveInteger"]) -> DiagnosticJ1939Spn:
        """
        Set spn and return self for chaining.

        Args:
            value: The spn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_spn("value")
        """
        self.spn = value  # Use property setter (gets validation)
        return self



class DiagnosticJ1939FreezeFrame(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a J1939 Freeze Frame.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::J1939::DiagnosticJ1939FreezeFrame

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 220, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the DiagnosticJ1939Node to which the frame is associated.
        # DiagnosticJ1939Spn * ref This represents the collection of SPNs that make the
                # Frame.
        self._node: Optional[DiagnosticJ1939Node] = None

    @property
    def node(self) -> Optional[DiagnosticJ1939Node]:
        """Get node (Pythonic accessor)."""
        return self._node

    @node.setter
    def node(self, value: Optional[DiagnosticJ1939Node]) -> None:
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

    def getNode(self) -> DiagnosticJ1939Node:
        """
        AUTOSAR-compliant getter for node.

        Returns:
            The node value

        Note:
            Delegates to node property (CODING_RULE_V2_00017)
        """
        return self.node  # Delegates to property

    def setNode(self, value: DiagnosticJ1939Node) -> DiagnosticJ1939FreezeFrame:
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

    def with_node(self, value: Optional[DiagnosticJ1939Node]) -> DiagnosticJ1939FreezeFrame:
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
        self._node: Optional[DiagnosticJ1939Node] = None

    @property
    def node(self) -> Optional[DiagnosticJ1939Node]:
        """Get node (Pythonic accessor)."""
        return self._node

    @node.setter
    def node(self, value: Optional[DiagnosticJ1939Node]) -> None:
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

    def getNode(self) -> DiagnosticJ1939Node:
        """
        AUTOSAR-compliant getter for node.

        Returns:
            The node value

        Note:
            Delegates to node property (CODING_RULE_V2_00017)
        """
        return self.node  # Delegates to property

    def setNode(self, value: DiagnosticJ1939Node) -> DiagnosticJ1939ExpandedFreezeFrame:
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

    def with_node(self, value: Optional[DiagnosticJ1939Node]) -> DiagnosticJ1939ExpandedFreezeFrame:
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

    def setNmNode(self, value: "J1939NmNode") -> DiagnosticJ1939Node:
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

    def with_nm_node(self, value: Optional["J1939NmNode"]) -> DiagnosticJ1939Node:
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
