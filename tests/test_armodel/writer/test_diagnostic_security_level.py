"""Writer round-trip tests for DiagnosticSecurityLevel (Table 4.32, p.75).

Child order per XSD complexType DIAGNOSTIC-SECURITY-LEVEL
(AUTOSAR_00052.xsd l.43467): SHORT-NAME (inherited),
ACCESS-DATA-RECORD-SIZE, KEY-SIZE, NUM-FAILED-SECURITY-ACCESS,
SECURITY-DELAY-TIME, SEED-SIZE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticSecurityLevel
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_level():
    pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
    level = pkg.createDiagnosticSecurityLevel("Sec1")
    level.setAccessDataRecordSize(PositiveInteger().setValue(32))
    level.setKeySize(PositiveInteger().setValue(4))
    level.setNumFailedSecurityAccess(PositiveInteger().setValue(3))
    level.setSecurityDelayTime(TimeValue().setValue(1.0))
    level.setSeedSize(PositiveInteger().setValue(8))
    return level


class TestWriteDiagnosticSecurityLevel:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityLevel(parent, _new_level())
        node = parent.find("DIAGNOSTIC-SECURITY-LEVEL")
        assert node is not None
        assert [child.tag for child in node] == [
            "SHORT-NAME",
            "ACCESS-DATA-RECORD-SIZE",
            "KEY-SIZE",
            "NUM-FAILED-SECURITY-ACCESS",
            "SECURITY-DELAY-TIME",
            "SEED-SIZE",
        ]
        assert node.find("ACCESS-DATA-RECORD-SIZE").text == "32"
        assert node.find("KEY-SIZE").text == "4"
        assert node.find("NUM-FAILED-SECURITY-ACCESS").text == "3"
        assert node.find("SECURITY-DELAY-TIME").text == "1.0"
        assert node.find("SEED-SIZE").text == "8"

    def test_write_empty_fields_omits_optional_tags(self):
        pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
        level = pkg.createDiagnosticSecurityLevel("Sec2")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityLevel(parent, level)
        node = parent.find("DIAGNOSTIC-SECURITY-LEVEL")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityLevel(parent, _new_level())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = DiagnosticSecurityLevel(AUTOSAR.getInstance(), "Sec3")
        ARXMLParser().readDiagnosticSecurityLevel(root[0], parsed)
        assert parsed.getAccessDataRecordSize().getValue() == 32
        assert parsed.getKeySize().getValue() == 4
        assert parsed.getNumFailedSecurityAccess().getValue() == 3
        assert parsed.getSecurityDelayTime().getValue() == 1.0
        assert parsed.getSeedSize().getValue() == 8
