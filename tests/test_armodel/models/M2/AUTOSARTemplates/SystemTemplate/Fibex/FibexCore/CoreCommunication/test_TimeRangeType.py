import inspect
import typing

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


RELATIVE_TOLERANCE_CLASS_NOTE = "Maximum allowable deviation"
RELATIVE_TOLERANCE_CLASS_CONSTRAINTS = (
    "[constr_9191] Existence of RelativeTolerance.relative: For each RelativeTolerance, the attribute relative shall exist at the time when the System Description is complete.",
)
RELATIVE_NOTE = "Maximum allowable deviation in percent (percent of the corresponding TimeValue)."


class TestRelativeTolerance:
    """RelativeTolerance (Table 6.68, p.398)."""

    def test_inheritance(self):
        assert issubclass(RelativeTolerance, TimeRangeTypeTolerance)

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

    def test_annotation_pins(self):
        getter_hints = typing.get_type_hints(RelativeTolerance.getRelative)
        assert getter_hints.get("return") == typing.Optional[Integer]
        setter_hints = typing.get_type_hints(RelativeTolerance.setRelative)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is RelativeTolerance

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RelativeTolerance.__doc__) == RELATIVE_TOLERANCE_CLASS_NOTE + "\n\n" + "\n".join(RELATIVE_TOLERANCE_CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        obj = RelativeTolerance()
        assert inspect.cleandoc(obj.getRelative.__doc__) == RELATIVE_NOTE
        assert inspect.cleandoc(obj.setRelative.__doc__).split("\n")[0] == RELATIVE_NOTE

    def test_init_has_no_docstring(self):
        assert RelativeTolerance.__init__.__doc__ is None


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
