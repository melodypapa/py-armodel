"""
Tests for writing EcucDerivationSpecification (Table 2.38) and EcucQuery
(Table 2.40) content, R23-11.

Element orders (XSD groups): DERIVATION → CALCULATION-FORMULA, ECUC-QUERYS,
INFORMAL-FORMULA; ECUC-QUERY → ECUC-QUERY-EXPRESSION.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_derivation_query.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDerivationSpecification, EcucQuery, EcucQueryExpression
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucDerivationAndQuery:
    def test_write_derivation_with_queries(self):
        """Test that the derivation aggregation is emitted with its queries."""
        derivation = EcucDerivationSpecification()
        query = derivation.createEcucQuery("Query1")
        query.setEcucQueryExpression(EcucQueryExpression())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucDerivationSpecification(parent, derivation)

        element = parent.find("DERIVATION")
        queries = element.findall("ECUC-QUERYS/ECUC-QUERY")
        assert len(queries) == 1
        assert queries[0].find("SHORT-NAME").text == "Query1"

    def test_write_query_expression(self):
        """Test that the ecucQueryExpression aggregation is emitted."""
        query = EcucQuery(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Query1")
        query.setEcucQueryExpression(EcucQueryExpression())

        element = ET.Element("ECUC-QUERY")
        ARXMLWriter().writeEcucQuery(element, query)

        assert element.find("SHORT-NAME").text == "Query1"
        assert element.find("ECUC-QUERY-EXPRESSION") is not None
