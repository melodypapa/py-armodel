"""Reader round-trip tests for ApplicationDeferredDataType (R23-11 Table 3.17)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationDeferredDataType
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.parser.arxml_parser import ARXMLParser


class TestApplicationDeferredDataTypeParser:

    def test_read_application_deferred_data_type(self):
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        xml_content = """
            <AUTOSAR xmlns="http://autosar.org/schema/r4.0">
                <AR-PACKAGES>
                    <AR-PACKAGE>
                        <SHORT-NAME>AppPkg</SHORT-NAME>
                        <ELEMENTS>
                            <APPLICATION-DEFERRED-DATA-TYPE>
                                <SHORT-NAME>MyDeferred</SHORT-NAME>
                            </APPLICATION-DEFERRED-DATA-TYPE>
                        </ELEMENTS>
                    </AR-PACKAGE>
                </AR-PACKAGES>
            </AUTOSAR>
        """
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        ar_package = document.getARPackages()[0]
        data_type = ar_package.getElement("MyDeferred", ApplicationDeferredDataType)
        assert data_type is not None
        assert isinstance(data_type, ApplicationDeferredDataType)
        assert data_type.getShortName() == "MyDeferred"

    def test_read_application_deferred_data_type_with_uuid(self):
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        xml_content = """
            <AUTOSAR xmlns="http://autosar.org/schema/r4.0">
                <AR-PACKAGES>
                    <AR-PACKAGE>
                        <SHORT-NAME>AppPkg</SHORT-NAME>
                        <ELEMENTS>
                            <APPLICATION-DEFERRED-DATA-TYPE UUID="DCE:f73f677c-1389-4425-83f8-921d567b2ad4">
                                <SHORT-NAME>MyDeferred</SHORT-NAME>
                            </APPLICATION-DEFERRED-DATA-TYPE>
                        </ELEMENTS>
                    </AR-PACKAGE>
                </AR-PACKAGES>
            </AUTOSAR>
        """
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        ar_package = document.getARPackages()[0]
        data_type = ar_package.getElement("MyDeferred", ApplicationDeferredDataType)
        assert data_type is not None
        assert data_type.getUuid().getValue() == "DCE:f73f677c-1389-4425-83f8-921d567b2ad4"

    def test_round_trip_application_deferred_data_type(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.writer.arxml_writer import ARXMLWriter

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AppPkg")
        data_type = pkg.createApplicationDeferredDataType("MyDeferred")
        assert isinstance(data_type, ApplicationDeferredDataType)

        import os
        import tempfile

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            reparsed = AUTOSAR.getInstance()
            ARXMLParser().load(file_path, reparsed)
            re_data_type = reparsed.getARPackages()[0].getElement("MyDeferred", ApplicationDeferredDataType)
            assert re_data_type is not None
            assert isinstance(re_data_type, ApplicationDeferredDataType)
            assert re_data_type.getShortName() == "MyDeferred"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
