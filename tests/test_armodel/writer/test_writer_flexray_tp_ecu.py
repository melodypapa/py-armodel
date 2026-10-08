"""Tests for the writeFlexrayTpEcu handler (R23-11 FlexrayTpEcu, Table 6.244, p.597)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig, FlexrayTpEcu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "CANCELLATION",
    "CYCLE-TIME-MAIN-FUNCTION",
    "ECU-INSTANCE-REF",
    "FULL-DUPLEX-ENABLED",
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


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _boolean(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _fill_ecu(ecu: FlexrayTpEcu) -> FlexrayTpEcu:
    ecu.setCancellation(_boolean(True))
    ecu.setCycleTimeMainFunction(_time(0.005))
    ecu.setEcuInstanceRef(_ref("/Topology/Ecu1", "ECU-INSTANCE"))
    ecu.setFullDuplexEnabled(_boolean(True))
    return ecu


class TestWriteFlexrayTpEcu:
    """Tests for writeFlexrayTpEcu (R23-11 FlexrayTpEcu, Table 6.244, p.597)."""

    def test_children_in_xsd_order(self, writer):
        ecu = _fill_ecu(FlexrayTpEcu())
        parent = _parent()
        writer.writeFlexrayTpEcu(parent, ecu)
        child = parent.find("FLEXRAY-TP-ECU")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("CANCELLATION").text == "true"
        assert child.find("CYCLE-TIME-MAIN-FUNCTION").text == "0.005"
        assert child.find("ECU-INSTANCE-REF").text == "/Topology/Ecu1"
        assert child.find("FULL-DUPLEX-ENABLED").text == "true"

    def test_empty_ecu_writes_no_attributes(self, writer):
        ecu = FlexrayTpEcu()
        parent = _parent()
        writer.writeFlexrayTpEcu(parent, ecu)
        child = parent.find("FLEXRAY-TP-ECU")
        assert child is not None
        assert len(child) == 0

    def test_round_trip_via_config(self, writer, parser):
        config = FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        config.addTpEcu(_fill_ecu(FlexrayTpEcu()))

        parent = _parent()
        writer.writeFlexrayTpConfig(parent, config)
        xml_text = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        assert "FLEXRAY-TP-ECU" in xml_text

        reparsed = ET.fromstring(xml_text)[0]
        config2 = FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        parser.readFlexrayTpConfig(reparsed, config2)
        ecus = config2.getTpEcus()
        assert len(ecus) == 1
        loaded = ecus[0]
        assert loaded.getCancellation().getValue() is True
        assert loaded.getCycleTimeMainFunction().getValue() == 0.005
        assert loaded.getEcuInstanceRef().getValue() == "/Topology/Ecu1"
        assert loaded.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert loaded.getFullDuplexEnabled().getValue() is True
