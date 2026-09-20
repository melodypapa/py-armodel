"""Tests for the writeDltApplication handler (R23-11 DltApplication, Table F.47, p.9)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltApplication
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "APPLICATION-DESCRIPTION",
    "APPLICATION-ID",
    "CONTEXTS",
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


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest("DLT-CONTEXT")
    return ref


def _fill(application: DltApplication) -> DltApplication:
    application.setApplicationDescription(_string("Diagnostics application of the ECU"))
    application.setApplicationId(_string("APP1"))
    application.addContextRef(_ref("/LogAndTrace/DltContexts/Context1"))
    application.addContextRef(_ref("/LogAndTrace/DltContexts/Context2"))
    return application


class TestWriteDltApplication:
    """Tests for writeDltApplication handler (R23-11 DltApplication, Table F.47, p.9)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writeDltApplication(parent, _fill(DltApplication(None, "app_one")))
        child = parent.find("DLT-APPLICATION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("SHORT-NAME").text == "app_one"
        assert child.find("APPLICATION-DESCRIPTION").text == "Diagnostics application of the ECU"
        assert child.find("APPLICATION-ID").text == "APP1"
        contexts_element = child.find("CONTEXTS")
        conditionals = contexts_element.findall("DLT-CONTEXT-REF-CONDITIONAL")
        assert len(conditionals) == 2
        assert conditionals[0].find("DLT-CONTEXT-REF").text == "/LogAndTrace/DltContexts/Context1"
        assert conditionals[0].find("DLT-CONTEXT-REF").get("DEST") == "DLT-CONTEXT"
        assert conditionals[1].find("DLT-CONTEXT-REF").text == "/LogAndTrace/DltContexts/Context2"

    def test_empty_wrapper_list_omitted(self, writer):
        parent = _parent()
        writer.writeDltApplication(parent, DltApplication(None, "app_empty"))
        child = parent.find("DLT-APPLICATION")
        assert child is not None
        assert child.find("APPLICATION-DESCRIPTION") is None
        assert child.find("APPLICATION-ID") is None
        assert child.find("CONTEXTS") is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writeDltApplication(parent, _fill(DltApplication(None, "app_one")))
        child = parent.find("DLT-APPLICATION")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = DltApplication(None, "app_one")
        parser.readDltApplication(reloaded.find(f"{{{NS}}}DLT-APPLICATION"), parsed)
        assert parsed.getShortName() == "app_one"
        assert parsed.getApplicationDescription().getValue() == "Diagnostics application of the ECU"
        assert parsed.getApplicationId().getValue() == "APP1"
        refs = parsed.getContextRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/LogAndTrace/DltContexts/Context1"
        assert refs[0].getDest() == "DLT-CONTEXT"
        assert refs[1].getValue() == "/LogAndTrace/DltContexts/Context2"
