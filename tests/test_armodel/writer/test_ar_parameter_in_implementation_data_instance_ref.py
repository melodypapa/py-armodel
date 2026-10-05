"""Writer round-trip tests for ArParameterInImplementationDataInstanceRef (SWCT Table 5.38).

The class is serialized nested inside ImplementationDataTypeSubElementRef
(PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT, AUTOSAR_00052.xsd l.71876); the
parent's dispatch is pending its own sync (Group1.md:954-955), so the reusable
writeArParameterInImplementationDataInstanceRef helper is exercised directly on
the element the parent will create. XSD group order: CONTEXT-DATA-PROTOTYPE-REFS
(wrapper, only when non-empty) < PORT-PROTOTYPE-REF < ROOT-PARAMETER-DATA-PROTOTYPE-REF
< TARGET-DATA-PROTOTYPE-REF.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ArParameterInImplementationDataInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _make_ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestArParameterInImplementationDataInstanceRefWriter:
    def test_write_field_values(self):
        iref = ArParameterInImplementationDataInstanceRef()
        iref.addContextDataPrototypeRef(_make_ref("/DataTypes/ArrayElement", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
        iref.addContextDataPrototypeRef(_make_ref("/DataTypes/LeafElement", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
        iref.setPortPrototypeRef(_make_ref("/Swc/InnerPort", "PORT-PROTOTYPE"))
        iref.setRootParameterDataPrototypeRef(_make_ref("/Swc/RootParameter", "PARAMETER-DATA-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(_make_ref("/DataTypes/TargetElement", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))

        parent = ET.Element("PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT")
        ARXMLWriter().writeArParameterInImplementationDataInstanceRef(parent, iref)

        wrapper = parent.find("CONTEXT-DATA-PROTOTYPE-REFS")
        assert wrapper is not None
        context_refs = wrapper.findall("CONTEXT-DATA-PROTOTYPE-REF")
        assert len(context_refs) == 2
        assert context_refs[0].text == "/DataTypes/ArrayElement"
        assert context_refs[0].get("DEST") == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert context_refs[1].text == "/DataTypes/LeafElement"

        children = [child.tag for child in parent]
        assert children.index("CONTEXT-DATA-PROTOTYPE-REFS") < children.index("PORT-PROTOTYPE-REF")
        assert children.index("PORT-PROTOTYPE-REF") < children.index("ROOT-PARAMETER-DATA-PROTOTYPE-REF")
        assert children.index("ROOT-PARAMETER-DATA-PROTOTYPE-REF") < children.index("TARGET-DATA-PROTOTYPE-REF")

        port_ref = parent.find("PORT-PROTOTYPE-REF")
        assert port_ref.text == "/Swc/InnerPort"
        assert port_ref.get("DEST") == "PORT-PROTOTYPE"
        root_ref = parent.find("ROOT-PARAMETER-DATA-PROTOTYPE-REF")
        assert root_ref.text == "/Swc/RootParameter"
        assert root_ref.get("DEST") == "PARAMETER-DATA-PROTOTYPE"
        target_ref = parent.find("TARGET-DATA-PROTOTYPE-REF")
        assert target_ref.text == "/DataTypes/TargetElement"
        assert target_ref.get("DEST") == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

    def test_write_empty_context_list_emits_no_wrapper(self):
        iref = ArParameterInImplementationDataInstanceRef()
        iref.setTargetDataPrototypeRef(_make_ref("/DataTypes/TargetElement", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))

        parent = ET.Element("PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT")
        ARXMLWriter().writeArParameterInImplementationDataInstanceRef(parent, iref)

        assert parent.find("CONTEXT-DATA-PROTOTYPE-REFS") is None
        assert parent.find("PORT-PROTOTYPE-REF") is None
        assert parent.find("ROOT-PARAMETER-DATA-PROTOTYPE-REF") is None
        assert parent.find("TARGET-DATA-PROTOTYPE-REF") is not None

    def test_write_all_absent(self):
        iref = ArParameterInImplementationDataInstanceRef()

        parent = ET.Element("PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT")
        ARXMLWriter().writeArParameterInImplementationDataInstanceRef(parent, iref)

        assert len(list(parent)) == 0

    def test_round_trip(self):
        iref = ArParameterInImplementationDataInstanceRef()
        iref.addContextDataPrototypeRef(_make_ref("/DataTypes/ArrayElement", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
        iref.addContextDataPrototypeRef(_make_ref("/DataTypes/LeafElement", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
        iref.setPortPrototypeRef(_make_ref("/Swc/InnerPort", "PORT-PROTOTYPE"))
        iref.setRootParameterDataPrototypeRef(_make_ref("/Swc/RootParameter", "PARAMETER-DATA-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(_make_ref("/DataTypes/TargetElement", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))

        parent = ET.Element("PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT")
        ARXMLWriter().writeArParameterInImplementationDataInstanceRef(parent, iref)
        xml = f"""<AUTOSAR xmlns='{NS}'>{ET.tostring(parent, encoding="unicode")}</AUTOSAR>"""  # xsd-skip: runtime writer output, static scan cannot resolve

        element = ET.fromstring(xml)[0]
        iref_read = ArParameterInImplementationDataInstanceRef()
        ARXMLParser().readArParameterInImplementationDataInstanceRef(element, iref_read)

        context_refs = iref_read.getContextDataPrototypeRefs()
        assert len(context_refs) == 2
        assert context_refs[0].getValue() == "/DataTypes/ArrayElement"
        assert context_refs[0].getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert context_refs[1].getValue() == "/DataTypes/LeafElement"
        assert iref_read.getPortPrototypeRef().getValue() == "/Swc/InnerPort"
        assert iref_read.getPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref_read.getRootParameterDataPrototypeRef().getValue() == "/Swc/RootParameter"
        assert iref_read.getRootParameterDataPrototypeRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        assert iref_read.getTargetDataPrototypeRef().getValue() == "/DataTypes/TargetElement"
        assert iref_read.getTargetDataPrototypeRef().getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
