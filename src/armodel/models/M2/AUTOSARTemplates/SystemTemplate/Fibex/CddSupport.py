from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, PhysicalChannel


class UserDefinedCluster(CommunicationCluster):
    """This element allows the modeling of arbitrary Communication Clusters (e.g. bus systems that are not supported by AUTOSAR). Tags: atp.recommendedPackage=CommunicationClusters"""

    # UserDefinedCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.129, p.179
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class UserDefinedPhysicalChannel(PhysicalChannel):
    """This element allows the modeling of arbitrary Physical Channels."""

    # UserDefinedPhysicalChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.130, p.179
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes; Base = ARObject, Identifiable, MultilanguageReferrable, PhysicalChannel, Referrable; reader/writer coverage flows through the concrete USER-DEFINED-PHYSICAL-CHANNEL dispatch — XSD group USER-DEFINED-PHYSICAL-CHANNEL, AUTOSAR_00052.xsd line 128980, is an empty sequence)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
