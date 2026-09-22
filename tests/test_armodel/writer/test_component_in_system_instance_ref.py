"""
Writer tests for COMPONENT-IN-SYSTEM-INSTANCE-REF — Table B.1 (p.1000, R23-11).

XML element order (xml.sequenceOffset): BASE-REF(10) → CONTEXT-COMPOSITION-REF(20) →
CONTEXT-COMPONENT-REF(30, unbounded) → TARGET-COMPONENT-REF(40).

Round-trip counterpart: tests/test_armodel/parser/test_component_in_system_instance_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestSetComponentInSystemInstanceRef:
    def test_write_field_values(self, writer):
        """All refs written in the sequenceOffset order of Table B.1."""
        iref = ComponentInSystemInstanceRef()
        iref.setBaseRef(_ref("/b", "COMPOSITION-SW-COMPONENT-TYPE"))
        iref.setContextCompositionRef(_ref("/comp", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.addContextComponentRef(_ref("/c1", "SW-COMPONENT-PROTOTYPE"))
        iref.addContextComponentRef(_ref("/c2", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetComponentRef(_ref("/t", "SW-COMPONENT-PROTOTYPE"))

        parent = ET.Element("PARENT")
        writer.setComponentInSystemInstanceRef(parent, "COMPONENT-IREF", iref)

        iref_tag = parent.find("COMPONENT-IREF")
        assert iref_tag is not None
        assert [child.tag for child in iref_tag] == [
            "BASE-REF",
            "CONTEXT-COMPOSITION-REF",
            "CONTEXT-COMPONENT-REF",
            "CONTEXT-COMPONENT-REF",
            "TARGET-COMPONENT-REF",
        ]

        base_tag = iref_tag.find("BASE-REF")
        assert base_tag.text == "/b"
        assert base_tag.attrib["DEST"] == "COMPOSITION-SW-COMPONENT-TYPE"

        assert iref_tag.find("CONTEXT-COMPOSITION-REF").text == "/comp"
        assert iref_tag.find("CONTEXT-COMPOSITION-REF").attrib["DEST"] == "ROOT-SW-COMPOSITION-PROTOTYPE"

        ctx_tags = iref_tag.findall("CONTEXT-COMPONENT-REF")
        assert [r.text for r in ctx_tags] == ["/c1", "/c2"]
        assert all(r.attrib["DEST"] == "SW-COMPONENT-PROTOTYPE" for r in ctx_tags)

        target_tag = iref_tag.find("TARGET-COMPONENT-REF")
        assert target_tag.text == "/t"
        assert target_tag.attrib["DEST"] == "SW-COMPONENT-PROTOTYPE"

    def test_write_none(self, writer):
        """A None iref writes no element."""
        parent = ET.Element("PARENT")
        writer.setComponentInSystemInstanceRef(parent, "COMPONENT-IREF", None)

        assert parent.find("COMPONENT-IREF") is None

    def test_write_empty_iref(self, writer):
        """An iref without refs writes an empty wrapper element."""
        iref = ComponentInSystemInstanceRef()

        parent = ET.Element("PARENT")
        writer.setComponentInSystemInstanceRef(parent, "COMPONENT-IREF", iref)

        iref_tag = parent.find("COMPONENT-IREF")
        assert iref_tag is not None
        assert len(list(iref_tag)) == 0

    def test_round_trip(self, writer):
        """write -> re-parse -> read yields the same field values."""
        iref = ComponentInSystemInstanceRef()
        iref.setBaseRef(_ref("/b", "COMPOSITION-SW-COMPONENT-TYPE"))
        iref.setContextCompositionRef(_ref("/comp", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.addContextComponentRef(_ref("/c1", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetComponentRef(_ref("/t", "SW-COMPONENT-PROTOTYPE"))

        parent = ET.Element("PARENT")
        writer.setComponentInSystemInstanceRef(parent, "COMPONENT-IREF", iref)

        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parser = ARXMLParser()
        iref2 = parser.getComponentInSystemInstanceRef(reparsed[0])

        assert iref2 is not None
        assert iref2.getBaseRef().getValue() == "/b"
        assert iref2.getBaseRef().getDest() == "COMPOSITION-SW-COMPONENT-TYPE"
        assert iref2.getContextCompositionRef().getValue() == "/comp"
        assert [r.getValue() for r in iref2.getContextComponentRefs()] == ["/c1"]
        assert iref2.getTargetComponentRef().getValue() == "/t"
        assert iref2.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
