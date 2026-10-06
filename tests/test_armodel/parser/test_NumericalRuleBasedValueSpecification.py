"""Reader tests for NumericalRuleBasedValueSpecification (Swc TPS Table 5.132, p.467).

The XSD group NUMERICAL-RULE-BASED-VALUE-SPECIFICATION carries a single
RULE-BASED-VALUES element (type RULE-BASED-VALUE-SPECIFICATION,
xml.roleElement=true, no wrappers).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalRuleBasedValueSpecification
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


def _wrap(content: str) -> ET.Element:
    return ET.fromstring('<NUMERICAL-RULE-BASED-VALUE-SPECIFICATION xmlns="%s">%s</NUMERICAL-RULE-BASED-VALUE-SPECIFICATION>' % (NS, content))


def test_read_rule_based_values(parser):
    element = _wrap("<RULE-BASED-VALUES><RULE>FILL_UNTIL_END</RULE>" "<ARGUMENTSS><RULE-ARGUMENTS><V>4</V></RULE-ARGUMENTS></ARGUMENTSS>" "</RULE-BASED-VALUES>")
    spec = parser.getNumericalRuleBasedValueSpecification(element)
    assert spec is not None
    rule = spec.getRuleBasedValues()
    assert rule is not None
    assert rule.getRule().getValue() == "FILL_UNTIL_END"
    assert float(rule.getArguments()[0].getV().getValue()) == 4.0
    assert rule.getMaxSizeToFill() is None


def test_read_dispatch_via_get_value_specification(parser):
    element = _wrap("<RULE-BASED-VALUES><RULE>FILL_UNTIL_MAX_SIZE</RULE></RULE-BASED-VALUES>")
    value_spec = parser.getValueSpecification(element, "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION")
    assert isinstance(value_spec, NumericalRuleBasedValueSpecification)
    assert value_spec.getRuleBasedValues().getRule().getValue() == "FILL_UNTIL_MAX_SIZE"


def test_read_empty(parser):
    element = _wrap("")
    spec = parser.getNumericalRuleBasedValueSpecification(element)
    assert spec is not None
    assert spec.getRuleBasedValues() is None
