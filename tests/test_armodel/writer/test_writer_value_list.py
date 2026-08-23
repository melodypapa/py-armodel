"""Writer round-trip tests for ValueList (Table 5.127)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _namespaced(element: ET.Element) -> ET.Element:
    xml_text = ET.tostring(element, encoding="unicode")
    return ET.fromstring(xml_text.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))


def test_write_value_list_with_v(writer):
    parent = _parent()
    value_list = ValueList()
    value_list.setV(Numerical().setValue("4"))

    writer.setValueList(parent, "SW-ARRAYSIZE", value_list)

    element = parent.find("SW-ARRAYSIZE")
    assert element is not None
    assert float(element.find("V").text) == 4.0


def test_write_value_list_with_vf_list(writer):
    parent = _parent()
    value_list = ValueList()
    value_list.setV(Numerical().setValue("4"))
    value_list.addVf(Numerical().setValue("1.5"))
    value_list.addVf(Numerical().setValue("2.5"))

    writer.setValueList(parent, "SW-ARRAYSIZE", value_list)

    element = parent.find("SW-ARRAYSIZE")
    assert element is not None
    vfs = element.findall("VF")
    assert len(vfs) == 2
    assert float(vfs[0].find("V").text) == 1.5
    assert float(vfs[1].find("V").text) == 2.5


def test_sw_arraysize_vf_round_trip_preserves_order(writer, parser):
    cont = SwValueCont()
    sw_arraysize = ValueList()
    sw_arraysize.addVf(Numerical().setValue("3.5"))
    sw_arraysize.addVf(Numerical().setValue("1.5"))
    sw_arraysize.addVf(Numerical().setValue("2.5"))
    cont.setSwArraysize(sw_arraysize)

    parent = _parent()
    writer.writeSwValueCont(parent, cont)

    reloaded_cont = parser.getSwValueCont(_namespaced(parent))
    assert reloaded_cont is not None
    reloaded = reloaded_cont.getSwArraysize()
    assert reloaded is not None
    vfs = reloaded.getVfs()
    assert len(vfs) == 3
    assert [float(v.getValue()) for v in vfs] == [3.5, 1.5, 2.5]
