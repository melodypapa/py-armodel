"""Parser tests for DiagnosticServiceDataMapping (Table 5.4, p.228) and
DiagnosticParameterElementAccess (Table 5.5, p.229).

XSD complexType DIAGNOSTIC-SERVICE-DATA-MAPPING element order: infrastructure
groups, DIAGNOSTIC-MAPPING group (provider/requester refs), then own group
(l.43661): DIAGNOSTIC-DATA-ELEMENT-REF, MAPPED-DATA-ELEMENT-IREF,
PARAMETER-ELEMENT-ACCESS, DIAGNOSTIC-PARAMETER-REF.
Own group DIAGNOSTIC-PARAMETER-ELEMENT-ACCESS (l.40680): CONTEXT-ELEMENT-REFS/
CONTEXT-ELEMENT-REF, TARGET-ELEMENT-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticServiceDataMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-SERVICE-DATA-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticServiceDataMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticServiceDataMapping(AUTOSAR.getInstance(), "Mapping")
        element = _snip(
            "<SHORT-NAME>Mapping</SHORT-NAME>"
            "<PROVIDER-SOFTWARE-CLUSTER-REF DEST='CP-SOFTWARE-CLUSTER'>/AUTOSAR/Clusters/C1</PROVIDER-SOFTWARE-CLUSTER-REF>"
            "<DIAGNOSTIC-DATA-ELEMENT-REF DEST='DIAGNOSTIC-DATA-ELEMENT'>/AUTOSAR/DataElements/Did1</DIAGNOSTIC-DATA-ELEMENT-REF>"
            "<MAPPED-DATA-ELEMENT-IREF DEST='DATA-PROTOTYPE'>/AUTOSAR/System/DataProtos/Proto1</MAPPED-DATA-ELEMENT-IREF>"
            "<PARAMETER-ELEMENT-ACCESS>"
            "<CONTEXT-ELEMENT-REFS>"
            "<CONTEXT-ELEMENT-REF DEST='DIAGNOSTIC-PARAMETER-ELEMENT'>/AUTOSAR/ParamElements/Ctx1</CONTEXT-ELEMENT-REF>"
            "</CONTEXT-ELEMENT-REFS>"
            "<TARGET-ELEMENT-REF DEST='DIAGNOSTIC-PARAMETER-ELEMENT'>/AUTOSAR/ParamElements/Target</TARGET-ELEMENT-REF>"
            "</PARAMETER-ELEMENT-ACCESS>"
            "<DIAGNOSTIC-PARAMETER-REF DEST='DIAGNOSTIC-PARAMETER-IDENT'>/AUTOSAR/ParamIdents/Ident1</DIAGNOSTIC-PARAMETER-REF>"
        )
        parser.readDiagnosticServiceDataMapping(element, mapping)
        assert mapping.getShortName() == "Mapping"
        assert mapping.getProviderSoftwareClusterRef().getValue() == "/AUTOSAR/Clusters/C1"
        assert mapping.getDiagnosticDataElementRef().getValue() == "/AUTOSAR/DataElements/Did1"
        assert mapping.getMappedDataElementIRef().getValue() == "/AUTOSAR/System/DataProtos/Proto1"
        pea = mapping.getParameterElementAccess()
        assert pea is not None
        assert len(pea.getContextElementRefs()) == 1
        assert pea.getContextElementRefs()[0].getValue() == "/AUTOSAR/ParamElements/Ctx1"
        assert pea.getTargetElementRef().getValue() == "/AUTOSAR/ParamElements/Target"
        assert mapping.getDiagnosticParameterRef().getValue() == "/AUTOSAR/ParamIdents/Ident1"

    def test_read_empty(self, parser):
        mapping = DiagnosticServiceDataMapping(AUTOSAR.getInstance(), "Mapping")
        element = _snip("")
        parser.readDiagnosticServiceDataMapping(element, mapping)
        assert mapping.getDiagnosticDataElementRef() is None
        assert mapping.getDiagnosticParameterRef() is None
        assert mapping.getMappedDataElementIRef() is None
        assert mapping.getParameterElementAccess() is None
