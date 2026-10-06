"""Reader tests for SwAxisCont (Swc TPS Table 5.124, p.457).

XSD group SW-AXIS-CONT: CATEGORY, UNIT-REF, UNIT-DISPLAY-NAME, SW-AXIS-INDEX,
SW-ARRAYSIZE, SW-VALUES-PHYS. Reads go through the dedicated helper and the
APPLICATION-VALUE-SPECIFICATION dispatch; all reads assert field values.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType
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
    return ET.fromstring('<SW-AXIS-CONT xmlns="%s">%s</SW-AXIS-CONT>' % (NS, content))


def test_read_full_fields(parser):
    element = _wrap(
        "<CATEGORY>STD_AXIS</CATEGORY>"
        '<UNIT-REF DEST="UNIT">/Units/Nm</UNIT-REF>'
        "<UNIT-DISPLAY-NAME>Nm<SUB>s</SUB></UNIT-DISPLAY-NAME>"
        "<SW-AXIS-INDEX>2</SW-AXIS-INDEX>"
        "<SW-ARRAYSIZE><V>3</V></SW-ARRAYSIZE>"
        "<SW-VALUES-PHYS><V>0.5</V><V>1.5</V></SW-VALUES-PHYS>"
    )
    axis_cont = parser.getSwAxisCont(element)
    assert axis_cont is not None
    assert axis_cont.getCategory() is not None
    assert axis_cont.getCategory().getValue() == "stdAxis"
    assert axis_cont.getUnitRef() is not None
    assert axis_cont.getUnitRef().getValue() == "/Units/Nm"
    assert axis_cont.getUnitRef().getDest() == "UNIT"
    assert axis_cont.getUnitDisplayName() is not None
    assert axis_cont.getUnitDisplayName().getMixedString() == "Nm"
    assert isinstance(axis_cont.getSwAxisIndex(), AxisIndexType)
    assert axis_cont.getSwAxisIndex().getValue() == "2"
    assert float(axis_cont.getSwArraysize().getV().getValue()) == 3.0
    assert [float(v.getValue()) for v in axis_cont.getSwValuesPhys().getVs()] == [0.5, 1.5]


def test_read_empty(parser):
    axis_cont = parser.getSwAxisCont(_wrap(""))
    assert axis_cont is not None
    assert axis_cont.getCategory() is None
    assert axis_cont.getSwArraysize() is None
    assert axis_cont.getSwValuesPhys() is None


def test_read_through_application_value_specification(parser):
    element = ET.fromstring(
        '<APPLICATION-VALUE-SPECIFICATION xmlns="%s">'
        "<SW-AXIS-CONTS>"
        "<SW-AXIS-CONT><CATEGORY>RES_AXIS</CATEGORY><SW-AXIS-INDEX>1</SW-AXIS-INDEX></SW-AXIS-CONT>"
        "</SW-AXIS-CONTS>"
        "</APPLICATION-VALUE-SPECIFICATION>" % NS
    )
    spec = parser.getApplicationValueSpecification(element)
    axis_conts = spec.getSwAxisConts()
    assert len(axis_conts) == 1
    assert isinstance(axis_conts[0], SwAxisCont)
    assert axis_conts[0].getCategory().getValue() == "resAxis"
    assert axis_conts[0].getSwAxisIndex().getValue() == "1"
