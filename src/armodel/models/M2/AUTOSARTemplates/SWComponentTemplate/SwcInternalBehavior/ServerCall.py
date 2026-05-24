"""
This module contains classes for representing AUTOSAR server call points
in software component internal behavior templates.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ROperationInAtomicSwcInstanceRef

class ServerCallPoint(AbstractAccessPoint, ABC):
    """
    If a RunnableEntity owns a ServerCallPoint it is entitled to invoke a
    particular ClientServerOperation of a specific RPortPrototype of the
    corresponding AtomicSwComponentType.
    """

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ServerCallPoint:
            raise TypeError("ServerCallPoint is an abstract class.")
        super().__init__(parent, short_name)

        self.operationIRef: 'ROperationInAtomicSwcInstanceRef' = None
        self.timeout: float = None

    def getOperationIRef(self):
        """
        Gets the operation instance reference.

        Returns:
            ROperationInAtomicSwcInstanceRef: The operation instance reference
        """
        return self.operationIRef

    def setOperationIRef(self, value):
        """
        Sets the operation instance reference.

        Args:
            value: The operation instance reference to set

        Returns:
            self for method chaining
        """
        self.operationIRef = value
        return self

    def getTimeout(self):
        """
        Gets the timeout in seconds before the server call times out.

        Returns:
            float: The timeout in seconds
        """
        return self.timeout

    def setTimeout(self, value):
        """
        Sets the timeout in seconds before the server call times out.

        Args:
            value: The timeout in seconds to set

        Returns:
            self for method chaining
        """
        self.timeout = value
        return self
