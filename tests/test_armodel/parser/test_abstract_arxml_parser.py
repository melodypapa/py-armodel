"""Tests for abstract_arxml_parser module."""

import logging
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock, patch

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral, ARNumerical, Integer, PositiveInteger, Boolean,
    ARFloat, TimeValue, RevisionLabelString, RefType, Limit
)
from armodel.parser.abstract_arxml_parser import AbstractARXMLParser


class ConcreteARXMLParser(AbstractARXMLParser):
    """Concrete implementation of AbstractARXMLParser for testing."""
    pass


class TestAbstractARXMLParserInit:
    """Tests for AbstractARXMLParser initialization."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractARXMLParser abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="AbstractArxmlParser is an abstract class."):
            AbstractARXMLParser()

    def test_concrete_class_initialization_default_options(self):
        """Test concrete class initialization with default options."""
        parser = ConcreteARXMLParser()
        assert parser.options['warning'] is False
        assert parser.nsmap == {"xmlns": "http://autosar.org/schema/r4.0"}

    def test_concrete_class_initialization_with_warning_option(self):
        """Test concrete class initialization with warning option."""
        parser = ConcreteARXMLParser(options={'warning': True})
        assert parser.options['warning'] is True

    def test_process_options_with_warning(self):
        """Test _processOptions sets warning option."""
        parser = ConcreteARXMLParser(options={'warning': True})
        assert parser.options['warning'] is True


class TestGetTagName:
    """Tests for getTagName method."""

    def test_getTagName_with_element(self):
        """Test getTagName with ET.Element."""
        parser = ConcreteARXMLParser()
        element = ET.Element("{http://autosar.org/schema/r4.0}SHORT-NAME")
        result = parser.getTagName(element)
        assert result == "SHORT-NAME"

    def test_getTagName_with_string(self):
        """Test getTagName with string tag."""
        parser = ConcreteARXMLParser()
        tag = "{http://autosar.org/schema/r4.0}SHORT-NAME"
        result = parser.getTagName(tag)
        assert result == "SHORT-NAME"

    def test_getTagName_with_invalid_type(self, caplog):
        """Test getTagName with invalid type raises ValueError."""
        parser = ConcreteARXMLParser(options={'warning': False})
        with pytest.raises(ValueError, match="Invalid Tag type"):
            parser.getTagName(123)

    def test_getTagName_with_invalid_type_warning_mode(self, caplog):
        """Test getTagName with invalid type logs error in warning mode."""
        parser = ConcreteARXMLParser(options={'warning': True})
        with caplog.at_level(logging.ERROR):
            parser.getTagName(123)
        assert "Invalid Tag type" in caplog.text


class TestRaiseError:
    """Tests for raiseError method."""

    def test_raiseError_without_warning_mode(self):
        """Test raiseError raises ValueError when warning mode is False."""
        
        parser = ConcreteARXMLParser(options={'warning': False})
        with pytest.raises(ValueError, match="Test error message"):
            parser.raiseError("Test error message")

    def test_raiseError_with_warning_mode(self, caplog):
        """Test raiseError logs error when warning mode is True."""
        
        parser = ConcreteARXMLParser(options={'warning': True})
        with caplog.at_level(logging.ERROR):
            parser.raiseError("Test error message")
        assert "Test error message" in caplog.text


class TestNotImplemented:
    """Tests for notImplemented method."""

    def test_notImplemented_without_warning_mode(self):
        """Test notImplemented raises NotImplementedError when warning mode is False."""
        
        parser = ConcreteARXMLParser(options={'warning': False})
        with pytest.raises(NotImplementedError, match="Not implemented feature"):
            parser.notImplemented("Not implemented feature")

    def test_notImplemented_with_warning_mode(self, caplog):
        """Test notImplemented logs error when warning mode is True."""
        
        parser = ConcreteARXMLParser(options={'warning': True})
        with caplog.at_level(logging.ERROR):
            parser.notImplemented("Not implemented feature")
        assert "Not implemented feature" in caplog.text


class TestRaiseWarning:
    """Tests for raiseWarning method."""

    def test_raiseWarning(self, caplog):
        """Test raiseWarning logs warning."""
        
        parser = ConcreteARXMLParser()
        with caplog.at_level(logging.WARNING):
            parser.raiseWarning("Test warning message")
        assert "Test warning message" in caplog.text


class TestGetPureTagName:
    """Tests for getPureTagName method."""

    def test_getPureTagName(self):
        """Test getPureTagName removes namespace."""
        
        parser = ConcreteARXMLParser()
        tag = "{http://autosar.org/schema/r4.0}SHORT-NAME"
        result = parser.getPureTagName(tag)
        assert result == "SHORT-NAME"


class TestGetChildElementLiteral:
    """Tests for getChildElementLiteral method."""

    def test_getChildElementLiteral_found(self):
        """Test getChildElementLiteral when element is found."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = "test-value"

        result = parser.getChildElementLiteral("parent", parent, "child")
        assert isinstance(result, ARLiteral)
        assert result._value == "test-value"

    def test_getChildElementLiteral_not_found(self):
        """Test getChildElementLiteral when element is not found."""
        
        parser = ConcreteARXMLParser(options={'warning': False})
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")

        with pytest.raises(ValueError, match="has not been defined"):
            parser.getChildElementLiteral("parent", parent, "child")


