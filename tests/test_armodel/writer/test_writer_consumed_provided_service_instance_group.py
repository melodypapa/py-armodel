"""Tests for the writeConsumedProvidedServiceInstanceGroup handler (R23-11 ConsumedProvidedServiceInstanceGroup, Table 6.174, p.523)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedProvidedServiceInstanceGroup
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "CONSUMED-SERVICE-INSTANCES",
    "PROVIDED-SERVICE-INSTANCES",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _fill_group(group):
    group.addConsumedServiceInstanceRef(_ref("/ServiceInstances/ConsumedServiceInstance1", "CONSUMED-SERVICE-INSTANCE"))
    group.addConsumedServiceInstanceRef(_ref("/ServiceInstances/ConsumedServiceInstance2", "CONSUMED-SERVICE-INSTANCE"))
    group.addProvidedServiceInstanceRef(_ref("/ServiceInstances/ProvidedServiceInstance1", "PROVIDED-SERVICE-INSTANCE"))
    return group


class TestWriteConsumedProvidedServiceInstanceGroup:
    """Tests for writeConsumedProvidedServiceInstanceGroup handler (R23-11, Table 6.174, p.523)."""

    def test_children_in_xsd_order(self, writer):
        group = _fill_group(ConsumedProvidedServiceInstanceGroup(AUTOSAR.getInstance(), "Group1"))

        parent = _parent()
        writer.writeConsumedProvidedServiceInstanceGroup(parent, group)
        child = parent.find("CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag in XSD_CHILD_ORDER]
        assert child_tags == XSD_CHILD_ORDER

        consumed_wrapper = child.find("CONSUMED-SERVICE-INSTANCES")
        conditional_tags = consumed_wrapper.findall("CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL")
        assert len(conditional_tags) == 2
        consumed_refs = consumed_wrapper.findall("CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL/CONSUMED-SERVICE-INSTANCE-REF")
        assert len(consumed_refs) == 2
        assert consumed_refs[0].text == "/ServiceInstances/ConsumedServiceInstance1"
        assert consumed_refs[0].get("DEST") == "CONSUMED-SERVICE-INSTANCE"
        assert consumed_refs[1].text == "/ServiceInstances/ConsumedServiceInstance2"

        provided_wrapper = child.find("PROVIDED-SERVICE-INSTANCES")
        provided_refs = provided_wrapper.findall("PROVIDED-SERVICE-INSTANCE-REF-CONDITIONAL/PROVIDED-SERVICE-INSTANCE-REF")
        assert len(provided_refs) == 1
        assert provided_refs[0].text == "/ServiceInstances/ProvidedServiceInstance1"
        assert provided_refs[0].get("DEST") == "PROVIDED-SERVICE-INSTANCE"

    def test_empty_wrappers_omitted(self, writer):
        group = ConsumedProvidedServiceInstanceGroup(AUTOSAR.getInstance(), "Group1")

        parent = _parent()
        writer.writeConsumedProvidedServiceInstanceGroup(parent, group)
        child = parent.find("CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP")
        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None

    def test_dispatch_via_write_ar_package_element(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("ServiceInstances")
        group = _fill_group(pkg.createConsumedProvidedServiceInstanceGroup("Group1"))

        parent = ET.Element("ELEMENTS")
        writer.writeARPackageElement(parent, group)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP"
        assert child.find("SHORT-NAME").text == "Group1"
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER

    def test_round_trip_set_save_reload(self, writer, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("ServiceInstances")
        _fill_group(pkg.createConsumedProvidedServiceInstanceGroup("Group1"))

        filename = str(tmp_path / "group.arxml")
        writer.save(filename, AUTOSAR.getInstance())

        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parser = ARXMLParser()
        parser.load(filename, AUTOSAR.getInstance())

        pkg = AUTOSAR.getInstance().find("ServiceInstances")
        groups = [e for e in pkg.getElements() if isinstance(e, ConsumedProvidedServiceInstanceGroup)]
        assert len(groups) == 1
        reloaded = groups[0]
        assert reloaded.getShortName() == "Group1"
        consumed_values = [ref.getValue() for ref in reloaded.getConsumedServiceInstanceRefs()]
        assert consumed_values == ["/ServiceInstances/ConsumedServiceInstance1", "/ServiceInstances/ConsumedServiceInstance2"]
        provided_values = [ref.getValue() for ref in reloaded.getProvidedServiceInstanceRefs()]
        assert provided_values == ["/ServiceInstances/ProvidedServiceInstance1"]
