"""Writer round-trip tests for the timing constraints (AGE-CONSTRAINT, LATENCY-TIMING-CONSTRAINT, OFFSET-TIMING-CONSTRAINT, SYNCHRONIZATION-TIMING-CONSTRAINT, event triggering constraints)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import AgeConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    ConfidenceInterval,
    PeriodicEventTriggering,
    SporadicEventTriggering,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyConstraintTypeEnum,
    LatencyTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import (
    OffsetTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
    EventOccurrenceKindEnum,
    SynchronizationTimingConstraint,
    SynchronizationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Float,
    Integer,
    PositiveInteger,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    if xml_str.rstrip().endswith("/>"):
        xml_str = xml_str.rstrip()[:-2].rstrip() + ' xmlns="http://autosar.org/schema/r4.0"/>'
    else:
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
    return ET.fromstring(xml_str)


def _mdt(cse_code: str = "0", factor: str = "50") -> MultidimensionalTime:
    mdt = MultidimensionalTime()
    mdt.setCseCode(CseCodeType().setValue(cse_code))
    mdt.setCseCodeFactor(Integer().setValue(factor))
    return mdt


class TestWriteAgeConstraint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_age_constraint(self):
        parent = self._parent()
        constraint = AgeConstraint(parent, "Age1")
        constraint.setMaximum(_mdt("0", "100"))
        constraint.setMinimum(_mdt("0", "20"))
        constraint.setScopeRef(RefType().setValue("/AUTOSAR/TdEvent").setDest("TIMING-DESCRIPTION-EVENT"))

        element = ET.Element("AGE-CONSTRAINT")
        ARXMLWriter().writeAgeConstraint(element, constraint)
        maximum_idx = list(element).index(element.find("MAXIMUM"))
        minimum_idx = list(element).index(element.find("MINIMUM"))
        assert maximum_idx < minimum_idx
        assert element.find("MAXIMUM/CSE-CODE").text == "0"
        assert element.find("MAXIMUM/CSE-CODE-FACTOR").text == "100"
        assert element.find("MINIMUM/CSE-CODE-FACTOR").text == "20"
        assert element.find("SCOPE-REF").text == "/AUTOSAR/TdEvent"
        assert element.find("SCOPE-REF").attrib["DEST"] == "TIMING-DESCRIPTION-EVENT"

        reloaded = AgeConstraint(parent, "Age1")
        ARXMLParser().readAgeConstraint(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Age1"
        assert reloaded.getMaximum().getCseCode().getValue() == "0"
        assert reloaded.getMaximum().getCseCodeFactor().getValue() == 100
        assert reloaded.getMinimum().getCseCodeFactor().getValue() == 20
        assert reloaded.getScopeRef().getValue() == "/AUTOSAR/TdEvent"
        assert reloaded.getScopeRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_write_age_constraint_empty(self):
        parent = self._parent()
        constraint = AgeConstraint(parent, "Age1")

        element = ET.Element("AGE-CONSTRAINT")
        ARXMLWriter().writeAgeConstraint(element, constraint)
        assert element.find("MAXIMUM") is None
        assert element.find("MINIMUM") is None
        assert element.find("SCOPE-REF") is None
        assert element.find("TIMING-CONDITION-REF") is None

        reloaded = AgeConstraint(parent, "Age1")
        ARXMLParser().readAgeConstraint(_round_trip(element), reloaded)
        assert reloaded.getMaximum() is None
        assert reloaded.getMinimum() is None
        assert reloaded.getScopeRef() is None

    def test_round_trip_age_constraint_inherits_timing_condition_ref(self):
        parent = self._parent()
        constraint = AgeConstraint(parent, "Age1")
        constraint.setTimingConditionRef(RefType().setValue("/AUTOSAR/Cond1").setDest("TIMING-CONDITION"))

        element = ET.Element("AGE-CONSTRAINT")
        ARXMLWriter().writeAgeConstraint(element, constraint)

        reloaded = AgeConstraint(parent, "Age1")
        ARXMLParser().readAgeConstraint(_round_trip(element), reloaded)
        assert reloaded.getTimingConditionRef().getValue() == "/AUTOSAR/Cond1"
        assert reloaded.getTimingConditionRef().getDest() == "TIMING-CONDITION"


class TestWriteLatencyTimingConstraint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_latency_timing_constraint(self):
        parent = self._parent()
        constraint = LatencyTimingConstraint(parent, "Latency1")
        constraint.setLatencyConstraintType(LatencyConstraintTypeEnum().setValue(LatencyConstraintTypeEnum.REACTION))
        constraint.setMinimum(_mdt("0", "10"))
        constraint.setMaximum(_mdt("0", "20"))
        constraint.setNominal(_mdt("0", "15"))
        constraint.setScopeRef(RefType().setValue("/AUTOSAR/Chain").setDest("TIMING-DESCRIPTION-EVENT-CHAIN"))

        element = ET.Element("LATENCY-TIMING-CONSTRAINT")
        ARXMLWriter().writeLatencyTimingConstraint(element, constraint)
        type_idx = list(element).index(element.find("LATENCY-CONSTRAINT-TYPE"))
        scope_idx = list(element).index(element.find("SCOPE-REF"))
        min_idx = list(element).index(element.find("MINIMUM"))
        max_idx = list(element).index(element.find("MAXIMUM"))
        nom_idx = list(element).index(element.find("NOMINAL"))
        assert type_idx < scope_idx < min_idx < max_idx < nom_idx
        assert element.find("LATENCY-CONSTRAINT-TYPE").text == "reaction"

        reloaded = LatencyTimingConstraint(parent, "Latency1")
        ARXMLParser().readLatencyTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Latency1"
        assert reloaded.getLatencyConstraintType() is not None
        assert reloaded.getLatencyConstraintType().getValue() == "reaction"
        assert reloaded.getMinimum().getCseCodeFactor().getValue() == 10
        assert reloaded.getMaximum().getCseCodeFactor().getValue() == 20
        assert reloaded.getNominal().getCseCodeFactor().getValue() == 15
        assert reloaded.getScopeRef().getValue() == "/AUTOSAR/Chain"
        assert reloaded.getScopeRef().getDest() == "TIMING-DESCRIPTION-EVENT-CHAIN"

    def test_write_latency_timing_constraint_empty(self):
        parent = self._parent()
        constraint = LatencyTimingConstraint(parent, "Latency1")

        element = ET.Element("LATENCY-TIMING-CONSTRAINT")
        ARXMLWriter().writeLatencyTimingConstraint(element, constraint)
        assert element.find("LATENCY-CONSTRAINT-TYPE") is None
        assert element.find("SCOPE-REF") is None
        assert element.find("MINIMUM") is None
        assert element.find("MAXIMUM") is None
        assert element.find("NOMINAL") is None

        reloaded = LatencyTimingConstraint(parent, "Latency1")
        ARXMLParser().readLatencyTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getLatencyConstraintType() is None
        assert reloaded.getScopeRef() is None
        assert reloaded.getMinimum() is None
        assert reloaded.getMaximum() is None
        assert reloaded.getNominal() is None


class TestWriteOffsetTimingConstraint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_offset_timing_constraint(self):
        parent = self._parent()
        constraint = OffsetTimingConstraint(parent, "Offset1")
        constraint.setMinimum(_mdt("0", "10"))
        constraint.setMaximum(_mdt("0", "20"))
        constraint.setSourceRef(RefType().setValue("/AUTOSAR/SrcEvent").setDest("TIMING-DESCRIPTION-EVENT"))
        constraint.setTargetRef(RefType().setValue("/AUTOSAR/TgtEvent").setDest("TIMING-DESCRIPTION-EVENT"))

        element = ET.Element("OFFSET-TIMING-CONSTRAINT")
        ARXMLWriter().writeOffsetTimingConstraint(element, constraint)
        source_idx = list(element).index(element.find("SOURCE-REF"))
        target_idx = list(element).index(element.find("TARGET-REF"))
        min_idx = list(element).index(element.find("MINIMUM"))
        max_idx = list(element).index(element.find("MAXIMUM"))
        assert source_idx < target_idx < min_idx < max_idx

        reloaded = OffsetTimingConstraint(parent, "Offset1")
        ARXMLParser().readOffsetTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Offset1"
        assert reloaded.getMinimum().getCseCodeFactor().getValue() == 10
        assert reloaded.getMaximum().getCseCodeFactor().getValue() == 20
        assert reloaded.getSourceRef().getValue() == "/AUTOSAR/SrcEvent"
        assert reloaded.getSourceRef().getDest() == "TIMING-DESCRIPTION-EVENT"
        assert reloaded.getTargetRef().getValue() == "/AUTOSAR/TgtEvent"
        assert reloaded.getTargetRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_write_offset_timing_constraint_empty(self):
        parent = self._parent()
        constraint = OffsetTimingConstraint(parent, "Offset1")

        element = ET.Element("OFFSET-TIMING-CONSTRAINT")
        ARXMLWriter().writeOffsetTimingConstraint(element, constraint)
        assert element.find("SOURCE-REF") is None
        assert element.find("TARGET-REF") is None
        assert element.find("MINIMUM") is None
        assert element.find("MAXIMUM") is None

        reloaded = OffsetTimingConstraint(parent, "Offset1")
        ARXMLParser().readOffsetTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getSourceRef() is None
        assert reloaded.getTargetRef() is None
        assert reloaded.getMinimum() is None
        assert reloaded.getMaximum() is None


class TestWriteSynchronizationTimingConstraint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_synchronization_timing_constraint_full(self):
        parent = self._parent()
        constraint = SynchronizationTimingConstraint(parent, "Sync1")
        constraint.setEventOccurrenceKind(EventOccurrenceKindEnum().setValue(EventOccurrenceKindEnum.SINGLE_OCCURRENCE))
        constraint.addScope(RefType().setValue("/AUTOSAR/Chain1").setDest("TIMING-DESCRIPTION-EVENT-CHAIN"))
        constraint.addScope(RefType().setValue("/AUTOSAR/Chain2").setDest("TIMING-DESCRIPTION-EVENT-CHAIN"))
        constraint.addScopeEvent(RefType().setValue("/AUTOSAR/Evt1").setDest("TIMING-DESCRIPTION-EVENT"))
        constraint.addScopeEvent(RefType().setValue("/AUTOSAR/Evt2").setDest("TIMING-DESCRIPTION-EVENT"))
        constraint.addScopeEvent(RefType().setValue("/AUTOSAR/Evt3").setDest("TIMING-DESCRIPTION-EVENT"))
        constraint.setSynchronizationConstraintType(SynchronizationTypeEnum().setValue(SynchronizationTypeEnum.RESPONSE_SYNCHRONIZATION))
        constraint.setTolerance(_mdt("0", "500"))

        element = ET.Element("SYNCHRONIZATION-TIMING-CONSTRAINT")
        ARXMLWriter().writeSynchronizationTimingConstraint(element, constraint)
        kind_idx = list(element).index(element.find("EVENT-OCCURRENCE-KIND"))
        scope_events_idx = list(element).index(element.find("SCOPE-EVENT-REFS"))
        scopes_idx = list(element).index(element.find("SCOPE-REFS"))
        sync_type_idx = list(element).index(element.find("SYNCHRONIZATION-CONSTRAINT-TYPE"))
        tolerance_idx = list(element).index(element.find("TOLERANCE"))
        assert kind_idx < scope_events_idx < scopes_idx < sync_type_idx < tolerance_idx
        assert element.find("EVENT-OCCURRENCE-KIND").text == "singleOccurrence"
        assert element.find("SYNCHRONIZATION-CONSTRAINT-TYPE").text == "responseSynchronization"
        scope_event_refs = element.findall("SCOPE-EVENT-REFS/SCOPE-EVENT-REF")
        assert len(scope_event_refs) == 3
        assert scope_event_refs[0].text == "/AUTOSAR/Evt1"
        assert scope_event_refs[0].attrib["DEST"] == "TIMING-DESCRIPTION-EVENT"
        scope_refs = element.findall("SCOPE-REFS/SCOPE-REF")
        assert len(scope_refs) == 2
        assert scope_refs[1].text == "/AUTOSAR/Chain2"
        assert scope_refs[1].attrib["DEST"] == "TIMING-DESCRIPTION-EVENT-CHAIN"

        reloaded = SynchronizationTimingConstraint(parent, "Sync1")
        ARXMLParser().readSynchronizationTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Sync1"
        assert reloaded.getEventOccurrenceKind() is not None
        assert reloaded.getEventOccurrenceKind().getValue() == "singleOccurrence"
        assert reloaded.getSynchronizationConstraintType() is not None
        assert reloaded.getSynchronizationConstraintType().getValue() == "responseSynchronization"
        events = reloaded.getScopeEvents()
        assert len(events) == 3
        assert events[0].getValue() == "/AUTOSAR/Evt1"
        assert events[0].getDest() == "TIMING-DESCRIPTION-EVENT"
        assert events[2].getValue() == "/AUTOSAR/Evt3"
        chains = reloaded.getScopes()
        assert len(chains) == 2
        assert chains[0].getValue() == "/AUTOSAR/Chain1"
        assert chains[1].getDest() == "TIMING-DESCRIPTION-EVENT-CHAIN"
        assert reloaded.getTolerance() is not None
        assert reloaded.getTolerance().getCseCodeFactor().getValue() == 500

    def test_write_synchronization_timing_constraint_empty_wrapper_lists(self):
        parent = self._parent()
        constraint = SynchronizationTimingConstraint(parent, "Sync1")

        element = ET.Element("SYNCHRONIZATION-TIMING-CONSTRAINT")
        ARXMLWriter().writeSynchronizationTimingConstraint(element, constraint)
        assert element.find("EVENT-OCCURRENCE-KIND") is None
        assert element.find("SCOPE-EVENT-REFS") is None
        assert element.find("SCOPE-REFS") is None
        assert element.find("SYNCHRONIZATION-CONSTRAINT-TYPE") is None
        assert element.find("TOLERANCE") is None

        reloaded = SynchronizationTimingConstraint(parent, "Sync1")
        ARXMLParser().readSynchronizationTimingConstraint(_round_trip(element), reloaded)
        assert reloaded.getEventOccurrenceKind() is None
        assert reloaded.getScopeEvents() == []
        assert reloaded.getScopes() == []
        assert reloaded.getSynchronizationConstraintType() is None
        assert reloaded.getTolerance() is None


class TestWritePeriodicEventTriggering:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_periodic_event_triggering(self):
        parent = self._parent()
        constraint = PeriodicEventTriggering(parent, "Periodic1")
        constraint.setMinimumInterArrivalTime(_mdt("0", "10"))
        constraint.setJitter(_mdt("0", "20"))
        constraint.setPeriod(_mdt("0", "30"))
        constraint.setEventRef(RefType().setValue("/AUTOSAR/TdEvent").setDest("TIMING-DESCRIPTION-EVENT"))

        element = ET.Element("PERIODIC-EVENT-TRIGGERING")
        ARXMLWriter().writePeriodicEventTriggering(element, constraint)
        event_ref_idx = list(element).index(element.find("EVENT-REF"))
        min_iat_idx = list(element).index(element.find("MINIMUM-INTER-ARRIVAL-TIME"))
        jitter_idx = list(element).index(element.find("JITTER"))
        period_idx = list(element).index(element.find("PERIOD"))
        assert event_ref_idx < min_iat_idx < jitter_idx < period_idx
        assert element.find("EVENT-REF").text == "/AUTOSAR/TdEvent"
        assert element.find("EVENT-REF").attrib["DEST"] == "TIMING-DESCRIPTION-EVENT"
        assert element.find("MINIMUM-INTER-ARRIVAL-TIME/CSE-CODE-FACTOR").text == "10"
        assert element.find("JITTER/CSE-CODE-FACTOR").text == "20"
        assert element.find("PERIOD/CSE-CODE-FACTOR").text == "30"

        reloaded = PeriodicEventTriggering(parent, "Periodic1")
        ARXMLParser().readPeriodicEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Periodic1"
        assert reloaded.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 10
        assert reloaded.getJitter().getCseCodeFactor().getValue() == 20
        assert reloaded.getPeriod().getCseCodeFactor().getValue() == 30
        assert reloaded.getEventRef().getValue() == "/AUTOSAR/TdEvent"
        assert reloaded.getEventRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_write_periodic_event_triggering_empty(self):
        parent = self._parent()
        constraint = PeriodicEventTriggering(parent, "Periodic1")

        element = ET.Element("PERIODIC-EVENT-TRIGGERING")
        ARXMLWriter().writePeriodicEventTriggering(element, constraint)
        assert element.find("EVENT-REF") is None
        assert element.find("MINIMUM-INTER-ARRIVAL-TIME") is None
        assert element.find("JITTER") is None
        assert element.find("PERIOD") is None

        reloaded = PeriodicEventTriggering(parent, "Periodic1")
        ARXMLParser().readPeriodicEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getMinimumInterArrivalTime() is None
        assert reloaded.getJitter() is None
        assert reloaded.getPeriod() is None
        assert reloaded.getEventRef() is None


class TestWriteSporadicEventTriggering:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_sporadic_event_triggering(self):
        parent = self._parent()
        constraint = SporadicEventTriggering(parent, "Sporadic1")
        constraint.setJitter(_mdt("0", "30"))
        constraint.setMaximumInterArrivalTime(_mdt("0", "20"))
        constraint.setMinimumInterArrivalTime(_mdt("0", "10"))
        constraint.setPeriod(_mdt("0", "40"))

        element = ET.Element("SPORADIC-EVENT-TRIGGERING")
        ARXMLWriter().writeSporadicEventTriggering(element, constraint)
        min_iat_idx = list(element).index(element.find("MINIMUM-INTER-ARRIVAL-TIME"))
        max_iat_idx = list(element).index(element.find("MAXIMUM-INTER-ARRIVAL-TIME"))
        jitter_idx = list(element).index(element.find("JITTER"))
        period_idx = list(element).index(element.find("PERIOD"))
        assert min_iat_idx < max_iat_idx < jitter_idx < period_idx
        assert element.find("MAXIMUM-INTER-ARRIVAL-TIME/CSE-CODE-FACTOR").text == "20"

        reloaded = SporadicEventTriggering(parent, "Sporadic1")
        ARXMLParser().readSporadicEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Sporadic1"
        assert reloaded.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 10
        assert reloaded.getMaximumInterArrivalTime().getCseCodeFactor().getValue() == 20
        assert reloaded.getJitter().getCseCodeFactor().getValue() == 30
        assert reloaded.getPeriod().getCseCodeFactor().getValue() == 40

    def test_write_sporadic_event_triggering_empty(self):
        parent = self._parent()
        constraint = SporadicEventTriggering(parent, "Sporadic1")

        element = ET.Element("SPORADIC-EVENT-TRIGGERING")
        ARXMLWriter().writeSporadicEventTriggering(element, constraint)
        assert element.find("MINIMUM-INTER-ARRIVAL-TIME") is None
        assert element.find("MAXIMUM-INTER-ARRIVAL-TIME") is None
        assert element.find("JITTER") is None
        assert element.find("PERIOD") is None

        reloaded = SporadicEventTriggering(parent, "Sporadic1")
        ARXMLParser().readSporadicEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getMinimumInterArrivalTime() is None
        assert reloaded.getMaximumInterArrivalTime() is None
        assert reloaded.getJitter() is None
        assert reloaded.getPeriod() is None


class TestWriteConcretePatternEventTriggering:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_concrete_pattern_event_triggering(self):
        parent = self._parent()
        constraint = ConcretePatternEventTriggering(parent, "Concrete1")
        constraint.addOffset(_mdt("0", "5"))
        constraint.addOffset(_mdt("0", "15"))
        constraint.setPatternJitter(_mdt("0", "2"))
        constraint.setPatternLength(_mdt("0", "100"))
        constraint.setPatternPeriod(_mdt("0", "200"))

        element = ET.Element("CONCRETE-PATTERN-EVENT-TRIGGERING")
        ARXMLWriter().writeConcretePatternEventTriggering(element, constraint)
        pattern_jitter_idx = list(element).index(element.find("PATTERN-JITTER"))
        pattern_period_idx = list(element).index(element.find("PATTERN-PERIOD"))
        offsets_idx = list(element).index(element.find("OFFSETS"))
        pattern_length_idx = list(element).index(element.find("PATTERN-LENGTH"))
        assert pattern_jitter_idx < pattern_period_idx < offsets_idx < pattern_length_idx
        time_values = element.findall("OFFSETS/TIME-VALUE")
        assert len(time_values) == 2
        assert time_values[0].find("CSE-CODE-FACTOR").text == "5"
        assert time_values[1].find("CSE-CODE-FACTOR").text == "15"
        assert element.find("PATTERN-JITTER/CSE-CODE-FACTOR").text == "2"

        reloaded = ConcretePatternEventTriggering(parent, "Concrete1")
        ARXMLParser().readConcretePatternEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Concrete1"
        offsets = reloaded.getOffsets()
        assert len(offsets) == 2
        assert offsets[0].getCseCodeFactor().getValue() == 5
        assert offsets[1].getCseCodeFactor().getValue() == 15
        assert reloaded.getPatternJitter().getCseCodeFactor().getValue() == 2
        assert reloaded.getPatternLength().getCseCodeFactor().getValue() == 100
        assert reloaded.getPatternPeriod().getCseCodeFactor().getValue() == 200

    def test_write_concrete_pattern_event_triggering_empty_wrapper_list(self):
        parent = self._parent()
        constraint = ConcretePatternEventTriggering(parent, "Concrete1")

        element = ET.Element("CONCRETE-PATTERN-EVENT-TRIGGERING")
        ARXMLWriter().writeConcretePatternEventTriggering(element, constraint)
        assert element.find("OFFSETS") is None
        assert element.find("PATTERN-JITTER") is None
        assert element.find("PATTERN-LENGTH") is None
        assert element.find("PATTERN-PERIOD") is None

        reloaded = ConcretePatternEventTriggering(parent, "Concrete1")
        ARXMLParser().readConcretePatternEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getOffsets() == []
        assert reloaded.getPatternJitter() is None
        assert reloaded.getPatternLength() is None
        assert reloaded.getPatternPeriod() is None


class TestWriteBurstPatternEventTriggering:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_burst_pattern_event_triggering(self):
        parent = self._parent()
        constraint = BurstPatternEventTriggering(parent, "Burst1")
        constraint.setMaxNumberOfOccurrences(PositiveInteger().setValue("10"))
        constraint.setMinimumInterArrivalTime(_mdt("0", "5"))
        constraint.setMinNumberOfOccurrences(PositiveInteger().setValue("3"))
        constraint.setPatternJitter(_mdt("0", "1"))
        constraint.setPatternLength(_mdt("0", "50"))
        constraint.setPatternPeriod(_mdt("0", "80"))

        element = ET.Element("BURST-PATTERN-EVENT-TRIGGERING")
        ARXMLWriter().writeBurstPatternEventTriggering(element, constraint)
        max_occ_idx = list(element).index(element.find("MAX-NUMBER-OF-OCCURRENCES"))
        min_iat_idx = list(element).index(element.find("MINIMUM-INTER-ARRIVAL-TIME"))
        pattern_jitter_idx = list(element).index(element.find("PATTERN-JITTER"))
        pattern_length_idx = list(element).index(element.find("PATTERN-LENGTH"))
        pattern_period_idx = list(element).index(element.find("PATTERN-PERIOD"))
        min_occ_idx = list(element).index(element.find("MIN-NUMBER-OF-OCCURRENCES"))
        assert max_occ_idx < min_iat_idx < pattern_jitter_idx < pattern_length_idx < pattern_period_idx < min_occ_idx
        assert element.find("MAX-NUMBER-OF-OCCURRENCES").text == "10"
        assert element.find("MIN-NUMBER-OF-OCCURRENCES").text == "3"

        reloaded = BurstPatternEventTriggering(parent, "Burst1")
        ARXMLParser().readBurstPatternEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Burst1"
        assert reloaded.getMaxNumberOfOccurrences().getValue() == 10
        assert reloaded.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 5
        assert reloaded.getMinNumberOfOccurrences().getValue() == 3
        assert reloaded.getPatternJitter().getCseCodeFactor().getValue() == 1
        assert reloaded.getPatternLength().getCseCodeFactor().getValue() == 50
        assert reloaded.getPatternPeriod().getCseCodeFactor().getValue() == 80

    def test_write_burst_pattern_event_triggering_empty(self):
        parent = self._parent()
        constraint = BurstPatternEventTriggering(parent, "Burst1")

        element = ET.Element("BURST-PATTERN-EVENT-TRIGGERING")
        ARXMLWriter().writeBurstPatternEventTriggering(element, constraint)
        assert element.find("MAX-NUMBER-OF-OCCURRENCES") is None
        assert element.find("MINIMUM-INTER-ARRIVAL-TIME") is None
        assert element.find("MIN-NUMBER-OF-OCCURRENCES") is None
        assert element.find("PATTERN-JITTER") is None
        assert element.find("PATTERN-LENGTH") is None
        assert element.find("PATTERN-PERIOD") is None

        reloaded = BurstPatternEventTriggering(parent, "Burst1")
        ARXMLParser().readBurstPatternEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getMaxNumberOfOccurrences() is None
        assert reloaded.getMinimumInterArrivalTime() is None
        assert reloaded.getMinNumberOfOccurrences() is None
        assert reloaded.getPatternJitter() is None
        assert reloaded.getPatternLength() is None
        assert reloaded.getPatternPeriod() is None


class TestWriteArbitraryEventTriggering:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _interval(self, factor: str) -> ConfidenceInterval:
        interval = ConfidenceInterval()
        interval.setLowerBound(_mdt("0", "10"))
        interval.setPropability(Float().setValue("0.95"))
        interval.setUpperBound(_mdt("0", factor))
        return interval

    def test_round_trip_arbitrary_event_triggering(self):
        parent = self._parent()
        constraint = ArbitraryEventTriggering(parent, "Arbitrary1")
        constraint.addMinimumDistance(_mdt("0", "10"))
        constraint.addMinimumDistance(_mdt("0", "12"))
        constraint.addMaximumDistance(_mdt("0", "20"))
        constraint.addMaximumDistance(_mdt("0", "22"))
        constraint.addConfidenceInterval(self._interval("100"))
        constraint.addConfidenceInterval(self._interval("200"))
        constraint.setEventRef(RefType().setValue("/AUTOSAR/TdEvent").setDest("TIMING-DESCRIPTION-EVENT"))

        element = ET.Element("ARBITRARY-EVENT-TRIGGERING")
        ARXMLWriter().writeArbitraryEventTriggering(element, constraint)
        minimum_distances_idx = list(element).index(element.find("MINIMUM-DISTANCES"))
        maximum_distances_idx = list(element).index(element.find("MAXIMUM-DISTANCES"))
        confidence_intervals_idx = list(element).index(element.find("CONFIDENCE-INTERVALS"))
        assert minimum_distances_idx < maximum_distances_idx < confidence_intervals_idx
        min_time_values = element.findall("MINIMUM-DISTANCES/TIME-VALUE")
        assert len(min_time_values) == 2
        assert min_time_values[0].find("CSE-CODE-FACTOR").text == "10"
        assert min_time_values[1].find("CSE-CODE-FACTOR").text == "12"
        max_time_values = element.findall("MAXIMUM-DISTANCES/TIME-VALUE")
        assert len(max_time_values) == 2
        assert max_time_values[0].find("CSE-CODE-FACTOR").text == "20"
        intervals = element.findall("CONFIDENCE-INTERVALS/CONFIDENCE-INTERVAL")
        assert len(intervals) == 2
        assert intervals[0].find("UPPER-BOUND/CSE-CODE-FACTOR").text == "100"
        assert intervals[0].find("PROPABILITY").text == "0.95"
        assert intervals[1].find("UPPER-BOUND/CSE-CODE-FACTOR").text == "200"
        assert element.find("EVENT-REF").text == "/AUTOSAR/TdEvent"

        reloaded = ArbitraryEventTriggering(parent, "Arbitrary1")
        ARXMLParser().readArbitraryEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Arbitrary1"
        min_distances = reloaded.getMinimumDistances()
        assert len(min_distances) == 2
        assert min_distances[0].getCseCodeFactor().getValue() == 10
        assert min_distances[1].getCseCodeFactor().getValue() == 12
        max_distances = reloaded.getMaximumDistances()
        assert len(max_distances) == 2
        assert max_distances[0].getCseCodeFactor().getValue() == 20
        assert max_distances[1].getCseCodeFactor().getValue() == 22
        intervals_reloaded = reloaded.getConfidenceIntervals()
        assert len(intervals_reloaded) == 2
        assert isinstance(intervals_reloaded[0], ConfidenceInterval)
        assert intervals_reloaded[0].getLowerBound().getCseCodeFactor().getValue() == 10
        assert intervals_reloaded[0].getPropability().getValue() == 0.95
        assert intervals_reloaded[0].getUpperBound().getCseCodeFactor().getValue() == 100
        assert intervals_reloaded[1].getUpperBound().getCseCodeFactor().getValue() == 200
        assert reloaded.getEventRef().getValue() == "/AUTOSAR/TdEvent"
        assert reloaded.getEventRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_write_arbitrary_event_triggering_empty_wrapper_lists(self):
        parent = self._parent()
        constraint = ArbitraryEventTriggering(parent, "Arbitrary1")

        element = ET.Element("ARBITRARY-EVENT-TRIGGERING")
        ARXMLWriter().writeArbitraryEventTriggering(element, constraint)
        assert element.find("MINIMUM-DISTANCES") is None
        assert element.find("MAXIMUM-DISTANCES") is None
        assert element.find("CONFIDENCE-INTERVALS") is None
        assert element.find("EVENT-REF") is None

        reloaded = ArbitraryEventTriggering(parent, "Arbitrary1")
        ARXMLParser().readArbitraryEventTriggering(_round_trip(element), reloaded)
        assert reloaded.getMinimumDistances() == []
        assert reloaded.getMaximumDistances() == []
        assert reloaded.getConfidenceIntervals() == []
        assert reloaded.getEventRef() is None
