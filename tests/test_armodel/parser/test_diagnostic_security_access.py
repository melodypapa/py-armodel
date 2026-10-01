"""
Tests for reading the DIAGNOSTIC-SECURITY-ACCESS element —
DiagnosticSecurityAccess, Table 4.49 (p.96, R23-11).

DiagnosticSecurityAccess (Base most-derived ARElement, DiagnosticServiceInstance
in the chain) carries two 0..1 attr attributes — REQUEST-SEED-ID
(POSITIVE-INTEGER) and SECURITY-DELAY-TIME-ON-BOOT (TIME-VALUE) — and two 0..1
refs — SECURITY-ACCESS-CLASS-REF
(DIAGNOSTIC-SECURITY-ACCESS-CLASS--SUBTYPES-ENUM) and SECURITY-LEVEL-REF
(DIAGNOSTIC-SECURITY-LEVEL--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-SECURITY-ACCESS, AUTOSAR_00052.xsd l.43248.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_security_access.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticSecurityAccess:
    """Tests for readDiagnosticSecurityAccess — own element field values (Table 4.49)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticSecurityAccess

        security_access = DiagnosticSecurityAccess(parent=MagicMock(), short_name="SecAccess1")
        element = _snip(inner, root_tag="DIAGNOSTIC-SECURITY-ACCESS")
        parser.readDiagnosticSecurityAccess(element, security_access)
        return security_access

    def test_with_all_fields(self, parser):
        """Test that the two attributes and two refs are read with field values."""
        inner = (
            "<SHORT-NAME>SecAccess1</SHORT-NAME>"
            "<REQUEST-SEED-ID>259</REQUEST-SEED-ID>"
            '<SECURITY-ACCESS-CLASS-REF DEST="DIAGNOSTIC-SECURITY-ACCESS-CLASS">/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass</SECURITY-ACCESS-CLASS-REF>'
            "<SECURITY-DELAY-TIME-ON-BOOT>3.0</SECURITY-DELAY-TIME-ON-BOOT>"
            '<SECURITY-LEVEL-REF DEST="DIAGNOSTIC-SECURITY-LEVEL">/AUTOSAR/DiagnosticSecurityLevels/Level1</SECURITY-LEVEL-REF>'
        )
        security_access = self._read(parser, inner)
        assert security_access.getShortName() == "SecAccess1"
        request_seed_id = security_access.getRequestSeedId()
        assert request_seed_id is not None
        assert request_seed_id.getValue() == 259
        security_access_class_ref = security_access.getSecurityAccessClass()
        assert security_access_class_ref is not None
        assert security_access_class_ref.getValue() == "/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass"
        assert security_access_class_ref.getDest() == "DIAGNOSTIC-SECURITY-ACCESS-CLASS"
        security_delay_time_on_boot = security_access.getSecurityDelayTimeOnBoot()
        assert security_delay_time_on_boot is not None
        assert security_delay_time_on_boot.getValue() == 3.0
        security_level_ref = security_access.getSecurityLevel()
        assert security_level_ref is not None
        assert security_level_ref.getValue() == "/AUTOSAR/DiagnosticSecurityLevels/Level1"
        assert security_level_ref.getDest() == "DIAGNOSTIC-SECURITY-LEVEL"

    def test_without_fields(self, parser):
        """Test that absent children leave all four fields None."""
        security_access = self._read(parser, "<SHORT-NAME>SecAccess1</SHORT-NAME>")
        assert security_access.getRequestSeedId() is None
        assert security_access.getSecurityAccessClass() is None
        assert security_access.getSecurityDelayTimeOnBoot() is None
        assert security_access.getSecurityLevel() is None
