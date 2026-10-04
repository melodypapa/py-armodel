"""Tests for reading and writing SwTextProps elements (Swc TPS Table 5.7, p.250).

The XSD group SW-TEXT-PROPS (AUTOSAR_00052.xsd) fixes the child element order:
ARRAY-SIZE-SEMANTICS, SW-MAX-TEXT-SIZE (sequenceOffset 20), BASE-TYPE-REF (30),
SW-FILL-CHARACTER (40).
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, SwTextProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_base_type_ref(value: str = "/DataTypes/BaseTypes/uint8") -> RefType:
    base_type_ref = RefType()
    base_type_ref.setValue(value)
    base_type_ref.setDest("SW-BASE-TYPE")
    return base_type_ref


def _build_text_props() -> SwTextProps:
    sw_text_props = SwTextProps()
    sw_text_props.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE))
    sw_text_props.setSwMaxTextSize(Integer().setValue("200"))
    sw_text_props.setBaseTypeRef(_build_base_type_ref())
    sw_text_props.setSwFillCharacter(Integer().setValue("48"))
    return sw_text_props


class TestWriteSwTextProps:
    def test_write_element_order_matches_xsd_group(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setSwTextProps(parent_element, _build_text_props())

        child_element = parent_element.find("SW-TEXT-PROPS")
        assert child_element is not None
        tags = [element.tag for element in child_element]
        assert tags == ["ARRAY-SIZE-SEMANTICS", "SW-MAX-TEXT-SIZE", "BASE-TYPE-REF", "SW-FILL-CHARACTER"]
        assert child_element.find("ARRAY-SIZE-SEMANTICS").text == "fixedSize"
        assert child_element.find("SW-MAX-TEXT-SIZE").text == "200"
        base_type_ref_element = child_element.find("BASE-TYPE-REF")
        assert base_type_ref_element.text == "/DataTypes/BaseTypes/uint8"
        assert base_type_ref_element.attrib["DEST"] == "SW-BASE-TYPE"
        assert child_element.find("SW-FILL-CHARACTER").text == "48"

    def test_write_unset_props_omits_element(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setSwTextProps(parent_element, None)
        assert parent_element.find("SW-TEXT-PROPS") is None


class TestSwTextPropsRoundTrip:
    def test_round_trip_populated(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("StringType")
        sw_data_def_props = SwDataDefProps()
        sw_data_def_props.setSwTextProps(_build_text_props())
        data_type.setSwDataDefProps(sw_data_def_props)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "SW-TEXT-PROPS" in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            props = data_type_2.getSwDataDefProps().getSwTextProps()
            assert props is not None
            assert props.getArraySizeSemantics().getValue() == "fixedSize"
            assert props.getSwMaxTextSize().getValue() == 200
            assert props.getBaseTypeRef().getValue() == "/DataTypes/BaseTypes/uint8"
            assert props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"
            assert props.getSwFillCharacter().getValue() == 48
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_without_sw_text_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("PlainType")
        data_type.setSwDataDefProps(SwDataDefProps())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "SW-TEXT-PROPS" not in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            assert data_type_2.getSwDataDefProps() is not None
            assert data_type_2.getSwDataDefProps().getSwTextProps() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
