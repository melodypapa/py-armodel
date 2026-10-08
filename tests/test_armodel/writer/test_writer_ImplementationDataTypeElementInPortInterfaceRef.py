"""Writer/reader round-trip tests for ImplementationDataTypeElementInPortInterfaceRef (Table 7.22, p.789).

Wire shape per AUTOSAR_00052.xsd: TAG-ID, ROOT-DATA-PROTOTYPE-REF, the
CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS wrapper (emitted only when non-empty) holding one
CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF per entry, and TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF.
As a subtype of the DataPrototypeTransformationProps.dataPrototypeInPortInterfaceRef choice
(PDF Table 7.17 Type = DataPrototypeReference) it is dispatched by isinstance in the
aggregator's reader/writer.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInPortInterfaceRef,
    DataPrototypeTransformationProps,
    ImplementationDataTypeElementInPortInterfaceRef,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _full_ref() -> ImplementationDataTypeElementInPortInterfaceRef:
    ref = ImplementationDataTypeElementInPortInterfaceRef()
    ref.setTagId(PositiveInteger().setValue("5"))
    ref.setRootDataPrototypeRef(_ref("/Root/Var", "AUTOSAR-DATA-PROTOTYPE"))
    ref.addContextImplementationDataElementRefs(_ref("/ImplDt/RecElem", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    ref.addContextImplementationDataElementRefs(_ref("/ImplDt/RecElem/CppElem", "CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    ref.setTargetImplementationDataTypeElementRef(_ref("/ImplDt/TargetElem", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    return ref


class TestImplementationDataTypeElementInPortInterfaceRefWriter:
    def test_write_full_ref(self, writer):
        parent = ET.Element("PARENT")
        writer.writeImplementationDataTypeElementInPortInterfaceRef(parent, _full_ref())

        el = parent.find("IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF")
        assert el is not None
        assert el.find("TAG-ID").text == "5"

        root_ref = el.find("ROOT-DATA-PROTOTYPE-REF")
        assert root_ref is not None
        assert root_ref.text == "/Root/Var"
        assert root_ref.attrib["DEST"] == "AUTOSAR-DATA-PROTOTYPE"

        ctx_wrapper = el.find("CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS")
        assert ctx_wrapper is not None
        ctx_refs = ctx_wrapper.findall("CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF")
        assert len(ctx_refs) == 2
        assert ctx_refs[0].text == "/ImplDt/RecElem"
        assert ctx_refs[0].attrib["DEST"] == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert ctx_refs[1].text == "/ImplDt/RecElem/CppElem"
        assert ctx_refs[1].attrib["DEST"] == "CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT"

        target_ref = el.find("TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF")
        assert target_ref is not None
        assert target_ref.text == "/ImplDt/TargetElem"
        assert target_ref.attrib["DEST"] == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

        children = [child.tag for child in el]
        assert children.index("TAG-ID") < children.index("ROOT-DATA-PROTOTYPE-REF")
        assert children.index("ROOT-DATA-PROTOTYPE-REF") < children.index("CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS")
        assert children.index("CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS") < children.index("TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF")

    def test_write_empty_ref_has_no_context_wrapper(self, writer):
        parent = ET.Element("PARENT")
        writer.writeImplementationDataTypeElementInPortInterfaceRef(parent, ImplementationDataTypeElementInPortInterfaceRef())

        el = parent.find("IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF")
        assert el is not None
        assert el.find("TAG-ID") is None
        assert el.find("ROOT-DATA-PROTOTYPE-REF") is None
        assert el.find("CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS") is None
        assert el.find("TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF") is None

    def test_write_via_transformation_props_dispatch(self, writer):
        props = DataPrototypeTransformationProps()
        props.setDataPrototypeInPortInterfaceRef(_full_ref())

        parent = ET.Element("PARENT")
        writer.writeDataPrototypeTransformationProps(parent, props)

        dp_tp = parent.find("DATA-PROTOTYPE-TRANSFORMATION-PROPS")
        outer = dp_tp.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        assert outer is not None
        inner = outer.find("IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF")
        assert inner is not None
        assert inner.find("TAG-ID").text == "5"
        assert inner.find("ROOT-DATA-PROTOTYPE-REF").text == "/Root/Var"

    def test_write_via_transformation_props_dispatch_data_prototype_branch(self, writer):
        ref = DataPrototypeInPortInterfaceRef()
        ref.setTagId(PositiveInteger().setValue("7"))
        props = DataPrototypeTransformationProps()
        props.setDataPrototypeInPortInterfaceRef(ref)

        parent = ET.Element("PARENT")
        writer.writeDataPrototypeTransformationProps(parent, props)

        dp_tp = parent.find("DATA-PROTOTYPE-TRANSFORMATION-PROPS")
        outer = dp_tp.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        assert outer is not None
        inner = outer.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        assert inner is not None
        assert inner.find("TAG-ID").text == "7"
        assert outer.find("IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF") is None


class TestImplementationDataTypeElementInPortInterfaceRefRoundTrip:
    def test_round_trip_preserves_all_refs(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeImplementationDataTypeElementInPortInterfaceRef(parent, _full_ref())

        out_file = str(tmp_path / "implementation_data_type_element_in_port_interface_ref.arxml")
        inner = ET.tostring(parent[0]).decode("utf-8")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")

        tree = ET.parse(out_file)
        recovered = ImplementationDataTypeElementInPortInterfaceRef()
        parser.readImplementationDataTypeElementInPortInterfaceRef(parser.find(tree.getroot(), "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF"), recovered)

        assert recovered.getTagId() is not None
        assert recovered.getTagId().getValue() == 5
        assert recovered.getRootDataPrototypeRef() is not None
        assert recovered.getRootDataPrototypeRef().getValue() == "/Root/Var"
        assert recovered.getRootDataPrototypeRef().getDest() == "AUTOSAR-DATA-PROTOTYPE"

        ctx_refs = recovered.getContextImplementationDataElementRefs()
        assert len(ctx_refs) == 2
        assert ctx_refs[0].getValue() == "/ImplDt/RecElem"
        assert ctx_refs[0].getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert ctx_refs[1].getValue() == "/ImplDt/RecElem/CppElem"
        assert ctx_refs[1].getDest() == "CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT"

        assert recovered.getTargetImplementationDataTypeElementRef() is not None
        assert recovered.getTargetImplementationDataTypeElementRef().getValue() == "/ImplDt/TargetElem"

    def test_round_trip_via_transformation_props(self, writer, parser, tmp_path):
        props = DataPrototypeTransformationProps()
        props.setDataPrototypeInPortInterfaceRef(_full_ref())

        parent = ET.Element("PARENT")
        writer.writeDataPrototypeTransformationProps(parent, props)

        out_file = str(tmp_path / "data_prototype_transformation_props_impl_ref.arxml")
        inner = ET.tostring(parent[0]).decode("utf-8")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")

        tree = ET.parse(out_file)
        recovered_props = DataPrototypeTransformationProps()
        parser.readDataPrototypeTransformationProps(parser.find(tree.getroot(), "DATA-PROTOTYPE-TRANSFORMATION-PROPS"), recovered_props)

        recovered = recovered_props.getDataPrototypeInPortInterfaceRef()
        assert isinstance(recovered, ImplementationDataTypeElementInPortInterfaceRef)
        assert recovered.getTagId() is not None
        assert recovered.getTagId().getValue() == 5
        assert recovered.getRootDataPrototypeRef() is not None
        assert recovered.getRootDataPrototypeRef().getValue() == "/Root/Var"
        assert len(recovered.getContextImplementationDataElementRefs()) == 2
        assert recovered.getTargetImplementationDataTypeElementRef() is not None
        assert recovered.getTargetImplementationDataTypeElementRef().getValue() == "/ImplDt/TargetElem"
