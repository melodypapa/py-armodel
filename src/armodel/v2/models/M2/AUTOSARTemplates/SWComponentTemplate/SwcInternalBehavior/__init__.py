"""
AUTOSAR Package - SwcInternalBehavior

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior
"""


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ExecutableEntity,
    InternalBehavior,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)


class RunnableEntity(ExecutableEntity):
    """
    A RunnableEntity represents the smallest code-fragment that is provided by
    an AtomicSwComponent Type and are executed under control of the RTE.
    RunnableEntities are for instance set up to respond to data reception or
    operation invocation on a server.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RunnableEntity

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
        self._argument: List[RunnableEntity] = []

    @property
    def argument(self) -> List[RunnableEntity]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # The server call result point admits a runnable to fetch the result of an
                # asynchronous server call.
        # aggregation of AsynchronousServerCallResultPoint to variability with the
                # purpose to support the of client server PortPrototypes and existence of
                # server call result points in the atpVariation 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._asynchronous: List[AsynchronousServer] = []

    @property
    def asynchronous(self) -> List[AsynchronousServer]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous
        # If the value of this attribute is set to "true" the enclosing can be invoked
        # concurrently (even for one the corresponding AtomicSwComponent implies that
        # it is the responsibility of the the RunnableEntity to take care of this
        # concurrency.
        self._canBeInvoked: Optional[Boolean] = None

    @property
    def can_be_invoked(self) -> Optional[Boolean]:
        """Get canBeInvoked (Pythonic accessor)."""
        return self._canBeInvoked

    @can_be_invoked.setter
    def can_be_invoked(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"canBeInvoked must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._canBeInvoked = value
        # RunnableEntity has implicit read access to dataElement a sender-receiver
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
        self._serverCallPoint: List[ServerCallPoint] = []

    @property
    def server_call_point(self) -> List[ServerCallPoint]:
        """Get serverCallPoint (Pythonic accessor)."""
        return self._serverCallPoint
        # The symbol describing this RunnableEntity’s entry point.
        # considered the API of the RunnableEntity and is the RTE contract phase.
        self._symbol: Optional[CIdentifier] = None

    @property
    def symbol(self) -> Optional[CIdentifier]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional[CIdentifier]) -> None:
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
        # The WaitPoint associated with the RunnableEntity.
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

    def with_ar_typed_per(self, value):
        """
        Set ar_typed_per and return self for chaining.

        Args:
            value: The ar_typed_per to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ar_typed_per("value")
        """
        self.ar_typed_per = value  # Use property setter (gets validation)
        return self

    def with_event(self, value):
        """
        Set event and return self for chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_explicit_inter(self, value):
        """
        Set explicit_inter and return self for chaining.

        Args:
            value: The explicit_inter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_explicit_inter("value")
        """
        self.explicit_inter = value  # Use property setter (gets validation)
        return self

    def with_implicit_inter(self, value):
        """
        Set implicit_inter and return self for chaining.

        Args:
            value: The implicit_inter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implicit_inter("value")
        """
        self.implicit_inter = value  # Use property setter (gets validation)
        return self

    def with_included_data(self, value):
        """
        Set included_data and return self for chaining.

        Args:
            value: The included_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_included_data("value")
        """
        self.included_data = value  # Use property setter (gets validation)
        return self

    def with_included_mode(self, value):
        """
        Set included_mode and return self for chaining.

        Args:
            value: The included_mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_included_mode("value")
        """
        self.included_mode = value  # Use property setter (gets validation)
        return self

    def with_instantiation(self, value):
        """
        Set instantiation and return self for chaining.

        Args:
            value: The instantiation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_instantiation("value")
        """
        self.instantiation = value  # Use property setter (gets validation)
        return self

    def with_per_instance(self, value):
        """
        Set per_instance and return self for chaining.

        Args:
            value: The per_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_per_instance("value")
        """
        self.per_instance = value  # Use property setter (gets validation)
        return self

    def with_port_api_option(self, value):
        """
        Set port_api_option and return self for chaining.

        Args:
            value: The port_api_option to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_api_option("value")
        """
        self.port_api_option = value  # Use property setter (gets validation)
        return self

    def with_runnable(self, value):
        """
        Set runnable and return self for chaining.

        Args:
            value: The runnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_runnable("value")
        """
        self.runnable = value  # Use property setter (gets validation)
        return self

    def with_service(self, value):
        """
        Set service and return self for chaining.

        Args:
            value: The service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service("value")
        """
        self.service = value  # Use property setter (gets validation)
        return self

    def with_shared(self, value):
        """
        Set shared and return self for chaining.

        Args:
            value: The shared to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_shared("value")
        """
        self.shared = value  # Use property setter (gets validation)
        return self

    def with_variation_point(self, value):
        """
        Set variation_point and return self for chaining.

        Args:
            value: The variation_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variation_point("value")
        """
        self.variation_point = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List[RunnableEntity]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getAsynchronous(self) -> List[AsynchronousServer]:
        """
        AUTOSAR-compliant getter for asynchronous.

        Returns:
            The asynchronous value

        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def getCanBeInvoked(self) -> Boolean:
        """
        AUTOSAR-compliant getter for canBeInvoked.

        Returns:
            The canBeInvoked value

        Note:
            Delegates to can_be_invoked property (CODING_RULE_V2_00017)
        """
        return self.can_be_invoked  # Delegates to property

    def setCanBeInvoked(self, value: Boolean) -> RunnableEntity:
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

    def getServerCallPoint(self) -> List[ServerCallPoint]:
        """
        AUTOSAR-compliant getter for serverCallPoint.

        Returns:
            The serverCallPoint value

        Note:
            Delegates to server_call_point property (CODING_RULE_V2_00017)
        """
        return self.server_call_point  # Delegates to property

    def getSymbol(self) -> CIdentifier:
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: CIdentifier) -> RunnableEntity:
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

    def with_can_be_invoked(self, value: Optional[Boolean]) -> RunnableEntity:
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

    def with_symbol(self, value: Optional[CIdentifier]) -> RunnableEntity:
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



class SwcInternalBehavior(InternalBehavior):
    """
    The SwcInternalBehavior of an AtomicSwComponentType describes the relevant
    aspects of the software-component with respect to the RTE, i.e. the
    RunnableEntities and the RTEEvents they respond to.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::SwcInternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 345, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 518, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2070, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 246, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 472, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 217, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines an AUTOSAR typed memory-block that needs to available for each
                # instance of the SW-component.
        # is typically only useful if supportsMultipleInstantiation to "true" or if the
                # component defines NVRAM permanent blocks.
        # of arTypedPerInstanceMemory is subject with the purpose to support
                # variability in the implementations.
        # Typically different the implementation are requiring different memory
                # objects.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._arTypedPer: List[RefType] = []

    @property
    def ar_typed_per(self) -> List[RefType]:
        """Get arTypedPer (Pythonic accessor)."""
        return self._arTypedPer
        # This is a RTEEvent specified for the particular Swc of RTEEvent is subject to
        # variability with to support the conditional existence of RTE the number of
        # RTE events might vary due conditional existence of PortPrototypes using Data
        # due to different scheduling needs of atpVariation.
        self._event: List[RTEEvent] = []

    @property
    def event(self) -> List[RTEEvent]:
        """Get event (Pythonic accessor)."""
        return self._event
        # Options how to generate the ExclusiveArea related APIs.
        # When no SwcExclusiveAreaPolicy is specified for an default values apply.
        # atpVariation.
        self._exclusiveArea: List["SwcExclusiveArea"] = []

    @property
    def exclusive_area(self) -> List["SwcExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea
        # Implement state message semantics for establishing among runnables of the
        # same The aggregation of explicitInterRunnable subject to variability with the
        # purpose to in the software components different algorithms in the requiring
        # different number of memory atpVariation.
        self._explicitInter: List[RefType] = []

    @property
    def explicit_inter(self) -> List[RefType]:
        """Get explicitInter (Pythonic accessor)."""
        return self._explicitInter
        # Implement state message semantics for establishing among runnables of the
        # same The aggregation of implicitInterRunnable subject to variability with the
        # purpose to in the software components different algorithms in the requiring
        # different number of memory atpVariation.
        self._implicitInter: List[RefType] = []

    @property
    def implicit_inter(self) -> List[RefType]:
        """Get implicitInter (Pythonic accessor)."""
        return self._implicitInter
        # The includedDataTypeSet is used by a software for its implementation.
        self._includedData: List[RefType] = []

    @property
    def included_data(self) -> List[RefType]:
        """Get includedData (Pythonic accessor)."""
        return self._includedData
        # This aggregation represents the included Mode DeclarationGroups atpSplitable
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
        # Description Template R23-11.
        self._includedMode: List["IncludedMode"] = []

    @property
    def included_mode(self) -> List["IncludedMode"]:
        """Get includedMode (Pythonic accessor)."""
        return self._includedMode
        # The purpose of this is that within the context of a given SwComponentType
                # some data def properties of individual be modified.
        # The aggregation of subject to variability with the support the conditional
                # existence of Port component local memories like "per
                # "arTypedPerInstanceMemory".
        # atpVariation.
        self._instantiation: List["InstantiationDataDef"] = []

    @property
    def instantiation(self) -> List["InstantiationDataDef"]:
        """Get instantiation (Pythonic accessor)."""
        return self._instantiation
        # Defines parameter(s) or characteristic value(s) that needs to be available
                # for each instance of the is typically only useful if set to "true".
        # The perInstanceParameter is subject to the purpose to support variability in
                # the implementations.
        # Typically different the implementation are requiring different memory
                # objects.
        # atpVariation.
        self._perInstance: List["ParameterData"] = []

    @property
    def per_instance(self) -> List["ParameterData"]:
        """Get perInstance (Pythonic accessor)."""
        return self._perInstance
        # Options for generating the signature of port-related calls runnable to the
                # RTE and vice versa.
        # The PortPrototypes is subject to variability with to support the conditional
                # existence of ports.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._portAPIOption: List["PortAPIOption"] = []

    @property
    def port_api_option(self) -> List["PortAPIOption"]:
        """Get portAPIOption (Pythonic accessor)."""
        return self._portAPIOption
        # This is a RunnableEntity specified for the particular Swc of RunnableEntity
                # is subject to variability purpose to support the conditional existence of the
                # number of RunnableEntities due to the conditional existence of Port
                # DataReceivedEvents or due to different of algorithms.
        # atpVariation.
        self._runnable: List[RunnableEntity] = []

    @property
    def runnable(self) -> List[RunnableEntity]:
        """Get runnable (Pythonic accessor)."""
        return self._runnable
        # Defines the requirements on AUTOSAR Services for a particular item.
        # of SwcServiceDependency is subject to the purpose to support the conditional
                # ports as well as the conditional existence of owned by an SwcInternal be
                # located in a different physical file in order that SwcServiceDependency might
                # be later development steps or even by different (e.
        # g OBD expert for Obd related Service Therefore the aggregation is <<atp
                # atpVariation.
        self._service: List["SwcService"] = []

    @property
    def service(self) -> List["SwcService"]:
        """Get service (Pythonic accessor)."""
        return self._service
        # Defines parameter(s) or characteristic value(s) shared between
                # SwComponentPrototypes of the same Sw aggregation of sharedParameter is
                # variability with the purpose to support variability software components
                # implementations.
        # Typically in the implementation are requiring of memory objects.
        # atpVariation.
        self._shared: List["ParameterData"] = []

    @property
    def shared(self) -> List["ParameterData"]:
        """Get shared (Pythonic accessor)."""
        return self._shared
        # Indicate whether the corresponding software-component be multiply
                # instantiated on one ECU.
        # In this case the will result in an appropriate component API on level (with
                # or without instance.
        self._supports: Optional[Boolean] = None

    @property
    def supports(self) -> Optional[Boolean]:
        """Get supports (Pythonic accessor)."""
        return self._supports

    @supports.setter
    def supports(self, value: Optional[Boolean]) -> None:
        """
        Set supports with validation.

        Args:
            value: The supports to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supports = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"supports must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._supports = value
        # Proxy of a variation points in the C/C++ implementation.
        # atpSplitable.
        self._variationPoint: List["VariationPointProxy"] = []

    @property
    def variation_point(self) -> List["VariationPointProxy"]:
        """Get variationPoint (Pythonic accessor)."""
        return self._variationPoint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArTypedPer(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for arTypedPer.

        Returns:
            The arTypedPer value

        Note:
            Delegates to ar_typed_per property (CODING_RULE_V2_00017)
        """
        return self.ar_typed_per  # Delegates to property

    def getEvent(self) -> List[RTEEvent]:
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def getExclusiveArea(self) -> List["SwcExclusiveArea"]:
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def getExplicitInter(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for explicitInter.

        Returns:
            The explicitInter value

        Note:
            Delegates to explicit_inter property (CODING_RULE_V2_00017)
        """
        return self.explicit_inter  # Delegates to property

    def getImplicitInter(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for implicitInter.

        Returns:
            The implicitInter value

        Note:
            Delegates to implicit_inter property (CODING_RULE_V2_00017)
        """
        return self.implicit_inter  # Delegates to property

    def getIncludedData(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for includedData.

        Returns:
            The includedData value

        Note:
            Delegates to included_data property (CODING_RULE_V2_00017)
        """
        return self.included_data  # Delegates to property

    def getIncludedMode(self) -> List["IncludedMode"]:
        """
        AUTOSAR-compliant getter for includedMode.

        Returns:
            The includedMode value

        Note:
            Delegates to included_mode property (CODING_RULE_V2_00017)
        """
        return self.included_mode  # Delegates to property

    def getInstantiation(self) -> List["InstantiationDataDef"]:
        """
        AUTOSAR-compliant getter for instantiation.

        Returns:
            The instantiation value

        Note:
            Delegates to instantiation property (CODING_RULE_V2_00017)
        """
        return self.instantiation  # Delegates to property

    def getPerInstance(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for perInstance.

        Returns:
            The perInstance value

        Note:
            Delegates to per_instance property (CODING_RULE_V2_00017)
        """
        return self.per_instance  # Delegates to property

    def getPortAPIOption(self) -> List["PortAPIOption"]:
        """
        AUTOSAR-compliant getter for portAPIOption.

        Returns:
            The portAPIOption value

        Note:
            Delegates to port_api_option property (CODING_RULE_V2_00017)
        """
        return self.port_api_option  # Delegates to property

    def getRunnable(self) -> List[RunnableEntity]:
        """
        AUTOSAR-compliant getter for runnable.

        Returns:
            The runnable value

        Note:
            Delegates to runnable property (CODING_RULE_V2_00017)
        """
        return self.runnable  # Delegates to property

    def getService(self) -> List["SwcService"]:
        """
        AUTOSAR-compliant getter for service.

        Returns:
            The service value

        Note:
            Delegates to service property (CODING_RULE_V2_00017)
        """
        return self.service  # Delegates to property

    def getShared(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for shared.

        Returns:
            The shared value

        Note:
            Delegates to shared property (CODING_RULE_V2_00017)
        """
        return self.shared  # Delegates to property

    def getSupports(self) -> Boolean:
        """
        AUTOSAR-compliant getter for supports.

        Returns:
            The supports value

        Note:
            Delegates to supports property (CODING_RULE_V2_00017)
        """
        return self.supports  # Delegates to property

    def setSupports(self, value: Boolean) -> SwcInternalBehavior:
        """
        AUTOSAR-compliant setter for supports with method chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Note:
            Delegates to supports property setter (gets validation automatically)
        """
        self.supports = value  # Delegates to property setter
        return self

    def getVariationPoint(self) -> List["VariationPointProxy"]:
        """
        AUTOSAR-compliant getter for variationPoint.

        Returns:
            The variationPoint value

        Note:
            Delegates to variation_point property (CODING_RULE_V2_00017)
        """
        return self.variation_point  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_supports(self, value: Optional[Boolean]) -> SwcInternalBehavior:
        """
        Set supports and return self for chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supports("value")
        """
        self.supports = value  # Use property setter (gets validation)
        return self



class SwcExclusiveAreaPolicy(ARObject):
    """
    Options how to generate the ExclusiveArea related APIs. If no
    SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values
    apply.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::SwcExclusiveAreaPolicy

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 556, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies for this ExclusiveArea if either one common set and Exit APIs for
                # the whole software component from the Rte or if the set of Enter and Exit
                # expected per RunnableEntity.
        # The default value is.
        self._apiPrinciple: Optional[ApiPrincipleEnum] = None

    @property
    def api_principle(self) -> Optional[ApiPrincipleEnum]:
        """Get apiPrinciple (Pythonic accessor)."""
        return self._apiPrinciple

    @api_principle.setter
    def api_principle(self, value: Optional[ApiPrincipleEnum]) -> None:
        """
        Set apiPrinciple with validation.

        Args:
            value: The apiPrinciple to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._apiPrinciple = None
            return

        if not isinstance(value, ApiPrincipleEnum):
            raise TypeError(
                f"apiPrinciple must be ApiPrincipleEnum or None, got {type(value).__name__}"
            )
        self._apiPrinciple = value
        # This reference represents the ExclusiveArea for which the.
        self._exclusiveArea: Optional["ExclusiveArea"] = None

    @property
    def exclusive_area(self) -> Optional["ExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea

    @exclusive_area.setter
    def exclusive_area(self, value: Optional["ExclusiveArea"]) -> None:
        """
        Set exclusiveArea with validation.

        Args:
            value: The exclusiveArea to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exclusiveArea = None
            return

        if not isinstance(value, ExclusiveArea):
            raise TypeError(
                f"exclusiveArea must be ExclusiveArea or None, got {type(value).__name__}"
            )
        self._exclusiveArea = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApiPrinciple(self) -> ApiPrincipleEnum:
        """
        AUTOSAR-compliant getter for apiPrinciple.

        Returns:
            The apiPrinciple value

        Note:
            Delegates to api_principle property (CODING_RULE_V2_00017)
        """
        return self.api_principle  # Delegates to property

    def setApiPrinciple(self, value: ApiPrincipleEnum) -> SwcExclusiveAreaPolicy:
        """
        AUTOSAR-compliant setter for apiPrinciple with method chaining.

        Args:
            value: The apiPrinciple to set

        Returns:
            self for method chaining

        Note:
            Delegates to api_principle property setter (gets validation automatically)
        """
        self.api_principle = value  # Delegates to property setter
        return self

    def getExclusiveArea(self) -> "ExclusiveArea":
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def setExclusiveArea(self, value: "ExclusiveArea") -> SwcExclusiveAreaPolicy:
        """
        AUTOSAR-compliant setter for exclusiveArea with method chaining.

        Args:
            value: The exclusiveArea to set

        Returns:
            self for method chaining

        Note:
            Delegates to exclusive_area property setter (gets validation automatically)
        """
        self.exclusive_area = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_api_principle(self, value: Optional[ApiPrincipleEnum]) -> SwcExclusiveAreaPolicy:
        """
        Set apiPrinciple and return self for chaining.

        Args:
            value: The apiPrinciple to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_api_principle("value")
        """
        self.api_principle = value  # Use property setter (gets validation)
        return self

    def with_exclusive_area(self, value: Optional["ExclusiveArea"]) -> SwcExclusiveAreaPolicy:
        """
        Set exclusiveArea and return self for chaining.

        Args:
            value: The exclusiveArea to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exclusive_area("value")
        """
        self.exclusive_area = value  # Use property setter (gets validation)
        return self


__all__ = [
    RunnableEntity,
    SwcInternalBehavior,
    SwcExclusiveAreaPolicy,
]
