"""Reader round-trip tests for VariableDataPrototype (SWCT Table 5.31).

initValue (ValueSpecification, 0..1, aggr) is the class's only own attribute,
serialized as INIT-VALUE inside the VARIABLE-DATA-PROTOTYPE element; exercised
here via a SenderReceiverInterface data element.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestVariableDataPrototypeReader:
    def test_read_field_values(self):
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        <SENDER-RECEIVER-INTERFACE>
                            <SHORT-NAME>SR</SHORT-NAME>
                            <DATA-ELEMENTS>
                                <VARIABLE-DATA-PROTOTYPE>
                                    <SHORT-NAME>DE</SHORT-NAME>
                                    <TYPE-TREF DEST="IMPLEMENTATION-DATA-TYPE">/DataTypes/UInt8</TYPE-TREF>
                                    <INIT-VALUE>
                                        <NUMERICAL-VALUE-SPECIFICATION>
                                            <VALUE>42</VALUE>
                                        </NUMERICAL-VALUE-SPECIFICATION>
                                    </INIT-VALUE>
                                </VARIABLE-DATA-PROTOTYPE>
                            </DATA-ELEMENTS>
                        </SENDER-RECEIVER-INTERFACE>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        ARXMLParser().readARPackages(element, document)

        sr_if = document.getARPackages()[0].getSenderReceiverInterfaces()[0]
        prototype = sr_if.getDataElements()[0]
        assert prototype.getShortName() == "DE"
        assert prototype.getTypeTRef().getValue() == "/DataTypes/UInt8"
        assert prototype.getTypeTRef().getDest() == "IMPLEMENTATION-DATA-TYPE"
        init_value = prototype.getInitValue()
        assert isinstance(init_value, NumericalValueSpecification)
        assert init_value.getValue().getValue() == 42

    def test_read_no_init_value(self):
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        <SENDER-RECEIVER-INTERFACE>
                            <SHORT-NAME>SR</SHORT-NAME>
                            <DATA-ELEMENTS>
                                <VARIABLE-DATA-PROTOTYPE>
                                    <SHORT-NAME>DE</SHORT-NAME>
                                    <TYPE-TREF DEST="IMPLEMENTATION-DATA-TYPE">/DataTypes/UInt8</TYPE-TREF>
                                </VARIABLE-DATA-PROTOTYPE>
                            </DATA-ELEMENTS>
                        </SENDER-RECEIVER-INTERFACE>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        ARXMLParser().readARPackages(element, document)

        sr_if = document.getARPackages()[0].getSenderReceiverInterfaces()[0]
        prototype = sr_if.getDataElements()[0]
        assert prototype.getInitValue() is None
