"""Parser tests for DiagnosticTestRoutineIdentifier (Table 4.143, p.158).

XSD group DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER (AUTOSAR_00052.xsd l.46056) element
order: ID, REQUEST-DATA-SIZE, RESPONSE-DATA-SIZE.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_test_routine_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTestRoutineIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticTestRoutineIdentifier:
    def test_read_sets_all_fields(self, parser):
        routine_identifier = DiagnosticTestRoutineIdentifier(AUTOSAR.getInstance(), "Routine1")
        element = _snip("<SHORT-NAME>Routine1</SHORT-NAME>" "<ID>1</ID>" "<REQUEST-DATA-SIZE>8</REQUEST-DATA-SIZE>" "<RESPONSE-DATA-SIZE>16</RESPONSE-DATA-SIZE>")
        parser.readDiagnosticTestRoutineIdentifier(element, routine_identifier)
        assert routine_identifier.getShortName() == "Routine1"
        assert routine_identifier.getId() is not None
        assert routine_identifier.getId().getValue() == 1
        assert routine_identifier.getRequestDataSize() is not None
        assert routine_identifier.getRequestDataSize().getValue() == 8
        assert routine_identifier.getResponseDataSize() is not None
        assert routine_identifier.getResponseDataSize().getValue() == 16

    def test_read_empty(self, parser):
        routine_identifier = DiagnosticTestRoutineIdentifier(AUTOSAR.getInstance(), "Routine1")
        element = _snip("<SHORT-NAME>Routine1</SHORT-NAME>")
        parser.readDiagnosticTestRoutineIdentifier(element, routine_identifier)
        assert routine_identifier.getId() is None
        assert routine_identifier.getRequestDataSize() is None
        assert routine_identifier.getResponseDataSize() is None
