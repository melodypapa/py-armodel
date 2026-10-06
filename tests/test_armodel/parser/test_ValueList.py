"""Reader tests for ValueList (Swc TPS Table 5.127, p.459).

XSD group VALUE-LIST: an unbounded choice of VF (ordered, `*`) and V (0..1,
offset 30). VF is typed NUMERICAL-VALUE-VARIATION-POINT (mixed content) — the
value is the ELEMENT TEXT, never a nested V child.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


def _wrap(content: str) -> ET.Element:
    return ET.fromstring('<PARENT xmlns="%s"><SW-ARRAYSIZE>%s</SW-ARRAYSIZE></PARENT>' % (NS, content))


def test_read_v_and_vf_text_entries(parser):
    element = _wrap("<VF>1.5</VF><VF>2.5</VF><V>4</V>")
    value_list = parser.getValueList(element, "SW-ARRAYSIZE")
    assert value_list is not None
    assert float(value_list.getV().getValue()) == 4.0
    assert [float(vf.getValue()) for vf in value_list.getVfs()] == [1.5, 2.5]


def test_read_empty(parser):
    value_list = parser.getValueList(_wrap(""), "SW-ARRAYSIZE")
    assert value_list is not None
    assert value_list.getV() is None
    assert value_list.getVfs() == []


def test_read_missing_returns_none(parser):
    element = ET.fromstring('<PARENT xmlns="%s"/>' % NS)
    assert parser.getValueList(element, "SW-ARRAYSIZE") is None
