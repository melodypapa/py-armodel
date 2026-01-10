
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.parser.arxml_parser import ARXMLParser
import xml.etree.ElementTree as ET


class TestARXMLParser:
    def test_convert_find_key(self):
        parser = ARXMLParser()
        assert (parser.convert_find_key("ELEMENTS") == "xmlns:ELEMENTS")
        assert (parser.convert_find_key("ELEMENTS/*") == "xmlns:ELEMENTS/*")
        assert (parser.convert_find_key("./ELEMENTS") == "./xmlns:ELEMENTS")
        assert (parser.convert_find_key("./ELEMENTS/*") == "./xmlns:ELEMENTS/*")
        assert (parser.convert_find_key("A/B") == "xmlns:A/xmlns:B")
        assert (parser.convert_find_key("A/B/*") == "xmlns:A/xmlns:B/*")
        assert (parser.convert_find_key("./A/B") == "./xmlns:A/xmlns:B")
        assert (parser.convert_find_key("./A/B/*") == "./xmlns:A/xmlns:B/*")

    def test_read_ar_packages(self):
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        xml_content = """
            <AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-3-0.xsd">
                <AR-PACKAGES T="2023-03-08T00:27:29+08:00" UUID="cb03ce49-8b4b-4565-abce-0a7a054d24af">
                    <AR-PACKAGE>
                        <SHORT-NAME>ApplicationTypes</SHORT-NAME>s
                        <ELEMENTS>
                            <IMPLEMENTATION-DATA-TYPE>
                                <SHORT-NAME>MyDataType</SHORT-NAME>
                            </IMPLEMENTATION-DATA-TYPE>
                        </ELEMENTS>
                    </AR-PACKAGE>
                    <AR-PACKAGE>
                        <SHORT-NAME>MyPackage</SHORT-NAME>
                        <ELEMENTS>
                            <IMPLEMENTATION-DATA-TYPE>
                                <SHORT-NAME>MyDataType2</SHORT-NAME>
                            </IMPLEMENTATION-DATA-TYPE>
                        </ELEMENTS>
                    </AR-PACKAGE>
                </AR-PACKAGES>
            </AUTOSAR>
        """ # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)

        document = AUTOSARDoc()
        parser.readARPackages(element, document)
        assert len(document.getARPackages()) == 2
        assert document.getARPackages()[0].getShortName() == "ApplicationTypes"
        assert document.getARPackages()[1].getShortName() == "MyPackage"
