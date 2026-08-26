"""Parser tests for TIMING-CONDITION and CONFIDENCE-INTERVAL fragments."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingCondition,
    TimingConditionFormula,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.parser.arxml_parser import ARXMLParser

TIMING_CONDITION_XML = """<TIMING-CONDITION xmlns="http://autosar.org/schema/r4.0">
    <SHORT-NAME>Cond1</SHORT-NAME>
    <TIMING-CONDITION-FORMULA>modeA == 1<SHORT-NAME>Formula1</SHORT-NAME><TIMING-EVENT-REF DEST="TIMING-DESCRIPTION-EVENT">/Pkg/Event</TIMING-EVENT-REF></TIMING-CONDITION-FORMULA>
</TIMING-CONDITION>"""

CONFIDENCE_INTERVAL_XML = """<CONFIDENCE-INTERVAL xmlns="http://autosar.org/schema/r4.0">
    <LOWER-BOUND>
        <CSE-CODE>0</CSE-CODE>
        <CSE-CODE-FACTOR>50</CSE-CODE-FACTOR>
    </LOWER-BOUND>
    <PROPABILITY>0.95</PROPABILITY>
    <UPPER-BOUND>
        <CSE-CODE>0</CSE-CODE>
        <CSE-CODE-FACTOR>100</CSE-CODE-FACTOR>
    </UPPER-BOUND>
</CONFIDENCE-INTERVAL>"""


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


class TestReadTimingCondition:
    def test_read_timing_condition(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        parent = document.createARPackage("AUTOSAR")

        condition = TimingCondition(parent, "Cond1")
        ARXMLParser().readTimingCondition(_parse(TIMING_CONDITION_XML), condition)

        assert condition.getShortName() == "Cond1"
        formula = condition.getTimingConditionFormula()
        assert isinstance(formula, TimingConditionFormula)
        assert formula.getShortName() == "Formula1"
        assert formula.getText() == "modeA == 1"
        assert formula.getTimingEventRef().getValue() == "/Pkg/Event"
        assert formula.getTimingEventRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_read_confidence_interval(self):
        interval = ConfidenceInterval()
        ARXMLParser().readConfidenceInterval(_parse(CONFIDENCE_INTERVAL_XML), interval)

        lower_bound = interval.getLowerBound()
        assert isinstance(lower_bound, MultidimensionalTime)
        assert lower_bound.getCseCode().getValue() == "0"
        assert lower_bound.getCseCodeFactor().getValue() == 50
        assert interval.getPropability().getValue() == 0.95
        upper_bound = interval.getUpperBound()
        assert isinstance(upper_bound, MultidimensionalTime)
        assert upper_bound.getCseCodeFactor().getValue() == 100
