"""Writer round-trip tests for RuleBasedValueCont (Swc TPS Table 5.131, p.465).

The writer emits the SW-VALUE-CONT element (type RULE-BASED-VALUE-CONT) in
the XSD group order UNIT-REF (30), SW-ARRAYSIZE (40), RULE-BASED-VALUES (80).
The save-reload round-trip goes through the ConstantSpecification VALUE-SPEC
dispatch (APPLICATION-RULE-BASED-VALUE-SPECIFICATION carrier) so the
bundled-XSD validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ApplicationRuleBasedValueSpecification,
    RuleBasedValueCont,
    RuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Numerical,
    RefType,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_cont() -> RuleBasedValueCont:
    cont = RuleBasedValueCont()
    unit_ref = RefType().setValue("/Units/N")
    unit_ref.setDest("UNIT")
    cont.setUnitRef(unit_ref)
    arraysize = ValueList()
    arraysize.setV(Numerical().setValue("2"))
    cont.setSwArraysize(arraysize)
    rule = RuleBasedValueSpecification()
    rule.setRule(Identifier().setValue("FILL_UNTIL_END"))
    cont.setRuleBasedValues(rule)
    return cont


class TestWriteRuleBasedValueCont:
    def test_write_element_order_matches_xsd_group(self):
        parent = ET.Element("APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
        ARXMLWriter().writeRuleBasedValueCont(parent, _build_cont())

        child = parent.find("SW-VALUE-CONT")
        assert child is not None
        tags = [element.tag for element in child]
        assert tags.index("UNIT-REF") < tags.index("SW-ARRAYSIZE") < tags.index("RULE-BASED-VALUES")
        assert child.find("UNIT-REF").attrib["DEST"] == "UNIT"
        assert child.find("SW-ARRAYSIZE/V").text == "2"
        assert child.find("RULE-BASED-VALUES/RULE").text == "FILL_UNTIL_END"

    def test_write_none_no_element(self):
        parent = ET.Element("APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
        ARXMLWriter().writeRuleBasedValueCont(parent, None)
        assert len(parent) == 0

    def test_write_unset_fields_omit_elements(self):
        parent = ET.Element("APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
        ARXMLWriter().writeRuleBasedValueCont(parent, RuleBasedValueCont())

        child = parent.find("SW-VALUE-CONT")
        assert child is not None
        assert child.find("UNIT-REF") is None
        assert child.find("SW-ARRAYSIZE") is None
        assert child.find("RULE-BASED-VALUES") is None


class TestRuleBasedValueContRoundTrip:
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
        spec = ApplicationRuleBasedValueSpecification()
        spec.setSwValueCont(_build_cont())

        reloaded_spec = self._save_and_reload(spec)
        assert isinstance(reloaded_spec, ApplicationRuleBasedValueSpecification)
        cont = reloaded_spec.getSwValueCont()
        assert isinstance(cont, RuleBasedValueCont)
        assert cont.getUnitRef().getValue() == "/Units/N"
        assert cont.getUnitRef().getDest() == "UNIT"
        assert float(cont.getSwArraysize().getV().getValue()) == 2.0
        assert cont.getRuleBasedValues().getRule().getValue() == "FILL_UNTIL_END"

    def test_round_trip_empty_cont(self):
        spec = ApplicationRuleBasedValueSpecification()
        spec.setSwValueCont(RuleBasedValueCont())

        reloaded_spec = self._save_and_reload(spec)
        cont = reloaded_spec.getSwValueCont()
        assert isinstance(cont, RuleBasedValueCont)
        assert cont.getUnitRef() is None
        assert cont.getSwArraysize() is None
        assert cont.getRuleBasedValues() is None
