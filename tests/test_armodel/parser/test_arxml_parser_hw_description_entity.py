import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement
from armodel.parser.arxml_parser import ARXMLParser


class TestReadHwDescriptionEntity:
    def test_read_hw_element_attributes(self):
        xml_content = """
            <HW-ELEMENT>
              <SHORT-NAME>TestElement</SHORT-NAME>
              <HW-TYPE-REF DEST="HW-TYPE">/HwTypes/TestType</HW-TYPE-REF>
              <HW-CATEGORY-REFS>
                <HW-CATEGORY-REF DEST="HW-CATEGORY">/HwCategories/Cat1</HW-CATEGORY-REF>
                <HW-CATEGORY-REF DEST="HW-CATEGORY">/HwCategories/Cat2</HW-CATEGORY-REF>
              </HW-CATEGORY-REFS>
              <HW-ATTRIBUTE-VALUES>
                <HW-ATTRIBUTE-VALUE>
                  <HW-ATTRIBUTE-DEF-REF DEST="HW-ATTRIBUTE-DEF">/HwCategories/Cat1/AttrDef</HW-ATTRIBUTE-DEF-REF>
                </HW-ATTRIBUTE-VALUE>
              </HW-ATTRIBUTE-VALUES>
            </HW-ELEMENT>
        """
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        hw_element = HwElement(document, "TestElement")
        parser.readHwElement(element, hw_element)

        assert hw_element.getShortName() == "TestElement"
        assert hw_element.getHwTypeRef() is not None
        assert hw_element.getHwTypeRef().getValue() == "/HwTypes/TestType"
        assert hw_element.getHwTypeRef().getDest() == "HW-TYPE"

        category_refs = hw_element.getHwCategoryRefs()
        assert len(category_refs) == 2
        assert category_refs[0].getValue() == "/HwCategories/Cat1"
        assert category_refs[0].getDest() == "HW-CATEGORY"
        assert category_refs[1].getValue() == "/HwCategories/Cat2"

        attribute_values = hw_element.getHwAttributeValues()
        assert len(attribute_values) == 1
        assert attribute_values[0].getHwAttributeDefRef().getValue() == "/HwCategories/Cat1/AttrDef"

    def test_read_hw_element_empty_wrappers(self):
        xml_content = """
            <HW-ELEMENT>
              <SHORT-NAME>TestElement</SHORT-NAME>
            </HW-ELEMENT>
        """
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        hw_element = HwElement(document, "TestElement")
        parser.readHwElement(element, hw_element)

        assert hw_element.getHwTypeRef() is None
        assert hw_element.getHwCategoryRefs() == []
        assert hw_element.getHwAttributeValues() == []

    def test_read_hw_element_connections_and_nested(self):
        xml_content = """
            <HW-ELEMENT>
              <SHORT-NAME>TestElement</SHORT-NAME>
              <HW-ELEMENT-CONNECTIONS>
                <HW-ELEMENT-CONNECTOR>
                  <HW-ELEMENT-REF DEST="HW-ELEMENT">/Elements/ElemA</HW-ELEMENT-REF>
                  <HW-ELEMENT-REF DEST="HW-ELEMENT">/Elements/ElemB</HW-ELEMENT-REF>
                  <HW-PIN-CONNECTION>
                    <HW-PIN-REF DEST="HW-PIN">/Elements/ElemA/Pin1</HW-PIN-REF>
                  </HW-PIN-CONNECTION>
                  <HW-PIN-GROUP-CONNECTION>
                    <HW-PIN-GROUP-REF DEST="HW-PIN-GROUP">/Elements/ElemA/Group1</HW-PIN-GROUP-REF>
                  </HW-PIN-GROUP-CONNECTION>
                </HW-ELEMENT-CONNECTOR>
              </HW-ELEMENT-CONNECTIONS>
              <NESTED-ELEMENTS>
                <HW-ELEMENT-REF DEST="HW-ELEMENT">/Elements/ElemB</HW-ELEMENT-REF>
                <HW-ELEMENT-REF DEST="HW-ELEMENT">/Elements/ElemC</HW-ELEMENT-REF>
              </NESTED-ELEMENTS>
            </HW-ELEMENT>
        """
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        hw_element = HwElement(document, "TestElement")
        parser.readHwElement(element, hw_element)

        connections = hw_element.getHwElementConnections()
        assert len(connections) == 1
        hw_element_refs = connections[0].getHwElementRefs()
        assert len(hw_element_refs) == 2
        assert hw_element_refs[0].getValue() == "/Elements/ElemA"
        assert hw_element_refs[0].getDest() == "HW-ELEMENT"
        assert hw_element_refs[1].getValue() == "/Elements/ElemB"

        pin_connections = connections[0].getHwPinConnections()
        assert len(pin_connections) == 1
        assert len(pin_connections[0].getHwPinRefs()) == 1
        assert pin_connections[0].getHwPinRefs()[0].getValue() == "/Elements/ElemA/Pin1"

        pin_group_connections = connections[0].getHwPinGroupConnections()
        assert len(pin_group_connections) == 1
        assert len(pin_group_connections[0].getHwPinGroupRefs()) == 1
        assert pin_group_connections[0].getHwPinGroupRefs()[0].getValue() == "/Elements/ElemA/Group1"

        nested = hw_element.getNestedElementRefs()
        assert len(nested) == 2
        assert [ref.getValue() for ref in nested] == ["/Elements/ElemB", "/Elements/ElemC"]
        assert all(ref.getDest() == "HW-ELEMENT" for ref in nested)

    def test_read_hw_element_connector_refs(self):
        xml_content = """
            <HW-ELEMENT-CONNECTOR>
              <HW-ELEMENT-REF DEST="HW-ELEMENT">/Elements/ElemA</HW-ELEMENT-REF>
              <HW-ELEMENT-REF DEST="HW-ELEMENT">/Elements/ElemB</HW-ELEMENT-REF>
              <HW-PIN-CONNECTION>
                <HW-PIN-REF DEST="HW-PIN">/Elements/ElemA/Pin1</HW-PIN-REF>
              </HW-PIN-CONNECTION>
            </HW-ELEMENT-CONNECTOR>
        """
        element = ET.fromstring(xml_content)
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElementConnector

        connector = HwElementConnector()
        parser.readHwElementConnector(element, connector)

        assert len(connector.getHwElementRefs()) == 2
        assert connector.getHwElementRefs()[0].getValue() == "/Elements/ElemA"
        assert connector.getHwElementRefs()[1].getDest() == "HW-ELEMENT"
        assert len(connector.getHwPinConnections()) == 1
        assert connector.getHwPinConnections()[0].getHwPinRefs()[0].getValue() == "/Elements/ElemA/Pin1"
