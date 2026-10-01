"""
Tests for writing DIAGNOSTIC-SECURITY-ACCESS elements —
DiagnosticSecurityAccess, Table 4.49 (p.96, R23-11).

DiagnosticSecurityAccess (Base most-derived ARElement, DiagnosticServiceInstance
in the chain) carries two 0..1 attr attributes — REQUEST-SEED-ID
(POSITIVE-INTEGER) and SECURITY-DELAY-TIME-ON-BOOT (TIME-VALUE) — and two 0..1
refs — SECURITY-ACCESS-CLASS-REF
(DIAGNOSTIC-SECURITY-ACCESS-CLASS--SUBTYPES-ENUM) and SECURITY-LEVEL-REF
(DIAGNOSTIC-SECURITY-LEVEL--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-SECURITY-ACCESS, AUTOSAR_00052.xsd l.43248. The writer reads the
model via the get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticSecurityAccess.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_security_access.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticSecurityAccess
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticSecurityAccess:
    """Tests for writeDiagnosticSecurityAccess — own element field values (Table 4.49)."""

    def test_write_all_fields(self):
        """Test that the two attributes and two refs are emitted with the spec values in XSD order."""
        package = AUTOSAR.getInstance().createARPackage("SecAccesses")
        security_access = package.createDiagnosticSecurityAccess("SecAccess1")
        request_seed_id = PositiveInteger()
        request_seed_id.setValue("259")
        security_access.setRequestSeedId(request_seed_id)
        security_access.setSecurityAccessClass(_ref("DIAGNOSTIC-SECURITY-ACCESS-CLASS", "/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass"))
        delay = TimeValue()
        delay.setValue("3.0")
        security_access.setSecurityDelayTimeOnBoot(delay)
        security_access.setSecurityLevel(_ref("DIAGNOSTIC-SECURITY-LEVEL", "/AUTOSAR/DiagnosticSecurityLevels/Level1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityAccess(parent, security_access)

        child = parent.find("DIAGNOSTIC-SECURITY-ACCESS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SecAccess1"
        assert child.find("REQUEST-SEED-ID").text == "259"
        security_access_class_ref = child.find("SECURITY-ACCESS-CLASS-REF")
        assert security_access_class_ref is not None
        assert security_access_class_ref.text == "/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass"
        assert security_access_class_ref.get("DEST") == "DIAGNOSTIC-SECURITY-ACCESS-CLASS"
        assert child.find("SECURITY-DELAY-TIME-ON-BOOT").text == "3.0"
        security_level_ref = child.find("SECURITY-LEVEL-REF")
        assert security_level_ref is not None
        assert security_level_ref.text == "/AUTOSAR/DiagnosticSecurityLevels/Level1"
        assert security_level_ref.get("DEST") == "DIAGNOSTIC-SECURITY-LEVEL"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["REQUEST-SEED-ID", "SECURITY-ACCESS-CLASS-REF", "SECURITY-DELAY-TIME-ON-BOOT", "SECURITY-LEVEL-REF"]

    def test_write_unset_fields_omit_tags(self):
        """Test that unset fields emit no elements beyond SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("SecAccesses")
        package.createDiagnosticSecurityAccess("SecAccess1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityAccess(parent, package.getElement("SecAccess1", DiagnosticSecurityAccess))

        child = parent.find("DIAGNOSTIC-SECURITY-ACCESS")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("REQUEST-SEED-ID") is None
        assert child.find("SECURITY-ACCESS-CLASS-REF") is None
        assert child.find("SECURITY-DELAY-TIME-ON-BOOT") is None
        assert child.find("SECURITY-LEVEL-REF") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticSecurityAccess to a DIAGNOSTIC-SECURITY-ACCESS element."""
        package = AUTOSAR.getInstance().createARPackage("SecAccesses")
        security_access = package.createDiagnosticSecurityAccess("SecAccess1")
        security_access.setSecurityLevel(_ref("DIAGNOSTIC-SECURITY-LEVEL", "/AUTOSAR/DiagnosticSecurityLevels/Level1"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, security_access)

        child = parent.find("DIAGNOSTIC-SECURITY-ACCESS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SecAccess1"
        assert child.find("SECURITY-LEVEL-REF").text == "/AUTOSAR/DiagnosticSecurityLevels/Level1"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("SecAccesses")
        security_access = package.createDiagnosticSecurityAccess("SecAccess1")
        request_seed_id = PositiveInteger()
        request_seed_id.setValue("259")
        security_access.setRequestSeedId(request_seed_id)
        security_access.setSecurityAccessClass(_ref("DIAGNOSTIC-SECURITY-ACCESS-CLASS", "/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass"))
        delay = TimeValue()
        delay.setValue("3.0")
        security_access.setSecurityDelayTimeOnBoot(delay)
        security_access.setSecurityLevel(_ref("DIAGNOSTIC-SECURITY-LEVEL", "/AUTOSAR/DiagnosticSecurityLevels/Level1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            security_access_2 = package_2.getElement("SecAccess1", DiagnosticSecurityAccess)
            assert security_access_2 is not None
            assert security_access_2.getRequestSeedId() is not None
            assert security_access_2.getRequestSeedId().getValue() == 259
            assert security_access_2.getSecurityAccessClass() is not None
            assert security_access_2.getSecurityAccessClass().getValue() == "/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass"
            assert security_access_2.getSecurityAccessClass().getDest() == "DIAGNOSTIC-SECURITY-ACCESS-CLASS"
            assert security_access_2.getSecurityDelayTimeOnBoot() is not None
            assert security_access_2.getSecurityDelayTimeOnBoot().getValue() == 3.0
            assert security_access_2.getSecurityLevel() is not None
            assert security_access_2.getSecurityLevel().getValue() == "/AUTOSAR/DiagnosticSecurityLevels/Level1"
            assert security_access_2.getSecurityLevel().getDest() == "DIAGNOSTIC-SECURITY-LEVEL"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticSecurityAccess without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("SecAccesses")
        package.createDiagnosticSecurityAccess("SecAccess1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            security_access_2 = package_2.getElement("SecAccess1", DiagnosticSecurityAccess)
            assert security_access_2 is not None
            assert security_access_2.getRequestSeedId() is None
            assert security_access_2.getSecurityAccessClass() is None
            assert security_access_2.getSecurityDelayTimeOnBoot() is None
            assert security_access_2.getSecurityLevel() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
