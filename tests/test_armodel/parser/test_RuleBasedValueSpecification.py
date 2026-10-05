"""Reader tests for RuleBasedValueSpecification (Swc TPS Table 5.133, p.469).

The XSD group RULE-BASED-VALUE-SPECIFICATION fixes the child element order:
RULE (offset 20), ARGUMENTSS (offset 30; wrapper of unbounded RULE-ARGUMENTS
elements — the upper multiplicity was increased to * by the atpVariation
resolution), MAX-SIZE-TO-FILL (offset 40, XSD type INTEGER).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
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
    return ET.fromstring('<RULE-BASED-VALUE-SPECIFICATION xmlns="%s">%s</RULE-BASED-VALUE-SPECIFICATION>' % (NS, content))


def test_read_full(parser):
    element = _wrap(
        "<RULE>FILL_UNTIL_END</RULE>" "<ARGUMENTSS><RULE-ARGUMENTS><V>1</V></RULE-ARGUMENTS><RULE-ARGUMENTS><V>2</V></RULE-ARGUMENTS></ARGUMENTSS>" "<MAX-SIZE-TO-FILL>8</MAX-SIZE-TO-FILL>"
    )
    spec = parser.getRuleBasedValueSpecification(element)
    assert spec is not None
    assert spec.getRule().getValue() == "FILL_UNTIL_END"
    arguments = spec.getArguments()
    assert len(arguments) == 2
    assert float(arguments[0].getV().getValue()) == 1.0
    assert float(arguments[1].getV().getValue()) == 2.0
    assert spec.getMaxSizeToFill().getValue() == 8


def test_read_negative_max_size_to_fill(parser):
    element = _wrap("<RULE>FILL_UNTIL_MAX_SIZE</RULE><MAX-SIZE-TO-FILL>-1</MAX-SIZE-TO-FILL>")
    spec = parser.getRuleBasedValueSpecification(element)
    assert spec is not None
    assert spec.getRule().getValue() == "FILL_UNTIL_MAX_SIZE"
    assert spec.getMaxSizeToFill().getValue() == -1


def test_read_empty(parser):
    element = _wrap("")
    spec = parser.getRuleBasedValueSpecification(element)
    assert spec is not None
    assert spec.getRule() is None
    assert spec.getArguments() == []
    assert spec.getMaxSizeToFill() is None
