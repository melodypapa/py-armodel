from typing import List


class CommonSignalPath(SignalPathConstraint):
    """
    The CommonSignalPath describes that two or more SwcToSwcSignals and/or
    SwcToSwcOperation Arguments shall take the same way (Signal Path) in the
    topology.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::CommonSignalPath

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The arguments sent in one direction (either from client to or server to
        # client) of the operations that shall take signal path.
        self._operation: List["SwcToSwcOperation"] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation
        # The SwcToSwcSignals that shall take the same way in the topology.
        self._signal: List["SwcToSwcSignal"] = []

    @property
    def signal(self) -> List["SwcToSwcSignal"]:
        """Get signal (Pythonic accessor)."""
        return self._signal

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> List["SwcToSwcOperation"]:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def getSignal(self) -> List["SwcToSwcSignal"]:
        """
        AUTOSAR-compliant getter for signal.

        Returns:
            The signal value

        Note:
            Delegates to signal property (CODING_RULE_V2_00017)
        """
        return self.signal  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
