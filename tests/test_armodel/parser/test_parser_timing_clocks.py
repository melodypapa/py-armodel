"""Parser tests for the timing constraint base class and timing clocks (TIMING-CONSTRAINT, TIMING-CLOCK, TDLET-ZONE-CLOCK, TIMING-CLOCK-SYNC-ACCURACY)."""

import xml.etree.ElementTree as ET

import pytest

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
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteTimingConstraint(TimingConstraint):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent():
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


class TestReadTimingConstraint:
    def test_read_timing_constraint_full(self, parser):
        parent = _parent()
        constraint = ConcreteTimingConstraint(parent, "Constraint1")
        element = ET.fromstring(
            f"<EXECUTION-TIME-CONSTRAINT xmlns='{NS}'>"
            "<SHORT-NAME>Constraint1</SHORT-NAME>"
            "<TRACE-REFS>"
            "<TRACE-REF>/AUTOSAR/Requirement1</TRACE-REF>"
            "</TRACE-REFS>"
            "<TIMING-CONDITION-REF DEST='TIMING-CONDITION'>/AUTOSAR/Condition</TIMING-CONDITION-REF>"
            "</EXECUTION-TIME-CONSTRAINT>"
        )
        parser.readTimingConstraint(element, constraint)
        assert constraint.getShortName() == "Constraint1"
        assert constraint.getTimingConditionRef() is not None
        assert constraint.getTimingConditionRef().getValue() == "/AUTOSAR/Condition"
        assert constraint.getTimingConditionRef().getDest() == "TIMING-CONDITION"
        trace_refs = constraint.getTraceRefs()
        assert len(trace_refs) == 1
        assert trace_refs[0].getValue() == "/AUTOSAR/Requirement1"

    def test_read_timing_constraint_empty(self, parser):
        parent = _parent()
        constraint = ConcreteTimingConstraint(parent, "Constraint1")
        element = ET.fromstring(f"<EXECUTION-TIME-CONSTRAINT xmlns='{NS}'>" "<SHORT-NAME>Constraint1</SHORT-NAME>" "</EXECUTION-TIME-CONSTRAINT>")
        parser.readTimingConstraint(element, constraint)
        assert constraint.getShortName() == "Constraint1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getTraceRefs() == []


class TestReadTimingClock:
    def test_read_tdlet_zone_clock_full(self, parser):
        parent = _parent()
        clock = TDLETZoneClock(parent, "Zone1")
        element = ET.fromstring(
            f"<TDLET-ZONE-CLOCK xmlns='{NS}'>"
            "<SHORT-NAME>Zone1</SHORT-NAME>"
            "<PLATFORM-TIME-BASES>"
            "<GLOBAL-TIME-DOMAIN-REF-CONDITIONAL>"
            "<GLOBAL-TIME-DOMAIN-REF DEST='GLOBAL-TIME-DOMAIN'>/AUTOSAR/TimeDomain</GLOBAL-TIME-DOMAIN-REF>"
            "</GLOBAL-TIME-DOMAIN-REF-CONDITIONAL>"
            "</PLATFORM-TIME-BASES>"
            "<ACCURACY-EXT>"
            "<CSE-CODE>0</CSE-CODE>"
            "<CSE-CODE-FACTOR>30</CSE-CODE-FACTOR>"
            "</ACCURACY-EXT>"
            "<ACCURACY-INT>"
            "<CSE-CODE>0</CSE-CODE>"
            "<CSE-CODE-FACTOR>50</CSE-CODE-FACTOR>"
            "</ACCURACY-INT>"
            "</TDLET-ZONE-CLOCK>"
        )
        parser.readTDLETZoneClock(element, clock)
        assert clock.getShortName() == "Zone1"
        assert clock.getPlatformTimeBaseRef() is not None
        assert clock.getPlatformTimeBaseRef().getValue() == "/AUTOSAR/TimeDomain"
        assert clock.getPlatformTimeBaseRef().getDest() == "GLOBAL-TIME-DOMAIN"
        ext = clock.getAccuracyExt()
        assert ext is not None
        assert ext.getCseCode().getValue() == "0"
        assert ext.getCseCodeFactor().getValue() == 30
        internal = clock.getAccuracyInt()
        assert internal is not None
        assert internal.getCseCodeFactor().getValue() == 50

    def test_read_tdlet_zone_clock_empty(self, parser):
        parent = _parent()
        clock = TDLETZoneClock(parent, "Zone1")
        element = ET.fromstring(f"<TDLET-ZONE-CLOCK xmlns='{NS}'>" "<SHORT-NAME>Zone1</SHORT-NAME>" "</TDLET-ZONE-CLOCK>")
        parser.readTDLETZoneClock(element, clock)
        assert clock.getShortName() == "Zone1"
        assert clock.getPlatformTimeBaseRef() is None
        assert clock.getAccuracyExt() is None
        assert clock.getAccuracyInt() is None


class TestReadTimingClockSyncAccuracy:
    def test_read_timing_clock_sync_accuracy_full(self, parser):
        parent = _parent()
        accuracy = TimingClockSyncAccuracy(parent, "Sync1")
        element = ET.fromstring(
            f"<TIMING-CLOCK-SYNC-ACCURACY xmlns='{NS}'>"
            "<SHORT-NAME>Sync1</SHORT-NAME>"
            "<ACCURACY>"
            "<CSE-CODE>0</CSE-CODE>"
            "<CSE-CODE-FACTOR>10</CSE-CODE-FACTOR>"
            "</ACCURACY>"
            "<LOWER-REF DEST='TDLET-ZONE-CLOCK'>/AUTOSAR/TargetClock</LOWER-REF>"
            "<UPPER-REF DEST='TDLET-ZONE-CLOCK'>/AUTOSAR/SourceClock</UPPER-REF>"
            "</TIMING-CLOCK-SYNC-ACCURACY>"
        )
        parser.readTimingClockSyncAccuracy(element, accuracy)
        assert accuracy.getShortName() == "Sync1"
        value = accuracy.getAccuracy()
        assert value is not None
        assert value.getCseCode().getValue() == "0"
        assert value.getCseCodeFactor().getValue() == 10
        assert accuracy.getLowerRef().getValue() == "/AUTOSAR/TargetClock"
        assert accuracy.getLowerRef().getDest() == "TDLET-ZONE-CLOCK"
        assert accuracy.getUpperRef().getValue() == "/AUTOSAR/SourceClock"

    def test_read_timing_clock_sync_accuracy_empty(self, parser):
        parent = _parent()
        accuracy = TimingClockSyncAccuracy(parent, "Sync1")
        element = ET.fromstring(f"<TIMING-CLOCK-SYNC-ACCURACY xmlns='{NS}'>" "<SHORT-NAME>Sync1</SHORT-NAME>" "</TIMING-CLOCK-SYNC-ACCURACY>")
        parser.readTimingClockSyncAccuracy(element, accuracy)
        assert accuracy.getShortName() == "Sync1"
        assert accuracy.getAccuracy() is None
        assert accuracy.getLowerRef() is None
        assert accuracy.getUpperRef() is None
