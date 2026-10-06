"""Reader tests for NumericalOrText (Swc TPS Table 5.123, p.456).

XSD group NUMERICAL-OR-TEXT: VF (0..1), VT (0..1), VARIATION-POINT (0..1,
anchored by the atpVariation on RuleArguments.vtf / SwValues.vtf).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, String
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
    return ET.fromstring('<VTF xmlns="%s">%s</VTF>' % (NS, content))


def test_read_numerical(parser):
    not_text = parser.getNumericalOrText(_wrap("<VF>3.5</VF>"))
    assert not_text is not None
    assert isinstance(not_text.getVf(), Numerical)
    assert float(not_text.getVf().getValue()) == 3.5
    assert not_text.getVt() is None


def test_read_text(parser):
    not_text = parser.getNumericalOrText(_wrap("<VT>label|text</VT>"))
    assert not_text is not None
    assert isinstance(not_text.getVt(), String)
    assert not_text.getVt().getValue() == "label|text"
    assert not_text.getVf() is None


def test_read_empty(parser):
    not_text = parser.getNumericalOrText(_wrap(""))
    assert not_text is not None
    assert not_text.getVf() is None
    assert not_text.getVt() is None
