from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class System(ARElement):
    """
    The top level element of the System Description. The System description
    defines five major elements: Topology, Software, Communication, Mapping and
    Mapping Constraints. The System element directly aggregates the elements
    describing the Software, Mapping and Mapping Constraints; it contains a
    reference to an ASAM FIBEX description specifying Communication and
    Topology.

    Package: M2::AUTOSARTemplates::SystemTemplate

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
        self._containerIPdu: Optional["ByteOrderEnum"] = None

    @property
    def container_i_pdu(self) -> Optional["ByteOrderEnum"]:
        """Get containerIPdu (Pythonic accessor)."""
        return self._containerIPdu

    @container_i_pdu.setter
    def container_i_pdu(self, value: Optional["ByteOrderEnum"]) -> None:
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
        self._ecuExtractVersion: Optional["RevisionLabelString"] = None

    @property
    def ecu_extract_version(self) -> Optional["RevisionLabelString"]:
        """Get ecuExtractVersion (Pythonic accessor)."""
        return self._ecuExtractVersion

    @ecu_extract_version.setter
    def ecu_extract_version(self, value: Optional["RevisionLabelString"]) -> None:
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
        # Elements used within a System Description shall from the System Element.
        # order to describe a product-line, all Fibex be optional.
        # atpVariation.
        self._fibexElement: List["FibexElement"] = []

    @property
    def fibex_element(self) -> List["FibexElement"]:
        """Get fibexElement (Pythonic accessor)."""
        return self._fibexElement
        # This reference identifies the InterpolationRoutineMapping Sets that are
        # relevant in the context of the enclosing.
        self._interpolation: List["InterpolationRoutine"] = []

    @property
    def interpolation(self) -> List["InterpolationRoutine"]:
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
        self._pncVector: Optional["PositiveInteger"] = None

    @property
    def pnc_vector(self) -> Optional["PositiveInteger"]:
        """Get pncVector (Pythonic accessor)."""
        return self._pncVector

    @pnc_vector.setter
    def pnc_vector(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pncVector must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pncVector = value
        # information vector that in bytes as an index starting with 0.
        self._pncVectorOffset: Optional["PositiveInteger"] = None

    @property
    def pnc_vector_offset(self) -> Optional["PositiveInteger"]:
        """Get pncVectorOffset (Pythonic accessor)."""
        return self._pncVectorOffset

    @pnc_vector_offset.setter
    def pnc_vector_offset(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pncVectorOffset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pncVectorOffset = value
                # components in the System in a hierarchical element is not required when the
                # System used for a network-only use-case.
        # RootSwCompositionPrototype can vary.
        # atpVariation.
        self._rootSoftware: Optional["RootSwComposition"] = None

    @property
    def root_software(self) -> Optional["RootSwComposition"]:
        """Get rootSoftware (Pythonic accessor)."""
        return self._rootSoftware

    @root_software.setter
    def root_software(self, value: Optional["RootSwComposition"]) -> None:
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
        self._swCluster: List["CpSoftwareCluster"] = []

    @property
    def sw_cluster(self) -> List["CpSoftwareCluster"]:
        """Get swCluster (Pythonic accessor)."""
        return self._swCluster
        # Possibility to provide additional documentation while the System.
        # The System documentation can be several chapters.
        # atpVariation.
        self._system: List["Chapter"] = []

    @property
    def system(self) -> List["Chapter"]:
        """Get system (Pythonic accessor)."""
        return self._system
        # Version number of the System Description.
        self._systemVersion: Optional["RevisionLabelString"] = None

    @property
    def system_version(self) -> Optional["RevisionLabelString"]:
        """Get systemVersion (Pythonic accessor)."""
        return self._systemVersion

    @system_version.setter
    def system_version(self, value: Optional["RevisionLabelString"]) -> None:
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

    def with_client_id(self, value):
        """
        Set client_id and return self for chaining.

        Args:
            value: The client_id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_id("value")
        """
        self.client_id = value  # Use property setter (gets validation)
        return self

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

    def getContainerIPdu(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for containerIPdu.

        Returns:
            The containerIPdu value

        Note:
            Delegates to container_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.container_i_pdu  # Delegates to property

    def setContainerIPdu(self, value: "ByteOrderEnum") -> "System":
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

    def setEcuExtractVersion(self, value: "RevisionLabelString") -> "System":
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

    def getFibexElement(self) -> List["FibexElement"]:
        """
        AUTOSAR-compliant getter for fibexElement.

        Returns:
            The fibexElement value

        Note:
            Delegates to fibex_element property (CODING_RULE_V2_00017)
        """
        return self.fibex_element  # Delegates to property

    def getInterpolation(self) -> List["InterpolationRoutine"]:
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

    def getPncVector(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pncVector.

        Returns:
            The pncVector value

        Note:
            Delegates to pnc_vector property (CODING_RULE_V2_00017)
        """
        return self.pnc_vector  # Delegates to property

    def setPncVector(self, value: "PositiveInteger") -> "System":
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

    def getPncVectorOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pncVectorOffset.

        Returns:
            The pncVectorOffset value

        Note:
            Delegates to pnc_vector_offset property (CODING_RULE_V2_00017)
        """
        return self.pnc_vector_offset  # Delegates to property

    def setPncVectorOffset(self, value: "PositiveInteger") -> "System":
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

    def setRootSoftware(self, value: "RootSwComposition") -> "System":
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

    def getSystem(self) -> List["Chapter"]:
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

    def setSystemVersion(self, value: "RevisionLabelString") -> "System":
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

    def with_container_i_pdu(self, value: Optional["ByteOrderEnum"]) -> "System":
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

    def with_ecu_extract_version(self, value: Optional["RevisionLabelString"]) -> "System":
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

    def with_pnc_vector(self, value: Optional["PositiveInteger"]) -> "System":
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

    def with_pnc_vector_offset(self, value: Optional["PositiveInteger"]) -> "System":
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

    def with_root_software(self, value: Optional["RootSwComposition"]) -> "System":
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

    def with_system_version(self, value: Optional["RevisionLabelString"]) -> "System":
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
