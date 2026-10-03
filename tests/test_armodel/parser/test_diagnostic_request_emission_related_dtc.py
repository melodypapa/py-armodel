"""Parser tests for DiagnosticRequestEmissionRelatedDTC (Table 4.135, p.154).

XSD group DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC (AUTOSAR_00052.xsd l.41879)
element order: REQUEST-EMISSION-RELATED-DTC-CLASS-REF (single 0..1).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_emission_related_dtc.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestEmissionRelatedDTC

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestEmissionRelatedDTC:
    def test_read_sets_all_fields(self, parser):
        mode0307 = DiagnosticRequestEmissionRelatedDTC(AUTOSAR.getInstance(), "Mode0307")
        element = _snip(
            "<SHORT-NAME>Mode0307</SHORT-NAME>"
            "<REQUEST-EMISSION-RELATED-DTC-CLASS-REF DEST='DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS'>/AUTOSAR/DiagnosticRequestEmissionRelatedDTCClasses/Class1</REQUEST-EMISSION-RELATED-DTC-CLASS-REF>"
        )
        parser.readDiagnosticRequestEmissionRelatedDTC(element, mode0307)
        assert mode0307.getShortName() == "Mode0307"
        assert mode0307.getRequestEmissionRelatedDtcClassRef() is not None
        assert mode0307.getRequestEmissionRelatedDtcClassRef().getValue() == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCClasses/Class1"
        assert mode0307.getRequestEmissionRelatedDtcClassRef().getDest() == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS"

    def test_read_empty(self, parser):
        mode0307 = DiagnosticRequestEmissionRelatedDTC(AUTOSAR.getInstance(), "Mode0307")
        element = _snip("<SHORT-NAME>Mode0307</SHORT-NAME>")
        parser.readDiagnosticRequestEmissionRelatedDTC(element, mode0307)
        assert mode0307.getRequestEmissionRelatedDtcClassRef() is None
