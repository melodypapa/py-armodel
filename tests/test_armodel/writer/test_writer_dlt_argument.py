"""Tests for the writeDltArgument handler (R23-11 DltArgument, Table E.20, p.13)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltArgument
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "DLT-ARGUMENT-ENTRYS",
    "LENGTH",
    "NETWORK-REPRESENTATION",
    "OPTIONAL",
    "PREDEFINED-TEXT",
    "VARIABLE-LENGTH",
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


def _boolean(value: str) -> Boolean:
    flag = Boolean()
    flag.setValue(value)
    return flag


def _positive_integer(value: str) -> PositiveInteger:
    number = PositiveInteger()
    number.setValue(value)
    return number


def _base_type_ref() -> RefType:
    ref = RefType()
    ref.setDest("SW-BASE-TYPE")
    ref.setValue("/DataTypes/BaseTypes/uint8")
    return ref


def _network_representation() -> SwDataDefProps:
    props = SwDataDefProps()
    props.setBaseTypeRef(_base_type_ref())
    return props


def _fill(argument: DltArgument) -> DltArgument:
    entry = argument.createDltArgumentEntry("struct_member")
    entry.setOptional(_boolean("true"))
    argument.setLength(_positive_integer("8"))
    argument.setNetworkRepresentation(_network_representation())
    argument.setOptional(_boolean("true"))
    argument.setPredefinedText(_boolean("false"))
    argument.setVariableLength(_boolean("true"))
    return argument


class TestWriteDltArgument:
    """Tests for writeDltArgument handler (R23-11 DltArgument, Table E.20, p.13)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writeDltArgument(parent, _fill(DltArgument(None, "top_arg")))
        child = parent.find("DLT-ARGUMENT")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("SHORT-NAME").text == "top_arg"
        entries_element = child.find("DLT-ARGUMENT-ENTRYS")
        entries = entries_element.findall("DLT-ARGUMENT")
        assert len(entries) == 1
        assert entries[0].find("SHORT-NAME").text == "struct_member"
        assert entries[0].find("OPTIONAL").text == "true"
        assert child.find("LENGTH").text == "8"
        base_type_ref = child.find("NETWORK-REPRESENTATION/SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL/BASE-TYPE-REF")
        assert base_type_ref.text == "/DataTypes/BaseTypes/uint8"
        assert base_type_ref.get("DEST") == "SW-BASE-TYPE"
        assert child.find("OPTIONAL").text == "true"
        assert child.find("PREDEFINED-TEXT").text == "false"
        assert child.find("VARIABLE-LENGTH").text == "true"

    def test_empty_wrapper_list_omitted(self, writer):
        parent = _parent()
        writer.writeDltArgument(parent, DltArgument(None, "empty_arg"))
        child = parent.find("DLT-ARGUMENT")
        assert child is not None
        assert child.find("DLT-ARGUMENT-ENTRYS") is None
        assert child.find("LENGTH") is None
        assert child.find("NETWORK-REPRESENTATION") is None
        assert child.find("OPTIONAL") is None
        assert child.find("PREDEFINED-TEXT") is None
        assert child.find("VARIABLE-LENGTH") is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writeDltArgument(parent, _fill(DltArgument(None, "top_arg")))
        child = parent.find("DLT-ARGUMENT")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = DltArgument(None, "top_arg")
        parser.readDltArgument(reloaded.find(f"{{{NS}}}DLT-ARGUMENT"), parsed)
        assert parsed.getShortName() == "top_arg"
        entries = parsed.getDltArgumentEntries()
        assert len(entries) == 1
        assert entries[0].getShortName() == "struct_member"
        assert entries[0].getOptional().getValue() is True
        assert parsed.getLength().getValue() == 8
        assert parsed.getNetworkRepresentation().getBaseTypeRef().getValue() == "/DataTypes/BaseTypes/uint8"
        assert parsed.getNetworkRepresentation().getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert parsed.getOptional().getValue() is True
        assert parsed.getPredefinedText().getValue() is False
        assert parsed.getVariableLength().getValue() is True
