"""Parser tests for DiagnosticJ1939SwMapping (Table 5.42, p.268).

XSD group DIAGNOSTIC-J-1939-SW-MAPPING element order (AUTOSAR_00052.xsd): NODE-REF, SW-COMPONENT-PROTOTYPE-IREF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939SwMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-J-1939-SW-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticJ1939SwMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticJ1939SwMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<NODE-REF DEST='DEST'>/AUTOSAR/Node1</NODE-REF><SW-COMPONENT-PROTOTYPE-IREF DEST='DEST'>/AUTOSAR/SwComponentPrototype1</SW-COMPONENT-PROTOTYPE-IREF>"
        )
        parser.readDiagnosticJ1939SwMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getNodeRef() is not None
        assert mapping.getNodeRef().getValue() == "/AUTOSAR/Node1"
        assert mapping.getSwComponentPrototypeRef() is not None
        assert mapping.getSwComponentPrototypeRef().getValue() == "/AUTOSAR/SwComponentPrototype1"

    def test_read_empty(self, parser):
        mapping = DiagnosticJ1939SwMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticJ1939SwMapping(element, mapping)
        assert mapping.getNodeRef() is None
        assert mapping.getSwComponentPrototypeRef() is None
