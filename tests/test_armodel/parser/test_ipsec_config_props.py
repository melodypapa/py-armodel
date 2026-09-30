"""Parser tests for IPSecConfigProps (AUTOSAR_CP_TPS_SystemTemplate Table 6.223, p.573).

Element order per XSD group IP-SEC-CONFIG-PROPS (00052.xsd L73693): AH-CIPHER-SUITE-NAMES,
DPD-ACTION, DPD-DELAY, ESP-CIPHER-SUITE-NAMES, IKE-CIPHER-SUITE-NAME, IKE-OVER-TIME,
IKE-RAND-TIME, IKE-REAUTH-TIME, IKE-REKEY-TIME, SA-OVER-TIME, SA-RAND-TIME, SA-REKEY-TIME.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecConfigProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _parse(inner: str) -> IPSecConfigProps:
    root = _snip(inner)
    node = ARXMLParser().find(root, "IP-SEC-CONFIG-PROPS")
    props = IPSecConfigProps(AUTOSAR.getInstance(), "Props1")
    ARXMLParser().readIPSecConfigProps(node, props)
    return props


FULL_INNER = (
    "<IP-SEC-CONFIG-PROPS>"
    "<AH-CIPHER-SUITE-NAMES>"
    "<AH-CIPHER-SUITE-NAME>HMAC/SHA2-256</AH-CIPHER-SUITE-NAME>"
    "<AH-CIPHER-SUITE-NAME>HMAC/SHA2-384</AH-CIPHER-SUITE-NAME>"
    "</AH-CIPHER-SUITE-NAMES>"
    "<DPD-ACTION>CLEAR</DPD-ACTION>"
    "<DPD-DELAY>300.0</DPD-DELAY>"
    "<ESP-CIPHER-SUITE-NAMES>"
    "<ESP-CIPHER-SUITE-NAME>AES-128+SHA2-256</ESP-CIPHER-SUITE-NAME>"
    "<ESP-CIPHER-SUITE-NAME>AES-256+SHA2-384</ESP-CIPHER-SUITE-NAME>"
    "</ESP-CIPHER-SUITE-NAMES>"
    "<IKE-CIPHER-SUITE-NAME>AES-128+SHA2-256</IKE-CIPHER-SUITE-NAME>"
    "<IKE-OVER-TIME>10.0</IKE-OVER-TIME>"
    "<IKE-RAND-TIME>10</IKE-RAND-TIME>"
    "<IKE-REAUTH-TIME>3600.0</IKE-REAUTH-TIME>"
    "<IKE-REKEY-TIME>7200.0</IKE-REKEY-TIME>"
    "<SA-OVER-TIME>110</SA-OVER-TIME>"
    "<SA-RAND-TIME>30.0</SA-RAND-TIME>"
    "<SA-REKEY-TIME>4800.0</SA-REKEY-TIME>"
    "</IP-SEC-CONFIG-PROPS>"
)


class TestReadIPSecConfigProps:
    def test_read_field_values(self):
        props = _parse(FULL_INNER)

        assert [v.getValue() for v in props.getAhCipherSuiteNames()] == ["HMAC/SHA2-256", "HMAC/SHA2-384"]
        assert props.getDpdAction() is not None
        assert props.getDpdAction().getValue() == "CLEAR"
        assert props.getDpdDelay() is not None
        assert float(props.getDpdDelay().getValue()) == 300.0
        assert [v.getValue() for v in props.getEspCipherSuiteNames()] == ["AES-128+SHA2-256", "AES-256+SHA2-384"]
        assert props.getIkeCipherSuiteName() is not None
        assert props.getIkeCipherSuiteName().getValue() == "AES-128+SHA2-256"
        assert props.getIkeOverTime() is not None
        assert float(props.getIkeOverTime().getValue()) == 10.0
        assert props.getIkeRandTime().getValue() == 10
        assert props.getIkeReauthTime() is not None
        assert float(props.getIkeReauthTime().getValue()) == 3600.0
        assert props.getIkeRekeyTime() is not None
        assert float(props.getIkeRekeyTime().getValue()) == 7200.0
        assert props.getSaOverTime().getValue() == 110
        assert props.getSaRandTime() is not None
        assert float(props.getSaRandTime().getValue()) == 30.0
        assert props.getSaRekeyTime() is not None
        assert float(props.getSaRekeyTime().getValue()) == 4800.0

    def test_read_absent_elements_yields_none(self):
        props = _parse("<IP-SEC-CONFIG-PROPS/>")

        assert props.getAhCipherSuiteNames() == []
        assert props.getDpdAction() is None
        assert props.getDpdDelay() is None
        assert props.getEspCipherSuiteNames() == []
        assert props.getIkeCipherSuiteName() is None
        assert props.getIkeOverTime() is None
        assert props.getIkeRandTime() is None
        assert props.getIkeReauthTime() is None
        assert props.getIkeRekeyTime() is None
        assert props.getSaOverTime() is None
        assert props.getSaRandTime() is None
        assert props.getSaRekeyTime() is None

    def test_read_partial_element(self):
        props = _parse("<IP-SEC-CONFIG-PROPS><DPD-ACTION>TRAP</DPD-ACTION><SA-OVER-TIME>110</SA-OVER-TIME></IP-SEC-CONFIG-PROPS>")

        assert props.getDpdAction().getValue() == "TRAP"
        assert props.getSaOverTime().getValue() == 110
        assert props.getAhCipherSuiteNames() == []
        assert props.getDpdDelay() is None
        assert props.getEspCipherSuiteNames() == []
        assert props.getIkeCipherSuiteName() is None
        assert props.getSaRandTime() is None
