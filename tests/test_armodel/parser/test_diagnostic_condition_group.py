"""
Tests for reading the (empty) DIAGNOSTIC-CONDITION-GROUP group —
DiagnosticConditionGroup, Table 4.193 (p.200, R23-11).

DiagnosticConditionGroup (spec marks it abstract) is the base of
DiagnosticEnableConditionGroup and DiagnosticStorageConditionGroup; its own XSD
group DIAGNOSTIC-CONDITION-GROUP (AUTOSAR_00052.xsd l.33439) is an empty
<xsd:sequence/> — the spec table carries no Attribute rows — embedded in each
concrete subclass element. There is no standalone DIAGNOSTIC-CONDITION-GROUP
element, so the reader is the named reusable helper readDiagnosticConditionGroup
that the concrete subclass readers call (Rule 0001.7 abstract-XML-bearing-base
clause). The concrete subclasses are still unsynced stubs, so the tests drive
the helper directly through the stub subclass instances and assert the helper
is a lossless no-op (it must consume nothing, not even SHORT-NAME).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_condition_group.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableConditionGroup, DiagnosticStorageConditionGroup

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str = "", root_tag: str = "DIAGNOSTIC-ENABLE-CONDITION-GROUP") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticConditionGroup:
    """Tests for readDiagnosticConditionGroup — own (empty) group is a lossless no-op (Table 4.193)."""

    def _read(self, parser, inner="", cls=DiagnosticEnableConditionGroup, short_name="Grp1"):
        group = cls(AUTOSAR.getInstance(), short_name)
        parser.readDiagnosticConditionGroup(_snip(inner), group)
        return group

    def test_read_empty_group_leaves_object_intact(self, parser):
        """Test that reading an empty group element changes nothing on the group object."""
        group = self._read(parser)
        assert group.getShortName() == "Grp1"

    def test_read_group_does_not_consume_sibling_content(self, parser):
        """Test that the helper consumes nothing — SHORT-NAME stays for the subclass reader."""
        group = self._read(parser, "<SHORT-NAME>OtherName</SHORT-NAME>", short_name="Grp1")
        assert group.getShortName() == "Grp1"

    def test_read_storage_condition_group_subclass(self, parser):
        """Test that the helper populates a DiagnosticStorageConditionGroup stub the same way."""
        group = self._read(parser, "", cls=DiagnosticStorageConditionGroup, short_name="Grp2")
        assert group.getShortName() == "Grp2"
