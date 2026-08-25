"""Writer round-trip tests for the timing constraint base class and timing clocks (TIMING-CONSTRAINT, TIMING-CLOCK, TDLET-ZONE-CLOCK, TIMING-CLOCK-SYNC-ACCURACY)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TDLETZoneClock import (
    TDLETZoneClock,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TimingClockSyncAccuracy import (
    TimingClockSyncAccuracy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteTimingConstraint(TimingConstraint):
    pass


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    if xml_str.rstrip().endswith("/>"):
        xml_str = xml_str.rstrip()[:-2].rstrip() + ' xmlns="http://autosar.org/schema/r4.0"/>'
    else:
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestWriteTimingConstraint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_timing_constraint_full(self):
        parent = self._parent()
        constraint = ConcreteTimingConstraint(parent, "Constraint1")
        constraint.addTraceRef(RefType().setValue("/AUTOSAR/Requirement1"))
        constraint.setTimingConditionRef(RefType().setValue("/AUTOSAR/Condition").setDest("TIMING-CONDITION"))

        element = ET.Element("EXECUTION-TIME-CONSTRAINT")
        ARXMLWriter().writeTimingConstraint(element, constraint)
        assert element.find("SHORT-NAME").text == "Constraint1"
        condition_ref = element.find("TIMING-CONDITION-REF")
        assert condition_ref is not None
        assert condition_ref.text == "/AUTOSAR/Condition"
        assert condition_ref.attrib["DEST"] == "TIMING-CONDITION"
        trace_refs_tag = element.find("TRACE-REFS")
        assert trace_refs_tag is not None
        assert len(trace_refs_tag.findall("TRACE-REF")) == 1

        reloaded = ConcreteTimingConstraint(parent, "Constraint1")
        ARXMLParser().readTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Constraint1"
        assert reloaded.getTimingConditionRef().getValue() == "/AUTOSAR/Condition"
        assert reloaded.getTimingConditionRef().getDest() == "TIMING-CONDITION"
        assert len(reloaded.getTraceRefs()) == 1
        assert reloaded.getTraceRefs()[0].getValue() == "/AUTOSAR/Requirement1"

    def test_write_timing_constraint_empty(self):
        parent = self._parent()
        constraint = ConcreteTimingConstraint(parent, "Constraint1")

        element = ET.Element("EXECUTION-TIME-CONSTRAINT")
        ARXMLWriter().writeTimingConstraint(element, constraint)
        assert element.find("SHORT-NAME").text == "Constraint1"
        assert element.find("TIMING-CONDITION-REF") is None
        assert element.find("TRACE-REFS") is None

        reloaded = ConcreteTimingConstraint(parent, "Constraint1")
        ARXMLParser().readTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Constraint1"
        assert reloaded.getTimingConditionRef() is None
        assert reloaded.getTraceRefs() == []


class TestWriteTimingClocks:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    @staticmethod
    def _mdt(cse_code: str, factor: str) -> MultidimensionalTime:
        mdt = MultidimensionalTime()
        mdt.setCseCode(CseCodeType().setValue(cse_code))
        mdt.setCseCodeFactor(Integer().setValue(factor))
        return mdt

    def test_round_trip_tdlet_zone_clock_full(self):
        parent = self._parent()
        clock = TDLETZoneClock(parent, "Zone1")
        clock.setPlatformTimeBaseRef(RefType().setValue("/AUTOSAR/TimeDomain").setDest("GLOBAL-TIME-DOMAIN"))
        clock.setAccuracyExt(self._mdt("0", "30"))
        clock.setAccuracyInt(self._mdt("0", "50"))

        element = ET.Element("TDLET-ZONE-CLOCK")
        ARXMLWriter().writeTDLETZoneClock(element, clock)
        assert element.find("SHORT-NAME").text == "Zone1"
        platform_time_bases = element.find("PLATFORM-TIME-BASES")
        assert platform_time_bases is not None
        conditional = platform_time_bases.find("GLOBAL-TIME-DOMAIN-REF-CONDITIONAL")
        assert conditional is not None
        domain_ref = conditional.find("GLOBAL-TIME-DOMAIN-REF")
        assert domain_ref.text == "/AUTOSAR/TimeDomain"
        assert domain_ref.attrib["DEST"] == "GLOBAL-TIME-DOMAIN"
        accuracy_ext = element.find("ACCURACY-EXT")
        assert accuracy_ext is not None
        assert accuracy_ext.find("CSE-CODE-FACTOR").text == "30"
        accuracy_int = element.find("ACCURACY-INT")
        assert accuracy_int is not None
        assert accuracy_int.find("CSE-CODE-FACTOR").text == "50"

        reloaded = TDLETZoneClock(parent, "Zone1")
        ARXMLParser().readTDLETZoneClock(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Zone1"
        assert reloaded.getPlatformTimeBaseRef().getValue() == "/AUTOSAR/TimeDomain"
        assert reloaded.getPlatformTimeBaseRef().getDest() == "GLOBAL-TIME-DOMAIN"
        assert reloaded.getAccuracyExt().getCseCodeFactor().getValue() == 30
        assert reloaded.getAccuracyInt().getCseCodeFactor().getValue() == 50

    def test_write_tdlet_zone_clock_empty(self):
        parent = self._parent()
        clock = TDLETZoneClock(parent, "Zone1")

        element = ET.Element("TDLET-ZONE-CLOCK")
        ARXMLWriter().writeTDLETZoneClock(element, clock)
        assert element.find("SHORT-NAME").text == "Zone1"
        assert element.find("PLATFORM-TIME-BASES") is None
        assert element.find("ACCURACY-EXT") is None
        assert element.find("ACCURACY-INT") is None

        reloaded = TDLETZoneClock(parent, "Zone1")
        ARXMLParser().readTDLETZoneClock(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Zone1"
        assert reloaded.getPlatformTimeBaseRef() is None
        assert reloaded.getAccuracyExt() is None
        assert reloaded.getAccuracyInt() is None

    def test_round_trip_timing_clock_sync_accuracy_full(self):
        parent = self._parent()
        accuracy = TimingClockSyncAccuracy(parent, "Sync1")
        accuracy.setAccuracy(self._mdt("0", "10"))
        accuracy.setLowerRef(RefType().setValue("/AUTOSAR/TargetClock").setDest("TDLET-ZONE-CLOCK"))
        accuracy.setUpperRef(RefType().setValue("/AUTOSAR/SourceClock").setDest("TDLET-ZONE-CLOCK"))

        element = ET.Element("TIMING-CLOCK-SYNC-ACCURACY")
        ARXMLWriter().writeTimingClockSyncAccuracy(element, accuracy)
        assert element.find("SHORT-NAME").text == "Sync1"
        accuracy_tag = element.find("ACCURACY")
        assert accuracy_tag is not None
        assert accuracy_tag.find("CSE-CODE-FACTOR").text == "10"
        lower_ref = element.find("LOWER-REF")
        assert lower_ref.text == "/AUTOSAR/TargetClock"
        assert lower_ref.attrib["DEST"] == "TDLET-ZONE-CLOCK"
        upper_ref = element.find("UPPER-REF")
        assert upper_ref.text == "/AUTOSAR/SourceClock"

        reloaded = TimingClockSyncAccuracy(parent, "Sync1")
        ARXMLParser().readTimingClockSyncAccuracy(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Sync1"
        assert reloaded.getAccuracy().getCseCodeFactor().getValue() == 10
        assert reloaded.getLowerRef().getValue() == "/AUTOSAR/TargetClock"
        assert reloaded.getLowerRef().getDest() == "TDLET-ZONE-CLOCK"
        assert reloaded.getUpperRef().getValue() == "/AUTOSAR/SourceClock"
        assert reloaded.getUpperRef().getDest() == "TDLET-ZONE-CLOCK"

    def test_write_timing_clock_sync_accuracy_empty(self):
        parent = self._parent()
        accuracy = TimingClockSyncAccuracy(parent, "Sync1")

        element = ET.Element("TIMING-CLOCK-SYNC-ACCURACY")
        ARXMLWriter().writeTimingClockSyncAccuracy(element, accuracy)
        assert element.find("SHORT-NAME").text == "Sync1"
        assert element.find("ACCURACY") is None
        assert element.find("LOWER-REF") is None
        assert element.find("UPPER-REF") is None

        reloaded = TimingClockSyncAccuracy(parent, "Sync1")
        ARXMLParser().readTimingClockSyncAccuracy(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Sync1"
        assert reloaded.getAccuracy() is None
        assert reloaded.getLowerRef() is None
        assert reloaded.getUpperRef() is None


class TestWriteTimingClockBase:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_timing_clock_platform_time_base(self):
        from tests.test_armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.test_TimingClock import (
            ConcreteTimingClock as TestClock,
        )

        parent = self._parent()
        clock = TestClock(parent, "Clock1")
        clock.setPlatformTimeBaseRef(RefType().setValue("/AUTOSAR/TimeDomain").setDest("GLOBAL-TIME-DOMAIN"))

        element = ET.Element("TDLET-ZONE-CLOCK")
        ARXMLWriter().writeTimingClock(element, clock)
        assert element.find("SHORT-NAME").text == "Clock1"
        platform_time_bases = element.find("PLATFORM-TIME-BASES")
        assert platform_time_bases is not None
        domain_ref = platform_time_bases.find("GLOBAL-TIME-DOMAIN-REF-CONDITIONAL/GLOBAL-TIME-DOMAIN-REF")
        assert domain_ref is not None
        assert domain_ref.text == "/AUTOSAR/TimeDomain"

        reloaded = TestClock(parent, "Clock1")
        ARXMLParser().readTimingClock(_round_trip(element), reloaded)
        assert reloaded.getPlatformTimeBaseRef().getValue() == "/AUTOSAR/TimeDomain"
        assert reloaded.getPlatformTimeBaseRef().getDest() == "GLOBAL-TIME-DOMAIN"

    def test_write_timing_clock_no_platform_time_base_wrapper_when_unset(self):
        from tests.test_armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.test_TimingClock import (
            ConcreteTimingClock as TestClock,
        )

        parent = self._parent()
        clock = TestClock(parent, "Clock1")

        element = ET.Element("TDLET-ZONE-CLOCK")
        ARXMLWriter().writeTimingClock(element, clock)
        assert element.find("PLATFORM-TIME-BASES") is None

        reloaded = TestClock(parent, "Clock1")
        ARXMLParser().readTimingClock(_round_trip(element), reloaded)
        assert reloaded.getPlatformTimeBaseRef() is None
