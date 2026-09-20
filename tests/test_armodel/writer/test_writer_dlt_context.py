"""Tests for the writeDltContext handler and the ARPackage DltContext dispatch (R23-11 DltContext, Table F.48, p.9)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltContext
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "CONTEXT-DESCRIPTION",
    "CONTEXT-ID",
    "DLT-MESSAGES",
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
    ref.setDest("DLT-MESSAGE")
    return ref


def _fill(context: DltContext) -> DltContext:
    context.setContextDescription(_string("Context of the diagnostics application"))
    context.setContextId(_string("CTX1"))
    context.addDltMessageRef(_ref("/LogAndTrace/DltMessages/Message1"))
    context.addDltMessageRef(_ref("/LogAndTrace/DltMessages/Message2"))
    return context


class TestWriteDltContext:
    """Tests for writeDltContext handler (R23-11 DltContext, Table F.48, p.9)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writeDltContext(parent, _fill(DltContext(None, "ctx_one")))
        child = parent.find("DLT-CONTEXT")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("SHORT-NAME").text == "ctx_one"
        assert child.find("CONTEXT-DESCRIPTION").text == "Context of the diagnostics application"
        assert child.find("CONTEXT-ID").text == "CTX1"
        messages_element = child.find("DLT-MESSAGES")
        conditionals = messages_element.findall("DLT-MESSAGE-REF-CONDITIONAL")
        assert len(conditionals) == 2
        assert conditionals[0].find("DLT-MESSAGE-REF").text == "/LogAndTrace/DltMessages/Message1"
        assert conditionals[0].find("DLT-MESSAGE-REF").get("DEST") == "DLT-MESSAGE"
        assert conditionals[1].find("DLT-MESSAGE-REF").text == "/LogAndTrace/DltMessages/Message2"

    def test_empty_wrapper_list_omitted(self, writer):
        parent = _parent()
        writer.writeDltContext(parent, DltContext(None, "ctx_empty"))
        child = parent.find("DLT-CONTEXT")
        assert child is not None
        assert child.find("CONTEXT-DESCRIPTION") is None
        assert child.find("CONTEXT-ID") is None
        assert child.find("DLT-MESSAGES") is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writeDltContext(parent, _fill(DltContext(None, "ctx_one")))
        child = parent.find("DLT-CONTEXT")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = DltContext(None, "ctx_one")
        parser.readDltContext(reloaded.find(f"{{{NS}}}DLT-CONTEXT"), parsed)
        assert parsed.getShortName() == "ctx_one"
        assert parsed.getContextDescription().getValue() == "Context of the diagnostics application"
        assert parsed.getContextId().getValue() == "CTX1"
        refs = parsed.getDltMessageRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/LogAndTrace/DltMessages/Message1"
        assert refs[0].getDest() == "DLT-MESSAGE"
        assert refs[1].getValue() == "/LogAndTrace/DltMessages/Message2"


class TestWriteARPackageDltContextDispatch:
    """Test for the DltContext branch of the writeARPackageElement dispatch."""

    def test_dispatch_emits_dlt_context_tag(self, writer):
        pkg_element = ET.Element("AR-PACKAGE")
        context = DltContext(None, "DC1")
        context.setContextId(_string("CTX8"))
        writer.writeARPackageElement(pkg_element, context)
        children = list(pkg_element)
        assert len(children) == 1
        assert children[0].tag == "DLT-CONTEXT"
        assert children[0].find("SHORT-NAME").text == "DC1"
        assert children[0].find("CONTEXT-ID").text == "CTX8"
