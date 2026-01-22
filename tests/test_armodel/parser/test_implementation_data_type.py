from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.parser.arxml_parser import ARXMLParser
import xml.etree.ElementTree as ET


class TestImplementationDataTypeParser:

    def test_read_value_implementation_data_type(self):
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        xml_content = """
            <AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-3-0.xsd">
                <AR-PACKAGES T="2023-03-08T00:27:29+08:00" UUID="cb03ce49-8b4b-4565-abce-0a7a054d24af">
                    <AR-PACKAGE>
                        <SHORT-NAME>ImplementationDataType</SHORT-NAME>s
                        <ELEMENTS>
                            <IMPLEMENTATION-DATA-TYPE>
                                <SHORT-NAME>MyDataType</SHORT-NAME>
                                <CATEGORY>VALUE</CATEGORY>
                                <SW-DATA-DEF-PROPS T="2020-08-24T10:22:17+02:00">
                                    <SW-DATA-DEF-PROPS-VARIANTS>
                                    <SW-DATA-DEF-PROPS-CONDITIONAL T="2020-08-31T10:28:32+02:00">
                                        <BASE-TYPE-REF DEST="SW-BASE-TYPE">/AUTOSAR_Platform/BaseTypes/uint8</BASE-TYPE-REF>
                                        <COMPU-METHOD-REF DEST="COMPU-METHOD">/Application/ApplicationTypes/compu_Application_E_MyDataType</COMPU-METHOD-REF>
                                    </SW-DATA-DEF-PROPS-CONDITIONAL>
                                    </SW-DATA-DEF-PROPS-VARIANTS>
                                </SW-DATA-DEF-PROPS>
                            </IMPLEMENTATION-DATA-TYPE>
                        </ELEMENTS>
                    </AR-PACKAGE>
                </AR-PACKAGES>
            </AUTOSAR>
        """  # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)

        # read the XML content using the parser
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        # assert the ARPackages
        assert len(document.getARPackages()) == 1
        ar_package = document.getARPackages()[0]
        assert ar_package.getShortName() == "ImplementationDataType"

        # assert the ImplementationDataType
        assert len(ar_package.getImplementationDataTypes()) == 1
        data_type = ar_package.getImplementationDataTypes()[0]
        assert data_type.getShortName() == "MyDataType"
        assert str(data_type.getCategory()) == "VALUE"
        assert data_type.getCategory().getValue() == "VALUE"
        assert data_type.getSwDataDefProps() is not None
        assert data_type.getSwDataDefProps().getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert data_type.getSwDataDefProps().getBaseTypeRef().getValue() == "/AUTOSAR_Platform/BaseTypes/uint8"
        assert data_type.getSwDataDefProps().getCompuMethodRef().getDest() == "COMPU-METHOD"
        assert data_type.getSwDataDefProps().getCompuMethodRef().getValue() == "/Application/ApplicationTypes/compu_Application_E_MyDataType"

    def test_read_array_implementation_data_type(self):
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        xml_content = """
            <AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-3-0.xsd">
                <AR-PACKAGES T="2023-03-08T00:27:29+08:00" UUID="cb03ce49-8b4b-4565-abce-0a7a054d24af">
                    <AR-PACKAGE>
                        <SHORT-NAME>ImplementationDataType</SHORT-NAME>s
                        <ELEMENTS>
                            <IMPLEMENTATION-DATA-TYPE>
                                <SHORT-NAME>MyArrayDataType</SHORT-NAME>
                                <CATEGORY>ARRAY</CATEGORY>
                                <SW-DATA-DEF-PROPS>
                                    <SW-DATA-DEF-PROPS-VARIANTS>
                                    <SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-CONDITIONAL>
                                    </SW-DATA-DEF-PROPS-VARIANTS>
                                </SW-DATA-DEF-PROPS>
                                <SUB-ELEMENTS>
                                    <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="2264d081-8375-489d-bd02-b71b9d495a18">
                                    <SHORT-NAME>Byte</SHORT-NAME>
                                    <CATEGORY>VALUE</CATEGORY>
                                    <ARRAY-SIZE T="2021-03-26T19:19:25+01:00">8</ARRAY-SIZE>
                                    <ARRAY-SIZE-SEMANTICS>FIXED-SIZE</ARRAY-SIZE-SEMANTICS>
                                    <SW-DATA-DEF-PROPS>
                                        <SW-DATA-DEF-PROPS-VARIANTS>
                                            <SW-DATA-DEF-PROPS-CONDITIONAL T="2021-03-26T20:19:25+01:00">
                                                <BASE-TYPE-REF DEST="SW-BASE-TYPE">/AUTOSAR_Platform/BaseTypes/uint8</BASE-TYPE-REF>
                                            </SW-DATA-DEF-PROPS-CONDITIONAL>
                                        </SW-DATA-DEF-PROPS-VARIANTS>
                                    </SW-DATA-DEF-PROPS>
                                    </IMPLEMENTATION-DATA-TYPE-ELEMENT>
                                </SUB-ELEMENTS>
                            </IMPLEMENTATION-DATA-TYPE>
                        </ELEMENTS>
                    </AR-PACKAGE>
                </AR-PACKAGES>
            </AUTOSAR>
        """ # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)

        # read the XML content using the parser
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        # assert the ARPackages
        assert len(document.getARPackages()) == 1
        ar_package = document.getARPackages()[0]
        assert ar_package.getShortName() == "ImplementationDataType"

        # assert the ImplementationDataType
        assert len(ar_package.getImplementationDataTypes()) == 1
        data_type = ar_package.getImplementationDataTypes()[0]
        assert data_type.getShortName() == "MyArrayDataType"
        assert str(data_type.getCategory()) == "ARRAY"
        assert data_type.getCategory().getValue() == "ARRAY"
        assert data_type.getSwDataDefProps() is not None
        assert data_type.getSwDataDefProps().getBaseTypeRef() is None
        assert data_type.getSwDataDefProps().getCompuMethodRef() is None

        # assert the SubElements of ImplementationDataType
        assert len(data_type.getSubElements()) == 1
        sub_element = data_type.getSubElements()[0]
        assert sub_element.getShortName() == "Byte"
        assert str(sub_element.getCategory()) == "VALUE"
        assert sub_element.getCategory().getValue() == "VALUE"
        assert sub_element.getArraySize().getValue() == 8
        assert str(sub_element.getArraySizeSemantics()) == "FIXED-SIZE"
        assert sub_element.getArraySizeSemantics().getValue() == "FIXED-SIZE"
        assert sub_element.getSwDataDefProps() is not None
        assert sub_element.getSwDataDefProps().getBaseTypeRef() is not None
        assert sub_element.getSwDataDefProps().getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert sub_element.getSwDataDefProps().getBaseTypeRef().getValue() == "/AUTOSAR_Platform/BaseTypes/uint8"
        assert sub_element.getSwDataDefProps().getCompuMethodRef() is None

        # root = ET.Element("AUTOSAR", parser.nsmap)
        # writer = ARXMLWriter()
        # writer.writeARPackage(root, document)
        # xml_str = ET.tostring(root, encoding='utf-8')
        # assert xml_str == xml_content

    def test_structure_implementation_data_type(self):
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        xml_content = """
            <AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-3-0.xsd">
                <AR-PACKAGES T="2023-03-08T00:27:29+08:00" UUID="cb03ce49-8b4b-4565-abce-0a7a054d24af">
                    <AR-PACKAGE>
                        <SHORT-NAME>ImplementationDataType</SHORT-NAME>s
                        <ELEMENTS>
                            <IMPLEMENTATION-DATA-TYPE>
                                <SHORT-NAME>MyStructDataType</SHORT-NAME>
                                <CATEGORY>STRUCTURE</CATEGORY>
                                <SW-DATA-DEF-PROPS>
                                    <SW-DATA-DEF-PROPS-VARIANTS>
                                    <SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-CONDITIONAL>
                                    </SW-DATA-DEF-PROPS-VARIANTS>
                                </SW-DATA-DEF-PROPS>
                                <SUB-ELEMENTS>
                                    <IMPLEMENTATION-DATA-TYPE-ELEMENT T="2021-03-26T20:42:24+01:00" UUID="DCE:7700371a-cddc-4346-8b1e-749bddae5ed0">
                                        <SHORT-NAME>PayloadSize</SHORT-NAME>
                                        <CATEGORY>VALUE</CATEGORY>
                                        <SW-DATA-DEF-PROPS>
                                            <SW-DATA-DEF-PROPS-VARIANTS>
                                            <SW-DATA-DEF-PROPS-CONDITIONAL T="2021-03-26T19:16:35+01:00">
                                                <BASE-TYPE-REF DEST="SW-BASE-TYPE">/AUTOSAR_Platform/BaseTypes/uint8</BASE-TYPE-REF>
                                            </SW-DATA-DEF-PROPS-CONDITIONAL>
                                            </SW-DATA-DEF-PROPS-VARIANTS>
                                        </SW-DATA-DEF-PROPS>
                                    </IMPLEMENTATION-DATA-TYPE-ELEMENT>
                                    <IMPLEMENTATION-DATA-TYPE-ELEMENT T="2021-03-26T20:42:45+01:00">
                                        <SHORT-NAME>Payload</SHORT-NAME>
                                        <CATEGORY>TYPE_REFERENCE</CATEGORY>
                                        <SW-DATA-DEF-PROPS>
                                            <SW-DATA-DEF-PROPS-VARIANTS>
                                            <SW-DATA-DEF-PROPS-CONDITIONAL T="2021-03-26T19:25:45+01:00">
                                                <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/Application/ApplicationTypes/ArrayData</IMPLEMENTATION-DATA-TYPE-REF>
                                            </SW-DATA-DEF-PROPS-CONDITIONAL>
                                            </SW-DATA-DEF-PROPS-VARIANTS>
                                        </SW-DATA-DEF-PROPS>
                                    </IMPLEMENTATION-DATA-TYPE-ELEMENT>
                                </SUB-ELEMENTS>
                            </IMPLEMENTATION-DATA-TYPE>
                        </ELEMENTS>
                    </AR-PACKAGE>
                </AR-PACKAGES>
            </AUTOSAR>
        """ # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)

        # read the XML content using the parser
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        # assert the ARPackages
        assert len(document.getARPackages()) == 1
        ar_package = document.getARPackages()[0]
        assert ar_package.getShortName() == "ImplementationDataType"

        # assert the ImplementationDataType
        assert len(ar_package.getImplementationDataTypes()) == 1
        data_type = ar_package.getImplementationDataTypes()[0]
        assert data_type.getShortName() == "MyStructDataType"
        assert str(data_type.getCategory()) == "STRUCTURE"
        assert data_type.getCategory().getValue() == "STRUCTURE"
        assert data_type.getSwDataDefProps() is not None
        assert data_type.getSwDataDefProps().getBaseTypeRef() is None
        assert data_type.getSwDataDefProps().getCompuMethodRef() is None

        # assert the SubElements of ImplementationDataType
        assert len(data_type.getSubElements()) == 2

        # assert the first sub element
        sub_element1 = data_type.getSubElements()[0]
        assert sub_element1.getShortName() == "PayloadSize"
        assert str(sub_element1.getCategory()) == "VALUE"
        assert sub_element1.getCategory().getValue() == "VALUE"
        assert sub_element1.getSwDataDefProps() is not None
        assert sub_element1.getSwDataDefProps().getBaseTypeRef() is not None
        assert sub_element1.getSwDataDefProps().getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert sub_element1.getSwDataDefProps().getBaseTypeRef().getValue() == "/AUTOSAR_Platform/BaseTypes/uint8"
        assert sub_element1.getSwDataDefProps().getCompuMethodRef() is None
        assert sub_element1.getArraySize() is None
        assert sub_element1.getArraySizeSemantics() is None
        assert sub_element1.getArraySizeHandling() is None
        assert sub_element1.getIsOptional() is None
        assert sub_element1.getSwDataDefProps().getCompuMethodRef() is None
        
        # assert the second sub element
        sub_element2 = data_type.getSubElements()[1]
        assert sub_element2.getShortName() == "Payload"
        assert str(sub_element2.getCategory()) == "TYPE_REFERENCE"
        assert sub_element2.getCategory().getValue() == "TYPE_REFERENCE"
        assert sub_element2.getSwDataDefProps() is not None
        assert sub_element2.getSwDataDefProps().getBaseTypeRef() is None
        assert sub_element2.getSwDataDefProps().getImplementationDataTypeRef() is not None
        assert sub_element2.getSwDataDefProps().getImplementationDataTypeRef().getDest() == "IMPLEMENTATION-DATA-TYPE"
        assert sub_element2.getSwDataDefProps().getImplementationDataTypeRef().getValue() == "/Application/ApplicationTypes/ArrayData"
        assert sub_element2.getSwDataDefProps().getCompuMethodRef() is None
        assert sub_element2.getArraySize() is None
        assert sub_element2.getArraySizeSemantics() is None
        assert sub_element2.getArraySizeHandling() is None
        assert sub_element2.getIsOptional() is None
        assert sub_element2.getSwDataDefProps().getCompuMethodRef() is None
        
