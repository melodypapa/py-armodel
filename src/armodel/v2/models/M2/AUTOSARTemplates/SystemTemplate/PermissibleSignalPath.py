from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SignalPathConstraint


class PermissibleSignalPath(SignalPathConstraint):
    """
    The PermissibleSignalPath describes the way a data element shall take in the
    topology. The path is described by ordered references to PhysicalChannels.
    If more than one PermissibleSignalPath is defined for the same
    signal/operation attributes, any of them can be chosen. Such a signal path
    can be a constraint for the communication matrix . This path describes that
    one data element should take path A (e.g. 1. CAN channel, 2. LIN channel)
    and not path B (1. CAN channel, FlexRay channel A). This has an effect on
    the frame generation and the frame path.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::PermissibleSignalPath

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 256, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The arguments of an operation that can take the way in the topology.
        self._operation: List["SwcToSwcOperation"] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation
        # The SwcToSwcSignal can be transmitted on one of these channels.
        self._physical: List["PhysicalChannel"] = []

    @property
    def physical(self) -> List["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical
        # The data element which can take the predefined way in.
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
