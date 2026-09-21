"""Tests for the readPdurIPduGroup handler (R23-11 PdurIPduGroup, Table 6.34, p.352)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PdurIPduGroup
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


def _autosar_root():
    """Return the AUTOSAR singleton for use as a parent in model constructors."""
    return AUTOSAR.getInstance()


class TestReadPdurIPduGroup:
    """Tests for readPdurIPduGroup handler (R23-11 PdurIPduGroup, Table 6.34, p.352)."""

    def test_read_pdur_ipdu_group_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>PduGroup1</SHORT-NAME>
                <COMMUNICATION-MODE>diagnostic</COMMUNICATION-MODE>
                <I-PDUS>
                    <PDU-TRIGGERING-REF-CONDITIONAL>
                        <PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/System/Ecu1/PduTriggering1</PDU-TRIGGERING-REF>
                    </PDU-TRIGGERING-REF-CONDITIONAL>
                    <PDU-TRIGGERING-REF-CONDITIONAL>
                        <PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/System/Ecu1/PduTriggering2</PDU-TRIGGERING-REF>
                    </PDU-TRIGGERING-REF-CONDITIONAL>
                </I-PDUS>
            """,
            root_tag="PDUR-I-PDU-GROUP",
        )
        group = PdurIPduGroup(parent=_autosar_root(), short_name="PduGroup1")
        parser.readPdurIPduGroup(element, group)
        assert group.getCommunicationMode() is not None
        assert group.getCommunicationMode().getValue() == "diagnostic"
        refs = group.getIPduRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/System/Ecu1/PduTriggering1"
        assert refs[0].getDest() == "PDU-TRIGGERING"
        assert refs[1].getValue() == "/System/Ecu1/PduTriggering2"

    def test_read_pdur_ipdu_group_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>PduGroup1</SHORT-NAME>
            """,
            root_tag="PDUR-I-PDU-GROUP",
        )
        group = PdurIPduGroup(parent=_autosar_root(), short_name="PduGroup1")
        parser.readPdurIPduGroup(element, group)
        assert group.getCommunicationMode() is None
        assert group.getIPduRefs() == []
