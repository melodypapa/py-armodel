"""Writer round-trip tests for ISignalTriggering (Table 6.16, p.330).

Serialized through the I-SIGNAL-TRIGGERING element; child order per the
I-SIGNAL-TRIGGERING group of AUTOSAR_00052.xsd (l.67499).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "I-SIGNAL-GROUP-REF",
    "I-SIGNAL-PORT-REFS",
    "I-SIGNAL-REF",
    "VARIATION-POINT",
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


def _populate(triggering: ISignalTriggering):
    triggering.setISignalGroupRef(_ref("/AUTOSAR/ISignalGroups/Group1", "I-SIGNAL-GROUP"))
    triggering.addISignalPortRef(_ref("/AUTOSAR/ECUs/Ecu1/ISignalPorts/Port1", "I-SIGNAL-PORT"))
    triggering.addISignalPortRef(_ref("/AUTOSAR/ECUs/Ecu2/ISignalPorts/Port2", "I-SIGNAL-PORT"))
    triggering.setISignalRef(_ref("/AUTOSAR/ISignals/Signal1", "I-SIGNAL"))

    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vp_label"))
    triggering.setVariationPoint(variation_point)


def _assert_full_values(triggering: ISignalTriggering):
    assert triggering.getShortName() == "Triggering1"
    assert triggering.getISignalGroupRef().getValue() == "/AUTOSAR/ISignalGroups/Group1"
    assert triggering.getISignalGroupRef().getDest() == "I-SIGNAL-GROUP"
    port_refs = triggering.getISignalPortRefs()
    assert len(port_refs) == 2
    assert port_refs[0].getValue() == "/AUTOSAR/ECUs/Ecu1/ISignalPorts/Port1"
    assert port_refs[0].getDest() == "I-SIGNAL-PORT"
    assert port_refs[1].getValue() == "/AUTOSAR/ECUs/Ecu2/ISignalPorts/Port2"
    assert port_refs[1].getDest() == "I-SIGNAL-PORT"
    assert triggering.getISignalRef().getValue() == "/AUTOSAR/ISignals/Signal1"
    assert triggering.getISignalRef().getDest() == "I-SIGNAL"
    assert triggering.getVariationPoint() is not None
    assert triggering.getVariationPoint().getShortLabel().getValue() == "vp_label"


class TestWriteISignalTriggering:
    def test_write_empty(self):
        triggering = ISignalTriggering(None, "Triggering1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalTriggering(parent, triggering)

        node = parent.find("I-SIGNAL-TRIGGERING")
        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        triggering = ISignalTriggering(None, "Triggering1")
        _populate(triggering)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalTriggering(parent, triggering)

        node = parent.find("I-SIGNAL-TRIGGERING")
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        triggering = ISignalTriggering(None, "Triggering1")
        _populate(triggering)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalTriggering(parent, triggering)

        node = parent.find("I-SIGNAL-TRIGGERING")
        group_ref = node.find("I-SIGNAL-GROUP-REF")
        assert group_ref.text == "/AUTOSAR/ISignalGroups/Group1"
        assert group_ref.get("DEST") == "I-SIGNAL-GROUP"
        port_refs = node.findall("I-SIGNAL-PORT-REFS/I-SIGNAL-PORT-REF")
        assert [ref.text for ref in port_refs] == [
            "/AUTOSAR/ECUs/Ecu1/ISignalPorts/Port1",
            "/AUTOSAR/ECUs/Ecu2/ISignalPorts/Port2",
        ]
        assert all(ref.get("DEST") == "I-SIGNAL-PORT" for ref in port_refs)
        signal_ref = node.find("I-SIGNAL-REF")
        assert signal_ref.text == "/AUTOSAR/ISignals/Signal1"
        assert signal_ref.get("DEST") == "I-SIGNAL"
        assert node.find("VARIATION-POINT/SHORT-LABEL").text == "vp_label"

    def test_round_trip_full(self):
        triggering = ISignalTriggering(None, "Triggering1")
        _populate(triggering)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalTriggering(parent, triggering)

        reloaded = ISignalTriggering(None, "Triggering1")
        ARXMLParser().readISignalTriggering(_with_ns(parent)[0], reloaded)

        _assert_full_values(reloaded)

    def test_round_trip_empty_wrapper_list(self):
        triggering = ISignalTriggering(None, "Triggering1")
        triggering.setISignalRef(_ref("/AUTOSAR/ISignals/Signal1", "I-SIGNAL"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalTriggering(parent, triggering)

        node = parent.find("I-SIGNAL-TRIGGERING")
        assert node.find("I-SIGNAL-PORT-REFS") is None

        reloaded = ISignalTriggering(None, "Triggering1")
        ARXMLParser().readISignalTriggering(_with_ns(parent)[0], reloaded)

        assert reloaded.getISignalPortRefs() == []
        assert reloaded.getISignalRef().getValue() == "/AUTOSAR/ISignals/Signal1"
