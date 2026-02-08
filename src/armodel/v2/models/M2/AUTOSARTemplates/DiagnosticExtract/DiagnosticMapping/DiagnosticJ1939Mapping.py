from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagnosticMapping,
)


class DiagnosticJ1939SpnMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to define a mapping between an SPN
    and a SystemSignal. The existence of a mapping means that neither the SPN
    nor the SystemSignal need to be updated if the relation between the two
    changes.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 267, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This additional reference has a supporting role in that it sending nodes of a
                # given SPN.
        # It is positively a given SPN is sent by more than one node.
        # the reference targets the Diagnostic semantics of the reference is bound to
                # that is in turn referenced by the.
        self._sendingNode: List["DiagnosticJ1939Node"] = []

    @property
    def sending_node(self) -> List["DiagnosticJ1939Node"]:
        """Get sendingNode (Pythonic accessor)."""
        return self._sendingNode
        # This reference goes to the SPN that shall be associated SystemSignal.
        self._spn: Optional["DiagnosticJ1939Spn"] = None

    @property
    def spn(self) -> Optional["DiagnosticJ1939Spn"]:
        """Get spn (Pythonic accessor)."""
        return self._spn

    @spn.setter
    def spn(self, value: Optional["DiagnosticJ1939Spn"]) -> None:
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

        if not isinstance(value, DiagnosticJ1939Spn):
            raise TypeError(
                f"spn must be DiagnosticJ1939Spn or None, got {type(value).__name__}"
            )
        self._spn = value
        # This reference goes to the SystemSignal that shall be an SPN.
        self._systemSignal: Optional["SystemSignal"] = None

    @property
    def system_signal(self) -> Optional["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["SystemSignal"]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSendingNode(self) -> List["DiagnosticJ1939Node"]:
        """
        AUTOSAR-compliant getter for sendingNode.

        Returns:
            The sendingNode value

        Note:
            Delegates to sending_node property (CODING_RULE_V2_00017)
        """
        return self.sending_node  # Delegates to property

    def getSpn(self) -> "DiagnosticJ1939Spn":
        """
        AUTOSAR-compliant getter for spn.

        Returns:
            The spn value

        Note:
            Delegates to spn property (CODING_RULE_V2_00017)
        """
        return self.spn  # Delegates to property

    def setSpn(self, value: "DiagnosticJ1939Spn") -> "DiagnosticJ1939SpnMapping":
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

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "DiagnosticJ1939SpnMapping":
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_spn(self, value: Optional["DiagnosticJ1939Spn"]) -> "DiagnosticJ1939SpnMapping":
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

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "DiagnosticJ1939SpnMapping":
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagnosticSwMapping,
)


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """
    This meta-class represents the ability to map a piece of application
    software to a J1939DiagnosticNode. By this means the diagnostic
    configuration can be associated with the application software.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping

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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagnosticMapping,
)


class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    """
    By means of this meta-class it is possible to associate a DiagnosticEvent to
    a DiagnosticTroubleCode J1939.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 269, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which a J1939 Code is assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to a J1939 Diagnostic Trouble Code to which a DiagnosticEvent is
        # assigned.
        self._troubleCode: Optional["DiagnosticTroubleCode"] = None

    @property
    def trouble_code(self) -> Optional["DiagnosticTroubleCode"]:
        """Get troubleCode (Pythonic accessor)."""
        return self._troubleCode

    @trouble_code.setter
    def trouble_code(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set troubleCode with validation.

        Args:
            value: The troubleCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._troubleCode = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"troubleCode must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._troubleCode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getTroubleCode(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for troubleCode.

        Returns:
            The troubleCode value

        Note:
            Delegates to trouble_code property (CODING_RULE_V2_00017)
        """
        return self.trouble_code  # Delegates to property

    def setTroubleCode(self, value: "DiagnosticTroubleCode") -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        AUTOSAR-compliant setter for troubleCode with method chaining.

        Args:
            value: The troubleCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to trouble_code property setter (gets validation automatically)
        """
        self.trouble_code = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_trouble_code(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        Set troubleCode and return self for chaining.

        Args:
            value: The troubleCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trouble_code("value")
        """
        self.trouble_code = value  # Use property setter (gets validation)
        return self
