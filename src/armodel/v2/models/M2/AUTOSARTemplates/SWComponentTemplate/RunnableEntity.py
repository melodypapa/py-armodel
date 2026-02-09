from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ExecutableEntity,
)

    RefType,
)


class RunnableEntity(ExecutableEntity):
    """
    A RunnableEntity represents the smallest code-fragment that is provided by
    an AtomicSwComponent Type and are executed under control of the RTE.
    RunnableEntities are for instance set up to respond to data reception or
    operation invocation on a server.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 331, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 524, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2050, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 240, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 461, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 203, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the formal definition of a an argument to a RunnableEntity.
        self._argument: List["RunnableEntity"] = []

    @property
    def argument(self) -> List["RunnableEntity"]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # The server call result point admits a runnable to fetch the result of an
                # asynchronous server call.
        # aggregation of AsynchronousServerCallResultPoint to variability with the
                # purpose to support the of client server PortPrototypes and existence of
                # server call result points in the atpVariation 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._asynchronous: List["AsynchronousServer"] = []

    @property
    def asynchronous(self) -> List["AsynchronousServer"]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous
        # If the value of this attribute is set to "true" the enclosing can be invoked
        # concurrently (even for one the corresponding AtomicSwComponent implies that
        # it is the responsibility of the the RunnableEntity to take care of this
        # concurrency.
        self._canBeInvoked: Optional["Boolean"] = None

    @property
    def can_be_invoked(self) -> Optional["Boolean"]:
        """Get canBeInvoked (Pythonic accessor)."""
        return self._canBeInvoked

    @can_be_invoked.setter
    def can_be_invoked(self, value: Optional["Boolean"]) -> None:
        """
        Set canBeInvoked with validation.

        Args:
            value: The canBeInvoked to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canBeInvoked = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"canBeInvoked must be Boolean or None, got {type(value).__name__}"
            )
        self._canBeInvoked = value
                # PortPrototype or nv data of a nv data of dataReadAccess is subject to the
                # purpose to support the conditional sender receiver ports or the variant
                # existence in the implementation.
        # atpVariation.
        self._dataRead: List["VariableAccess"] = []

    @property
    def data_read(self) -> List["VariableAccess"]:
        """Get dataRead (Pythonic accessor)."""
        return self._dataRead
        # RunnableEntity has explicit read access to dataElement a sender-receiver
                # PortPrototype or nv data of a nv data is passed back to the application by
                # means of value.
        # The aggregation of dataReceivePointBy subject to variability with the purpose
                # to support existence of sender receiver ports or the of data receive points
                # in the atpVariation 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._dataReceive: List["VariableAccess"] = []

    @property
    def data_receive(self) -> List["VariableAccess"]:
        """Get dataReceive (Pythonic accessor)."""
        return self._dataReceive
        # RunnableEntity has explicit write access to dataElement sender-receiver
                # PortPrototype or nv data of a nv data of dataSendPoint is subject to
                # variability purpose to support the conditional existence of PortPrototype or
                # the variant existence of points in the implementation.
        # atpVariation.
        self._dataSendPoint: List["VariableAccess"] = []

    @property
    def data_send_point(self) -> List["VariableAccess"]:
        """Get dataSendPoint (Pythonic accessor)."""
        return self._dataSendPoint
        # RunnableEntity has implicit write access to dataElement a sender-receiver
                # PortPrototype or nv data of a nv data of dataWriteAccess is subject to the
                # purpose to support the conditional sender receiver ports or the variant
                # existence in the implementation.
        # atpVariation.
        self._dataWrite: List["VariableAccess"] = []

    @property
    def data_write(self) -> List["VariableAccess"]:
        """Get dataWrite (Pythonic accessor)."""
        return self._dataWrite
        # The aggregation of ExternalTriggeringPoint is subject to with the purpose to
                # support the conditional trigger ports or the variant existence of points in
                # the implementation.
        # atpVariation.
        self._external: List[RefType] = []

    @property
    def external(self) -> List[RefType]:
        """Get external (Pythonic accessor)."""
        return self._external
        # The aggregation of InternalTriggeringPoint is subject to with the purpose to
        # support the variant internal triggering points in the atpVariation.
        self._internal: List[RefType] = []

    @property
    def internal(self) -> List[RefType]:
        """Get internal (Pythonic accessor)."""
        return self._internal
        # The runnable has a mode access point.
        # The aggregation ModeAccessPoint is subject to variability with the support
                # the conditional existence of mode the variant existence of mode access points
                # in atpVariation 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._modeAccess: List["ModeAccessPoint"] = []

    @property
    def mode_access(self) -> List["ModeAccessPoint"]:
        """Get modeAccess (Pythonic accessor)."""
        return self._modeAccess
        # The runnable has a mode switch point.
        # The aggregation ModeSwitchPoint is subject to variability with the support
                # the conditional existence of mode the variant existence of mode switch points
                # in the atpVariation.
        self._modeSwitch: List["ModeSwitchPoint"] = []

    @property
    def mode_switch(self) -> List["ModeSwitchPoint"]:
        """Get modeSwitch (Pythonic accessor)."""
        return self._modeSwitch
        # The presence of a ParameterAccess implies that a needs read only access to a
                # Parameter may either be local or within a Port of ParameterAccess is subject
                # to the purpose to support the conditional parameter ports and component local
                # well as the variant existence of Parameter in the implementation.
        # atpVariation.
        self._parameter: List["ParameterAccess"] = []

    @property
    def parameter(self) -> List["ParameterAccess"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter
        # The presence of a readLocalVariable implies that a needs read access to a
                # VariableData the role of implicitInterRunnableVariable or of
                # readLocalVariable is subject to the purpose to support the conditional
                # implicitInterRunnableVariable and explicit the variant existence of read in
                # the implementation.
        # atpVariation.
        self._readLocal: List["VariableAccess"] = []

    @property
    def read_local(self) -> List["VariableAccess"]:
        """Get readLocal (Pythonic accessor)."""
        return self._readLocal
        # The RunnableEntity has a ServerCallPoint.
        # The ServerCallPoint is subject to variability with to support the conditional
                # existence of client or the variant existence of server in the implementation.
        # atpVariation.
        self._serverCallPoint: List["ServerCallPoint"] = []

    @property
    def server_call_point(self) -> List["ServerCallPoint"]:
        """Get serverCallPoint (Pythonic accessor)."""
        return self._serverCallPoint
        # The symbol describing this RunnableEntity’s entry point.
        # considered the API of the RunnableEntity and is the RTE contract phase.
        self._symbol: Optional["CIdentifier"] = None

    @property
    def symbol(self) -> Optional["CIdentifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["CIdentifier"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"symbol must be CIdentifier or None, got {type(value).__name__}"
            )
        self._symbol = value
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._waitPoint: List["WaitPoint"] = []

    @property
    def wait_point(self) -> List["WaitPoint"]:
        """Get waitPoint (Pythonic accessor)."""
        return self._waitPoint
        # The presence of a writtenLocalVariable implies that a needs write access to a
                # VariableData the role of implicitInterRunnableVariable or of
                # writtenLocalVariable is subject to the purpose to support the conditional
                # implicitInterRunnableVariable and explicit the variant existence of written
                # in the implementation.
        # atpVariation.
        self._writtenLocal: List["VariableAccess"] = []

    @property
    def written_local(self) -> List["VariableAccess"]:
        """Get writtenLocal (Pythonic accessor)."""
        return self._writtenLocal

    def with_argument(self, value):
        """
        Set argument and return self for chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_asynchronous(self, value):
        """
        Set asynchronous and return self for chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_asynchronous("value")
        """
        self.asynchronous = value  # Use property setter (gets validation)
        return self

    def with_data_read(self, value):
        """
        Set data_read and return self for chaining.

        Args:
            value: The data_read to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_read("value")
        """
        self.data_read = value  # Use property setter (gets validation)
        return self

    def with_data_receive(self, value):
        """
        Set data_receive and return self for chaining.

        Args:
            value: The data_receive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_receive("value")
        """
        self.data_receive = value  # Use property setter (gets validation)
        return self

    def with_data_send_point(self, value):
        """
        Set data_send_point and return self for chaining.

        Args:
            value: The data_send_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_send_point("value")
        """
        self.data_send_point = value  # Use property setter (gets validation)
        return self

    def with_data_write(self, value):
        """
        Set data_write and return self for chaining.

        Args:
            value: The data_write to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_write("value")
        """
        self.data_write = value  # Use property setter (gets validation)
        return self

    def with_external(self, value):
        """
        Set external and return self for chaining.

        Args:
            value: The external to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_external("value")
        """
        self.external = value  # Use property setter (gets validation)
        return self

    def with_internal(self, value):
        """
        Set internal and return self for chaining.

        Args:
            value: The internal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal("value")
        """
        self.internal = value  # Use property setter (gets validation)
        return self

    def with_mode_access(self, value):
        """
        Set mode_access and return self for chaining.

        Args:
            value: The mode_access to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_access("value")
        """
        self.mode_access = value  # Use property setter (gets validation)
        return self

    def with_mode_switch(self, value):
        """
        Set mode_switch and return self for chaining.

        Args:
            value: The mode_switch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_switch("value")
        """
        self.mode_switch = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value):
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self

    def with_read_local(self, value):
        """
        Set read_local and return self for chaining.

        Args:
            value: The read_local to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_read_local("value")
        """
        self.read_local = value  # Use property setter (gets validation)
        return self

    def with_server_call_point(self, value):
        """
        Set server_call_point and return self for chaining.

        Args:
            value: The server_call_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_server_call_point("value")
        """
        self.server_call_point = value  # Use property setter (gets validation)
        return self

    def with_wait_point(self, value):
        """
        Set wait_point and return self for chaining.

        Args:
            value: The wait_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wait_point("value")
        """
        self.wait_point = value  # Use property setter (gets validation)
        return self

    def with_written_local(self, value):
        """
        Set written_local and return self for chaining.

        Args:
            value: The written_local to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_written_local("value")
        """
        self.written_local = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List["RunnableEntity"]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getAsynchronous(self) -> List["AsynchronousServer"]:
        """
        AUTOSAR-compliant getter for asynchronous.

        Returns:
            The asynchronous value

        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def getCanBeInvoked(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for canBeInvoked.

        Returns:
            The canBeInvoked value

        Note:
            Delegates to can_be_invoked property (CODING_RULE_V2_00017)
        """
        return self.can_be_invoked  # Delegates to property

    def setCanBeInvoked(self, value: "Boolean") -> "RunnableEntity":
        """
        AUTOSAR-compliant setter for canBeInvoked with method chaining.

        Args:
            value: The canBeInvoked to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_be_invoked property setter (gets validation automatically)
        """
        self.can_be_invoked = value  # Delegates to property setter
        return self

    def getDataRead(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for dataRead.

        Returns:
            The dataRead value

        Note:
            Delegates to data_read property (CODING_RULE_V2_00017)
        """
        return self.data_read  # Delegates to property

    def getDataReceive(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for dataReceive.

        Returns:
            The dataReceive value

        Note:
            Delegates to data_receive property (CODING_RULE_V2_00017)
        """
        return self.data_receive  # Delegates to property

    def getDataSendPoint(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for dataSendPoint.

        Returns:
            The dataSendPoint value

        Note:
            Delegates to data_send_point property (CODING_RULE_V2_00017)
        """
        return self.data_send_point  # Delegates to property

    def getDataWrite(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for dataWrite.

        Returns:
            The dataWrite value

        Note:
            Delegates to data_write property (CODING_RULE_V2_00017)
        """
        return self.data_write  # Delegates to property

    def getExternal(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for external.

        Returns:
            The external value

        Note:
            Delegates to external property (CODING_RULE_V2_00017)
        """
        return self.external  # Delegates to property

    def getInternal(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for internal.

        Returns:
            The internal value

        Note:
            Delegates to internal property (CODING_RULE_V2_00017)
        """
        return self.internal  # Delegates to property

    def getModeAccess(self) -> List["ModeAccessPoint"]:
        """
        AUTOSAR-compliant getter for modeAccess.

        Returns:
            The modeAccess value

        Note:
            Delegates to mode_access property (CODING_RULE_V2_00017)
        """
        return self.mode_access  # Delegates to property

    def getModeSwitch(self) -> List["ModeSwitchPoint"]:
        """
        AUTOSAR-compliant getter for modeSwitch.

        Returns:
            The modeSwitch value

        Note:
            Delegates to mode_switch property (CODING_RULE_V2_00017)
        """
        return self.mode_switch  # Delegates to property

    def getParameter(self) -> List["ParameterAccess"]:
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def getReadLocal(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for readLocal.

        Returns:
            The readLocal value

        Note:
            Delegates to read_local property (CODING_RULE_V2_00017)
        """
        return self.read_local  # Delegates to property

    def getServerCallPoint(self) -> List["ServerCallPoint"]:
        """
        AUTOSAR-compliant getter for serverCallPoint.

        Returns:
            The serverCallPoint value

        Note:
            Delegates to server_call_point property (CODING_RULE_V2_00017)
        """
        return self.server_call_point  # Delegates to property

    def getSymbol(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "CIdentifier") -> "RunnableEntity":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    def getWaitPoint(self) -> List["WaitPoint"]:
        """
        AUTOSAR-compliant getter for waitPoint.

        Returns:
            The waitPoint value

        Note:
            Delegates to wait_point property (CODING_RULE_V2_00017)
        """
        return self.wait_point  # Delegates to property

    def getWrittenLocal(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for writtenLocal.

        Returns:
            The writtenLocal value

        Note:
            Delegates to written_local property (CODING_RULE_V2_00017)
        """
        return self.written_local  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_be_invoked(self, value: Optional["Boolean"]) -> "RunnableEntity":
        """
        Set canBeInvoked and return self for chaining.

        Args:
            value: The canBeInvoked to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_be_invoked("value")
        """
        self.can_be_invoked = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["CIdentifier"]) -> "RunnableEntity":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self
