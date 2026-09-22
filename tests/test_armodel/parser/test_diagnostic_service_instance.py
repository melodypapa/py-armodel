"""Parser tests for DiagnosticServiceInstance (Table 4.26, p.70).

Fragment+helper pattern: DiagnosticServiceInstance is abstract and has no
ARPackage-level dispatch (concrete subclasses own their XML tags); its group
DIAGNOSTIC-SERVICE-INSTANCE carries ACCESS-PERMISSION-REF (the atpDerived
serviceClass association is XSD-skipped but covered per the table-row family
precedent).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticServiceInstance

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _ConcreteServiceInstance(DiagnosticServiceInstance):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-ECU-RESET") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticServiceInstance:
    def test_read_sets_refs(self, parser):
        instance = _ConcreteServiceInstance(AUTOSAR.getInstance(), "Dsi")
        element = _snip(
            '<ACCESS-PERMISSION-REF DEST="DIAGNOSTIC-ACCESS-PERMISSION">/Diag/AccessPerms/Ap1</ACCESS-PERMISSION-REF>'
            '<SERVICE-CLASS-REF DEST="DIAGNOSTIC-SERVICE-CLASS">/Diag/ServiceClasses/Sc1</SERVICE-CLASS-REF>'
        )
        parser.readDiagnosticServiceInstance(element, instance)
        assert instance.getAccessPermissionRef() is not None
        assert instance.getAccessPermissionRef().getValue() == "/Diag/AccessPerms/Ap1"
        assert instance.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert instance.getServiceClassRef() is not None
        assert instance.getServiceClassRef().getValue() == "/Diag/ServiceClasses/Sc1"
        assert instance.getServiceClassRef().getDest() == "DIAGNOSTIC-SERVICE-CLASS"

    def test_read_empty(self, parser):
        instance = _ConcreteServiceInstance(AUTOSAR.getInstance(), "Dsi")
        element = _snip("")
        parser.readDiagnosticServiceInstance(element, instance)
        assert instance.getAccessPermissionRef() is None
        assert instance.getServiceClassRef() is None
