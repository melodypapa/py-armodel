"""
Tests for writing APPLICATION-COMPOSITE-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF — Table D.17 (p.953, R23-11).

XML element order (xml.sequenceOffset): ROOT(15) → CONTEXT(20) → TARGET(30); base has no XML element.

Round-trip counterpart: tests/test_armodel/parser/test_application_composite_element_in_port_interface_instance_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (
    ApplicationCompositeElementInPortInterfaceInstanceRef,
)
from armodel.writer.arxml_writer import ARXMLWriter


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


class TestSetApplicationCompositeElementInPortInterfaceInstanceRef:
    """
    Test setApplicationCompositeElementInPortInterfaceInstanceRef (Table D.17).
    """

    def test_write_field_values(self, writer):
        """
        Test that all ref fields are written in sequenceOffset order:
        ROOT(15) → CONTEXT(20, unbounded) → TARGET(30).
        """
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        iref.setRootDataPrototypeRef(_ref("/pkg/root", "AUTOSAR-DATA-PROTOTYPE"))
        iref.addContextDataPrototypeRef(_ref("/pkg/ctx1", "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"))
        iref.addContextDataPrototypeRef(_ref("/pkg/ctx2", "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(_ref("/pkg/target", "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"))

        element = ET.Element("PARENT")
        writer.setApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF", iref)

        iref_tag = element.find("LEAF-ELEMENT-IREF")
        assert iref_tag is not None

        children = list(iref_tag)
        assert [child.tag for child in children] == [
            "ROOT-DATA-PROTOTYPE-REF",
            "CONTEXT-DATA-PROTOTYPE-REF",
            "CONTEXT-DATA-PROTOTYPE-REF",
            "TARGET-DATA-PROTOTYPE-REF",
        ]

        root_tag = iref_tag.find("ROOT-DATA-PROTOTYPE-REF")
        assert root_tag.text == "/pkg/root"
        assert root_tag.attrib["DEST"] == "AUTOSAR-DATA-PROTOTYPE"

        ctx_tags = iref_tag.findall("CONTEXT-DATA-PROTOTYPE-REF")
        assert len(ctx_tags) == 2
        assert ctx_tags[0].text == "/pkg/ctx1"
        assert ctx_tags[0].attrib["DEST"] == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"
        assert ctx_tags[1].text == "/pkg/ctx2"

        target_tag = iref_tag.find("TARGET-DATA-PROTOTYPE-REF")
        assert target_tag.text == "/pkg/target"

    def test_write_none(self, writer):
        """
        Test that a None iref writes no element.
        """
        element = ET.Element("PARENT")

        writer.setApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF", None)

        assert element.find("LEAF-ELEMENT-IREF") is None

    def test_write_empty_iref(self, writer):
        """
        Test that an iref without refs writes an empty wrapper element.
        """
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()

        element = ET.Element("PARENT")
        writer.setApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF", iref)

        iref_tag = element.find("LEAF-ELEMENT-IREF")
        assert iref_tag is not None
        assert len(list(iref_tag)) == 0
