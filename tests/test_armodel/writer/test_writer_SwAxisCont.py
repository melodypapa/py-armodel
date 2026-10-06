"""Writer round-trip tests for SwAxisCont (Swc TPS Table 5.124, p.457).

XSD group SW-AXIS-CONT fixes the child element order: CATEGORY (offset 20),
UNIT-REF (30), UNIT-DISPLAY-NAME (40), SW-AXIS-INDEX (50), SW-ARRAYSIZE (70),
SW-VALUES-PHYS (80). The save-reload round-trip goes through the
ConstantSpecification VALUE-SPEC dispatch so the bundled-XSD validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical
from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_axis_cont() -> SwAxisCont:
    axis_cont = SwAxisCont()
    axis_cont.setCategory(CalprmAxisCategoryEnum().setValue(CalprmAxisCategoryEnum.STD_AXIS))

    unit_ref = RefType()
    unit_ref.setValue("/Units/Nm")
    unit_ref.setDest("UNIT")
    axis_cont.setUnitRef(unit_ref)

    display_name = SingleLanguageUnitNames()
    display_name.setMixedString("Nm")
    axis_cont.setUnitDisplayName(display_name)

    axis_cont.setSwAxisIndex(AxisIndexType().setValue("2"))

    arraysize = ValueList()
    arraysize.setV(Numerical().setValue("3"))
    axis_cont.setSwArraysize(arraysize)

    from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValues

    values = SwValues()
    values.addV(Numerical().setValue("0.5"))
    values.addV(Numerical().setValue("1.5"))
    axis_cont.setSwValuesPhys(values)
    return axis_cont


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType  # noqa: E402


class TestWriteSwAxisCont:
    def test_write_element_order_matches_xsd_group(self):
        parent_element = ET.Element("SW-AXIS-CONTS")
        ARXMLWriter().writeSwAxisCont(parent_element, _build_axis_cont())

        child_element = parent_element.find("SW-AXIS-CONT")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags == [
            "CATEGORY",
            "UNIT-REF",
            "UNIT-DISPLAY-NAME",
            "SW-AXIS-INDEX",
            "SW-ARRAYSIZE",
            "SW-VALUES-PHYS",
        ]
        assert child_element.find("CATEGORY").text == "STD_AXIS"
        assert child_element.find("UNIT-REF").text == "/Units/Nm"
        assert child_element.find("UNIT-REF").get("DEST") == "UNIT"
        assert child_element.find("SW-AXIS-INDEX").text == "2"

    def test_write_unset_fields_omit_elements(self):
        parent_element = ET.Element("SW-AXIS-CONTS")
        ARXMLWriter().writeSwAxisCont(parent_element, SwAxisCont())

        child_element = parent_element.find("SW-AXIS-CONT")
        assert child_element is not None
        assert len(list(child_element)) == 0


class TestSwAxisContRoundTrip:
    def test_round_trip_populated(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")
        spec = ApplicationValueSpecification()
        spec.addSwAxisCont(_build_axis_cont())
        constant.setValueSpec(spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            spec2 = constant2.getValueSpec()
            axis_conts = spec2.getSwAxisConts()
            assert len(axis_conts) == 1
            axis_cont = axis_conts[0]
            assert axis_cont.getCategory().getValue() == "stdAxis"
            assert axis_cont.getUnitRef().getValue() == "/Units/Nm"
            assert axis_cont.getUnitRef().getDest() == "UNIT"
            assert axis_cont.getUnitDisplayName().getMixedString() == "Nm"
            assert axis_cont.getSwAxisIndex().getValue() == "2"
            assert float(axis_cont.getSwArraysize().getV().getValue()) == 3.0
            assert [float(v.getValue()) for v in axis_cont.getSwValuesPhys().getVs()] == [0.5, 1.5]
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
