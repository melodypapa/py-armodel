"""Parser tests for DiagnosticSecurityLevel (Table 4.32, p.75).

XSD group DIAGNOSTIC-SECURITY-LEVEL (AUTOSAR_00052.xsd l.43427) element order:
ACCESS-DATA-RECORD-SIZE, KEY-SIZE, NUM-FAILED-SECURITY-ACCESS,
SECURITY-DELAY-TIME, SEED-SIZE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticSecurityLevel

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-SECURITY-LEVEL") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticSecurityLevel:
    def test_read_sets_all_fields(self, parser):
        level = DiagnosticSecurityLevel(AUTOSAR.getInstance(), "Sec1")
        element = _snip(
            "<SHORT-NAME>Sec1</SHORT-NAME>"
            "<ACCESS-DATA-RECORD-SIZE>32</ACCESS-DATA-RECORD-SIZE>"
            "<KEY-SIZE>4</KEY-SIZE>"
            "<NUM-FAILED-SECURITY-ACCESS>3</NUM-FAILED-SECURITY-ACCESS>"
            "<SECURITY-DELAY-TIME>1.0</SECURITY-DELAY-TIME>"
            "<SEED-SIZE>8</SEED-SIZE>"
        )
        parser.readDiagnosticSecurityLevel(element, level)
        assert level.getAccessDataRecordSize().getValue() == 32
        assert level.getKeySize().getValue() == 4
        assert level.getNumFailedSecurityAccess().getValue() == 3
        assert level.getSecurityDelayTime().getValue() == 1.0
        assert level.getSeedSize().getValue() == 8

    def test_read_empty(self, parser):
        level = DiagnosticSecurityLevel(AUTOSAR.getInstance(), "Sec1")
        parser.readDiagnosticSecurityLevel(_snip("<SHORT-NAME>Sec1</SHORT-NAME>"), level)
        assert level.getAccessDataRecordSize() is None
        assert level.getKeySize() is None
        assert level.getNumFailedSecurityAccess() is None
        assert level.getSecurityDelayTime() is None
        assert level.getSeedSize() is None


def test_arpackage_dispatch_reads_element(parser):
    package = AUTOSAR.getInstance().createARPackage("SecLevels")
    ar_package = ET.fromstring(
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>SecLevels</SHORT-NAME>"
        "<ELEMENTS>"
        "<DIAGNOSTIC-SECURITY-LEVEL>"
        "<SHORT-NAME>Sec1</SHORT-NAME>"
        "<KEY-SIZE>4</KEY-SIZE>"
        "<SEED-SIZE>8</SEED-SIZE>"
        "</DIAGNOSTIC-SECURITY-LEVEL>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )
    parser.readARPackageElements(ar_package, package)

    level = package.getElement("Sec1", DiagnosticSecurityLevel)
    assert level is not None
    assert isinstance(level, DiagnosticSecurityLevel)
    assert level.getKeySize().getValue() == 4
    assert level.getSeedSize().getValue() == 8
