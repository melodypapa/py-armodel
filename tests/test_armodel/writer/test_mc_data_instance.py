"""
Tests for writing MC-DATA-INSTANCE elements (McDataInstance, Table 9.30).

The consumer of interest here is ``displayIdentifier`` (spec Type ``McdIdentifier``,
Table 9.30), which rides the ``DISPLAY-IDENTIFIER`` element. McdIdentifier itself has
no XML element of its own (Rule 0001.7), so this is where its value is proven to
survive a full save -> load round-trip with the spec type preserved (Rule 0013.2).

Leaf-helper coverage for McdIdentifier lives in
tests/test_armodel/parser/test_primitive_leaf_helpers.py and
tests/test_armodel/writer/test_primitive_leaf_helpers.py (``TestMcdIdentifierLeaf``).
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import (
    McSupportData,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    DateTime,
    McdIdentifier,
    String,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_document(display_identifier):
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()

    ar_root = document.createARPackage("AUTOSAR")
    impl = ar_root.createBswImplementation("Impl")
    support = McSupportData()
    instance = support.createMcVariableInstance("MeasVar1")
    if display_identifier is not None:
        instance.setDisplayIdentifier(display_identifier)
    impl.setMcSupport(support)

    return document


def _first_instance(document):
    return document.getARPackages()[0].getBswImplementations()[0].getMcSupport().getMcVariableInstances()[0]


def _save_and_reload(document):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)
        written = open(file_path, encoding="utf-8").read()

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)
        return written, document_2
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


class TestMcDataInstanceDisplayIdentifierRoundTrip:
    """
    Round-trip coverage for the McdIdentifier value carried by DISPLAY-IDENTIFIER.
    """

    def test_round_trip_preserves_value_and_type(self):
        """Write then re-read DISPLAY-IDENTIFIER; assert the value and the spec type survive."""
        document = _build_document(McdIdentifier().setValue("meas_1"))

        written, document_2 = _save_and_reload(document)

        assert "<DISPLAY-IDENTIFIER>meas_1</DISPLAY-IDENTIFIER>" in written
        reparsed = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport().getMcVariableInstances()[0].getDisplayIdentifier()
        assert isinstance(reparsed, McdIdentifier)
        assert reparsed.getValue() == "meas_1"

    def test_round_trip_preserves_value_with_bracket_and_dot_syntax(self):
        """A value using the Note's bracket/dot forms also survives unchanged."""
        document = _build_document(McdIdentifier().setValue("obj.field.sub[3]"))

        written, document_2 = _save_and_reload(document)

        assert "<DISPLAY-IDENTIFIER>obj.field.sub[3]</DISPLAY-IDENTIFIER>" in written
        reparsed = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport().getMcVariableInstances()[0].getDisplayIdentifier()
        assert isinstance(reparsed, McdIdentifier)
        assert reparsed.getValue() == "obj.field.sub[3]"

    def test_unset_display_identifier_emits_nothing_and_reparses_as_none(self):
        """The empty case: no element is written and the attribute re-parses as None."""
        document = _build_document(None)

        written, document_2 = _save_and_reload(document)

        assert "DISPLAY-IDENTIFIER" not in written
        assert _first_instance(document_2).getDisplayIdentifier() is None


class TestMcDataInstanceIdentifiableLevelRoundTrip:
    """
    Rule 0025 coverage: readMcDataInstance must read the Identifiable level itself.

    The writer has always emitted ``T``/``UUID`` on ``<MC-DATA-INSTANCE>`` via
    ``writeIdentifiable``, but the reader did not call any base helper, so the whole
    Identifiable level was dropped on parse. These tests pin the attributes that level
    owns so the reader side cannot regress silently again.
    """

    def test_round_trip_preserves_identifiable_level_attributes(self):
        """Uuid, timestamp, category and shortName survive the round-trip."""
        document = _build_document(None)
        instance = _first_instance(document)
        instance.setUuid(String().setValue("11111111-1111-1111-1111-111111111111"))
        instance.setTimestamp(DateTime().setValue("2026-10-13T00:00:00Z"))
        instance.setCategory(CategoryString().setValue("DATA_SET"))

        written, document_2 = _save_and_reload(document)

        assert 'UUID="11111111-1111-1111-1111-111111111111"' in written
        assert 'T="2026-10-13T00:00:00Z"' in written
        reparsed = _first_instance(document_2)
        assert reparsed.getUuid().getValue() == "11111111-1111-1111-1111-111111111111"
        assert reparsed.getTimestamp().getValue() == "2026-10-13T00:00:00Z"
        assert reparsed.getCategory().getValue() == "DATA_SET"
        assert reparsed.getShortName() == "MeasVar1"

    def test_identifiable_level_survives_on_nested_sub_elements(self):
        """The base helper also applies to each SUB-ELEMENTS/MC-DATA-INSTANCE."""
        document = _build_document(None)
        support = document.getARPackages()[0].getBswImplementations()[0].getMcSupport()
        support.createMcVariableInstance("MeasVar2").createSubElement("Inner").setUuid(String().setValue("22222222-2222-2222-2222-222222222222"))

        _, document_2 = _save_and_reload(document)

        inner = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport().getMcVariableInstances()[1].getSubElements()[0]
        assert inner.getShortName() == "Inner"
        assert inner.getUuid().getValue() == "22222222-2222-2222-2222-222222222222"
