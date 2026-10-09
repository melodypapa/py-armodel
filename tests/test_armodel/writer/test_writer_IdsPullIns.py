"""Writer tests for the IdsM signature-support and security-event-context-data elements."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import IdsmSignatureSupportAp, IdsmSignatureSupportCp, SecurityEventContextData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteIdsPullIns:
    def test_write_signature_support_ap(self):
        obj = IdsmSignatureSupportAp()
        value = String()
        value.setValue("TLS-AES-128-GCM")
        obj.setCryptoPrimitive(value)
        obj.setKeySlotRef(RefType().setValue("/Pkg/KeySlot").setDest("CRYPTO-KEY-SLOT"))

        container = ET.Element("CONTAINER")
        ARXMLWriter().writeIdsmSignatureSupportAp(container, obj)
        element = container.find("SIGNATURE-SUPPORT-AP")

        assert element.find("CRYPTO-PRIMITIVE").text == "TLS-AES-128-GCM"
        key_slot_ref = element.find("KEY-SLOT-REF")
        assert key_slot_ref.text == "/Pkg/KeySlot"
        assert key_slot_ref.attrib["DEST"] == "CRYPTO-KEY-SLOT"

    def test_write_signature_support_cp(self):
        obj = IdsmSignatureSupportCp()
        obj.setAuthenticationRef(RefType().setValue("/Pkg/Primitive").setDest("CRYPTO-SERVICE-PRIMITIVE"))
        obj.setCryptoServiceKeyRef(RefType().setValue("/Pkg/Key").setDest("CRYPTO-SERVICE-KEY"))

        container = ET.Element("CONTAINER")
        ARXMLWriter().writeIdsmSignatureSupportCp(container, obj)
        element = container.find("SIGNATURE-SUPPORT-CP")

        assert element.find("AUTHENTICATION-REF").text == "/Pkg/Primitive"
        assert element.find("CRYPTO-SERVICE-KEY-REF").text == "/Pkg/Key"

    def test_write_security_event_context_data(self):
        obj = SecurityEventContextData()

        container = ET.Element("CONTEXT-DATAS")
        ARXMLWriter().writeSecurityEventContextData(container, obj)
        element = container.find("SECURITY-EVENT-CONTEXT-DATA")

        assert element is not None

    def test_round_trip_signature_support_ap(self):
        obj = IdsmSignatureSupportAp()
        value = String()
        value.setValue("TLS-AES-128-GCM")
        obj.setCryptoPrimitive(value)
        obj.setKeySlotRef(RefType().setValue("/Pkg/KeySlot").setDest("CRYPTO-KEY-SLOT"))

        container = ET.Element("CONTAINER")
        ARXMLWriter().writeIdsmSignatureSupportAp(container, obj)
        element = container.find("SIGNATURE-SUPPORT-AP")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]

        parsed = ARXMLParser().readIdsmSignatureSupportAp(ET.fromstring(xml_str), IdsmSignatureSupportAp())
        assert parsed.getCryptoPrimitive().getValue() == "TLS-AES-128-GCM"
        assert parsed.getKeySlotRef().getValue() == "/Pkg/KeySlot"
