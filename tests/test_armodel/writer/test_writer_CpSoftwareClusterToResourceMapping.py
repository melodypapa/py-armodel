"""Writer/reader round-trip tests for CpSoftwareClusterToResourceMapping (Table 11.16, p.907)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterToResourceMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterMappingSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_mapping(short_name: str = "mapping1") -> CpSoftwareClusterToResourceMapping:
    mapping = CpSoftwareClusterToResourceMapping(None, short_name)

    mapping.setProviderRef(_ref("/Clusters/ProvidingCluster", "CP-SOFTWARE-CLUSTER"))
    mapping.addRequesterRef(_ref("/Clusters/RequestingClusterA", "CP-SOFTWARE-CLUSTER"))
    mapping.addRequesterRef(_ref("/Clusters/RequestingClusterB", "CP-SOFTWARE-CLUSTER"))
    mapping.setServiceResourceRef(_ref("/Resources/MyServiceResource", "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"))

    return mapping


def _assert_all_fields(mapping: CpSoftwareClusterToResourceMapping):
    assert mapping.getProviderRef().getValue() == "/Clusters/ProvidingCluster"
    assert mapping.getProviderRef().getDest() == "CP-SOFTWARE-CLUSTER"

    assert [ref.getValue() for ref in mapping.getRequesterRefs()] == ["/Clusters/RequestingClusterA", "/Clusters/RequestingClusterB"]
    assert all(ref.getDest() == "CP-SOFTWARE-CLUSTER" for ref in mapping.getRequesterRefs())

    assert mapping.getServiceResourceRef().getValue() == "/Resources/MyServiceResource"
    assert mapping.getServiceResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"


class TestWriteCpSoftwareClusterToResourceMapping:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: the SHORT-NAME first via the
        Identifiable base group, then the three Table 11.16 rows in the XSD group order
        (AUTOSAR_00052.xsd l.24782), with the unbounded REQUESTER-REF choice inside a
        REQUESTER-REFS wrapper emitted only when non-empty.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING")
        writer.writeCpSoftwareClusterToResourceMapping(element, _new_mapping())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[1:] == [
            "PROVIDER-REF",
            "REQUESTER-REFS",
            "SERVICE-RESOURCE-REF",
        ]
        assert element.find("PROVIDER-REF").text == "/Clusters/ProvidingCluster"
        assert element.find("PROVIDER-REF").attrib["DEST"] == "CP-SOFTWARE-CLUSTER"
        assert [ref.text for ref in element.findall("REQUESTER-REFS/REQUESTER-REF")] == ["/Clusters/RequestingClusterA", "/Clusters/RequestingClusterB"]
        assert all(ref.attrib["DEST"] == "CP-SOFTWARE-CLUSTER" for ref in element.findall("REQUESTER-REFS/REQUESTER-REF"))
        assert element.find("SERVICE-RESOURCE-REF").text == "/Resources/MyServiceResource"
        assert element.find("SERVICE-RESOURCE-REF").attrib["DEST"] == "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"

    def test_write_empty_element(self, writer):
        """
        A mapping without members emits no reference elements and no REQUESTER-REFS wrapper.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING")
        writer.writeCpSoftwareClusterToResourceMapping(element, CpSoftwareClusterToResourceMapping(None, "mapping2"))

        tags = [child.tag for child in element]
        assert tags == ["SHORT-NAME"]


class TestCpSoftwareClusterToResourceMappingRoundTrip:
    def test_round_trip_via_cp_software_cluster_mapping_set(self, writer, parser):
        """
        Write -> serialize -> re-parse through the CpSoftwareClusterMappingSet parent
        dispatch keeps every field value.
        """
        mapping_set = CpSoftwareClusterMappingSet(None, "mapping_set")
        mapping_set.createSoftwareClusterToResourceMapping("scr_mapping")
        mapping = mapping_set.getSoftwareClusterToResourceMappings()[0]
        populated = _new_mapping("scr_mapping")
        mapping.setProviderRef(populated.getProviderRef())
        mapping.addRequesterRef(populated.getRequesterRefs()[0])
        mapping.addRequesterRef(populated.getRequesterRefs()[1])
        mapping.setServiceResourceRef(populated.getServiceResourceRef())

        parent = ET.Element("PARENT")
        writer.writeCpSoftwareClusterMappingSet(parent, mapping_set)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = CpSoftwareClusterMappingSet(None, "mapping_set")
        parser.readCpSoftwareClusterMappingSet(root[0], reloaded)

        scr_mappings = reloaded.getSoftwareClusterToResourceMappings()
        assert len(scr_mappings) == 1
        assert scr_mappings[0].getShortName() == "scr_mapping"
        _assert_all_fields(scr_mappings[0])

    def test_round_trip_via_system_mapping(self, writer, parser):
        """
        Write -> serialize -> re-parse through the SystemMapping parent dispatch keeps
        every field value.
        """
        mapping = SystemMapping(AUTOSAR.getInstance(), "mapping")
        mapping.createSoftwareClusterToResourceMapping("scr_mapping")
        stored = mapping.getSoftwareClusterToResourceMappings()[0]
        populated = _new_mapping("scr_mapping")
        stored.setProviderRef(populated.getProviderRef())
        stored.addRequesterRef(populated.getRequesterRefs()[0])
        stored.addRequesterRef(populated.getRequesterRefs()[1])
        stored.setServiceResourceRef(populated.getServiceResourceRef())

        parent = ET.Element("PARENT")
        writer.writeSystemMapping(parent, mapping)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = SystemMapping(AUTOSAR.getInstance(), "mapping")
        parser.readSystemMapping(root[0], reloaded)

        scr_mappings = reloaded.getSoftwareClusterToResourceMappings()
        assert len(scr_mappings) == 1
        assert scr_mappings[0].getShortName() == "scr_mapping"
        _assert_all_fields(scr_mappings[0])

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: a mapping set without software cluster to resource
        mappings emits no SOFTWARE-CLUSTER-TO-RESOURCE-MAPPINGS wrapper, and a mapping
        without members re-parses to unset fields.
        """
        mapping_set = CpSoftwareClusterMappingSet(None, "mapping_set")
        parent = ET.Element("PARENT")
        writer.writeCpSoftwareClusterMappingSet(parent, mapping_set)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = CpSoftwareClusterMappingSet(None, "mapping_set")
        parser.readCpSoftwareClusterMappingSet(root[0], reloaded)
        assert reloaded.getSoftwareClusterToResourceMappings() == []

        element = ET.Element("CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING")
        writer.writeCpSoftwareClusterToResourceMapping(element, CpSoftwareClusterToResourceMapping(None, "mapping2"))
        xml = ET.tostring(element).decode("utf-8").replace("<CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING>", "<CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING xmlns='%s'>" % NS, 1)
        parsed_element = ET.fromstring(xml)
        mapping = parser.readCpSoftwareClusterToResourceMapping(parsed_element, CpSoftwareClusterToResourceMapping(None, "mapping2"))
        assert mapping.getProviderRef() is None
        assert mapping.getRequesterRefs() == []
        assert mapping.getServiceResourceRef() is None
