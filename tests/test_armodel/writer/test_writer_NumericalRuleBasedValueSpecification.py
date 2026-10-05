"""Writer round-trip tests for NumericalRuleBasedValueSpecification (Swc TPS Table 5.132, p.467).

The writer emits the NUMERICAL-RULE-BASED-VALUE-SPECIFICATION element with the
single RULE-BASED-VALUES role element. The save-reload round-trip goes through
the ConstantSpecification VALUE-SPEC dispatch so the bundled-XSD validation
runs.
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


def _build_spec() -> NumericalRuleBasedValueSpecification:
    spec = NumericalRuleBasedValueSpecification()
    rule = RuleBasedValueSpecification()
    rule.setRule(Identifier().setValue("FILL_UNTIL_MAX_SIZE"))
    argument = RuleArguments()
    argument.setV(Numerical().setValue("4"))
    rule.addArgument(argument)
    spec.setRuleBasedValues(rule)
    return spec


class TestWriteNumericalRuleBasedValueSpecification:
    def test_write_element(self):
        parent = ET.Element("VALUE-SPEC")
        ARXMLWriter().writeNumericalRuleBasedValueSpecification(parent, _build_spec())

        child = parent.find("NUMERICAL-RULE-BASED-VALUE-SPECIFICATION")
        assert child is not None
        rule = child.find("RULE-BASED-VALUES")
        assert rule is not None
        assert rule.find("RULE").text == "FILL_UNTIL_MAX_SIZE"
        assert rule.find("ARGUMENTSS/RULE-ARGUMENTS/V").text == "4"
        assert rule.find("MAX-SIZE-TO-FILL") is None

    def test_write_none_no_element(self):
        parent = ET.Element("VALUE-SPEC")
        ARXMLWriter().writeNumericalRuleBasedValueSpecification(parent, None)
        assert len(parent) == 0

    def test_write_unset_field_omits_element(self):
        parent = ET.Element("VALUE-SPEC")
        ARXMLWriter().writeNumericalRuleBasedValueSpecification(parent, NumericalRuleBasedValueSpecification())

        child = parent.find("NUMERICAL-RULE-BASED-VALUE-SPECIFICATION")
        assert child is not None
        assert child.find("RULE-BASED-VALUES") is None


class TestNumericalRuleBasedValueSpecificationRoundTrip:
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
        reloaded_spec = self._save_and_reload(_build_spec())
        assert isinstance(reloaded_spec, NumericalRuleBasedValueSpecification)
        rule = reloaded_spec.getRuleBasedValues()
        assert rule is not None
        assert rule.getRule().getValue() == "FILL_UNTIL_MAX_SIZE"
        assert float(rule.getArguments()[0].getV().getValue()) == 4.0
        assert rule.getMaxSizeToFill() is None

    def test_round_trip_empty(self):
        reloaded_spec = self._save_and_reload(NumericalRuleBasedValueSpecification())
        assert isinstance(reloaded_spec, NumericalRuleBasedValueSpecification)
        assert reloaded_spec.getRuleBasedValues() is None
