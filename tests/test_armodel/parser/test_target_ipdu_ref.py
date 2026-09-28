"""Reader tests for TargetIPduRef (AUTOSAR_CP_TPS_SystemTemplate Table 8.4, p.841).

getTargetIPduRef reads the XSD group TARGET-I-PDU-REF (00052.xsd L120230):
DEFAULT-VALUE (PDU-MAPPING-DEFAULT-VALUE wrapper carrying DEFAULT-VALUE-ELEMENTS)
first, then TARGET-I-PDU-REF (REF + DEST PDU-TRIGGERING) — after the AR-OBJECT
group; no VARIATION-POINT in the complexType.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _target_ipdu_element(with_default_value=True):
    xml = """<ROOT xmlns='%s'><TARGET-I-PDU>
        %s
        <TARGET-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PduTriggering_Target</TARGET-I-PDU-REF>
    </TARGET-I-PDU></ROOT>""" % (
        NS,
        """<DEFAULT-VALUE>
            <DEFAULT-VALUE-ELEMENTS>
                <DEFAULT-VALUE-ELEMENT><ELEMENT-BYTE-VALUE>171</ELEMENT-BYTE-VALUE><ELEMENT-POSITION>0</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>
                <DEFAULT-VALUE-ELEMENT><ELEMENT-BYTE-VALUE>204</ELEMENT-BYTE-VALUE><ELEMENT-POSITION>1</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>
            </DEFAULT-VALUE-ELEMENTS>
        </DEFAULT-VALUE>""" if with_default_value else "",
    )
    return ET.fromstring(xml)


class TestGetTargetIPduRef:
    def test_read_all_elements(self):
        target = ARXMLParser().getTargetIPduRef(_target_ipdu_element(), "TARGET-I-PDU")

        ref = target.getTargetIPduRef()
        assert ref.getValue() == "/Cluster/PduTriggering_Target"
        assert ref.getDest() == "PDU-TRIGGERING"

        default_value = target.getDefaultValue()
        assert default_value is not None
        elements = default_value.getDefaultValueElements()
        assert len(elements) == 2
        assert elements[0].getElementByteValue().getValue() == 171
        assert elements[0].getElementPosition().getValue() == 0
        assert elements[1].getElementByteValue().getValue() == 204
        assert elements[1].getElementPosition().getValue() == 1

    def test_read_ref_only(self):
        target = ARXMLParser().getTargetIPduRef(_target_ipdu_element(with_default_value=False), "TARGET-I-PDU")

        assert target.getTargetIPduRef().getValue() == "/Cluster/PduTriggering_Target"
        assert target.getTargetIPduRef().getDest() == "PDU-TRIGGERING"
        assert target.getDefaultValue() is None

    def test_absent_element_returns_none(self):
        root = ET.fromstring("<OTHER xmlns='%s'/>" % NS)

        assert ARXMLParser().getTargetIPduRef(root, "TARGET-I-PDU") is None

    def test_dispatch_via_ipdu_mappings(self):
        gateway_xml = (
            """<GATEWAY xmlns='%s'>
            <I-PDU-MAPPINGS>
                <I-PDU-MAPPING>
                    <SOURCE-I-PDU-REF DEST="I-SIGNAL-I-PDU">/Cluster/Src</SOURCE-I-PDU-REF>
                    <TARGET-I-PDU>
                        <DEFAULT-VALUE>
                            <DEFAULT-VALUE-ELEMENTS>
                                <DEFAULT-VALUE-ELEMENT><ELEMENT-BYTE-VALUE>7</ELEMENT-BYTE-VALUE><ELEMENT-POSITION>3</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>
                            </DEFAULT-VALUE-ELEMENTS>
                        </DEFAULT-VALUE>
                        <TARGET-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Target</TARGET-I-PDU-REF>
                    </TARGET-I-PDU>
                </I-PDU-MAPPING>
            </I-PDU-MAPPINGS>
        </GATEWAY>""" % NS
        )
        root = ET.fromstring(gateway_xml)

        mappings = ARXMLParser().getIPduMappings(root)
        assert len(mappings) == 1
        target = mappings[0].getTargetIPdu()
        assert target.getTargetIPduRef().getValue() == "/Cluster/PT_Target"
        elements = target.getDefaultValue().getDefaultValueElements()
        assert len(elements) == 1
        assert elements[0].getElementByteValue().getValue() == 7
        assert elements[0].getElementPosition().getValue() == 3
