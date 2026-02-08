"""
AUTOSAR Package - ServerCall

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)




class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    """
    If a RunnableEntity owns a AsynchronousServerCallResultPoint it is entitled
    to get the result of the referenced AsynchronousServerCallPoint. If it is
    associated with AsynchronousServerCallReturnsEvent, this RTEEvent notifies
    the completion of the required ClientServerOperation or a timeout. The
    occurrence of this event can either unblock a WaitPoint or can lead to the
    invocation of a RunnableEntity.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall::AsynchronousServerCallResultPoint
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 304, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 581, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced Asynchronous Server Call Point defines the asynchronous server
        # call from which the results are.
        self._asynchronous: Optional["AsynchronousServer"] = None

    @property
    def asynchronous(self) -> Optional["AsynchronousServer"]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, value: Optional["AsynchronousServer"]) -> None:
        """
        Set asynchronous with validation.
        
        Args:
            value: The asynchronous to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._asynchronous = None
            return

        if not isinstance(value, AsynchronousServer):
            raise TypeError(
                f"asynchronous must be AsynchronousServer or None, got {type(value).__name__}"
            )
        self._asynchronous = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAsynchronous(self) -> "AsynchronousServer":
        """
        AUTOSAR-compliant getter for asynchronous.
        
        Returns:
            The asynchronous value
        
        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def setAsynchronous(self, value: "AsynchronousServer") -> "AsynchronousServerCallResultPoint":
        """
        AUTOSAR-compliant setter for asynchronous with method chaining.
        
        Args:
            value: The asynchronous to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to asynchronous property setter (gets validation automatically)
        """
        self.asynchronous = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_asynchronous(self, value: Optional["AsynchronousServer"]) -> "AsynchronousServerCallResultPoint":
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



class ServerCallPoint(AbstractAccessPoint, ABC):
    """
    If a RunnableEntity owns a ServerCallPoint it is entitled to invoke a
    particular ClientServerOperation of a specific RPortPrototype of the
    corresponding AtomicSwComponentType
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall::ServerCallPoint
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 335, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 580, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2055, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ServerCallPoint:
            raise TypeError("ServerCallPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: ROperationInAtomicSwc.
        self._operationInstanceRef: Optional["ClientServerOperation"] = None

    @property
    def operation_instance_ref(self) -> Optional["ClientServerOperation"]:
        """Get operationInstanceRef (Pythonic accessor)."""
        return self._operationInstanceRef

    @operation_instance_ref.setter
    def operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operationInstanceRef with validation.
        
        Args:
            value: The operationInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operationInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operationInstanceRef = value
        # Time in seconds before the server call times out and an error message.
        # It depends on the call type asynchronous) how this is reported.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.
        
        Args:
            value: The timeout to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperationInstanceRef(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operationInstanceRef.
        
        Returns:
            The operationInstanceRef value
        
        Note:
            Delegates to operation_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.operation_instance_ref  # Delegates to property

    def setOperationInstanceRef(self, value: "ClientServerOperation") -> "ServerCallPoint":
        """
        AUTOSAR-compliant setter for operationInstanceRef with method chaining.
        
        Args:
            value: The operationInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to operation_instance_ref property setter (gets validation automatically)
        """
        self.operation_instance_ref = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.
        
        Returns:
            The timeout value
        
        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "ServerCallPoint":
        """
        AUTOSAR-compliant setter for timeout with method chaining.
        
        Args:
            value: The timeout to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> "ServerCallPoint":
        """
        Set operationInstanceRef and return self for chaining.
        
        Args:
            value: The operationInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_operation_instance_ref("value")
        """
        self.operation_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["TimeValue"]) -> "ServerCallPoint":
        """
        Set timeout and return self for chaining.
        
        Args:
            value: The timeout to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self



class SynchronousServerCallPoint(ServerCallPoint):
    """
    This means that the RunnableEntity is supposed to perform a blocking wait
    for a response from the server.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall::SynchronousServerCallPoint
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 580, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2074, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This indicates that the call point is located at the deepest level inside one
        # or more ExclusiveAreas that are nested the given order.
        self._calledFrom: Optional["ExclusiveAreaNesting"] = None

    @property
    def called_from(self) -> Optional["ExclusiveAreaNesting"]:
        """Get calledFrom (Pythonic accessor)."""
        return self._calledFrom

    @called_from.setter
    def called_from(self, value: Optional["ExclusiveAreaNesting"]) -> None:
        """
        Set calledFrom with validation.
        
        Args:
            value: The calledFrom to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledFrom = None
            return

        if not isinstance(value, ExclusiveAreaNesting):
            raise TypeError(
                f"calledFrom must be ExclusiveAreaNesting or None, got {type(value).__name__}"
            )
        self._calledFrom = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalledFrom(self) -> "ExclusiveAreaNesting":
        """
        AUTOSAR-compliant getter for calledFrom.
        
        Returns:
            The calledFrom value
        
        Note:
            Delegates to called_from property (CODING_RULE_V2_00017)
        """
        return self.called_from  # Delegates to property

    def setCalledFrom(self, value: "ExclusiveAreaNesting") -> "SynchronousServerCallPoint":
        """
        AUTOSAR-compliant setter for calledFrom with method chaining.
        
        Args:
            value: The calledFrom to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to called_from property setter (gets validation automatically)
        """
        self.called_from = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_from(self, value: Optional["ExclusiveAreaNesting"]) -> "SynchronousServerCallPoint":
        """
        Set calledFrom and return self for chaining.
        
        Args:
            value: The calledFrom to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_called_from("value")
        """
        self.called_from = value  # Use property setter (gets validation)
        return self



class AsynchronousServerCallPoint(ServerCallPoint):
    """
    An AsynchronousServerCallPoint is used for asynchronous invocation of a
    ClientServerOperation. IMPORTANT: a ServerCallPoint cannot be used
    concurrently. Once the client RunnableEntity has made the invocation, the
    ServerCallPoint cannot be used until the call returns (or an error occurs!)
    at which point the ServerCallPoint becomes available again.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall::AsynchronousServerCallPoint
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 581, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====