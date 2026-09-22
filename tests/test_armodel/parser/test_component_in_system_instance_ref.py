"""
Reader tests for COMPONENT-IN-SYSTEM-INSTANCE-REF — Table B.1 (p.1000, R23-11).

The class is a nested value type (no ARPackage dispatch), so the reader helper
getComponentInSystemInstanceRef is exercised directly on XML fragments.

Writer counterpart: tests/test_armodel/writer/test_component_in_system_instance_ref.py
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
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "PARENT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestGetComponentInSystemInstanceRef:
    def test_full(self, parser):
        element = _snip(
            "<COMPONENT-IREF>"
            "<BASE-REF DEST='COMPOSITION-SW-COMPONENT-TYPE'>/b</BASE-REF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/comp</CONTEXT-COMPOSITION-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c1</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c2</CONTEXT-COMPONENT-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/t</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>"
        )
        iref = parser.getComponentInSystemInstanceRef(parser.find(element, "COMPONENT-IREF"))

        assert iref is not None
        assert iref.getBaseRef().getValue() == "/b"
        assert iref.getBaseRef().getDest() == "COMPOSITION-SW-COMPONENT-TYPE"
        assert iref.getContextCompositionRef().getValue() == "/comp"
        assert iref.getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        ctx = iref.getContextComponentRefs()
        assert [r.getValue() for r in ctx] == ["/c1", "/c2"]
        assert all(r.getDest() == "SW-COMPONENT-PROTOTYPE" for r in ctx)
        assert iref.getTargetComponentRef().getValue() == "/t"
        assert iref.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"

    def test_empty(self, parser):
        element = _snip("<COMPONENT-IREF>" "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/t</TARGET-COMPONENT-REF>" "</COMPONENT-IREF>")
        iref = parser.getComponentInSystemInstanceRef(parser.find(element, "COMPONENT-IREF"))

        assert iref is not None
        assert iref.getBaseRef() is None
        assert iref.getContextCompositionRef() is None
        assert iref.getContextComponentRefs() == []
        assert iref.getTargetComponentRef().getValue() == "/t"

    def test_none_element(self, parser):
        assert parser.getComponentInSystemInstanceRef(None) is None
