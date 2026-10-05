"""
Tests for writing DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP elements —
DiagnosticIumprDenominatorGroup, Table 4.211 (p.211, R23-11).

The XSD group DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP (AUTOSAR_00052.xsd
l.38677) fixes the wrapper structure: the optional IUMPR-REFS wrapper
holds an unbounded choice of IUMPR-REF elements (DEST
DIAGNOSTIC-IUMPR, atpSplitable); the wrapper is emitted only when the
iumprRefs list is non-empty (DiagnosticDataIdentifierSet
DATA-IDENTIFIER-REFS precedent).
The dispatch entry is writeARPackageElement →
writeDiagnosticIumprDenominatorGroup.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_iumpr_denominator_group.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumprDenominatorGroup
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


class TestWriteDiagnosticIumprDenominatorGroup:
    """Tests for writeDiagnosticIumprDenominatorGroup — own element field values (Table 4.211)."""

    def _make_group(self, short_name: str = "DenominatorGroup1") -> DiagnosticIumprDenominatorGroup:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIumprDenominatorGroups")
        return package.createDiagnosticIumprDenominatorGroup(short_name)

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-IUMPR")
        ref.setValue(value)
        return ref

    def _populate(self, group: DiagnosticIumprDenominatorGroup) -> DiagnosticIumprDenominatorGroup:
        group.addIumprRef(self._make_ref("/AUTOSAR/DiagnosticIumprs/Iumpr1"))
        group.addIumprRef(self._make_ref("/AUTOSAR/DiagnosticIumprs/Iumpr2"))
        return group

    def test_write_refs_in_wrapper_in_xsd_order(self):
        """Test that the refs are emitted inside one IUMPR-REFS wrapper after SHORT-NAME with the spec values."""
        group = self._populate(self._make_group())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIumprDenominatorGroup(parent, group)

        child = parent.find("DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP")
        assert child is not None
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "IUMPR-REFS",
        ]
        refs_tag = child.find("IUMPR-REFS")
        assert refs_tag is not None
        ref_elements = refs_tag.findall("IUMPR-REF")
        assert len(ref_elements) == 2
        assert ref_elements[0].text == "/AUTOSAR/DiagnosticIumprs/Iumpr1"
        assert ref_elements[0].attrib["DEST"] == "DIAGNOSTIC-IUMPR"
        assert ref_elements[1].text == "/AUTOSAR/DiagnosticIumprs/Iumpr2"
        assert ref_elements[1].attrib["DEST"] == "DIAGNOSTIC-IUMPR"

    def test_write_unset_refs_emit_no_wrapper(self):
        """Test that an unpopulated group emits no IUMPR-REFS wrapper (empty wrapper case)."""
        self._make_group()

        parent = ET.Element("PARENT")
        group = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("DenominatorGroup1", DiagnosticIumprDenominatorGroup)
        ARXMLWriter().writeDiagnosticIumprDenominatorGroup(parent, group)

        child = parent.find("DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("IUMPR-REFS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticIumprDenominatorGroup to a DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP element."""
        group = self._populate(self._make_group())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, group)

        child = parent.find("DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "DenominatorGroup1"
        assert child.find("IUMPR-REFS").find("IUMPR-REF").text == "/AUTOSAR/DiagnosticIumprs/Iumpr1"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIumprDenominatorGroups")
        self._populate(package.createDiagnosticIumprDenominatorGroup("DenominatorGroup1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("DenominatorGroup1", DiagnosticIumprDenominatorGroup)
            assert group_2 is not None
            assert group_2.getShortName() == "DenominatorGroup1"
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
        """Test that a DiagnosticIumprDenominatorGroup without own fields round-trips with an empty refs list."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIumprDenominatorGroups")
        package.createDiagnosticIumprDenominatorGroup("DenominatorGroup1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("DenominatorGroup1", DiagnosticIumprDenominatorGroup)
            assert group_2 is not None
            assert group_2.getIumprRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
