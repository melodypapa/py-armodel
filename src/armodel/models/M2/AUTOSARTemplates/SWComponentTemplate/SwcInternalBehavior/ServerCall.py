"""
This module contains classes for representing AUTOSAR server call points
in software component internal behavior templates.
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ROperationInAtomicSwcInstanceRef


class ServerCallPoint(AbstractAccessPoint, VariationPointCapable, ABC):
    """
    If a RunnableEntity owns a ServerCallPoint it is entitled to invoke a particular ClientServerOperation of a specific RPortPrototype of the corresponding AtomicSwComponentType
    """

    # ServerCallPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.35, p.580 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOperationIRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOperationIRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeout                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeout                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ServerCallPoint:
            raise TypeError("ServerCallPoint is an abstract class.")
        super().__init__(parent, short_name)

        # The operation that is called by this runnable.
        self.operationIRef: Optional[ROperationInAtomicSwcInstanceRef] = None

        # Time in seconds before the server call times out and returns with an error message. It depends on the call type (synchronous or asynchronous) how this is reported.
        self.timeout: Optional[TimeValue] = None

    def getOperationIRef(self) -> Optional[ROperationInAtomicSwcInstanceRef]:
        """
        The operation that is called by this runnable.

        Returns:
            Optional[ROperationInAtomicSwcInstanceRef]: The operation instance reference, or None if not set
        """
        return self.operationIRef

    def setOperationIRef(self, value: Optional[ROperationInAtomicSwcInstanceRef]) -> "ServerCallPoint":
        """
        The operation that is called by this runnable.
        A None value is a no-op and does not overwrite an existing operation instance reference.

        Args:
            value: The operation instance reference to set

        Returns:
            ServerCallPoint: self for method chaining
        """
        if value is not None:
            self.operationIRef = value
        return self

    def getTimeout(self) -> Optional[TimeValue]:
        """
        Time in seconds before the server call times out and returns with an error message. It depends on the call type (synchronous or asynchronous) how this is reported.

        Returns:
            Optional[TimeValue]: The timeout, or None if not set
        """
        return self.timeout

    def setTimeout(self, value: Optional[TimeValue]) -> "ServerCallPoint":
        """
        Time in seconds before the server call times out and returns with an error message. It depends on the call type (synchronous or asynchronous) how this is reported.
        A None value is a no-op and does not overwrite an existing timeout.

        Args:
            value: The timeout to set

        Returns:
            ServerCallPoint: self for method chaining
        """
        if value is not None:
            self.timeout = value
        return self


class AsynchronousServerCallResultPoint(AbstractAccessPoint, VariationPointCapable):
    # AsynchronousServerCallResultPoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAsynchronousServerCallPointRef [x] impl  [ ] docstring  [ ] test
    # [ ] setAsynchronousServerCallPointRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.asynchronousServerCallPointRef = None  # type: RefType

    def getAsynchronousServerCallPointRef(self):
        return self.asynchronousServerCallPointRef

    def setAsynchronousServerCallPointRef(self, value):
        self.asynchronousServerCallPointRef = value
        return self


class AsynchronousServerCallPoint(ServerCallPoint):
    """
    An AsynchronousServerCallPoint is used for asynchronous invocation of a ClientServerOperation. IMPORTANT: a ServerCallPoint cannot be used concurrently. Once the client RunnableEntity has made the invocation, the ServerCallPoint cannot be used until the call returns (or an error occurs!) at which point the ServerCallPoint becomes available again.
    """

    # AsynchronousServerCallPoint method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.37, p.581 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SynchronousServerCallPoint(ServerCallPoint):
    """
    This means that the RunnableEntity is supposed to perform a blocking wait for a response from the server.
    """

    # SynchronousServerCallPoint method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.36, p.580 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCalledFromWithinExclusiveAreaRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCalledFromWithinExclusiveAreaRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This indicates that the call point is located at the deepest level inside one or more ExclusiveAreas that are nested in the given order.
        self.calledFromWithinExclusiveAreaRef: Optional[RefType] = None

    def getCalledFromWithinExclusiveAreaRef(self) -> Optional[RefType]:
        """
        This indicates that the call point is located at the deepest level inside one or more ExclusiveAreas that are nested in the given order.
        """
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value: Optional[RefType]) -> "SynchronousServerCallPoint":
        """
        This indicates that the call point is located at the deepest level inside one or more ExclusiveAreas that are nested in the given order.
        A None value is a no-op and does not overwrite an existing calledFromWithinExclusiveAreaRef.
        """
        if value is not None:
            self.calledFromWithinExclusiveAreaRef = value
        return self
