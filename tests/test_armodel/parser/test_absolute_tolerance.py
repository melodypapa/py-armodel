"""Parser tests for AbsoluteTolerance (Table 6.69, p.398).

The ABSOLUTE-TOLERANCE group of AUTOSAR_00052.xsd (l.37) holds the single
optional ABSOLUTE element (AR:TIME-VALUE); the complexType (l.53) stacks the
base groups AR-OBJECT .. TIME-RANGE-TYPE-TOLERANCE in front of it, so the
reader entry point getTimeRangeType must call readARObject for the S/T base
level and populate ABSOLUTE via the setAbsolute mutator. TOLERANCE is a choice
wrapper over ABSOLUTE-/RELATIVE-TOLERANCE; an empty wrapper selects neither.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import AbsoluteTolerance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadAbsoluteTolerance:
    def test_read_field_value(self):
        xml = f"""<ROOT xmlns='{NS}'>
            <TIME-PERIOD>
                <TOLERANCE>
                    <ABSOLUTE-TOLERANCE>
                        <ABSOLUTE>0.5</ABSOLUTE>
                    </ABSOLUTE-TOLERANCE>
                </TOLERANCE>
                <VALUE>1.5</VALUE>
            </TIME-PERIOD>
        </ROOT>"""
        time_range = ARXMLParser().getTimeRangeType(ET.fromstring(xml), "TIME-PERIOD")

        tolerance = time_range.getTolerance()
        assert isinstance(tolerance, AbsoluteTolerance)
        assert tolerance.getAbsolute().getValue() == 0.5
        assert time_range.getValue().getValue() == 1.5

    def test_read_base_level_attributes(self):
        xml = f"""<ROOT xmlns='{NS}'>
            <TIME-PERIOD>
                <TOLERANCE>
                    <ABSOLUTE-TOLERANCE S='5' T='2025-04-04T00:00:00Z'>
                        <ABSOLUTE>0.25</ABSOLUTE>
                    </ABSOLUTE-TOLERANCE>
                </TOLERANCE>
            </TIME-PERIOD>
        </ROOT>"""
        time_range = ARXMLParser().getTimeRangeType(ET.fromstring(xml), "TIME-PERIOD")

        tolerance = time_range.getTolerance()
        assert tolerance.getChecksum().getValue() == "5"
        assert tolerance.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_read_empty_tolerance_element(self):
        xml = f"""<ROOT xmlns='{NS}'>
            <TIME-PERIOD>
                <TOLERANCE>
                    <ABSOLUTE-TOLERANCE/>
                </TOLERANCE>
            </TIME-PERIOD>
        </ROOT>"""
        time_range = ARXMLParser().getTimeRangeType(ET.fromstring(xml), "TIME-PERIOD")

        tolerance = time_range.getTolerance()
        assert isinstance(tolerance, AbsoluteTolerance)
        assert tolerance.getAbsolute() is None

    def test_read_empty_tolerance_wrapper_selects_neither_branch(self):
        xml = f"""<ROOT xmlns='{NS}'>
            <TIME-PERIOD>
                <TOLERANCE/>
                <VALUE>2.0</VALUE>
            </TIME-PERIOD>
        </ROOT>"""
        time_range = ARXMLParser().getTimeRangeType(ET.fromstring(xml), "TIME-PERIOD")

        assert time_range.getTolerance() is None
        assert time_range.getValue().getValue() == 2.0

    def test_read_absent_tolerance(self):
        xml = f"""<ROOT xmlns='{NS}'>
            <TIME-PERIOD>
                <VALUE>3.0</VALUE>
            </TIME-PERIOD>
        </ROOT>"""
        time_range = ARXMLParser().getTimeRangeType(ET.fromstring(xml), "TIME-PERIOD")

        assert time_range.getTolerance() is None
        assert time_range.getValue().getValue() == 3.0
