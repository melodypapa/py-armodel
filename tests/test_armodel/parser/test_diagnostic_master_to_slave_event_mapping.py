"""Parser tests for DiagnosticMasterToSlaveEventMapping (Table 5.29, p.256).

XSD group DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING element order (AUTOSAR_00052.xsd): MASTER-EVENT-REF, SLAVE-EVENT-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMasterToSlaveEventMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticMasterToSlaveEventMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticMasterToSlaveEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<MASTER-EVENT-REF DEST='DEST'>/AUTOSAR/MasterEvent1</MASTER-EVENT-REF><SLAVE-EVENT-REF DEST='DEST'>/AUTOSAR/SlaveEvent1</SLAVE-EVENT-REF>"
        )
        parser.readDiagnosticMasterToSlaveEventMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getMasterEventRef() is not None
        assert mapping.getMasterEventRef().getValue() == "/AUTOSAR/MasterEvent1"
        assert mapping.getSlaveEventRef() is not None
        assert mapping.getSlaveEventRef().getValue() == "/AUTOSAR/SlaveEvent1"

    def test_read_empty(self, parser):
        mapping = DiagnosticMasterToSlaveEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticMasterToSlaveEventMapping(element, mapping)
        assert mapping.getMasterEventRef() is None
        assert mapping.getSlaveEventRef() is None
