"""Reader tests for the BaseType aggregation inside SW-BASE-TYPE (Swc TPS Table 5.26, p.292).

The XSD group BASE-TYPE (AUTOSAR_00052.xsd line 8384) embeds a 0..1 choice of the
BASE-TYPE-DIRECT-DEFINITION group inline (role/type/wrapper element flags all false):
BASE-TYPE-SIZE (70), BASE-TYPE-ENCODING (90), MEM-ALIGNMENT (100), BYTE-ORDER (110),
NATIVE-DECLARATION (120). MAX-BASE-TYPE-SIZE (80) is atp.Status="removed" and is not
modeled. The aggregation is flattened - no wrapper element exists in the XML.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ByteOrderEnum
from armodel.models.M2.MSR.AsamHdo.BaseTypes import BaseTypeDirectDefinition
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestBaseTypeReader:
    def test_read_base_type_definition_field_values(self, parser):
        root = _snip("""
            <SW-BASE-TYPE>
                <SHORT-NAME>uint8</SHORT-NAME>
                <BASE-TYPE-SIZE>8</BASE-TYPE-SIZE>
                <BASE-TYPE-ENCODING>IEEE754</BASE-TYPE-ENCODING>
                <MEM-ALIGNMENT>8</MEM-ALIGNMENT>
                <BYTE-ORDER>MOST-SIGNIFICANT-BYTE-FIRST</BYTE-ORDER>
                <NATIVE-DECLARATION>unsigned char</NATIVE-DECLARATION>
            </SW-BASE-TYPE>
            """)
        pkg = _autosar_root().createARPackage("TestPkg")
        data_type = pkg.createSwBaseType("uint8")

        parser.readSwBaseType(parser.find(root, "SW-BASE-TYPE"), data_type)

        assert data_type.getShortName() == "uint8"
        definition = data_type.getBaseTypeDefinition()
        assert isinstance(definition, BaseTypeDirectDefinition)
        assert definition.getBaseTypeSize().getValue() == 8
        assert definition.getBaseTypeEncoding().getValue() == "IEEE754"
        assert definition.getMemAlignment().getValue() == 8
        assert definition.getByteOrder().getValue() == "mostSignificantByteFirst"
        assert definition.getNativeDeclaration().getValue() == "unsigned char"

    def test_read_empty_base_type_yields_unset_definition(self, parser):
        root = _snip("<SW-BASE-TYPE><SHORT-NAME>void</SHORT-NAME></SW-BASE-TYPE>")
        pkg = _autosar_root().createARPackage("TestPkg")
        data_type = pkg.createSwBaseType("void")

        parser.readSwBaseType(parser.find(root, "SW-BASE-TYPE"), data_type)

        definition = data_type.getBaseTypeDefinition()
        assert isinstance(definition, BaseTypeDirectDefinition)
        assert definition.getBaseTypeSize() is None
        assert definition.getBaseTypeEncoding() is None
        assert definition.getMemAlignment() is None
        assert definition.getByteOrder() is None
        assert definition.getNativeDeclaration() is None


class TestBaseTypeDirectDefinitionReader:
    """Per-attribute reader coverage of the flattened BASE-TYPE-DIRECT-DEFINITION group
    (Swc TPS Table 5.24, p.291): one element present, the other four stay unset."""

    def _read_definition(self, parser, inner: str) -> BaseTypeDirectDefinition:
        root = _snip("<SW-BASE-TYPE><SHORT-NAME>u8</SHORT-NAME>%s</SW-BASE-TYPE>" % inner)
        pkg = _autosar_root().createARPackage("TestPkg")
        data_type = pkg.createSwBaseType("u8")

        parser.readSwBaseType(parser.find(root, "SW-BASE-TYPE"), data_type)

        return data_type.getBaseTypeDefinition()

    def test_read_base_type_size_alone(self, parser):
        definition = self._read_definition(parser, "<BASE-TYPE-SIZE>16</BASE-TYPE-SIZE>")
        assert definition.getBaseTypeSize().getValue() == 16
        assert definition.getBaseTypeEncoding() is None
        assert definition.getMemAlignment() is None
        assert definition.getByteOrder() is None
        assert definition.getNativeDeclaration() is None

    def test_read_base_type_encoding_alone(self, parser):
        definition = self._read_definition(parser, "<BASE-TYPE-ENCODING>IEEE754</BASE-TYPE-ENCODING>")
        assert definition.getBaseTypeEncoding().getValue() == "IEEE754"
        assert definition.getBaseTypeSize() is None
        assert definition.getMemAlignment() is None
        assert definition.getByteOrder() is None
        assert definition.getNativeDeclaration() is None

    def test_read_mem_alignment_alone(self, parser):
        definition = self._read_definition(parser, "<MEM-ALIGNMENT>32</MEM-ALIGNMENT>")
        assert definition.getMemAlignment().getValue() == 32
        assert definition.getBaseTypeSize() is None
        assert definition.getBaseTypeEncoding() is None
        assert definition.getByteOrder() is None
        assert definition.getNativeDeclaration() is None

    def test_read_byte_order_alone_xsd_value_form(self, parser):
        """The XSD serializes BYTE-ORDER in the UPPERCASE literal form; the reader maps it to the ByteOrderEnum member via BYTE_ORDER_XML_MAP."""
        definition = self._read_definition(parser, "<BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</BYTE-ORDER>")
        assert isinstance(definition.getByteOrder(), ByteOrderEnum)
        assert definition.getByteOrder().getValue() == "mostSignificantByteLast"
        assert definition.getBaseTypeSize() is None
        assert definition.getBaseTypeEncoding() is None
        assert definition.getMemAlignment() is None
        assert definition.getNativeDeclaration() is None

    def test_read_native_declaration_alone(self, parser):
        definition = self._read_definition(parser, "<NATIVE-DECLARATION>unsigned short</NATIVE-DECLARATION>")
        assert definition.getNativeDeclaration().getValue() == "unsigned short"
        assert definition.getBaseTypeSize() is None
        assert definition.getBaseTypeEncoding() is None
        assert definition.getMemAlignment() is None
        assert definition.getByteOrder() is None
