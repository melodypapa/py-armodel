"""Writer round-trip tests for DiagnosticSession (Table 4.30, p.74).

Child order per XSD complexType DIAGNOSTIC-SESSION (AUTOSAR_00052.xsd
l.44355): SHORT-NAME (inherited), ID, JUMP-TO-BOOT-LOADER, P-2-SERVER-MAX,
P-2-STAR-SERVER-MAX.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticJumpToBootLoaderEnum, DiagnosticSession
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_session():
    pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
    session = pkg.createDiagnosticSession("Sess1")
    session.setId(PositiveInteger().setValue(2))
    session.setJumpToBootLoader(DiagnosticJumpToBootLoaderEnum().setValue(DiagnosticJumpToBootLoaderEnum.OEM_BOOT))
    session.setP2ServerMax(TimeValue().setValue(0.05))
    session.setP2StarServerMax(TimeValue().setValue(0.5))
    return session


class TestWriteDiagnosticSession:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSession(parent, _new_session())
        node = parent.find("DIAGNOSTIC-SESSION")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME", "ID", "JUMP-TO-BOOT-LOADER", "P-2-SERVER-MAX", "P-2-STAR-SERVER-MAX"]
        assert node.find("ID").text == "2"
        assert node.find("JUMP-TO-BOOT-LOADER").text == "OEM-BOOT"
        assert node.find("P-2-SERVER-MAX").text == "0.05"
        assert node.find("P-2-STAR-SERVER-MAX").text == "0.5"

    def test_write_empty_fields_omits_optional_tags(self):
        pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
        session = pkg.createDiagnosticSession("Sess2")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSession(parent, session)
        node = parent.find("DIAGNOSTIC-SESSION")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSession(parent, _new_session())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = DiagnosticSession(AUTOSAR.getInstance(), "Sess3")
        ARXMLParser().readDiagnosticSession(root[0], parsed)
        assert parsed.getId().getValue() == 2
        assert parsed.getJumpToBootLoader().getValue() == "OEM-BOOT"
        assert parsed.getP2ServerMax().getValue() == 0.05
        assert parsed.getP2StarServerMax().getValue() == 0.5
