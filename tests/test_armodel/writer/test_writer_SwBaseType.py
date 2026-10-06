"""Writer tests for the SwBaseType element and its BaseType aggregation
(Swc TPS Tables 5.22 p.290 / 5.26 p.292).

The XSD group BASE-TYPE (AUTOSAR_00052.xsd line 8384) embeds the
BASE-TYPE-DIRECT-DEFINITION group inline: BASE-TYPE-SIZE (70), BASE-TYPE-ENCODING (90),
MEM-ALIGNMENT (100), BYTE-ORDER (110), NATIVE-DECLARATION (120) - the aggregation is
flattened, so no wrapper element is emitted. Unset definition fields emit nothing.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    BaseTypeEncodingString,
    ByteOrderEnum,
    NativeDeclarationString,
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes import BaseTypeDirectDefinition, SwBaseType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_sw_base_type(short_name: str = "uint8") -> SwBaseType:
    base_type = SwBaseType(None, short_name)
    definition = base_type.getBaseTypeDefinition()
    definition.setBaseTypeSize(PositiveInteger().setValue("8"))
    definition.setBaseTypeEncoding(BaseTypeEncodingString().setValue("IEEE754"))
    definition.setMemAlignment(PositiveInteger().setValue("8"))
    definition.setByteOrder(ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST))
    definition.setNativeDeclaration(NativeDeclarationString().setValue("unsigned char"))
    return base_type


class TestBaseTypeWriter:
    def test_write_base_type_definition_elements(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeSwBaseType(parent_element, _build_sw_base_type())

        element = parent_element.find("SW-BASE-TYPE")
        assert element is not None
        assert element.find("SHORT-NAME").text == "uint8"
        assert element.find("BASE-TYPE-SIZE").text == "8"
        assert element.find("BASE-TYPE-ENCODING").text == "IEEE754"
        assert element.find("MEM-ALIGNMENT").text == "8"
        assert element.find("BYTE-ORDER").text == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert element.find("NATIVE-DECLARATION").text == "unsigned char"

    def test_write_unset_definition_omits_elements(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeSwBaseType(parent_element, SwBaseType(None, "void"))

        element = parent_element.find("SW-BASE-TYPE")
        assert element is not None
        assert element.find("SHORT-NAME").text == "void"
        assert element.find("BASE-TYPE-SIZE") is None
        assert element.find("BASE-TYPE-ENCODING") is None
        assert element.find("MEM-ALIGNMENT") is None
        assert element.find("BYTE-ORDER") is None
        assert element.find("NATIVE-DECLARATION") is None


class TestSwBaseTypeWriter:
    def test_write_element_order_matches_xsd_group(self):
        """SHORT-NAME (IDENTIFIABLE group) first, then the flattened BASE-TYPE group in
        sequenceOffset order (70, 90, 100, 110, 120)."""
        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeSwBaseType(parent_element, _build_sw_base_type())

        element = parent_element.find("SW-BASE-TYPE")
        tags = [child.tag for child in element]
        assert tags == [
            "SHORT-NAME",
            "BASE-TYPE-SIZE",
            "BASE-TYPE-ENCODING",
            "MEM-ALIGNMENT",
            "BYTE-ORDER",
            "NATIVE-DECLARATION",
        ]


class TestBaseTypeDirectDefinitionWriter:
    """Per-attribute writer coverage of the flattened BASE-TYPE-DIRECT-DEFINITION group
    (Swc TPS Table 5.24, p.291): one field set, only its element is emitted."""

    def _write_definition(self, configure) -> ET.Element:
        base_type = SwBaseType(None, "u8")
        configure(base_type.getBaseTypeDefinition())
        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeSwBaseType(parent_element, base_type)
        return parent_element.find("SW-BASE-TYPE")

    def test_write_base_type_size_alone(self):
        element = self._write_definition(lambda d: d.setBaseTypeSize(PositiveInteger().setValue("16")))
        assert element.find("BASE-TYPE-SIZE").text == "16"
        assert element.find("BASE-TYPE-ENCODING") is None
        assert element.find("MEM-ALIGNMENT") is None
        assert element.find("BYTE-ORDER") is None
        assert element.find("NATIVE-DECLARATION") is None

    def test_write_base_type_encoding_alone(self):
        element = self._write_definition(lambda d: d.setBaseTypeEncoding(BaseTypeEncodingString().setValue("IEEE754")))
        assert element.find("BASE-TYPE-ENCODING").text == "IEEE754"
        assert element.find("BASE-TYPE-SIZE") is None
        assert element.find("MEM-ALIGNMENT") is None
        assert element.find("BYTE-ORDER") is None
        assert element.find("NATIVE-DECLARATION") is None

    def test_write_mem_alignment_alone(self):
        element = self._write_definition(lambda d: d.setMemAlignment(PositiveInteger().setValue("32")))
        assert element.find("MEM-ALIGNMENT").text == "32"
        assert element.find("BASE-TYPE-SIZE") is None
        assert element.find("BASE-TYPE-ENCODING") is None
        assert element.find("BYTE-ORDER") is None
        assert element.find("NATIVE-DECLARATION") is None

    def test_write_byte_order_alone_member_value_form(self):
        """The writer emits the XSD token form (BYTE_ORDER_XML_MAP) for the ByteOrderEnum member value."""
        element = self._write_definition(lambda d: d.setByteOrder(ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_LAST)))
        assert element.find("BYTE-ORDER").text == "MOST-SIGNIFICANT-BYTE-LAST"
        assert element.find("BASE-TYPE-SIZE") is None
        assert element.find("BASE-TYPE-ENCODING") is None
        assert element.find("MEM-ALIGNMENT") is None
        assert element.find("NATIVE-DECLARATION") is None

    def test_write_native_declaration_alone(self):
        element = self._write_definition(lambda d: d.setNativeDeclaration(NativeDeclarationString().setValue("unsigned short")))
        assert element.find("NATIVE-DECLARATION").text == "unsigned short"
        assert element.find("BASE-TYPE-SIZE") is None
        assert element.find("BASE-TYPE-ENCODING") is None
        assert element.find("MEM-ALIGNMENT") is None
        assert element.find("BYTE-ORDER") is None


class TestSwBaseTypeRoundTrip:
    def test_round_trip_populated(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("BaseTypes")
        base_type = pkg.createSwBaseType("uint8")
        definition = base_type.getBaseTypeDefinition()
        definition.setBaseTypeSize(PositiveInteger().setValue("8"))
        definition.setBaseTypeEncoding(BaseTypeEncodingString().setValue("IEEE754"))
        definition.setMemAlignment(PositiveInteger().setValue("8"))
        definition.setByteOrder(ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST))
        definition.setNativeDeclaration(NativeDeclarationString().setValue("unsigned char"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            loaded = document_2.getARPackages()[0].getSwBaseTypes()[0]
            assert loaded.getShortName() == "uint8"
            definition_2 = loaded.getBaseTypeDefinition()
            assert isinstance(definition_2, BaseTypeDirectDefinition)
            assert definition_2.getBaseTypeSize().getValue() == 8
            assert definition_2.getBaseTypeEncoding().getValue() == "IEEE754"
            assert definition_2.getMemAlignment().getValue() == 8
            assert definition_2.getByteOrder().getValue() == ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST
            assert definition_2.getNativeDeclaration().getValue() == "unsigned char"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty_element(self):
        """An SW-BASE-TYPE without definition children round-trips to all-None fields."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("BaseTypes")
        pkg.createSwBaseType("void")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            loaded = document_2.getARPackages()[0].getSwBaseTypes()[0]
            assert loaded.getShortName() == "void"
            definition_2 = loaded.getBaseTypeDefinition()
            assert isinstance(definition_2, BaseTypeDirectDefinition)
            assert definition_2.getBaseTypeSize() is None
            assert definition_2.getBaseTypeEncoding() is None
            assert definition_2.getMemAlignment() is None
            assert definition_2.getByteOrder() is None
            assert definition_2.getNativeDeclaration() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
