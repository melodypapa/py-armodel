"""Writer/reader round-trip tests for CpSoftwareClusterServiceResource (Table 11.14, p.904)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterServiceResource
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    String,
)
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


def _new_service_resource():
    resource = CpSoftwareClusterServiceResource(None, "service1")
    resource.setUuid(String().setValue("1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"))
    resource.addResourceNeedsRef(RefType().setValue("/Config/Container1").setDest("ECUC-CONTAINER-VALUE"))
    resource.addResourceNeedsRef(RefType().setValue("/Config/Container2").setDest("ECUC-CONTAINER-VALUE"))
    resource.setGlobalResourceId(PositiveInteger().setValue(7))
    resource.setIsMandatory(Boolean().setValue(True))
    return resource


class TestWriteCpSoftwareClusterServiceResource:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: the SHORT-NAME first via the
        CpSoftwareClusterResource base group, then the 0..1 RESOURCE-NEEDS-REFS wrapper
        (Table 11.14 resourceNeeds) emitted only when non-empty.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE")
        writer.writeCpSoftwareClusterServiceResource(element, _new_service_resource())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-1] == "RESOURCE-NEEDS-REFS"
        assert element.attrib["UUID"] == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        refs = element.find("RESOURCE-NEEDS-REFS")
        assert [child.tag for child in refs] == ["RESOURCE-NEEDS-REF", "RESOURCE-NEEDS-REF"]
        assert refs[0].text == "/Config/Container1"
        assert refs[0].attrib["DEST"] == "ECUC-CONTAINER-VALUE"
        assert refs[1].text == "/Config/Container2"

        assert element.find("GLOBAL-RESOURCE-ID").text == "7"
        assert element.find("IS-MANDATORY").text == "true"

    def test_write_empty_element(self, writer):
        """
        A resource without members emits no reference wrapper.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE")
        writer.writeCpSoftwareClusterServiceResource(element, CpSoftwareClusterServiceResource(None, "service2"))

        assert element.find("RESOURCE-NEEDS-REFS") is None


class TestCpSoftwareClusterServiceResourceRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the base
        CpSoftwareClusterResource level populated through the base helper.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE")
        writer.writeCpSoftwareClusterServiceResource(element, _new_service_resource())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        resource = parser.readCpSoftwareClusterServiceResource(parsed_element, CpSoftwareClusterServiceResource(None, "service1"))

        assert resource.getShortName() == "service1"
        assert resource.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        refs = resource.getResourceNeedsRefs()
        assert [ref.getValue() for ref in refs] == ["/Config/Container1", "/Config/Container2"]
        assert refs[0].getDest() == "ECUC-CONTAINER-VALUE"

        assert resource.getGlobalResourceId().getValue() == 7
        assert resource.getIsMandatory().getValue() is True

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: unset optional group elements serialize to nothing and
        re-parse to empty/None fields.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE")
        writer.writeCpSoftwareClusterServiceResource(element, CpSoftwareClusterServiceResource(None, "service2"))
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        resource = parser.readCpSoftwareClusterServiceResource(parsed_element, CpSoftwareClusterServiceResource(None, "service2"))

        assert resource.getResourceNeedsRefs() == []
        assert resource.getGlobalResourceId() is None
        assert resource.getIsMandatory() is None
