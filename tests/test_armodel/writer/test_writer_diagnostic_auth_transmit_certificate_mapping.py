"""
Tests for writing DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-MAPPING elements —
DiagnosticAuthTransmitCertificateMapping, Table 5.17 (p.242, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_auth_transmit_certificate_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthTransmitCertificateMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticAuthTransmitCertificateMapping:
    """Tests for writeDiagnosticAuthTransmitCertificateMapping — own element field values (Table 5.17)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticAuthTransmitCertificateMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticAuthTransmitCertificateMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificateMapping(parent, package.getReferrableElement("M1", DiagnosticAuthTransmitCertificateMapping))

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticAuthTransmitCertificateMapping("M1")
        mapping.addCryptoServiceCertificateRef(RefType().setValue("/AUTOSAR/CryptoServiceCertificate1"))
        mapping.setServiceInstanceRef(RefType().setValue("/AUTOSAR/ServiceInstance1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificateMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "CRYPTO-SERVICE-CERTIFICATE-REFS", "SERVICE-INSTANCE-REF"]
        assert child.find("CRYPTO-SERVICE-CERTIFICATE-REFS/CRYPTO-SERVICE-CERTIFICATE-REF").text == "/AUTOSAR/CryptoServiceCertificate1"
        assert child.find("SERVICE-INSTANCE-REF").text == "/AUTOSAR/ServiceInstance1"
