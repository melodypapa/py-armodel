"""Reader tests for AutosarDataPrototype.typeTRef (SWCT Table 5.29).

AutosarDataPrototype is abstract; its single attribute type (AutosarDataType,
0..1, tref) is serialized as TYPE-TREF through the reusable
readAutosarDataPrototype helper, exercised here via concrete subclasses.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AutosarDataPrototype, VariableDataPrototype
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestAutosarDataPrototypeReader:
    def test_read_type_tref_field_values(self):
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
        assert isinstance(prototype, AutosarDataPrototype)
        assert prototype.getTypeTRef().getValue() == "/DataTypes/UInt8"
        assert prototype.getTypeTRef().getDest() == "IMPLEMENTATION-DATA-TYPE"

    def test_read_type_tref_absent(self):
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
        assert isinstance(prototype, VariableDataPrototype)
        assert prototype.getTypeTRef() is None
