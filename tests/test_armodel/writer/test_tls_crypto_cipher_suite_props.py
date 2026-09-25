"""Writer tests for TlsCryptoCipherSuiteProps (AUTOSAR_CP_TPS_SystemTemplate, Table 6.215, p.563).

Direct writeTlsCryptoCipherSuiteProps helper; child order per XSD complexType
TLS-CRYPTO-CIPHER-SUITE-PROPS (IDENTIFIABLE group first — SHORT-NAME — then the class
group's TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC); absent members are omitted.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import TlsCryptoCipherSuiteProps
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def test_write_tls_crypto_cipher_suite_props_full():
    props = TlsCryptoCipherSuiteProps(_MockParent(), "Props")
    props.setTcpIpTlsUseSecurityExtensionForceEncryptThenMac(_bool(True))

    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlsCryptoCipherSuiteProps(parent, props)

    assert parent[0].tag == "PROPS"
    children = list(parent[0])
    assert [c.tag for c in children] == ["SHORT-NAME", "TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC"]
    assert children[0].text == "Props"
    assert children[1].text == "true"


def test_write_tls_crypto_cipher_suite_props_empty_omits_optional_children():
    props = TlsCryptoCipherSuiteProps(_MockParent(), "Props")
    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlsCryptoCipherSuiteProps(parent, props)

    children = list(parent[0])
    assert [c.tag for c in children] == ["SHORT-NAME"]
