import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    AbsoluteTolerance,
    CyclicTiming,
    RelativeTolerance,
    TimeRangeType,
    TimeRangeTypeTolerance,
    TimeValue,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = """The timeRange can be specified with the value attribute. Optionally a tolerance can be defined."""


class TestTimeRangeType:
    """Test cases for TimeRangeType (Table 6.67, p.413)."""

    def test_initialization_defaults(self):
        obj = TimeRangeType()
        assert obj.getTolerance() is None
        assert obj.getValue() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = TimeRangeType()
        item = TimeRangeTypeTolerance()
        assert obj.setTolerance(item) is obj
        assert obj.getTolerance() is item
        obj.setTolerance(None)
        assert obj.getTolerance() is item
        item = TimeValue()
        assert obj.setValue(item) is obj
        assert obj.getValue() is item
        obj.setValue(None)
        assert obj.getValue() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimeRangeType.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = TimeRangeType()
        assert inspect.cleandoc(obj.getTolerance.__doc__) == "Optional specification of a tolerance."
        assert inspect.cleandoc(obj.setTolerance.__doc__).split("\n")[0] == "Optional specification of a tolerance."
        assert inspect.cleandoc(obj.getValue.__doc__) == "Average value of a date (in seconds)"
        assert inspect.cleandoc(obj.setValue.__doc__).split("\n")[0] == "Average value of a date (in seconds)"


class TestAbsoluteTolerance:
    """AbsoluteTolerance (XSD-only; AUTOSAR_00052.xsd group ABSOLUTE-TOLERANCE l.37)."""

    def test_initialization(self):
        obj = AbsoluteTolerance()
        assert obj.getAbsolute() is None

    def test_get_set_round_trip_and_none_noop(self):
        obj = AbsoluteTolerance()
        value = TimeValue()
        assert obj.setAbsolute(value) is obj
        assert obj.getAbsolute() is value
        obj.setAbsolute(None)
        assert obj.getAbsolute() is value


class TestRelativeTolerance:
    """RelativeTolerance (XSD-only; AUTOSAR_00052.xsd group RELATIVE-TOLERANCE l.98240)."""

    def test_initialization(self):
        obj = RelativeTolerance()
        assert obj.getRelative() is None

    def test_get_set_round_trip_and_none_noop(self):
        obj = RelativeTolerance()
        value = Integer()
        assert obj.setRelative(value) is obj
        assert obj.getRelative() is value
        obj.setRelative(None)
        assert obj.getRelative() is value


class TestTimeRangeTypeToleranceChoice:
    """The TOLERANCE element carries the ABSOLUTE-/RELATIVE-TOLERANCE choice (polymorphic TimeRangeTypeTolerance)."""

    def test_absolute_choice(self):
        wrapper = AbsoluteTolerance()
        value = TimeValue()
        wrapper.setAbsolute(value)
        assert wrapper.getAbsolute() is value

    def test_relative_choice(self):
        wrapper = RelativeTolerance()
        value = Integer()
        wrapper.setRelative(value)
        assert wrapper.getRelative() is value

    def test_subclasses_of_time_range_type_tolerance(self):
        assert issubclass(AbsoluteTolerance, TimeRangeTypeTolerance)
        assert issubclass(RelativeTolerance, TimeRangeTypeTolerance)


class TestToleranceRoundTrip:
    """Writer → XML → parser round-trip of the TOLERANCE choice (helper level)."""

    def _round_trip(self, period: TimeRangeType):
        import xml.etree.ElementTree as ET

        cyclic = CyclicTiming()
        cyclic.setTimePeriod(period)
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import TransmissionModeTiming

        wrapper = TransmissionModeTiming()
        wrapper.setCyclicTiming(cyclic)
        root = ET.Element("ROOT")
        ARXMLWriter().setTransmissionModeTiming(root, "TRANSMISSION-MODE-TIMING", wrapper)
        root.set("xmlns", "http://autosar.org/schema/r4.0")
        xml_bytes = ET.tostring(root, encoding="utf-8")

        reparsed = ET.fromstring(xml_bytes)
        ns = "http://autosar.org/schema/r4.0"
        for el in reparsed.iter():
            if not el.tag.startswith("{"):
                el.tag = "{%s}%s" % (ns, el.tag)
        parser = ARXMLParser()
        return parser.getTransmissionModeTiming(reparsed, "TRANSMISSION-MODE-TIMING").getCyclicTiming().getTimePeriod()

    def test_absolute_tolerance_round_trip(self):
        period = TimeRangeType()
        tolerance = AbsoluteTolerance()
        absolute = TimeValue()
        absolute.setValue("0.5")
        tolerance.setAbsolute(absolute)
        period.setTolerance(tolerance)
        value = TimeValue()
        value.setValue("1.0")
        period.setValue(value)

        period_2 = self._round_trip(period)
        tolerance_2 = period_2.getTolerance()
        assert isinstance(tolerance_2, AbsoluteTolerance)
        assert tolerance_2.getAbsolute().getValue() == 0.5
        assert period_2.getValue().getValue() == 1.0

    def test_relative_tolerance_round_trip(self):
        period = TimeRangeType()
        tolerance = RelativeTolerance()
        relative = Integer()
        relative.setValue("10")
        tolerance.setRelative(relative)
        period.setTolerance(tolerance)

        period_2 = self._round_trip(period)
        tolerance_2 = period_2.getTolerance()
        assert isinstance(tolerance_2, RelativeTolerance)
        assert tolerance_2.getRelative().getValue() == 10
