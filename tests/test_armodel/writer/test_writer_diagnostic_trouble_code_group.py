"""
Tests for writing DIAGNOSTIC-TROUBLE-CODE-GROUP elements —
DiagnosticTroubleCodeGroup, Table 4.162 (p.177, R23-11).

DiagnosticTroubleCodeGroup (Base most-derived ARElement) carries two Attribute rows:
dtc (DiagnosticTroubleCode, *, ref) and groupNumber (PositiveInteger, 0..1, attr).
The XSD serializes dtc as the DTCS wrapper (AUTOSAR_00052.xsd l.46211) holding
unbounded DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL items, each with a
DIAGNOSTIC-TROUBLE-CODE-REF — the RefConditional wrapper class is not modeled, so
the writer flattens dtcRefs through the wrapper path (twin precedent
writeDiagnosticStorageConditionGroup). groupNumber is XSD-typed
POSITIVE-INTEGER-VALUE-VARIATION-POINT (l.46230) and is written through the nested
POSITIVE-INTEGER-VALUE-VARIATION-POINT child (precedent
DiagnosticEvent.confirmationThreshold). The writer is writeDiagnosticTroubleCodeGroup =
DIAGNOSTIC-TROUBLE-CODE-GROUP subelement + writeIdentifiable + the dtcRefs flatten +
the groupNumber nested value, in XSD element order (DTCS before GROUP-NUMBER). The
dispatch entry is writeARPackageElement → writeDiagnosticTroubleCodeGroup.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_trouble_code_group.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCodeGroup
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticTroubleCodeGroup:
    """Tests for writeDiagnosticTroubleCodeGroup — own element field values (Table 4.162)."""

    def _dtc_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-TROUBLE-CODE")
        ref.setValue(value)
        return ref

    def _group_number(self, value: int) -> PositiveInteger:
        group_number = PositiveInteger()
        group_number.setValue(value)
        return group_number

    def test_write_dtc_refs_and_group_number(self):
        """Test that set dtcRefs/groupNumber are emitted in XSD order (DTCS before GROUP-NUMBER) with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        group = package.createDiagnosticTroubleCodeGroup("TroubleCodeGroup1")
        group.addDtcRef(self._dtc_ref("/DiagnosticTroubleCodes/TroubleCode1"))
        group.addDtcRef(self._dtc_ref("/DiagnosticTroubleCodes/TroubleCode2"))
        group.setGroupNumber(self._group_number(3))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCodeGroup(parent, group)

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "TroubleCodeGroup1"
        assert [c.tag for c in child if c.tag not in ("SHORT-NAME", "CATEGORY")] == ["DTCS", "GROUP-NUMBER"]
        wrapper = child.find("DTCS")
        assert wrapper is not None
        conditionals = wrapper.findall("DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL")
        assert len(conditionals) == 2
        ref1 = conditionals[0].find("DIAGNOSTIC-TROUBLE-CODE-REF")
        assert ref1 is not None
        assert ref1.text == "/DiagnosticTroubleCodes/TroubleCode1"
        assert ref1.get("DEST") == "DIAGNOSTIC-TROUBLE-CODE"
        ref2 = conditionals[1].find("DIAGNOSTIC-TROUBLE-CODE-REF")
        assert ref2 is not None
        assert ref2.text == "/DiagnosticTroubleCodes/TroubleCode2"
        group_number_element = child.find("GROUP-NUMBER/POSITIVE-INTEGER-VALUE-VARIATION-POINT")
        assert group_number_element is not None
        assert group_number_element.text == "3"

    def test_write_unset_fields_emit_no_children(self):
        """Test that unset dtcRefs/groupNumber emit no DTCS/GROUP-NUMBER children (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        package.createDiagnosticTroubleCodeGroup("TroubleCodeGroup1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCodeGroup(parent, package.getReferrableElement("TroubleCodeGroup1", DiagnosticTroubleCodeGroup))

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-GROUP")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("DTCS") is None
        assert child.find("GROUP-NUMBER") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticTroubleCodeGroup to a DIAGNOSTIC-TROUBLE-CODE-GROUP element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        group = package.createDiagnosticTroubleCodeGroup("TroubleCodeGroup1")
        group.addDtcRef(self._dtc_ref("/DiagnosticTroubleCodes/TroubleCode1"))
        group.setGroupNumber(self._group_number(3))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, group)

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "TroubleCodeGroup1"
        assert child.find("DTCS") is not None
        assert child.find("GROUP-NUMBER") is not None

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticTroubleCodes")
        group = package.createDiagnosticTroubleCodeGroup("TroubleCodeGroup1")
        group.addDtcRef(self._dtc_ref("/DiagnosticTroubleCodes/TroubleCode1"))
        group.addDtcRef(self._dtc_ref("/DiagnosticTroubleCodes/TroubleCode2"))
        group.setGroupNumber(self._group_number(3))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("TroubleCodeGroup1", DiagnosticTroubleCodeGroup)
            assert group_2 is not None
            assert group_2.getShortName() == "TroubleCodeGroup1"
            refs = group_2.getDtcRefs()
            assert len(refs) == 2
            assert refs[0].getValue() == "/DiagnosticTroubleCodes/TroubleCode1"
            assert refs[0].getDest() == "DIAGNOSTIC-TROUBLE-CODE"
            assert refs[1].getValue() == "/DiagnosticTroubleCodes/TroubleCode2"
            group_number = group_2.getGroupNumber()
            assert group_number is not None
            assert group_number.value == 3
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticTroubleCodeGroup without dtcRefs/groupNumber round-trips with defaults."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticTroubleCodes")
        package.createDiagnosticTroubleCodeGroup("TroubleCodeGroup1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("TroubleCodeGroup1", DiagnosticTroubleCodeGroup)
            assert group_2 is not None
            assert group_2.getDtcRefs() == []
            assert group_2.getGroupNumber() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
