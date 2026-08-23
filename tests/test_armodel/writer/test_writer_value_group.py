"""Writer round-trip tests for ValueGroup (Table 5.126)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValues, ValueGroup
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _build_value_group():
    vg = ValueGroup()
    label = MultilanguageLongName()
    l4 = LLongName()
    l4.setValue("group label")
    l4.setL("FOR-ALL")
    label.addL4(l4)
    vg.setLabel(label)

    contents = SwValues()
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat

    contents.addV(ARFloat().setValue(1.5))
    contents.addV(ARFloat().setValue(2.5))
    vg.setVgContents(contents)
    return vg


def test_write_value_group_full(writer):
    parent = _parent()
    writer.setValueGroup(parent, "VG", _build_value_group())

    vg_element = parent.find("VG")
    assert vg_element is not None

    label = vg_element.find("LABEL")
    assert label is not None
    l4 = label.find("L-4")
    assert l4 is not None
    assert l4.text == "group label"
    assert l4.get("L") == "FOR-ALL"

    vs = vg_element.findall("V")
    assert len(vs) == 2
    assert float(vs[0].text) == 1.5
    assert float(vs[1].text) == 2.5


def test_write_value_group_empty(writer):
    parent = _parent()
    writer.setValueGroup(parent, "VG", ValueGroup())

    vg_element = parent.find("VG")
    assert vg_element is not None
    assert vg_element.find("LABEL") is None
    assert vg_element.findall("V") == []


def test_write_value_group_none_is_noop(writer):
    parent = _parent()
    writer.setValueGroup(parent, "VG", None)
    assert parent.find("VG") is None


def test_write_sw_values_with_nested_vg_round_trip(writer):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat
    from armodel.parser.arxml_parser import ARXMLParser

    sw_values = SwValues()
    sw_values.addV(ARFloat().setValue(0.0))
    sw_values.setVg(_build_value_group())

    parent = _parent()
    writer.setSwValues(parent, "SW-VALUES-PHYS", sw_values)

    NS = "http://autosar.org/schema/r4.0"
    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getSwValues(reparsed, "SW-VALUES-PHYS")
    assert reloaded is not None
    assert len(reloaded.getVs()) == 1

    vg = reloaded.getVg()
    assert vg is not None
    assert vg.getLabel() is not None
    assert vg.getLabel().getL4s()[0].getValue() == "group label"
    assert len(vg.getVgContents().getVs()) == 2