class TestGetChildElementOptionalRevisionLabelString:
    """Tests for getChildElementOptionalRevisionLabelString method."""

    def test_getChildElementOptionalRevisionLabelString_valid(self):
        """Test getChildElementOptionalRevisionLabelString with valid version."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = "1.0.0"

        result = parser.getChildElementOptionalRevisionLabelString(parent, "child")
        assert isinstance(result, RevisionLabelString)
        assert result.getValue() == "1.0.0"

    def test_getChildElementOptionalRevisionLabelString_invalid_format(self):
        """Test getChildElementOptionalRevisionLabelString with invalid format."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = "invalid"

        with pytest.raises(ValueError, match="Invalid RevisionLabelString"):
            parser.getChildElementOptionalRevisionLabelString(parent, "child")

    def test_getChildElementOptionalRevisionLabelString_none_text(self):
        """Test getChildElementOptionalRevisionLabelString with None text."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")

        result = parser.getChildElementOptionalRevisionLabelString(parent, "child")
        assert result is None


class TestGetChildElementOptionalDataTime:
    """Tests for getChildElementOptionalDataTime method."""

    def test_getChildElementOptionalDataTime(self):
        """Test getChildElementOptionalDataTime returns optional literal."""

        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = "2024-01-01T00:00:00"

        result = parser.getChildElementOptionalDataTime(parent, "child")
        assert isinstance(result, ARLiteral)
        assert result.getValue() == "2024-01-01T00:00:00"


class TestConvertStringToBooleanValue:
    """Tests for _convertStringToBooleanValue method."""

    def test_convertStringToBooleanValue_true(self):
        """Test _convertStringToBooleanValue with 'true'."""
        
        parser = ConcreteARXMLParser()
        result = parser._convertStringToBooleanValue("true")
        assert result is True

    def test_convertStringToBooleanValue_false(self):
        """Test _convertStringToBooleanValue with non-'true' value."""
        
        parser = ConcreteARXMLParser()
        result = parser._convertStringToBooleanValue("false")
        assert result is False

    def test_convertStringToBooleanValue_other(self):
        """Test _convertStringToBooleanValue with any non-'true' value returns False."""
        
        parser = ConcreteARXMLParser()
        result = parser._convertStringToBooleanValue("anything")
        assert result is False


class TestGetChildElementFloatValueList:
    """Tests for getChildElementFloatValueList method."""

    def test_getChildElementFloatValueList(self):
        """Test getChildElementFloatValueList returns list of ARFloat."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child1 = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child1.text = "3.14"
        child2 = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child2.text = "2.71"

        result = parser.getChildElementFloatValueList(parent, "child")
        assert len(result) == 2
        assert all(isinstance(item, ARFloat) for item in result)


