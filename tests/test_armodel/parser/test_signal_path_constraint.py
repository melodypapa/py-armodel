"""Reader tests for SignalPathConstraint (Table F.114, R23-11 markdown appendix).

XML group SIGNAL-PATH-CONSTRAINT (AUTOSAR_00052.xsd l.107091):
INTRODUCTION (DOCUMENTATION-BLOCK) + VARIATION-POINT (atpVariation via
SystemMapping.signalPathConstraint). Abstract class — exercised through a
concrete subclass; the helper is reused by CommonSignalPath and siblings.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SignalPathConstraint
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class ConcreteSignalPathConstraint(SignalPathConstraint):
    pass


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


class TestReadSignalPathConstraint:
    def test_read_full(self):
        xml = (
            """
        <CONSTRAINT xmlns="%s">
            <INTRODUCTION>
                <P><L-1>The introduction text.</L-1></P>
            </INTRODUCTION>
        </CONSTRAINT>
        """
            % NS
        )
        element = _parse(xml)
        constraint = ConcreteSignalPathConstraint()
        ARXMLParser().readSignalPathConstraint(element, constraint)

        introduction = constraint.getIntroduction()
        assert introduction is not None
        paragraphs = introduction.getPs()
        assert len(paragraphs) == 1
        assert paragraphs[0].getL1s()[0].getValue() == "The introduction text."

    def test_read_empty(self):
        xml = '<CONSTRAINT xmlns="%s"/>' % NS
        element = _parse(xml)
        constraint = ConcreteSignalPathConstraint()
        ARXMLParser().readSignalPathConstraint(element, constraint)

        assert constraint.getIntroduction() is None
