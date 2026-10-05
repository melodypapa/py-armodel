"""Reader tests for ApplicationValueSpecification (Swc TPS Table 5.122, p.455).

The XSD group APPLICATION-VALUE-SPECIFICATION (AUTOSAR_00052.xsd) fixes the
child element order: CATEGORY, SW-AXIS-CONTS (wrapper of SW-AXIS-CONT
elements), SW-VALUE-CONT. All reads assert field values.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationValueSpecification
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont
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
    return ET.fromstring('<APPLICATION-VALUE-SPECIFICATION xmlns="%s">%s</APPLICATION-VALUE-SPECIFICATION>' % (NS, content))


def test_read_full(parser):
    element = _wrap(
        "<SHORT-LABEL>init</SHORT-LABEL>"
        "<CATEGORY>VALUE</CATEGORY>"
        "<SW-AXIS-CONTS>"
        "<SW-AXIS-CONT><CATEGORY>STD_AXIS</CATEGORY></SW-AXIS-CONT>"
        "<SW-AXIS-CONT><CATEGORY>COM_AXIS</CATEGORY></SW-AXIS-CONT>"
        "</SW-AXIS-CONTS>"
        "<SW-VALUE-CONT>"
        '<UNIT-REF DEST="UNIT">/Units/Nm</UNIT-REF>'
        "<SW-ARRAYSIZE><V>2</V></SW-ARRAYSIZE>"
        "<SW-VALUES-PHYS><V>1.5</V><V>2.5</V></SW-VALUES-PHYS>"
        "</SW-VALUE-CONT>"
    )
    spec = parser.getApplicationValueSpecification(element)
    assert spec is not None
    assert spec.getCategory() is not None
    assert spec.getCategory().getValue() == "VALUE"
    assert spec.getShortLabel() is not None
    assert spec.getShortLabel().getValue() == "init"
    assert len(spec.getSwAxisConts()) == 2

    cont = spec.getSwValueCont()
    assert isinstance(cont, SwValueCont)
    assert cont.getUnitRef() is not None
    assert cont.getUnitRef().getValue() == "/Units/Nm"
    assert cont.getUnitRef().getDest() == "UNIT"
    assert float(cont.getSwArraysize().getV().getValue()) == 2.0
    assert [float(v.getValue()) for v in cont.getSwValuesPhys().getVs()] == [1.5, 2.5]


def test_read_without_axis_conts(parser):
    element = _wrap("<CATEGORY>BOOLEAN</CATEGORY>" "<SW-VALUE-CONT><SW-VALUES-PHYS><V>1</V></SW-VALUES-PHYS></SW-VALUE-CONT>")
    spec = parser.getApplicationValueSpecification(element)
    assert spec is not None
    assert spec.getSwAxisConts() == []
    assert float(spec.getSwValueCont().getSwValuesPhys().getVs()[0].getValue()) == 1.0


def test_read_empty_element(parser):
    element = _wrap("")
    spec = parser.getApplicationValueSpecification(element)
    assert spec is not None
    assert spec.getCategory() is None
    assert spec.getSwAxisConts() == []
    assert spec.getSwValueCont() is None


def test_dispatch_via_get_value_specification(parser):
    element = _wrap("<CATEGORY>VALUE</CATEGORY>")
    value_spec = parser.getValueSpecification(element, "APPLICATION-VALUE-SPECIFICATION")
    assert isinstance(value_spec, ApplicationValueSpecification)
    assert value_spec.getCategory().getValue() == "VALUE"
