"""
Writer tests for VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF — Table B.3 (p.1004, R23-11).

XML element order: Table B.3 sets no xml.sequenceOffset ("the properties are serialized
in an alphabetical order") - BASE-REF, CONTEXT-COMPONENT-REF*, CONTEXT-COMPOSITION-REF,
CONTEXT-PORT-REF, TARGET-DATA-PROTOTYPE-REF.

Round-trip counterpart: tests/test_armodel/parser/test_variable_data_prototype_in_system_instance_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
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


class TestSetVariableDataPrototypeInSystemInstanceRef:
    def test_write_field_values(self, writer):
        """All refs written in the alphabetical order of Table B.3."""
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.setBaseRef(_ref("/b", "COMPOSITION-SW-COMPONENT-TYPE"))
        iref.addContextComponentRef(_ref("/c1", "SW-COMPONENT-PROTOTYPE"))
        iref.addContextComponentRef(_ref("/c2", "SW-COMPONENT-PROTOTYPE"))
        iref.setContextCompositionRef(_ref("/comp", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.setContextPortRef(_ref("/port", "PORT-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(_ref("/vdp", "VARIABLE-DATA-PROTOTYPE"))

        parent = ET.Element("PARENT")
        writer.setVariableDataPrototypeInSystemInstanceRef(parent, "SENDER-IREF", iref)

        iref_tag = parent.find("SENDER-IREF")
        assert iref_tag is not None
        assert [child.tag for child in iref_tag] == [
            "BASE-REF",
            "CONTEXT-COMPONENT-REF",
            "CONTEXT-COMPONENT-REF",
            "CONTEXT-COMPOSITION-REF",
            "CONTEXT-PORT-REF",
            "TARGET-DATA-PROTOTYPE-REF",
        ]

        base_tag = iref_tag.find("BASE-REF")
        assert base_tag.text == "/b"
        assert base_tag.attrib["DEST"] == "COMPOSITION-SW-COMPONENT-TYPE"

        ctx_tags = iref_tag.findall("CONTEXT-COMPONENT-REF")
        assert [r.text for r in ctx_tags] == ["/c1", "/c2"]
        assert all(r.attrib["DEST"] == "SW-COMPONENT-PROTOTYPE" for r in ctx_tags)

        assert iref_tag.find("CONTEXT-COMPOSITION-REF").text == "/comp"
        assert iref_tag.find("CONTEXT-COMPOSITION-REF").attrib["DEST"] == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert iref_tag.find("CONTEXT-PORT-REF").text == "/port"
        assert iref_tag.find("CONTEXT-PORT-REF").attrib["DEST"] == "PORT-PROTOTYPE"
        assert iref_tag.find("TARGET-DATA-PROTOTYPE-REF").text == "/vdp"
        assert iref_tag.find("TARGET-DATA-PROTOTYPE-REF").attrib["DEST"] == "VARIABLE-DATA-PROTOTYPE"

    def test_write_none(self, writer):
        """A None iref writes no element."""
        parent = ET.Element("PARENT")
        writer.setVariableDataPrototypeInSystemInstanceRef(parent, "SENDER-IREF", None)

        assert parent.find("SENDER-IREF") is None

    def test_write_empty_iref(self, writer):
        """An iref without refs writes an empty wrapper element."""
        iref = VariableDataPrototypeInSystemInstanceRef()

        parent = ET.Element("PARENT")
        writer.setVariableDataPrototypeInSystemInstanceRef(parent, "RECEIVER-IREF", iref)

        iref_tag = parent.find("RECEIVER-IREF")
        assert iref_tag is not None
        assert len(list(iref_tag)) == 0

    def test_round_trip(self, writer):
        """write -> re-parse -> read yields the same field values."""
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.setBaseRef(_ref("/b", "COMPOSITION-SW-COMPONENT-TYPE"))
        iref.addContextComponentRef(_ref("/c1", "SW-COMPONENT-PROTOTYPE"))
        iref.setContextCompositionRef(_ref("/comp", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.setContextPortRef(_ref("/port", "PORT-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(_ref("/vdp", "VARIABLE-DATA-PROTOTYPE"))

        parent = ET.Element("PARENT")
        writer.setVariableDataPrototypeInSystemInstanceRef(parent, "SENDER-IREF", iref)

        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parser = ARXMLParser()
        iref2 = parser.getVariableDataPrototypeInSystemInstanceRef(reparsed[0])

        assert iref2 is not None
        assert iref2.getBaseRef().getValue() == "/b"
        assert iref2.getBaseRef().getDest() == "COMPOSITION-SW-COMPONENT-TYPE"
        assert [r.getValue() for r in iref2.getContextComponentRefs()] == ["/c1"]
        assert iref2.getContextCompositionRef().getValue() == "/comp"
        assert iref2.getContextPortRef().getValue() == "/port"
        assert iref2.getTargetDataPrototypeRef().getValue() == "/vdp"
        assert iref2.getTargetDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
