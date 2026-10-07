"""
Tests for reading DDS-CP-PROVIDED-SERVICE-INSTANCE elements — DdsCpProvidedServiceInstance, Table 6.153 (p.473, R23-11).

The class is a nested non-top-level element (aggregated by the still-unsynced
ServiceInstanceCollectionSet.serviceInstance under the unsynced DdsCpServiceInstance branch),
so the reusable helper readDdsCpProvidedServiceInstance is exercised directly on a
standalone XML subtree (XSD complexType DDS-CP-PROVIDED-SERVICE-INSTANCE,
AUTOSAR_00052.xsd l.28944: AR-OBJECT attributeGroup — S/T round-trip; group members in
xml.sequenceOffset order LOCAL-UNICAST-ADDRESSES, MINOR-VERSION, PROVIDED-DDS-OPERATIONS,
PROVIDED-DDS-SERVICE-INSTANCE-EVENTS, STATIC-REMOTE-MULTICAST-ADDRESSES,
STATIC-REMOTE-UNICAST-ADDRESSES).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_provided_service_instance.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    DdsCpProvidedServiceInstance,
    DdsCpServiceInstanceEvent,
    DdsCpServiceInstanceOperation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-PROVIDED-SERVICE-INSTANCE xmlns='{NS}'>{inner}</DDS-CP-PROVIDED-SERVICE-INSTANCE>")


class TestReadDdsCpProvidedServiceInstance:
    """Tests for readDdsCpProvidedServiceInstance — own group field values (Table 6.153)."""

    def _read(self, parser, inner):
        instance = DdsCpProvidedServiceInstance()
        parser.readDdsCpProvidedServiceInstance(_snip(inner), instance)
        return instance

    def test_read_sets_all_fields(self, parser):
        """Test that the wrapper refs, minor version and aggregated children are read with their values."""
        instance = self._read(
            parser,
            "<LOCAL-UNICAST-ADDRESSES>"
            '<APPLICATION-ENDPOINT-REF-CONDITIONAL><APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/Cluster/Eps/LocalEp</APPLICATION-ENDPOINT-REF></APPLICATION-ENDPOINT-REF-CONDITIONAL>'
            "</LOCAL-UNICAST-ADDRESSES>"
            "<MINOR-VERSION>4</MINOR-VERSION>"
            "<PROVIDED-DDS-OPERATIONS>"
            '<DDS-CP-SERVICE-INSTANCE-OPERATION><DDS-OPERATION-REQUEST-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/Triggers/Req</DDS-OPERATION-REQUEST-TRIGGERING-REF></DDS-CP-SERVICE-INSTANCE-OPERATION>'
            "</PROVIDED-DDS-OPERATIONS>"
            "<PROVIDED-DDS-SERVICE-INSTANCE-EVENTS>"
            '<DDS-CP-SERVICE-INSTANCE-EVENT><DDS-EVENT-REF DEST="PDU-TRIGGERING">/Fibex/Triggers/Evt</DDS-EVENT-REF></DDS-CP-SERVICE-INSTANCE-EVENT>'
            "</PROVIDED-DDS-SERVICE-INSTANCE-EVENTS>"
            "<STATIC-REMOTE-MULTICAST-ADDRESSES>"
            '<APPLICATION-ENDPOINT-REF-CONDITIONAL><APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/Cluster/Eps/MulticastEp</APPLICATION-ENDPOINT-REF></APPLICATION-ENDPOINT-REF-CONDITIONAL>'
            "</STATIC-REMOTE-MULTICAST-ADDRESSES>"
            "<STATIC-REMOTE-UNICAST-ADDRESSES>"
            '<APPLICATION-ENDPOINT-REF-CONDITIONAL><APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/Cluster/Eps/UnicastEp1</APPLICATION-ENDPOINT-REF></APPLICATION-ENDPOINT-REF-CONDITIONAL>'
            '<APPLICATION-ENDPOINT-REF-CONDITIONAL><APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/Cluster/Eps/UnicastEp2</APPLICATION-ENDPOINT-REF></APPLICATION-ENDPOINT-REF-CONDITIONAL>'
            "</STATIC-REMOTE-UNICAST-ADDRESSES>",
        )
        assert instance.getLocalUnicastAddressRef() is not None
        assert instance.getLocalUnicastAddressRef().getValue() == "/Cluster/Eps/LocalEp"
        assert instance.getLocalUnicastAddressRef().getDest() == "APPLICATION-ENDPOINT"
        assert instance.getMinorVersion() is not None
        assert instance.getMinorVersion().getValue() == 4
        operations = instance.getProvidedDdsOperations()
        assert len(operations) == 1
        assert isinstance(operations[0], DdsCpServiceInstanceOperation)
        assert operations[0].getDdsOperationRequestTriggeringRef().getValue() == "/Fibex/Triggers/Req"
        events = instance.getProvidedDdsServiceInstanceEvents()
        assert len(events) == 1
        assert isinstance(events[0], DdsCpServiceInstanceEvent)
        assert events[0].getDdsEventRef().getValue() == "/Fibex/Triggers/Evt"
        assert instance.getStaticRemoteMulticastAddressRef() is not None
        assert instance.getStaticRemoteMulticastAddressRef().getValue() == "/Cluster/Eps/MulticastEp"
        unicast_refs = instance.getStaticRemoteUnicastAddressRefs()
        assert len(unicast_refs) == 2
        assert unicast_refs[0].getValue() == "/Cluster/Eps/UnicastEp1"
        assert unicast_refs[1].getValue() == "/Cluster/Eps/UnicastEp2"

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None/empty."""
        instance = self._read(parser, "")
        assert instance.getLocalUnicastAddressRef() is None
        assert instance.getMinorVersion() is None
        assert instance.getProvidedDdsOperations() == []
        assert instance.getProvidedDdsServiceInstanceEvents() == []
        assert instance.getStaticRemoteMulticastAddressRef() is None
        assert instance.getStaticRemoteUnicastAddressRefs() == []

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<DDS-CP-PROVIDED-SERVICE-INSTANCE xmlns='%s' S='42' T='2025-05-05T00:00:00Z'/>" % NS)
        instance = DdsCpProvidedServiceInstance()
        parser.readDdsCpProvidedServiceInstance(element, instance)
        assert instance.getChecksum() is not None
        assert instance.getChecksum().getValue() == "42"
        assert instance.getTimestamp() is not None
        assert instance.getTimestamp().getValue() == "2025-05-05T00:00:00Z"

    def test_minor_version_is_positive_integer(self, parser):
        """Test that MINOR-VERSION materializes a PositiveInteger (PDF type, Rule 0001.3)."""
        instance = self._read(parser, "<MINOR-VERSION>10</MINOR-VERSION>")
        assert isinstance(instance.getMinorVersion(), PositiveInteger)
        assert instance.getMinorVersion().getValue() == 10
