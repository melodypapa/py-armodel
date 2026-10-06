"""Reader tests for ArParameterInImplementationDataInstanceRef (SWCT Table 5.38).

The class is serialized nested inside ImplementationDataTypeSubElementRef
(PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT, AUTOSAR_00052.xsd l.71876); the
parent's dispatch is pending its own sync (Group1.md:954-955), so the reusable
readArParameterInImplementationDataInstanceRef helper is exercised directly on
the element the parent will hand over.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ArParameterInImplementationDataInstanceRef
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestArParameterInImplementationDataInstanceRefReader:
    def test_read_field_values(self):
        xml = f"""<PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'>
            <CONTEXT-DATA-PROTOTYPE-REFS>
                <CONTEXT-DATA-PROTOTYPE-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/DataTypes/ArrayElement</CONTEXT-DATA-PROTOTYPE-REF>
                <CONTEXT-DATA-PROTOTYPE-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/DataTypes/LeafElement</CONTEXT-DATA-PROTOTYPE-REF>
            </CONTEXT-DATA-PROTOTYPE-REFS>
            <PORT-PROTOTYPE-REF DEST="PORT-PROTOTYPE">/Swc/InnerPort</PORT-PROTOTYPE-REF>
            <ROOT-PARAMETER-DATA-PROTOTYPE-REF DEST="PARAMETER-DATA-PROTOTYPE">/Swc/RootParameter</ROOT-PARAMETER-DATA-PROTOTYPE-REF>
            <TARGET-DATA-PROTOTYPE-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/DataTypes/TargetElement</TARGET-DATA-PROTOTYPE-REF>
        </PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT>"""
        element = ET.fromstring(xml)

        iref = ArParameterInImplementationDataInstanceRef()
        ARXMLParser().readArParameterInImplementationDataInstanceRef(element, iref)

        context_refs = iref.getContextDataPrototypeRefs()
        assert len(context_refs) == 2
        assert context_refs[0].getValue() == "/DataTypes/ArrayElement"
        assert context_refs[0].getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert context_refs[1].getValue() == "/DataTypes/LeafElement"
        assert context_refs[1].getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert iref.getPortPrototypeRef().getValue() == "/Swc/InnerPort"
        assert iref.getPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getRootParameterDataPrototypeRef().getValue() == "/Swc/RootParameter"
        assert iref.getRootParameterDataPrototypeRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        assert iref.getTargetDataPrototypeRef().getValue() == "/DataTypes/TargetElement"
        assert iref.getTargetDataPrototypeRef().getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

    def test_read_empty_context_wrapper(self):
        xml = f"""<PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'>
            <CONTEXT-DATA-PROTOTYPE-REFS/>
        </PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT>"""
        element = ET.fromstring(xml)

        iref = ArParameterInImplementationDataInstanceRef()
        ARXMLParser().readArParameterInImplementationDataInstanceRef(element, iref)

        assert iref.getContextDataPrototypeRefs() == []
        assert iref.getPortPrototypeRef() is None
        assert iref.getRootParameterDataPrototypeRef() is None
        assert iref.getTargetDataPrototypeRef() is None

    def test_read_absent_fields(self):
        xml = f"""<PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'/>"""
        element = ET.fromstring(xml)

        iref = ArParameterInImplementationDataInstanceRef()
        ARXMLParser().readArParameterInImplementationDataInstanceRef(element, iref)

        assert iref.getContextDataPrototypeRefs() == []
        assert iref.getPortPrototypeRef() is None
        assert iref.getRootParameterDataPrototypeRef() is None
        assert iref.getTargetDataPrototypeRef() is None
