"""
Tests for reading DDS-CP-SERVICE-INSTANCE-OPERATION elements — DdsCpServiceInstanceOperation, Table 6.156 (p.476, R23-11).

The class is a nested non-top-level element (aggregated by the still-unsynced
DdsCpConsumedServiceInstance.consumedDdsOperation / DdsCpProvidedServiceInstance.providedDdsOperation),
so the reusable helper readDdsCpServiceInstanceOperation is exercised directly on a
standalone XML subtree (XSD complexType DDS-CP-SERVICE-INSTANCE-OPERATION, AUTOSAR_00052.xsd
l.29282: AR-OBJECT group + attributeGroup — S/T round-trip; group members
DDS-OPERATION-REQUEST-TRIGGERING-REF, DDS-OPERATION-RESPONSE-TRIGGERING-REF,
VARIATION-POINT last per xml.sequenceOffset=10000).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_service_instance_operation.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsCpServiceInstanceOperation

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-SERVICE-INSTANCE-OPERATION xmlns='{NS}'>{inner}</DDS-CP-SERVICE-INSTANCE-OPERATION>")


class TestReadDdsCpServiceInstanceOperation:
    """Tests for readDdsCpServiceInstanceOperation — own group field values (Table 6.156)."""

    def _read(self, parser, inner):
        operation = DdsCpServiceInstanceOperation()
        parser.readDdsCpServiceInstanceOperation(_snip(inner), operation)
        return operation

    def test_read_sets_all_refs(self, parser):
        """Test that both triggering refs are read with their DEST and value."""
        operation = self._read(
            parser,
            '<DDS-OPERATION-REQUEST-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/Ecu1/PduTriggerings/Req</DDS-OPERATION-REQUEST-TRIGGERING-REF>'
            '<DDS-OPERATION-RESPONSE-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/Ecu1/PduTriggerings/Resp</DDS-OPERATION-RESPONSE-TRIGGERING-REF>',
        )
        assert operation.getDdsOperationRequestTriggeringRef() is not None
        assert operation.getDdsOperationRequestTriggeringRef().getDest() == "PDU-TRIGGERING"
        assert operation.getDdsOperationRequestTriggeringRef().getValue() == "/Fibex/Ecu1/PduTriggerings/Req"
        assert operation.getDdsOperationResponseTriggeringRef() is not None
        assert operation.getDdsOperationResponseTriggeringRef().getDest() == "PDU-TRIGGERING"
        assert operation.getDdsOperationResponseTriggeringRef().getValue() == "/Fibex/Ecu1/PduTriggerings/Resp"

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        operation = self._read(parser, "")
        assert operation.getDdsOperationRequestTriggeringRef() is None
        assert operation.getDdsOperationResponseTriggeringRef() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<DDS-CP-SERVICE-INSTANCE-OPERATION xmlns='%s' S='100' T='2024-01-01T00:00:00Z'/>" % NS)
        operation = DdsCpServiceInstanceOperation()
        parser.readDdsCpServiceInstanceOperation(element, operation)
        assert operation.getChecksum() is not None
        assert operation.getChecksum().getValue() == "100"
        assert operation.getTimestamp() is not None
        assert operation.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_read_variation_point(self, parser):
        """Test that a trailing VARIATION-POINT (sequenceOffset=10000) is read via the VP mixin."""
        operation = self._read(
            parser,
            '<DDS-OPERATION-REQUEST-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/Ecu1/PduTriggerings/Req</DDS-OPERATION-REQUEST-TRIGGERING-REF>'
            "<VARIATION-POINT><SHORT-LABEL>vp1</SHORT-LABEL></VARIATION-POINT>",
        )
        assert operation.getVariationPoint() is not None
        assert operation.getVariationPoint().getShortLabel() is not None
        assert operation.getVariationPoint().getShortLabel().getValue() == "vp1"
