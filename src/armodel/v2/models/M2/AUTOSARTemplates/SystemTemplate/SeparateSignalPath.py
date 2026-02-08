from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SignalPathConstraint


class SeparateSignalPath(SignalPathConstraint):
    """
    The SeparateSignalPath describes that two SwcToSwcSignals and/or
    SwcToSwcOperationArguments shall not take the same way (Signal Path) in the
    topology (e.g. Redundancy). This means that the signals are not allowed to
    share even a single physical channel in their path.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::SeparateSignalPath

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 257, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The SwcToSwcOperationArguments that shall not take same way (Signal Path) in
        # the topology.
        self._operation: List["SwcToSwcOperation"] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation
        # The SwcToSwcSignals that shall not take the same way in the topology.
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
