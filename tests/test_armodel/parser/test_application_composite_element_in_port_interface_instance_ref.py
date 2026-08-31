"""
Tests for parsing APPLICATION-COMPOSITE-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF — Table D.17 (p.953, R23-11).

XML element order (xml.sequenceOffset): ROOT(15) → CONTEXT(20) → TARGET(30); base has no XML element.

Round-trip counterpart: tests/test_armodel/writer/test_application_composite_element_in_port_interface_instance_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


class TestGetApplicationCompositeElementInPortInterfaceInstanceRef:
    """
    Test getApplicationCompositeElementInPortInterfaceInstanceRef (Table D.17).
    """

    def test_read_field_values(self, parser):
        """
        Test that all ref fields (root, multiple contexts, target) are populated
        in order with DEST attributes.
        """
        element = ET.fromstring(
            f"""<PARENT xmlns='{NS}'>
                <LEAF-ELEMENT-IREF>
                    <ROOT-DATA-PROTOTYPE-REF DEST='AUTOSAR-DATA-PROTOTYPE'>/pkg/root</ROOT-DATA-PROTOTYPE-REF>
                    <CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE'>/pkg/ctx1</CONTEXT-DATA-PROTOTYPE-REF>
                    <CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE'>/pkg/ctx2</CONTEXT-DATA-PROTOTYPE-REF>
                    <TARGET-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE'>/pkg/target</TARGET-DATA-PROTOTYPE-REF>
                </LEAF-ELEMENT-IREF>
            </PARENT>"""
        )

        iref = parser.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")

        assert iref is not None
        assert iref.getRootDataPrototypeRef().getValue() == "/pkg/root"
        assert iref.getRootDataPrototypeRef().getDest() == "AUTOSAR-DATA-PROTOTYPE"

        ctx_refs = iref.getContextDataPrototypeRefs()
        assert len(ctx_refs) == 2
        assert ctx_refs[0].getValue() == "/pkg/ctx1"
        assert ctx_refs[0].getDest() == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"
        assert ctx_refs[1].getValue() == "/pkg/ctx2"

        assert iref.getTargetDataPrototypeRef().getValue() == "/pkg/target"
        assert iref.getTargetDataPrototypeRef().getDest() == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"

    def test_read_empty(self, parser):
        """
        Test that a missing LEAF-ELEMENT-IREF returns None.
        """
        element = ET.fromstring(f"<PARENT xmlns='{NS}'></PARENT>")

        iref = parser.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")

        assert iref is None

    def test_read_present_without_refs(self, parser):
        """
        Test that an empty LEAF-ELEMENT-IREF yields an iref with empty fields.
        """
        element = ET.fromstring(f"<PARENT xmlns='{NS}'><LEAF-ELEMENT-IREF></LEAF-ELEMENT-IREF></PARENT>")

        iref = parser.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")

        assert iref is not None
        assert iref.getRootDataPrototypeRef() is None
        assert iref.getContextDataPrototypeRefs() == []
        assert iref.getTargetDataPrototypeRef() is None
