"""Reader round-trip tests for DataPrototype.swDataDefProps (SWCT Table 5.28).

DataPrototype is abstract; its single attribute swDataDefProps (SwDataDefProps, 0..1,
aggr) is serialized through the shared readDataPrototype helper, exercised here via a
concrete VariableDataPrototype inside a SenderReceiverInterface.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestDataPrototypeReader:
    def test_read_sw_data_def_props_via_concrete_subclass(self):
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
                                    <SW-DATA-DEF-PROPS>
                                        <SW-DATA-DEF-PROPS-VARIANTS>
                                            <SW-DATA-DEF-PROPS-CONDITIONAL>
                                                <SW-ADDR-METHOD-REF DEST="AUTOSAR/SwAddrMethods/ram"></SW-ADDR-METHOD-REF>
                                            </SW-DATA-DEF-PROPS-CONDITIONAL>
                                        </SW-DATA-DEF-PROPS-VARIANTS>
                                    </SW-DATA-DEF-PROPS>
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
        props = prototype.getSwDataDefProps()
        assert props is not None
        assert props.getSwAddrMethodRef().getDest() == "AUTOSAR/SwAddrMethods/ram"
