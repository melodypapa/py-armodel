import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPin
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestHwPinParserWriter:
    def test_read_hw_pin_with_function_names(self):
        """Test reading HwPin with multiple function names"""
        parser = ARXMLParser()
        xml_content = """<HW-PIN xmlns="http://autosar.org/schema/r4.0">
                <SHORT-NAME>TestPin</SHORT-NAME>
                <FUNCTION-NAMES>
                    <FUNCTION-NAME>CAN_TX</FUNCTION-NAME>
                    <FUNCTION-NAME>CAN_RX</FUNCTION-NAME>
                </FUNCTION-NAMES>
                <PACKAGING-PIN-NAME>A03</PACKAGING-PIN-NAME>
                <PIN-NUMBER>42</PIN-NUMBER>
            </HW-PIN>
        """
        element = ET.fromstring(xml_content)
        hw_pin = HwPin(None, "TestPin")
        parser.readHwPin(element, hw_pin)

        assert hw_pin.getShortName() == "TestPin"
        function_names = hw_pin.getFunctionNames()
        assert len(function_names) == 2
        assert "CAN_TX" in function_names
        assert "CAN_RX" in function_names
        assert hw_pin.getPackagingPinName() == "A03"
        assert hw_pin.getPinNumber().getValue() == 42

    def test_read_hw_pin_without_function_names(self):
        """Test reading HwPin without function names"""
        parser = ARXMLParser()
        xml_content = """<HW-PIN xmlns="http://autosar.org/schema/r4.0">
                <SHORT-NAME>SimplePin</SHORT-NAME>
            </HW-PIN>
        """
        element = ET.fromstring(xml_content)
        hw_pin = HwPin(None, "SimplePin")
        parser.readHwPin(element, hw_pin)

        assert hw_pin.getShortName() == "SimplePin"
        assert len(hw_pin.getFunctionNames()) == 0
        assert hw_pin.getPackagingPinName() is None
        assert hw_pin.getPinNumber() is None

    def test_write_hw_pin_with_function_names(self):
        """Test writing HwPin with multiple function names"""
        hw_pin = HwPin(None, "TestPin")
        hw_pin.addFunctionName("CAN_TX")
        hw_pin.addFunctionName("CAN_RX")
        hw_pin.setPackagingPinName("A03")
        hw_pin.setPinNumber(Integer().setValue("42"))

        writer = ARXMLWriter()
        root = ET.Element("ROOT")
        writer.writeHwPin(root, hw_pin)

        hw_pin_element = root.find("HW-PIN")
        assert hw_pin_element is not None

        short_name = hw_pin_element.find("SHORT-NAME")
        assert short_name is not None
        assert short_name.text == "TestPin"

        function_names_element = hw_pin_element.find("FUNCTION-NAMES")
        assert function_names_element is not None

        function_name_elements = function_names_element.findall("FUNCTION-NAME")
        assert len(function_name_elements) == 2
        assert function_name_elements[0].text == "CAN_TX"
        assert function_name_elements[1].text == "CAN_RX"

        packaging_pin_name = hw_pin_element.find("PACKAGING-PIN-NAME")
        assert packaging_pin_name is not None
        assert packaging_pin_name.text == "A03"

        pin_number = hw_pin_element.find("PIN-NUMBER")
        assert pin_number is not None
        assert pin_number.text == "42"

    def test_hw_pin_round_trip_with_namespace(self):
        """Test HwPin round-trip with proper AUTOSAR namespace"""
        hw_pin_original = HwPin(None, "RoundTripPin")
        hw_pin_original.addFunctionName("GPIO_OUTPUT")
        hw_pin_original.addFunctionName("GPIO_INPUT")
        hw_pin_original.setPackagingPinName("B05")
        hw_pin_original.setPinNumber(Integer().setValue("99"))

        parser = ARXMLParser()
        xml_content = """<HW-PIN xmlns="http://autosar.org/schema/r4.0">
                <SHORT-NAME>RoundTripPin</SHORT-NAME>
                <FUNCTION-NAMES>
                    <FUNCTION-NAME>GPIO_OUTPUT</FUNCTION-NAME>
                    <FUNCTION-NAME>GPIO_INPUT</FUNCTION-NAME>
                </FUNCTION-NAMES>
                <PACKAGING-PIN-NAME>B05</PACKAGING-PIN-NAME>
                <PIN-NUMBER>99</PIN-NUMBER>
            </HW-PIN>
        """
        element = ET.fromstring(xml_content)
        hw_pin_restored = HwPin(None, "RoundTripPin")
        parser.readHwPin(element, hw_pin_restored)

        assert hw_pin_restored.getShortName() == "RoundTripPin"
        assert len(hw_pin_restored.getFunctionNames()) == 2
        assert "GPIO_OUTPUT" in hw_pin_restored.getFunctionNames()
        assert "GPIO_INPUT" in hw_pin_restored.getFunctionNames()
        assert hw_pin_restored.getPackagingPinName() == "B05"
        assert hw_pin_restored.getPinNumber().getValue() == 99
