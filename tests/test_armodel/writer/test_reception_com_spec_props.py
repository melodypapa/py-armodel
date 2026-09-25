"""
Tests for writing RECEPTION-PROPS elements — ReceptionComSpecProps, Table 4.64 (p.174, R23-11).

ReceptionComSpecProps (Base = ARObject) carries the optional reception attributes
DATA-UPDATE-PERIOD and TIMEOUT (both TIME-VALUE, 0..1). Writer element order must
follow the XSD sequenceOffset (AUTOSAR_00052.xsd group RECEPTION-COM-SPEC-PROPS:
DATA-UPDATE-PERIOD → TIMEOUT). The wrapper is emitted only when receptionProps is
set; the comspec-level round-trip goes through NonqueuedReceiverComSpec.

Round-trip counterpart: tests/test_armodel/parser/test_reception_com_spec_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, ReceptionComSpecProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _time_value(val):
    t = TimeValue()
    t.setValue(val)
    return t


class TestWriteReceptionComSpecProps:
    """Tests for writeReceptionComSpecProps — own element field values (Table 4.64)."""

    def test_write_field_values(self, writer):
        """Test that DATA-UPDATE-PERIOD and TIMEOUT are emitted with the field values."""
        props = ReceptionComSpecProps()
        props.setDataUpdatePeriod(_time_value(0.02))
        props.setTimeout(_time_value(2.5))
        parent = ET.Element("PARENT")

        writer.writeReceptionComSpecProps(parent, "RECEPTION-PROPS", props)

        child = parent.find("RECEPTION-PROPS")
        assert child is not None
        assert child.find("DATA-UPDATE-PERIOD").text == "0.02"
        assert child.find("TIMEOUT").text == "2.5"

    def test_write_element_order_matches_xsd(self, writer):
        """Test that the emitted own elements follow the XSD group order."""
        props = ReceptionComSpecProps()
        props.setDataUpdatePeriod(_time_value(0.02))
        props.setTimeout(_time_value(2.5))
        parent = ET.Element("PARENT")

        writer.writeReceptionComSpecProps(parent, "RECEPTION-PROPS", props)

        child = parent.find("RECEPTION-PROPS")
        tags = [c.tag for c in child]
        assert tags == ["DATA-UPDATE-PERIOD", "TIMEOUT"]

    def test_write_none_props_emits_nothing(self, writer):
        """Test that a None receptionProps emits no RECEPTION-PROPS element."""
        parent = ET.Element("PARENT")

        writer.writeReceptionComSpecProps(parent, "RECEPTION-PROPS", None)

        assert len(parent) == 0

    def test_write_unset_fields_emits_empty_wrapper(self, writer):
        """Test that set-but-empty receptionProps emits the wrapper without child elements."""
        props = ReceptionComSpecProps()
        parent = ET.Element("PARENT")

        writer.writeReceptionComSpecProps(parent, "RECEPTION-PROPS", props)

        child = parent.find("RECEPTION-PROPS")
        assert child is not None
        assert len(child) == 0


class TestReceptionPropsRoundTrip:
    """Round-trip through the NonqueuedReceiverComSpec aggregation (set → save → reload → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that receptionProps field values survive a comspec-level write/read cycle."""
        com_spec = NonqueuedReceiverComSpec()
        props = ReceptionComSpecProps()
        props.setDataUpdatePeriod(_time_value(0.02))
        props.setTimeout(_time_value(2.5))
        com_spec.setReceptionProps(props)

        parent = ET.Element("PARENT")
        writer.writeNonqueuedReceiverComSpec(parent, com_spec)
        com_spec_element = parent.find("NONQUEUED-RECEIVER-COM-SPEC")

        xml_text = ET.tostring(com_spec_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NONQUEUED-RECEIVER-COM-SPEC", "NONQUEUED-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getNonqueuedReceiverComSpec(reloaded_element)
        assert reloaded is not None
        reloaded_props = reloaded.getReceptionProps()
        assert reloaded_props is not None
        assert reloaded_props.getDataUpdatePeriod() is not None
        assert reloaded_props.getDataUpdatePeriod().getValue() == 0.02
        assert reloaded_props.getTimeout() is not None
        assert reloaded_props.getTimeout().getValue() == 2.5

    def test_round_trip_absent_props(self, writer):
        """Test that an unset receptionProps emits no RECEPTION-PROPS and reloads as None."""
        com_spec = NonqueuedReceiverComSpec()

        parent = ET.Element("PARENT")
        writer.writeNonqueuedReceiverComSpec(parent, com_spec)
        com_spec_element = parent.find("NONQUEUED-RECEIVER-COM-SPEC")
        assert com_spec_element.find("RECEPTION-PROPS") is None

        xml_text = ET.tostring(com_spec_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NONQUEUED-RECEIVER-COM-SPEC", "NONQUEUED-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getNonqueuedReceiverComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getReceptionProps() is None
