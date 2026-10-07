"""
Writer tests for DDS-CP-SERVICE-INSTANCE-OPERATION elements — DdsCpServiceInstanceOperation, Table 6.156 (p.476, R23-11).

writeDdsCpServiceInstanceOperation emits <DDS-CP-SERVICE-INSTANCE-OPERATION> with the
group members in XSD sequenceOffset order (DDS-OPERATION-REQUEST-TRIGGERING-REF,
DDS-OPERATION-RESPONSE-TRIGGERING-REF, VARIATION-POINT last) plus the AR-OBJECT
S/T attributes (AUTOSAR_00052.xsd l.29282).

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_service_instance_operation.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsCpServiceInstanceOperation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_operation() -> DdsCpServiceInstanceOperation:
    operation = DdsCpServiceInstanceOperation()
    operation.setDdsOperationRequestTriggeringRef(RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Ecu1/PduTriggerings/Req"))
    operation.setDdsOperationResponseTriggeringRef(RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Ecu1/PduTriggerings/Resp"))
    operation.setChecksum(String().setValue("100"))
    operation.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    return operation


class TestWriteDdsCpServiceInstanceOperation:
    def test_write_emits_element_and_refs(self):
        """Test that the writer emits the element with both refs in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceOperation(parent, _new_operation())
        node = parent.find("DDS-CP-SERVICE-INSTANCE-OPERATION")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["DDS-OPERATION-REQUEST-TRIGGERING-REF", "DDS-OPERATION-RESPONSE-TRIGGERING-REF"]
        request = node.find("DDS-OPERATION-REQUEST-TRIGGERING-REF")
        assert request.attrib["DEST"] == "PDU-TRIGGERING"
        assert request.text == "/Fibex/Ecu1/PduTriggerings/Req"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceOperation(parent, _new_operation())
        node = parent.find("DDS-CP-SERVICE-INSTANCE-OPERATION")
        assert node.attrib["S"] == "100"
        assert node.attrib["T"] == "2024-01-01T00:00:00Z"

    def test_write_empty_omits_refs(self):
        """Test that an empty operation emits no ref elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceOperation(parent, DdsCpServiceInstanceOperation())
        node = parent.find("DDS-CP-SERVICE-INSTANCE-OPERATION")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceOperation(parent, _new_operation())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsCpServiceInstanceOperation()
        ARXMLParser().readDdsCpServiceInstanceOperation(root.find("{%s}DDS-CP-SERVICE-INSTANCE-OPERATION" % NS), reloaded)
        assert reloaded.getDdsOperationRequestTriggeringRef().getValue() == "/Fibex/Ecu1/PduTriggerings/Req"
        assert reloaded.getDdsOperationRequestTriggeringRef().getDest() == "PDU-TRIGGERING"
        assert reloaded.getDdsOperationResponseTriggeringRef().getValue() == "/Fibex/Ecu1/PduTriggerings/Resp"
        assert reloaded.getChecksum().getValue() == "100"
        assert reloaded.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_round_trip_variation_point(self):
        """Test that a set variation point round-trips through the VP mixin."""
        operation = _new_operation()
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("vp1"))
        operation.setVariationPoint(variation_point)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceOperation(parent, operation)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        node = root.find("{%s}DDS-CP-SERVICE-INSTANCE-OPERATION" % NS)
        assert node.find("{%s}VARIATION-POINT" % NS) is not None

        reloaded = DdsCpServiceInstanceOperation()
        ARXMLParser().readDdsCpServiceInstanceOperation(node, reloaded)
        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vp1"
