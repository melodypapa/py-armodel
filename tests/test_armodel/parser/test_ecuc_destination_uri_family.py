"""Parser tests for the destination-uri family (Tables 2.34/2.35/2.36) and
EcucDerivationSpecification (2.38) + EcucQuery (2.40).

Element orders (XSD groups): ECUC-DESTINATION-URI-DEF-SET →
DESTINATION-URI-DEFS; ECUC-DESTINATION-URI-DEF → DESTINATION-URI-POLICY;
ECUC-DESTINATION-URI-POLICY → CONTAINERS, DESTINATION-URI-NESTING-CONTRACT,
PARAMETERS, REFERENCES; DERIVATION → CALCULATION-FORMULA, ECUC-QUERYS,
INFORMAL-FORMULA; ECUC-QUERY → ECUC-QUERY-EXPRESSION.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDestinationUriDef, EcucDestinationUriDefSet, EcucDestinationUriPolicy

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestReadEcucDestinationUriFamily:
    def test_read_uri_def_set(self, parser):
        uri_def_set = EcucDestinationUriDefSet(AUTOSAR.getInstance(), "UriDefSet")
        element = ET.fromstring(
            f"<ECUC-DESTINATION-URI-DEF-SET xmlns='{NS}'>"
            "<SHORT-NAME>UriDefSet</SHORT-NAME>"
            "<DESTINATION-URI-DEFS>"
            "<ECUC-DESTINATION-URI-DEF><SHORT-NAME>UriDef1</SHORT-NAME></ECUC-DESTINATION-URI-DEF>"
            "</DESTINATION-URI-DEFS>"
            "</ECUC-DESTINATION-URI-DEF-SET>"
        )
        parser.readEcucDestinationUriDefSet(element, uri_def_set)
        defs = uri_def_set.getDestinationUriDefs()
        assert len(defs) == 1
        assert isinstance(defs[0], EcucDestinationUriDef)
        assert defs[0].getShortName() == "UriDef1"

    def test_read_uri_def_with_policy(self, parser):
        uri_def = EcucDestinationUriDef(AUTOSAR.getInstance(), "UriDef")
        element = ET.fromstring(
            f"<ECUC-DESTINATION-URI-DEF xmlns='{NS}'>"
            "<SHORT-NAME>UriDef</SHORT-NAME>"
            "<DESTINATION-URI-POLICY>"
            "<DESTINATION-URI-NESTING-CONTRACT>TARGET-CONTAINER</DESTINATION-URI-NESTING-CONTRACT>"
            "</DESTINATION-URI-POLICY>"
            "</ECUC-DESTINATION-URI-DEF>"
        )
        parser.readEcucDestinationUriDef(element, uri_def)
        policy = uri_def.getDestinationUriPolicy()
        assert isinstance(policy, EcucDestinationUriPolicy)
        assert policy.getDestinationUriNestingContract().getValue() == "TARGET-CONTAINER"
