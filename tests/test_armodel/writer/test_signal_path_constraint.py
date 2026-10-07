"""Writer round-trip tests for SignalPathConstraint (Table F.114, R23-11 markdown appendix).

Serialized through the SIGNAL-PATH-CONSTRAINT group
(INTRODUCTION emitted only when set; VARIATION-POINT via the
VariationPointCapable mixin) and the SIGNAL-PATH-CONSTRAINTS wrapper of
SystemMapping (AUTOSAR_00052.xsd l.119632).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SignalPathConstraint
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class ConcreteSignalPathConstraint(SignalPathConstraint):
    pass


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _introduction(text: str) -> DocumentationBlock:
    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setValue(text)
    paragraph.addL1(l1)
    block.addP(paragraph)
    return block


class TestWriteSignalPathConstraint:
    def test_empty_no_introduction(self):
        constraint = ConcreteSignalPathConstraint()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSignalPathConstraint(parent, constraint)

        assert parent.find("INTRODUCTION") is None

    def test_full(self):
        constraint = ConcreteSignalPathConstraint()
        constraint.setIntroduction(_introduction("The introduction text."))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSignalPathConstraint(parent, constraint)

        node = parent.find("INTRODUCTION")
        assert node is not None
        assert node.find("P/L-1").text == "The introduction text."

    def test_round_trip_full(self):
        constraint = ConcreteSignalPathConstraint()
        constraint.setIntroduction(_introduction("The introduction text."))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSignalPathConstraint(parent, constraint)

        reloaded = ConcreteSignalPathConstraint()
        ARXMLParser().readSignalPathConstraint(_with_ns(parent), reloaded)

        introduction = reloaded.getIntroduction()
        assert introduction is not None
        assert introduction.getPs()[0].getL1s()[0].getValue() == "The introduction text."
