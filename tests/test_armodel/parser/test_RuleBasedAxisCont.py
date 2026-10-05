"""Reader tests for RuleBasedAxisCont (Swc TPS Table 5.130, p.464).

The XSD group RULE-BASED-AXIS-CONT fixes the child element order:
CATEGORY (20), UNIT-REF (30), SW-ARRAYSIZE (40), SW-AXIS-INDEX (50),
RULE-BASED-VALUES (80, role element of RULE-BASED-VALUE-SPECIFICATION).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import RuleBasedAxisCont
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
    return ET.fromstring('<RULE-BASED-AXIS-CONT xmlns="%s">%s</RULE-BASED-AXIS-CONT>' % (NS, content))


def test_read_full(parser):
    element = _wrap(
        "<CATEGORY>COM_AXIS</CATEGORY>"
        '<UNIT-REF DEST="UNIT">/Units/N</UNIT-REF>'
        "<SW-ARRAYSIZE><V>3</V></SW-ARRAYSIZE>"
        "<SW-AXIS-INDEX>2</SW-AXIS-INDEX>"
        "<RULE-BASED-VALUES><RULE>FILL_UNTIL_END</RULE></RULE-BASED-VALUES>"
    )
    cont = parser.getRuleBasedAxisCont(element)
    assert cont is not None
    assert isinstance(cont, RuleBasedAxisCont)
    assert cont.getCategory().getValue() == "comAxis"
    assert cont.getUnitRef().getValue() == "/Units/N"
    assert cont.getUnitRef().getDest() == "UNIT"
    assert float(cont.getSwArraysize().getV().getValue()) == 3.0
    assert cont.getSwAxisIndex().getValue() == "2"
    assert cont.getRuleBasedValues().getRule().getValue() == "FILL_UNTIL_END"


def test_read_empty(parser):
    element = _wrap("")
    cont = parser.getRuleBasedAxisCont(element)
    assert cont is not None
    assert cont.getCategory() is None
    assert cont.getUnitRef() is None
    assert cont.getSwArraysize() is None
    assert cont.getSwAxisIndex() is None
    assert cont.getRuleBasedValues() is None
