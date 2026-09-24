from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticServiceTable(DiagnosticCommonElement):
    """This meta-class represents a model of a diagnostic service table, i.e. the UDS services applicable for a given ECU. Tags: atp.recommendedPackage=DiagnosticServiceTables"""

    # DiagnosticServiceTable method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.16, p.59
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticConnectionRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDiagnosticConnectionRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuInstanceRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuInstanceRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProtocolKind                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProtocolKind                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceInstanceRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addServiceInstanceRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the DiagnosticConnection that is taken for handling the data transmission for the enclosing DiagnosticServiceTable. It is possible to refer to more than one diagnostic Connections in order to support more than one diagnostic tester. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticConnection.diagnosticConnection, diagnosticConnection.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.diagnosticConnectionRefs: List[RefType] = []

        # This represents the applicable EcuInstance for this DiagnosticServiceTable. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance
        self.ecuInstanceRef: Optional[RefType] = None

        # This identifies the applicable protocol.
        self.protocolKind: Optional[NameToken] = None

        # This represents the collection of DiagnosticService Instances to be considered in the scope of this Diagnostic ServiceTable, Stereotypes: atpSplitable Tags: atp.Splitkey=serviceInstance
        self.serviceInstanceRefs: List[RefType] = []

    def getDiagnosticConnectionRefs(self) -> List[RefType]:
        """
        This represents the DiagnosticConnection that is taken for handling the data transmission for the enclosing DiagnosticServiceTable. It is possible to refer to more than one diagnostic Connections in order to support more than one diagnostic tester. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticConnection.diagnosticConnection, diagnosticConnection.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.diagnosticConnectionRefs

    def addDiagnosticConnectionRef(self, value: Optional[RefType]):
        """
        This represents the DiagnosticConnection that is taken for handling the data transmission for the enclosing DiagnosticServiceTable. It is possible to refer to more than one diagnostic Connections in order to support more than one diagnostic tester. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticConnection.diagnosticConnection, diagnosticConnection.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value does not extend the diagnosticConnectionRefs list.
        """
        if value is not None:
            self.diagnosticConnectionRefs.append(value)
        return self

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        This represents the applicable EcuInstance for this DiagnosticServiceTable. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]):
        """
        This represents the applicable EcuInstance for this DiagnosticServiceTable. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance

        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getProtocolKind(self) -> Optional[NameToken]:
        """
        This identifies the applicable protocol.
        """
        return self.protocolKind

    def setProtocolKind(self, value: Optional[NameToken]):
        """
        This identifies the applicable protocol.

        A None value is a no-op and does not overwrite an existing protocolKind.
        """
        if value is not None:
            self.protocolKind = value
        return self

    def getServiceInstanceRefs(self) -> List[RefType]:
        """
        This represents the collection of DiagnosticService Instances to be considered in the scope of this Diagnostic ServiceTable, Stereotypes: atpSplitable Tags: atp.Splitkey=serviceInstance
        """
        return self.serviceInstanceRefs

    def addServiceInstanceRef(self, value: Optional[RefType]):
        """
        This represents the collection of DiagnosticService Instances to be considered in the scope of this Diagnostic ServiceTable, Stereotypes: atpSplitable Tags: atp.Splitkey=serviceInstance

        A None value does not extend the serviceInstanceRefs list.
        """
        if value is not None:
            self.serviceInstanceRefs.append(value)
        return self
