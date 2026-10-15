import logging

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.validation import PrimitivePatternError, warning_mode


class _DummyLiteral(ARLiteral):
    PATTERN = r"[A-Z][a-zA-Z0-9_]*"


class _UnconstrainedLiteral(ARLiteral):
    pass


class TestCheckValue:
    def test_valid_value_accepted(self):
        literal = _DummyLiteral()
        literal.value = "Valid_Name2"
        assert literal.value == "Valid_Name2"

    def test_invalid_value_raises_by_default(self):
        with pytest.raises(PrimitivePatternError) as exc_info:
            _DummyLiteral().value = "9bad"
        assert exc_info.value.class_name == "_DummyLiteral"
        assert exc_info.value.value == "9bad"
        assert exc_info.value.pattern == r"[A-Z][a-zA-Z0-9_]*"

    def test_warning_mode_logs_and_keeps_value(self, caplog):
        literal = _DummyLiteral()
        with warning_mode(True, "test.arxml"), caplog.at_level(logging.WARNING, logger="armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes"):
            literal.value = "9bad"
        assert literal.value == "9bad"
        assert any("9bad" in record.message and "test.arxml" in record.message for record in caplog.records)

    def test_warning_mode_without_context_omits_prefix(self, caplog):
        literal = _DummyLiteral()
        with warning_mode(True), caplog.at_level(logging.WARNING, logger="armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes"):
            literal.value = "9bad"
        assert literal.value == "9bad"
        assert any("9bad" in record.message and "<" not in record.message for record in caplog.records)

    def test_none_pattern_passthrough(self):
        literal = _UnconstrainedLiteral()
        literal.value = "anything ! goes"
        assert literal.value == "anything ! goes"

    def test_empty_string_passthrough(self):
        literal = _DummyLiteral()
        literal.value = ""
        assert literal.value == ""

    def test_nonempty_string_not_a_str_type_still_rejected(self):
        with pytest.raises(ValueError) as exc_info:
            _DummyLiteral().value = 123
        assert "Unsupported Type" in str(exc_info.value)

    def test_set_value_flows_through_check(self):
        literal = _DummyLiteral()
        with pytest.raises(PrimitivePatternError):
            literal.setValue("bad")
        literal.setValue("Good")
        assert literal.getValue() == "Good"

    def test_pattern_cache_reuse(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import _PATTERN_CACHE

        _DummyLiteral().value = "A"
        assert r"[A-Z][a-zA-Z0-9_]*" in _PATTERN_CACHE


class TestPopulatedPatterns:
    def test_meta_class_name_accepts_and_rejects(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MetaClassName

        assert MetaClassName().setValue("MyMetaClass").getValue() == "MyMetaClass"
        with pytest.raises(PrimitivePatternError):
            MetaClassName().value = "lowercaseStart"

    def test_mcd_identifier_accepts_and_rejects(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import McdIdentifier

        assert McdIdentifier().setValue("Cal_prm[3].Sub[0]").getValue() == "Cal_prm[3].Sub[0]"
        with pytest.raises(PrimitivePatternError):
            McdIdentifier().value = "9bad"

    def test_c_identifier_with_index(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifierWithIndex

        assert CIdentifierWithIndex().setValue("Var[12]").getValue() == "Var[12]"
        with pytest.raises(PrimitivePatternError):
            CIdentifierWithIndex().value = "Var"

    def test_ip4_address_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString

        assert Ip4AddressString().setValue("192.168.0.1").getValue() == "192.168.0.1"
        with pytest.raises(PrimitivePatternError):
            Ip4AddressString().value = "999.1.1.1"

    def test_ref_pattern(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ref

        assert Ref().setValue("/Pkg/Elem").getValue() == "/Pkg/Elem"
        with pytest.raises(PrimitivePatternError):
            Ref().value = "/Pkg//Elem"

    def test_c_identifier(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier

        assert CIdentifier().setValue("Cal_prm").getValue() == "Cal_prm"
        with pytest.raises(PrimitivePatternError):
            CIdentifier().value = "9bad"

    def test_strong_revision_label_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import StrongRevisionLabelString

        assert StrongRevisionLabelString().setValue("1.0.0-beta+exp.sha.5114f85").getValue() == "1.0.0-beta+exp.sha.5114f85"
        with pytest.raises(PrimitivePatternError):
            StrongRevisionLabelString().value = "1.2"

    def test_category_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString

        assert CategoryString().setValue("CATEGORY_1").getValue() == "CATEGORY_1"
        with pytest.raises(PrimitivePatternError):
            CategoryString().value = "9category"

    def test_diag_requirement_id_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagRequirementIdString

        assert DiagRequirementIdString().setValue("DiagReq_01").getValue() == "DiagReq_01"
        with pytest.raises(PrimitivePatternError):
            DiagRequirementIdString().value = "req 1"

    def test_identifier(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

        assert Identifier().setValue("Identifier_1").getValue() == "Identifier_1"
        with pytest.raises(PrimitivePatternError):
            Identifier().value = "9bad"

    def test_revision_label_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RevisionLabelString

        assert RevisionLabelString().setValue("4.0.0;12").getValue() == "4.0.0;12"
        with pytest.raises(PrimitivePatternError):
            RevisionLabelString().value = "4.0"

    def test_ip6_address_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip6AddressString

        assert Ip6AddressString().setValue("2001:0db8:85a3:0000:0000:8a2e:0370:7334").getValue() == "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        with pytest.raises(PrimitivePatternError):
            Ip6AddressString().value = "fe80::1"

    def test_mac_address_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString

        assert MacAddressString().setValue("00:1A:2B:3C:4D:5E").getValue() == "00:1A:2B:3C:4D:5E"
        with pytest.raises(PrimitivePatternError):
            MacAddressString().value = "00:1A:2B:3C:4D"

    def test_any_service_instance_id(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AnyServiceInstanceId

        assert AnyServiceInstanceId().setValue("0x1F").getValue() == "0x1F"
        with pytest.raises(PrimitivePatternError):
            AnyServiceInstanceId().value = "-1"

    def test_any_version_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AnyVersionString

        assert AnyVersionString().setValue("30").getValue() == "30"
        with pytest.raises(PrimitivePatternError):
            AnyVersionString().value = "1.0"

    def test_address(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Address

        assert Address().setValue("0xDEADBEEF").getValue() == "0xDEADBEEF"
        with pytest.raises(PrimitivePatternError):
            Address().value = "1234"

    def test_primitive_identifier(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PrimitiveIdentifier

        assert PrimitiveIdentifier().setValue("aB_1").getValue() == "aB_1"
        with pytest.raises(PrimitivePatternError):
            PrimitiveIdentifier().value = "_abc"

    def test_alignment_type(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AlignmentType

        assert AlignmentType().setValue("PTR").getValue() == "PTR"
        with pytest.raises(PrimitivePatternError):
            AlignmentType().value = "FOO"

    def test_display_format_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DisplayFormatString

        assert DisplayFormatString().setValue("%5.2f").getValue() == "%5.2f"
        with pytest.raises(PrimitivePatternError):
            DisplayFormatString().value = "%q"

    def test_date_time(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime

        assert DateTime().setValue("2009-07-23T13:38:00Z").getValue() == "2009-07-23T13:38:00Z"
        with pytest.raises(PrimitivePatternError):
            DateTime().value = "2023-1-2"

    def test_view_tokens(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ViewTokens

        assert ViewTokens().setValue("debug view").getValue() == "debug view"
        with pytest.raises(PrimitivePatternError):
            ViewTokens().value = "1mode"
