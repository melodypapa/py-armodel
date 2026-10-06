"""Tests for reading and writing ApplicationArrayDataType elements (Swc TPS Table 5.8, p.252).

The XSD group APPLICATION-ARRAY-DATA-TYPE (AUTOSAR_00052.xsd) fixes the child
element order: DYNAMIC-ARRAY-SIZE-PROFILE, then ELEMENT. ARPackage dispatch
(reader branch APPLICATION-ARRAY-DATA-TYPE / writer isinstance branch) is
exercised through the save-reload round-trip.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_array_data_type() -> ApplicationArrayDataType:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Pkg")
    data_type = pkg.createApplicationArrayDataType("ArrayType")
    data_type.setDynamicArraySizeProfile(String().setValue("VARIABLE-LENGTH"))

    array_element = data_type.createApplicationArrayElement("Elem")
    type_tref = TRefType()
    type_tref.setValue("/DataTypes/uint8")
    type_tref.setDest("APPLICATION-PRIMITIVE-DATA-TYPE")
    array_element.setTypeTRef(type_tref)
    array_element.setMaxNumberOfElements(PositiveInteger().setValue("4"))
    return data_type


class TestWriteApplicationArrayDataType:
    def test_write_element_order_matches_xsd_group(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        data_type = ApplicationArrayDataType(document, "ArrayType")
        data_type.setDynamicArraySizeProfile(String().setValue("VARIABLE-LENGTH"))
        data_type.createApplicationArrayElement("Elem")

        parent_element = ET.Element("ELEMENTS")
        ARXMLWriter().writeApplicationArrayDataType(parent_element, data_type)

        child_element = parent_element.find("APPLICATION-ARRAY-DATA-TYPE")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags.index("DYNAMIC-ARRAY-SIZE-PROFILE") < tags.index("ELEMENT")
        assert child_element.find("DYNAMIC-ARRAY-SIZE-PROFILE").text == "VARIABLE-LENGTH"
        element_element = child_element.find("ELEMENT")
        assert element_element.find("SHORT-NAME").text == "Elem"

    def test_write_unset_fields_omit_elements(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        data_type = ApplicationArrayDataType(document, "ArrayType")

        parent_element = ET.Element("ELEMENTS")
        ARXMLWriter().writeApplicationArrayDataType(parent_element, data_type)

        child_element = parent_element.find("APPLICATION-ARRAY-DATA-TYPE")
        assert child_element is not None
        assert child_element.find("DYNAMIC-ARRAY-SIZE-PROFILE") is None
        assert child_element.find("ELEMENT") is None


class TestApplicationArrayDataTypeRoundTrip:
    def test_round_trip_populated(self):
        _build_array_data_type()
        document = AUTOSAR.getInstance()

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
            assert isinstance(data_type_2, ApplicationArrayDataType)
            assert data_type_2.short_name == "ArrayType"
            assert data_type_2.getDynamicArraySizeProfile().getValue() == "VARIABLE-LENGTH"

            array_element = data_type_2.getApplicationArrayElement()
            assert array_element is not None
            assert array_element.short_name == "Elem"
            assert array_element.getTypeTRef().getValue() == "/DataTypes/uint8"
            assert array_element.getTypeTRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
            assert array_element.getMaxNumberOfElements().getValue() == 4
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_without_optional_fields(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        pkg.createApplicationArrayDataType("PlainArrayType")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "APPLICATION-ARRAY-DATA-TYPE" in xml
            assert "DYNAMIC-ARRAY-SIZE-PROFILE" not in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_types = document_2.getARPackages()[0].getApplicationArrayDataTypes()
            assert len(data_types) == 1
            assert data_types[0].short_name == "PlainArrayType"
            assert data_types[0].getDynamicArraySizeProfile() is None
            assert data_types[0].getApplicationArrayElement() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
