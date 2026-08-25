"""Parser tests for the timing constraints (AGE-CONSTRAINT, LATENCY-TIMING-CONSTRAINT, OFFSET-TIMING-CONSTRAINT, SYNCHRONIZATION-TIMING-CONSTRAINT)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import AgeConstraint
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
