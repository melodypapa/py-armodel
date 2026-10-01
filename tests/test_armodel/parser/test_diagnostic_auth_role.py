"""
Tests for reading the DIAGNOSTIC-AUTH-ROLE element —
DiagnosticAuthRole, Table 4.34 (p.77, R23-11).

DiagnosticAuthRole (Base most-derived ARElement) carries two 0..1 attr
attributes — BIT-POSITION (PositiveInteger) and IS-DEFAULT (Boolean) — XSD group
DIAGNOSTIC-AUTH-ROLE, AUTOSAR_00052.xsd l.31670.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_auth_role.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAuthRole:
    """Tests for readDiagnosticAuthRole — own element field values (Table 4.34)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthRole

        auth_role = DiagnosticAuthRole(parent=MagicMock(), short_name="Role1")
        element = _snip(inner, root_tag="DIAGNOSTIC-AUTH-ROLE")
        parser.readDiagnosticAuthRole(element, auth_role)
        return auth_role

    def test_with_bit_position_and_is_default(self, parser):
        """Test that BIT-POSITION and IS-DEFAULT are read with field values."""
        inner = "<SHORT-NAME>Role1</SHORT-NAME><BIT-POSITION>7</BIT-POSITION><IS-DEFAULT>true</IS-DEFAULT>"
        auth_role = self._read(parser, inner)
        assert auth_role.getShortName() == "Role1"
        assert auth_role.getBitPosition() is not None
        assert auth_role.getBitPosition().getValue() == 7
        assert auth_role.getIsDefault() is not None
        assert auth_role.getIsDefault().getValue() is True

    def test_without_attributes(self, parser):
        """Test that absent BIT-POSITION / IS-DEFAULT leave the fields None."""
        auth_role = self._read(parser, "<SHORT-NAME>Role1</SHORT-NAME>")
        assert auth_role.getBitPosition() is None
        assert auth_role.getIsDefault() is None

    def test_is_default_false(self, parser):
        """Test that IS-DEFAULT false is read as a False Boolean."""
        inner = "<SHORT-NAME>Role1</SHORT-NAME><IS-DEFAULT>false</IS-DEFAULT>"
        auth_role = self._read(parser, inner)
        assert auth_role.getIsDefault() is not None
        assert auth_role.getIsDefault().getValue() is False
