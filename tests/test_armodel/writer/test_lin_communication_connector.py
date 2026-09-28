"""Writer round-trip tests for LinCommunicationConnector (Table 3.43, p.98).

XML element order per XSD group LIN-COMMUNICATION-CONNECTOR: INITIAL-NAD,
LIN-CONFIGURABLE-FRAMES/LIN-CONFIGURABLE-FRAME,
LIN-ORDERED-CONFIGURABLE-FRAMES/LIN-ORDERED-CONFIGURABLE-FRAME,
SCHEDULE-CHANGE-NEXT-TIME-BASE.
Coverage runs through the CONNECTORS dispatch on writeEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinConfigurableFrame, LinOrderedConfigurableFrame
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["INITIAL-NAD", "LIN-CONFIGURABLE-FRAMES", "LIN-ORDERED-CONFIGURABLE-FRAMES", "SCHEDULE-CHANGE-NEXT-TIME-BASE"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _int(text):
    value = Integer()
    value.setValue(text)
    return value


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _boolean(value):
    value_obj = Boolean()
    value_obj.setValue(value)
    return value_obj


def _new_instance_with_connector():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    connector = instance.createLinCommunicationConnector("conn")
    connector.setInitialNad(_int("5"))

    frame1 = LinConfigurableFrame()
    frame1.setFrameRef(RefType().setValue("/lin/frame1"))
    frame1.setMessageId(_pos_int("33"))
    frame2 = LinConfigurableFrame()
    frame2.setFrameRef(RefType().setValue("/lin/frame2"))
    frame2.setMessageId(_pos_int("34"))
    connector.addLinConfigurableFrame(frame1)
    connector.addLinConfigurableFrame(frame2)

    ordered = LinOrderedConfigurableFrame()
    ordered.setFrameRef(RefType().setValue("/lin/frame1"))
    ordered.setIndex(_int("3"))
    connector.addLinOrderedConfigurableFrame(ordered)

    connector.setScheduleChangeNextTimeBase(_boolean(True))
    return instance


def _write_instance(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceConnectors(parent, instance)
    return parent


class TestWriteLinCommunicationConnector:
    def test_write_all_fields_in_xsd_order(self):
        parent = _write_instance(_new_instance_with_connector())
        connector_tag = parent.find("CONNECTORS/LIN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        tags = [child.tag for child in connector_tag]
        assert tags == ["SHORT-NAME"] + XSD_ORDER

    def test_write_field_values(self):
        parent = _write_instance(_new_instance_with_connector())
        connector_tag = parent.find("CONNECTORS/LIN-COMMUNICATION-CONNECTOR")
        assert connector_tag.find("INITIAL-NAD").text == "5"
        assert connector_tag.find("SCHEDULE-CHANGE-NEXT-TIME-BASE").text == "true"

        frames_tag = connector_tag.find("LIN-CONFIGURABLE-FRAMES")
        assert frames_tag is not None
        frames = frames_tag.findall("LIN-CONFIGURABLE-FRAME")
        assert len(frames) == 2
        assert frames[0].find("FRAME-REF").text == "/lin/frame1"
        assert frames[0].find("MESSAGE-ID").text == "33"
        assert frames[1].find("FRAME-REF").text == "/lin/frame2"
        assert frames[1].find("MESSAGE-ID").text == "34"

        ordered_tag = connector_tag.find("LIN-ORDERED-CONFIGURABLE-FRAMES")
        assert ordered_tag is not None
        ordered = ordered_tag.findall("LIN-ORDERED-CONFIGURABLE-FRAME")
        assert len(ordered) == 1
        assert ordered[0].find("FRAME-REF").text == "/lin/frame1"
        assert ordered[0].find("INDEX").text == "3"

    def test_write_connector_without_lin_fields_omits_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        instance = EcuInstance(pkg, "Ecu")
        instance.createLinCommunicationConnector("conn")
        parent = _write_instance(instance)
        connector_tag = parent.find("CONNECTORS/LIN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        tags = [child.tag for child in connector_tag]
        for lin_tag in XSD_ORDER:
            assert lin_tag not in tags

    def test_round_trip_preserves_all_values(self):
        instance = _new_instance_with_connector()
        parent = _write_instance(instance)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parsed_instance = EcuInstance(parsed_pkg, "Ecu")
        ARXMLParser().readEcuInstanceConnectors(root[0], parsed_instance)

        connector = parsed_instance.getConnectors()[0]
        assert connector.getShortName() == "conn"
        assert isinstance(connector.getInitialNad(), Integer)
        assert connector.getInitialNad().getValue() == 5

        frames = connector.getLinConfigurableFrames()
        assert len(frames) == 2
        assert all(isinstance(frame, LinConfigurableFrame) for frame in frames)
        assert frames[0].getFrameRef().getValue() == "/lin/frame1"
        assert frames[0].getMessageId().getValue() == 33
        assert frames[1].getFrameRef().getValue() == "/lin/frame2"
        assert frames[1].getMessageId().getValue() == 34

        ordered = connector.getLinOrderedConfigurableFrames()
        assert len(ordered) == 1
        assert isinstance(ordered[0], LinOrderedConfigurableFrame)
        assert ordered[0].getFrameRef().getValue() == "/lin/frame1"
        assert ordered[0].getIndex().getValue() == 3

        assert isinstance(connector.getScheduleChangeNextTimeBase(), Boolean)
        assert connector.getScheduleChangeNextTimeBase().getValue() is True
