import pytest
import tempfile
import os
import xml.etree.cElementTree as ET

from armodel.writer.abstract_arxml_writer import AbstractARXMLWriter
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARFloat, ARLiteral, ARNumerical, DateTime, Integer, 
    RevisionLabelString, TimeValue, RefType, ARBoolean, ARPositiveInteger
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class ConcreteARXMLWriter(AbstractARXMLWriter):
    """Concrete implementation of AbstractARXMLWriter for testing"""
    def __init__(self, options=None):
        super().__init__(options)


class ConcreteTestARObject(Identifiable):
    """Concrete implementation of Identifiable for testing ARObject attributes"""
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)
        self.timestamp = None
        self.uuid = None


class TestAbstractARXMLWriter:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractARXMLWriter abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="AbstractARXMLWriter is an abstract class."):
            AbstractARXMLWriter()

    def test_concrete_class_initialization_default_options(self):
        """Test concrete class initialization with default options"""
        writer = ConcreteARXMLWriter()
        assert writer.options['warning'] is False
        assert writer.options['version'] == "4.2.2"
        assert writer.nsmap == {"xmlns": "http://autosar.org/schema/r4.0"}

    def test_concrete_class_initialization_with_warning_option(self):
        """Test concrete class initialization with warning option"""
        writer = ConcreteARXMLWriter(options={'warning': True})
        assert writer.options['warning'] is True
        assert writer.options['version'] == "4.2.2"

    def test_raise_error_without_warning_mode(self):
        """Test _raiseError raises ValueError when warning mode is False"""
        writer = ConcreteARXMLWriter(options={'warning': False})
        with pytest.raises(ValueError, match="Test error message"):
            writer._raiseError("Test error message")

    def test_raise_error_with_warning_mode(self, caplog):
        """Test _raiseError logs error when warning mode is True"""
        import logging
        writer = ConcreteARXMLWriter(options={'warning': True})
        with caplog.at_level(logging.ERROR):
            writer._raiseError("Test error message")
        assert "Test error message" in caplog.text

    def test_not_implemented_without_warning_mode(self):
        """Test notImplemented raises NotImplementedError when warning mode is False"""
        writer = ConcreteARXMLWriter(options={'warning': False})
        with pytest.raises(NotImplementedError, match="Not implemented feature"):
            writer.notImplemented("Not implemented feature")

    def test_not_implemented_with_warning_mode(self, caplog):
        """Test notImplemented logs error when warning mode is True"""
        import logging
        writer = ConcreteARXMLWriter(options={'warning': True})
        with caplog.at_level(logging.ERROR):
            writer.notImplemented("Not implemented feature")
        assert "Not implemented feature" in caplog.text

    def test_write_ar_object_attributes_with_timestamp(self):
        """Test writeARObjectAttributes with timestamp"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        ar_obj = ConcreteTestARObject(None, "TestObj")
        ar_obj.timestamp = "2024-01-01T00:00:00"
        
        writer.writeARObjectAttributes(parent, ar_obj)
        assert parent.attrib['T'] == "2024-01-01T00:00:00"

    def test_write_ar_object_attributes_with_uuid(self):
        """Test writeARObjectAttributes with UUID"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        ar_obj = ConcreteTestARObject(None, "TestObj")
        ar_obj.uuid = "12345678-1234-1234-1234-123456789012"
        
        writer.writeARObjectAttributes(parent, ar_obj)
        assert parent.attrib['UUID'] == "12345678-1234-1234-1234-123456789012"

    def test_write_ar_object_attributes_with_both(self):
        """Test writeARObjectAttributes with both timestamp and UUID"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        ar_obj = ConcreteTestARObject(None, "TestObj")
        ar_obj.timestamp = "2024-01-01T00:00:00"
        ar_obj.uuid = "12345678-1234-1234-1234-123456789012"
        
        writer.writeARObjectAttributes(parent, ar_obj)
        assert parent.attrib['T'] == "2024-01-01T00:00:00"
        assert parent.attrib['UUID'] == "12345678-1234-1234-1234-123456789012"

    def test_write_ar_object_attributes_without_attributes(self):
        """Test writeARObjectAttributes without timestamp or UUID"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        ar_obj = ConcreteTestARObject(None, "TestObj")
        
        writer.writeARObjectAttributes(parent, ar_obj)
        assert 'T' not in parent.attrib
        assert 'UUID' not in parent.attrib

    def test_set_child_element_optional_numerical_value(self):
        """Test setChildElementOptionalNumericalValue"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        numerical = ARNumerical()
        numerical._text = "123"
        numerical.setValue(123)
        
        writer.setChildElementOptionalNumericalValue(parent, "test-num", numerical)
        assert len(parent) == 1
        child = parent.find("test-num")
        assert child.text == "123"

    def test_set_child_element_optional_numerical_value_with_short_label(self):
        """Test setChildElementOptionalNumericalValue with short label"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        numerical = ARNumerical()
        numerical._text = "456"
        numerical.setValue(456)
        numerical.shortLabel = "test"
        
        writer.setChildElementOptionalNumericalValue(parent, "test-num", numerical)
        child = parent.find("test-num")
        assert child.attrib["SHORT-LABEL"] == "test"
        assert child.text == "456"

    def test_set_child_element_optional_numerical_value_none(self):
        """Test setChildElementOptionalNumericalValue with None"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        
        writer.setChildElementOptionalNumericalValue(parent, "test-num", None)
        assert len(parent) == 0

    def test_set_child_element_optional_integer_value(self):
        """Test setChildElementOptionalIntegerValue"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        integer = Integer()
        integer.setValue(42)
        integer._text = "42"  # Set the text attribute used by writer
        
        writer.setChildElementOptionalIntegerValue(parent, "test-int", integer)
        assert len(parent) == 1
        child = parent.find("test-int")
        assert child.text == "42"

    def test_set_child_element_optional_positive_integer(self):
        """Test setChildElementOptionalPositiveInteger"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        pos_int = ARPositiveInteger()
        pos_int.setValue(100)
        pos_int._text = "100"  # Set the text attribute used by writer
        
        writer.setChildElementOptionalPositiveInteger(parent, "test-pos-int", pos_int)
        assert len(parent) == 1
        child = parent.find("test-pos-int")
        assert child.text == "100"

    def test_set_child_element_optional_revision_label_string(self):
        """Test setChildElementOptionalRevisionLabelString"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        revision = RevisionLabelString()
        revision.setValue("1.0.0")
        
        writer.setChildElementOptionalRevisionLabelString(parent, "test-revision", revision)
        assert len(parent) == 1
        child = parent.find("test-revision")
        assert child.text == "1.0.0"

    def test_set_child_element_optional_date_time(self):
        """Test setChildElementOptionalDataTime"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        datetime = DateTime()
        datetime.setValue("2024-01-01T00:00:00")
        
        writer.setChildElementOptionalDataTime(parent, "test-datetime", datetime)
        assert len(parent) == 1
        child = parent.find("test-datetime")
        assert child.text == "2024-01-01T00:00:00"

    def test_set_child_element_optional_ref_type_with_base(self):
        """Test setChildElementOptionalRefType with BASE attribute"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        ref = RefType()
        ref.setBase("SwComponentType")
        ref.setValue("/AUTOSAR/MyComponent")
        
        writer.setChildElementOptionalRefType(parent, "test-ref", ref)
        assert len(parent) == 1
        child = parent.find("test-ref")
        assert child.attrib['BASE'] == "SwComponentType"
        assert child.text == "/AUTOSAR/MyComponent"

    def test_set_child_element_optional_ref_type_with_dest(self):
        """Test setChildElementOptionalRefType with DEST attribute"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        ref = RefType()
        ref.setDest("SenderReceiverInterface")
        ref.setValue("/AUTOSAR/MyInterface")
        
        writer.setChildElementOptionalRefType(parent, "test-ref", ref)
        assert len(parent) == 1
        child = parent.find("test-ref")
        assert child.attrib['DEST'] == "SenderReceiverInterface"
        assert child.text == "/AUTOSAR/MyInterface"

    def test_set_child_element_optional_ref_type_with_both_base_and_dest(self):
        """Test setChildElementOptionalRefType with both BASE and DEST"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        ref = RefType()
        ref.setBase("SwComponentType")
        ref.setDest("SenderReceiverInterface")
        ref.setValue("/AUTOSAR/MyComponent")
        
        writer.setChildElementOptionalRefType(parent, "test-ref", ref)
        assert len(parent) == 1
        child = parent.find("test-ref")
        assert child.attrib['BASE'] == "SwComponentType"
        assert child.attrib['DEST'] == "SenderReceiverInterface"
        assert child.text == "/AUTOSAR/MyComponent"

    def test_set_child_element_optional_ref_type_none(self):
        """Test setChildElementOptionalRefType with None"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        
        writer.setChildElementOptionalRefType(parent, "test-ref", None)
        assert len(parent) == 0

    def test_set_child_element_optional_float_value(self):
        """Test setChildElementOptionalFloatValue"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        float_val = ARFloat()
        float_val.setValue(3.14)
        
        writer.setChildElementOptionalFloatValue(parent, "test-float", float_val)
        assert len(parent) == 1
        child = parent.find("test-float")
        assert child.text == "3.14"

    def test_set_child_element_optional_time_value(self):
        """Test setChildElementOptionalTimeValue"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        time_val = TimeValue()
        time_val.setValue(0.001)
        
        writer.setChildElementOptionalTimeValue(parent, "test-time", time_val)
        assert len(parent) == 1
        child = parent.find("test-time")
        assert child.text == "0.001"

    def test_set_child_element_optional_boolean_value_true(self):
        """Test setChildElementOptionalBooleanValue with True"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        bool_val = ARBoolean()
        bool_val.setValue(True)
        
        result = writer.setChildElementOptionalBooleanValue(parent, "test-bool", bool_val)
        assert result is parent
        assert len(parent) == 1
        child = parent.find("test-bool")
        assert child.text == "true"

    def test_set_child_element_optional_boolean_value_false(self):
        """Test setChildElementOptionalBooleanValue with False"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        bool_val = ARBoolean()
        bool_val.setValue(False)
        
        writer.setChildElementOptionalBooleanValue(parent, "test-bool", bool_val)
        assert len(parent) == 1
        child = parent.find("test-bool")
        assert child.text == "false"

    def test_set_child_element_optional_literal(self):
        """Test setChildElementOptionalLiteral"""
        writer = ConcreteARXMLWriter()
        parent = ET.Element("parent")
        literal = ARLiteral()
        literal.setValue("test-value")
        
        result = writer.setChildElementOptionalLiteral(parent, "test-literal", literal)
        assert result is parent
        assert len(parent) == 1
        child = parent.find("test-literal")
        assert child.text == "test-value"

    def test_patch_xml_self_closing_tags(self):
        """Test patch_xml converts self-closing tags to open/close format"""
        writer = ConcreteARXMLWriter()
        xml = "<root><empty-tag/><another-empty/></root>"
        result = writer.patch_xml(xml)
        assert "<empty-tag></empty-tag>" in result
        assert "<another-empty></another-empty>" in result

    def test_patch_xml_normal_tags(self):
        """Test patch_xml leaves normal tags unchanged"""
        writer = ConcreteARXMLWriter()
        xml = "<root><tag>content</tag></root>"
        result = writer.patch_xml(xml)
        assert result == xml

    def test_save_to_file(self):
        """Test saveToFile creates XML file"""
        writer = ConcreteARXMLWriter()
        root = ET.Element("AUTOSAR")
        child = ET.SubElement(root, "AR-PACKAGES")
        ET.SubElement(child, "AR-PACKAGE", {"UUID": "test-uuid"})
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.arxml') as tmp:
            tmp_path = tmp.name
        
        try:
            writer.saveToFile(tmp_path, root)
            assert os.path.exists(tmp_path)
            
            with open(tmp_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert '<?xml version' in content
            assert '<AUTOSAR>' in content
            assert '<AR-PACKAGES>' in content
            assert '<AR-PACKAGE' in content
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_save_to_file_with_nested_elements(self):
        """Test saveToFile with nested elements"""
        writer = ConcreteARXMLWriter()
        root = ET.Element("AUTOSAR")
        packages = ET.SubElement(root, "AR-PACKAGES")
        pkg = ET.SubElement(packages, "AR-PACKAGE", {"UUID": "pkg-uuid"})
        ET.SubElement(pkg, "SHORT-NAME").text = "TestPackage"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.arxml') as tmp:
            tmp_path = tmp.name
        
        try:
            writer.saveToFile(tmp_path, root)
            
            with open(tmp_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert 'TestPackage' in content
            assert 'pkg-uuid' in content
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)


class TestARXMLWriterIntegration:
    """Integration tests using the actual ARXMLWriter implementation"""
    
    def test_arxml_writer_initialization(self):
        """Test ARXMLWriter initialization"""
        writer = ARXMLWriter()
        assert writer.options['warning'] is False
        assert writer.options['version'] == "4.2.2"

    def test_arxml_writer_with_warning_option(self):
        """Test ARXMLWriter with warning option"""
        writer = ARXMLWriter(options={'warning': True})
        assert writer.options['warning'] is True

    def test_arxml_writer_write_to_file(self):
        """Test ARXMLWriter writes valid ARXML file"""
        autosar = AUTOSAR.getInstance()
        autosar.clear()
        
        pkg = autosar.createARPackage("TestPackage")
        pkg.createApplicationPrimitiveDataType("TestType")
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.arxml') as tmp:
            tmp_path = tmp.name
        
        try:
            writer = ARXMLWriter()
            writer.save(tmp_path, autosar)
            
            assert os.path.exists(tmp_path)
            
            with open(tmp_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert '<?xml version' in content
            assert 'AUTOSAR' in content
            assert 'TestPackage' in content
            assert 'TestType' in content
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            autosar.clear()