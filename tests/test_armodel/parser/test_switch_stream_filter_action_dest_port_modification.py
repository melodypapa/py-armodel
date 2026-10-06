"""
Reader tests for SwitchStreamFilterActionDestPortModification (CP_TPS_SystemTemplate Table 3.93, p.140, R23-11).

Covers the IDENTIFIABLE base level (SHORT-NAME round-trip) and the EGRESS-PORT-REFS /
MODIFICATION children of the SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION element
shape (AUTOSAR_00052.xsd group SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION —
emitted in live documents as the FILTER-ACTION-DEST-PORT-MODIFICATION child of the
SWITCH-STREAM-IDENTIFICATION), the MODIFICATION enum value, the absent-element case and
the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_switch_stream_filter_action_dest_port_modification.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchStreamFilterActionDestPortModification,
    SwitchStreamFilterActionPortModificationEnum,
    SwitchStreamIdentification,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION xmlns='{NS}'>{inner}</SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION xmlns='{NS}' {attrs}>{inner}</SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION>")


def _full_inner() -> str:
    return (
        "<EGRESS-PORT-REFS>"
        "<EGRESS-PORT-REF DEST='COUPLING-PORT'>/AUTOSAR/Switch/Cport2</EGRESS-PORT-REF>"
        "<EGRESS-PORT-REF DEST='COUPLING-PORT'>/AUTOSAR/Switch/Cport3</EGRESS-PORT-REF>"
        "</EGRESS-PORT-REFS>"
        "<MODIFICATION>OVERWRITE</MODIFICATION>"
    )


class TestReadStreamSwitchStreamFilterActionDestPortModification:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs("UUID='5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1'", "")
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "Initial")
        parser.readSwitchStreamFilterActionDestPortModification(element, modification)

        assert modification.getUuid().getValue() == "5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1"
        assert modification.getEgressPortRefs() == []
        assert modification.getModification() is None

    def test_read_egress_port_refs(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "Initial")
        parser.readSwitchStreamFilterActionDestPortModification(element, modification)

        egress_port_refs = modification.getEgressPortRefs()
        assert len(egress_port_refs) == 2
        assert egress_port_refs[0].getValue() == "/AUTOSAR/Switch/Cport2"
        assert egress_port_refs[0].getDest() == "COUPLING-PORT"
        assert egress_port_refs[1].getValue() == "/AUTOSAR/Switch/Cport3"

    def test_read_modification(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "Initial")
        parser.readSwitchStreamFilterActionDestPortModification(element, modification)

        value = modification.getModification()
        assert isinstance(value, SwitchStreamFilterActionPortModificationEnum)
        assert value.getValue() == SwitchStreamFilterActionPortModificationEnum.OVERWRITE

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "Initial")
        parser.readSwitchStreamFilterActionDestPortModification(element, modification)

        assert modification.getEgressPortRefs() == []
        assert modification.getModification() is None

    def test_dispatch_from_switch_stream_identification(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            f"""<SWITCH-STREAM-IDENTIFICATION xmlns='{NS}'>
                <SHORT-NAME>Stream1</SHORT-NAME>
                <FILTER-ACTION-DEST-PORT-MODIFICATION>
                    <SHORT-NAME>DestMod</SHORT-NAME>
                    <EGRESS-PORT-REFS>
                        <EGRESS-PORT-REF DEST='COUPLING-PORT'>/AUTOSAR/Switch/Cport1</EGRESS-PORT-REF>
                    </EGRESS-PORT-REFS>
                    <MODIFICATION>EXTEND</MODIFICATION>
                </FILTER-ACTION-DEST-PORT-MODIFICATION>
            </SWITCH-STREAM-IDENTIFICATION>"""
        )
        stream_identification = SwitchStreamIdentification(MockParent(), "Initial")
        parser.readSwitchStreamIdentification(element, stream_identification)

        modification = stream_identification.getFilterActionDestPortModification()
        assert isinstance(modification, SwitchStreamFilterActionDestPortModification)
        assert modification.getShortName() == "DestMod"
        egress_port_refs = modification.getEgressPortRefs()
        assert len(egress_port_refs) == 1
        assert egress_port_refs[0].getValue() == "/AUTOSAR/Switch/Cport1"
        assert egress_port_refs[0].getDest() == "COUPLING-PORT"
        assert modification.getModification().getValue() == SwitchStreamFilterActionPortModificationEnum.EXTEND
