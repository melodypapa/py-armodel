"""
Tests for reading CALIBRATION-PARAMETER-VALUE-SET — SWCT Table 5.137 (p.477, R23-11).

CalibrationParameterValueSet (Base = ARElement) is aggregated by ARPackage.element. The
reader walks the CALIBRATION-PARAMETER-VALUES wrapper (AUTOSAR_00052.xsd group
CALIBRATION-PARAMETER-VALUE-SET, unbounded PHYSICAL-DIMENSION-style choice) and populates
the model via addCalibrationParameterValue, reading each nested CALIBRATION-PARAMETER-VALUE
through readCalibrationParameterValue (Table 5.138).

Round-trip counterpart: tests/test_armodel/writer/test_writer_calibration_parameter_value_set.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CalibrationParameterValueSet
from armodel.parser.arxml_parser import ARXMLParser

FULL_SET_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>CalibrationParameterValueSets</SHORT-NAME>
            <ELEMENTS>
                <CALIBRATION-PARAMETER-VALUE-SET>
                    <SHORT-NAME>EngineCalprm</SHORT-NAME>
                    <CALIBRATION-PARAMETER-VALUES>
                        <CALIBRATION-PARAMETER-VALUE>
                            <APPL-INIT-VALUE>
                                <TEXT-VALUE-SPECIFICATION>
                                    <VALUE>injection map</VALUE>
                                </TEXT-VALUE-SPECIFICATION>
                            </APPL-INIT-VALUE>
                            <INITIALIZED-PARAMETER-REF DEST="FLAT-INSTANCE-DESCRIPTOR">/CalibrationParameterValueSets/FlatInstanceDescriptors/FID1</INITIALIZED-PARAMETER-REF>
                        </CALIBRATION-PARAMETER-VALUE>
                        <CALIBRATION-PARAMETER-VALUE>
                            <IMPL-INIT-VALUE>
                                <NUMERICAL-VALUE-SPECIFICATION>
                                    <VALUE>42</VALUE>
                                </NUMERICAL-VALUE-SPECIFICATION>
                            </IMPL-INIT-VALUE>
                        </CALIBRATION-PARAMETER-VALUE>
                    </CALIBRATION-PARAMETER-VALUES>
                </CALIBRATION-PARAMETER-VALUE-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501

EMPTY_SET_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>CalibrationParameterValueSets</SHORT-NAME>
            <ELEMENTS>
                <CALIBRATION-PARAMETER-VALUE-SET>
                    <SHORT-NAME>EmptyCalprm</SHORT-NAME>
                    <CALIBRATION-PARAMETER-VALUES/>
                </CALIBRATION-PARAMETER-VALUE-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501

NO_WRAPPER_SET_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>CalibrationParameterValueSets</SHORT-NAME>
            <ELEMENTS>
                <CALIBRATION-PARAMETER-VALUE-SET>
                    <SHORT-NAME>NoCalprm</SHORT-NAME>
                </CALIBRATION-PARAMETER-VALUE-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501


def _load_set(xml_text):
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = ET.fromstring(xml_text)
    document = AUTOSARDoc()
    parser.readARPackages(element, document)
    ar_package = document.getARPackages()[0]
    sets = ar_package.getCalibrationParameterValueSets()
    assert len(sets) == 1
    return sets[0]


class TestCalibrationParameterValueSetParser:
    """Reader coverage for the CALIBRATION-PARAMETER-VALUE-SET content (Table 5.137)."""

    def test_read_calibration_parameter_value_set_short_name(self):
        calprm_set = _load_set(FULL_SET_XML)
        assert isinstance(calprm_set, CalibrationParameterValueSet)
        assert calprm_set.getShortName() == "EngineCalprm"

    def test_read_calibration_parameter_value_set_values(self):
        """Both nested CALIBRATION-PARAMETER-VALUE items round-trip with their field values."""
        calprm_set = _load_set(FULL_SET_XML)
        values = calprm_set.getCalibrationParameterValues()
        assert len(values) == 2
        first, second = values
        assert isinstance(first.getApplInitValue(), TextValueSpecification)
        assert first.getApplInitValue().getValue().getValue() == "injection map"
        assert first.getInitializedParameterRef().getValue() == "/CalibrationParameterValueSets/FlatInstanceDescriptors/FID1"
        assert first.getInitializedParameterRef().getDest() == "FLAT-INSTANCE-DESCRIPTOR"
        assert second.getImplInitValue().getValue().getValue() == 42
        assert second.getApplInitValue() is None
        assert second.getInitializedParameterRef() is None

    def test_read_calibration_parameter_value_set_empty_wrapper(self):
        """An empty CALIBRATION-PARAMETER-VALUES wrapper yields an empty list."""
        calprm_set = _load_set(EMPTY_SET_XML)
        assert calprm_set.getCalibrationParameterValues() == []

    def test_read_calibration_parameter_value_set_absent_wrapper(self):
        """A CALIBRATION-PARAMETER-VALUE-SET without the wrapper yields an empty list (0..*)."""
        calprm_set = _load_set(NO_WRAPPER_SET_XML)
        assert calprm_set.getCalibrationParameterValues() == []
