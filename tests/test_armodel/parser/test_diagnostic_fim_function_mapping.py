"""Parser tests for DiagnosticFimFunctionMapping (Table 5.37, p.265).

XSD group DIAGNOSTIC-FIM-FUNCTION-MAPPING element order (AUTOSAR_00052.xsd): MAPPED-BSW-SERVICE-DEPENDENCY-REF, MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF, MAPPED-FUNCTION-REF, MAPPED-SWC-SERVICE-DEPENDENCY-IREF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimFunctionMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-FIM-FUNCTION-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticFimFunctionMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticFimFunctionMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<MAPPED-BSW-SERVICE-DEPENDENCY-REF DEST='DEST'>/AUTOSAR/MappedBswServiceDependency1</MAPPED-BSW-SERVICE-DEPENDENCY-REF><MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF DEST='DEST'>/AUTOSAR/MappedFlatSwcServiceDependency1</MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF><MAPPED-FUNCTION-REF DEST='DEST'>/AUTOSAR/MappedFunction1</MAPPED-FUNCTION-REF><MAPPED-SWC-SERVICE-DEPENDENCY-IREF DEST='DEST'>/AUTOSAR/MappedSwcServiceDependency1</MAPPED-SWC-SERVICE-DEPENDENCY-IREF>"
        )
        parser.readDiagnosticFimFunctionMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getMappedBswServiceDependencyRef() is not None
        assert mapping.getMappedBswServiceDependencyRef().getValue() == "/AUTOSAR/MappedBswServiceDependency1"
        assert mapping.getMappedFlatSwcServiceDependencyRef() is not None
        assert mapping.getMappedFlatSwcServiceDependencyRef().getValue() == "/AUTOSAR/MappedFlatSwcServiceDependency1"
        assert mapping.getMappedFunctionRef() is not None
        assert mapping.getMappedFunctionRef().getValue() == "/AUTOSAR/MappedFunction1"
        assert mapping.getMappedSwcServiceDependencyRef() is not None
        assert mapping.getMappedSwcServiceDependencyRef().getValue() == "/AUTOSAR/MappedSwcServiceDependency1"

    def test_read_empty(self, parser):
        mapping = DiagnosticFimFunctionMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticFimFunctionMapping(element, mapping)
        assert mapping.getMappedBswServiceDependencyRef() is None
        assert mapping.getMappedFlatSwcServiceDependencyRef() is None
        assert mapping.getMappedFunctionRef() is None
        assert mapping.getMappedSwcServiceDependencyRef() is None
