"""Reader/writer round-trip tests for the SwTextProps meta-class (Table D.72)."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, SwTextProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestSwTextPropsRoundTrip:
    def _build(self, document):
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("StringType")

        props = SwDataDefProps()
        sw_text_props = SwTextProps()
        sw_text_props.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE))
        sw_text_props.setBaseTypeRef(RefType().setDest("AUTOSAR/BaseTypes/uint8"))
        sw_text_props.setSwFillCharacter(Integer().setValue("0"))
        sw_text_props.setSwMaxTextSize(Integer().setValue("200"))
        props.setSwTextProps(sw_text_props)
        data_type.setSwDataDefProps(props)
        return data_type

    def test_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        self._build(document)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            sw_text_props_2 = data_type_2.getSwDataDefProps().getSwTextProps()
            assert sw_text_props_2 is not None
            assert sw_text_props_2.getArraySizeSemantics().getValue() == "fixedSize"
            assert sw_text_props_2.getBaseTypeRef().getDest() == "AUTOSAR/BaseTypes/uint8"
            assert sw_text_props_2.getSwFillCharacter().getValue() == 0
            assert sw_text_props_2.getSwMaxTextSize().getValue() == 200
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_no_sw_text_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        pkg.createApplicationPrimitiveDataType("StringType")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            assert data_type_2.getSwDataDefProps() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
