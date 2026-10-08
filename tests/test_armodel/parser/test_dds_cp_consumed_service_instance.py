"""
Tests for reading DDS-CP-CONSUMED-SERVICE-INSTANCE elements — DdsCpConsumedServiceInstance, Table 6.154 (p.475, R23-11).

The class is a nested Identifiable element (aggregated by the still-unsynced
ServiceInstanceCollectionSet.serviceInstance, Table 6.157), so the reusable helper
readDdsCpConsumedServiceInstance is exercised directly on a standalone XML subtree
(XSD complexType DDS-CP-CONSUMED-SERVICE-INSTANCE, AUTOSAR_00052.xsd l.28692: group
sequence AR-OBJECT, REFERRABLE, MULTILANGUAGE-REFERRABLE, IDENTIFIABLE,
ABSTRACT-SERVICE-INSTANCE, DDS-CP-SERVICE-INSTANCE, DDS-CP-CONSUMED-SERVICE-INSTANCE —
the helper calls readDdsCpServiceInstance once for the inherited levels and reads its own
group members CONSUMED-DDS-OPERATIONS, CONSUMED-DDS-SERVICE-EVENTS,
LOCAL-UNICAST-ADDRESSES, MINOR-VERSION, STATIC-REMOTE-MULTICAST-ADDRESSES,
STATIC-REMOTE-UNICAST-ADDRESSES in xml.sequenceOffset order).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_consumed_service_instance.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    DdsCpServiceInstanceEvent,
    DdsCpServiceInstanceOperation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpConsumedServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AnyVersionString

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-CONSUMED-SERVICE-INSTANCE xmlns='{NS}'>{inner}</DDS-CP-CONSUMED-SERVICE-INSTANCE>")


class TestReadDdsCpConsumedServiceInstance:
    """Tests for readDdsCpConsumedServiceInstance — own group field values (Table 6.154)."""

    def _read(self, parser, inner):
        instance = DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "ConsumedInstance1")
        parser.readDdsCpConsumedServiceInstance(_snip(inner), instance)
        return instance

    def test_read_sets_all_fields(self, parser):
        """Test that the consumed collections, wrapper refs and minor version are read with their values."""
        instance = self._read(
            parser,
            "<CONSUMED-DDS-OPERATIONS>"
            '<DDS-CP-SERVICE-INSTANCE-OPERATION><DDS-OPERATION-REQUEST-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/Triggers/Req</DDS-OPERATION-REQUEST-TRIGGERING-REF></DDS-CP-SERVICE-INSTANCE-OPERATION>'
            '<DDS-CP-SERVICE-INSTANCE-OPERATION><DDS-OPERATION-RESPONSE-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/Triggers/Resp</DDS-OPERATION-RESPONSE-TRIGGERING-REF></DDS-CP-SERVICE-INSTANCE-OPERATION>'
            "</CONSUMED-DDS-OPERATIONS>"
            "<CONSUMED-DDS-SERVICE-EVENTS>"
            '<DDS-CP-SERVICE-INSTANCE-EVENT><DDS-EVENT-REF DEST="PDU-TRIGGERING">/Fibex/Triggers/Evt</DDS-EVENT-REF></DDS-CP-SERVICE-INSTANCE-EVENT>'
            "</CONSUMED-DDS-SERVICE-EVENTS>"
            "<LOCAL-UNICAST-ADDRESSES>"
            '<APPLICATION-ENDPOINT-REF-CONDITIONAL><APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/Cluster/Eps/LocalEp</APPLICATION-ENDPOINT-REF></APPLICATION-ENDPOINT-REF-CONDITIONAL>'
            "</LOCAL-UNICAST-ADDRESSES>"
            "<MINOR-VERSION>ANY</MINOR-VERSION>"
            "<STATIC-REMOTE-MULTICAST-ADDRESSES>"
            '<APPLICATION-ENDPOINT-REF-CONDITIONAL><APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/Cluster/Eps/MulticastEp</APPLICATION-ENDPOINT-REF></APPLICATION-ENDPOINT-REF-CONDITIONAL>'
            "</STATIC-REMOTE-MULTICAST-ADDRESSES>"
            "<STATIC-REMOTE-UNICAST-ADDRESSES>"
            '<APPLICATION-ENDPOINT-REF-CONDITIONAL><APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/Cluster/Eps/UnicastEp</APPLICATION-ENDPOINT-REF></APPLICATION-ENDPOINT-REF-CONDITIONAL>'
            "</STATIC-REMOTE-UNICAST-ADDRESSES>",
        )
        operations = instance.getConsumedDdsOperations()
        assert len(operations) == 2
        assert isinstance(operations[0], DdsCpServiceInstanceOperation)
        assert operations[0].getDdsOperationRequestTriggeringRef().getValue() == "/Fibex/Triggers/Req"
        assert operations[1].getDdsOperationResponseTriggeringRef().getValue() == "/Fibex/Triggers/Resp"
        events = instance.getConsumedDdsServiceEvents()
        assert len(events) == 1
        assert isinstance(events[0], DdsCpServiceInstanceEvent)
        assert events[0].getDdsEventRef().getValue() == "/Fibex/Triggers/Evt"
        assert instance.getLocalUnicastAddressRef() is not None
        assert instance.getLocalUnicastAddressRef().getValue() == "/Cluster/Eps/LocalEp"
        assert instance.getLocalUnicastAddressRef().getDest() == "APPLICATION-ENDPOINT"
        assert instance.getMinorVersion() is not None
        assert instance.getMinorVersion().getValue() == "ANY"
        assert instance.getStaticRemoteMulticastAddressRef() is not None
        assert instance.getStaticRemoteMulticastAddressRef().getValue() == "/Cluster/Eps/MulticastEp"
        assert instance.getStaticRemoteUnicastAddressRef() is not None
        assert instance.getStaticRemoteUnicastAddressRef().getValue() == "/Cluster/Eps/UnicastEp"

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None/empty."""
        instance = self._read(parser, "")
        assert instance.getConsumedDdsOperations() == []
        assert instance.getConsumedDdsServiceEvents() == []
        assert instance.getLocalUnicastAddressRef() is None
        assert instance.getMinorVersion() is None
        assert instance.getStaticRemoteMulticastAddressRef() is None
        assert instance.getStaticRemoteUnicastAddressRef() is None

    def test_read_inherited_base_group_members(self, parser):
        """Test that the inherited DDS-CP-SERVICE-INSTANCE group members are read via the base helper (Rule 0025)."""
        instance = self._read(
            parser,
            '<DDS-SERVICE-QOS-PROFILE-REF DEST="DDS-CP-QOS-PROFILE">/DdsCpConfig/QosProfiles/Profile1</DDS-SERVICE-QOS-PROFILE-REF>'
            "<SERVICE-INSTANCE-ID>42</SERVICE-INSTANCE-ID>"
            "<SERVICE-INTERFACE-ID>MyServiceInterface</SERVICE-INTERFACE-ID>",
        )
        assert instance.getShortName() == "ConsumedInstance1"
        assert instance.getDdsServiceQosProfileRef().getValue() == "/DdsCpConfig/QosProfiles/Profile1"
        assert instance.getServiceInstanceId().getValue() == 42
        assert instance.getServiceInterfaceId().getValue() == "MyServiceInterface"

    def test_minor_version_is_any_version_string(self, parser):
        """Test that MINOR-VERSION materializes an AnyVersionString (PDF type, Rule 0001.3)."""
        instance = self._read(parser, "<MINOR-VERSION>2</MINOR-VERSION>")
        assert isinstance(instance.getMinorVersion(), AnyVersionString)
        assert instance.getMinorVersion().getValue() == "2"
