"""
This module contains tests for the CpSoftwareClusterToResourceMapping class in the
AUTOSAR GenericStructure.GeneralTemplateClasses.Identifiable module.

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.16, p.907
"""

import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CpSoftwareClusterToResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestCpSoftwareClusterToResourceMapping:
    """
    Test class for CpSoftwareClusterToResourceMapping functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.16, p.907
    """

    CLASS_NOTE = "This meta class maps a service resource to CP Software Clusters. By this mapping it's specified whether the Software Cluster has to provide or to require the resource."
    PROVIDER_NOTE = "CP Software Cluster providing the resource"
    REQUESTER_NOTE = "CP Software Cluster requesting the resource"
    SERVICE_RESOURCE_NOTE = "Service resource for which the mapping applies."

    def _create_mapping(self) -> CpSoftwareClusterToResourceMapping:
        return CpSoftwareClusterToResourceMapping(None, "mapping1")

    def test_is_identifiable_subclass(self):
        """
        Test that CpSoftwareClusterToResourceMapping derives from Identifiable per the Table 11.16 Base row.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        assert issubclass(CpSoftwareClusterToResourceMapping, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(CpSoftwareClusterToResourceMapping.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSoftwareClusterToResourceMapping.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.16 displayed row order
        (getter then setter per scalar row, mutator then getter per the requester list row).
        """
        methods = [name for name, value in CpSoftwareClusterToResourceMapping.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getProviderRef",
            "setProviderRef",
            "addRequesterRef",
            "getRequesterRefs",
            "getServiceResourceRef",
            "setServiceResourceRef",
        ]

    def test_initialization_defaults(self):
        """
        Test that the instance initializes all attributes to their defaults.
        """
        obj = self._create_mapping()

        assert obj.getShortName() == "mapping1"
        assert obj.getProviderRef() is None
        assert obj.getRequesterRefs() == []
        assert obj.getServiceResourceRef() is None

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types. All three members are REF-kind
        members modeled as RefType (the concrete spec types CpSoftwareCluster /
        CpSoftwareClusterServiceResource travel in the DEST attribute), which resolves
        at runtime.
        """
        hints = typing.get_type_hints(CpSoftwareClusterToResourceMapping.getProviderRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterToResourceMapping.setProviderRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is CpSoftwareClusterToResourceMapping

        hints = typing.get_type_hints(CpSoftwareClusterToResourceMapping.addRequesterRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is CpSoftwareClusterToResourceMapping
        hints = typing.get_type_hints(CpSoftwareClusterToResourceMapping.getRequesterRefs)
        assert hints.get("return") == typing.List[RefType]

        hints = typing.get_type_hints(CpSoftwareClusterToResourceMapping.getServiceResourceRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterToResourceMapping.setServiceResourceRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is CpSoftwareClusterToResourceMapping

    def test_method_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim
        (the mutators carry the None no-op tail).
        """
        assert inspect.cleandoc(CpSoftwareClusterToResourceMapping.getProviderRef.__doc__) == self.PROVIDER_NOTE
        assert inspect.cleandoc(CpSoftwareClusterToResourceMapping.setProviderRef.__doc__) == (self.PROVIDER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing providerRef.")
        assert inspect.cleandoc(CpSoftwareClusterToResourceMapping.addRequesterRef.__doc__) == (self.REQUESTER_NOTE + "\n\nA None value is a no-op and does not add to requesterRefs.")
        assert inspect.cleandoc(CpSoftwareClusterToResourceMapping.getRequesterRefs.__doc__) == self.REQUESTER_NOTE
        assert inspect.cleandoc(CpSoftwareClusterToResourceMapping.getServiceResourceRef.__doc__) == self.SERVICE_RESOURCE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterToResourceMapping.setServiceResourceRef.__doc__) == (
            self.SERVICE_RESOURCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing serviceResourceRef."
        )

    def test_get_set_provider_ref(self):
        """
        Test setProviderRef stores the reference and ignores None.
        """
        obj = self._create_mapping()

        ref = RefType().setValue("/Clusters/ProvidingCluster").setDest("CP-SOFTWARE-CLUSTER")
        result = obj.setProviderRef(ref)
        assert result is obj
        assert obj.getProviderRef() is ref
        assert obj.getProviderRef().getValue() == "/Clusters/ProvidingCluster"
        assert obj.getProviderRef().getDest() == "CP-SOFTWARE-CLUSTER"

        obj.setProviderRef(None)
        assert obj.getProviderRef() is ref

    def test_add_get_requester_refs(self):
        """
        Test addRequesterRef appends the references and ignores None.
        """
        obj = self._create_mapping()

        ref1 = RefType().setValue("/Clusters/RequestingClusterA").setDest("CP-SOFTWARE-CLUSTER")
        ref2 = RefType().setValue("/Clusters/RequestingClusterB").setDest("CP-SOFTWARE-CLUSTER")
        result = obj.addRequesterRef(ref1)
        assert result is obj
        obj.addRequesterRef(ref2)
        assert obj.getRequesterRefs() == [ref1, ref2]

        obj.addRequesterRef(None)
        assert obj.getRequesterRefs() == [ref1, ref2]

    def test_get_set_service_resource_ref(self):
        """
        Test setServiceResourceRef stores the reference and ignores None.
        """
        obj = self._create_mapping()

        ref = RefType().setValue("/Resources/MyServiceResource").setDest("CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE")
        result = obj.setServiceResourceRef(ref)
        assert result is obj
        assert obj.getServiceResourceRef() is ref
        assert obj.getServiceResourceRef().getValue() == "/Resources/MyServiceResource"
        assert obj.getServiceResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"

        obj.setServiceResourceRef(None)
        assert obj.getServiceResourceRef() is ref

    def test_created_via_parent_factories(self):
        """
        Test that both aggregators (CpSoftwareClusterMappingSet, SystemMapping) create
        CpSoftwareClusterToResourceMapping instances (Table 11.16 Aggregated by rows).
        """
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("pkg")
        mapping_set = pkg.createCpSoftwareClusterMappingSet("mapping_set")

        mapping = mapping_set.createSoftwareClusterToResourceMapping("scr_mapping")
        assert isinstance(mapping, CpSoftwareClusterToResourceMapping)
        assert mapping.getShortName() == "scr_mapping"
        assert mapping_set.createSoftwareClusterToResourceMapping("scr_mapping") is mapping

        system = pkg.createSystem("system")
        system_mapping = system.createSystemMapping("system_mapping")
        system_mapping.addSoftwareClusterToResourceMapping(CpSoftwareClusterToResourceMapping(system_mapping, "scr_mapping2"))
        assert isinstance(system_mapping.getSoftwareClusterToResourceMappings()[0], CpSoftwareClusterToResourceMapping)
