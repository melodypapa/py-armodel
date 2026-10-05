"""
Tests for reading the INIT-VALUE element of the DIAGNOSTIC-CONDITION group —
DiagnosticCondition, Table 4.184 (p.194, R23-11).

DiagnosticCondition (spec marks it abstract) is the base of
DiagnosticEnableCondition and DiagnosticStorageCondition; its own XSD group
DIAGNOSTIC-CONDITION (AUTOSAR_00052.xsd l.33411) carries the single 0..1 element
INIT-VALUE, embedded in each concrete subclass element. There is no standalone
DIAGNOSTIC-CONDITION element, so the reader is the named reusable helper
readDiagnosticCondition that the concrete subclass readers call
(Rule 0001.7 abstract-XML-bearing-base clause). The concrete subclasses are
still unsynced stubs, so the tests drive the helper directly through the stub
subclass instances.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_condition.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableCondition, DiagnosticStorageCondition

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-ENABLE-CONDITION") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticCondition:
    """Tests for readDiagnosticCondition — own group field values (Table 4.184)."""

    def _read(self, parser, inner, cls=DiagnosticEnableCondition, short_name="Cond1"):
        condition = cls(AUTOSAR.getInstance(), short_name)
        parser.readDiagnosticCondition(_snip(inner), condition)
        return condition

    def test_read_sets_init_value_true(self, parser):
        """Test that INIT-VALUE true is read into initValue."""
        condition = self._read(parser, "<INIT-VALUE>true</INIT-VALUE>")
        assert condition.getInitValue() is not None
        assert condition.getInitValue().value is True

    def test_read_sets_init_value_false(self, parser):
        """Test that INIT-VALUE false is read into initValue."""
        condition = self._read(parser, "<INIT-VALUE>false</INIT-VALUE>")
        assert condition.getInitValue() is not None
        assert condition.getInitValue().value is False

    def test_read_empty_leaves_init_value_none(self, parser):
        """Test that an element without INIT-VALUE leaves initValue None."""
        condition = self._read(parser, "")
        assert condition.getInitValue() is None

    def test_read_storage_condition_subclass(self, parser):
        """Test that the helper populates a DiagnosticStorageCondition stub the same way."""
        condition = self._read(parser, "<INIT-VALUE>false</INIT-VALUE>", cls=DiagnosticStorageCondition, short_name="Cond2")
        assert condition.getInitValue() is not None
        assert condition.getInitValue().value is False
