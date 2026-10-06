"""Writer round-trip tests for NumericalOrText (Swc TPS Table 5.123, p.456).

XSD group NUMERICAL-OR-TEXT fixes the child element order: VF (offset 10),
VT (offset 20), VARIATION-POINT (offset 10000). The save-reload round-trip
reaches the VTF element through ConstantSpecification VALUE-SPEC /
APPLICATION-VALUE-SPECIFICATION / SW-VALUE-CONT / SW-VALUES-PHYS so the
bundled-XSD validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ApplicationValueSpecification,
    NumericalOrText,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, String
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont, SwValues
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_vtf() -> NumericalOrText:
    vtf = NumericalOrText()
    vtf.setVf(Numerical().setValue("7.25"))
    vtf.setVt(String().setValue("fallback"))
    return vtf


def _build_document():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Pkg")
    constant = pkg.createConstantSpecification("Const")
    spec = ApplicationValueSpecification()
    cont = SwValueCont()
    values = SwValues()
    values.addVtf(_build_vtf())
    cont.setSwValuesPhys(values)
    spec.setSwValueCont(cont)
    constant.setValueSpec(spec)
    return document


class TestWriteNumericalOrText:
    def test_write_element_order_matches_xsd_group(self):
        parent_element = ET.Element("SW-VALUES-PHYS")
        ARXMLWriter().writeNumericalOrText(parent_element, "VTF", _build_vtf())

        child_element = parent_element.find("VTF")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags.index("VF") < tags.index("VT")
        assert child_element.find("VF").text == "7.25"
        assert child_element.find("VT").text == "fallback"

    def test_write_unset_fields_omit_elements(self):
        parent_element = ET.Element("SW-VALUES-PHYS")
        ARXMLWriter().writeNumericalOrText(parent_element, "VTF", NumericalOrText())

        child_element = parent_element.find("VTF")
        assert child_element is not None
        assert child_element.find("VF") is None
        assert child_element.find("VT") is None


class TestNumericalOrTextRoundTrip:
    def test_round_trip_populated(self):
        document = _build_document()

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            spec = constant.getValueSpec()
            values = spec.getSwValueCont().getSwValuesPhys()
            vtfs = values.getVtfs()
            assert len(vtfs) == 1
            vtf = vtfs[0]
            assert isinstance(vtf, NumericalOrText)
            assert isinstance(vtf.getVf(), Numerical)
            assert float(vtf.getVf().getValue()) == 7.25
            assert isinstance(vtf.getVt(), String)
            assert vtf.getVt().getValue() == "fallback"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
