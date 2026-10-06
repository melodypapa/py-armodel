"""Tests for reading and writing ImplementationDataType elements (Swc TPS Table 5.15, p.268).

The XSD group IMPLEMENTATION-DATA-TYPE (AUTOSAR_00052.xsd) fixes the child
element order: DYNAMIC-ARRAY-SIZE-PROFILE, IS-STRUCT-WITH-OPTIONAL-ELEMENT,
SUB-ELEMENTS, SYMBOL-PROPS, TYPE-EMITTER. ARPackage dispatch (reader branch
IMPLEMENTATION-DATA-TYPE / writer isinstance branch) is exercised through the
save-reload round-trip.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum, ImplementationDataType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, CIdentifier, NameToken, PositiveInteger, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_implementation_data_type() -> ImplementationDataType:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Pkg")
    data_type = pkg.createImplementationDataType("StructType")
    data_type.setDynamicArraySizeProfile(String().setValue("VARIABLE-LENGTH"))
    data_type.setIsStructWithOptionalElement(Boolean().setValue(True))

    size_element = data_type.createImplementationDataTypeElement("Size")
    size_element.setArraySize(PositiveInteger().setValue("8"))
    size_element.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE))

    data_type.createImplementationDataTypeElement("Payload")

    symbol_props = data_type.createSymbolProps("Sym")
    symbol_props.setSymbol(CIdentifier().setValue("REASON_SYM"))

    data_type.setTypeEmitter(NameToken().setValue("RTE"))
    return data_type


class TestWriteImplementationDataType:
    def test_write_element_order_matches_xsd_group(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        data_type = ImplementationDataType(document, "StructType")
        data_type.setDynamicArraySizeProfile(String().setValue("VARIABLE-LENGTH"))
        data_type.setIsStructWithOptionalElement(Boolean().setValue(True))
        data_type.createImplementationDataTypeElement("Size")
        symbol_props = data_type.createSymbolProps("Sym")
        symbol_props.setSymbol(CIdentifier().setValue("REASON_SYM"))
        data_type.setTypeEmitter(NameToken().setValue("RTE"))

        parent_element = ET.Element("ELEMENTS")
        ARXMLWriter().writeImplementationDataType(parent_element, data_type)

        child_element = parent_element.find("IMPLEMENTATION-DATA-TYPE")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags.index("DYNAMIC-ARRAY-SIZE-PROFILE") < tags.index("IS-STRUCT-WITH-OPTIONAL-ELEMENT")
        assert tags.index("IS-STRUCT-WITH-OPTIONAL-ELEMENT") < tags.index("SUB-ELEMENTS")
        assert tags.index("SUB-ELEMENTS") < tags.index("SYMBOL-PROPS")
        assert tags.index("SYMBOL-PROPS") < tags.index("TYPE-EMITTER")
        assert child_element.find("DYNAMIC-ARRAY-SIZE-PROFILE").text == "VARIABLE-LENGTH"
        assert child_element.find("TYPE-EMITTER").text == "RTE"

    def test_write_unset_fields_omit_elements(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        data_type = ImplementationDataType(document, "PlainType")

        parent_element = ET.Element("ELEMENTS")
        ARXMLWriter().writeImplementationDataType(parent_element, data_type)

        child_element = parent_element.find("IMPLEMENTATION-DATA-TYPE")
        assert child_element is not None
        assert child_element.find("DYNAMIC-ARRAY-SIZE-PROFILE") is None
        assert child_element.find("IS-STRUCT-WITH-OPTIONAL-ELEMENT") is None
        assert child_element.find("SUB-ELEMENTS") is None
        assert child_element.find("SYMBOL-PROPS") is None
        assert child_element.find("TYPE-EMITTER") is None


class TestImplementationDataTypeRoundTrip:
    def test_round_trip_populated(self):
        _build_implementation_data_type()
        document = AUTOSAR.getInstance()

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "IMPLEMENTATION-DATA-TYPE" in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_types = document_2.getARPackages()[0].getImplementationDataTypes()
            assert len(data_types) == 1
            data_type_2 = data_types[0]
            assert isinstance(data_type_2, ImplementationDataType)
            assert data_type_2.short_name == "StructType"
            assert data_type_2.getDynamicArraySizeProfile().getValue() == "VARIABLE-LENGTH"
            assert data_type_2.getIsStructWithOptionalElement().getValue() is True

            sub_elements = data_type_2.getSubElements()
            assert len(sub_elements) == 2
            assert sub_elements[0].short_name == "Size"
            assert sub_elements[0].getArraySize().getValue() == 8
            assert sub_elements[0].getArraySizeSemantics().getValue() == ArraySizeSemanticsEnum.FIXED_SIZE
            assert sub_elements[1].short_name == "Payload"

            symbol_props = data_type_2.getSymbolProps()
            assert symbol_props is not None
            assert symbol_props.short_name == "Sym"
            assert symbol_props.getSymbol().getValue() == "REASON_SYM"

            assert data_type_2.getTypeEmitter().getValue() == "RTE"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_without_optional_fields(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        pkg.createImplementationDataType("PlainType")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "IMPLEMENTATION-DATA-TYPE" in xml
            assert "SUB-ELEMENTS" not in xml
            assert "SYMBOL-PROPS" not in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_types = document_2.getARPackages()[0].getImplementationDataTypes()
            assert len(data_types) == 1
            assert data_types[0].short_name == "PlainType"
            assert data_types[0].getDynamicArraySizeProfile() is None
            assert data_types[0].getIsStructWithOptionalElement() is None
            assert data_types[0].getSubElements() == []
            assert data_types[0].getSymbolProps() is None
            assert data_types[0].getTypeEmitter() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
