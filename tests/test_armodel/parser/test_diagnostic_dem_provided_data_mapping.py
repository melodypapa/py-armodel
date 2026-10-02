"""Parser tests for DiagnosticDemProvidedDataMapping (Table 5.28, p.255).

XSD group DIAGNOSTIC-DEM-PROVIDED-DATA-MAPPING element order (AUTOSAR_00052.xsd): DATA-ELEMENT-REF, DATA-PROVIDER.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDemProvidedDataMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-DEM-PROVIDED-DATA-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticDemProvidedDataMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticDemProvidedDataMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("<SHORT-NAME>M1</SHORT-NAME>" "<DATA-ELEMENT-REF DEST='DEST'>/AUTOSAR/DataElement1</DATA-ELEMENT-REF><DATA-PROVIDER>provider</DATA-PROVIDER>")
        parser.readDiagnosticDemProvidedDataMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDataElementRef() is not None
        assert mapping.getDataElementRef().getValue() == "/AUTOSAR/DataElement1"
        assert mapping.getDataProvider() is not None
        assert mapping.getDataProvider().getValue() == "provider"

    def test_read_empty(self, parser):
        mapping = DiagnosticDemProvidedDataMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticDemProvidedDataMapping(element, mapping)
        assert mapping.getDataElementRef() is None
        assert mapping.getDataProvider() is None
