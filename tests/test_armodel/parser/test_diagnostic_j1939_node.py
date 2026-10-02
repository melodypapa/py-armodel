"""Parser tests for DiagnosticJ1939Node (Table 5.41, p.267).

XSD group DIAGNOSTIC-J-1939-NODE element order (AUTOSAR_00052.xsd): NM-NODE-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939Node

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-J-1939-NODE") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticJ1939Node:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticJ1939Node(AUTOSAR.getInstance(), "M1")
        element = _snip("<SHORT-NAME>M1</SHORT-NAME>" "<NM-NODE-REF DEST='DEST'>/AUTOSAR/NmNode1</NM-NODE-REF>")
        parser.readDiagnosticJ1939Node(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getNmNodeRef() is not None
        assert mapping.getNmNodeRef().getValue() == "/AUTOSAR/NmNode1"

    def test_read_empty(self, parser):
        mapping = DiagnosticJ1939Node(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticJ1939Node(element, mapping)
        assert mapping.getNmNodeRef() is None