class TestGetChildElementOptionalBooleanValue:
    """Tests for getChildElementOptionalBooleanValue method."""

    def test_getChildElementOptionalBooleanValue_empty_text(self):
        """Test getChildElementOptionalBooleanValue with empty text returns None."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = ""

        result = parser.getChildElementOptionalBooleanValue(parent, "child")
        assert result is None


class TestConvertStringToNumberValue:
    """Tests for _convertStringToNumberValue method."""

    def test_convertStringToNumberValue_hex_lowercase(self):
        """Test _convertStringToNumberValue with lowercase hex."""
        
        parser = ConcreteARXMLParser()
        result = parser._convertStringToNumberValue("0xff")
        assert result == 255

    def test_convertStringToNumberValue_hex_uppercase(self):
        """Test _convertStringToNumberValue with uppercase hex."""
        
        parser = ConcreteARXMLParser()
        result = parser._convertStringToNumberValue("0xFF")
        assert result == 255

    def test_convertStringToNumberValue_decimal(self):
        """Test _convertStringToNumberValue with decimal."""
        
        parser = ConcreteARXMLParser()
        result = parser._convertStringToNumberValue("42")
        assert result == 42


class TestGetChildElementOptionalNumericalValue:
    """Tests for getChildElementOptionalNumericalValue method."""

    def test_getChildElementOptionalNumericalValue_with_short_label(self):
        """Test getChildElementOptionalNumericalValue with SHORT-LABEL attribute."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = "123"
        child.set("SHORT-LABEL", "test")

        result = parser.getChildElementOptionalNumericalValue(parent, "child")
        assert isinstance(result, ARNumerical)
        assert result.getShortLabel() == "test"


class TestGetChildElementOptionalPositiveInteger:
    """Tests for getChildElementOptionalPositiveInteger method."""

    def test_getChildElementOptionalPositiveInteger_none_text(self):
        """Test getChildElementOptionalPositiveInteger with None text returns None."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")

        result = parser.getChildElementOptionalPositiveInteger(parent, "child")
        assert result is None

    def test_getChildElementOptionalPositiveInteger_negative_value(self):
        """Test getChildElementOptionalPositiveInteger with negative value."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = "-1"

        with pytest.raises(ValueError, match="Invalid PositiveInteger"):
            parser.getChildElementOptionalPositiveInteger(parent, "child")


class TestGetChildElementNumericalValueList:
    """Tests for getChildElementNumericalValueList method."""

    def test_getChildElementNumericalValueList(self):
        """Test getChildElementNumericalValueList returns list of ARNumerical."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child1 = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child1.text = "123"
        child2 = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child2.text = "456"

        result = parser.getChildElementNumericalValueList(parent, "child")
        assert len(result) == 2
        assert all(isinstance(item, ARNumerical) for item in result)


class TestGetChildLimitElement:
    """Tests for getChildLimitElement method."""

    def test_getChildLimitElement_without_interval_type(self):
        """Test getChildLimitElement without INTERVAL-TYPE attribute."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")
        child = ET.SubElement(parent, "{http://autosar.org/schema/r4.0}child")
        child.text = "100"

        result = parser.getChildLimitElement(parent, "child")
        assert isinstance(result, Limit)
        assert result.intervalType is None

    def test_getChildLimitElement_none(self):
        """Test getChildLimitElement when element is None."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")

        result = parser.getChildLimitElement(parent, "child")
        assert result is None


class TestGetChildElementRefType:
    """Tests for getChildElementRefType method."""

    def test_getChildElementRefType_not_found(self):
        """Test getChildElementRefType when element is not found."""
        
        parser = ConcreteARXMLParser(options={'warning': False})
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")

        with pytest.raises(ValueError, match="has not been defined"):
            parser.getChildElementRefType("parent", parent, "child")


class TestGetShortName:
    """Tests for getShortName method."""

    def test_getShortName_not_found(self):
        """Test getShortName when SHORT-NAME element is missing."""
        
        parser = ConcreteARXMLParser()
        parent = ET.Element("{http://autosar.org/schema/r4.0}parent")

        with pytest.raises(ValueError, match="Short Name is required"):
            parser.getShortName(parent)
