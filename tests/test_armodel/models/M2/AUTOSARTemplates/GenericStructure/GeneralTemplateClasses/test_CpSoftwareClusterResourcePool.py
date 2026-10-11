"""
This module contains tests for the CpSoftwareClusterResourcePool class in the
AUTOSAR GenericStructure.GeneralTemplateClasses.ARPackage module.

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.5, p.901
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
    CpSoftwareClusterResourcePool,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CpSoftwareClusterCommunicationResource,
    CpSoftwareClusterResource,
    CpSoftwareClusterServiceResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestCpSoftwareClusterResourcePool:
    """
    Test class for CpSoftwareClusterResourcePool functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.5, p.901
    """

    CLASS_NOTE = "Represents the pool of resources which can be provided or required by CP Software Clusters. Tags: atp.recommendedPackage=CpSoftwareClusterResourcePools"
    ECU_SCOPE_NOTE = "This reference identifies the EcuInstance in which the resource pool is defined. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuScope"
    RESOURCE_NOTE = "This aggregation represents the collection of resources in the enclosing resource pool. Stereotypes: atpSplitable Tags: atp.Splitkey=resource.shortName"

    def _create_pool(self) -> CpSoftwareClusterResourcePool:
        return CpSoftwareClusterResourcePool(None, "Pool1")

    def test_is_arelement_subclass(self):
        """
        Test that CpSoftwareClusterResourcePool derives from ARElement per the Table 11.5 Base row.
        """
        assert issubclass(CpSoftwareClusterResourcePool, ARElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(CpSoftwareClusterResourcePool.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSoftwareClusterResourcePool.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.5 displayed row order
        (adds/creates first on the multi rows, getter last).
        """
        methods = [name for name, value in CpSoftwareClusterResourcePool.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "addEcuScopeRef",
            "getEcuScopeRefs",
            "createCpSoftwareClusterCommunicationResource",
            "createCpSoftwareClusterServiceResource",
            "getResources",
        ]

    def test_initialization_defaults(self):
        """
        Test that the instance initializes all attributes to their defaults.
        """
        obj = self._create_pool()

        assert obj.getShortName() == "Pool1"
        assert obj.getEcuScopeRefs() == []
        assert obj.getResources() == []

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types.
        """
        hints = typing.get_type_hints(CpSoftwareClusterResourcePool.addEcuScopeRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is CpSoftwareClusterResourcePool
        hints = typing.get_type_hints(CpSoftwareClusterResourcePool.getEcuScopeRefs)
        assert hints.get("return") == typing.List[RefType]

        hints = typing.get_type_hints(CpSoftwareClusterResourcePool.createCpSoftwareClusterCommunicationResource)
        assert hints.get("short_name") is str
        assert hints.get("return") is CpSoftwareClusterCommunicationResource
        hints = typing.get_type_hints(CpSoftwareClusterResourcePool.createCpSoftwareClusterServiceResource)
        assert hints.get("short_name") is str
        assert hints.get("return") is CpSoftwareClusterServiceResource
        hints = typing.get_type_hints(CpSoftwareClusterResourcePool.getResources)
        assert hints.get("return") == typing.List[CpSoftwareClusterResource]

    def test_method_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim
        (adders carry the None no-op tail).
        """
        assert inspect.cleandoc(CpSoftwareClusterResourcePool.addEcuScopeRef.__doc__) == (self.ECU_SCOPE_NOTE + "\n\nA None value is a no-op and does not append to ecuScopeRefs.")
        assert inspect.cleandoc(CpSoftwareClusterResourcePool.getEcuScopeRefs.__doc__) == self.ECU_SCOPE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterResourcePool.createCpSoftwareClusterCommunicationResource.__doc__) == self.RESOURCE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterResourcePool.createCpSoftwareClusterServiceResource.__doc__) == self.RESOURCE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterResourcePool.getResources.__doc__) == self.RESOURCE_NOTE

    def test_add_ecu_scope_ref(self):
        """
        Test addEcuScopeRef appends, returns self and ignores None.
        """
        obj = self._create_pool()

        ref = RefType().setValue("/Ecu/Ecu1").setDest("ECU-INSTANCE")
        result = obj.addEcuScopeRef(ref)
        assert result is obj
        assert obj.getEcuScopeRefs() == [ref]
        assert obj.getEcuScopeRefs()[0].getValue() == "/Ecu/Ecu1"
        assert obj.getEcuScopeRefs()[0].getDest() == "ECU-INSTANCE"

        result = obj.addEcuScopeRef(None)
        assert result is obj
        assert obj.getEcuScopeRefs() == [ref]

        second = RefType().setValue("/Ecu/Ecu2").setDest("ECU-INSTANCE")
        obj.addEcuScopeRef(second)
        assert obj.getEcuScopeRefs() == [ref, second]

    def test_create_cp_software_cluster_communication_resource(self):
        """
        Test createCpSoftwareClusterCommunicationResource registers the child and duplicate-protects by type.
        """
        obj = self._create_pool()
        resource = obj.createCpSoftwareClusterCommunicationResource("CommResource1")
        assert isinstance(resource, CpSoftwareClusterCommunicationResource)
        assert isinstance(resource, CpSoftwareClusterResource)
        assert resource.getParent() is obj
        assert obj.getResources() == [resource]

        same = obj.createCpSoftwareClusterCommunicationResource("CommResource1")
        assert same is resource
        assert obj.getResources() == [resource]

    def test_create_cp_software_cluster_service_resource(self):
        """
        Test createCpSoftwareClusterServiceResource registers the child and duplicate-protects by type.
        """
        obj = self._create_pool()
        resource = obj.createCpSoftwareClusterServiceResource("ServiceResource1")
        assert isinstance(resource, CpSoftwareClusterServiceResource)
        assert isinstance(resource, CpSoftwareClusterResource)
        assert resource.getParent() is obj
        assert obj.getResources() == [resource]

        same = obj.createCpSoftwareClusterServiceResource("ServiceResource1")
        assert same is resource
        assert obj.getResources() == [resource]

    def test_create_resource_subtypes_append(self):
        """
        Test both resource factory subtypes append to the collection in order.
        """
        obj = self._create_pool()
        comm = obj.createCpSoftwareClusterCommunicationResource("CommResource1")
        service = obj.createCpSoftwareClusterServiceResource("ServiceResource1")
        assert isinstance(comm, CpSoftwareClusterCommunicationResource)
        assert isinstance(service, CpSoftwareClusterServiceResource)
        assert obj.getResources() == [comm, service]
