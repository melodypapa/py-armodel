"""
Writer tests for the DdsCpServiceInstance group members — DdsCpServiceInstance, Table 6.152 (p.472, R23-11).

writeDdsCpServiceInstance writes the IDENTIFIABLE level (SHORT-NAME, UUID —
writeIdentifiable) and the group members DDS-FIELD-REPLY-TOPIC-REF,
DDS-FIELD-REQUEST-TOPIC-REF, DDS-METHOD-REPLY-TOPIC-REF, DDS-METHOD-REQUEST-TOPIC-REF,
DDS-SERVICE-QOS-PROFILE-REF, SERVICE-INSTANCE-ID, SERVICE-INTERFACE-ID in XSD
sequenceOffset order (group DDS-CP-SERVICE-INSTANCE, AUTOSAR_00052.xsd l.29079) INTO the
element passed by the caller — the abstract class has no own complexType; the subclass
writers create their element and delegate here.

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_service_instance.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpConsumedServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_instance() -> DdsCpConsumedServiceInstance:
    instance = DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "DdsInstance1")
    instance.setDdsFieldReplyTopicRef(RefType().setDest("DDS-CP-TOPIC").setValue("/DdsCpConfig/Topics/FieldReplyTopic"))
    instance.setDdsFieldRequestTopicRef(RefType().setDest("DDS-CP-TOPIC").setValue("/DdsCpConfig/Topics/FieldRequestTopic"))
    instance.setDdsMethodReplyTopicRef(RefType().setDest("DDS-CP-TOPIC").setValue("/DdsCpConfig/Topics/MethodReplyTopic"))
    instance.setDdsMethodRequestTopicRef(RefType().setDest("DDS-CP-TOPIC").setValue("/DdsCpConfig/Topics/MethodRequestTopic"))
    instance.setDdsServiceQosProfileRef(RefType().setDest("DDS-CP-QOS-PROFILE").setValue("/DdsCpConfig/QosProfiles/Profile1"))
    instance.setServiceInstanceId(PositiveInteger().setValue("42"))
    instance.setServiceInterfaceId(String().setValue("MyServiceInterface"))
    return instance


class TestWriteDdsCpServiceInstance:
    def test_write_emits_members_in_xsd_order(self):
        """Test that the writer emits SHORT-NAME and all seven members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstance(parent, _new_instance())

        children = [child.tag for child in parent]
        assert children[0] == "SHORT-NAME"
        assert parent.find("SHORT-NAME").text == "DdsInstance1"
        assert children.index("DDS-FIELD-REPLY-TOPIC-REF") < children.index("DDS-FIELD-REQUEST-TOPIC-REF")
        assert children.index("DDS-FIELD-REQUEST-TOPIC-REF") < children.index("DDS-METHOD-REPLY-TOPIC-REF")
        assert children.index("DDS-METHOD-REPLY-TOPIC-REF") < children.index("DDS-METHOD-REQUEST-TOPIC-REF")
        assert children.index("DDS-METHOD-REQUEST-TOPIC-REF") < children.index("DDS-SERVICE-QOS-PROFILE-REF")
        assert children.index("DDS-SERVICE-QOS-PROFILE-REF") < children.index("SERVICE-INSTANCE-ID")
        assert children.index("SERVICE-INSTANCE-ID") < children.index("SERVICE-INTERFACE-ID")

        qos_ref = parent.find("DDS-SERVICE-QOS-PROFILE-REF")
        assert qos_ref.attrib["DEST"] == "DDS-CP-QOS-PROFILE"
        assert qos_ref.text == "/DdsCpConfig/QosProfiles/Profile1"
        assert parent.find("SERVICE-INSTANCE-ID").text == "42"
        assert parent.find("SERVICE-INTERFACE-ID").text == "MyServiceInterface"

    def test_write_empty_omits_members(self):
        """Test that an empty instance emits only the SHORT-NAME (Identifiable level)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstance(parent, DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "Empty"))
        children = [child.tag for child in parent]
        assert children == ["SHORT-NAME"]

    def test_round_trip_via_subclass_element(self, tmp_path):
        """Element-level round-trip: write into a DDS-CP-CONSUMED-SERVICE-INSTANCE wrapper,
        reload, read back via readDdsCpServiceInstance, assert field values."""
        parent = ET.Element("DDS-CP-CONSUMED-SERVICE-INSTANCE")
        ARXMLWriter().writeDdsCpServiceInstance(parent, _new_instance())
        inner = ET.tostring(parent).decode("utf-8")

        out_file = str(tmp_path / "dds_cp_service_instance.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        re_instance = DdsCpConsumedServiceInstance(re_document, "DdsInstance1")
        parser.readDdsCpServiceInstance(ET.parse(out_file).getroot()[0], re_instance)

        assert re_instance.getShortName() == "DdsInstance1"
        assert re_instance.getDdsFieldReplyTopicRef().getValue() == "/DdsCpConfig/Topics/FieldReplyTopic"
        assert re_instance.getDdsFieldRequestTopicRef().getValue() == "/DdsCpConfig/Topics/FieldRequestTopic"
        assert re_instance.getDdsMethodReplyTopicRef().getValue() == "/DdsCpConfig/Topics/MethodReplyTopic"
        assert re_instance.getDdsMethodRequestTopicRef().getValue() == "/DdsCpConfig/Topics/MethodRequestTopic"
        assert re_instance.getDdsServiceQosProfileRef().getDest() == "DDS-CP-QOS-PROFILE"
        assert re_instance.getServiceInstanceId().getValue() == 42
        assert re_instance.getServiceInterfaceId().getValue() == "MyServiceInterface"
