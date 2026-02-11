"""
AUTOSAR Package - SignalPaths

Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.MSR.Documentation.BlockElements import (
    DocumentationBlock,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerOperation,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PhysicalChannel,
)


class SwcToSwcSignal(ARObject):
    """
    The SwcToSwcSignal describes the information (data element) that is
    exchanged between two SW Components. On the SWC Level it is possible that a
    SW Component sends one data element from one P-Port to two different SW
    Components (1:n Communication). The SwcToSwcSignal describes exactly the
    information which is exchanged between one P-Port of a SW Component and one
    R-Port of another SW Component.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::SwcToSwcSignal

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # same data element on the RPortPrototype.
        # by: VariableDataPrototypeIn.
        self._dataElement: List[RefType] = []
        self._operation: Optional[ClientServerOperation] = None
        self._signal: Optional["SwcToSwcSignal"] = None
        self._physical: Optional[PhysicalChannel] = None

    @property
    def data_element(self) -> List[RefType]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: List[RefType]) -> None:
        """
        Set data_element with validation.

        Args:
            value: The data_element to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, list):
            raise TypeError(
                f"data_element must be a list, got {type(value).__name__}"
            )
        self._dataElement = value

    @property
    def operation(self) -> Optional[ClientServerOperation]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional[ClientServerOperation]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value

    @property
    def signal(self) -> Optional["SwcToSwcSignal"]:
        """Get signal (Pythonic accessor)."""
        return self._signal

    @signal.setter
    def signal(self, value: Optional["SwcToSwcSignal"]) -> None:
        """
        Set signal with validation.

        Args:
            value: The signal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signal = None
            return

        if not isinstance(value, SwcToSwcSignal):
            raise TypeError(
                f"signal must be SwcToSwcSignal or None, got {type(value).__name__}"
            )
        self._signal = value

    @property
    def physical(self) -> Optional[PhysicalChannel]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional[PhysicalChannel]) -> None:
        """
        Set physical with validation.

        Args:
            value: The physical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"physical must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._physical = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: List[RefType]) -> "SwcToSwcSignal":
        """
        Set data_element and return self for chaining.

        Args:
            value: The data_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_operation(self, value: Optional[ClientServerOperation]) -> "SwcToSwcSignal":
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_signal(self, value: Optional["SwcToSwcSignal"]) -> "SwcToSwcSignal":
        """
        Set signal and return self for chaining.

        Args:
            value: The signal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal("value")
        """
        self.signal = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value: Optional[PhysicalChannel]) -> "SwcToSwcSignal":
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwcToSwcOperationArguments(ARObject):
    """
    The SwcToSwcOperationArguments describes the information (client server
    operation arguments, plus the operation identification, if required) that
    are exchanged between two SW Components from exactly one client to one
    server, or from one server back to one client. The direction attribute
    defines which direction is described. If direction == IN, all arguments sent
    from the client to the server are described by the
    SwcToSwcOperationArguments, in direction == OUT, it's the arguments sent
    back from server to client.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::SwcToSwcOperationArguments

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Direction addressed by this SwcToSwcClientServer element.
        self._direction: Optional["SwcToSwcOperationArgumentsDirectionEnum"] = None
        # in the software component by: OperationInSystem.
        self._operation: List[ClientServerOperation] = []

    @property
    def direction(self) -> Optional["SwcToSwcOperationArgumentsDirectionEnum"]:
        """Get direction (Pythonic accessor)."""
        return self._direction

    @direction.setter
    def direction(self, value: Optional["SwcToSwcOperationArgumentsDirectionEnum"]) -> None:
        """
        Set direction with validation.

        Args:
            value: The direction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._direction = None
            return

        if not isinstance(value, SwcToSwcOperationArgumentsDirectionEnum):
            raise TypeError(
                f"direction must be SwcToSwcOperationArgumentsDirectionEnum or None, got {type(value).__name__}"
            )
        self._direction = value

    @property
    def operation(self) -> List[ClientServerOperation]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: List[ClientServerOperation]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, list):
            raise TypeError(
                f"operation must be a list, got {type(value).__name__}"
            )
        self._operation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirection(self) -> Optional["SwcToSwcOperationArgumentsDirectionEnum"]:
        """
        AUTOSAR-compliant getter for direction.

        Returns:
            The direction value

        Note:
            Delegates to direction property (CODING_RULE_V2_00017)
        """
        return self.direction  # Delegates to property

    def setDirection(self, value: Optional["SwcToSwcOperationArgumentsDirectionEnum"]) -> "SwcToSwcOperationArguments":
        """
        AUTOSAR-compliant setter for direction with method chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Note:
            Delegates to direction property setter (gets validation automatically)
        """
        self.direction = value  # Delegates to property setter
        return self

    def getOperation(self) -> List[ClientServerOperation]:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direction(self, value: Optional["SwcToSwcOperationArgumentsDirectionEnum"]) -> "SwcToSwcOperationArguments":
        """
        Set direction and return self for chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direction("value")
        """
        self.direction = value  # Use property setter (gets validation)
        return self



