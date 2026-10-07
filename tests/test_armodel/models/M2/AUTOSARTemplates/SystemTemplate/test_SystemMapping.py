"""
This module contains tests for the SystemMapping class
in the AUTOSAR SystemTemplate module (R23-11, Table 5.1, p.193).
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    J1939ControllerApplicationToJ1939NmNodeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import (
    VariationPointCapable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import (
    ComManagementMapping,
    SecOcCryptoServiceMapping,
    SystemMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import TriggerToSignalMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsCpISignalToDdsTopicMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping import PncMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import (
    AppOsTaskProxyToEcuTaskProxyMapping,
    RteEventInSystemSeparation,
    RteEventInSystemToOsTaskProxyMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import CommonSignalPath
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    CpSoftwareClusterResourceToApplicationPartitionMapping,
    CpSoftwareClusterToApplicationPartitionMapping,
    CpSoftwareClusterToEcuInstanceMapping,
    CpSoftwareClusterToResourceMapping,
    SystemSignalGroupToCommunicationResourceMapping,
    SystemSignalToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    ApplicationPartitionToEcuPartitionMapping,
    ComponentClustering,
    EcuResourceEstimation,
    MappingConstraint,
    SwcToApplicationPartitionMapping,
    SwcToEcuMapping,
    SwcToImplMapping,
)

SPEC_NOTE = "The system mapping aggregates all mapping aspects (mapping of SW components to ECUs, mapping of data elements to signals, and mapping constraints)."

MEMBER_FACTORIES = {
    "applicationPartitionToEcuPartitionMappings": lambda ar_root: ApplicationPartitionToEcuPartitionMapping(ar_root, "AppPartitionToEcuPartitionMapping"),
    "appOsTaskProxyToEcuTaskProxyMappings": lambda ar_root: AppOsTaskProxyToEcuTaskProxyMapping(ar_root, "AppOsTaskProxyToEcuTaskProxyMapping"),
    "comManagementMappings": lambda ar_root: ComManagementMapping(ar_root, "ComManagementMapping"),
    "cryptoServiceMappings": lambda ar_root: SecOcCryptoServiceMapping(ar_root, "CryptoServiceMapping"),
    "dataMappings": lambda ar_root: TriggerToSignalMapping(),
    "ddsISignalToTopicMappings": lambda ar_root: DdsCpISignalToDdsTopicMapping(),
    "ecuResourceMappings": lambda ar_root: ECUMapping(ar_root, "EcuResourceMapping"),
    "j1939ControllerApplicationToJ1939NmNodeMappings": lambda ar_root: J1939ControllerApplicationToJ1939NmNodeMapping(),
    "mappingConstraints": lambda ar_root: ComponentClustering(),
    "pncMappings": lambda ar_root: PncMapping(),
    "portElementToComResourceMappings": lambda ar_root: PortElementToCommunicationResourceMapping(ar_root, "PortElementToComResourceMapping"),
    "resourceEstimations": lambda ar_root: EcuResourceEstimation(),
    "resourceToApplicationPartitionMappings": lambda ar_root: CpSoftwareClusterResourceToApplicationPartitionMapping(ar_root, "ResourceToApplicationPartitionMapping"),
    "rteEventSeparations": lambda ar_root: RteEventInSystemSeparation(ar_root, "RteEventSeparation"),
    "rteEventToOsTaskProxyMappings": lambda ar_root: RteEventInSystemToOsTaskProxyMapping(ar_root, "RteEventToOsTaskProxyMapping"),
    "signalPathConstraints": lambda ar_root: CommonSignalPath(),
    "softwareClusterToApplicationPartitionMappings": lambda ar_root: CpSoftwareClusterToApplicationPartitionMapping(ar_root, "SoftwareClusterToApplicationPartitionMapping"),
    "softwareClusterToResourceMappings": lambda ar_root: CpSoftwareClusterToResourceMapping(ar_root, "SoftwareClusterToResourceMapping"),
    "swClusterMappings": lambda ar_root: CpSoftwareClusterToEcuInstanceMapping(ar_root, "SwClusterMapping"),
    "swcToApplicationPartitionMappings": lambda ar_root: SwcToApplicationPartitionMapping(ar_root, "SwcToApplicationPartitionMapping"),
    "swImplMappings": lambda ar_root: SwcToImplMapping(ar_root, "SwImplMapping"),
    "swMappings": lambda ar_root: SwcToEcuMapping(ar_root, "SwMapping"),
    "systemSignalGroupToComResourceMappings": lambda ar_root: SystemSignalGroupToCommunicationResourceMapping(ar_root, "SystemSignalGroupToComResourceMapping"),
    "systemSignalToComResourceMappings": lambda ar_root: SystemSignalToCommunicationResourceMapping(ar_root, "SystemSignalToComResourceMapping"),
}

ATTRIBUTE_NOTES = {
    "applicationPartitionToEcuPartitionMapping": "Mapping of ApplicationPartitions to EcuPartitions Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=applicationPartitionToEcuPartitionMapping.shortName, applicationPartitionToEcuPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild",
    "appOsTaskProxyToEcuTaskProxyMapping": "Mapping of an OsTaskProxy that was created in the context of a SwComponent to an OsTaskProxy that was created in the context of an Ecu.",
    "comManagementMapping": "Mappings between Mode Management PortGroups and communication channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comManagementMapping.shortName, comManagementMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "cryptoServiceMapping": "This aggregation represents the collection of crypto service mappings in the context of the enclosing System Mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=cryptoServiceMapping.shortName, cryptoServiceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild",
    "dataMapping": "The data mappings defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataMapping, dataMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild",
    "ddsISignalToTopicMapping": "Collection of DdsISignalToDdsTopicMappings. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ddsISignalToTopicMapping, ddsISignalToTopicMapping.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild",
    "ecuResourceMapping": "Mapping of hardware related topology elements onto their counterpart definitions in the ECU Resource Template. atpVariation: The ECU Resource type might be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuResourceMapping.shortName, ecuResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "j1939ControllerApplicationToJ1939NmNodeMapping": "Mapping of a J1939ControllerApplication to a J1939NmNode.",
    "mappingConstraint": "Constraints that limit the mapping freedom for the mapping of SW components to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mappingConstraint, mappingConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "pncMapping": "Mappings between Virtual Function Clusters and Partial Network Clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pncMapping, pncMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "portElementToComResourceMapping": "maps a communication resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portElementToComResourceMapping.shortName, portElementToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild",
    "resourceEstimation": "Resource estimations for this set of mappings, zero or one per ECU instance. atpVariation: Used ECUs are variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceEstimation, resourceEstimation.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "resourceToApplicationPartitionMapping": "Maps a Software Cluster resource to an Application Partition to restrict the usage. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceToApplicationPartitionMapping.shortName, resourceToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "rteEventSeparation": "Separation constraint that limits the mapping freedom for the mapping of RteEvents to OsTasks in the System context.",
    "rteEventToOsTaskProxyMapping": "Constraint that enforces a mapping of RteEvent to a particular OsTask in the System context.",
    "signalPathConstraint": "Constraints that limit the mapping freedom for the mapping of data elements to signals. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=signalPathConstraint, signalPathConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "softwareClusterToApplicationPartitionMapping": "The mapping of ApplicationPartitions to a CpSoftwareCluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToApplicationPartitionMapping.shortName, softwareClusterToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "softwareClusterToResourceMapping": "maps a service resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToResourceMapping.shortName, softwareClusterToResourceMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime",
    "swClusterMapping": "The mappings of SW cluster to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swClusterMapping.shortName, swClusterMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "swcToApplicationPartitionMapping": "Allows to map a given SwComponentPrototype to a formally defined partition at a point in time when the corresponding EcuInstance is not yet known or defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swcToApplicationPartitionMapping.shortName, swcToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild",
    "swImplMapping": "The mappings of AtomicSoftwareComponent Instances to Implementations. atpVariation: Derived, because SwcToEcuMapping is variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swImplMapping.shortName, swImplMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime",
    "swMapping": "The mappings of SW components to ECUs. atpVariation: SWC shall be mapped to other ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swMapping.shortName, swMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime",
    "systemSignalGroupToComResourceMapping": "Mapping of a communication resource to a SystemSignalGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalGroupToComResourceMapping.shortName, systemSignalGroupToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
    "systemSignalToComResourceMapping": "Mapping of a communication resource to a SystemSignal. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalToComResourceMapping.shortName, systemSignalToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime",
}

CREATE_FACTORIES = [
    ("createApplicationPartitionToEcuPartitionMapping", "applicationPartitionToEcuPartitionMappings"),
    ("createAppOsTaskProxyToEcuTaskProxyMapping", "appOsTaskProxyToEcuTaskProxyMappings"),
    ("createComManagementMapping", "comManagementMappings"),
    ("createSecOcCryptoServiceMapping", "cryptoServiceMappings"),
    ("createTlsCryptoServiceMapping", "cryptoServiceMappings"),
    ("createECUMapping", "ecuResourceMappings"),
    ("createPortElementToComResourceMapping", "portElementToComResourceMappings"),
    ("createSwcToApplicationPartitionMapping", "swcToApplicationPartitionMappings"),
    ("createSwcToImplMapping", "swImplMappings"),
    ("createSwcToEcuMapping", "swMappings"),
]


def _field_of(attr: str) -> str:
    return attr + "s"


class TestSystemMapping:
    def _create(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return SystemMapping(ar_root, "TestSystemMapping")

    def test_initialization(self):
        """Test that the SystemMapping is an Identifiable wired with parent and short name"""
        mapping = self._create()

        assert isinstance(mapping, Identifiable)
        assert isinstance(mapping, VariationPointCapable)
        assert isinstance(mapping, ARObject)
        assert mapping.getShortName() == "TestSystemMapping"
        for field in MEMBER_FACTORIES:
            assert getattr(mapping, "get" + field[0].upper() + field[1:])() == []

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 5.1)"""
        assert SystemMapping.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert SystemMapping.__init__.__doc__ is None

    def test_attribute_docstrings_are_spec_notes(self):
        """Test that the adder and getter docstrings carry the attribute Notes verbatim (Table 5.1)"""
        adder_exceptions = {"ecuResourceMapping", "swImplMapping", "swMapping"}
        for attr, note in ATTRIBUTE_NOTES.items():
            field = _field_of(attr)
            getter = getattr(SystemMapping, "get" + field[0].upper() + field[1:])
            assert getter.__doc__.strip() == note, "getter docstring drift: %s" % field
            if attr in adder_exceptions:
                assert not hasattr(SystemMapping, "add" + attr[0].upper() + attr[1:]), "unexpected adder: %s" % attr
            else:
                adder = getattr(SystemMapping, "add" + attr[0].upper() + attr[1:])
                assert adder.__doc__.strip().startswith(note), "adder docstring drift: %s" % attr
                assert "A None value is a no-op and does not add to %s." % field in adder.__doc__, "adder None-no-op note drift: %s" % attr

    def test_add_get_round_trip(self):
        """Test every mapping list: default empty, append, chaining, None no-op"""
        create_only_fields = {"ecuResourceMappings", "swImplMappings", "swMappings"}
        for field, factory in MEMBER_FACTORIES.items():
            mapping = self._create()
            attr = field[:-1]
            getter = getattr(mapping, "get" + field[0].upper() + field[1:])

            member = factory(AUTOSAR.getInstance())
            assert getter() == []
            if field in create_only_fields:
                continue
            adder = getattr(mapping, "add" + attr[0].upper() + attr[1:])
            assert mapping == adder(member)
            assert getter() == [member]
            assert isinstance(getter(), list)

            assert mapping == adder(None)
            assert getter() == [member]

    def test_create_factories(self):
        """Test aggregate factories: appending to the dedicated list, duplicate returns existing"""
        for method_name, field in CREATE_FACTORIES:
            mapping = self._create()
            create = getattr(mapping, method_name)

            member = create("FactoryMember")
            assert member is not None
            assert getattr(mapping, "get" + field[0].upper() + field[1:])() == [member]
            assert create("FactoryMember") is member

    def test_mapping_constraint_typed_list(self):
        """Test that mappingConstraints holds MappingConstraint subtypes (Rule 0004 dedicated list)"""
        mapping = self._create()
        clustering = ComponentClustering()
        mapping.addMappingConstraint(clustering)
        assert mapping.getMappingConstraints() == [clustering]
        assert isinstance(clustering, MappingConstraint)

    def test_getter_type_annotations(self):
        """Test that every getter is annotated List[T] with the spec member type (Rule 0001.3)"""
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServiceMapping
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SignalPathConstraint

        expected = {
            "getApplicationPartitionToEcuPartitionMappings": typing.List[ApplicationPartitionToEcuPartitionMapping],
            "getAppOsTaskProxyToEcuTaskProxyMappings": typing.List[AppOsTaskProxyToEcuTaskProxyMapping],
            "getComManagementMappings": typing.List[ComManagementMapping],
            "getCryptoServiceMappings": typing.List[CryptoServiceMapping],
            "getDataMappings": typing.List[DataMapping],
            "getDdsISignalToTopicMappings": typing.List[DdsCpISignalToDdsTopicMapping],
            "getEcuResourceMappings": typing.List[ECUMapping],
            "getJ1939ControllerApplicationToJ1939NmNodeMappings": typing.List[J1939ControllerApplicationToJ1939NmNodeMapping],
            "getMappingConstraints": typing.List[MappingConstraint],
            "getPncMappings": typing.List[PncMapping],
            "getPortElementToComResourceMappings": typing.List[PortElementToCommunicationResourceMapping],
            "getResourceEstimations": typing.List[EcuResourceEstimation],
            "getResourceToApplicationPartitionMappings": typing.List[CpSoftwareClusterResourceToApplicationPartitionMapping],
            "getRteEventSeparations": typing.List[RteEventInSystemSeparation],
            "getRteEventToOsTaskProxyMappings": typing.List[RteEventInSystemToOsTaskProxyMapping],
            "getSignalPathConstraints": typing.List[SignalPathConstraint],
            "getSoftwareClusterToApplicationPartitionMappings": typing.List[CpSoftwareClusterToApplicationPartitionMapping],
            "getSoftwareClusterToResourceMappings": typing.List[CpSoftwareClusterToResourceMapping],
            "getSwClusterMappings": typing.List[CpSoftwareClusterToEcuInstanceMapping],
            "getSwcToApplicationPartitionMappings": typing.List[SwcToApplicationPartitionMapping],
            "getSwImplMappings": typing.List[SwcToImplMapping],
            "getSwMappings": typing.List[SwcToEcuMapping],
            "getSystemSignalGroupToComResourceMappings": typing.List[SystemSignalGroupToCommunicationResourceMapping],
            "getSystemSignalToComResourceMappings": typing.List[SystemSignalToCommunicationResourceMapping],
        }
        for getter_name, expected_hint in expected.items():
            hints = typing.get_type_hints(getattr(SystemMapping, getter_name))
            assert hints.get("return") is not None, "untyped getter: %s" % getter_name
