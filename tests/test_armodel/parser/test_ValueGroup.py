"""Reader tests for ValueGroup (Swc TPS Table 5.126, p.459).

XSD group VALUE-GROUP: LABEL (offset 20), then the vgContents SwValues items
inlined (xml.roleElement=false): VF, VT, V, VG, VTF. A nested VG inside the
contents belongs to vgContents.vg (SwValues.vg) and must not be dropped.
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
    return ET.fromstring('<PARENT xmlns="%s"><VG>%s</VG></PARENT>' % (NS, content))


def test_read_label_and_contents(parser):
    element = _wrap('<LABEL><L-4 L="FOR-ALL">group</L-4></LABEL>' "<V>1.5</V><V>2.5</V>")
    value_group = parser.getValueGroup(element, "VG")
    assert value_group is not None
    assert value_group.getLabel() is not None
    assert value_group.getLabel().getL4s()[0].getValue() == "group"
    assert [float(v.getValue()) for v in value_group.getVgContents().getVs()] == [1.5, 2.5]


def test_read_nested_vg_into_contents(parser):
    element = _wrap('<LABEL><L-4 L="FOR-ALL">outer</L-4></LABEL>' "<V>0.0</V>" '<VG><LABEL><L-4 L="FOR-ALL">inner</L-4></LABEL><V>9.5</V></VG>')
    value_group = parser.getValueGroup(element, "VG")
    assert value_group is not None
    contents = value_group.getVgContents()
    assert [float(v.getValue()) for v in contents.getVs()] == [0.0]
    nested = contents.getVg()
    assert nested is not None
    assert nested.getLabel() is not None
    assert nested.getLabel().getL4s()[0].getValue() == "inner"
    assert [float(v.getValue()) for v in nested.getVgContents().getVs()] == [9.5]


def test_read_empty_vg(parser):
    value_group = parser.getValueGroup(_wrap(""), "VG")
    assert value_group is not None
    assert value_group.getLabel() is None
    assert value_group.getVgContents() is None
