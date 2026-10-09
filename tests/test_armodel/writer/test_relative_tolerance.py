"""Writer round-trip tests for RelativeTolerance (Table 6.68, p.398).

The TIME-RANGE-TYPE group of AUTOSAR_00052.xsd orders TOLERANCE (choice of
ABSOLUTE-/RELATIVE-TOLERANCE) before VALUE; the RELATIVE-TOLERANCE complexType
(l.98256) adds only the RELATIVE child after the base groups, which are XML
attributes (S/T) at the AR-OBJECT level. The writer entry point setTimeRangeType
must emit the TOLERANCE/RELATIVE-TOLERANCE chain through the isinstance dispatch,
call writeARObject for the base level, and read RELATIVE through getRelative.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Integer, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import RelativeTolerance, TimeRangeType
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
    tolerance = RelativeTolerance()
    relative = Integer()
    relative.setValue("10")
    tolerance.setRelative(relative)
    time_range.setTolerance(tolerance)
    value = TimeValue()
    value.setValue("1.5")
    time_range.setValue(value)
    return time_range


def _set_base_level_attributes(tolerance: RelativeTolerance):
    checksum = String()
    checksum.setValue("9")
    tolerance.setChecksum(checksum)
    timestamp = DateTime()
    timestamp.setValue("2025-04-04T00:00:00Z")
    tolerance.setTimestamp(timestamp)


class TestWriteRelativeTolerance:
    def test_write_dispatch_creates_correct_tag(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", _build_time_range())

        tolerance_element = parent.find("TIME-PERIOD/TOLERANCE")
        assert tolerance_element is not None
        assert tolerance_element.find("RELATIVE-TOLERANCE") is not None
        assert tolerance_element.find("ABSOLUTE-TOLERANCE") is None

    def test_write_field_values_and_xsd_element_order(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", _build_time_range())

        time_range_element = parent.find("TIME-PERIOD")
        assert [child.tag for child in time_range_element] == ["TOLERANCE", "VALUE"]
        relative_element = time_range_element.find("TOLERANCE/RELATIVE-TOLERANCE/RELATIVE")
        assert relative_element is not None
        assert relative_element.text == "10"

    def test_write_base_level_attributes(self):
        time_range = _build_time_range()
        _set_base_level_attributes(time_range.getTolerance())

        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)

        relative_tolerance_element = parent.find("TIME-PERIOD/TOLERANCE/RELATIVE-TOLERANCE")
        assert relative_tolerance_element.attrib["S"] == "9"
        assert relative_tolerance_element.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_unset_relative_omits_child(self):
        time_range = TimeRangeType()
        time_range.setTolerance(RelativeTolerance())

        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)

        relative_tolerance_element = parent.find("TIME-PERIOD/TOLERANCE/RELATIVE-TOLERANCE")
        assert relative_tolerance_element is not None
        assert relative_tolerance_element.find("RELATIVE") is None

    def test_write_absent_tolerance_omits_wrapper(self):
        time_range = TimeRangeType()

        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)

        assert parent.find("TIME-PERIOD/TOLERANCE") is None


class TestRelativeToleranceRoundTrip:
    def _round_trip(self, time_range: TimeRangeType) -> TimeRangeType:
        parent = ET.Element("ROOT")
        ARXMLWriter().setTimeRangeType(parent, "TIME-PERIOD", time_range)
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
        return ARXMLParser().getTimeRangeType(root, "TIME-PERIOD")

    def test_round_trip_field_values(self):
        time_range_2 = self._round_trip(_build_time_range())
        tolerance_2 = time_range_2.getTolerance()
        assert isinstance(tolerance_2, RelativeTolerance)
        assert tolerance_2.getRelative().getValue() == 10
        assert time_range_2.getValue().getValue() == 1.5

    def test_round_trip_base_level_attributes(self):
        time_range = _build_time_range()
        _set_base_level_attributes(time_range.getTolerance())

        tolerance_2 = self._round_trip(time_range).getTolerance()
        assert tolerance_2.getChecksum().getValue() == "9"
        assert tolerance_2.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_round_trip_unset_relative(self):
        time_range = TimeRangeType()
        time_range.setTolerance(RelativeTolerance())

        tolerance_2 = self._round_trip(time_range).getTolerance()
        assert isinstance(tolerance_2, RelativeTolerance)
        assert tolerance_2.getRelative() is None
