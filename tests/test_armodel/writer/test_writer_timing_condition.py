"""Writer round-trip tests for TIMING-CONDITION and CONFIDENCE-INTERVAL."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingConditionFormula,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingCondition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Float,
    Integer,
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


class TestWriteTimingCondition:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_timing_condition(self):
        parent = self._parent()
        condition = TimingCondition(parent, "Cond1")
        formula = TimingConditionFormula(condition, "Formula1")
        formula.setText("modeA == 1")
        formula.setTimingEventRef(RefType().setValue("/Pkg/Event").setDest("TIMING-DESCRIPTION-EVENT"))
        condition.setTimingConditionFormula(formula)

        element = ET.Element("TIMING-CONDITION")
        ARXMLWriter().writeTimingCondition(element, condition)
        assert element.find("SHORT-NAME").text == "Cond1"
        assert element.find("TIMING-CONDITION-FORMULA") is not None

        reloaded = TimingCondition(parent, "Cond1")
        ARXMLParser().readTimingCondition(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Cond1"
        formula = reloaded.getTimingConditionFormula()
        assert isinstance(formula, TimingConditionFormula)
        assert formula.getShortName() == "Formula1"
        assert formula.getText() == "modeA == 1"
        assert formula.getTimingEventRef().getValue() == "/Pkg/Event"
        assert formula.getTimingEventRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_write_timing_condition_no_formula(self):
        parent = self._parent()
        condition = TimingCondition(parent, "Cond1")

        element = ET.Element("TIMING-CONDITION")
        ARXMLWriter().writeTimingCondition(element, condition)
        assert element.find("SHORT-NAME").text == "Cond1"
        assert element.find("TIMING-CONDITION-FORMULA") is None

        reloaded = TimingCondition(parent, "Cond1")
        ARXMLParser().readTimingCondition(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Cond1"
        assert reloaded.getTimingConditionFormula() is None


class TestWriteConfidenceInterval:
    def _mdt(self, cse_code: str, factor: str) -> MultidimensionalTime:
        mdt = MultidimensionalTime()
        mdt.setCseCode(CseCodeType().setValue(cse_code))
        mdt.setCseCodeFactor(Integer().setValue(factor))
        return mdt

    def test_round_trip_confidence_interval(self):
        interval = ConfidenceInterval()
        interval.setLowerBound(self._mdt("0", "50"))
        interval.setPropability(Float().setValue("0.95"))
        interval.setUpperBound(self._mdt("0", "100"))

        element = ET.Element("CONFIDENCE-INTERVAL")
        ARXMLWriter().writeConfidenceInterval(element, interval)
        assert element.find("LOWER-BOUND") is not None
        assert element.find("PROPABILITY") is not None
        assert element.find("UPPER-BOUND") is not None

        reloaded = ConfidenceInterval()
        ARXMLParser().readConfidenceInterval(_round_trip(element), reloaded)
        lower_bound = reloaded.getLowerBound()
        assert isinstance(lower_bound, MultidimensionalTime)
        assert lower_bound.getCseCode().getValue() == "0"
        assert lower_bound.getCseCodeFactor().getValue() == 50
        assert reloaded.getPropability().getValue() == 0.95
        upper_bound = reloaded.getUpperBound()
        assert isinstance(upper_bound, MultidimensionalTime)
        assert upper_bound.getCseCodeFactor().getValue() == 100

    def test_write_confidence_interval_empty(self):
        interval = ConfidenceInterval()

        element = ET.Element("CONFIDENCE-INTERVAL")
        ARXMLWriter().writeConfidenceInterval(element, interval)
        assert len(element.findall("*")) == 0

        reloaded = ConfidenceInterval()
        ARXMLParser().readConfidenceInterval(_round_trip(element), reloaded)
        assert reloaded.getLowerBound() is None
        assert reloaded.getPropability() is None
        assert reloaded.getUpperBound() is None
