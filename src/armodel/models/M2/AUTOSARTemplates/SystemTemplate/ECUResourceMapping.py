from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable


class ECUMapping(Identifiable, VariationPointCapable):
    """
    Represents an ECU mapping that defines the relationship between AUTOSAR software components
    and their physical ECU instances. This class maps communication controllers, hardware ports,
    and other ECU resources to specific ECU instances within the system configuration.
    """

    # ECUMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommControllerMappings    [x] impl  [ ] docstring  [ ] test
    # [ ] setCommControllerMappings    [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuInstanceRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuInstanceRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getHwPortMappings            [x] impl  [ ] docstring  [ ] test
    # [ ] setHwPortMappings            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.commControllerMappings = []  # type: List[CommunicationControllerMapping]
        self.ecuRef = None  # type: RefType
        self.ecuInstanceRef = None  # type: RefType
        self.hwPortMappings = []  # type: List[HwPortMapping]

    def getCommControllerMappings(self):
        return self.commControllerMappings

    def setCommControllerMappings(self, value):
        if value is not None:
            self.commControllerMappings = value
        return self

    def getEcuRef(self):
        return self.ecuRef

    def setEcuRef(self, value):
        if value is not None:
            self.ecuRef = value
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getHwPortMappings(self):
        return self.hwPortMappings

    def setHwPortMappings(self, value):
        if value is not None:
            self.hwPortMappings = value
        return self


class CommunicationControllerMapping(ARObject):
    """CommunicationControllerMapping specifies the CommunicationPeripheral hardware (defined in the ECU Resource Template) to realize the specified CommunicationController in a physical topology."""

    # CommunicationControllerMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.134, p.183
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
