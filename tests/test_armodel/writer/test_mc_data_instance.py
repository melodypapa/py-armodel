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
    McdIdentifier,
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
        assert document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport().getMcVariableInstances()[0].getDisplayIdentifier() is None
