"""
This module contains classes for representing AUTOSAR diagnostic service contributions
in the DiagnosticExtract module.
"""

from typing import (
    List,
    Optional,
    Union,
)

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
)


class DiagnosticServiceTable(DiagnosticCommonElement):
    """
    Represents a diagnostic service table in AUTOSAR diagnostic extract.
    This class defines the relationship between diagnostic connections,
    service instances, and ECU instances for specific protocols.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the DiagnosticServiceTable with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic service table
            short_name: The unique short name of this diagnostic service table
        """
        super().__init__(parent, short_name)

        self.diagnosticConnectionRefs: List[RefType] = []
        self.diagnosticServiceInstanceRefs: List[RefType] = []
        self.ecuInstanceRef: Union[Optional[RefType] , None] = None
        self.protocolKind: Union[Optional[NameToken] , None] = None

    def getDiagnosticConnectionRefs(self) -> List[RefType]:
        """
        Gets the list of diagnostic connection references for this service table.

        Returns:
            List of RefType instances representing diagnostic connection references
        """
        return self.diagnosticConnectionRefs

    def addDiagnosticConnectionRef(self, value: RefType):
        """
        Adds a diagnostic connection reference to this service table.
        Only adds the value if it is not None.

        Args:
            value: The diagnostic connection reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.diagnosticConnectionRefs.append(value)
        return self

    def getDiagnosticServiceInstanceRefs(self) -> List[RefType]:
        """
        Gets the list of diagnostic service instance references for this service table.

        Returns:
            List of RefType instances representing diagnostic service instance references
        """
        return self.diagnosticServiceInstanceRefs

    def addDiagnosticServiceInstanceRef(self, value: RefType):
        """
        Adds a diagnostic service instance reference to this service table.
        Only adds the value if it is not None.

        Args:
            value: The diagnostic service instance reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.diagnosticServiceInstanceRefs.append(value)
        return self

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        Gets the ECU instance reference for this service table.

        Returns:
            RefType representing the ECU instance reference, or None if not set
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: RefType):
        """
        Sets the ECU instance reference for this service table.
        Only sets the value if it is not None.

        Args:
            value: The ECU instance reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getProtocolKind(self) -> Optional[NameToken]:
        """
        Gets the protocol kind for this service table.

        Returns:
            NameToken representing the protocol kind, or None if not set
        """
        return self.protocolKind

    def setProtocolKind(self, value: NameToken):
        """
        Sets the protocol kind for this service table.
        Only sets the value if it is not None.

        Args:
            value: The protocol kind to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.protocolKind = value
        return self
