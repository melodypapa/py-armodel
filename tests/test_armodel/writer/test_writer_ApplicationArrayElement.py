"""Tests for reading and writing ApplicationArrayElement (Swc TPS Table 5.9, p.252).

The XSD group APPLICATION-ARRAY-ELEMENT (AUTOSAR_00052.xsd, L2846) fixes the
child element order: ARRAY-SIZE-HANDLING, ARRAY-SIZE-SEMANTICS,
INDEX-DATA-TYPE-REF, MAX-NUMBER-OF-ELEMENTS (after the inherited
APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE group's TYPE-TREF). ARPackage
dispatch (reader branch APPLICATION-ARRAY-DATA-TYPE / writer isinstance branch)
is exercised through the save-reload round-trip.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType, ArraySizeHandlingEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_array_element(data_type: ApplicationArrayDataType):
    array_element = data_type.createApplicationArrayElement("Elem")
    type_tref = TRefType()
    type_tref.setValue("/DataTypes/uint8")
    type_tref.setDest("APPLICATION-PRIMITIVE-DATA-TYPE")
    array_element.setTypeTRef(type_tref)
    array_element.setArraySizeHandling(ArraySizeHandlingEnum().setValue(ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE))
    array_element.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.VARIABLE_SIZE))
    index_ref = RefType()
    index_ref.setValue("/DataTypes/IndexType")
    index_ref.setDest("APPLICATION-PRIMITIVE-DATA-TYPE")
    array_element.setIndexDataTypeRef(index_ref)
    array_element.setMaxNumberOfElements(PositiveInteger().setValue("4"))
    return array_element


class TestWriteApplicationArrayElement:
    def test_write_element_order_matches_xsd_group(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        data_type = ApplicationArrayDataType(document, "ArrayType")
        _build_array_element(data_type)

        parent_element = ET.Element("ELEMENTS")
        ARXMLWriter().setApplicationArrayElement(parent_element, data_type.getApplicationArrayElement())

        child_element = parent_element.find("ELEMENT")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags.index("TYPE-TREF") < tags.index("ARRAY-SIZE-HANDLING")
        assert tags.index("ARRAY-SIZE-HANDLING") < tags.index("ARRAY-SIZE-SEMANTICS")
        assert tags.index("ARRAY-SIZE-SEMANTICS") < tags.index("INDEX-DATA-TYPE-REF")
        assert tags.index("INDEX-DATA-TYPE-REF") < tags.index("MAX-NUMBER-OF-ELEMENTS")
        assert child_element.find("TYPE-TREF").text == "/DataTypes/uint8"
        assert child_element.find("TYPE-TREF").attrib["DEST"] == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert child_element.find("ARRAY-SIZE-HANDLING").text == "allIndicesSameArraySize"
        assert child_element.find("ARRAY-SIZE-SEMANTICS").text == "variableSize"
        assert child_element.find("INDEX-DATA-TYPE-REF").text == "/DataTypes/IndexType"
        assert child_element.find("INDEX-DATA-TYPE-REF").attrib["DEST"] == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert child_element.find("MAX-NUMBER-OF-ELEMENTS").text == "4"

    def test_write_unset_fields_omit_elements(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        data_type = ApplicationArrayDataType(document, "ArrayType")
        data_type.createApplicationArrayElement("Elem")

        parent_element = ET.Element("ELEMENTS")
        ARXMLWriter().setApplicationArrayElement(parent_element, data_type.getApplicationArrayElement())

        child_element = parent_element.find("ELEMENT")
        assert child_element is not None
        assert child_element.find("TYPE-TREF") is None
        assert child_element.find("ARRAY-SIZE-HANDLING") is None
        assert child_element.find("ARRAY-SIZE-SEMANTICS") is None
        assert child_element.find("INDEX-DATA-TYPE-REF") is None
        assert child_element.find("MAX-NUMBER-OF-ELEMENTS") is None


class TestApplicationArrayElementRoundTrip:
    def test_round_trip_populated(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        data_type = pkg.createApplicationArrayDataType("ArrayType")
        _build_array_element(data_type)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "APPLICATION-ARRAY-DATA-TYPE" in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_types = document_2.getARPackages()[0].getApplicationArrayDataTypes()
            assert len(data_types) == 1
            data_type_2 = data_types[0]

            array_element = data_type_2.getApplicationArrayElement()
            assert array_element is not None
            assert array_element.short_name == "Elem"
            assert array_element.getTypeTRef().getValue() == "/DataTypes/uint8"
            assert array_element.getTypeTRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
            assert array_element.getArraySizeHandling().getValue() == "allIndicesSameArraySize"
            assert array_element.getArraySizeSemantics().getValue() == "variableSize"
            assert array_element.getIndexDataTypeRef().getValue() == "/DataTypes/IndexType"
            assert array_element.getIndexDataTypeRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
            assert isinstance(array_element.getMaxNumberOfElements(), PositiveInteger)
            assert array_element.getMaxNumberOfElements().getValue() == 4
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_without_optional_fields(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        data_type = pkg.createApplicationArrayDataType("PlainArrayType")
        data_type.createApplicationArrayElement("Elem")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_types = document_2.getARPackages()[0].getApplicationArrayDataTypes()
            assert len(data_types) == 1
            array_element = data_types[0].getApplicationArrayElement()
            assert array_element is not None
            assert array_element.short_name == "Elem"
            assert array_element.getTypeTRef() is None
            assert array_element.getArraySizeHandling() is None
            assert array_element.getArraySizeSemantics() is None
            assert array_element.getIndexDataTypeRef() is None
            assert array_element.getMaxNumberOfElements() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
