"""Parser tests for ImplementationDataTypeElementInPortInterfaceRef (Table 7.22, p.789).

Element/complexType shape per AUTOSAR_00052.xsd: the class is the type of the inner
IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF element (the polymorphic choice
inside DataPrototypeTransformationProps' outer DATA-PROTOTYPE-IN-PORT-INTERFACE-REF
element). Content: TAG-ID (shared DATA-PROTOTYPE-REFERENCE group), ROOT-DATA-PROTOTYPE-REF,
the CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS wrapper holding 0..*
CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF items, and TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInPortInterfaceRef,
    DataPrototypeTransformationProps,
    ImplementationDataTypeElementInPortInterfaceRef,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestImplementationDataTypeElementInPortInterfaceRef:
    def test_read_full_ref(self, parser):
        xml = """
          <IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF>
            <TAG-ID>5</TAG-ID>
            <ROOT-DATA-PROTOTYPE-REF DEST="AUTOSAR-DATA-PROTOTYPE">/Root/Var</ROOT-DATA-PROTOTYPE-REF>
            <CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS>
              <CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/ImplDt/RecElem</CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF>
              <CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF DEST="CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT">/ImplDt/RecElem/CppElem</CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF>
            </CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS>
            <TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/ImplDt/TargetElem</TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF>
          </IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF>
        """
        root = _snip(xml)
        element = parser.find(root, "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF")
        ref = ImplementationDataTypeElementInPortInterfaceRef()
        parser.readImplementationDataTypeElementInPortInterfaceRef(element, ref)

        assert ref.getTagId() is not None
        assert ref.getTagId().getValue() == 5

        root_ref = ref.getRootDataPrototypeRef()
        assert root_ref is not None
        assert root_ref.getValue() == "/Root/Var"
        assert root_ref.getDest() == "AUTOSAR-DATA-PROTOTYPE"

        ctx_refs = ref.getContextImplementationDataElementRefs()
        assert len(ctx_refs) == 2
        assert ctx_refs[0].getValue() == "/ImplDt/RecElem"
        assert ctx_refs[0].getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert ctx_refs[1].getValue() == "/ImplDt/RecElem/CppElem"
        assert ctx_refs[1].getDest() == "CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT"

        target_ref = ref.getTargetImplementationDataTypeElementRef()
        assert target_ref is not None
        assert target_ref.getValue() == "/ImplDt/TargetElem"
        assert target_ref.getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

    def test_read_empty_ref(self, parser):
        root = _snip("<IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF/>")
        element = parser.find(root, "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF")
        ref = ImplementationDataTypeElementInPortInterfaceRef()
        parser.readImplementationDataTypeElementInPortInterfaceRef(element, ref)

        assert ref.getTagId() is None
        assert ref.getRootDataPrototypeRef() is None
        assert ref.getContextImplementationDataElementRefs() == []
        assert ref.getTargetImplementationDataTypeElementRef() is None

    def test_read_via_transformation_props_dispatch(self, parser):
        xml = """
          <DATA-PROTOTYPE-TRANSFORMATION-PROPS>
            <DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
              <IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF>
                <TAG-ID>3</TAG-ID>
                <ROOT-DATA-PROTOTYPE-REF DEST="AUTOSAR-DATA-PROTOTYPE">/Root/Var</ROOT-DATA-PROTOTYPE-REF>
                <TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/ImplDt/TargetElem</TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF>
              </IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF>
            </DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
          </DATA-PROTOTYPE-TRANSFORMATION-PROPS>
        """
        root = _snip(xml)
        element = parser.find(root, "DATA-PROTOTYPE-TRANSFORMATION-PROPS")
        props = DataPrototypeTransformationProps()
        parser.readDataPrototypeTransformationProps(element, props)

        ref = props.getDataPrototypeInPortInterfaceRef()
        assert isinstance(ref, ImplementationDataTypeElementInPortInterfaceRef)
        assert ref.getTagId() is not None
        assert ref.getTagId().getValue() == 3
        assert ref.getRootDataPrototypeRef() is not None
        assert ref.getRootDataPrototypeRef().getValue() == "/Root/Var"
        assert ref.getTargetImplementationDataTypeElementRef() is not None
        assert ref.getTargetImplementationDataTypeElementRef().getValue() == "/ImplDt/TargetElem"

    def test_read_via_transformation_props_dispatch_data_prototype_branch(self, parser):
        xml = """
          <DATA-PROTOTYPE-TRANSFORMATION-PROPS>
            <DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
              <DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
                <TAG-ID>5</TAG-ID>
              </DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
            </DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
          </DATA-PROTOTYPE-TRANSFORMATION-PROPS>
        """
        root = _snip(xml)
        element = parser.find(root, "DATA-PROTOTYPE-TRANSFORMATION-PROPS")
        props = DataPrototypeTransformationProps()
        parser.readDataPrototypeTransformationProps(element, props)

        ref = props.getDataPrototypeInPortInterfaceRef()
        assert isinstance(ref, DataPrototypeInPortInterfaceRef)
        assert ref.getTagId() is not None
        assert ref.getTagId().getValue() == 5
