"""Parser tests for DiagnosticFimEventGroup (Table 4.218, p.217).

XSD group DIAGNOSTIC-FIM-EVENT-GROUP (AUTOSAR_00052.xsd l.37639) element order:
EVENT-REFS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimEventGroup

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-FIM-EVENT-GROUP") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticFimEventGroup:
    def test_read_sets_all_fields(self, parser):
        group = DiagnosticFimEventGroup(AUTOSAR.getInstance(), "FimGroup")
        element = _snip(
            "<SHORT-NAME>FimGroup</SHORT-NAME>"
            "<EVENT-REFS>"
            '<EVENT-REF DEST="DIAGNOSTIC-EVENT">/AUTOSAR/DiagEvents/Evt1</EVENT-REF>'
            '<EVENT-REF DEST="DIAGNOSTIC-EVENT">/AUTOSAR/DiagEvents/Evt2</EVENT-REF>'
            "</EVENT-REFS>"
        )
        parser.readDiagnosticFimEventGroup(element, group)
        assert group.getShortName() == "FimGroup"
        refs = group.getEventRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/DiagEvents/Evt1"
        assert refs[0].getDest() == "DIAGNOSTIC-EVENT"
        assert refs[1].getValue() == "/AUTOSAR/DiagEvents/Evt2"
        assert refs[1].getDest() == "DIAGNOSTIC-EVENT"

    def test_read_empty(self, parser):
        group = DiagnosticFimEventGroup(AUTOSAR.getInstance(), "FimGroup")
        element = _snip("")
        parser.readDiagnosticFimEventGroup(element, group)
        assert group.getEventRefs() == []
