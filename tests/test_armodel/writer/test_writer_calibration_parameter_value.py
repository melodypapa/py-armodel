"""
Writer tests for CALIBRATION-PARAMETER-VALUE — SWCT Table 5.138 (p.478, R23-11).

Builds a fully populated CalibrationParameterValue, saves it through
writeCalibrationParameterValue (the writer validates every save against the bundled XSD),
re-parses the element through readCalibrationParameterValue and asserts every field value
round-trips. The choice wrappers APPL-INIT-VALUE/IMPL-INIT-VALUE are emitted only when
set (XSD minOccurs=0); VARIATION-POINT stays the last element (xml.sequenceOffset=10000).

Round-trip counterpart: tests/test_armodel/parser/test_calibration_parameter_value.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalValueSpecification, TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import CalibrationParameterValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, RefType, String, VerbatimString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_value() -> CalibrationParameterValue:
    value = CalibrationParameterValue()

    appl = TextValueSpecification()
    appl.setShortLabel(String().setValue("APPL_INIT"))
    appl.setValue(VerbatimString().setValue("application init value"))
    value.setApplInitValue(appl)

    impl = NumericalValueSpecification()
    impl.setShortLabel(String().setValue("IMPL_INIT"))
    impl.setValue(Numerical().setValue("42"))
    value.setImplInitValue(impl)

    value.setInitializedParameterRef(RefType().setDest("FLAT-INSTANCE-DESCRIPTOR").setValue("/Pkg/FlatInstanceDescriptors/FID1"))
    return value


def _write_value_element(value: CalibrationParameterValue) -> ET.Element:
    writer = ARXMLWriter()
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    parent = ET.Element("WRAPPER")
    writer.writeCalibrationParameterValue(parent, value)
    return parent.find("CALIBRATION-PARAMETER-VALUE")


def _read_back(element: ET.Element) -> CalibrationParameterValue:
    wrapped = '<AUTOSAR xmlns="http://autosar.org/schema/r4.0">%s</AUTOSAR>' % ET.tostring(element, encoding="unicode")
    root = ET.fromstring(wrapped)
    parser = ARXMLParser()
    value = CalibrationParameterValue()
    parser.readCalibrationParameterValue(root[0], value)
    return value


class TestCalibrationParameterValueWriter:
    """Writer coverage for the CALIBRATION-PARAMETER-VALUE content (Table 5.138)."""

    def test_write_calibration_parameter_value_wrappers_and_ref(self):
        child = _write_value_element(_build_value())

        appl = child.find("APPL-INIT-VALUE")
        assert appl is not None
        appl_spec = appl.find("TEXT-VALUE-SPECIFICATION")
        assert appl_spec is not None
        assert appl_spec.find("VALUE").text == "application init value"

        impl = child.find("IMPL-INIT-VALUE")
        assert impl is not None
        impl_spec = impl.find("NUMERICAL-VALUE-SPECIFICATION")
        assert impl_spec is not None
        assert impl_spec.find("VALUE").text == "42"

        ref = child.find("INITIALIZED-PARAMETER-REF")
        assert ref is not None
        assert ref.get("DEST") == "FLAT-INSTANCE-DESCRIPTOR"
        assert ref.text == "/Pkg/FlatInstanceDescriptors/FID1"

    def test_write_calibration_parameter_value_xsd_sequence_order(self):
        """Elements are emitted in the XSD group order (APPL, IMPL, REF)."""
        child = _write_value_element(_build_value())
        tags = [child_tag.tag for child_tag in child]
        assert tags == ["APPL-INIT-VALUE", "IMPL-INIT-VALUE", "INITIALIZED-PARAMETER-REF"]

    def test_write_calibration_parameter_value_empty_omits_wrappers(self):
        """An empty CALIBRATION-PARAMETER-VALUE emits none of the optional wrappers."""
        child = _write_value_element(CalibrationParameterValue())
        assert child.find("APPL-INIT-VALUE") is None
        assert child.find("IMPL-INIT-VALUE") is None
        assert child.find("INITIALIZED-PARAMETER-REF") is None
        assert child.find("VARIATION-POINT") is None

    def test_calibration_parameter_value_element_round_trip(self):
        """Write -> re-parse -> every field value survives, one level down."""
        value = _read_back(_write_value_element(_build_value()))

        appl = value.getApplInitValue()
        assert isinstance(appl, TextValueSpecification)
        assert appl.getValue().getValue() == "application init value"
        assert appl.getShortLabel().getValue() == "APPL_INIT"

        impl = value.getImplInitValue()
        assert isinstance(impl, NumericalValueSpecification)
        assert impl.getValue().getValue() == 42

        ref = value.getInitializedParameterRef()
        assert ref is not None
        assert ref.getValue() == "/Pkg/FlatInstanceDescriptors/FID1"
        assert ref.getDest() == "FLAT-INSTANCE-DESCRIPTOR"

    def test_calibration_parameter_value_variation_point_is_last_element(self):
        """A set VariationPoint is written as the last element (xml.sequenceOffset=10000)."""
        value = _build_value()
        value.setVariationPoint(VariationPoint())

        child = _write_value_element(value)
        assert child[-1].tag == "VARIATION-POINT"

        reloaded = _read_back(child)
        assert reloaded.getVariationPoint() is not None
