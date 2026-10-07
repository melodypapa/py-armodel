"""
Writer tests for DDS-OWNERSHIP elements — DdsOwnership, Table 6.187 (p.532, R23-11).

writeDdsOwnership emits <OWNERSHIP> (the object element, per the DdsCpQosProfile.ownership
aggregation) with the AR-OBJECT S/T attributes and the OWNERSHIP-KIND member (XSD group
DDS-OWNERSHIP, AUTOSAR_00052.xsd l.29836; facet spelling per DDS-OWNERSHIP-KIND-ENUM--SIMPLE).

Round-trip counterpart: tests/test_armodel/parser/test_dds_ownership.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsOwnership
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, DdsOwnershipKindEnum, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_ownership() -> DdsOwnership:
    ownership = DdsOwnership()
    ownership.setOwnershipKind(DdsOwnershipKindEnum().setValue(DdsOwnershipKindEnum.EXCLUSIVE))
    ownership.setChecksum(String().setValue("5"))
    ownership.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return ownership


class TestWriteDdsOwnership:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the OWNERSHIP-KIND facet."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnership(parent, _new_ownership())
        node = parent.find("OWNERSHIP")
        assert node is not None
        assert node.find("OWNERSHIP-KIND").text == "EXCLUSIVE"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnership(parent, _new_ownership())
        node = parent.find("OWNERSHIP")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_member(self):
        """Test that an empty object emits no member element."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnership(parent, DdsOwnership())
        node = parent.find("OWNERSHIP")
        assert node is not None
        assert node.find("OWNERSHIP-KIND") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnership(parent, _new_ownership())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsOwnership()
        ARXMLParser().readDdsOwnership(root.find("{%s}OWNERSHIP" % NS), reloaded)
        assert reloaded.getOwnershipKind() is not None
        assert reloaded.getOwnershipKind().getValue() == DdsOwnershipKindEnum.EXCLUSIVE
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
