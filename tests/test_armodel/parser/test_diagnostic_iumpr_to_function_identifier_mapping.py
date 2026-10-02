"""Parser tests for DiagnosticIumprToFunctionIdentifierMapping (Table 5.39, p.265).

XSD group DIAGNOSTIC-IUMPR-TO-FUNCTION-IDENTIFIER-MAPPING element order (AUTOSAR_00052.xsd): FUNCTION-IDENTIFIER-REF, IUMPR-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumprToFunctionIdentifierMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-IUMPR-TO-FUNCTION-IDENTIFIER-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticIumprToFunctionIdentifierMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticIumprToFunctionIdentifierMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("<SHORT-NAME>M1</SHORT-NAME>" "<FUNCTION-IDENTIFIER-REF DEST='DEST'>/AUTOSAR/FunctionIdentifier1</FUNCTION-IDENTIFIER-REF><IUMPR-REF DEST='DEST'>/AUTOSAR/Iumpr1</IUMPR-REF>")
        parser.readDiagnosticIumprToFunctionIdentifierMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getFunctionIdentifierRef() is not None
        assert mapping.getFunctionIdentifierRef().getValue() == "/AUTOSAR/FunctionIdentifier1"
        assert mapping.getIumprRef() is not None
        assert mapping.getIumprRef().getValue() == "/AUTOSAR/Iumpr1"

    def test_read_empty(self, parser):
        mapping = DiagnosticIumprToFunctionIdentifierMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticIumprToFunctionIdentifierMapping(element, mapping)
        assert mapping.getFunctionIdentifierRef() is None
        assert mapping.getIumprRef() is None
