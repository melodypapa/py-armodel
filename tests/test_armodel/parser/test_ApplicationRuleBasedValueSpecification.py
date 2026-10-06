"""Reader tests for ApplicationRuleBasedValueSpecification (Swc TPS Table 5.129, p.463).

The XSD group APPLICATION-RULE-BASED-VALUE-SPECIFICATION fixes the child
element order: CATEGORY (offset -20), SW-AXIS-CONTS (wrapper of unbounded
RULE-BASED-AXIS-CONT elements), SW-VALUE-CONT (type RULE-BASED-VALUE-CONT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationRuleBasedValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
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
    return ET.fromstring('<APPLICATION-RULE-BASED-VALUE-SPECIFICATION xmlns="%s">%s</APPLICATION-RULE-BASED-VALUE-SPECIFICATION>' % (NS, content))


def test_read_full(parser):
    element = _wrap(
        "<CATEGORY>VAL_BLK</CATEGORY>"
        "<SW-AXIS-CONTS>"
        "<RULE-BASED-AXIS-CONT><CATEGORY>STD_AXIS</CATEGORY></RULE-BASED-AXIS-CONT>"
        "<RULE-BASED-AXIS-CONT><CATEGORY>COM_AXIS</CATEGORY></RULE-BASED-AXIS-CONT>"
        "</SW-AXIS-CONTS>"
        "<SW-VALUE-CONT>"
        '<UNIT-REF DEST="UNIT">/Units/Nm</UNIT-REF>'
        "<SW-ARRAYSIZE><V>2</V></SW-ARRAYSIZE>"
        "</SW-VALUE-CONT>"
    )
    spec = parser.getApplicationRuleBasedValueSpecification(element)
    assert spec is not None
    assert isinstance(spec.getCategory(), Identifier)
    assert spec.getCategory().getValue() == "VAL_BLK"
    assert len(spec.getSwAxisConts()) == 2
    assert spec.getSwAxisConts()[0].getCategory().getValue() == "STD-AXIS"

    cont = spec.getSwValueCont()
    assert cont is not None
    assert cont.getUnitRef().getValue() == "/Units/Nm"
    assert cont.getUnitRef().getDest() == "UNIT"
    assert float(cont.getSwArraysize().getV().getValue()) == 2.0
    assert cont.getRuleBasedValues() is None


def test_read_dispatch_via_get_value_specification(parser):
    element = _wrap("<CATEGORY>ARRAY</CATEGORY>")
    value_spec = parser.getValueSpecification(element, "APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
    assert isinstance(value_spec, ApplicationRuleBasedValueSpecification)
    assert value_spec.getCategory().getValue() == "ARRAY"


def test_read_empty(parser):
    element = _wrap("")
    spec = parser.getApplicationRuleBasedValueSpecification(element)
    assert spec is not None
    assert spec.getCategory() is None
    assert spec.getSwAxisConts() == []
    assert spec.getSwValueCont() is None
