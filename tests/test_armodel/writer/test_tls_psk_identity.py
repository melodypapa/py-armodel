"""Writer tests for TlsPskIdentity (AUTOSAR_CP_TPS_SystemTemplate, Table 6.214, p.563).

Direct writeTlsPskIdentity helper; child order per XSD group
TLS-PSK-IDENTITY: PRE-SHARED-KEY-REF, PSK-IDENTITY, PSK-IDENTITY-HINT;
absent members are omitted.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import TlsPskIdentity
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest="CRYPTO-SERVICE-KEY"):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _string(value):
    s = String()
    s.setValue(value)
    return s


def test_write_tls_psk_identity_full():
    psk = TlsPskIdentity()
    psk.setPreSharedKeyRef(_ref("/Crypto/Keys/Master"))
    psk.setPskIdentity(_string("psk_id_1"))
    psk.setPskIdentityHint(_string("hint_1"))

    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlsPskIdentity(parent, psk)

    assert parent[0].tag == "PSK-IDENTITY"
    children = list(parent[0])
    assert [c.tag for c in children] == ["PRE-SHARED-KEY-REF", "PSK-IDENTITY", "PSK-IDENTITY-HINT"]
    assert children[0].get("DEST") == "CRYPTO-SERVICE-KEY"
    assert children[0].text == "/Crypto/Keys/Master"
    assert children[1].text == "psk_id_1"
    assert children[2].text == "hint_1"


def test_write_tls_psk_identity_empty_omits_children():
    psk = TlsPskIdentity()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlsPskIdentity(parent, psk)

    assert len(list(parent[0])) == 0
