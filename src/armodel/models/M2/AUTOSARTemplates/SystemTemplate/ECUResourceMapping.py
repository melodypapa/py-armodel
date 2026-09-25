from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable


class CommunicationControllerMapping(ARObject):
    """CommunicationControllerMapping specifies the CommunicationPeripheral hardware (defined in the ECU Resource Template) to realize the specified CommunicationController in a physical topology."""

    # CommunicationControllerMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.134, p.183
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getCommunicationControllerRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setCommunicationControllerRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getHwCommunicationControllerRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setHwCommunicationControllerRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the CommunicationController in the System Template
        self.communicationControllerRef: Optional[RefType] = None

        # Reference to a HwElement of category CommunicationController in the ECU Resource Template.
        self.hwCommunicationControllerRef: Optional[RefType] = None

    def getCommunicationControllerRef(self) -> Optional[RefType]:
        """
        Reference to the CommunicationController in the System Template
        """
        return self.communicationControllerRef

    def setCommunicationControllerRef(self, value: Optional[RefType]):
        """
        Reference to the CommunicationController in the System Template

        A None value is a no-op and does not overwrite an existing communicationControllerRef.
        """
        if value is not None:
            self.communicationControllerRef = value
        return self

    def getHwCommunicationControllerRef(self) -> Optional[RefType]:
        """
        Reference to a HwElement of category CommunicationController in the ECU Resource Template.
        """
        return self.hwCommunicationControllerRef

    def setHwCommunicationControllerRef(self, value: Optional[RefType]):
        """
        Reference to a HwElement of category CommunicationController in the ECU Resource Template.

        A None value is a no-op and does not overwrite an existing hwCommunicationControllerRef.
        """
        if value is not None:
            self.hwCommunicationControllerRef = value
        return self


class HwPortMapping(ARObject):
    """HWPortMapping specifies the hwCommunicationPort (defined in the ECU Resource Template) to realize the specified CommunicationConnector in a physical topology."""

    # HwPortMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.135, p.183
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getCommunicationConnectorRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setCommunicationConnectorRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getHwCommunicationPortRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setHwCommunicationPortRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the CommunicationConnector in the System Template
        self.communicationConnectorRef: Optional[RefType] = None

        # Reference to the HwPinPortGroup of category CommunicationPort. The connection to the HwCommunicationController is described in the Ecu Resource Description.
        self.hwCommunicationPortRef: Optional[RefType] = None

    def getCommunicationConnectorRef(self) -> Optional[RefType]:
        """
        Reference to the CommunicationConnector in the System Template
        """
        return self.communicationConnectorRef

    def setCommunicationConnectorRef(self, value: Optional[RefType]):
        """
        Reference to the CommunicationConnector in the System Template

        A None value is a no-op and does not overwrite an existing communicationConnectorRef.
        """
        if value is not None:
            self.communicationConnectorRef = value
        return self

    def getHwCommunicationPortRef(self) -> Optional[RefType]:
        """
        Reference to the HwPinPortGroup of category CommunicationPort. The connection to the HwCommunicationController is described in the Ecu Resource Description.
        """
        return self.hwCommunicationPortRef

    def setHwCommunicationPortRef(self, value: Optional[RefType]):
        """
        Reference to the HwPinPortGroup of category CommunicationPort. The connection to the HwCommunicationController is described in the Ecu Resource Description.

        A None value is a no-op and does not overwrite an existing hwCommunicationPortRef.
        """
        if value is not None:
            self.hwCommunicationPortRef = value
        return self


class ECUMapping(Identifiable, VariationPointCapable):
    """ECUMapping allows to assign an ECU hardware type (defined in the ECU Resource Template) to an ECUInstance used in a physical topology."""

    # ECUMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.133, p.182
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getCommControllerMappings    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setCommControllerMappings    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCommControllerMapping     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEcuRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setEcuRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEcuInstanceRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setEcuInstanceRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getHwPortMappings            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setHwPortMappings            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addHwPortMapping             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The ECUMapping contains the mapping of all CommunicationControllers of the ECU.
        self.commControllerMappings: List[CommunicationControllerMapping] = []

        # Reference to a HwElement of category ECU in the ECU Resource Template.
        self.ecuRef: Optional[RefType] = None

        # Reference to the EcuInstance in the System Template
        self.ecuInstanceRef: Optional[RefType] = None

        # The ECUMapping contains the mapping of all HW Communication Ports of the ECU.
        self.hwPortMappings: List[HwPortMapping] = []

    def getCommControllerMappings(self) -> List[CommunicationControllerMapping]:
        """
        The ECUMapping contains the mapping of all CommunicationControllers of the ECU.
        """
        return self.commControllerMappings

    def setCommControllerMappings(self, value: List[CommunicationControllerMapping]):
        """
        The ECUMapping contains the mapping of all CommunicationControllers of the ECU.

        A None value is a no-op and does not overwrite an existing commControllerMappings list.
        """
        if value is not None:
            self.commControllerMappings = value
        return self

    def addCommControllerMapping(self, value: CommunicationControllerMapping):
        """
        The ECUMapping contains the mapping of all CommunicationControllers of the ECU.

        A None value does not extend the commControllerMappings list.
        """
        if value is not None:
            self.commControllerMappings.append(value)
        return self

    def getEcuRef(self) -> Optional[RefType]:
        """
        Reference to a HwElement of category ECU in the ECU Resource Template.
        """
        return self.ecuRef

    def setEcuRef(self, value: Optional[RefType]):
        """
        Reference to a HwElement of category ECU in the ECU Resource Template.

        A None value is a no-op and does not overwrite an existing ecuRef.
        """
        if value is not None:
            self.ecuRef = value
        return self

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        Reference to the EcuInstance in the System Template
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]):
        """
        Reference to the EcuInstance in the System Template

        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getHwPortMappings(self) -> List[HwPortMapping]:
        """
        The ECUMapping contains the mapping of all HW Communication Ports of the ECU.
        """
        return self.hwPortMappings

    def setHwPortMappings(self, value: List[HwPortMapping]):
        """
        The ECUMapping contains the mapping of all HW Communication Ports of the ECU.

        A None value is a no-op and does not overwrite an existing hwPortMappings list.
        """
        if value is not None:
            self.hwPortMappings = value
        return self

    def addHwPortMapping(self, value: HwPortMapping):
        """
        The ECUMapping contains the mapping of all HW Communication Ports of the ECU.

        A None value does not extend the hwPortMappings list.
        """
        if value is not None:
            self.hwPortMappings.append(value)
        return self
