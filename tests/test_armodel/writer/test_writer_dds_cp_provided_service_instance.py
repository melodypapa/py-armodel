"""
Writer tests for DDS-CP-PROVIDED-SERVICE-INSTANCE elements — DdsCpProvidedServiceInstance, Table 6.153 (p.473, R23-11).

writeDdsCpProvidedServiceInstance emits <DDS-CP-PROVIDED-SERVICE-INSTANCE> with the group
members in XSD sequenceOffset order (LOCAL-UNICAST-ADDRESSES, MINOR-VERSION,
PROVIDED-DDS-OPERATIONS, PROVIDED-DDS-SERVICE-INSTANCE-EVENTS,
STATIC-REMOTE-MULTICAST-ADDRESSES, STATIC-REMOTE-UNICAST-ADDRESSES — wrappers only when
non-empty) plus the AR-OBJECT S/T attributes (AUTOSAR_00052.xsd l.28944).

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_provided_service_instance.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    DdsCpProvidedServiceInstance,
    DdsCpServiceInstanceEvent,
    DdsCpServiceInstanceOperation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, RefType, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_instance() -> DdsCpProvidedServiceInstance:
    instance = DdsCpProvidedServiceInstance()
    instance.setLocalUnicastAddressRef(RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Eps/LocalEp"))
    instance.setMinorVersion(PositiveInteger().setValue("4"))
    operation = DdsCpServiceInstanceOperation()
    operation.setDdsOperationRequestTriggeringRef(RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Triggers/Req"))
    instance.addProvidedDdsOperation(operation)
    event = DdsCpServiceInstanceEvent()
    event.setDdsEventRef(RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Triggers/Evt"))
    instance.addProvidedDdsServiceInstanceEvent(event)
    instance.setStaticRemoteMulticastAddressRef(RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Eps/MulticastEp"))
    instance.addStaticRemoteUnicastAddressRef(RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Eps/UnicastEp1"))
    instance.addStaticRemoteUnicastAddressRef(RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Eps/UnicastEp2"))
    instance.setChecksum(String().setValue("42"))
    instance.setTimestamp(DateTime().setValue("2025-05-05T00:00:00Z"))
    return instance


class TestWriteDdsCpProvidedServiceInstance:
    def test_write_emits_element_and_children_in_xsd_order(self):
        """Test that the writer emits the element with all members in XSD sequenceOffset order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpProvidedServiceInstance(parent, _new_instance())
        node = parent.find("DDS-CP-PROVIDED-SERVICE-INSTANCE")
        assert node is not None
        children = [child.tag for child in node]
        assert children == [
            "LOCAL-UNICAST-ADDRESSES",
            "MINOR-VERSION",
            "PROVIDED-DDS-OPERATIONS",
            "PROVIDED-DDS-SERVICE-INSTANCE-EVENTS",
            "STATIC-REMOTE-MULTICAST-ADDRESSES",
            "STATIC-REMOTE-UNICAST-ADDRESSES",
        ]
        assert node.find("MINOR-VERSION").text == "4"
        local_ref = node.find("LOCAL-UNICAST-ADDRESSES/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF")
        assert local_ref.attrib["DEST"] == "APPLICATION-ENDPOINT"
        assert local_ref.text == "/Cluster/Eps/LocalEp"
        operation_node = node.find("PROVIDED-DDS-OPERATIONS/DDS-CP-SERVICE-INSTANCE-OPERATION")
        assert operation_node.find("DDS-OPERATION-REQUEST-TRIGGERING-REF").text == "/Fibex/Triggers/Req"
        event_node = node.find("PROVIDED-DDS-SERVICE-INSTANCE-EVENTS/DDS-CP-SERVICE-INSTANCE-EVENT")
        assert event_node.find("DDS-EVENT-REF").text == "/Fibex/Triggers/Evt"
        unicast_conditionals = node.findall("STATIC-REMOTE-UNICAST-ADDRESSES/APPLICATION-ENDPOINT-REF-CONDITIONAL")
        assert len(unicast_conditionals) == 2
        assert unicast_conditionals[0].find("APPLICATION-ENDPOINT-REF").text == "/Cluster/Eps/UnicastEp1"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpProvidedServiceInstance(parent, _new_instance())
        node = parent.find("DDS-CP-PROVIDED-SERVICE-INSTANCE")
        assert node.attrib["S"] == "42"
        assert node.attrib["T"] == "2025-05-05T00:00:00Z"

    def test_write_empty_omits_wrappers(self):
        """Test that an empty instance emits no wrapper elements (wrapper only when non-empty)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpProvidedServiceInstance(parent, DdsCpProvidedServiceInstance())
        node = parent.find("DDS-CP-PROVIDED-SERVICE-INSTANCE")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values one level down."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpProvidedServiceInstance(parent, _new_instance())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsCpProvidedServiceInstance()
        ARXMLParser().readDdsCpProvidedServiceInstance(root.find("{%s}DDS-CP-PROVIDED-SERVICE-INSTANCE" % NS), reloaded)
        assert reloaded.getLocalUnicastAddressRef().getValue() == "/Cluster/Eps/LocalEp"
        assert reloaded.getMinorVersion().getValue() == 4
        assert len(reloaded.getProvidedDdsOperations()) == 1
        assert reloaded.getProvidedDdsOperations()[0].getDdsOperationRequestTriggeringRef().getValue() == "/Fibex/Triggers/Req"
        assert len(reloaded.getProvidedDdsServiceInstanceEvents()) == 1
        assert reloaded.getProvidedDdsServiceInstanceEvents()[0].getDdsEventRef().getValue() == "/Fibex/Triggers/Evt"
        assert reloaded.getStaticRemoteMulticastAddressRef().getValue() == "/Cluster/Eps/MulticastEp"
        assert len(reloaded.getStaticRemoteUnicastAddressRefs()) == 2
        assert reloaded.getStaticRemoteUnicastAddressRefs()[1].getValue() == "/Cluster/Eps/UnicastEp2"
        assert reloaded.getChecksum().getValue() == "42"
        assert reloaded.getTimestamp().getValue() == "2025-05-05T00:00:00Z"
