"""Writer round-trip tests for ValueList (Swc TPS Table 5.127, p.459).

XSD group VALUE-LIST: an unbounded choice of VF (ordered, `*`) and V (0..1,
offset 30). VF is typed NUMERICAL-VALUE-VARIATION-POINT (mixed content) — the
value is the ELEMENT TEXT; a nested V child inside VF is schema-invalid. The
save-reload round-trip goes through the ConstantSpecification VALUE-SPEC
dispatch so the bundled-XSD validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
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


def _build_value_list() -> ValueList:
    value_list = ValueList()
    value_list.addVf(Numerical().setValue("1.5"))
    value_list.addVf(Numerical().setValue("2.5"))
    value_list.setV(Numerical().setValue("4"))
    return value_list


def test_write_value_list_with_v(writer):
    parent = _parent()
    value_list = ValueList()
    value_list.setV(Numerical().setValue("4"))

    writer.setValueList(parent, "SW-ARRAYSIZE", value_list)

    element = parent.find("SW-ARRAYSIZE")
    assert element is not None
    assert float(element.find("V").text) == 4.0
    assert element.find("VF") is None


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
    assert [vf.text for vf in vfs] == ["1.5", "2.5"]
    assert [vf.find("V") for vf in vfs] == [None, None]


def test_write_element_order_matches_xsd_group(writer):
    parent = _parent()
    writer.setValueList(parent, "SW-ARRAYSIZE", _build_value_list())

    element = parent.find("SW-ARRAYSIZE")
    assert element is not None
    tags = [child.tag for child in element]
    assert tags == ["VF", "VF", "V"]
    assert element.find("V").text == "4"


def test_write_unset_fields_omit_elements(writer):
    parent = _parent()
    writer.setValueList(parent, "SW-ARRAYSIZE", ValueList())

    element = parent.find("SW-ARRAYSIZE")
    assert element is not None
    assert len(list(element)) == 0


def test_write_none_is_noop(writer):
    parent = _parent()
    writer.setValueList(parent, "SW-ARRAYSIZE", None)
    assert parent.find("SW-ARRAYSIZE") is None


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


class TestValueListRoundTrip:
    def test_round_trip_through_save(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")
        spec = ApplicationValueSpecification()
        cont = SwValueCont()
        cont.setSwArraysize(_build_value_list())
        spec.setSwValueCont(cont)
        constant.setValueSpec(spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            value_list = constant2.getValueSpec().getSwValueCont().getSwArraysize()
            assert value_list is not None
            assert float(value_list.getV().getValue()) == 4.0
            assert [float(vf.getValue()) for vf in value_list.getVfs()] == [1.5, 2.5]
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
