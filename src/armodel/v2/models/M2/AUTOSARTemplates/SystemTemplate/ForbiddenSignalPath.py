from typing import List


class ForbiddenSignalPath(SignalPathConstraint):
    """
    The ForbiddenSignalPath describes the physical channels which an element
    shall not take in the topology. Such a signal path can be a constraint for
    the communication matrix, because such a path has an effect on the frame
    generation and the frame path.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::ForbiddenSignalPath

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 255, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the operation arguments of one operation shall not take the
        # predefined way in the topology.
        self._operation: List["SwcToSwcOperation"] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation
        # The SwcToSwcSignal shall not be transmitted on one of physical channels.
        self._physical: List["PhysicalChannel"] = []

    @property
    def physical(self) -> List["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical
        # The data element which shall not take the predefined way topology.
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

    def getPhysical(self) -> List["PhysicalChannel"]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

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
