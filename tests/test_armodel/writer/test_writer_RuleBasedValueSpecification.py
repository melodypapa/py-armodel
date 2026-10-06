"""Writer round-trip tests for RuleBasedValueSpecification (Swc TPS Table 5.133, p.469).

The writer emits the RULE-BASED-VALUE-SPECIFICATION element under the caller's
role key (RULE-BASED-VALUES) with the XSD group order RULE (20), ARGUMENTSS
(30, wrapper, omitted when empty), MAX-SIZE-TO-FILL (40). The save-reload
round-trip goes through the ConstantSpecification VALUE-SPEC dispatch
(NUMERICAL-RULE-BASED-VALUE-SPECIFICATION carrier) so the bundled-XSD
validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    NumericalRuleBasedValueSpecification,
    RuleArguments,
    RuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    Numerical,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_spec() -> RuleBasedValueSpecification:
    spec = RuleBasedValueSpecification()
    spec.setRule(Identifier().setValue("FILL_UNTIL_MAX_SIZE"))
    first = RuleArguments()
    first.setV(Numerical().setValue("1"))
    second = RuleArguments()
    second.setV(Numerical().setValue("2"))
    spec.addArgument(first)
    spec.addArgument(second)
    spec.setMaxSizeToFill(Integer().setValue("8"))
    return spec


class TestWriteRuleBasedValueSpecification:
    def test_write_element_order_matches_xsd_group(self):
        parent = ET.Element("RULE-BASED-AXIS-CONT")
        ARXMLWriter().writeRuleBasedValueSpecification(parent, "RULE-BASED-VALUES", _build_spec())

        child = parent.find("RULE-BASED-VALUES")
        assert child is not None
        tags = [element.tag for element in child]
        assert tags.index("RULE") < tags.index("ARGUMENTSS") < tags.index("MAX-SIZE-TO-FILL")
        assert child.find("RULE").text == "FILL_UNTIL_MAX_SIZE"
        argss = child.find("ARGUMENTSS")
        assert [element.tag for element in argss] == ["RULE-ARGUMENTS", "RULE-ARGUMENTS"]
        assert argss.find("RULE-ARGUMENTS/V").text == "1"
        assert child.find("MAX-SIZE-TO-FILL").text == "8"

    def test_write_none_no_element(self):
        parent = ET.Element("RULE-BASED-AXIS-CONT")
        ARXMLWriter().writeRuleBasedValueSpecification(parent, "RULE-BASED-VALUES", None)
        assert len(parent) == 0

    def test_write_empty_arguments_omit_wrapper(self):
        parent = ET.Element("RULE-BASED-AXIS-CONT")
        ARXMLWriter().writeRuleBasedValueSpecification(parent, "RULE-BASED-VALUES", RuleBasedValueSpecification())

        child = parent.find("RULE-BASED-VALUES")
        assert child is not None
        assert child.find("RULE") is None
        assert child.find("ARGUMENTSS") is None
        assert child.find("MAX-SIZE-TO-FILL") is None


class TestRuleBasedValueSpecificationRoundTrip:
    def _save_and_reload(self, value_spec):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")
        constant.setValueSpec(value_spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            return constant2.getValueSpec()
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_populated(self):
        spec = NumericalRuleBasedValueSpecification()
        spec.setRuleBasedValues(_build_spec())

        reloaded_spec = self._save_and_reload(spec)
        assert isinstance(reloaded_spec, NumericalRuleBasedValueSpecification)
        rule = reloaded_spec.getRuleBasedValues()
        assert isinstance(rule, RuleBasedValueSpecification)
        assert rule.getRule().getValue() == "FILL_UNTIL_MAX_SIZE"
        arguments = rule.getArguments()
        assert len(arguments) == 2
        assert float(arguments[0].getV().getValue()) == 1.0
        assert float(arguments[1].getV().getValue()) == 2.0
        assert rule.getMaxSizeToFill().getValue() == 8

    def test_round_trip_empty(self):
        spec = NumericalRuleBasedValueSpecification()
        spec.setRuleBasedValues(RuleBasedValueSpecification())

        reloaded_spec = self._save_and_reload(spec)
        rule = reloaded_spec.getRuleBasedValues()
        assert isinstance(rule, RuleBasedValueSpecification)
        assert rule.getRule() is None
        assert rule.getArguments() == []
        assert rule.getMaxSizeToFill() is None
