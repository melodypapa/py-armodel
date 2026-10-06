"""Reader tests for RuleBasedValueCont (Swc TPS Table 5.131, p.465).

The XSD group RULE-BASED-VALUE-CONT fixes the child element order:
UNIT-REF (30), SW-ARRAYSIZE (40), RULE-BASED-VALUES (80). The
serialization container is the APPLICATION-RULE-BASED-VALUE-SPECIFICATION
group's SW-VALUE-CONT element (type RULE-BASED-VALUE-CONT), read through
the parser's getRuleBasedValueCont.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import RuleBasedValueCont
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


def _wrap_application_spec(content: str) -> ET.Element:
    return ET.fromstring('<APPLICATION-RULE-BASED-VALUE-SPECIFICATION xmlns="%s">%s</APPLICATION-RULE-BASED-VALUE-SPECIFICATION>' % (NS, content))


def test_read_full(parser):
    element = _wrap_application_spec(
        "<SW-VALUE-CONT>"
        '<UNIT-REF DEST="UNIT">/Units/N</UNIT-REF>'
        "<SW-ARRAYSIZE><V>2</V></SW-ARRAYSIZE>"
        "<RULE-BASED-VALUES><RULE>FILL_UNTIL_END</RULE>"
        "<ARGUMENTSS><RULE-ARGUMENTS><V>5</V></RULE-ARGUMENTS></ARGUMENTSS>"
        "</RULE-BASED-VALUES>"
        "</SW-VALUE-CONT>"
    )
    cont = parser.getRuleBasedValueCont(element)
    assert cont is not None
    assert isinstance(cont, RuleBasedValueCont)
    assert cont.getUnitRef().getValue() == "/Units/N"
    assert cont.getUnitRef().getDest() == "UNIT"
    assert float(cont.getSwArraysize().getV().getValue()) == 2.0
    assert cont.getRuleBasedValues().getRule().getValue() == "FILL_UNTIL_END"
    assert float(cont.getRuleBasedValues().getArguments()[0].getV().getValue()) == 5.0


def test_read_absent_returns_none(parser):
    element = _wrap_application_spec("<CATEGORY>VAL_BLK</CATEGORY>")
    cont = parser.getRuleBasedValueCont(element)
    assert cont is None
