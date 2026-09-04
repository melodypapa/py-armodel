"""Reader/writer round-trip tests for AutosarDataType (Table 5.1, p.232).

AutosarDataType is abstract, so its swDataDefProps aggregation is exercised through
the concrete subclass ApplicationPrimitiveDataType. readAutosarDataType (parser) and
writeAutosarDataType (writer) own the SW-DATA-DEF-PROPS serialization.
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestAutosarDataTypeSwDataDefPropsRoundTrip:
    def test_round_trip_with_sw_data_def_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("MyType")
        data_type.setSwDataDefProps(SwDataDefProps())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "SW-DATA-DEF-PROPS" in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            assert data_type_2.getShortName() == "MyType"
            assert data_type_2.getSwDataDefProps() is not None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_without_sw_data_def_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        pkg.createApplicationPrimitiveDataType("MyType")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "SW-DATA-DEF-PROPS" not in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            assert data_type_2.getSwDataDefProps() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
