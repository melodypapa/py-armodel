"""Spec-sync tests for ServiceInstanceCollectionSet (R23-11 CP_TPS_SystemTemplate, Table 6.157, p.476)."""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    DdsCpProvidedServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    DdsCpConsumedServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ConsumedServiceInstance,
    ProvidedServiceInstance,
    ServiceInstanceCollectionSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestServiceInstanceCollectionSet:
    MEMBERS = [
        "serviceInstances",
    ]

    SERVICE_INSTANCE_NOTE = "ServiceInstances that are part of the collection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serviceInstance.shortName, serviceInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild"

    def _set(self):
        return ServiceInstanceCollectionSet(MockParent(), "collection_set")

    def test_rehoused_to_spec_package(self):
        """Spec Package row = Fibex4Ethernet::ServiceInstances (Rule 0007) - rehoused from the FibexCore stub."""
        module = inspect.getmodule(ServiceInstanceCollectionSet).__name__

        assert module == "armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances"

    def test_inheritance(self):
        collection_set = self._set()

        assert isinstance(collection_set, FibexElement)

    def test_top_level_export(self):
        import armodel

        assert armodel.ServiceInstanceCollectionSet is ServiceInstanceCollectionSet

    def test_init_parameter_annotations(self):
        annotations = typing.get_type_hints(ServiceInstanceCollectionSet.__init__)

        assert annotations["parent"] is ARObject
        assert annotations["short_name"] is str

    def test_member_annotations_match_getter_returns(self):
        expected = typing.List[typing.Union[ConsumedServiceInstance, DdsCpConsumedServiceInstance, DdsCpProvidedServiceInstance, ProvidedServiceInstance]]
        assert typing.get_type_hints(ServiceInstanceCollectionSet.getServiceInstances)["return"] == expected

    def test_initialization_defaults(self):
        collection_set = self._set()

        assert collection_set.getServiceInstances() == []

    def test_member_order(self):
        collection_set = self._set()

        members = [k for k in vars(collection_set) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_consumed_service_instance(self):
        collection_set = self._set()

        instance = collection_set.createConsumedServiceInstance("consumed_1")
        assert isinstance(instance, ConsumedServiceInstance)
        assert instance.getShortName() == "consumed_1"
        assert collection_set.getServiceInstances() == [instance]

        again = collection_set.createConsumedServiceInstance("consumed_1")
        assert again is instance
        assert len(collection_set.getServiceInstances()) == 1

    def test_create_provided_service_instance(self):
        collection_set = self._set()

        instance = collection_set.createProvidedServiceInstance("provided_1")
        assert isinstance(instance, ProvidedServiceInstance)
        assert instance.getShortName() == "provided_1"
        assert collection_set.getServiceInstances() == [instance]

        again = collection_set.createProvidedServiceInstance("provided_1")
        assert again is instance
        assert len(collection_set.getServiceInstances()) == 1

    def test_create_dds_cp_consumed_service_instance(self):
        collection_set = self._set()

        instance = collection_set.createDdsCpConsumedServiceInstance("dds_consumed_1")
        assert isinstance(instance, DdsCpConsumedServiceInstance)
        assert instance.getShortName() == "dds_consumed_1"
        assert collection_set.getServiceInstances() == [instance]

        again = collection_set.createDdsCpConsumedServiceInstance("dds_consumed_1")
        assert again is instance
        assert len(collection_set.getServiceInstances()) == 1

    def test_add_dds_cp_provided_service_instance(self):
        collection_set = self._set()

        instance = DdsCpProvidedServiceInstance()
        collection_set.addDdsCpProvidedServiceInstance(instance)
        assert collection_set.getServiceInstances() == [instance]

        collection_set.addDdsCpProvidedServiceInstance(None)
        assert len(collection_set.getServiceInstances()) == 1

    def test_class_docstring_note(self):
        expected = "Collection of ServiceInstances Tags: atp.recommendedPackage=ServiceInstanceCollectionSets"
        assert inspect.cleandoc(ServiceInstanceCollectionSet.__doc__) == expected

    def test_notes_verbatim(self):
        for factory in (
            ServiceInstanceCollectionSet.createConsumedServiceInstance,
            ServiceInstanceCollectionSet.createDdsCpConsumedServiceInstance,
            ServiceInstanceCollectionSet.createProvidedServiceInstance,
            ServiceInstanceCollectionSet.getServiceInstances,
        ):
            assert inspect.cleandoc(factory.__doc__) == self.SERVICE_INSTANCE_NOTE
        assert inspect.cleandoc(ServiceInstanceCollectionSet.addDdsCpProvidedServiceInstance.__doc__).startswith(self.SERVICE_INSTANCE_NOTE)
        assert self.SERVICE_INSTANCE_NOTE in inspect.getsource(ServiceInstanceCollectionSet.__init__)
