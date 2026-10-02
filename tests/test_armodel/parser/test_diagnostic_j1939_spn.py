"""Parser tests for DiagnosticJ1939Spn (Table 4.219, p.219).

XSD group DIAGNOSTIC-J-1939-SPN (AUTOSAR_00052.xsd l.39071) element order:
SPN.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939Spn

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-J-1939-SPN") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticJ1939Spn:
    def test_read_sets_all_fields(self, parser):
        spn = DiagnosticJ1939Spn(AUTOSAR.getInstance(), "Spn")
        element = _snip("<SHORT-NAME>Spn</SHORT-NAME><SPN>19000</SPN>")
        parser.readDiagnosticJ1939Spn(element, spn)
        assert spn.getShortName() == "Spn"
        assert spn.getSpn() is not None
        assert spn.getSpn().getValue() == 19000

    def test_read_empty(self, parser):
        spn = DiagnosticJ1939Spn(AUTOSAR.getInstance(), "Spn")
        element = _snip("")
        parser.readDiagnosticJ1939Spn(element, spn)
        assert spn.getSpn() is None
