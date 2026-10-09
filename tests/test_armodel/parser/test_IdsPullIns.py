"""Parser tests for the IdsM signature-support and security-event-context-data elements."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import IdsmSignatureSupportAp, IdsmSignatureSupportCp, SecurityEventContextData
from armodel.parser.arxml_parser import ARXMLParser


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    xml_str = re.sub(r"^(<[A-Za-z][\w.-]*)", r'\1 xmlns="http://autosar.org/schema/r4.0"', xml_str)
    return ET.fromstring(xml_str)


class TestReadIdsPullIns:
    def test_read_signature_support_ap(self):
        element = ET.Element("SIGNATURE-SUPPORT-AP")
        crypto = ET.SubElement(element, "CRYPTO-PRIMITIVE")
        crypto.text = "TLS-AES-128-GCM"
        key_slot_ref = ET.SubElement(element, "KEY-SLOT-REF")
        key_slot_ref.attrib["DEST"] = "CRYPTO-KEY-SLOT"
        key_slot_ref.text = "/Pkg/KeySlot"

        obj = ARXMLParser().readIdsmSignatureSupportAp(_round_trip(element), IdsmSignatureSupportAp())
        assert obj.getCryptoPrimitive().getValue() == "TLS-AES-128-GCM"
        assert obj.getKeySlotRef().getValue() == "/Pkg/KeySlot"
        assert obj.getKeySlotRef().getDest() == "CRYPTO-KEY-SLOT"

    def test_read_signature_support_cp(self):
        element = ET.Element("SIGNATURE-SUPPORT-CP")
        auth_ref = ET.SubElement(element, "AUTHENTICATION-REF")
        auth_ref.attrib["DEST"] = "CRYPTO-SERVICE-PRIMITIVE"
        auth_ref.text = "/Pkg/Primitive"
        key_ref = ET.SubElement(element, "CRYPTO-SERVICE-KEY-REF")
        key_ref.attrib["DEST"] = "CRYPTO-SERVICE-KEY"
        key_ref.text = "/Pkg/Key"

        obj = ARXMLParser().readIdsmSignatureSupportCp(_round_trip(element), IdsmSignatureSupportCp())
        assert obj.getAuthenticationRef().getValue() == "/Pkg/Primitive"
        assert obj.getCryptoServiceKeyRef().getValue() == "/Pkg/Key"

    def test_read_security_event_context_data(self):
        element = ET.Element("SECURITY-EVENT-CONTEXT-DATA")

        obj = ARXMLParser().readSecurityEventContextData(_round_trip(element), SecurityEventContextData())
        assert isinstance(obj, SecurityEventContextData)
