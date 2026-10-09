"""Parser tests for RelativeTolerance (Table 6.68, p.398).

The RELATIVE-TOLERANCE group of AUTOSAR_00052.xsd (l.98240) holds the single
optional RELATIVE element (AR:INTEGER); the complexType (l.98256) stacks the
base groups AR-OBJECT .. TIME-RANGE-TYPE-TOLERANCE in front of it, so the
reader entry point getTimeRangeType must call readARObject for the S/T base
level and populate RELATIVE via the setRelative mutator. TOLERANCE is a choice
wrapper over ABSOLUTE-/RELATIVE-TOLERANCE; an empty wrapper selects neither.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import RelativeTolerance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadRelativeTolerance:
    def test_read_field_value(self):
        xml = f"""<ROOT xmlns='{NS}'>
            <TIME-PERIOD>
                <TOLERANCE>
                    <RELATIVE-TOLERANCE>
                        <RELATIVE>10</RELATIVE>
                    </RELATIVE-TOLERANCE>
                </TOLERANCE>
                <VALUE>1.5</VALUE>
            </TIME-PERIOD>
        </ROOT>"""
        time_range = ARXMLParser().getTimeRangeType(ET.fromstring(xml), "TIME-PERIOD")

        tolerance = time_range.getTolerance()
        assert isinstance(tolerance, RelativeTolerance)
        assert tolerance.getRelative().getValue() == 10
        assert time_range.getValue().getValue() == 1.5

    def test_read_base_level_attributes(self):
        xml = f"""<ROOT xmlns='{NS}'>
            <TIME-PERIOD>
                <TOLERANCE>
                    <RELATIVE-TOLERANCE S='5' T='2025-04-04T00:00:00Z'>
                        <RELATIVE>7</RELATIVE>
                    </RELATIVE-TOLERANCE>
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
                    <RELATIVE-TOLERANCE/>
                </TOLERANCE>
            </TIME-PERIOD>
        </ROOT>"""
        time_range = ARXMLParser().getTimeRangeType(ET.fromstring(xml), "TIME-PERIOD")

        tolerance = time_range.getTolerance()
        assert isinstance(tolerance, RelativeTolerance)
        assert tolerance.getRelative() is None

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
