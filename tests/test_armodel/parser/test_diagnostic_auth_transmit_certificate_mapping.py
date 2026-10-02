"""Parser tests for DiagnosticAuthTransmitCertificateMapping (Table 5.17, p.242).

XSD group DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-MAPPING element order (AUTOSAR_00052.xsd): CRYPTO-SERVICE-CERTIFICATE-REFS, SERVICE-INSTANCE-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthTransmitCertificateMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticAuthTransmitCertificateMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticAuthTransmitCertificateMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<CRYPTO-SERVICE-CERTIFICATE-REFS><CRYPTO-SERVICE-CERTIFICATE-REF DEST='DEST'>/AUTOSAR/CryptoServiceCertificate1</CRYPTO-SERVICE-CERTIFICATE-REF></CRYPTO-SERVICE-CERTIFICATE-REFS><SERVICE-INSTANCE-REF DEST='DEST'>/AUTOSAR/ServiceInstance1</SERVICE-INSTANCE-REF>"
        )
        parser.readDiagnosticAuthTransmitCertificateMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert len(mapping.getCryptoServiceCertificateRefs()) == 1
        assert mapping.getCryptoServiceCertificateRefs()[0].getValue() == "/AUTOSAR/CryptoServiceCertificate1"
        assert mapping.getServiceInstanceRef() is not None
        assert mapping.getServiceInstanceRef().getValue() == "/AUTOSAR/ServiceInstance1"

    def test_read_empty(self, parser):
        mapping = DiagnosticAuthTransmitCertificateMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticAuthTransmitCertificateMapping(element, mapping)
        assert mapping.getCryptoServiceCertificateRefs() == []
        assert mapping.getServiceInstanceRef() is None
