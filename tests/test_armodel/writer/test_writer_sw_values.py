"""Writer round-trip tests for SwValues (Table 5.125)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalOrText
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, VerbatimString
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValues, ValueGroup
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


def _parent():
    return ET.Element("PARENT")


def _build_sw_values():
    sw_values = SwValues()
    sw_values.addV(Numerical().setValue("1.5"))
    sw_values.addV(Numerical().setValue("2.5"))
    sw_values.addVf(Numerical().setValue("0.25"))

    vt = VerbatimString()
    vt.setValue("a|b")
    sw_values.setVt(vt)

    vtf = NumericalOrText()
    vtf.setVf(Numerical().setValue("7"))
    sw_values.addVtf(vtf)
    return sw_values


def test_write_sw_values_full(writer):
    parent = _parent()
    writer.setSwValues(parent, "SW-VALUES-PHYS", _build_sw_values())

    tag = parent.find("SW-VALUES-PHYS")
    assert tag is not None
    vs = tag.findall("V")
    assert [v.text for v in vs] == ["1.5", "2.5"]
    vfs = tag.findall("VF")
    assert [vf.text for vf in vfs] == ["0.25"]
    vt_tag = tag.find("VT")
    assert vt_tag is not None
    assert vt_tag.text == "a|b"
    vtfs = tag.findall("VTF")
    assert len(vtfs) == 1
    assert vtfs[0].find("VF") is not None
    assert vtfs[0].find("VF").text == "7"


def test_write_sw_values_empty(writer):
    parent = _parent()
    writer.setSwValues(parent, "SW-VALUES-PHYS", SwValues())

    tag = parent.find("SW-VALUES-PHYS")
    assert tag is not None
    assert tag.find("V") is None
    assert tag.find("VF") is None
    assert tag.find("VG") is None
    assert tag.find("VT") is None
    assert tag.find("VTF") is None


def test_sw_values_round_trip(writer):
    parent = _parent()
    writer.setSwValues(parent, "SW-VALUES-PHYS", _build_sw_values())

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getSwValues(reparsed, "SW-VALUES-PHYS")
    assert reloaded is not None
    assert [float(v.getValue()) for v in reloaded.getVs()] == [1.5, 2.5]
    assert [float(vf.getValue()) for vf in reloaded.getVfs()] == [0.25]
    assert isinstance(reloaded.getVt(), VerbatimString)
    assert reloaded.getVt().getValue() == "a|b"
    assert reloaded.getVg() is None
    assert len(reloaded.getVtfs()) == 1
    assert float(reloaded.getVtfs()[0].getVf().getValue()) == 7


def test_sw_values_round_trip_with_vg(writer):
    parent = _parent()
    sw_values = _build_sw_values()
    vg = ValueGroup()
    vg_contents = SwValues()
    vg_contents.addV(Numerical().setValue("9.5"))
    vg.setVgContents(vg_contents)
    sw_values.setVg(vg)
    writer.setSwValues(parent, "SW-VALUES-PHYS", sw_values)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getSwValues(reparsed, "SW-VALUES-PHYS")
    assert reloaded is not None
    assert reloaded.getVg() is not None
    assert reloaded.getVg().getVgContents() is not None
    assert [float(v.getValue()) for v in reloaded.getVg().getVgContents().getVs()] == [9.5]


class TestSwValuesSchemaValidatedRoundTrip:
    def test_full_shape_round_trip_through_save(self):
        """All five members populated; save() validates against the bundled XSD."""
        import os
        import tempfile

        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationValueSpecification
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont

        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")

        sw_values = _build_sw_values()
        vg = ValueGroup()
        vg.setVgContents(SwValues().addV(Numerical().setValue("9.5")))
        sw_values.setVg(vg)
        cont = SwValueCont()
        cont.setSwValuesPhys(sw_values)
        spec = ApplicationValueSpecification()
        spec.setSwValueCont(cont)
        constant.setValueSpec(spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            values = constant2.getValueSpec().getSwValueCont().getSwValuesPhys()
            assert [float(v.getValue()) for v in values.getVs()] == [1.5, 2.5]
            assert [float(vf.getValue()) for vf in values.getVfs()] == [0.25]
            assert values.getVt() is not None
            assert values.getVt().getValue() == "a|b"
            assert values.getVg() is not None
            assert [float(v.getValue()) for v in values.getVg().getVgContents().getVs()] == [9.5]
            assert len(values.getVtfs()) == 1
            assert float(values.getVtfs()[0].getVf().getValue()) == 7
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
