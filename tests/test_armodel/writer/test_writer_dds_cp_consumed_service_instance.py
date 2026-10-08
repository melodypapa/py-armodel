"""
Writer tests for DDS-CP-CONSUMED-SERVICE-INSTANCE elements — DdsCpConsumedServiceInstance, Table 6.154 (p.475, R23-11).

writeDdsCpConsumedServiceInstance creates the DDS-CP-CONSUMED-SERVICE-INSTANCE element,
delegates the inherited levels (SHORT-NAME, UUID — writeIdentifiable — plus the
DDS-CP-SERVICE-INSTANCE group members) to writeDdsCpServiceInstance (called exactly once,
Rule 0013.1/0025), then emits its own group members in XSD sequenceOffset order
(group DDS-CP-CONSUMED-SERVICE-INSTANCE, AUTOSAR_00052.xsd l.28609):
CONSUMED-DDS-OPERATIONS, CONSUMED-DDS-SERVICE-EVENTS, LOCAL-UNICAST-ADDRESSES,
MINOR-VERSION, STATIC-REMOTE-MULTICAST-ADDRESSES, STATIC-REMOTE-UNICAST-ADDRESSES.

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_consumed_service_instance.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    DdsCpServiceInstanceEvent,
    DdsCpServiceInstanceOperation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpConsumedServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AnyVersionString, PositiveInteger, RefType, String
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
    instance = DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "ConsumedInstance1")
    operation = DdsCpServiceInstanceOperation()
    operation.setDdsOperationRequestTriggeringRef(RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Triggers/Req"))
    instance.addConsumedDdsOperation(operation)
    event = DdsCpServiceInstanceEvent()
    event.setDdsEventRef(RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Triggers/Evt"))
    instance.addConsumedDdsServiceEvent(event)
    instance.setLocalUnicastAddressRef(RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Eps/LocalEp"))
    instance.setMinorVersion(AnyVersionString().setValue("2"))
    instance.setStaticRemoteMulticastAddressRef(RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Eps/MulticastEp"))
    instance.setStaticRemoteUnicastAddressRef(RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Eps/UnicastEp"))
    return instance


class TestWriteDdsCpConsumedServiceInstance:
    def test_write_emits_members_in_xsd_order(self):
        """Test that the writer emits the inherited SHORT-NAME plus its own members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpConsumedServiceInstance(parent, _new_instance())

        child = parent.find("DDS-CP-CONSUMED-SERVICE-INSTANCE")
        assert child is not None
        children = [c.tag for c in child]
        assert children[0] == "SHORT-NAME"
        assert child.find("SHORT-NAME").text == "ConsumedInstance1"
        assert children.index("CONSUMED-DDS-OPERATIONS") < children.index("CONSUMED-DDS-SERVICE-EVENTS")
        assert children.index("CONSUMED-DDS-SERVICE-EVENTS") < children.index("LOCAL-UNICAST-ADDRESSES")
        assert children.index("LOCAL-UNICAST-ADDRESSES") < children.index("MINOR-VERSION")
        assert children.index("MINOR-VERSION") < children.index("STATIC-REMOTE-MULTICAST-ADDRESSES")
        assert children.index("STATIC-REMOTE-MULTICAST-ADDRESSES") < children.index("STATIC-REMOTE-UNICAST-ADDRESSES")

        assert child.find("CONSUMED-DDS-OPERATIONS/DDS-CP-SERVICE-INSTANCE-OPERATION/DDS-OPERATION-REQUEST-TRIGGERING-REF").text == "/Fibex/Triggers/Req"
        assert child.find("CONSUMED-DDS-SERVICE-EVENTS/DDS-CP-SERVICE-INSTANCE-EVENT/DDS-EVENT-REF").text == "/Fibex/Triggers/Evt"
        assert child.find("LOCAL-UNICAST-ADDRESSES/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").attrib["DEST"] == "APPLICATION-ENDPOINT"
        assert child.find("MINOR-VERSION").text == "2"
        assert child.find("STATIC-REMOTE-MULTICAST-ADDRESSES/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").text == "/Cluster/Eps/MulticastEp"
        assert child.find("STATIC-REMOTE-UNICAST-ADDRESSES/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").text == "/Cluster/Eps/UnicastEp"

    def test_write_empty_omits_members(self):
        """Test that an empty instance emits only the SHORT-NAME (Identifiable level)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpConsumedServiceInstance(parent, DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "Empty"))
        child = parent.find("DDS-CP-CONSUMED-SERVICE-INSTANCE")
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_emits_inherited_service_instance_members(self):
        """Test that the inherited DDS-CP-SERVICE-INSTANCE group members are emitted via the base helper (Rule 0025)."""
        instance = DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "ConsumedInstance1")
        instance.setDdsServiceQosProfileRef(RefType().setDest("DDS-CP-QOS-PROFILE").setValue("/DdsCpConfig/QosProfiles/Profile1"))
        instance.setServiceInstanceId(PositiveInteger().setValue("42"))
        instance.setServiceInterfaceId(String().setValue("MyServiceInterface"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpConsumedServiceInstance(parent, instance)
        child = parent.find("DDS-CP-CONSUMED-SERVICE-INSTANCE")
        assert child.find("DDS-SERVICE-QOS-PROFILE-REF").text == "/DdsCpConfig/QosProfiles/Profile1"
        assert child.find("SERVICE-INSTANCE-ID").text == "42"
        assert child.find("SERVICE-INTERFACE-ID").text == "MyServiceInterface"

    def test_round_trip_via_file(self, tmp_path):
        """Element-level round-trip: write, reload, read back via readDdsCpConsumedServiceInstance, assert field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpConsumedServiceInstance(parent, _new_instance())
        inner = ET.tostring(parent[0]).decode("utf-8")

        out_file = str(tmp_path / "dds_cp_consumed_service_instance.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        re_instance = DdsCpConsumedServiceInstance(re_document, "ConsumedInstance1")
        parser.readDdsCpConsumedServiceInstance(ET.parse(out_file).getroot()[0], re_instance)

        assert re_instance.getShortName() == "ConsumedInstance1"
        operations = re_instance.getConsumedDdsOperations()
        assert len(operations) == 1
        assert operations[0].getDdsOperationRequestTriggeringRef().getValue() == "/Fibex/Triggers/Req"
        events = re_instance.getConsumedDdsServiceEvents()
        assert len(events) == 1
        assert events[0].getDdsEventRef().getValue() == "/Fibex/Triggers/Evt"
        assert re_instance.getLocalUnicastAddressRef().getValue() == "/Cluster/Eps/LocalEp"
        assert re_instance.getMinorVersion().getValue() == "2"
        assert re_instance.getStaticRemoteMulticastAddressRef().getValue() == "/Cluster/Eps/MulticastEp"
        assert re_instance.getStaticRemoteUnicastAddressRef().getValue() == "/Cluster/Eps/UnicastEp"
