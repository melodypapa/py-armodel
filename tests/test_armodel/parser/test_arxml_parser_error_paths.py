"""Tests for error/warning paths and converters in AbstractARXMLParser.

Targets the uncovered branches in `src/armodel/parser/abstract_arxml_parser.py`:
- raiseError / notImplemented / raiseWarning (warning-mode vs raise-mode)
- _convertStringToBooleanValue / _convertStringToNumberValue
- Optional-element getters' null and error branches
- Required-element getters' raise branches
- Abstract instantiation guard
"""

import logging

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.abstract_arxml_parser import AbstractARXMLParser
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance (concrete subclass of AbstractARXMLParser)."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    """Parser configured in warning mode (logs instead of raising)."""
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _snip(inner_xml: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner_xml}</ROOT>")


# ==================== Abstract instantiation guard ====================


class TestAbstractInstantiation:
    def test_AbstractARXMLParser_cannot_be_instantiated(self):
        with pytest.raises(TypeError, match="abstract class"):
            AbstractARXMLParser()


# ==================== raiseError / notImplemented / raiseWarning ====================


class TestErrorAndWarning:
    def test_raiseError_raises_ValueError_by_default(self, parser):
        with pytest.raises(ValueError, match="boom"):
            parser.raiseError("boom")

    def test_raiseError_logs_in_warning_mode(self, warning_parser, caplog):
        with caplog.at_level(logging.ERROR):
            warning_parser.raiseError("soft fail")
        assert any("soft fail" in rec.getMessage() for rec in caplog.records)
        # Should NOT raise
        assert warning_parser.options["warning"] is True

    def test_notImplemented_raises_NotImplementedError_by_default(self, parser):
        with pytest.raises(NotImplementedError, match="not yet"):
            parser.notImplemented("not yet")

    def test_notImplemented_logs_in_warning_mode(self, warning_parser, caplog):
        with caplog.at_level(logging.ERROR):
            warning_parser.notImplemented("skip")
        assert any("skip" in rec.getMessage() for rec in caplog.records)

    def test_raiseWarning_always_logs(self, parser, caplog):
        with caplog.at_level(logging.WARNING):
            parser.raiseWarning("careful")
        assert any("careful" in rec.getMessage() for rec in caplog.records)


# ==================== String converters ====================


class TestStringConverters:
    def test_convertStringToBooleanValue_true(self, parser):
        assert parser._convertStringToBooleanValue("true") is True

    def test_convertStringToBooleanValue_false_for_non_true(self, parser):
        # Any value other than literal "true" is interpreted as False.
        assert parser._convertStringToBooleanValue("false") is False
        assert parser._convertStringToBooleanValue("False") is False
        assert parser._convertStringToBooleanValue("0") is False
        assert parser._convertStringToBooleanValue("") is False

    def test_convertStringToNumberValue_decimal(self, parser):
        assert parser._convertStringToNumberValue("42") == 42
        assert parser._convertStringToNumberValue("-7") == -7

    def test_convertStringToNumberValue_hex_lowercase(self, parser):
        assert parser._convertStringToNumberValue("0xff") == 255

    def test_convertStringToNumberValue_hex_uppercase(self, parser):
        # re.I is used, so 0X should also match.
        assert parser._convertStringToNumberValue("0X10") == 16

    def test_convertStringToNumberValue_hex_short_value(self, parser):
        assert parser._convertStringToNumberValue("0xa") == 10


# ==================== Required-element getters (raise on missing) ====================


class TestRequiredGetters:
    def test_getShortName_missing_raises_ValueError(self, parser):
        element = _snip("<NO-SHORT-NAME>foo</NO-SHORT-NAME>")
        with pytest.raises(ValueError, match="Short Name is required"):
            parser.getShortName(element)

    def test_getChildElementLiteral_missing_raises_ValueError(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        with pytest.raises(ValueError, match="has not been defined"):
            parser.getChildElementLiteral("X", element, "MISSING-KEY")

    def test_getChildElementLiteral_present_returns_literal(self, parser):
        element = _snip("<NAME>hello</NAME>")
        literal = parser.getChildElementLiteral("X", element, "NAME")
        assert literal is not None
        assert literal.getValue() == "hello"

    def test_getChildElementRefType_missing_raises_ValueError(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        with pytest.raises(ValueError, match="has not been defined"):
            parser.getChildElementRefType("X", element, "MISSING-REF")


# ==================== Optional-element getters (None handling) ====================


class TestOptionalGetters:
    def test_getChildElementOptionalLiteral_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalLiteral(element, "ABSENT") is None

    def test_getChildElementOptionalLiteral_empty_text_returns_empty_string(self, parser):
        # Empty element <X></X> — text is None and gets converted to "".
        element = _snip("<EMPTY></EMPTY>")
        literal = parser.getChildElementOptionalLiteral(element, "EMPTY")
        assert literal is not None
        assert literal.getText() == ""

    def test_getChildElementOptionalLiteral_with_text(self, parser):
        element = _snip("<NAME>value</NAME>")
        literal = parser.getChildElementOptionalLiteral(element, "NAME")
        assert literal is not None
        assert literal.getText() == "value"

    def test_getChildElementOptionalFloatValue_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalFloatValue(element, "ABSENT") is None

    def test_getChildElementOptionalFloatValue_empty_text_returns_None(self, parser):
        # Element exists but text is None → returns None (per implementation).
        element = _snip("<VAL></VAL>")
        assert parser.getChildElementOptionalFloatValue(element, "VAL") is None

    def test_getChildElementOptionalFloatValue_with_value(self, parser):
        element = _snip("<VAL>3.14</VAL>")
        f = parser.getChildElementOptionalFloatValue(element, "VAL")
        assert f is not None
        assert float(f.getValue()) == pytest.approx(3.14)

    def test_getChildElementOptionalTimeValue_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalTimeValue(element, "ABSENT") is None

    def test_getChildElementOptionalTimeValue_empty_text_returns_None(self, parser):
        element = _snip("<T></T>")
        assert parser.getChildElementOptionalTimeValue(element, "T") is None

    def test_getChildElementOptionalIntegerValue_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalIntegerValue(element, "ABSENT") is None

    def test_getChildElementOptionalIntegerValue_with_value(self, parser):
        element = _snip("<V>42</V>")
        i = parser.getChildElementOptionalIntegerValue(element, "V")
        assert i is not None
        assert i.getValue() == 42

    def test_getChildElementOptionalPositiveInteger_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalPositiveInteger(element, "ABSENT") is None

    def test_getChildElementOptionalPositiveInteger_empty_text_returns_None(self, parser):
        element = _snip("<V></V>")
        assert parser.getChildElementOptionalPositiveInteger(element, "V") is None

    def test_getChildElementOptionalPositiveInteger_negative_raises(self, parser):
        element = _snip("<V>-5</V>")
        with pytest.raises(ValueError, match="Invalid PositiveInteger"):
            parser.getChildElementOptionalPositiveInteger(element, "V")

    def test_getChildElementOptionalPositiveInteger_valid(self, parser):
        element = _snip("<V>5</V>")
        v = parser.getChildElementOptionalPositiveInteger(element, "V")
        assert v is not None
        assert v.getValue() == 5


class TestOptionalBooleanValue:
    def test_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalBooleanValue(element, "ABSENT") is None

    def test_empty_text_returns_None(self, parser):
        element = _snip("<B></B>")
        # getChildElementOptionalLiteral returns "" for empty, bool getter returns None.
        assert parser.getChildElementOptionalBooleanValue(element, "B") is None

    def test_true_returns_Boolean(self, parser):
        element = _snip("<B>true</B>")
        b = parser.getChildElementOptionalBooleanValue(element, "B")
        assert b is not None
        assert b.getValue() is True

    def test_false_returns_Boolean(self, parser):
        element = _snip("<B>false</B>")
        b = parser.getChildElementOptionalBooleanValue(element, "B")
        assert b is not None
        assert b.getValue() is False


class TestOptionalRevisionLabelString:
    def test_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalRevisionLabelString(element, "ABSENT") is None

    def test_none_text_returns_None(self, parser):
        element = _snip("<R></R>")
        assert parser.getChildElementOptionalRevisionLabelString(element, "R") is None

    def test_valid_value(self, parser):
        element = _snip("<R>1.0.0</R>")
        v = parser.getChildElementOptionalRevisionLabelString(element, "R")
        assert v is not None
        assert v.getValue() == "1.0.0"

    def test_valid_value_with_suffix(self, parser):
        element = _snip("<R>1.2.3;build5</R>")
        v = parser.getChildElementOptionalRevisionLabelString(element, "R")
        assert v is not None
        assert v.getValue() == "1.2.3;build5"

    def test_invalid_format_raises_ValueError(self, parser):
        element = _snip("<R>not-a-version</R>")
        with pytest.raises(ValueError, match="Invalid RevisionLabelString"):
            parser.getChildElementOptionalRevisionLabelString(element, "R")


# ==================== List getters ====================


class TestListGetters:
    def test_getChildElementLiteralValueList_empty(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementLiteralValueList(element, "ITEM") == []

    def test_getChildElementLiteralValueList_multiple(self, parser):
        element = _snip("<ITEMS><ITEM>a</ITEM><ITEM>b</ITEM></ITEMS>")
        result = parser.getChildElementLiteralValueList(element, "ITEMS/ITEM")
        assert [r.getValue() for r in result] == ["a", "b"]

    def test_getChildElementFloatValueList_empty(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementFloatValueList(element, "ITEM") == []

    def test_getChildElementFloatValueList_multiple(self, parser):
        element = _snip("<ITEMS><ITEM>1.5</ITEM><ITEM>2.5</ITEM></ITEMS>")
        result = parser.getChildElementFloatValueList(element, "ITEMS/ITEM")
        assert [float(r.getValue()) for r in result] == [1.5, 2.5]

    def test_getChildElementNumericalValueList_empty(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementNumericalValueList(element, "ITEM") == []

    def test_getChildElementNumericalValueList_multiple(self, parser):
        element = _snip("<ITEMS><ITEM>1</ITEM><ITEM>2</ITEM></ITEMS>")
        result = parser.getChildElementNumericalValueList(element, "ITEMS/ITEM")
        assert [r.getValue() for r in result] == [1, 2]


# ==================== Limit element ====================


class TestChildLimitElement:
    def test_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildLimitElement(element, "ABSENT") is None

    def test_with_interval_type(self, parser):
        element = _snip('<L INTERVAL-TYPE="CLOSED">100</L>')
        limit = parser.getChildLimitElement(element, "L")
        assert limit is not None
        assert limit.intervalType == "CLOSED"
        assert limit.value == "100"

    def test_without_interval_type(self, parser):
        element = _snip("<L>50</L>")
        limit = parser.getChildLimitElement(element, "L")
        assert limit is not None
        assert limit.intervalType is None
        assert limit.value == "50"


# ==================== RefType getters ====================


class TestRefTypeGetters:
    def test_getChildElementOptionalRefType_missing_returns_None(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalRefType(element, "ABSENT") is None

    def test_getChildElementOptionalRefType_with_base_and_dest(self, parser):
        element = _snip(
            '<R BASE="b" DEST="UNIT">/pkg/u</R>'
        )
        ref = parser.getChildElementOptionalRefType(element, "R")
        assert ref is not None
        assert ref.getBase() == "b"
        assert ref.getDest() == "UNIT"
        assert ref.getValue() == "/pkg/u"

    def test_getChildElementOptionalRefType_minimal(self, parser):
        element = _snip("<R>/pkg/u</R>")
        ref = parser.getChildElementOptionalRefType(element, "R")
        assert ref is not None
        assert ref.getValue() == "/pkg/u"

    def test_getChildElementRefTypeList_empty(self, parser):
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementRefTypeList(element, "ITEM") == []

    def test_getChildElementRefTypeList_multiple(self, parser):
        element = _snip(
            "<ITEMS>"
            "<R DEST=\"UNIT\">/a</R>"
            "<R DEST=\"UNIT\">/b</R>"
            "</ITEMS>"
        )
        result = parser.getChildElementRefTypeList(element, "ITEMS/R")
        assert len(result) == 2
        assert [r.getValue() for r in result] == ["/a", "/b"]


# ==================== Misc utility methods ====================


class TestUtilityMethods:
    def test_readElementOptionalAttrib_present(self, parser):
        root = _snip('<X T="t1" UUID="u1"/>')
        element = parser.find(root, "X")
        assert parser.readElementOptionalAttrib(element, "T") == "t1"
        assert parser.readElementOptionalAttrib(element, "UUID") == "u1"

    def test_readElementOptionalAttrib_absent_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.readElementOptionalAttrib(element, "MISSING") is None

    def test_getPureTagName_strips_namespace(self, parser):
        assert parser.getPureTagName(f"{{{NS}}}SHORT-NAME") == "SHORT-NAME"
        assert parser.getPureTagName("SHORT-NAME") == "SHORT-NAME"

    def test_convert_find_key_preserves_wildcards(self, parser):
        # "*" and "." should not be prefixed with xmlns:
        key = parser.convert_find_key("AR-PACKAGES/*")
        assert key == "xmlns:AR-PACKAGES/*"

    def test_convert_find_key_preserves_dot(self, parser):
        key = parser.convert_find_key("./SHORT-NAME")
        assert key == "./xmlns:SHORT-NAME"

    def test_convert_find_key_plain(self, parser):
        key = parser.convert_find_key("SHORT-NAME")
        assert key == "xmlns:SHORT-NAME"


# ==================== readARObjectAttributes ====================


class TestReadARObjectAttributes:
    def test_reads_timestamp_and_uuid(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        root = _snip('<X T="t1" UUID="u1"/>')
        element = parser.find(root, "X")
        obj = ARLiteral()
        parser.readARObjectAttributes(element, obj)
        assert obj.timestamp == "t1"
        assert obj.uuid == "u1"

    def test_handles_missing_attributes(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        root = _snip("<X/>")
        element = parser.find(root, "X")
        obj = ARLiteral()
        parser.readARObjectAttributes(element, obj)
        assert obj.timestamp is None
        assert obj.uuid is None


# ==================== getAUTOSARInfo ====================


class TestGetAUTOSARInfo:
    def test_records_schema_location(self, parser):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc

        document = AUTOSARDoc()
        element = ET.fromstring(
            f"<AUTOSAR xmlns='{NS}' "
            f"xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' "
            f"xsi:schemaLocation='http://autosar.org/schema/r4.0 AUTOSAR.xsd'>"
            f"</AUTOSAR>"
        )
        parser.getAUTOSARInfo(element, document)
        assert document.schema_location.startswith("http://autosar.org/schema/r4.0")

    def test_no_schema_location(self, parser):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc

        document = AUTOSARDoc()
        element = _snip("<X/>")
        # Should be a no-op; should not raise.
        parser.getAUTOSARInfo(element, document)


# ==================== Additional Branch Coverage ====================


class TestAdditionalBranchCoverage:
    """Additional tests for uncovered branches in abstract_arxml_parser.py."""

    def test_getChildElementLiteral_empty_element_returns_empty_literal(self, parser):
        element = _snip("<NAME></NAME>")
        literal = parser.getChildElementLiteral("X", element, "NAME")
        assert literal is not None
        assert literal.getValue() == ""

    def test_getChildElementLiteralValueList_single_element(self, parser):
        element = _snip("<ITEMS><ITEM>only</ITEM></ITEMS>")
        result = parser.getChildElementLiteralValueList(element, "ITEMS/ITEM")
        assert len(result) == 1
        assert result[0].getValue() == "only"

    def test_getChildElementOptionalLiteral_with_attributes(self, parser):
        element = _snip('<NAME T="ts" UUID="uid">value</NAME>')
        literal = parser.getChildElementOptionalLiteral(element, "NAME")
        assert literal is not None
        assert literal.timestamp == "ts"
        assert literal.uuid == "uid"

    def test_getChildElementOptionalFloatValue_with_value(self, parser):
        element = _snip("<VAL>3.14159</VAL>")
        f = parser.getChildElementOptionalFloatValue(element, "VAL")
        assert f is not None
        assert float(f.getValue()) == pytest.approx(3.14159)

    def test_getChildElementOptionalFloatValue_scientific_notation(self, parser):
        element = _snip("<VAL>1.5e-3</VAL>")
        f = parser.getChildElementOptionalFloatValue(element, "VAL")
        assert f is not None
        assert float(f.getValue()) == pytest.approx(0.0015)

    def test_getChildElementOptionalTimeValue_with_value(self, parser):
        element = _snip("<T>0.5</T>")
        t = parser.getChildElementOptionalTimeValue(element, "T")
        assert t is not None

    def test_getChildElementOptionalIntegerValue_negative(self, parser):
        element = _snip("<V>-42</V>")
        i = parser.getChildElementOptionalIntegerValue(element, "V")
        assert i is not None
        assert i.getValue() == -42

    def test_getChildElementOptionalIntegerValue_hex(self, parser):
        element = _snip("<V>0x10</V>")
        i = parser.getChildElementOptionalIntegerValue(element, "V")
        assert i is not None
        assert i.getValue() == 16

    def test_getChildElementOptionalBooleanValue_with_attributes(self, parser):
        element = _snip('<B T="ts">true</B>')
        b = parser.getChildElementOptionalBooleanValue(element, "B")
        assert b is not None
        assert b.timestamp == "ts"

    def test_getChildElementOptionalPositiveInteger_zero(self, parser):
        element = _snip("<V>0</V>")
        v = parser.getChildElementOptionalPositiveInteger(element, "V")
        assert v is not None
        assert v.getValue() == 0

    def test_getChildElementOptionalPositiveInteger_large_value(self, parser):
        element = _snip("<V>999999</V>")
        v = parser.getChildElementOptionalPositiveInteger(element, "V")
        assert v is not None
        assert v.getValue() == 999999

    def test_getChildLimitElement_with_value(self, parser):
        element = _snip("<L>100</L>")
        limit = parser.getChildLimitElement(element, "L")
        assert limit is not None
        assert limit.value == "100"

    def test_getChildElementRefType_with_value_only(self, parser):
        element = _snip("<R>/path/to/ref</R>")
        ref = parser.getChildElementRefType("X", element, "R")
        assert ref is not None
        assert ref.getValue() == "/path/to/ref"
        assert ref.getDest() is None
        assert ref.getBase() is None

    def test_getChildElementOptionalRefType_minimal_attributes(self, parser):
        element = _snip('<R DEST="TYPE">/ref</R>')
        ref = parser.getChildElementOptionalRefType(element, "R")
        assert ref is not None
        assert ref.getDest() == "TYPE"
        assert ref.getBase() is None

    def test_getChildElementRefTypeList_single_element(self, parser):
        element = _snip("<ITEMS><R DEST=\"UNIT\">/a</R></ITEMS>")
        result = parser.getChildElementRefTypeList(element, "ITEMS/R")
        assert len(result) == 1
        assert result[0].getValue() == "/a"

    def test_getChildElementRefTypeList_empty_result(self, parser):
        element = _snip("<ITEMS></ITEMS>")
        result = parser.getChildElementRefTypeList(element, "ITEMS/R")
        assert result == []

    def test_readElementOptionalAttrib_multiple_attrs(self, parser):
        root = _snip('<X T="t1" UUID="u1" OTHER="val"/>')
        element = parser.find(root, "X")
        assert parser.readElementOptionalAttrib(element, "T") == "t1"
        assert parser.readElementOptionalAttrib(element, "UUID") == "u1"
        assert parser.readElementOptionalAttrib(element, "OTHER") == "val"

    def test_convert_find_key_complex_path(self, parser):
        key = parser.convert_find_key("AR-PACKAGES/AR-PACKAGE/ELEMENTS/ELEMENT")
        assert "xmlns:AR-PACKAGES" in key
        assert "xmlns:AR-PACKAGE" in key

    def test_find_nested_path(self, parser):
        element = _snip("""
            <CONTAINER>
                <NESTED>
                    <ITEM>value</ITEM>
                </NESTED>
            </CONTAINER>
        """)
        item = parser.find(element, "CONTAINER/NESTED/ITEM")
        assert item is not None
        assert item.text == "value"

    def test_findall_nested_path(self, parser):
        element = _snip("""
            <CONTAINER>
                <NESTED>
                    <ITEM>1</ITEM>
                    <ITEM>2</ITEM>
                </NESTED>
            </CONTAINER>
        """)
        items = parser.findall(element, "CONTAINER/NESTED/ITEM")
        assert len(items) == 2

    def test_getChildElementOptionalNumericalValue_with_short_label(self, parser):
        element = _snip('<NUM SHORT-LABEL="SL">42</NUM>')
        result = parser.getChildElementOptionalNumericalValue(element, "NUM")
        assert result is not None
        assert result.shortLabel == "SL"
        assert result.getValue() == 42.0

    def test_getChildElementOptionalRevisionLabelString_valid(self, parser):
        element = _snip("<R>4.0.0</R>")
        v = parser.getChildElementOptionalRevisionLabelString(element, "R")
        assert v is not None
        assert v.getValue() == "4.0.0"

    def test_getChildElementOptionalRevisionLabelString_with_build_suffix(self, parser):
        element = _snip("<R>4.2.3;build123</R>")
        v = parser.getChildElementOptionalRevisionLabelString(element, "R")
        assert v is not None
        assert v.getValue() == "4.2.3;build123"

    def test_getChildElementOptionalRevisionLabelString_invalid_raises(self, parser):
        element = _snip("<R>invalid-version</R>")
        with pytest.raises(ValueError, match="Invalid RevisionLabelString"):
            parser.getChildElementOptionalRevisionLabelString(element, "R")

    def test_getChildElementOptionalRevisionLabelString_empty_returns_None(self, parser):
        element = _snip("<R></R>")
        result = parser.getChildElementOptionalRevisionLabelString(element, "R")
        assert result is None

    def test_convertStringToNumberValue_zero(self, parser):
        assert parser._convertStringToNumberValue("0") == 0

    def test_convertStringToNumberValue_large_hex(self, parser):
        assert parser._convertStringToNumberValue("0xFFFFFFFF") == 0xFFFFFFFF

    def test_readARObjectAttributes_with_both_attrs(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        element = ET.fromstring(f"<ROOT xmlns='{NS}' T='timestamp' UUID='unique-id'/>")
        obj = ARLiteral()
        parser.readARObjectAttributes(element, obj)
        assert obj.timestamp == "timestamp"
        assert obj.uuid == "unique-id"

    def test_getChildElementFloatValueList_empty(self, parser):
        element = _snip("<CONTAINER></CONTAINER>")
        result = parser.getChildElementFloatValueList(element, "CONTAINER/V")
        assert result == []

    def test_getChildElementNumericalValueList_with_values(self, parser):
        element = _snip("<ITEMS><ITEM>10</ITEM><ITEM>20</ITEM></ITEMS>")
        result = parser.getChildElementNumericalValueList(element, "ITEMS/ITEM")
        assert len(result) == 2
        assert [r.getValue() for r in result] == [10.0, 20.0]
