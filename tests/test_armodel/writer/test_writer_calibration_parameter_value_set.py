"""
Writer tests for CALIBRATION-PARAMETER-VALUE-SET — SWCT Table 5.137 (p.477, R23-11).

Builds a fully populated CalibrationParameterValueSet on an ARPackage, saves (the writer
validates every save against the bundled XSD), reloads and asserts every field value
round-trips — including the nested CALIBRATION-PARAMETER-VALUE items of Table 5.138. The
CALIBRATION-PARAMETER-VALUES wrapper is emitted only when non-empty (XSD minOccurs=0).

Round-trip counterpart: tests/test_armodel/parser/test_calibration_parameter_value_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalValueSpecification, TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import CalibrationParameterValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CalibrationParameterValueSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, RefType, VerbatimString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_document() -> AUTOSAR:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _make_value(appl_text=None, impl_number=None, ref=None) -> CalibrationParameterValue:
    value = CalibrationParameterValue()
    if appl_text is not None:
        appl = TextValueSpecification()
        appl.setValue(VerbatimString().setValue(appl_text))
        value.setApplInitValue(appl)
    if impl_number is not None:
        impl = NumericalValueSpecification()
        impl.setValue(Numerical().setValue(impl_number))
        value.setImplInitValue(impl)
    if ref is not None:
        value.setInitializedParameterRef(RefType().setDest("FLAT-INSTANCE-DESCRIPTOR").setValue(ref))
    return value


def _build_set(document) -> CalibrationParameterValueSet:
    ar_package = document.createARPackage("CalibrationParameterValueSets")
    calprm_set = ar_package.createCalibrationParameterValueSet("EngineCalprm")

    calprm_set.addCalibrationParameterValue(_make_value(appl_text="injection map", ref="/CalibrationParameterValueSets/FlatInstanceDescriptors/FID1"))
    calprm_set.addCalibrationParameterValue(_make_value(impl_number="42"))
    return calprm_set


def _write_set_element(calprm_set):
    writer = ARXMLWriter()
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    parent = ET.Element("ELEMENTS")
    writer.writeCalibrationParameterValueSet(parent, calprm_set)
    return parent.find("CALIBRATION-PARAMETER-VALUE-SET")


def _save_and_reload(document):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)
        document_2 = _make_document()
        ARXMLParser().load(file_path, document_2)
        return document_2
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


class TestCalibrationParameterValueSetWriter:
    """Writer coverage for the CALIBRATION-PARAMETER-VALUE-SET content (Table 5.137)."""

    def test_write_calibration_parameter_value_set_wrapper_and_items(self):
        child = _write_set_element(_build_set(_make_document()))
        wrapper = child.find("CALIBRATION-PARAMETER-VALUES")
        assert wrapper is not None
        items = list(wrapper)
        assert [item.tag for item in items] == ["CALIBRATION-PARAMETER-VALUE", "CALIBRATION-PARAMETER-VALUE"]
        assert items[0].find("APPL-INIT-VALUE/TEXT-VALUE-SPECIFICATION/VALUE").text == "injection map"
        assert items[0].find("INITIALIZED-PARAMETER-REF").get("DEST") == "FLAT-INSTANCE-DESCRIPTOR"
        assert items[1].find("IMPL-INIT-VALUE/NUMERICAL-VALUE-SPECIFICATION/VALUE").text == "42"

    def test_write_calibration_parameter_value_set_empty_omits_wrapper(self):
        """A set without values emits no CALIBRATION-PARAMETER-VALUES wrapper (XSD minOccurs=0)."""
        document = _make_document()
        document.createARPackage("CalibrationParameterValueSets").createCalibrationParameterValueSet("EmptyCalprm")

        child = _write_set_element(document.getARPackages()[0].getCalibrationParameterValueSets()[0])
        assert child.find("CALIBRATION-PARAMETER-VALUES") is None

    def test_calibration_parameter_value_set_round_trip(self):
        """Save (XSD-validated) -> reload -> every field value survives, including nested values."""
        document = _make_document()
        _build_set(document)

        document_2 = _save_and_reload(document)
        sets = document_2.getARPackages()[0].getCalibrationParameterValueSets()
        assert len(sets) == 1
        reloaded = sets[0]
        assert isinstance(reloaded, CalibrationParameterValueSet)
        assert reloaded.getShortName() == "EngineCalprm"

        values = reloaded.getCalibrationParameterValues()
        assert len(values) == 2
        first, second = values
        assert isinstance(first.getApplInitValue(), TextValueSpecification)
        assert first.getApplInitValue().getValue().getValue() == "injection map"
        assert first.getInitializedParameterRef().getValue() == "/CalibrationParameterValueSets/FlatInstanceDescriptors/FID1"
        assert first.getInitializedParameterRef().getDest() == "FLAT-INSTANCE-DESCRIPTOR"
        assert isinstance(second.getImplInitValue(), NumericalValueSpecification)
        assert second.getImplInitValue().getValue().getValue() == 42

    def test_calibration_parameter_value_set_round_trip_empty(self):
        """A set without values round-trips to an empty list."""
        document = _make_document()
        document.createARPackage("CalibrationParameterValueSets").createCalibrationParameterValueSet("EmptyCalprm")

        document_2 = _save_and_reload(document)
        sets = document_2.getARPackages()[0].getCalibrationParameterValueSets()
        assert len(sets) == 1
        assert sets[0].getShortName() == "EmptyCalprm"
        assert sets[0].getCalibrationParameterValues() == []
