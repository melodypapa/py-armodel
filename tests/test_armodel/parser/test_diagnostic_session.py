"""Parser tests for DiagnosticSession (Table 4.30, p.74).

XSD group DIAGNOSTIC-SESSION (AUTOSAR_00052.xsd l.44315) element order:
ID, JUMP-TO-BOOT-LOADER, P-2-SERVER-MAX, P-2-STAR-SERVER-MAX.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticJumpToBootLoaderEnum, DiagnosticSession

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-SESSION") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticSession:
    def test_read_sets_all_fields(self, parser):
        session = DiagnosticSession(AUTOSAR.getInstance(), "Sess1")
        element = _snip(
            "<SHORT-NAME>Sess1</SHORT-NAME>" "<ID>2</ID>" "<JUMP-TO-BOOT-LOADER>OEM-BOOT</JUMP-TO-BOOT-LOADER>" "<P-2-SERVER-MAX>0.05</P-2-SERVER-MAX>" "<P-2-STAR-SERVER-MAX>0.5</P-2-STAR-SERVER-MAX>"
        )
        parser.readDiagnosticSession(element, session)
        assert session.getId().getValue() == 2
        assert session.getJumpToBootLoader().getValue() == "OEM-BOOT"
        assert isinstance(session.getJumpToBootLoader(), DiagnosticJumpToBootLoaderEnum)
        assert session.getP2ServerMax().getValue() == 0.05
        assert session.getP2StarServerMax().getValue() == 0.5

    def test_read_empty(self, parser):
        session = DiagnosticSession(AUTOSAR.getInstance(), "Sess1")
        parser.readDiagnosticSession(_snip("<SHORT-NAME>Sess1</SHORT-NAME>"), session)
        assert session.getId() is None
        assert session.getJumpToBootLoader() is None
        assert session.getP2ServerMax() is None
        assert session.getP2StarServerMax() is None


def test_arpackage_dispatch_reads_element(parser):
    package = AUTOSAR.getInstance().createARPackage("Sessions")
    ar_package = ET.fromstring(
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>Sessions</SHORT-NAME>"
        "<ELEMENTS>"
        "<DIAGNOSTIC-SESSION>"
        "<SHORT-NAME>Sess1</SHORT-NAME>"
        "<ID>3</ID>"
        "<JUMP-TO-BOOT-LOADER>NO-BOOT</JUMP-TO-BOOT-LOADER>"
        "</DIAGNOSTIC-SESSION>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )
    parser.readARPackageElements(ar_package, package)

    session = package.getElement("Sess1", DiagnosticSession)
    assert session is not None
    assert isinstance(session, DiagnosticSession)
    assert session.getId().getValue() == 3
    assert session.getJumpToBootLoader().getValue() == "NO-BOOT"
