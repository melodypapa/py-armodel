"""Writer round-trip tests for RuleBasedAxisCont (Table 5.130)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    RuleBasedAxisCont,
    RuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import Numerical, ValueList
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _namespaced(element: ET.Element) -> ET.Element:
    xml_text = ET.tostring(element, encoding="unicode")
    return ET.fromstring(xml_text.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))


def _full_cont():
    cont = RuleBasedAxisCont()
    category = CalprmAxisCategoryEnum()
    category.setValue(CalprmAxisCategoryEnum.STD_AXIS)
    cont.setCategory(category)

    value_spec = RuleBasedValueSpecification()
    value_spec.setRule(Identifier().setValue("myRule"))
    cont.setRuleBasedValues(value_spec)

    value_list = ValueList()
    value_list.setV(Numerical().setValue("4"))
    cont.setSwArraysize(value_list)

    index = AxisIndexType()
    index.setValue("1")
    cont.setSwAxisIndex(index)

    unit = RefType()
    unit.setValue("/Unit/SomeUnit")
    unit.setDest("UNIT")
    cont.setUnitRef(unit)
    return cont


def test_write_rule_based_axis_cont(writer):
    parent = _parent()
    writer.writeRuleBasedAxisCont(parent, _full_cont())

    tag = parent.find("RULE-BASED-AXIS-CONT")
    assert tag is not None
    assert tag.find("CATEGORY").text == "STD_AXIS"
    assert tag.find("RULE-BASED-VALUES") is not None
    assert tag.find("SW-ARRAYSIZE") is not None
    assert tag.find("SW-AXIS-INDEX") is not None
    assert tag.find("UNIT-REF") is not None


def test_write_element_order_matches_xsd_group(writer):
    parent = _parent()
    writer.writeRuleBasedAxisCont(parent, _full_cont())

    tag = parent.find("RULE-BASED-AXIS-CONT")
    tags = [element.tag for element in tag]
    assert tags.index("CATEGORY") < tags.index("UNIT-REF") < tags.index("SW-ARRAYSIZE") < tags.index("SW-AXIS-INDEX") < tags.index("RULE-BASED-VALUES")
    assert tag.find("UNIT-REF").attrib["DEST"] == "UNIT"


def test_write_rule_based_axis_cont_empty(writer):
    parent = _parent()
    writer.writeRuleBasedAxisCont(parent, RuleBasedAxisCont())

    tag = parent.find("RULE-BASED-AXIS-CONT")
    assert tag is not None
    assert tag.find("CATEGORY") is None
    assert tag.find("RULE-BASED-VALUES") is None
    assert tag.find("SW-ARRAYSIZE") is None
    assert tag.find("SW-AXIS-INDEX") is None
    assert tag.find("UNIT-REF") is None


def test_rule_based_axis_cont_round_trip(writer, parser):
    parent = _parent()
    writer.writeRuleBasedAxisCont(parent, _full_cont())

    reparsed = _namespaced(parent)
    reloaded = parser.getRuleBasedAxisCont(reparsed[0])

    assert isinstance(reloaded, RuleBasedAxisCont)
    assert isinstance(reloaded.getCategory(), CalprmAxisCategoryEnum)
    assert reloaded.getCategory().getValue() == "stdAxis"
    assert reloaded.getRuleBasedValues() is not None
    assert reloaded.getRuleBasedValues().getRule().getValue() == "myRule"
    assert reloaded.getSwArraysize() is not None
    assert float(reloaded.getSwArraysize().getV().getValue()) == 4.0
    assert reloaded.getSwAxisIndex().getValue() == "1"
    assert reloaded.getUnitRef().getValue() == "/Unit/SomeUnit"


class TestDocumentRoundTrip:
    def test_round_trip_via_application_rule_based_value_specification(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationRuleBasedValueSpecification

        spec = ApplicationRuleBasedValueSpecification()
        spec.setCategory(Identifier().setValue("CURVE"))
        spec.addSwAxisCont(_full_cont())

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        constant = pkg.createConstantSpecification("Const")
        constant.setValueSpec(spec)

        import os
        import tempfile

        from armodel.writer.arxml_writer import ARXMLWriter as Writer

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            Writer().save(file_path, document)
            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser().load(file_path, reloaded)
            constant2 = reloaded.getARPackages()[0].getConstantSpecifications()[0]
            reloaded_spec = constant2.getValueSpec()
            assert isinstance(reloaded_spec, ApplicationRuleBasedValueSpecification)
            axis_conts = reloaded_spec.getSwAxisConts()
            assert len(axis_conts) == 1
            cont = axis_conts[0]
            assert isinstance(cont, RuleBasedAxisCont)
            assert cont.getCategory().getValue() == "stdAxis"
            assert cont.getSwAxisIndex().getValue() == "1"
            assert float(cont.getSwArraysize().getV().getValue()) == 4.0
            assert cont.getUnitRef().getValue() == "/Unit/SomeUnit"
            assert cont.getRuleBasedValues().getRule().getValue() == "myRule"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
