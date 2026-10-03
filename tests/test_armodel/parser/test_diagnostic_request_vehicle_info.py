"""Parser tests for DiagnosticRequestVehicleInfo (Table 4.144, p.160).

XSD group DIAGNOSTIC-REQUEST-VEHICLE-INFO (AUTOSAR_00052.xsd l.42539) element
order: INFO-TYPE-REF, REQUEST-VEHICLE-INFORMATION-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_vehicle_info.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestVehicleInfo

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-VEHICLE-INFO") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestVehicleInfo:
    def test_read_sets_all_fields(self, parser):
        mode09 = DiagnosticRequestVehicleInfo(AUTOSAR.getInstance(), "Mode09")
        element = _snip(
            "<SHORT-NAME>Mode09</SHORT-NAME>"
            "<INFO-TYPE-REF DEST='DIAGNOSTIC-INFO-TYPE'>/AUTOSAR/DiagnosticInfoTypes/InfoType1</INFO-TYPE-REF>"
            "<REQUEST-VEHICLE-INFORMATION-CLASS-REF DEST='DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS'>/AUTOSAR/DiagnosticRequestVehicleInfoClasses/Class1</REQUEST-VEHICLE-INFORMATION-CLASS-REF>"
        )
        parser.readDiagnosticRequestVehicleInfo(element, mode09)
        assert mode09.getShortName() == "Mode09"
        assert mode09.getInfoTypeRef() is not None
        assert mode09.getInfoTypeRef().getValue() == "/AUTOSAR/DiagnosticInfoTypes/InfoType1"
        assert mode09.getInfoTypeRef().getDest() == "DIAGNOSTIC-INFO-TYPE"
        assert mode09.getRequestVehicleInformationClassRef() is not None
        assert mode09.getRequestVehicleInformationClassRef().getValue() == "/AUTOSAR/DiagnosticRequestVehicleInfoClasses/Class1"
        assert mode09.getRequestVehicleInformationClassRef().getDest() == "DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS"

    def test_read_empty(self, parser):
        mode09 = DiagnosticRequestVehicleInfo(AUTOSAR.getInstance(), "Mode09")
        element = _snip("<SHORT-NAME>Mode09</SHORT-NAME>")
        parser.readDiagnosticRequestVehicleInfo(element, mode09)
        assert mode09.getInfoTypeRef() is None
        assert mode09.getRequestVehicleInformationClassRef() is None
