"""Writer round-trip tests for DiagnosticServiceInstance (Table 4.26, p.70).

DiagnosticServiceInstance is abstract: the helpers are content-only and the
concrete subclass owns the XML tag. Child order per XSD group
DIAGNOSTIC-SERVICE-INSTANCE: ACCESS-PERMISSION-REF, then SERVICE-CLASS-REF
(the atpDerived serviceClass association is XSD-skipped but covered per the
table-row family precedent).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _ConcreteServiceInstance(DiagnosticServiceInstance):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_instance():
    instance = _ConcreteServiceInstance(AUTOSAR.getInstance(), "Dsi")
    instance.setAccessPermissionRef(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/Diag/AccessPerms/Ap1"))
    instance.setServiceClassRef(_ref("DIAGNOSTIC-SERVICE-CLASS", "/Diag/ServiceClasses/Sc1"))
    return instance


class TestWriteDiagnosticServiceInstance:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("DIAGNOSTIC-ECU-RESET")
        ARXMLWriter().writeDiagnosticServiceInstance(parent, _new_instance())
        children = [child.tag for child in parent]
        assert children == ["ACCESS-PERMISSION-REF", "SERVICE-CLASS-REF"]
        access_ref = parent.find("ACCESS-PERMISSION-REF")
        assert access_ref.text == "/Diag/AccessPerms/Ap1"
        assert access_ref.attrib["DEST"] == "DIAGNOSTIC-ACCESS-PERMISSION"
        class_ref = parent.find("SERVICE-CLASS-REF")
        assert class_ref.text == "/Diag/ServiceClasses/Sc1"
        assert class_ref.attrib["DEST"] == "DIAGNOSTIC-SERVICE-CLASS"

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("DIAGNOSTIC-ECU-RESET")
        empty = _ConcreteServiceInstance(AUTOSAR.getInstance(), "Dsi")
        ARXMLWriter().writeDiagnosticServiceInstance(parent, empty)
        assert len(list(parent)) == 0

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("DIAGNOSTIC-ECU-RESET")
        ARXMLWriter().writeDiagnosticServiceInstance(parent, _new_instance())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<DIAGNOSTIC-ECU-RESET>", "<DIAGNOSTIC-ECU-RESET xmlns='%s'>" % NS, 1))
        parsed = _ConcreteServiceInstance(AUTOSAR.getInstance(), "Dsi2")
        ARXMLParser().readDiagnosticServiceInstance(root, parsed)
        assert parsed.getAccessPermissionRef().getValue() == "/Diag/AccessPerms/Ap1"
        assert parsed.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert parsed.getServiceClassRef().getValue() == "/Diag/ServiceClasses/Sc1"
        assert parsed.getServiceClassRef().getDest() == "DIAGNOSTIC-SERVICE-CLASS"
