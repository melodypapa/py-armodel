from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SystemMapping(Identifiable):
    """
    The system mapping aggregates all mapping aspects (mapping of SW components
    to ECUs, mapping of data elements to signals, and mapping constraints).

    Package: M2::AUTOSARTemplates::SystemTemplate

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
