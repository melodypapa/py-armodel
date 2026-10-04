"""
Tests for writing DIAGNOSTIC-IUMPR-GROUP elements —
DiagnosticIumprGroup, Table 4.209 (p.210, R23-11).

The XSD group DIAGNOSTIC-IUMPR-GROUP (AUTOSAR_00052.xsd l.38728) fixes the
wrapper structure and XML element order: the optional IUMPR-GROUP-IDENTIFIERS
wrapper (holding the DIAGNOSTIC-IUMPR-GROUP-IDENTIFIER choice element) comes
before the optional IUMPR-REFS wrapper (holding an unbounded choice of
IUMPR-REF elements, DEST DIAGNOSTIC-IUMPR, atpSplitable); a wrapper is
emitted only when its content is present (IUMPR-REFS precedent:
DiagnosticDataIdentifierSet DATA-IDENTIFIER-REFS). The XSD-only
GROUP-IDENTIFIER element carries atp.Status="removed" and is not written
(Rule 0015).
The dispatch entry is writeARPackageElement → writeDiagnosticIumprGroup.

DiagnosticIumprGroupIdentifier (Table 4.210) is still an empty stub queued
later in Group25 — the writer emits the wrapper presence until that row
syncs.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_iumpr_group.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumprGroup
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticIumprGroup:
    """Tests for writeDiagnosticIumprGroup — own element field values (Table 4.209)."""

    def _make_group(self, short_name: str = "IumprGroup1") -> DiagnosticIumprGroup:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIumprGroups")
        return package.createDiagnosticIumprGroup(short_name)

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-IUMPR")
        ref.setValue(value)
        return ref

    def _populate(self, group: DiagnosticIumprGroup) -> DiagnosticIumprGroup:
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticIumprGroupIdentifier

        group.setIumprGroupIdentifier(DiagnosticIumprGroupIdentifier())
        group.addIumprRef(self._make_ref("/AUTOSAR/DiagnosticIumprs/Iumpr1"))
        group.addIumprRef(self._make_ref("/AUTOSAR/DiagnosticIumprs/Iumpr2"))
        return group

    def test_write_wrappers_in_xsd_order(self):
        """Test that the wrappers are emitted inside one element after SHORT-NAME in XSD order (IUMPR-GROUP-IDENTIFIERS before IUMPR-REFS) with the spec values."""
        group = self._populate(self._make_group())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIumprGroup(parent, group)

        child = parent.find("DIAGNOSTIC-IUMPR-GROUP")
        assert child is not None
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "IUMPR-GROUP-IDENTIFIERS",
            "IUMPR-REFS",
        ]
        identifiers_tag = child.find("IUMPR-GROUP-IDENTIFIERS")
        assert identifiers_tag is not None
        assert identifiers_tag.find("DIAGNOSTIC-IUMPR-GROUP-IDENTIFIER") is not None
        refs_tag = child.find("IUMPR-REFS")
        assert refs_tag is not None
        ref_elements = refs_tag.findall("IUMPR-REF")
        assert len(ref_elements) == 2
        assert ref_elements[0].text == "/AUTOSAR/DiagnosticIumprs/Iumpr1"
        assert ref_elements[0].attrib["DEST"] == "DIAGNOSTIC-IUMPR"
        assert ref_elements[1].text == "/AUTOSAR/DiagnosticIumprs/Iumpr2"
        assert ref_elements[1].attrib["DEST"] == "DIAGNOSTIC-IUMPR"

    def test_write_unset_own_fields_emit_no_wrappers(self):
        """Test that an unpopulated group emits no IUMPR-GROUP-IDENTIFIERS and no IUMPR-REFS wrapper (empty wrapper case)."""
        self._make_group()

        parent = ET.Element("PARENT")
        group = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("IumprGroup1", DiagnosticIumprGroup)
        ARXMLWriter().writeDiagnosticIumprGroup(parent, group)

        child = parent.find("DIAGNOSTIC-IUMPR-GROUP")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("IUMPR-GROUP-IDENTIFIERS") is None
        assert child.find("IUMPR-REFS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticIumprGroup to a DIAGNOSTIC-IUMPR-GROUP element."""
        group = self._populate(self._make_group())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, group)

        child = parent.find("DIAGNOSTIC-IUMPR-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "IumprGroup1"
        assert child.find("IUMPR-REFS").find("IUMPR-REF").text == "/AUTOSAR/DiagnosticIumprs/Iumpr1"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIumprGroups")
        self._populate(package.createDiagnosticIumprGroup("IumprGroup1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("IumprGroup1", DiagnosticIumprGroup)
            assert group_2 is not None
            assert group_2.getShortName() == "IumprGroup1"
            identifier = group_2.getIumprGroupIdentifier()
            assert identifier is not None
            refs = group_2.getIumprRefs()
            assert len(refs) == 2
            assert refs[0].getValue() == "/AUTOSAR/DiagnosticIumprs/Iumpr1"
            assert refs[0].getDest() == "DIAGNOSTIC-IUMPR"
            assert refs[1].getValue() == "/AUTOSAR/DiagnosticIumprs/Iumpr2"
            assert refs[1].getDest() == "DIAGNOSTIC-IUMPR"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticIumprGroup without own fields round-trips with an empty refs list and no identifier."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIumprGroups")
        package.createDiagnosticIumprGroup("IumprGroup1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("IumprGroup1", DiagnosticIumprGroup)
            assert group_2 is not None
            assert group_2.getIumprRefs() == []
            assert group_2.getIumprGroupIdentifier() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
