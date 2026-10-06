"""Writer round-trip tests for ApplicationValueSpecification (Swc TPS Table 5.122, p.455).

The XSD group APPLICATION-VALUE-SPECIFICATION (AUTOSAR_00052.xsd) fixes the
child element order: CATEGORY, SW-AXIS-CONTS (wrapper of SW-AXIS-CONT
elements), SW-VALUE-CONT. The save-reload round-trip goes through the
ConstantSpecification VALUE-SPEC dispatch so the bundled-XSD validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ApplicationValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Numerical,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont, SwValueCont, SwValues, ValueList
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_spec() -> ApplicationValueSpecification:
    spec = ApplicationValueSpecification()
    spec.setCategory(Identifier().setValue("MAP"))
    spec.addSwAxisCont(SwAxisCont())
    spec.addSwAxisCont(SwAxisCont())

    cont = SwValueCont()
    unit_ref = _ref("/Units/Nm")
    unit_ref.setDest("UNIT")
    cont.setUnitRef(unit_ref)
    arraysize = ValueList()
    arraysize.setV(Numerical().setValue("2"))
    cont.setSwArraysize(arraysize)
    values = SwValues()
    values.addV(Numerical().setValue("1.5"))
    values.addV(Numerical().setValue("2.5"))
    cont.setSwValuesPhys(values)
    spec.setSwValueCont(cont)
    return spec


def _ref(value: str):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    return RefType().setValue(value)


class TestWriteApplicationValueSpecification:
    def test_write_element_order_matches_xsd_group(self):
        parent_element = ET.Element("VALUE-SPEC")
        ARXMLWriter().writeApplicationValueSpecification(parent_element, _build_spec())

        child_element = parent_element.find("APPLICATION-VALUE-SPECIFICATION")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags.index("CATEGORY") < tags.index("SW-AXIS-CONTS") < tags.index("SW-VALUE-CONT")
        assert child_element.find("CATEGORY").text == "MAP"
        axis_conts = child_element.find("SW-AXIS-CONTS")
        assert [element.tag for element in axis_conts] == ["SW-AXIS-CONT", "SW-AXIS-CONT"]

        cont_element = child_element.find("SW-VALUE-CONT")
        cont_tags = [element.tag for element in cont_element]
        assert cont_tags.index("UNIT-REF") < cont_tags.index("SW-ARRAYSIZE") < cont_tags.index("SW-VALUES-PHYS")

    def test_write_unset_fields_omit_elements(self):
        parent_element = ET.Element("VALUE-SPEC")
        ARXMLWriter().writeApplicationValueSpecification(parent_element, ApplicationValueSpecification())

        child_element = parent_element.find("APPLICATION-VALUE-SPECIFICATION")
        assert child_element is not None
        assert child_element.find("CATEGORY") is None
        assert child_element.find("SW-AXIS-CONTS") is None
        assert child_element.find("SW-VALUE-CONT") is None


class TestApplicationValueSpecificationRoundTrip:
    def test_round_trip_populated(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")
        constant.setValueSpec(_build_spec())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            spec = constant2.getValueSpec()
            assert isinstance(spec, ApplicationValueSpecification)
            assert spec.getCategory().getValue() == "MAP"
            assert len(spec.getSwAxisConts()) == 2

            cont = spec.getSwValueCont()
            assert cont.getUnitRef().getValue() == "/Units/Nm"
            assert float(cont.getSwArraysize().getV().getValue()) == 2.0
            assert [float(v.getValue()) for v in cont.getSwValuesPhys().getVs()] == [1.5, 2.5]
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")
        constant.setValueSpec(ApplicationValueSpecification())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            spec = constant2.getValueSpec()
            assert isinstance(spec, ApplicationValueSpecification)
            assert spec.getCategory() is None
            assert spec.getSwAxisConts() == []
            assert spec.getSwValueCont() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
