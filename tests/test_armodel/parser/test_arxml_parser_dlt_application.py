"""Tests for the readDltApplication handler (R23-11 DltApplication, Table F.47, p.9)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltApplication
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


class TestReadDltApplication:
    """Tests for readDltApplication handler (R23-11 DltApplication, Table F.47, p.9)."""

    def test_read_dlt_application_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>app_one</SHORT-NAME>
                <APPLICATION-DESCRIPTION>Diagnostics application of the ECU</APPLICATION-DESCRIPTION>
                <APPLICATION-ID>APP1</APPLICATION-ID>
                <CONTEXTS>
                    <DLT-CONTEXT-REF-CONDITIONAL>
                        <DLT-CONTEXT-REF DEST="DLT-CONTEXT">/LogAndTrace/DltContexts/Context1</DLT-CONTEXT-REF>
                    </DLT-CONTEXT-REF-CONDITIONAL>
                    <DLT-CONTEXT-REF-CONDITIONAL>
                        <DLT-CONTEXT-REF DEST="DLT-CONTEXT">/LogAndTrace/DltContexts/Context2</DLT-CONTEXT-REF>
                    </DLT-CONTEXT-REF-CONDITIONAL>
                </CONTEXTS>
            """,
            root_tag="DLT-APPLICATION",
        )
        application = DltApplication(None, "app_one")
        parser.readDltApplication(element, application)
        assert application.getShortName() == "app_one"
        assert application.getApplicationDescription().getValue() == "Diagnostics application of the ECU"
        assert application.getApplicationId().getValue() == "APP1"
        refs = application.getContextRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/LogAndTrace/DltContexts/Context1"
        assert refs[0].getDest() == "DLT-CONTEXT"
        assert refs[1].getValue() == "/LogAndTrace/DltContexts/Context2"

    def test_read_dlt_application_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DLT-APPLICATION",
        )
        application = DltApplication(None, "app_empty")
        parser.readDltApplication(element, application)
        assert application.getApplicationDescription() is None
        assert application.getApplicationId() is None
        assert application.getContextRefs() == []
