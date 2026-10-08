"""Parser tests for ISignalTriggering (Table 6.16, p.330).

Child set and order per the I-SIGNAL-TRIGGERING group of AUTOSAR_00052.xsd (l.67499).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<I-SIGNAL-TRIGGERING xmlns='{NS}' UUID='1a2b3c4d-5e6f-47a8-9b0c-1d2e3f4a5b6c'>
    <SHORT-NAME>Triggering1</SHORT-NAME>
    <I-SIGNAL-GROUP-REF DEST='I-SIGNAL-GROUP'>/AUTOSAR/ISignalGroups/Group1</I-SIGNAL-GROUP-REF>
    <I-SIGNAL-PORT-REFS>
        <I-SIGNAL-PORT-REF DEST='I-SIGNAL-PORT'>/AUTOSAR/ECUs/Ecu1/ISignalPorts/Port1</I-SIGNAL-PORT-REF>
        <I-SIGNAL-PORT-REF DEST='I-SIGNAL-PORT'>/AUTOSAR/ECUs/Ecu2/ISignalPorts/Port2</I-SIGNAL-PORT-REF>
    </I-SIGNAL-PORT-REFS>
    <I-SIGNAL-REF DEST='I-SIGNAL'>/AUTOSAR/ISignals/Signal1</I-SIGNAL-REF>
    <VARIATION-POINT>
        <SHORT-LABEL>vp_label</SHORT-LABEL>
    </VARIATION-POINT>
</I-SIGNAL-TRIGGERING>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadISignalTriggering:
    def test_read_full(self):
        triggering = ISignalTriggering(None, "Triggering1")
        ARXMLParser().readISignalTriggering(ET.fromstring(FULL_XML), triggering)

        assert triggering.getShortName() == "Triggering1"
        assert triggering.getUuid().getValue() == "1a2b3c4d-5e6f-47a8-9b0c-1d2e3f4a5b6c"
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

    def test_read_minimal(self):
        triggering = ISignalTriggering(None, "Triggering1")
        element = ET.fromstring(f"<I-SIGNAL-TRIGGERING xmlns='{NS}'><SHORT-NAME>Triggering1</SHORT-NAME></I-SIGNAL-TRIGGERING>")
        ARXMLParser().readISignalTriggering(element, triggering)

        assert triggering.getShortName() == "Triggering1"
        assert triggering.getISignalRef() is None
        assert triggering.getISignalGroupRef() is None
        assert triggering.getISignalPortRefs() == []
        assert triggering.getVariationPoint() is None

    def test_read_empty_wrapper_list(self):
        triggering = ISignalTriggering(None, "Triggering1")
        element = ET.fromstring(f"""<I-SIGNAL-TRIGGERING xmlns='{NS}'>
            <SHORT-NAME>Triggering1</SHORT-NAME>
            <I-SIGNAL-PORT-REFS/>
            <I-SIGNAL-REF DEST='I-SIGNAL'>/AUTOSAR/ISignals/Signal1</I-SIGNAL-REF>
        </I-SIGNAL-TRIGGERING>""")
        ARXMLParser().readISignalTriggering(element, triggering)

        assert triggering.getISignalPortRefs() == []
        assert triggering.getISignalRef().getValue() == "/AUTOSAR/ISignals/Signal1"
