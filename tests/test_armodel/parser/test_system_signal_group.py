"""Parser tests for SystemSignalGroup (Table 6.13, p.324).

Child set and order per the SYSTEM-SIGNAL-GROUP group of AUTOSAR_00052.xsd (l.119828).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SystemSignalGroup
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<SYSTEM-SIGNAL-GROUP xmlns='{NS}'>
    <SHORT-NAME>SigGroup1</SHORT-NAME>
    <SYSTEM-SIGNAL-REFS>
        <SYSTEM-SIGNAL-REF DEST='SYSTEM-SIGNAL'>/AUTOSAR/SystemSignal1</SYSTEM-SIGNAL-REF>
        <SYSTEM-SIGNAL-REF DEST='SYSTEM-SIGNAL'>/AUTOSAR/SystemSignal2</SYSTEM-SIGNAL-REF>
    </SYSTEM-SIGNAL-REFS>
    <TRANSFORMING-SYSTEM-SIGNAL-REF DEST='SYSTEM-SIGNAL'>/AUTOSAR/TransformedSignal</TRANSFORMING-SYSTEM-SIGNAL-REF>
</SYSTEM-SIGNAL-GROUP>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadSystemSignalGroup:
    def test_read_full(self):
        group = SystemSignalGroup(None, "SigGroup1")
        ARXMLParser().readSystemSignalGroup(ET.fromstring(FULL_XML), group)

        assert group.getShortName() == "SigGroup1"

        signal_refs = group.getSystemSignalRefs()
        assert len(signal_refs) == 2
        assert signal_refs[0].getValue() == "/AUTOSAR/SystemSignal1"
        assert signal_refs[0].getDest() == "SYSTEM-SIGNAL"
        assert signal_refs[1].getValue() == "/AUTOSAR/SystemSignal2"
        assert signal_refs[1].getDest() == "SYSTEM-SIGNAL"

        assert group.getTransformingSystemSignalRef().getValue() == "/AUTOSAR/TransformedSignal"
        assert group.getTransformingSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_minimal(self):
        group = SystemSignalGroup(None, "SigGroup1")
        element = ET.fromstring(f"<SYSTEM-SIGNAL-GROUP xmlns='{NS}'><SHORT-NAME>SigGroup1</SHORT-NAME></SYSTEM-SIGNAL-GROUP>")
        ARXMLParser().readSystemSignalGroup(element, group)

        assert group.getShortName() == "SigGroup1"
        assert group.getSystemSignalRefs() == []
        assert group.getTransformingSystemSignalRef() is None

    def test_read_empty_wrapper_list(self):
        group = SystemSignalGroup(None, "SigGroup1")
        element = ET.fromstring(f"<SYSTEM-SIGNAL-GROUP xmlns='{NS}'>" "<SHORT-NAME>SigGroup1</SHORT-NAME>" "<SYSTEM-SIGNAL-REFS/>" "</SYSTEM-SIGNAL-GROUP>")
        ARXMLParser().readSystemSignalGroup(element, group)

        assert group.getSystemSignalRefs() == []
        assert group.getTransformingSystemSignalRef() is None
