"""Tests for the writeDltEcu handler and the ARPackage DltEcu dispatch (R23-11 DltEcu, Table F.49, p.8)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltEcu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "APPLICATIONS",
    "ECU-ID",
]

NS = "http://autosar.org/schema/r4.0"


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


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _string(value: str) -> String:
    text = String()
    text.setValue(value)
    return text


def _fill(ecu: DltEcu) -> DltEcu:
    application = ecu.createApplication("app_one")
    application.setApplicationId(_string("APP1"))
    ecu.createApplication("app_two").setApplicationId(_string("APP2"))
    ecu.setEcuId(_string("ECU1"))
    return ecu


class TestWriteDltEcu:
    """Tests for writeDltEcu handler (R23-11 DltEcu, Table F.49, p.8)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writeDltEcu(parent, _fill(DltEcu(None, "ecu_one")))
        child = parent.find("DLT-ECU")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("SHORT-NAME").text == "ecu_one"
        applications_element = child.find("APPLICATIONS")
        applications = applications_element.findall("DLT-APPLICATION")
        assert len(applications) == 2
        assert applications[0].find("SHORT-NAME").text == "app_one"
        assert applications[0].find("APPLICATION-ID").text == "APP1"
        assert applications[1].find("SHORT-NAME").text == "app_two"
        assert applications[1].find("APPLICATION-ID").text == "APP2"
        assert child.find("ECU-ID").text == "ECU1"

    def test_empty_wrapper_list_omitted(self, writer):
        parent = _parent()
        writer.writeDltEcu(parent, DltEcu(None, "ecu_empty"))
        child = parent.find("DLT-ECU")
        assert child is not None
        assert child.find("APPLICATIONS") is None
        assert child.find("ECU-ID") is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writeDltEcu(parent, _fill(DltEcu(None, "ecu_one")))
        child = parent.find("DLT-ECU")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = DltEcu(None, "ecu_one")
        parser.readDltEcu(reloaded.find(f"{{{NS}}}DLT-ECU"), parsed)
        assert parsed.getShortName() == "ecu_one"
        applications = parsed.getApplications()
        assert len(applications) == 2
        assert applications[0].getShortName() == "app_one"
        assert applications[0].getApplicationId().getValue() == "APP1"
        assert applications[1].getShortName() == "app_two"
        assert applications[1].getApplicationId().getValue() == "APP2"
        assert parsed.getEcuId().getValue() == "ECU1"


class TestWriteARPackageDltEcuDispatch:
    """Test for the DltEcu branch of the writeARPackageElement dispatch."""

    def test_dispatch_emits_dlt_ecu_tag(self, writer):
        pkg_element = ET.Element("AR-PACKAGE")
        ecu = DltEcu(None, "DE1")
        ecu.setEcuId(_string("ECU8"))
        writer.writeARPackageElement(pkg_element, ecu)
        children = list(pkg_element)
        assert len(children) == 1
        assert children[0].tag == "DLT-ECU"
        assert children[0].find("SHORT-NAME").text == "DE1"
        assert children[0].find("ECU-ID").text == "ECU8"
