"""Tests for the readDltContext handler and the ARPackage DLT-CONTEXT dispatch (R23-11 DltContext, Table F.48, p.9)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltContext
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDltContext:
    """Tests for readDltContext handler (R23-11 DltContext, Table F.48, p.9)."""

    def test_read_dlt_context_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>ctx_one</SHORT-NAME>
                <CONTEXT-DESCRIPTION>Context of the diagnostics application</CONTEXT-DESCRIPTION>
                <CONTEXT-ID>CTX1</CONTEXT-ID>
                <DLT-MESSAGES>
                    <DLT-MESSAGE-REF-CONDITIONAL>
                        <DLT-MESSAGE-REF DEST="DLT-MESSAGE">/LogAndTrace/DltMessages/Message1</DLT-MESSAGE-REF>
                    </DLT-MESSAGE-REF-CONDITIONAL>
                    <DLT-MESSAGE-REF-CONDITIONAL>
                        <DLT-MESSAGE-REF DEST="DLT-MESSAGE">/LogAndTrace/DltMessages/Message2</DLT-MESSAGE-REF>
                    </DLT-MESSAGE-REF-CONDITIONAL>
                </DLT-MESSAGES>
            """,
            root_tag="DLT-CONTEXT",
        )
        context = DltContext(None, "ctx_one")
        parser.readDltContext(element, context)
        assert context.getShortName() == "ctx_one"
        assert context.getContextDescription().getValue() == "Context of the diagnostics application"
        assert context.getContextId().getValue() == "CTX1"
        refs = context.getDltMessageRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/LogAndTrace/DltMessages/Message1"
        assert refs[0].getDest() == "DLT-MESSAGE"
        assert refs[1].getValue() == "/LogAndTrace/DltMessages/Message2"

    def test_read_dlt_context_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DLT-CONTEXT",
        )
        context = DltContext(None, "ctx_empty")
        parser.readDltContext(element, context)
        assert context.getContextDescription() is None
        assert context.getContextId() is None
        assert context.getDltMessageRefs() == []


class TestDltContextDispatch:
    """Tests for the DLT-CONTEXT branch of the readARPackageElements dispatch."""

    def test_dispatch_creates_dlt_context_on_package(self, parser):
        parent = ARPackage(parent=AUTOSAR.getInstance(), short_name="TestPkg")
        xml = (
            f"<AR-PACKAGE xmlns='{NS}'>"
            "<SHORT-NAME>TestPkg</SHORT-NAME>"
            "<ELEMENTS>"
            "<DLT-CONTEXT><SHORT-NAME>DC1</SHORT-NAME><CONTEXT-ID>CTX9</CONTEXT-ID></DLT-CONTEXT>"
            "</ELEMENTS>"
            "</AR-PACKAGE>"
        )
        pkg_element = ET.fromstring(xml)
        parser.readARPackageElements(pkg_element, parent)
        created = parent.getElement("DC1", DltContext)
        assert created is not None
        assert isinstance(created, DltContext)
        assert created.getContextId().getValue() == "CTX9"
