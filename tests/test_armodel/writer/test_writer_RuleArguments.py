"""Writer round-trip tests for RuleArguments (Swc TPS Table 5.134, p.470).

The RULE-ARGUMENTS element serializes V, VF, VT, VTF (atpMixed choice, so the
emission order is free; the writer emits V, VF, VT, VTF, VARIATION-POINT).
The save-reload round-trip goes through the ConstantSpecification VALUE-SPEC
dispatch (NUMERICAL-RULE-BASED-VALUE-SPECIFICATION carrier) so the
bundled-XSD validation runs.
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
    VerbatimString,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import NumericalOrText
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_arguments() -> RuleArguments:
    arguments = RuleArguments()
    arguments.setV(Numerical().setValue("1.5"))
    arguments.setVf(Numerical().setValue("2.5"))
    arguments.setVt(VerbatimString().setValue("open|closed"))
    vtf = NumericalOrText()
    vtf.setVf(Numerical().setValue("3.5"))
    arguments.setVtf(vtf)
    return arguments


class TestWriteRuleArguments:
    def test_write_full(self):
        parent = ET.Element("ARGUMENTSS")
        ARXMLWriter().writeRuleArguments(parent, _build_arguments())

        child = parent.find("RULE-ARGUMENTS")
        assert child is not None
        assert child.find("V").text == "1.5"
        assert child.find("VF").text == "2.5"
        assert child.find("VT").text == "open|closed"
        assert child.find("VTF/VF").text == "3.5"

    def test_write_none_no_element(self):
        parent = ET.Element("ARGUMENTSS")
        ARXMLWriter().writeRuleArguments(parent, None)
        assert len(parent) == 0

    def test_write_unset_fields_omit_elements(self):
        parent = ET.Element("ARGUMENTSS")
        ARXMLWriter().writeRuleArguments(parent, RuleArguments())

        child = parent.find("RULE-ARGUMENTS")
        assert child is not None
        assert child.find("V") is None
        assert child.find("VF") is None
        assert child.find("VT") is None
        assert child.find("VTF") is None


class TestRuleArgumentsRoundTrip:
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
        rule = RuleBasedValueSpecification()
        rule.setRule(Identifier().setValue("FILL_UNTIL_END"))
        rule.addArgument(_build_arguments())
        spec = NumericalRuleBasedValueSpecification()
        spec.setRuleBasedValues(rule)

        reloaded_spec = self._save_and_reload(spec)
        assert isinstance(reloaded_spec, NumericalRuleBasedValueSpecification)
        arguments = reloaded_spec.getRuleBasedValues().getArguments()[0]
        assert isinstance(arguments, RuleArguments)
        assert float(arguments.getV().getValue()) == 1.5
        assert float(arguments.getVf().getValue()) == 2.5
        assert arguments.getVt().getValue() == "open|closed"
        assert float(arguments.getVtf().getVf().getValue()) == 3.5
        assert arguments.getVtf().getVt() is None

    def test_round_trip_v_only(self):
        arguments = RuleArguments()
        arguments.setV(Numerical().setValue("7"))
        rule = RuleBasedValueSpecification()
        rule.addArgument(arguments)
        spec = NumericalRuleBasedValueSpecification()
        spec.setRuleBasedValues(rule)

        reloaded_spec = self._save_and_reload(spec)
        arguments = reloaded_spec.getRuleBasedValues().getArguments()[0]
        assert float(arguments.getV().getValue()) == 7.0
        assert arguments.getVf() is None
        assert arguments.getVt() is None
        assert arguments.getVtf() is None
