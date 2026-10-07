"""Writer round-trip tests for ServiceInstanceCollectionSet (R23-11 CP_TPS_SystemTemplate, Table 6.157, p.476).

Aggregated by ARPackage.element. The SERVICE-INSTANCES wrapper aggregates an unbounded XSD
choice of the four synced service-instance subtypes - the writer dispatches on isinstance,
the reader on the child tag (five-place polymorphic dispatch).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsCpProvidedServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpConsumedServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AnyVersionString, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ConsumedServiceInstance,
    ProvidedServiceInstance,
    ServiceInstanceCollectionSet,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_collection_set():
    collection_set = ServiceInstanceCollectionSet(None, "ServiceInstances")

    consumed = collection_set.createConsumedServiceInstance("Consumed_1")
    consumed.setMajorVersion(PositiveInteger().setValue("2"))
    consumed.setMinorVersion(AnyVersionString().setValue("1"))

    dds_consumed = collection_set.createDdsCpConsumedServiceInstance("DdsConsumed_1")
    dds_consumed.setMinorVersion(AnyVersionString().setValue("3"))

    dds_provided = DdsCpProvidedServiceInstance()
    dds_provided.setMinorVersion(PositiveInteger().setValue("4"))
    collection_set.addDdsCpProvidedServiceInstance(dds_provided)

    provided = collection_set.createProvidedServiceInstance("Provided_1")
    provided.setMajorVersion(PositiveInteger().setValue("5"))
    provided.setServiceIdentifier(PositiveInteger().setValue("7"))
    return collection_set


def _namespaced(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _assert_collection_set_field_values(collection_set):
    instances = collection_set.getServiceInstances()
    assert len(instances) == 4

    consumed = instances[0]
    assert isinstance(consumed, ConsumedServiceInstance)
    assert consumed.getShortName() == "Consumed_1"
    assert consumed.getMajorVersion().getValue() == 2
    assert consumed.getMinorVersion().getValue() == "1"

    dds_consumed = instances[1]
    assert isinstance(dds_consumed, DdsCpConsumedServiceInstance)
    assert dds_consumed.getShortName() == "DdsConsumed_1"
    assert dds_consumed.getMinorVersion().getValue() == "3"

    dds_provided = instances[2]
    assert isinstance(dds_provided, DdsCpProvidedServiceInstance)
    assert dds_provided.getMinorVersion().getValue() == 4

    provided = instances[3]
    assert isinstance(provided, ProvidedServiceInstance)
    assert provided.getShortName() == "Provided_1"
    assert provided.getMajorVersion().getValue() == 5
    assert provided.getServiceIdentifier().getValue() == 7


class TestWriteServiceInstanceCollectionSet:
    def test_write_all_attrs(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_collection_set())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/SERVICE-INSTANCE-COLLECTION-SET")
        assert node is not None
        assert node.find("SHORT-NAME").text == "ServiceInstances"
        wrapper = node.find("SERVICE-INSTANCES")
        assert wrapper is not None
        children = list(wrapper)
        assert [child.tag for child in children] == [
            "CONSUMED-SERVICE-INSTANCE",
            "DDS-CP-CONSUMED-SERVICE-INSTANCE",
            "DDS-CP-PROVIDED-SERVICE-INSTANCE",
            "PROVIDED-SERVICE-INSTANCE",
        ]
        assert children[0].find("SHORT-NAME").text == "Consumed_1"
        assert children[0].findtext("MAJOR-VERSION") == "2"
        assert children[0].findtext("MINOR-VERSION") == "1"
        assert children[1].find("SHORT-NAME").text == "DdsConsumed_1"
        assert children[1].findtext("MINOR-VERSION") == "3"
        assert children[2].findtext("MINOR-VERSION") == "4"
        assert children[3].find("SHORT-NAME").text == "Provided_1"
        assert children[3].findtext("MAJOR-VERSION") == "5"
        assert children[3].findtext("SERVICE-IDENTIFIER") == "7"

    def test_write_empty_omits_wrapper(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(ServiceInstanceCollectionSet(None, "EmptySet"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/SERVICE-INSTANCE-COLLECTION-SET")
        assert node is not None
        assert node.find("SERVICE-INSTANCES") is None

    def test_round_trip_preserves_child_field_values(self):
        writer = ARXMLWriter()
        parser = ARXMLParser()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_collection_set())
        parent = ET.Element("PARENT")
        writer.writeARPackageElements(parent, package)
        root = _namespaced(parent)

        reloaded_package = AUTOSAR.getInstance().createARPackage("Pkg2")
        parser.readARPackageElements(root, reloaded_package)

        collection_set = reloaded_package.getReferrableElement("ServiceInstances", ServiceInstanceCollectionSet)
        assert isinstance(collection_set, ServiceInstanceCollectionSet)
        _assert_collection_set_field_values(collection_set)
