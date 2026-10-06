"""Writer round-trip tests for ApplicationRuleBasedValueSpecification (Swc TPS Table 5.129, p.463).

The XSD group APPLICATION-RULE-BASED-VALUE-SPECIFICATION fixes the child
element order: CATEGORY (-20), SW-AXIS-CONTS (wrapper, omitted when empty),
SW-VALUE-CONT. The save-reload round-trip goes through the
ConstantSpecification VALUE-SPEC dispatch so the bundled-XSD validation runs.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationRuleBasedValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Numerical,
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


def _build_spec() -> ApplicationRuleBasedValueSpecification:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import RuleBasedAxisCont, RuleBasedValueCont

    spec = ApplicationRuleBasedValueSpecification()
    spec.setCategory(Identifier().setValue("VAL_BLK"))

    axis = RuleBasedAxisCont()
    axis.setSwAxisIndex(_axis_index("1"))
    spec.addSwAxisCont(axis)

    cont = RuleBasedValueCont()
    arraysize = ValueList()
    arraysize.setV(Numerical().setValue("2"))
    cont.setSwArraysize(arraysize)
    spec.setSwValueCont(cont)
    return spec


def _axis_index(value: str):
    from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType

    return AxisIndexType().setValue(value)


class TestWriteApplicationRuleBasedValueSpecification:
    def test_write_element_order_matches_xsd_group(self):
        parent = ET.Element("VALUE-SPEC")
        ARXMLWriter().writeApplicationRuleBasedValueSpecification(parent, _build_spec())

        child = parent.find("APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
        assert child is not None
        tags = [element.tag for element in child]
        assert tags.index("CATEGORY") < tags.index("SW-AXIS-CONTS") < tags.index("SW-VALUE-CONT")
        assert child.find("CATEGORY").text == "VAL_BLK"
        assert [element.tag for element in child.find("SW-AXIS-CONTS")] == ["RULE-BASED-AXIS-CONT"]
        assert child.find("SW-VALUE-CONT/SW-ARRAYSIZE/V").text == "2"

    def test_write_unset_fields_omit_elements(self):
        parent = ET.Element("VALUE-SPEC")
        ARXMLWriter().writeApplicationRuleBasedValueSpecification(parent, ApplicationRuleBasedValueSpecification())

        child = parent.find("APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
        assert child is not None
        assert child.find("CATEGORY") is None
        assert child.find("SW-AXIS-CONTS") is None
        assert child.find("SW-VALUE-CONT") is None


class TestApplicationRuleBasedValueSpecificationRoundTrip:
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
        assert isinstance(reloaded_spec, ApplicationRuleBasedValueSpecification)
        assert isinstance(reloaded_spec.getCategory(), Identifier)
        assert reloaded_spec.getCategory().getValue() == "VAL_BLK"
        assert len(reloaded_spec.getSwAxisConts()) == 1
        assert reloaded_spec.getSwAxisConts()[0].getSwAxisIndex().getValue() == "1"

        cont = reloaded_spec.getSwValueCont()
        assert cont is not None
        assert float(cont.getSwArraysize().getV().getValue()) == 2.0
        assert cont.getRuleBasedValues() is None

    def test_round_trip_empty(self):
        reloaded_spec = self._save_and_reload(ApplicationRuleBasedValueSpecification())
        assert isinstance(reloaded_spec, ApplicationRuleBasedValueSpecification)
        assert reloaded_spec.getCategory() is None
        assert reloaded_spec.getSwAxisConts() == []
        assert reloaded_spec.getSwValueCont() is None
