"""Reader tests for the BlueprintGenerator element (FORMAL-BLUEPRINT-GENERATOR).

Spec: R23-11 AUTOSAR_FO_TPS_GenericStructureTemplate, Table E.12, pp.424-425
(appendix E caption-shift: the body renders above the caption). XSD 00052 group
BLUEPRINT-GENERATOR (line 9083): INTRODUCTION (offset 10) before EXPRESSION
(offset 20); consumed as VariationPoint.formalBlueprintGenerator.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import (
    BlueprintGenerator,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadBlueprintGenerator:
    def test_read_full_introduction_and_expression(self):
        xml = (
            "<FORMAL-BLUEPRINT-GENERATOR xmlns='%s'>"
            "<INTRODUCTION><P><L-1 L='EN'>Resolve the derivation with the formal expression.</L-1></P></INTRODUCTION>"
            '<EXPRESSION>LET Name = "Example";</EXPRESSION>'
            "</FORMAL-BLUEPRINT-GENERATOR>" % NS
        )
        element = ET.fromstring(xml)

        generator = ARXMLParser().readBlueprintGenerator(element, BlueprintGenerator())

        assert isinstance(generator, BlueprintGenerator)
        introduction = generator.getIntroduction()
        assert introduction is not None
        assert introduction.getPs()[0].getL1s()[0].getValue() == "Resolve the derivation with the formal expression."
        expression = generator.getExpression()
        assert expression is not None
        assert expression.getValue() == 'LET Name = "Example";'

    def test_read_expression_only_leaves_introduction_none(self):
        xml = "<FORMAL-BLUEPRINT-GENERATOR xmlns='%s'><EXPRESSION>defined(VAR)</EXPRESSION></FORMAL-BLUEPRINT-GENERATOR>" % NS
        element = ET.fromstring(xml)

        generator = ARXMLParser().readBlueprintGenerator(element, BlueprintGenerator())

        assert generator.getIntroduction() is None
        assert generator.getExpression().getValue() == "defined(VAR)"

    def test_read_empty_generator_leaves_both_none(self):
        xml = "<FORMAL-BLUEPRINT-GENERATOR xmlns='%s'/>" % NS
        element = ET.fromstring(xml)

        generator = ARXMLParser().readBlueprintGenerator(element, BlueprintGenerator())

        assert isinstance(generator, BlueprintGenerator)
        assert generator.getIntroduction() is None
        assert generator.getExpression() is None
