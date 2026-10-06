"""Parser tests for EcucDefinitionElement (Table 2.6, p.46).

XSD group ECUC-DEFINITION-ELEMENT (AUTOSAR_00052.xsd l.51829) element order:
RELATED-TRACE-ITEM-REF, ECUC-VALIDATION-CONDS, ECUC-COND, LOWER-MULTIPLICITY,
UPPER-MULTIPLICITY, UPPER-MULTIPLICITY-INFINITE, SCOPE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDefinitionElement

NS = "http://autosar.org/schema/r4.0"


class _Concrete(EcucDefinitionElement):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-VALIDATION-CONDITION") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucDefinitionElement:
    def test_read_sets_all_fields(self, parser):
        holder = _Concrete(AUTOSAR.getInstance(), "Holder")
        element = _snip(
            "<SHORT-NAME>Holder</SHORT-NAME>"
            "<RELATED-TRACE-ITEM-REF DEST='TRACEABLE'>/EcucId/Trace</RELATED-TRACE-ITEM-REF>"
            "<ECUC-VALIDATION-CONDS>"
            "<ECUC-VALIDATION-CONDITION><SHORT-NAME>C1</SHORT-NAME></ECUC-VALIDATION-CONDITION>"
            "</ECUC-VALIDATION-CONDS>"
            "<ECUC-COND><SHORT-NAME>Cond</SHORT-NAME></ECUC-COND>"
            "<LOWER-MULTIPLICITY>1</LOWER-MULTIPLICITY>"
            "<UPPER-MULTIPLICITY>4</UPPER-MULTIPLICITY>"
            "<UPPER-MULTIPLICITY-INFINITE>true</UPPER-MULTIPLICITY-INFINITE>"
            "<SCOPE>LOCAL</SCOPE>"
        )
        parser.readEcucDefinitionElement(element, holder)
        assert holder.getShortName() == "Holder"
        assert holder.getRelatedTraceItemRef().getValue() == "/EcucId/Trace"
        assert len(holder.getEcucValidationConds()) == 1
        assert holder.getEcucCond() is not None
        assert holder.getLowerMultiplicity().getValue() == 1
        assert holder.getUpperMultiplicity().getValue() == 4
        assert holder.getUpperMultiplicityInfinite().getValue() is True
        assert holder.getScope() is not None
        assert holder.getScope().getValue() == "LOCAL"

    def test_read_empty(self, parser):
        holder = _Concrete(AUTOSAR.getInstance(), "Holder")
        element = _snip("")
        parser.readEcucDefinitionElement(element, holder)
        assert holder.getRelatedTraceItemRef() is None
        assert holder.getEcucValidationConds() == []
        assert holder.getEcucCond() is None
        assert holder.getLowerMultiplicity() is None
        assert holder.getUpperMultiplicity() is None
        assert holder.getUpperMultiplicityInfinite() is None
        assert holder.getScope() is None
