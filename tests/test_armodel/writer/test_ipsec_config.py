"""Writer tests for IPSecConfig (Table 6.221, p.571) writeIPSecConfig, the
NetworkEndpoint.ipSecConfig emission (XSD position: after INFRASTRUCTURE-SERVICES,
before NETWORK-ENDPOINT-ADDRESSES) and the package-level IPSecConfigProps dispatch."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import IPSecConfig, NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecConfigProps, IPSecRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _tags(element):
    return [child.tag for child in element]


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _rule(parent, name, mode=None):
    rule = IPSecRule(parent, name)
    if mode is not None:
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPsecModeEnum

        e = IPsecModeEnum()
        e.setValue(mode)
        rule.setMode(e)
    return rule


def test_write_ip_sec_config(writer):
    config = IPSecConfig()
    config.setIpSecConfigPropsRef(_ref("IP-SEC-CONFIG-PROPS", "/pkg/GlobalProps"))
    config.addIPSecRule(_rule(AUTOSAR.getInstance(), "RuleA", mode="tunnel"))
    config.addIPSecRule(_rule(AUTOSAR.getInstance(), "RuleB"))

    element = ET.Element("ROOT")
    writer.writeIPSecConfig(element, config)

    assert _tags(element) == ["IP-SEC-CONFIG"]
    children = _tags(element[0])
    assert children == ["IP-SEC-CONFIG-PROPS-REF", "IP-SEC-RULES"]
    props_ref = element[0][0]
    assert props_ref.get("DEST") == "IP-SEC-CONFIG-PROPS"
    assert props_ref.text == "/pkg/GlobalProps"
    rules = element[0][1]
    assert _tags(rules) == ["IP-SEC-RULE", "IP-SEC-RULE"]
    modes = rules.findall("IP-SEC-RULE/MODE")
    assert len(modes) == 1
    assert modes[0].text == "tunnel"


def test_write_network_endpoint_emits_ip_sec_config_at_xsd_position(writer):
    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    config = IPSecConfig()
    config.setIpSecConfigPropsRef(_ref("IP-SEC-CONFIG-PROPS", "/pkg/Props"))
    endpoint.setIpSecConfig(config)

    element = ET.Element("ROOT")
    writer.writeNetworkEndPoint(element, endpoint)

    ne = element[0]
    assert _tags(ne) == ["SHORT-NAME", "IP-SEC-CONFIG"]


def test_write_network_endpoint_empty_config_omitted(writer):
    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    endpoint.setIpSecConfig(IPSecConfig())

    element = ET.Element("ROOT")
    writer.writeNetworkEndPoint(element, endpoint)

    ne = element[0]
    assert "IP-SEC-CONFIG" not in _tags(ne)


def test_write_ip_sec_config_props_package_dispatch(writer):
    pkg = ARPackage(AUTOSAR.getInstance(), "Pkg")
    props = pkg.createIPSecConfigProps("GlobalProps")
    props.addAhCipherSuiteName(_string("HMAC/SHA2-256"))

    element = ET.Element("ROOT")
    writer.writeARPackageElement(element, props)

    assert element[0].tag == "IP-SEC-CONFIG-PROPS"
    assert element[0].find("SHORT-NAME").text == "GlobalProps"
    names = element[0].find("AH-CIPHER-SUITE-NAMES")
    assert names is not None
    assert names.find("AH-CIPHER-SUITE-NAME").text == "HMAC/SHA2-256"


def _string(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

    s = String()
    s.setValue(value)
    return s


def test_ipsec_config_write_reparse_round_trip(writer):
    from armodel.parser.arxml_parser import ARXMLParser

    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    config = IPSecConfig()
    config.setIpSecConfigPropsRef(_ref("IP-SEC-CONFIG-PROPS", "/pkg/Props"))
    config.addIPSecRule(_rule(AUTOSAR.getInstance(), "RuleA", mode="transport"))
    endpoint.setIpSecConfig(config)

    ne_element = ET.Element("ROOT")
    writer.writeNetworkEndPoint(ne_element, endpoint)
    xml_text = ET.tostring(ne_element, encoding="unicode").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1)

    reparsed = ET.fromstring(xml_text)
    parser = ARXMLParser()
    endpoint2 = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    parser.readNetworkEndPoint(parser.find(reparsed, "NETWORK-ENDPOINT"), endpoint2)

    config2 = endpoint2.getIpSecConfig()
    assert config2 is not None
    assert config2.getIpSecConfigPropsRef().getValue() == "/pkg/Props"
    rules = config2.getIPSecRules()
    assert len(rules) == 1
    assert rules[0].getShortName() == "RuleA"
    assert rules[0].getMode().getValue() == "transport"
