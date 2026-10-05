"""Writer round-trip tests for ValueGroup (Swc TPS Table 5.126, p.459).

XSD group VALUE-GROUP: LABEL (offset 20), then the vgContents SwValues items
inlined (xml.roleElement=false) in the SW-VALUES group order: VF(20), VT(30),
V(40), VG(50), VTF(choice). The save-reload round-trip goes through the
ConstantSpecification VALUE-SPEC dispatch so the bundled-XSD validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, VerbatimString
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValues, ValueGroup
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _label(text: str) -> MultilanguageLongName:
    label = MultilanguageLongName()
    l4 = LLongName()
    l4.setValue(text)
    l4.setL("FOR-ALL")
    label.addL4(l4)
    return label


def _build_value_group() -> ValueGroup:
    value_group = ValueGroup()
    value_group.setLabel(_label("group"))
    contents = SwValues()
    contents.addV(Numerical().setValue("1.5"))
    contents.addV(Numerical().setValue("2.5"))
    vt = VerbatimString()
    vt.setValue("a|b")
    contents.setVt(vt)
    value_group.setVgContents(contents)
    return value_group


class TestWriteValueGroup:
    def test_write_element_order_matches_xsd_group(self):
        parent_element = ET.Element("SW-VALUES-PHYS")
        ARXMLWriter().setValueGroup(parent_element, "VG", _build_value_group())

        child_element = parent_element.find("VG")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags.index("LABEL") < tags.index("VT") < tags.index("V")
        assert child_element.find("LABEL").find("L-4").text == "group"
        assert [v.text for v in child_element.findall("V")] == ["1.5", "2.5"]
        assert child_element.find("VT").text == "a|b"

    def test_write_unset_fields_omit_elements(self):
        parent_element = ET.Element("SW-VALUES-PHYS")
        ARXMLWriter().setValueGroup(parent_element, "VG", ValueGroup())

        child_element = parent_element.find("VG")
        assert child_element is not None
        assert len(list(child_element)) == 0

    def test_write_none_is_noop(self):
        parent_element = ET.Element("SW-VALUES-PHYS")
        ARXMLWriter().setValueGroup(parent_element, "VG", None)
        assert parent_element.find("VG") is None


class TestValueGroupRoundTrip:
    def test_round_trip_with_nested_vg(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")

        outer = _build_value_group()
        outer.getVgContents().addV(Numerical().setValue("0.0"))
        nested = ValueGroup()
        nested.setLabel(_label("inner"))
        nested_contents = SwValues()
        nested_contents.addV(Numerical().setValue("9.5"))
        nested.setVgContents(nested_contents)
        outer.getVgContents().setVg(nested)

        spec = ApplicationValueSpecification()
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont

        cont = SwValueCont()
        values = SwValues()
        values.setVg(outer)
        cont.setSwValuesPhys(values)
        spec.setSwValueCont(cont)
        constant.setValueSpec(spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            values2 = constant2.getValueSpec().getSwValueCont().getSwValuesPhys()
            outer2 = values2.getVg()
            assert outer2 is not None
            assert outer2.getLabel().getL4s()[0].getValue() == "group"
            contents2 = outer2.getVgContents()
            assert [float(v.getValue()) for v in contents2.getVs()] == [1.5, 2.5, 0.0]
            assert contents2.getVt().getValue() == "a|b"
            nested2 = contents2.getVg()
            assert nested2 is not None
            assert nested2.getLabel().getL4s()[0].getValue() == "inner"
            assert [float(v.getValue()) for v in nested2.getVgContents().getVs()] == [9.5]
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
