"""Reader tests for RuleArguments (Swc TPS Table 5.134, p.470).

The XSD group RULE-ARGUMENTS is an atpMixed choice over V (0..1), VF (0..1),
VT (0..1), VTF (0..1) and VARIATION-POINT; the complexType RULE-ARGUMENTS
wraps AR-OBJECT + the group. All reads assert field values.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, VerbatimString
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import NumericalOrText
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
    return ET.fromstring('<RULE-ARGUMENTS xmlns="%s">%s</RULE-ARGUMENTS>' % (NS, content))


def test_read_v(parser):
    arguments = parser.getRuleArguments(_wrap("<V>1.5</V>"))
    assert arguments is not None
    assert isinstance(arguments.getV(), Numerical)
    assert float(arguments.getV().getValue()) == 1.5
    assert arguments.getVf() is None
    assert arguments.getVt() is None
    assert arguments.getVtf() is None


def test_read_vf(parser):
    arguments = parser.getRuleArguments(_wrap("<VF>2.5</VF>"))
    assert arguments is not None
    assert isinstance(arguments.getVf(), Numerical)
    assert float(arguments.getVf().getValue()) == 2.5
    assert arguments.getV() is None


def test_read_vt(parser):
    arguments = parser.getRuleArguments(_wrap("<VT>open|closed</VT>"))
    assert arguments is not None
    assert isinstance(arguments.getVt(), VerbatimString)
    assert arguments.getVt().getValue() == "open|closed"


def test_read_vtf(parser):
    arguments = parser.getRuleArguments(_wrap("<VTF><VF>3.5</VF></VTF>"))
    assert arguments is not None
    vtf = arguments.getVtf()
    assert isinstance(vtf, NumericalOrText)
    assert float(vtf.getVf().getValue()) == 3.5
    assert vtf.getVt() is None


def test_read_empty(parser):
    arguments = parser.getRuleArguments(_wrap(""))
    assert arguments is not None
    assert arguments.getV() is None
    assert arguments.getVf() is None
    assert arguments.getVt() is None
    assert arguments.getVtf() is None
