"""Writer round-trip tests for AbsoluteTolerance (Table 6.69, p.398).

The TIME-RANGE-TYPE group of AUTOSAR_00052.xsd orders TOLERANCE (choice of
ABSOLUTE-/RELATIVE-TOLERANCE) before VALUE; the ABSOLUTE-TOLERANCE complexType
(l.53) adds only the ABSOLUTE child after the base groups, which are XML
attributes (S/T) at the AR-OBJECT level. The writer entry point setTimeRangeType
must emit the TOLERANCE/ABSOLUTE-TOLERANCE chain through the isinstance dispatch,
call writeARObject for the base level, and read ABSOLUTE through getAbsolute.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import AbsoluteTolerance, TimeRangeType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_time_range() -> TimeRangeType:
    time_range = TimeRangeType()
    tolerance = AbsoluteTolerance()
    absolute = TimeValue()
    absolute.setValue("0.5")
    tolerance.setAbsolute(absolute)
    time_range.setTolerance(tolerance)
    value = TimeValue()
    value.setValue("1.5")
    time_range.setValue(value)
    return time_range


def _set_base_level_attributes(tolerance: AbsoluteTolerance):
    checksum = String()
    checksum.setValue("9")
    tolerance.setChecksum(checksum)
    timestamp = DateTime()
    timestamp.setValue("2025-04-04T00:00:00Z")
    tolerance.setTimestamp(timestamp)


class TestWriteAbsoluteTolerance:
    def test_write_dispatch_creates_correct_tag(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", _build_time_range())

        tolerance_element = parent.find("TIME-PERIOD/TOLERANCE")
        assert tolerance_element is not None
        assert tolerance_element.find("ABSOLUTE-TOLERANCE") is not None
        assert tolerance_element.find("RELATIVE-TOLERANCE") is None

    def test_write_field_values_and_xsd_element_order(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", _build_time_range())

        time_range_element = parent.find("TIME-PERIOD")
        assert [child.tag for child in time_range_element] == ["TOLERANCE", "VALUE"]
        absolute_element = time_range_element.find("TOLERANCE/ABSOLUTE-TOLERANCE/ABSOLUTE")
        assert absolute_element is not None
        assert absolute_element.text == "0.5"

    def test_write_base_level_attributes(self):
        time_range = _build_time_range()
        _set_base_level_attributes(time_range.getTolerance())

        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)

        absolute_tolerance_element = parent.find("TIME-PERIOD/TOLERANCE/ABSOLUTE-TOLERANCE")
        assert absolute_tolerance_element.attrib["S"] == "9"
        assert absolute_tolerance_element.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_unset_absolute_omits_child(self):
        time_range = TimeRangeType()
        time_range.setTolerance(AbsoluteTolerance())

        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)

        absolute_tolerance_element = parent.find("TIME-PERIOD/TOLERANCE/ABSOLUTE-TOLERANCE")
        assert absolute_tolerance_element is not None
        assert absolute_tolerance_element.find("ABSOLUTE") is None

    def test_write_absent_tolerance_omits_wrapper(self):
        time_range = TimeRangeType()

        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)

        assert parent.find("TIME-PERIOD/TOLERANCE") is None


class TestAbsoluteToleranceRoundTrip:
    def _round_trip(self, time_range: TimeRangeType) -> TimeRangeType:
        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
        return ARXMLParser().getTimeRangeType(root, "TIME-PERIOD")

    def test_round_trip_field_values(self):
        time_range_2 = self._round_trip(_build_time_range())
        tolerance_2 = time_range_2.getTolerance()
        assert isinstance(tolerance_2, AbsoluteTolerance)
        assert tolerance_2.getAbsolute().getValue() == 0.5
        assert time_range_2.getValue().getValue() == 1.5

    def test_round_trip_base_level_attributes(self):
        time_range = _build_time_range()
        _set_base_level_attributes(time_range.getTolerance())

        tolerance_2 = self._round_trip(time_range).getTolerance()
        assert tolerance_2.getChecksum().getValue() == "9"
        assert tolerance_2.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_round_trip_unset_absolute(self):
        time_range = TimeRangeType()
        time_range.setTolerance(AbsoluteTolerance())

        tolerance_2 = self._round_trip(time_range).getTolerance()
        assert isinstance(tolerance_2, AbsoluteTolerance)
        assert tolerance_2.getAbsolute() is None
