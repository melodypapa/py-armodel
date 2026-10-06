"""Writer/reader round-trip tests for IPSecConfigProps (AUTOSAR_CP_TPS_SystemTemplate Table 6.223, p.573).

The writer emits the IP-SEC-CONFIG-PROPS element per the XSD group IP-SEC-CONFIG-PROPS
sequenceOffset order; empty cipher-suite name lists emit no wrapper elements.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecConfigProps, IPsecDpdActionEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "AH-CIPHER-SUITE-NAMES",
    "DPD-ACTION",
    "DPD-DELAY",
    "ESP-CIPHER-SUITE-NAMES",
    "IKE-CIPHER-SUITE-NAME",
    "IKE-OVER-TIME",
    "IKE-RAND-TIME",
    "IKE-REAUTH-TIME",
    "IKE-REKEY-TIME",
    "SA-OVER-TIME",
    "SA-RAND-TIME",
    "SA-REKEY-TIME",
]

BASE_GROUP_TAGS = {"SHORT-NAME", "LONG-NAME", "DESC", "CATEGORY", "INTRODUCTION", "ADMIN-DATA", "ANNOTATIONS", "VARIATION-POINT"}


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _enum(enum_cls, member):
    e = enum_cls()
    e.setValue(member)
    return e


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _time_value(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _full_props() -> IPSecConfigProps:
    props = IPSecConfigProps(AUTOSAR.getInstance(), "Props1")
    props.addAhCipherSuiteName(_string("HMAC/SHA2-256"))
    props.addAhCipherSuiteName(_string("HMAC/SHA2-384"))
    props.setDpdAction(_enum(IPsecDpdActionEnum, IPsecDpdActionEnum.CLEAR))
    props.setDpdDelay(_time_value(300.0))
    props.addEspCipherSuiteName(_string("AES-128+SHA2-256"))
    props.addEspCipherSuiteName(_string("AES-256+SHA2-384"))
    props.setIkeCipherSuiteName(_string("AES-128+SHA2-256"))
    props.setIkeOverTime(_time_value(10.0))
    props.setIkeRandTime(_pos_int("10"))
    props.setIkeReauthTime(_time_value(3600.0))
    props.setIkeRekeyTime(_time_value(7200.0))
    props.setSaOverTime(_pos_int("110"))
    props.setSaRandTime(_time_value(30.0))
    props.setSaRekeyTime(_time_value(4800.0))
    return props


class TestWriteIPSecConfigProps:
    def _write(self, props: IPSecConfigProps) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIPSecConfigProps(parent, props)
        return parent.find("IP-SEC-CONFIG-PROPS")

    def test_write_element_order(self):
        element = self._write(_full_props())

        assert element is not None
        assert [child.tag for child in element if child.tag not in BASE_GROUP_TAGS] == XSD_ELEMENT_ORDER

    def test_write_empty_props_emits_no_wrappers(self):
        props = IPSecConfigProps(AUTOSAR.getInstance(), "EmptyProps")
        element = self._write(props)

        assert element is not None
        tags = [child.tag for child in element]
        assert "AH-CIPHER-SUITE-NAMES" not in tags
        assert "ESP-CIPHER-SUITE-NAMES" not in tags
        assert "DPD-ACTION" not in tags
        assert "DPD-DELAY" not in tags
        assert "SA-REKEY-TIME" not in tags

    def test_round_trip_field_values(self):
        element = self._write(_full_props())
        xml = ET.tostring(element, encoding="unicode")

        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
        node = ARXMLParser().find(root, "IP-SEC-CONFIG-PROPS")
        reparsed = IPSecConfigProps(AUTOSAR.getInstance(), "Props1")
        ARXMLParser().readIPSecConfigProps(node, reparsed)

        assert [v.getValue() for v in reparsed.getAhCipherSuiteNames()] == ["HMAC/SHA2-256", "HMAC/SHA2-384"]
        assert reparsed.getDpdAction().getValue() == "CLEAR"
        assert float(reparsed.getDpdDelay().getValue()) == 300.0
        assert [v.getValue() for v in reparsed.getEspCipherSuiteNames()] == ["AES-128+SHA2-256", "AES-256+SHA2-384"]
        assert reparsed.getIkeCipherSuiteName().getValue() == "AES-128+SHA2-256"
        assert float(reparsed.getIkeOverTime().getValue()) == 10.0
        assert reparsed.getIkeRandTime().getValue() == 10
        assert float(reparsed.getIkeReauthTime().getValue()) == 3600.0
        assert float(reparsed.getIkeRekeyTime().getValue()) == 7200.0
        assert reparsed.getSaOverTime().getValue() == 110
        assert float(reparsed.getSaRandTime().getValue()) == 30.0
        assert float(reparsed.getSaRekeyTime().getValue()) == 4800.0
