"""Writer round-trip tests for SystemSignalGroup (Table 6.13, p.324).

Serialized through the SYSTEM-SIGNAL-GROUP element; child order per the
SYSTEM-SIGNAL-GROUP group of AUTOSAR_00052.xsd (l.119828).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SystemSignalGroup
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SYSTEM-SIGNAL-REFS",
    "TRANSFORMING-SYSTEM-SIGNAL-REF",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _populate(group: SystemSignalGroup):
    group.addSystemSignalRef(_ref("/AUTOSAR/SystemSignal1", "SYSTEM-SIGNAL"))
    group.addSystemSignalRef(_ref("/AUTOSAR/SystemSignal2", "SYSTEM-SIGNAL"))
    group.setTransformingSystemSignalRef(_ref("/AUTOSAR/TransformedSignal", "SYSTEM-SIGNAL"))


class TestWriteSystemSignalGroup:
    def test_write_empty(self):
        group = SystemSignalGroup(None, "SigGroup1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroup(parent, group)

        node = parent.find("SYSTEM-SIGNAL-GROUP")
        assert node.find("SYSTEM-SIGNAL-REFS") is None
        assert node.find("TRANSFORMING-SYSTEM-SIGNAL-REF") is None

    def test_write_full_child_order_matches_xsd(self):
        group = SystemSignalGroup(None, "SigGroup1")
        _populate(group)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroup(parent, group)

        node = parent.find("SYSTEM-SIGNAL-GROUP")
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        group = SystemSignalGroup(None, "SigGroup1")
        _populate(group)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroup(parent, group)

        node = parent.find("SYSTEM-SIGNAL-GROUP")
        signal_refs = node.findall("SYSTEM-SIGNAL-REFS/SYSTEM-SIGNAL-REF")
        assert len(signal_refs) == 2
        assert signal_refs[0].text == "/AUTOSAR/SystemSignal1"
        assert signal_refs[0].get("DEST") == "SYSTEM-SIGNAL"
        assert signal_refs[1].text == "/AUTOSAR/SystemSignal2"
        assert signal_refs[1].get("DEST") == "SYSTEM-SIGNAL"

        transforming_ref = node.find("TRANSFORMING-SYSTEM-SIGNAL-REF")
        assert transforming_ref.text == "/AUTOSAR/TransformedSignal"
        assert transforming_ref.get("DEST") == "SYSTEM-SIGNAL"

    def test_round_trip_full(self):
        group = SystemSignalGroup(None, "SigGroup1")
        _populate(group)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroup(parent, group)

        reloaded = SystemSignalGroup(None, "SigGroup1")
        ARXMLParser().readSystemSignalGroup(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "SigGroup1"
        signal_refs = reloaded.getSystemSignalRefs()
        assert len(signal_refs) == 2
        assert signal_refs[0].getValue() == "/AUTOSAR/SystemSignal1"
        assert signal_refs[0].getDest() == "SYSTEM-SIGNAL"
        assert signal_refs[1].getValue() == "/AUTOSAR/SystemSignal2"
        assert signal_refs[1].getDest() == "SYSTEM-SIGNAL"
        assert reloaded.getTransformingSystemSignalRef().getValue() == "/AUTOSAR/TransformedSignal"
        assert reloaded.getTransformingSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_round_trip_empty(self):
        group = SystemSignalGroup(None, "SigGroup1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroup(parent, group)

        reloaded = SystemSignalGroup(None, "SigGroup1")
        ARXMLParser().readSystemSignalGroup(_with_ns(parent)[0], reloaded)

        assert reloaded.getSystemSignalRefs() == []
        assert reloaded.getTransformingSystemSignalRef() is None
