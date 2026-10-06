"""
Tests for reading CALIBRATION-PARAMETER-VALUE — SWCT Table 5.138 (p.478, R23-11).

CalibrationParameterValue (Base = ARObject) is aggregated by
CalibrationParameterValueSet.calibrationParameterValue. The reader walks the XSD group
CALIBRATION-PARAMETER-VALUE (AUTOSAR_00052.xsd l.14100: APPL-INIT-VALUE, IMPL-INIT-VALUE,
INITIALIZED-PARAMETER-REF, VARIATION-POINT last per xml.sequenceOffset=10000) and populates
the model via the setXxx mutators, reading both init-value wrappers through the shared
getValueSpecification choice dispatch.

Round-trip counterpart: tests/test_armodel/writer/test_writer_calibration_parameter_value.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalValueSpecification, TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import CalibrationParameterValue
from armodel.parser.arxml_parser import ARXMLParser

FULL_VALUE_XML = """
<CALIBRATION-PARAMETER-VALUE xmlns="http://autosar.org/schema/r4.0">
    <APPL-INIT-VALUE>
        <TEXT-VALUE-SPECIFICATION>
            <SHORT-LABEL>APPL_INIT</SHORT-LABEL>
            <VALUE>application init value</VALUE>
        </TEXT-VALUE-SPECIFICATION>
    </APPL-INIT-VALUE>
    <IMPL-INIT-VALUE>
        <NUMERICAL-VALUE-SPECIFICATION>
            <SHORT-LABEL>IMPL_INIT</SHORT-LABEL>
            <VALUE>42</VALUE>
        </NUMERICAL-VALUE-SPECIFICATION>
    </IMPL-INIT-VALUE>
    <INITIALIZED-PARAMETER-REF DEST="FLAT-INSTANCE-DESCRIPTOR">/Pkg/FlatInstanceDescriptors/FID1</INITIALIZED-PARAMETER-REF>
</CALIBRATION-PARAMETER-VALUE>
"""  # noqa E501

BARE_VALUE_XML = """
<CALIBRATION-PARAMETER-VALUE xmlns="http://autosar.org/schema/r4.0" S="5" T="2023-11-01T10:00:00+01:00">
</CALIBRATION-PARAMETER-VALUE>
"""  # noqa E501

VP_VALUE_XML = """
<CALIBRATION-PARAMETER-VALUE xmlns="http://autosar.org/schema/r4.0">
    <APPL-INIT-VALUE>
        <TEXT-VALUE-SPECIFICATION>
            <VALUE>variant value</VALUE>
        </TEXT-VALUE-SPECIFICATION>
    </APPL-INIT-VALUE>
    <VARIATION-POINT />
</CALIBRATION-PARAMETER-VALUE>
"""  # noqa E501


def _parse_value(xml_text):
    parser = ARXMLParser()
    element = ET.fromstring(xml_text)
    value = CalibrationParameterValue()
    parser.readCalibrationParameterValue(element, value)
    return value


class TestCalibrationParameterValueParser:
    """Reader coverage for the CALIBRATION-PARAMETER-VALUE content (Table 5.138)."""

    def test_read_calibration_parameter_value_appl_init_value(self):
        """The APPL-INIT-VALUE choice wrapper reads into a typed ValueSpecification."""
        value = _parse_value(FULL_VALUE_XML)
        appl = value.getApplInitValue()
        assert isinstance(appl, TextValueSpecification)
        assert appl.getValue().getValue() == "application init value"
        assert appl.getShortLabel().getValue() == "APPL_INIT"

    def test_read_calibration_parameter_value_impl_init_value(self):
        """The IMPL-INIT-VALUE choice wrapper reads into a typed ValueSpecification."""
        value = _parse_value(FULL_VALUE_XML)
        impl = value.getImplInitValue()
        assert isinstance(impl, NumericalValueSpecification)
        assert impl.getValue().getValue() == 42
        assert impl.getShortLabel().getValue() == "IMPL_INIT"

    def test_read_calibration_parameter_value_initialized_parameter_ref(self):
        """INITIALIZED-PARAMETER-REF reads with DEST and value (Kind ref row)."""
        value = _parse_value(FULL_VALUE_XML)
        ref = value.getInitializedParameterRef()
        assert ref is not None
        assert ref.getValue() == "/Pkg/FlatInstanceDescriptors/FID1"
        assert ref.getDest() == "FLAT-INSTANCE-DESCRIPTOR"

    def test_read_calibration_parameter_value_checksum(self):
        """The AR:AR-OBJECT level (S/T attributes) round-trips through readARObject (Rule 0025)."""
        value = _parse_value(FULL_VALUE_XML)
        assert value.getChecksum() is None

        bare = _parse_value(BARE_VALUE_XML)
        assert bare.getChecksum().getValue() == "5"

    def test_read_calibration_parameter_value_absent_optionals(self):
        """A CALIBRATION-PARAMETER-VALUE without the optional rows leaves the fields None."""
        value = _parse_value(BARE_VALUE_XML)
        assert value.getApplInitValue() is None
        assert value.getImplInitValue() is None
        assert value.getInitializedParameterRef() is None

    def test_read_calibration_parameter_value_variation_point(self):
        """A trailing VARIATION-POINT (sequenceOffset=10000) is read via the VP mixin."""
        value = _parse_value(VP_VALUE_XML)
        assert value.getVariationPoint() is not None
        assert isinstance(value.getApplInitValue(), TextValueSpecification)