class SignalPathConstraint(ARObject, ABC):
    """
    Additional guidelines for the System Generator, which specific way a signal
    between two Software Components should take in the network without defining
    in which frame and with which timing it is transmitted.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::SignalPathConstraint

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2057, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is SignalPathConstraint:
            raise TypeError("SignalPathConstraint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the constraint.
        self._introduction: Optional[DocumentationBlock] = None

    @property
    def introduction(self) -> Optional[DocumentationBlock]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> "SignalPathConstraint":
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "SignalPathConstraint":
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self



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
        # The SwcToSwcSignals that shall take the same way in the topology.
        self._signal: List[SwcToSwcSignal] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @property
    def signal(self) -> List[SwcToSwcSignal]:
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

    def getSignal(self) -> List[SwcToSwcSignal]:
        """
        AUTOSAR-compliant getter for signal.

        Returns:
            The signal value

        Note:
            Delegates to signal property (CODING_RULE_V2_00017)
        """
        return self.signal  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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
        # The SwcToSwcSignal shall not be transmitted on one of physical channels.
        self._physical: List[PhysicalChannel] = []
        # The data element which shall not take the predefined way topology.
        self._signal: List[SwcToSwcSignal] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @property
    def physical(self) -> List[PhysicalChannel]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @property
    def signal(self) -> List[SwcToSwcSignal]:
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

    def getPhysical(self) -> List[PhysicalChannel]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def getSignal(self) -> List[SwcToSwcSignal]:
        """
        AUTOSAR-compliant getter for signal.

        Returns:
            The signal value

        Note:
            Delegates to signal property (CODING_RULE_V2_00017)
        """
        return self.signal  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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
        # The SwcToSwcSignal can be transmitted on one of these channels.
        self._physical: List[PhysicalChannel] = []
        # The data element which can take the predefined way in.
        self._signal: List[SwcToSwcSignal] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @property
    def physical(self) -> List[PhysicalChannel]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @property
    def signal(self) -> List[SwcToSwcSignal]:
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

    def getPhysical(self) -> List[PhysicalChannel]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def getSignal(self) -> List[SwcToSwcSignal]:
        """
        AUTOSAR-compliant getter for signal.

        Returns:
            The signal value

        Note:
            Delegates to signal property (CODING_RULE_V2_00017)
        """
        return self.signal  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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
        # The SwcToSwcSignals that shall not take the same way in the topology.
        self._signal: List[SwcToSwcSignal] = []

    @property
    def operation(self) -> List["SwcToSwcOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @property
    def signal(self) -> List[SwcToSwcSignal]:
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

    def getSignal(self) -> List[SwcToSwcSignal]:
        """
        AUTOSAR-compliant getter for signal.

        Returns:
            The signal value

        Note:
            Delegates to signal property (CODING_RULE_V2_00017)
        """
        return self.signal  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class SwcToSwcOperationArgumentsDirectionEnum(AREnum):
    """
    SwcToSwcOperationArgumentsDirectionEnum enumeration

Direction addressed by this element. Aggregated by SwcToSwcOperationArguments.direction

Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths
    """

    def __init__(self) -> None:
        super().__init__([
            SwcToSwcOperationArgumentsDirectionEnum.in_,
            SwcToSwcOperationArgumentsDirectionEnum.out,
        ])

    # IN (all IN and INOUT arguments)
    # Note: 'in' is a Python keyword, so we use 'in_' instead
    in_ = "0"

    # OUT (all OUT and INOUT arguments) .
    out = "1"
