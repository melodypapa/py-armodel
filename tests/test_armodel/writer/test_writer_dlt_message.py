"""Tests for the writeDltMessage handler (R23-11 DltMessage, Table F.50, p.12)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltMessage, PrivacyLevel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "DLT-ARGUMENTS",
    "MESSAGE-ID",
    "MESSAGE-LINE-NUMBER",
    "MESSAGE-SOURCE-FILE",
    "MESSAGE-TYPE-INFO",
    "PRIVACY-LEVEL",
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


def _positive_integer(value: str) -> PositiveInteger:
    number = PositiveInteger()
    number.setValue(value)
    return number


def _string(value: str) -> String:
    text = String()
    text.setValue(value)
    return text


def _privacy_level(value: str) -> PrivacyLevel:
    level = PrivacyLevel()
    level.setPrivacyLevel(_positive_integer(value))
    return level


def _fill(message: DltMessage) -> DltMessage:
    argument = message.createDltArgument("arg_one")
    argument.setLength(_positive_integer("8"))
    message.setMessageId(_positive_integer("42"))
    message.setMessageLineNumber(_positive_integer("17"))
    message.setMessageSourceFile(_string("logger.c"))
    message.setMessageTypeInfo(_string("DLT_LOG_INFO"))
    message.setPrivacyLevel(_privacy_level("2"))
    return message


class TestWriteDltMessage:
    """Tests for writeDltMessage handler (R23-11 DltMessage, Table F.50, p.12)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writeDltMessage(parent, _fill(DltMessage(None, "top_message")))
        child = parent.find("DLT-MESSAGE")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("SHORT-NAME").text == "top_message"
        arguments_element = child.find("DLT-ARGUMENTS")
        arguments = arguments_element.findall("DLT-ARGUMENT")
        assert len(arguments) == 1
        assert arguments[0].find("SHORT-NAME").text == "arg_one"
        assert arguments[0].find("LENGTH").text == "8"
        assert child.find("MESSAGE-ID").text == "42"
        assert child.find("MESSAGE-LINE-NUMBER").text == "17"
        assert child.find("MESSAGE-SOURCE-FILE").text == "logger.c"
        assert child.find("MESSAGE-TYPE-INFO").text == "DLT_LOG_INFO"
        assert child.find("PRIVACY-LEVEL/PRIVACY-LEVEL").text == "2"

    def test_empty_wrapper_list_omitted(self, writer):
        parent = _parent()
        writer.writeDltMessage(parent, DltMessage(None, "empty_message"))
        child = parent.find("DLT-MESSAGE")
        assert child is not None
        assert child.find("DLT-ARGUMENTS") is None
        assert child.find("MESSAGE-ID") is None
        assert child.find("MESSAGE-LINE-NUMBER") is None
        assert child.find("MESSAGE-SOURCE-FILE") is None
        assert child.find("MESSAGE-TYPE-INFO") is None
        assert child.find("PRIVACY-LEVEL") is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writeDltMessage(parent, _fill(DltMessage(None, "top_message")))
        child = parent.find("DLT-MESSAGE")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = DltMessage(None, "top_message")
        parser.readDltMessage(reloaded.find(f"{{{NS}}}DLT-MESSAGE"), parsed)
        assert parsed.getShortName() == "top_message"
        arguments = parsed.getDltArguments()
        assert len(arguments) == 1
        assert arguments[0].getShortName() == "arg_one"
        assert arguments[0].getLength().getValue() == 8
        assert parsed.getMessageId().getValue() == 42
        assert parsed.getMessageLineNumber().getValue() == 17
        assert parsed.getMessageSourceFile().getValue() == "logger.c"
        assert parsed.getMessageTypeInfo().getValue() == "DLT_LOG_INFO"
        assert parsed.getPrivacyLevel().getPrivacyLevel().getValue() == 2
