"""Parser tests for the timing constraints (AGE-CONSTRAINT, LATENCY-TIMING-CONSTRAINT, OFFSET-TIMING-CONSTRAINT, SYNCHRONIZATION-TIMING-CONSTRAINT, event triggering constraints)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import AgeConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    PeriodicEventTriggering,
    SporadicEventTriggering,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import (
    OffsetTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
    SynchronizationTimingConstraint,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


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


class TestReadTimingConstraints:
    def test_read_age_constraint(self, parser):
        parent = _parent()
        constraint = AgeConstraint(parent, "Age1")
        element = ET.fromstring(
            f"<AGE-CONSTRAINT xmlns='{NS}'>"
            "<SHORT-NAME>Age1</SHORT-NAME>"
            "<MAXIMUM><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>100</CSE-CODE-FACTOR></MAXIMUM>"
            "<MINIMUM><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>20</CSE-CODE-FACTOR></MINIMUM>"
            "<SCOPE-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/TdEvent</SCOPE-REF>"
            "</AGE-CONSTRAINT>"
        )
        parser.readAgeConstraint(element, constraint)
        assert constraint.getShortName() == "Age1"
        assert constraint.getMaximum().getCseCode().getValue() == "0"
        assert constraint.getMaximum().getCseCodeFactor().getValue() == 100
        assert constraint.getMinimum().getCseCodeFactor().getValue() == 20
        assert constraint.getScopeRef().getValue() == "/AUTOSAR/TdEvent"
        assert constraint.getScopeRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_read_latency_timing_constraint(self, parser):
        parent = _parent()
        constraint = LatencyTimingConstraint(parent, "Latency1")
        element = ET.fromstring(
            f"<LATENCY-TIMING-CONSTRAINT xmlns='{NS}'>"
            "<SHORT-NAME>Latency1</SHORT-NAME>"
            "<LATENCY-CONSTRAINT-TYPE>REACTION</LATENCY-CONSTRAINT-TYPE>"
            "<SCOPE-REF DEST='TIMING-DESCRIPTION-EVENT-CHAIN'>/AUTOSAR/Chain</SCOPE-REF>"
            "<MINIMUM><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>10</CSE-CODE-FACTOR></MINIMUM>"
            "<MAXIMUM><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>20</CSE-CODE-FACTOR></MAXIMUM>"
            "<NOMINAL><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>15</CSE-CODE-FACTOR></NOMINAL>"
            "</LATENCY-TIMING-CONSTRAINT>"
        )
        parser.readLatencyTimingConstraint(element, constraint)
        assert constraint.getShortName() == "Latency1"
        assert constraint.getLatencyConstraintType().getValue() == "REACTION"
        assert constraint.getScopeRef().getValue() == "/AUTOSAR/Chain"
        assert constraint.getScopeRef().getDest() == "TIMING-DESCRIPTION-EVENT-CHAIN"
        assert constraint.getMinimum().getCseCodeFactor().getValue() == 10
        assert constraint.getMaximum().getCseCodeFactor().getValue() == 20
        assert constraint.getNominal().getCseCodeFactor().getValue() == 15

    def test_read_offset_timing_constraint(self, parser):
        parent = _parent()
        constraint = OffsetTimingConstraint(parent, "Offset1")
        element = ET.fromstring(
            f"<OFFSET-TIMING-CONSTRAINT xmlns='{NS}'>"
            "<SHORT-NAME>Offset1</SHORT-NAME>"
            "<SOURCE-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/SrcEvent</SOURCE-REF>"
            "<TARGET-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/TgtEvent</TARGET-REF>"
            "<MINIMUM><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>10</CSE-CODE-FACTOR></MINIMUM>"
            "<MAXIMUM><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>20</CSE-CODE-FACTOR></MAXIMUM>"
            "</OFFSET-TIMING-CONSTRAINT>"
        )
        parser.readOffsetTimingConstraint(element, constraint)
        assert constraint.getShortName() == "Offset1"
        assert constraint.getSourceRef().getValue() == "/AUTOSAR/SrcEvent"
        assert constraint.getTargetRef().getValue() == "/AUTOSAR/TgtEvent"
        assert constraint.getMinimum().getCseCodeFactor().getValue() == 10
        assert constraint.getMaximum().getCseCodeFactor().getValue() == 20

    def test_read_synchronization_timing_constraint(self, parser):
        parent = _parent()
        constraint = SynchronizationTimingConstraint(parent, "Sync1")
        element = ET.fromstring(
            f"<SYNCHRONIZATION-TIMING-CONSTRAINT xmlns='{NS}'>"
            "<SHORT-NAME>Sync1</SHORT-NAME>"
            "<EVENT-OCCURRENCE-KIND>SINGLE-OCCURRENCE</EVENT-OCCURRENCE-KIND>"
            "<SCOPE-EVENT-REFS>"
            "<SCOPE-EVENT-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/Evt1</SCOPE-EVENT-REF>"
            "<SCOPE-EVENT-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/Evt2</SCOPE-EVENT-REF>"
            "</SCOPE-EVENT-REFS>"
            "<SCOPE-REFS>"
            "<SCOPE-REF DEST='TIMING-DESCRIPTION-EVENT-CHAIN'>/AUTOSAR/Chain1</SCOPE-REF>"
            "</SCOPE-REFS>"
            "<SYNCHRONIZATION-CONSTRAINT-TYPE>RESPONSE-SYNCHRONIZATION</SYNCHRONIZATION-CONSTRAINT-TYPE>"
            "<TOLERANCE><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>500</CSE-CODE-FACTOR></TOLERANCE>"
            "</SYNCHRONIZATION-TIMING-CONSTRAINT>"
        )
        parser.readSynchronizationTimingConstraint(element, constraint)
        assert constraint.getShortName() == "Sync1"
        assert constraint.getEventOccurrenceKind().getValue() == "SINGLE-OCCURRENCE"
        events = constraint.getScopeEvents()
        assert len(events) == 2
        assert events[0].getValue() == "/AUTOSAR/Evt1"
        assert events[1].getDest() == "TIMING-DESCRIPTION-EVENT"
        chains = constraint.getScopes()
        assert len(chains) == 1
        assert chains[0].getValue() == "/AUTOSAR/Chain1"
        assert chains[0].getDest() == "TIMING-DESCRIPTION-EVENT-CHAIN"
        assert constraint.getSynchronizationConstraintType().getValue() == "RESPONSE-SYNCHRONIZATION"
        assert constraint.getTolerance().getCseCodeFactor().getValue() == 500

    def test_read_constraints_inherit_timing_condition_ref(self, parser):
        parent = _parent()
        constraint = AgeConstraint(parent, "Age1")
        element = ET.fromstring(
            f"<AGE-CONSTRAINT xmlns='{NS}'>" "<SHORT-NAME>Age1</SHORT-NAME>" "<TIMING-CONDITION-REF DEST='TIMING-CONDITION'>/AUTOSAR/Cond1</TIMING-CONDITION-REF>" "</AGE-CONSTRAINT>"
        )
        parser.readAgeConstraint(element, constraint)
        assert constraint.getTimingConditionRef().getValue() == "/AUTOSAR/Cond1"
        assert constraint.getTimingConditionRef().getDest() == "TIMING-CONDITION"

    def test_read_periodic_event_triggering(self, parser):
        parent = _parent()
        constraint = PeriodicEventTriggering(parent, "Periodic1")
        element = ET.fromstring(
            f"<PERIODIC-EVENT-TRIGGERING xmlns='{NS}'>"
            "<SHORT-NAME>Periodic1</SHORT-NAME>"
            "<EVENT-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/TdEvent</EVENT-REF>"
            "<MINIMUM-INTER-ARRIVAL-TIME><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>10</CSE-CODE-FACTOR></MINIMUM-INTER-ARRIVAL-TIME>"
            "<JITTER><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>20</CSE-CODE-FACTOR></JITTER>"
            "<PERIOD><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>30</CSE-CODE-FACTOR></PERIOD>"
            "</PERIODIC-EVENT-TRIGGERING>"
        )
        parser.readPeriodicEventTriggering(element, constraint)
        assert constraint.getShortName() == "Periodic1"
        assert constraint.getEventRef().getValue() == "/AUTOSAR/TdEvent"
        assert constraint.getEventRef().getDest() == "TIMING-DESCRIPTION-EVENT"
        assert constraint.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 10
        assert constraint.getJitter().getCseCodeFactor().getValue() == 20
        assert constraint.getPeriod().getCseCodeFactor().getValue() == 30

    def test_read_sporadic_event_triggering(self, parser):
        parent = _parent()
        constraint = SporadicEventTriggering(parent, "Sporadic1")
        element = ET.fromstring(
            f"<SPORADIC-EVENT-TRIGGERING xmlns='{NS}'>"
            "<SHORT-NAME>Sporadic1</SHORT-NAME>"
            "<MINIMUM-INTER-ARRIVAL-TIME><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>10</CSE-CODE-FACTOR></MINIMUM-INTER-ARRIVAL-TIME>"
            "<MAXIMUM-INTER-ARRIVAL-TIME><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>20</CSE-CODE-FACTOR></MAXIMUM-INTER-ARRIVAL-TIME>"
            "<JITTER><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>30</CSE-CODE-FACTOR></JITTER>"
            "<PERIOD><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>40</CSE-CODE-FACTOR></PERIOD>"
            "</SPORADIC-EVENT-TRIGGERING>"
        )
        parser.readSporadicEventTriggering(element, constraint)
        assert constraint.getShortName() == "Sporadic1"
        assert constraint.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 10
        assert constraint.getMaximumInterArrivalTime().getCseCodeFactor().getValue() == 20
        assert constraint.getJitter().getCseCodeFactor().getValue() == 30
        assert constraint.getPeriod().getCseCodeFactor().getValue() == 40

    def test_read_concrete_pattern_event_triggering(self, parser):
        parent = _parent()
        constraint = ConcretePatternEventTriggering(parent, "Concrete1")
        element = ET.fromstring(
            f"<CONCRETE-PATTERN-EVENT-TRIGGERING xmlns='{NS}'>"
            "<SHORT-NAME>Concrete1</SHORT-NAME>"
            "<PATTERN-JITTER><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>2</CSE-CODE-FACTOR></PATTERN-JITTER>"
            "<PATTERN-PERIOD><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>200</CSE-CODE-FACTOR></PATTERN-PERIOD>"
            "<OFFSETS>"
            "<TIME-VALUE><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>5</CSE-CODE-FACTOR></TIME-VALUE>"
            "<TIME-VALUE><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>15</CSE-CODE-FACTOR></TIME-VALUE>"
            "</OFFSETS>"
            "<PATTERN-LENGTH><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>100</CSE-CODE-FACTOR></PATTERN-LENGTH>"
            "</CONCRETE-PATTERN-EVENT-TRIGGERING>"
        )
        parser.readConcretePatternEventTriggering(element, constraint)
        assert constraint.getShortName() == "Concrete1"
        offsets = constraint.getOffsets()
        assert len(offsets) == 2
        assert offsets[0].getCseCodeFactor().getValue() == 5
        assert offsets[1].getCseCodeFactor().getValue() == 15
        assert constraint.getPatternJitter().getCseCodeFactor().getValue() == 2
        assert constraint.getPatternLength().getCseCodeFactor().getValue() == 100
        assert constraint.getPatternPeriod().getCseCodeFactor().getValue() == 200

    def test_read_burst_pattern_event_triggering(self, parser):
        parent = _parent()
        constraint = BurstPatternEventTriggering(parent, "Burst1")
        element = ET.fromstring(
            f"<BURST-PATTERN-EVENT-TRIGGERING xmlns='{NS}'>"
            "<SHORT-NAME>Burst1</SHORT-NAME>"
            "<MAX-NUMBER-OF-OCCURRENCES>10</MAX-NUMBER-OF-OCCURRENCES>"
            "<MINIMUM-INTER-ARRIVAL-TIME><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>5</CSE-CODE-FACTOR></MINIMUM-INTER-ARRIVAL-TIME>"
            "<PATTERN-JITTER><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>1</CSE-CODE-FACTOR></PATTERN-JITTER>"
            "<PATTERN-LENGTH><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>50</CSE-CODE-FACTOR></PATTERN-LENGTH>"
            "<PATTERN-PERIOD><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>80</CSE-CODE-FACTOR></PATTERN-PERIOD>"
            "<MIN-NUMBER-OF-OCCURRENCES>3</MIN-NUMBER-OF-OCCURRENCES>"
            "</BURST-PATTERN-EVENT-TRIGGERING>"
        )
        parser.readBurstPatternEventTriggering(element, constraint)
        assert constraint.getShortName() == "Burst1"
        assert constraint.getMaxNumberOfOccurrences().getValue() == 10
        assert constraint.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 5
        assert constraint.getMinNumberOfOccurrences().getValue() == 3
        assert constraint.getPatternJitter().getCseCodeFactor().getValue() == 1
        assert constraint.getPatternLength().getCseCodeFactor().getValue() == 50
        assert constraint.getPatternPeriod().getCseCodeFactor().getValue() == 80

    def test_read_arbitrary_event_triggering(self, parser):
        parent = _parent()
        constraint = ArbitraryEventTriggering(parent, "Arbitrary1")
        element = ET.fromstring(
            f"<ARBITRARY-EVENT-TRIGGERING xmlns='{NS}'>"
            "<SHORT-NAME>Arbitrary1</SHORT-NAME>"
            "<EVENT-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/TdEvent</EVENT-REF>"
            "<MINIMUM-DISTANCES>"
            "<TIME-VALUE><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>10</CSE-CODE-FACTOR></TIME-VALUE>"
            "<TIME-VALUE><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>12</CSE-CODE-FACTOR></TIME-VALUE>"
            "</MINIMUM-DISTANCES>"
            "<MAXIMUM-DISTANCES>"
            "<TIME-VALUE><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>20</CSE-CODE-FACTOR></TIME-VALUE>"
            "</MAXIMUM-DISTANCES>"
            "<CONFIDENCE-INTERVALS>"
            "<CONFIDENCE-INTERVAL>"
            "<LOWER-BOUND><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>8</CSE-CODE-FACTOR></LOWER-BOUND>"
            "<PROPABILITY>0.95</PROPABILITY>"
            "<UPPER-BOUND><CSE-CODE>0</CSE-CODE><CSE-CODE-FACTOR>80</CSE-CODE-FACTOR></UPPER-BOUND>"
            "</CONFIDENCE-INTERVAL>"
            "</CONFIDENCE-INTERVALS>"
            "</ARBITRARY-EVENT-TRIGGERING>"
        )
        parser.readArbitraryEventTriggering(element, constraint)
        assert constraint.getShortName() == "Arbitrary1"
        assert constraint.getEventRef().getValue() == "/AUTOSAR/TdEvent"
        min_distances = constraint.getMinimumDistances()
        assert len(min_distances) == 2
        assert min_distances[0].getCseCodeFactor().getValue() == 10
        assert min_distances[1].getCseCodeFactor().getValue() == 12
        max_distances = constraint.getMaximumDistances()
        assert len(max_distances) == 1
        assert max_distances[0].getCseCodeFactor().getValue() == 20
        intervals = constraint.getConfidenceIntervals()
        assert len(intervals) == 1
        assert intervals[0].getLowerBound().getCseCodeFactor().getValue() == 8
        assert intervals[0].getPropability().getValue() == 0.95
        assert intervals[0].getUpperBound().getCseCodeFactor().getValue() == 80
