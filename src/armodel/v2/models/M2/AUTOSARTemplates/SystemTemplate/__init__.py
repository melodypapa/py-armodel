"""
AUTOSAR Package - SystemTemplate

Package: M2::AUTOSARTemplates::SystemTemplate
"""


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import (
    FlatMap,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
    Numerical,
    ParameterData,
    PositiveInteger,
    RefType,
    RevisionLabelString,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerOperation,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    CpSoftwareCluster,
)


class System(ARElement):
    """
    The top level element of the System Description. The System description
    defines five major elements: Topology, Software, Communication, Mapping and
    Mapping Constraints. The System element directly aggregates the elements
    describing the Software, Mapping and Mapping Constraints; it contains a
    reference to an ASAM FIBEX description specifying Communication and
    Topology.

    Package: M2::AUTOSARTemplates::SystemTemplate::System

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 349, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 331, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1007, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 40, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 249, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 17, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 476, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Set of Client Identifiers that are used for inter-ECU communication in the
        # System.
        self._clientId: List[RefType] = []

    @property
    def client_id(self) -> List[RefType]:
        """Get clientId (Pythonic accessor)."""
        return self._clientId
        # Defines the byteOrder of the header in ContainerIPdus.
        self._containerIPdu: Optional[ByteOrderEnum] = None

    @property
    def container_i_pdu(self) -> Optional[ByteOrderEnum]:
        """Get containerIPdu (Pythonic accessor)."""
        return self._containerIPdu

    @container_i_pdu.setter
    def container_i_pdu(self, value: Optional[ByteOrderEnum]) -> None:
        """
        Set containerIPdu with validation.

        Args:
            value: The containerIPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._containerIPdu = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"containerIPdu must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._containerIPdu = value
        # Version number of the Ecu Extract.
        self._ecuExtractVersion: Optional[RevisionLabelString] = None

    @property
    def ecu_extract_version(self) -> Optional[RevisionLabelString]:
        """Get ecuExtractVersion (Pythonic accessor)."""
        return self._ecuExtractVersion

    @ecu_extract_version.setter
    def ecu_extract_version(self, value: Optional[RevisionLabelString]) -> None:
        """
        Set ecuExtractVersion with validation.

        Args:
            value: The ecuExtractVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuExtractVersion = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"ecuExtractVersion must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._ecuExtractVersion = value
        # Reference to ASAM FIBEX elements specifying Topology.
        # Elements used within a System Description shall from the System Element.
        # order to describe a product-line, all Fibex be optional.
        # atpVariation.
        self._fibexElement: List[FibexElement] = []

    @property
    def fibex_element(self) -> List[FibexElement]:
        """Get fibexElement (Pythonic accessor)."""
        return self._fibexElement
        # This reference identifies the InterpolationRoutineMapping Sets that are
        # relevant in the context of the enclosing.
        self._interpolation: List[InterpolationRoutine] = []

    @property
    def interpolation(self) -> List[InterpolationRoutine]:
        """Get interpolation (Pythonic accessor)."""
        return self._interpolation
        # Collection of J1939Clusters that share a common address space for the routing
                # of messages.
        # atpVariation.
        self._j1939Shared: List["J1939SharedAddress"] = []

    @property
    def j1939_shared(self) -> List["J1939SharedAddress"]:
        """Get j1939Shared (Pythonic accessor)."""
        return self._j1939Shared
        # Aggregation of all mapping aspects (mapping of SW ECUs, mapping of data
                # elements to mapping constraints).
        # to support OEM / Tier 1 interaction and shared one common System this
                # aggregation is atpVariation.
        # The content of System be provided by several parties using for the
                # SystemMapping.
        # is not required when the System description for a network-only use-case.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._mapping: List[RefType] = []

    @property
    def mapping(self) -> List[RefType]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping
        # Length of the partial networking request release vector (in bytes).
        self._pncVector: Optional[PositiveInteger] = None

    @property
    def pnc_vector(self) -> Optional[PositiveInteger]:
        """Get pncVector (Pythonic accessor)."""
        return self._pncVector

    @pnc_vector.setter
    def pnc_vector(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pncVector with validation.

        Args:
            value: The pncVector to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncVector = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pncVector must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pncVector = value
        # Absolute offset (with respect to the NM-PDU) of the request release
        # information vector that in bytes as an index starting with 0.
        self._pncVectorOffset: Optional[PositiveInteger] = None

    @property
    def pnc_vector_offset(self) -> Optional[PositiveInteger]:
        """Get pncVectorOffset (Pythonic accessor)."""
        return self._pncVectorOffset

    @pnc_vector_offset.setter
    def pnc_vector_offset(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pncVectorOffset with validation.

        Args:
            value: The pncVectorOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncVectorOffset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pncVectorOffset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pncVectorOffset = value
        # Aggregation of the root software composition, containing all software
                # components in the System in a hierarchical element is not required when the
                # System used for a network-only use-case.
        # RootSwCompositionPrototype can vary.
        # atpVariation.
        self._rootSoftware: Optional[RootSwComposition] = None

    @property
    def root_software(self) -> Optional[RootSwComposition]:
        """Get rootSoftware (Pythonic accessor)."""
        return self._rootSoftware

    @root_software.setter
    def root_software(self, value: Optional[RootSwComposition]) -> None:
        """
        Set rootSoftware with validation.

        Args:
            value: The rootSoftware to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootSoftware = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"rootSoftware must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._rootSoftware = value
        # CP Software Clusters of this System atpVariation.
        self._swCluster: List["CpSoftwareCluster"] = []

    @property
    def sw_cluster(self) -> List["CpSoftwareCluster"]:
        """Get swCluster (Pythonic accessor)."""
        return self._swCluster
        # Possibility to provide additional documentation while the System.
        # The System documentation can be several chapters.
        # atpVariation.
        self._system: List[Chapter] = []

    @property
    def system(self) -> List[Chapter]:
        """Get system (Pythonic accessor)."""
        return self._system
        # Version number of the System Description.
        self._systemVersion: Optional[RevisionLabelString] = None

    @property
    def system_version(self) -> Optional[RevisionLabelString]:
        """Get systemVersion (Pythonic accessor)."""
        return self._systemVersion

    @system_version.setter
    def system_version(self, value: Optional[RevisionLabelString]) -> None:
        """
        Set systemVersion with validation.

        Args:
            value: The systemVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemVersion = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"systemVersion must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._systemVersion = value

    def with_fibex_element(self, value):
        """
        Set fibex_element and return self for chaining.

        Args:
            value: The fibex_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fibex_element("value")
        """
        self.fibex_element = value  # Use property setter (gets validation)
        return self

    def with_interpolation(self, value):
        """
        Set interpolation and return self for chaining.

        Args:
            value: The interpolation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interpolation("value")
        """
        self.interpolation = value  # Use property setter (gets validation)
        return self

    def with_j1939_shared(self, value):
        """
        Set j1939_shared and return self for chaining.

        Args:
            value: The j1939_shared to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_j1939_shared("value")
        """
        self.j1939_shared = value  # Use property setter (gets validation)
        return self

    def with_mapping(self, value):
        """
        Set mapping and return self for chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping("value")
        """
        self.mapping = value  # Use property setter (gets validation)
        return self

    def with_sw_cluster(self, value):
        """
        Set sw_cluster and return self for chaining.

        Args:
            value: The sw_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_cluster("value")
        """
        self.sw_cluster = value  # Use property setter (gets validation)
        return self

    def with_system(self, value):
        """
        Set system and return self for chaining.

        Args:
            value: The system to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system("value")
        """
        self.system = value  # Use property setter (gets validation)
        return self

    def with_calibration(self, value):
        """
        Set calibration and return self for chaining.

        Args:
            value: The calibration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_calibration("value")
        """
        self.calibration = value  # Use property setter (gets validation)
        return self

    def with_application(self, value):
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_app_os_task(self, value):
        """
        Set app_os_task and return self for chaining.

        Args:
            value: The app_os_task to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_app_os_task("value")
        """
        self.app_os_task = value  # Use property setter (gets validation)
        return self

    def with_com(self, value):
        """
        Set com and return self for chaining.

        Args:
            value: The com to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com("value")
        """
        self.com = value  # Use property setter (gets validation)
        return self

    def with_crypto_service(self, value):
        """
        Set crypto_service and return self for chaining.

        Args:
            value: The crypto_service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_service("value")
        """
        self.crypto_service = value  # Use property setter (gets validation)
        return self

    def with_data_mapping(self, value):
        """
        Set data_mapping and return self for chaining.

        Args:
            value: The data_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_mapping("value")
        """
        self.data_mapping = value  # Use property setter (gets validation)
        return self

    def with_dds_i_signal_to(self, value):
        """
        Set dds_i_signal_to and return self for chaining.

        Args:
            value: The dds_i_signal_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_i_signal_to("value")
        """
        self.dds_i_signal_to = value  # Use property setter (gets validation)
        return self

    def with_ecu_resource(self, value):
        """
        Set ecu_resource and return self for chaining.

        Args:
            value: The ecu_resource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_resource("value")
        """
        self.ecu_resource = value  # Use property setter (gets validation)
        return self

    def with_j1939_controller(self, value):
        """
        Set j1939_controller and return self for chaining.

        Args:
            value: The j1939_controller to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_j1939_controller("value")
        """
        self.j1939_controller = value  # Use property setter (gets validation)
        return self

    def with_mapping(self, value):
        """
        Set mapping and return self for chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping("value")
        """
        self.mapping = value  # Use property setter (gets validation)
        return self

    def with_pnc_mapping(self, value):
        """
        Set pnc_mapping and return self for chaining.

        Args:
            value: The pnc_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_mapping("value")
        """
        self.pnc_mapping = value  # Use property setter (gets validation)
        return self

    def with_port_element_to(self, value):
        """
        Set port_element_to and return self for chaining.

        Args:
            value: The port_element_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_element_to("value")
        """
        self.port_element_to = value  # Use property setter (gets validation)
        return self

    def with_resource(self, value):
        """
        Set resource and return self for chaining.

        Args:
            value: The resource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resource("value")
        """
        self.resource = value  # Use property setter (gets validation)
        return self

    def with_resource_to(self, value):
        """
        Set resource_to and return self for chaining.

        Args:
            value: The resource_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resource_to("value")
        """
        self.resource_to = value  # Use property setter (gets validation)
        return self

    def with_rte_event(self, value):
        """
        Set rte_event and return self for chaining.

        Args:
            value: The rte_event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rte_event("value")
        """
        self.rte_event = value  # Use property setter (gets validation)
        return self

    def with_rte_event_to_os(self, value):
        """
        Set rte_event_to_os and return self for chaining.

        Args:
            value: The rte_event_to_os to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rte_event_to_os("value")
        """
        self.rte_event_to_os = value  # Use property setter (gets validation)
        return self

    def with_signal_path(self, value):
        """
        Set signal_path and return self for chaining.

        Args:
            value: The signal_path to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_path("value")
        """
        self.signal_path = value  # Use property setter (gets validation)
        return self

    def with_software_cluster(self, value):
        """
        Set software_cluster and return self for chaining.

        Args:
            value: The software_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software_cluster("value")
        """
        self.software_cluster = value  # Use property setter (gets validation)
        return self

    def with_sw_cluster(self, value):
        """
        Set sw_cluster and return self for chaining.

        Args:
            value: The sw_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_cluster("value")
        """
        self.sw_cluster = value  # Use property setter (gets validation)
        return self

    def with_swc_to(self, value):
        """
        Set swc_to and return self for chaining.

        Args:
            value: The swc_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_to("value")
        """
        self.swc_to = value  # Use property setter (gets validation)
        return self

    def with_sw_impl_mapping(self, value):
        """
        Set sw_impl_mapping and return self for chaining.

        Args:
            value: The sw_impl_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_impl_mapping("value")
        """
        self.sw_impl_mapping = value  # Use property setter (gets validation)
        return self

    def with_sw_mapping(self, value):
        """
        Set sw_mapping and return self for chaining.

        Args:
            value: The sw_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_mapping("value")
        """
        self.sw_mapping = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value):
        """
        Set system_signal and return self for chaining.

        Args:
            value: The system_signal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self

    def with_system_signal_to(self, value):
        """
        Set system_signal_to and return self for chaining.

        Args:
            value: The system_signal_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal_to("value")
        """
        self.system_signal_to = value  # Use property setter (gets validation)
        return self

    def with_com(self, value):
        """
        Set com and return self for chaining.

        Args:
            value: The com to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com("value")
        """
        self.com = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value):
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    def with_participating(self, value):
        """
        Set participating and return self for chaining.

        Args:
            value: The participating to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_participating("value")
        """
        self.participating = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientId(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for clientId.

        Returns:
            The clientId value

        Note:
            Delegates to client_id property (CODING_RULE_V2_00017)
        """
        return self.client_id  # Delegates to property

    def getContainerIPdu(self) -> ByteOrderEnum:
        """
        AUTOSAR-compliant getter for containerIPdu.

        Returns:
            The containerIPdu value

        Note:
            Delegates to container_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.container_i_pdu  # Delegates to property

    def setContainerIPdu(self, value: ByteOrderEnum) -> System:
        """
        AUTOSAR-compliant setter for containerIPdu with method chaining.

        Args:
            value: The containerIPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to container_i_pdu property setter (gets validation automatically)
        """
        self.container_i_pdu = value  # Delegates to property setter
        return self

    def getEcuExtractVersion(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for ecuExtractVersion.

        Returns:
            The ecuExtractVersion value

        Note:
            Delegates to ecu_extract_version property (CODING_RULE_V2_00017)
        """
        return self.ecu_extract_version  # Delegates to property

    def setEcuExtractVersion(self, value: "RevisionLabelString") -> System:
        """
        AUTOSAR-compliant setter for ecuExtractVersion with method chaining.

        Args:
            value: The ecuExtractVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_extract_version property setter (gets validation automatically)
        """
        self.ecu_extract_version = value  # Delegates to property setter
        return self

    def getFibexElement(self) -> List[FibexElement]:
        """
        AUTOSAR-compliant getter for fibexElement.

        Returns:
            The fibexElement value

        Note:
            Delegates to fibex_element property (CODING_RULE_V2_00017)
        """
        return self.fibex_element  # Delegates to property

    def getInterpolation(self) -> List[InterpolationRoutine]:
        """
        AUTOSAR-compliant getter for interpolation.

        Returns:
            The interpolation value

        Note:
            Delegates to interpolation property (CODING_RULE_V2_00017)
        """
        return self.interpolation  # Delegates to property

    def getJ1939Shared(self) -> List["J1939SharedAddress"]:
        """
        AUTOSAR-compliant getter for j1939Shared.

        Returns:
            The j1939Shared value

        Note:
            Delegates to j1939_shared property (CODING_RULE_V2_00017)
        """
        return self.j1939_shared  # Delegates to property

    def getMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    def getPncVector(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pncVector.

        Returns:
            The pncVector value

        Note:
            Delegates to pnc_vector property (CODING_RULE_V2_00017)
        """
        return self.pnc_vector  # Delegates to property

    def setPncVector(self, value: PositiveInteger) -> System:
        """
        AUTOSAR-compliant setter for pncVector with method chaining.

        Args:
            value: The pncVector to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_vector property setter (gets validation automatically)
        """
        self.pnc_vector = value  # Delegates to property setter
        return self

    def getPncVectorOffset(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pncVectorOffset.

        Returns:
            The pncVectorOffset value

        Note:
            Delegates to pnc_vector_offset property (CODING_RULE_V2_00017)
        """
        return self.pnc_vector_offset  # Delegates to property

    def setPncVectorOffset(self, value: PositiveInteger) -> System:
        """
        AUTOSAR-compliant setter for pncVectorOffset with method chaining.

        Args:
            value: The pncVectorOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_vector_offset property setter (gets validation automatically)
        """
        self.pnc_vector_offset = value  # Delegates to property setter
        return self

    def getRootSoftware(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for rootSoftware.

        Returns:
            The rootSoftware value

        Note:
            Delegates to root_software property (CODING_RULE_V2_00017)
        """
        return self.root_software  # Delegates to property

    def setRootSoftware(self, value: "RootSwComposition") -> System:
        """
        AUTOSAR-compliant setter for rootSoftware with method chaining.

        Args:
            value: The rootSoftware to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_software property setter (gets validation automatically)
        """
        self.root_software = value  # Delegates to property setter
        return self

    def getSwCluster(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for swCluster.

        Returns:
            The swCluster value

        Note:
            Delegates to sw_cluster property (CODING_RULE_V2_00017)
        """
        return self.sw_cluster  # Delegates to property

    def getSystem(self) -> List[Chapter]:
        """
        AUTOSAR-compliant getter for system.

        Returns:
            The system value

        Note:
            Delegates to system property (CODING_RULE_V2_00017)
        """
        return self.system  # Delegates to property

    def getSystemVersion(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for systemVersion.

        Returns:
            The systemVersion value

        Note:
            Delegates to system_version property (CODING_RULE_V2_00017)
        """
        return self.system_version  # Delegates to property

    def setSystemVersion(self, value: "RevisionLabelString") -> System:
        """
        AUTOSAR-compliant setter for systemVersion with method chaining.

        Args:
            value: The systemVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_version property setter (gets validation automatically)
        """
        self.system_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_container_i_pdu(self, value: Optional[ByteOrderEnum]) -> System:
        """
        Set containerIPdu and return self for chaining.

        Args:
            value: The containerIPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_container_i_pdu("value")
        """
        self.container_i_pdu = value  # Use property setter (gets validation)
        return self

    def with_ecu_extract_version(self, value: Optional[RevisionLabelString]) -> System:
        """
        Set ecuExtractVersion and return self for chaining.

        Args:
            value: The ecuExtractVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_extract_version("value")
        """
        self.ecu_extract_version = value  # Use property setter (gets validation)
        return self

    def with_pnc_vector(self, value: Optional[PositiveInteger]) -> System:
        """
        Set pncVector and return self for chaining.

        Args:
            value: The pncVector to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_vector("value")
        """
        self.pnc_vector = value  # Use property setter (gets validation)
        return self

    def with_pnc_vector_offset(self, value: Optional[PositiveInteger]) -> System:
        """
        Set pncVectorOffset and return self for chaining.

        Args:
            value: The pncVectorOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_vector_offset("value")
        """
        self.pnc_vector_offset = value  # Use property setter (gets validation)
        return self

    def with_root_software(self, value: Optional[RootSwComposition]) -> System:
        """
        Set rootSoftware and return self for chaining.

        Args:
            value: The rootSoftware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_software("value")
        """
        self.root_software = value  # Use property setter (gets validation)
        return self

    def with_system_version(self, value: Optional[RevisionLabelString]) -> System:
        """
        Set systemVersion and return self for chaining.

        Args:
            value: The systemVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_version("value")
        """
        self.system_version = value  # Use property setter (gets validation)
        return self



class RootSwCompositionPrototype(Identifiable):
    """
    The RootSwCompositionPrototype represents the top-level-composition of
    software components within a given System. According to the use case of the
    System, this may for example be a more or less complete VFB description, the
    software of a System Extract or the software of a flat ECU Extract with only
    atomic SWCs. Therefore the RootSwComposition will only occasionally contain
    all atomic software components that are used in a complete VFB System. The
    OEM is primarily interested in the required functionality and the interfaces
    defining the integration of the Software Component into the System. The
    internal structure of such a component contains often substantial
    intellectual property of a supplier. Therefore a top-level software
    composition will often contain empty compositions which represent
    subsystems. The contained SwComponentPrototypes are fully specified by their
    SwComponentTypes (including Port Prototypes, PortInterfaces,
    VariableDataPrototypes, SwcInternalBehavior etc.), and their ports are
    interconnected using SwConnectorPrototypes.

    Package: M2::AUTOSARTemplates::SystemTemplate::RootSwCompositionPrototype

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1003, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 186, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 240, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 18, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Used CalibrationParameterValueSet for instance specific initialization of
                # calibration parameters.
        # atpSplitable.
        self._calibration: List[CalibrationParameter] = []

    @property
    def calibration(self) -> List[CalibrationParameter]:
        """Get calibration (Pythonic accessor)."""
        return self._calibration
        # The FlatMap used in the scope of this RootSw.
        self._flatMap: Optional[FlatMap] = None

    @property
    def flat_map(self) -> Optional[FlatMap]:
        """Get flatMap (Pythonic accessor)."""
        return self._flatMap

    @flat_map.setter
    def flat_map(self, value: Optional[FlatMap]) -> None:
        """
        Set flatMap with validation.

        Args:
            value: The flatMap to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flatMap = None
            return

        if not isinstance(value, FlatMap):
            raise TypeError(
                f"flatMap must be FlatMap or None, got {type(value).__name__}"
            )
        self._flatMap = value
        # that includes all Component instances of the system.
        self._software: Optional["CompositionSw"] = None

    @property
    def software(self) -> Optional["CompositionSw"]:
        """Get software (Pythonic accessor)."""
        return self._software

    @software.setter
    def software(self, value: Optional["CompositionSw"]) -> None:
        """
        Set software with validation.

        Args:
            value: The software to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._software = None
            return

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"software must be CompositionSw or None, got {type(value).__name__}"
            )
        self._software = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalibration(self) -> List[CalibrationParameter]:
        """
        AUTOSAR-compliant getter for calibration.

        Returns:
            The calibration value

        Note:
            Delegates to calibration property (CODING_RULE_V2_00017)
        """
        return self.calibration  # Delegates to property

    def getFlatMap(self) -> "FlatMap":
        """
        AUTOSAR-compliant getter for flatMap.

        Returns:
            The flatMap value

        Note:
            Delegates to flat_map property (CODING_RULE_V2_00017)
        """
        return self.flat_map  # Delegates to property

    def setFlatMap(self, value: "FlatMap") -> RootSwCompositionPrototype:
        """
        AUTOSAR-compliant setter for flatMap with method chaining.

        Args:
            value: The flatMap to set

        Returns:
            self for method chaining

        Note:
            Delegates to flat_map property setter (gets validation automatically)
        """
        self.flat_map = value  # Delegates to property setter
        return self

    def getSoftware(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for software.

        Returns:
            The software value

        Note:
            Delegates to software property (CODING_RULE_V2_00017)
        """
        return self.software  # Delegates to property

    def setSoftware(self, value: "CompositionSw") -> RootSwCompositionPrototype:
        """
        AUTOSAR-compliant setter for software with method chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Note:
            Delegates to software property setter (gets validation automatically)
        """
        self.software = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_flat_map(self, value: Optional[FlatMap]) -> RootSwCompositionPrototype:
        """
        Set flatMap and return self for chaining.

        Args:
            value: The flatMap to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flat_map("value")
        """
        self.flat_map = value  # Use property setter (gets validation)
        return self

    def with_software(self, value: Optional["CompositionSw"]) -> RootSwCompositionPrototype:
        """
        Set software and return self for chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software("value")
        """
        self.software = value  # Use property setter (gets validation)
        return self



class ClientIdDefinitionSet(ARElement):
    """
    Set of Client Identifiers that are used for inter-ECU client-server
    communication in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate::ClientIdDefinitionSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 44, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of a Client Identifier that will be used by the in a inter-ECU
                # client-server communication.
        # atpVariation.
        self._clientId: List[ClientIdDefinition] = []

    @property
    def client_id(self) -> List[ClientIdDefinition]:
        """Get clientId (Pythonic accessor)."""
        return self._clientId

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientId(self) -> List[ClientIdDefinition]:
        """
        AUTOSAR-compliant getter for clientId.

        Returns:
            The clientId value

        Note:
            Delegates to client_id property (CODING_RULE_V2_00017)
        """
        return self.client_id  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ClientIdDefinition(Identifiable):
    """
    Several clients in one client-ECU can communicate via inter-ECU
    client-server communication with a server on a different ECU, if a client
    identifier is used to distinguish the different clients. The Client
    Identifier of the transaction handle that is used by the RTE can be defined
    by this element.

    Package: M2::AUTOSARTemplates::SystemTemplate::ClientIdDefinition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 45, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Client Identifier of the transaction handle used for an server
        # communication is defined by this defined the RTE generator shall use this
        # client.
        self._clientId: Optional[Numerical] = None

    @property
    def client_id(self) -> Optional[Numerical]:
        """Get clientId (Pythonic accessor)."""
        return self._clientId

    @client_id.setter
    def client_id(self, value: Optional[Numerical]) -> None:
        """
        Set clientId with validation.

        Args:
            value: The clientId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientId = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"clientId must be Numerical or None, got {type(value).__name__}"
            )
        self._clientId = value
        # client.
        # by: OperationInSystem.
        self._clientServerInstanceRef: Optional[ClientServerOperation] = None

    @property
    def client_server_instance_ref(self) -> Optional[ClientServerOperation]:
        """Get clientServerInstanceRef (Pythonic accessor)."""
        return self._clientServerInstanceRef

    @client_server_instance_ref.setter
    def client_server_instance_ref(self, value: Optional[ClientServerOperation]) -> None:
        """
        Set clientServerInstanceRef with validation.

        Args:
            value: The clientServerInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientServerInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"clientServerInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._clientServerInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientId(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for clientId.

        Returns:
            The clientId value

        Note:
            Delegates to client_id property (CODING_RULE_V2_00017)
        """
        return self.client_id  # Delegates to property

    def setClientId(self, value: "Numerical") -> ClientIdDefinition:
        """
        AUTOSAR-compliant setter for clientId with method chaining.

        Args:
            value: The clientId to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_id property setter (gets validation automatically)
        """
        self.client_id = value  # Delegates to property setter
        return self

    def getClientServerInstanceRef(self) -> ClientServerOperation:
        """
        AUTOSAR-compliant getter for clientServerInstanceRef.

        Returns:
            The clientServerInstanceRef value

        Note:
            Delegates to client_server_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.client_server_instance_ref  # Delegates to property

    def setClientServerInstanceRef(self, value: ClientServerOperation) -> ClientIdDefinition:
        """
        AUTOSAR-compliant setter for clientServerInstanceRef with method chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_server_instance_ref property setter (gets validation automatically)
        """
        self.client_server_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_client_id(self, value: Optional[Numerical]) -> ClientIdDefinition:
        """
        Set clientId and return self for chaining.

        Args:
            value: The clientId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_id("value")
        """
        self.client_id = value  # Use property setter (gets validation)
        return self

    def with_client_server_instance_ref(self, value: Optional[ClientServerOperation]) -> ClientIdDefinition:
        """
        Set clientServerInstanceRef and return self for chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server_instance_ref("value")
        """
        self.client_server_instance_ref = value  # Use property setter (gets validation)
        return self



class SystemMapping(Identifiable):
    """
    The system mapping aggregates all mapping aspects (mapping of SW components
    to ECUs, mapping of data elements to signals, and mapping constraints).

    Package: M2::AUTOSARTemplates::SystemTemplate::SystemMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 190, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Mapping of ApplicationPartitions to EcuPartitions Stereotypes: atpSplitable;
                # atpVariation Partition Tags: Mapping atp.
        # Splitkey=applicationPartitionToEcuPartition.
        self._application: List["ApplicationPartitionTo"] = []

    @property
    def application(self) -> List["ApplicationPartitionTo"]:
        """Get application (Pythonic accessor)."""
        return self._application
        # Mapping of an OsTaskProxy that was created in the context of a SwComponent to
        # an OsTaskProxy that was in the context of an Ecu.
        self._appOsTask: List["AppOsTaskProxyToEcu"] = []

    @property
    def app_os_task(self) -> List["AppOsTaskProxyToEcu"]:
        """Get appOsTask (Pythonic accessor)."""
        return self._appOsTask
        # Mappings between Mode Management PortGroups and communication channels.
        # atpSplitable; atpVariation.
        self._com: List["ComManagement"] = []

    @property
    def com(self) -> List["ComManagement"]:
        """Get com (Pythonic accessor)."""
        return self._com
        # This aggregation represents the collection of crypto mappings in the context
        # of the enclosing System atpVariation.
        self._cryptoService: List[RefType] = []

    @property
    def crypto_service(self) -> List[RefType]:
        """Get cryptoService (Pythonic accessor)."""
        return self._cryptoService
        # The data mappings defined.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dataMapping: List[RefType] = []

    @property
    def data_mapping(self) -> List[RefType]:
        """Get dataMapping (Pythonic accessor)."""
        return self._dataMapping
        # Collection of DdsISignalToDdsTopicMappings.
        # Stereotypes: atpSplitable; atpVariation.
        self._ddsISignalTo: List["DdsCpISignalToDds"] = []

    @property
    def dds_i_signal_to(self) -> List["DdsCpISignalToDds"]:
        """Get ddsISignalTo (Pythonic accessor)."""
        return self._ddsISignalTo
        # Mapping of hardware related topology elements onto their definitions in the
                # ECU Resource Template.
        # ECU Resource type might be variable.
        # atpVariation.
        self._ecuResource: List[RefType] = []

    @property
    def ecu_resource(self) -> List[RefType]:
        """Get ecuResource (Pythonic accessor)."""
        return self._ecuResource
        # Mapping of a J1939ControllerApplication to a J1939Nm Node.
        self._j1939Controller: List["J1939Controller"] = []

    @property
    def j1939_controller(self) -> List["J1939Controller"]:
        """Get j1939Controller (Pythonic accessor)."""
        return self._j1939Controller
        # Constraints that limit the mapping freedom for the of SW components to ECUs.
        # atpVariation.
        self._mapping: List[RefType] = []

    @property
    def mapping(self) -> List[RefType]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping
        # Mappings between Virtual Function Clusters and Partial atpVariation.
        self._pncMapping: List[RefType] = []

    @property
    def pnc_mapping(self) -> List[RefType]:
        """Get pncMapping (Pythonic accessor)."""
        return self._pncMapping
        # maps a communication resource to CP Software Clusters Stereotypes:
        # atpSplitable; atpVariation Mapping ResourceMapping Tags:.
        self._portElementTo: List["PortElementTo"] = []

    @property
    def port_element_to(self) -> List["PortElementTo"]:
        """Get portElementTo (Pythonic accessor)."""
        return self._portElementTo
        # Resource estimations for this set of mappings, zero or per ECU instance.
        # ECUs are variable.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._resource: List["EcuResourceEstimation"] = []

    @property
    def resource(self) -> List["EcuResourceEstimation"]:
        """Get resource (Pythonic accessor)."""
        return self._resource
        # Maps a Software Cluster resource to an Application Partition to restrict the
                # usage.
        # Stereotypes: atpSplitable; atpVariation Mapping Tags:.
        self._resourceTo: List["CpSoftwareCluster"] = []

    @property
    def resource_to(self) -> List["CpSoftwareCluster"]:
        """Get resourceTo (Pythonic accessor)."""
        return self._resourceTo
        # Separation constraint that limits the mapping freedom for the mapping of
        # RteEvents to OsTasks in the System.
        self._rteEvent: List["RteEventInSystem"] = []

    @property
    def rte_event(self) -> List["RteEventInSystem"]:
        """Get rteEvent (Pythonic accessor)."""
        return self._rteEvent
        # Constraint that enforces a mapping of RteEvent to a particular OsTask in the
        # System context.
        self._rteEventToOs: List["RteEventInSystemToOs"] = []

    @property
    def rte_event_to_os(self) -> List["RteEventInSystemToOs"]:
        """Get rteEventToOs (Pythonic accessor)."""
        return self._rteEventToOs
        # Constraints that limit the mapping freedom for the of data elements to
                # signals.
        # atpVariation.
        self._signalPath: List["SignalPathConstraint"] = []

    @property
    def signal_path(self) -> List["SignalPathConstraint"]:
        """Get signalPath (Pythonic accessor)."""
        return self._signalPath
        # maps a service resource to CP Software Clusters Stereotypes: atpSplitable;
        # atpVariation Mapping Tags:.
        self._softwareCluster: List["CpSoftwareClusterTo"] = []

    @property
    def software_cluster(self) -> List["CpSoftwareClusterTo"]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster
        # The mappings of SW cluster to ECUs.
        # Stereotypes: atpSplitable; atpVariation.
        self._swCluster: List["CpSoftwareClusterTo"] = []

    @property
    def sw_cluster(self) -> List["CpSoftwareClusterTo"]:
        """Get swCluster (Pythonic accessor)."""
        return self._swCluster
        # Allows to map a given SwComponentPrototype to a formally defined partition at
                # a point in time when the EcuInstance is not yet known or defined.
        # atpSplitable; atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate
                # R23-11.
        self._swcTo: List["SwcToApplication"] = []

    @property
    def swc_to(self) -> List["SwcToApplication"]:
        """Get swcTo (Pythonic accessor)."""
        return self._swcTo
        # The mappings of AtomicSoftwareComponent Instances to because SwcToEcuMapping
        # is atpVariation.
        self._swImplMapping: List[RefType] = []

    @property
    def sw_impl_mapping(self) -> List[RefType]:
        """Get swImplMapping (Pythonic accessor)."""
        return self._swImplMapping
        # The mappings of SW components to ECUs.
        # shall be mapped to other ECUs.
        # atpVariation.
        self._swMapping: List[RefType] = []

    @property
    def sw_mapping(self) -> List[RefType]:
        """Get swMapping (Pythonic accessor)."""
        return self._swMapping
        # Mapping of a communication resource to a SystemSignal Group.
        # Stereotypes: atpSplitable; atpVariation Mapping Tags:.
        self._systemSignal: List[RefType] = []

    @property
    def system_signal(self) -> List[RefType]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal
        # Mapping of a communication resource to a SystemSignal.
        # Stereotypes: atpSplitable; atpVariation Mapping ResourceMapping Tags:.
        self._systemSignalTo: List["SystemSignalTo"] = []

    @property
    def system_signal_to(self) -> List["SystemSignalTo"]:
        """Get systemSignalTo (Pythonic accessor)."""
        return self._systemSignalTo

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> List["ApplicationPartitionTo"]:
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def getAppOsTask(self) -> List["AppOsTaskProxyToEcu"]:
        """
        AUTOSAR-compliant getter for appOsTask.

        Returns:
            The appOsTask value

        Note:
            Delegates to app_os_task property (CODING_RULE_V2_00017)
        """
        return self.app_os_task  # Delegates to property

    def getCom(self) -> List["ComManagement"]:
        """
        AUTOSAR-compliant getter for com.

        Returns:
            The com value

        Note:
            Delegates to com property (CODING_RULE_V2_00017)
        """
        return self.com  # Delegates to property

    def getCryptoService(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for cryptoService.

        Returns:
            The cryptoService value

        Note:
            Delegates to crypto_service property (CODING_RULE_V2_00017)
        """
        return self.crypto_service  # Delegates to property

    def getDataMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataMapping.

        Returns:
            The dataMapping value

        Note:
            Delegates to data_mapping property (CODING_RULE_V2_00017)
        """
        return self.data_mapping  # Delegates to property

    def getDdsISignalTo(self) -> List["DdsCpISignalToDds"]:
        """
        AUTOSAR-compliant getter for ddsISignalTo.

        Returns:
            The ddsISignalTo value

        Note:
            Delegates to dds_i_signal_to property (CODING_RULE_V2_00017)
        """
        return self.dds_i_signal_to  # Delegates to property

    def getEcuResource(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for ecuResource.

        Returns:
            The ecuResource value

        Note:
            Delegates to ecu_resource property (CODING_RULE_V2_00017)
        """
        return self.ecu_resource  # Delegates to property

    def getJ1939Controller(self) -> List["J1939Controller"]:
        """
        AUTOSAR-compliant getter for j1939Controller.

        Returns:
            The j1939Controller value

        Note:
            Delegates to j1939_controller property (CODING_RULE_V2_00017)
        """
        return self.j1939_controller  # Delegates to property

    def getMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    def getPncMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pncMapping.

        Returns:
            The pncMapping value

        Note:
            Delegates to pnc_mapping property (CODING_RULE_V2_00017)
        """
        return self.pnc_mapping  # Delegates to property

    def getPortElementTo(self) -> List["PortElementTo"]:
        """
        AUTOSAR-compliant getter for portElementTo.

        Returns:
            The portElementTo value

        Note:
            Delegates to port_element_to property (CODING_RULE_V2_00017)
        """
        return self.port_element_to  # Delegates to property

    def getResource(self) -> List["EcuResourceEstimation"]:
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def getResourceTo(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for resourceTo.

        Returns:
            The resourceTo value

        Note:
            Delegates to resource_to property (CODING_RULE_V2_00017)
        """
        return self.resource_to  # Delegates to property

    def getRteEvent(self) -> List["RteEventInSystem"]:
        """
        AUTOSAR-compliant getter for rteEvent.

        Returns:
            The rteEvent value

        Note:
            Delegates to rte_event property (CODING_RULE_V2_00017)
        """
        return self.rte_event  # Delegates to property

    def getRteEventToOs(self) -> List["RteEventInSystemToOs"]:
        """
        AUTOSAR-compliant getter for rteEventToOs.

        Returns:
            The rteEventToOs value

        Note:
            Delegates to rte_event_to_os property (CODING_RULE_V2_00017)
        """
        return self.rte_event_to_os  # Delegates to property

    def getSignalPath(self) -> List["SignalPathConstraint"]:
        """
        AUTOSAR-compliant getter for signalPath.

        Returns:
            The signalPath value

        Note:
            Delegates to signal_path property (CODING_RULE_V2_00017)
        """
        return self.signal_path  # Delegates to property

    def getSoftwareCluster(self) -> List["CpSoftwareClusterTo"]:
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def getSwCluster(self) -> List["CpSoftwareClusterTo"]:
        """
        AUTOSAR-compliant getter for swCluster.

        Returns:
            The swCluster value

        Note:
            Delegates to sw_cluster property (CODING_RULE_V2_00017)
        """
        return self.sw_cluster  # Delegates to property

    def getSwcTo(self) -> List["SwcToApplication"]:
        """
        AUTOSAR-compliant getter for swcTo.

        Returns:
            The swcTo value

        Note:
            Delegates to swc_to property (CODING_RULE_V2_00017)
        """
        return self.swc_to  # Delegates to property

    def getSwImplMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for swImplMapping.

        Returns:
            The swImplMapping value

        Note:
            Delegates to sw_impl_mapping property (CODING_RULE_V2_00017)
        """
        return self.sw_impl_mapping  # Delegates to property

    def getSwMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for swMapping.

        Returns:
            The swMapping value

        Note:
            Delegates to sw_mapping property (CODING_RULE_V2_00017)
        """
        return self.sw_mapping  # Delegates to property

    def getSystemSignal(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def getSystemSignalTo(self) -> List["SystemSignalTo"]:
        """
        AUTOSAR-compliant getter for systemSignalTo.

        Returns:
            The systemSignalTo value

        Note:
            Delegates to system_signal_to property (CODING_RULE_V2_00017)
        """
        return self.system_signal_to  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ComManagementMapping(Identifiable):
    """
    Describes a mapping between one or several Mode Management PortGroups and
    communication channels.

    Package: M2::AUTOSARTemplates::SystemTemplate::ComManagementMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 282, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # channel.
        # This reference is optional in that the System Description doesn’t use a
                # complete Description (VFB View).
        # This inclusion of legacy systems.
        # by: PortGroupInSystem.
        self._com: List[RefType] = []

    @property
    def com(self) -> List[RefType]:
        """Get com (Pythonic accessor)."""
        return self._com
        # This reference maps the Mode Management PortGroup network to communication
        # channels.
        self._physical: List[PhysicalChannel] = []

    @property
    def physical(self) -> List[PhysicalChannel]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCom(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for com.

        Returns:
            The com value

        Note:
            Delegates to com property (CODING_RULE_V2_00017)
        """
        return self.com  # Delegates to property

    def getPhysical(self) -> List[PhysicalChannel]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939SharedAddressCluster(Identifiable):
    """
    This meta-class represents the ability to identify several J1939Clusters
    that share a common address space for the routing of messages

    Package: M2::AUTOSARTemplates::SystemTemplate::J1939SharedAddressCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 694, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This identifies the J1939Clusters that share a common space.
        self._participating: List["J1939Cluster"] = []

    @property
    def participating(self) -> List["J1939Cluster"]:
        """Get participating (Pythonic accessor)."""
        return self._participating

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParticipating(self) -> List["J1939Cluster"]:
        """
        AUTOSAR-compliant getter for participating.

        Returns:
            The participating value

        Note:
            Delegates to participating property (CODING_RULE_V2_00017)
        """
        return self.participating  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class PortElementToCommunicationResourceMapping(Identifiable):
    """
    This meta class maps a communication resource to CP Software Clusters. In
    this case the kind of Port Prototype specified whether the Software Cluster
    has to provide or to require the resource.

    Package: M2::AUTOSARTemplates::SystemTemplate::PortElementToCommunicationResourceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 905, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # resource by: OperationInSystem.
        self._clientServerInstanceRef: Optional[ClientServerOperation] = None

    @property
    def client_server_instance_ref(self) -> Optional[ClientServerOperation]:
        """Get clientServerInstanceRef (Pythonic accessor)."""
        return self._clientServerInstanceRef

    @client_server_instance_ref.setter
    def client_server_instance_ref(self, value: Optional[ClientServerOperation]) -> None:
        """
        Set clientServerInstanceRef with validation.

        Args:
            value: The clientServerInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientServerInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"clientServerInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._clientServerInstanceRef = value
        # Communication resource for which the mapping applies.
        self._communication: Optional[CpSoftwareCluster] = None

    @property
    def communication(self) -> Optional[CpSoftwareCluster]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional[CpSoftwareCluster]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"communication must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._communication = value
        # communication resource implemented by: ModeDeclarationGroup.
        self._mode: Optional[RefType] = None

    @property
    def mode(self) -> Optional[RefType]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional[RefType]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        self._mode = value
        # communication resource.
        # by: ParameterDataPrototype.
        self._parameterData: Optional[ParameterData] = None

    @property
    def parameter_data(self) -> Optional[ParameterData]:
        """Get parameterData (Pythonic accessor)."""
        return self._parameterData

    @parameter_data.setter
    def parameter_data(self, value: Optional[ParameterData]) -> None:
        """
        Set parameterData with validation.

        Args:
            value: The parameterData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameterData = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"parameterData must be ParameterData or None, got {type(value).__name__}"
            )
        self._parameterData = value
        # by: TriggerInSystemInstance.
        self._triggerRef: Optional[RefType] = None

    @property
    def trigger_ref(self) -> Optional[RefType]:
        """Get triggerRef (Pythonic accessor)."""
        return self._triggerRef

    @trigger_ref.setter
    def trigger_ref(self, value: Optional[RefType]) -> None:
        """
        Set triggerRef with validation.

        Args:
            value: The triggerRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerRef = None
            return

        self._triggerRef = value
        # resource by: VariableDataPrototypeIn.
        self._variableDataSystemInstanceRef: Optional[RefType] = None

    @property
    def variable_data_system_instance_ref(self) -> Optional[RefType]:
        """Get variableDataSystemInstanceRef (Pythonic accessor)."""
        return self._variableDataSystemInstanceRef

    @variable_data_system_instance_ref.setter
    def variable_data_system_instance_ref(self, value: Optional[RefType]) -> None:
        """
        Set variableDataSystemInstanceRef with validation.

        Args:
            value: The variableDataSystemInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableDataSystemInstanceRef = None
            return

        self._variableDataSystemInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientServerInstanceRef(self) -> ClientServerOperation:
        """
        AUTOSAR-compliant getter for clientServerInstanceRef.

        Returns:
            The clientServerInstanceRef value

        Note:
            Delegates to client_server_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.client_server_instance_ref  # Delegates to property

    def setClientServerInstanceRef(self, value: ClientServerOperation) -> PortElementToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for clientServerInstanceRef with method chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_server_instance_ref property setter (gets validation automatically)
        """
        self.client_server_instance_ref = value  # Delegates to property setter
        return self

    def getCommunication(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "CpSoftwareCluster") -> PortElementToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: RefType) -> PortElementToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getParameterData(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for parameterData.

        Returns:
            The parameterData value

        Note:
            Delegates to parameter_data property (CODING_RULE_V2_00017)
        """
        return self.parameter_data  # Delegates to property

    def setParameterData(self, value: "ParameterData") -> PortElementToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for parameterData with method chaining.

        Args:
            value: The parameterData to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter_data property setter (gets validation automatically)
        """
        self.parameter_data = value  # Delegates to property setter
        return self

    def getTriggerRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for triggerRef.

        Returns:
            The triggerRef value

        Note:
            Delegates to trigger_ref property (CODING_RULE_V2_00017)
        """
        return self.trigger_ref  # Delegates to property

    def setTriggerRef(self, value: RefType) -> PortElementToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for triggerRef with method chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger_ref property setter (gets validation automatically)
        """
        self.trigger_ref = value  # Delegates to property setter
        return self

    def getVariableDataSystemInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for variableDataSystemInstanceRef.

        Returns:
            The variableDataSystemInstanceRef value

        Note:
            Delegates to variable_data_system_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.variable_data_system_instance_ref  # Delegates to property

    def setVariableDataSystemInstanceRef(self, value: RefType) -> PortElementToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for variableDataSystemInstanceRef with method chaining.

        Args:
            value: The variableDataSystemInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable_data_system_instance_ref property setter (gets validation automatically)
        """
        self.variable_data_system_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_client_server_instance_ref(self, value: Optional[ClientServerOperation]) -> PortElementToCommunicationResourceMapping:
        """
        Set clientServerInstanceRef and return self for chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server_instance_ref("value")
        """
        self.client_server_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_communication(self, value: Optional[CpSoftwareCluster]) -> PortElementToCommunicationResourceMapping:
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional[RefType]) -> PortElementToCommunicationResourceMapping:
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_parameter_data(self, value: Optional[ParameterData]) -> PortElementToCommunicationResourceMapping:
        """
        Set parameterData and return self for chaining.

        Args:
            value: The parameterData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter_data("value")
        """
        self.parameter_data = value  # Use property setter (gets validation)
        return self

    def with_trigger_ref(self, value: Optional[RefType]) -> PortElementToCommunicationResourceMapping:
        """
        Set triggerRef and return self for chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_ref("value")
        """
        self.trigger_ref = value  # Use property setter (gets validation)
        return self

    def with_variable_data_system_instance_ref(self, value: Optional[RefType]) -> PortElementToCommunicationResourceMapping:
        """
        Set variableDataSystemInstanceRef and return self for chaining.

        Args:
            value: The variableDataSystemInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_data_system_instance_ref("value")
        """
        self.variable_data_system_instance_ref = value  # Use property setter (gets validation)
        return self


__all__ = [
    System,
    RootSwCompositionPrototype,
    ClientIdDefinitionSet,
    ClientIdDefinition,
    SystemMapping,
    ComManagementMapping,
    J1939SharedAddressCluster,
    PortElementToCommunicationResourceMapping,
]
