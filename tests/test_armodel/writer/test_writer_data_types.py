"""Tests for writer data types and compu method handlers."""
import xml.etree.cElementTree as ET
import pytest

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.AsamHdo.BaseTypes import BaseTypeDirectDefinition, SwBaseType
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import (
    Compu,
    CompuConst,
    CompuConstFormulaContent,
    CompuConstNumericContent,
    CompuConstTextContent,
    CompuConstContent,
    CompuMethod,
    CompuNominatorDenominator,
    CompuRationalCoeffs,
    CompuScale,
    CompuScaleConstantContents,
    CompuScaleRationalFormula,
    CompuScales,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import (
    DataConstr,
    DataConstrRule,
    InternalConstrs,
    PhysConstrs,
)
from armodel.models.M2.MSR.AsamHdo.Units import Unit
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGrouped, SwAxisIndividual
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    SwCalprmAxis,
    SwCalprmAxisSet,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
    SwPointerTargetProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
    ApplicationValueSpecification,
    ArrayValueSpecification,
    ConstantSpecification,
    NumericalValueSpecification,
    RecordValueSpecification,
    TextValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARNumerical,
    ARFloat,
    Limit,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _literal(text):
    literal = ARLiteral()
    literal.setValue(text)
    return literal


def _numerical(text):
    num = ARNumerical()
    num.value = text
    return num


def _float(text):
    num = ARFloat()
    num.value = text
    return num


def _text_scale_contents(text):
    contents = CompuScaleConstantContents()
    const = CompuConst()
    text_content = CompuConstTextContent()
    text_content.vt = _literal(text)
    const.setCompuConstContentType(text_content)
    contents.setCompuConst(const)
    return contents


class TestSwAxisIndividualWriter:
    def test_set_sw_axis_individual_full(self, writer):
        props = SwAxisIndividual()
        props.setInputVariableTypeRef(_ref("VARIABLE-DATA-PROTOTYPE", "/iv"))
        props.setCompuMethodRef(_ref("COMPU-METHOD", "/cm"))
        props.setSwMaxAxisPoints(_numerical("100"))
        props.setSwMinAxisPoints(_numerical("10"))
        props.setDataConstrRef(_ref("DATA-CONSTR", "/dc"))

        parent = _parent()
        writer.setSwAxisIndividual(parent, props)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-AXIS-INDIVIDUAL"
        assert child.find("INPUT-VARIABLE-TYPE-REF").text == "/iv"
        assert child.find("COMPU-METHOD-REF").text == "/cm"
        assert child.find("SW-MAX-AXIS-POINTS").text == "100"
        assert child.find("SW-MIN-AXIS-POINTS").text == "10"
        assert child.find("DATA-CONSTR-REF").text == "/dc"

    def test_set_sw_axis_individual_empty(self, writer):
        props = SwAxisIndividual()
        parent = _parent()
        writer.setSwAxisIndividual(parent, props)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-AXIS-INDIVIDUAL"
        assert child.find("INPUT-VARIABLE-TYPE-REF") is None
        assert child.find("SW-MAX-AXIS-POINTS") is None


class TestSwAxisGroupedWriter:
    def test_set_sw_axis_grouped(self, writer):
        props = SwAxisGrouped()
        props.setSharedAxisTypeRef(_ref("SW-CALPRM-AXIS", "/shared"))

        parent = _parent()
        writer.setSwAxisGrouped(parent, props)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-AXIS-GROUPED"
        ref_el = child.find("SHARED-AXIS-TYPE-REF")
        assert ref_el is not None
        assert ref_el.text == "/shared"
        assert ref_el.attrib.get("DEST") == "SW-CALPRM-AXIS"


class TestSwCalprmAxisWriter:
    def test_set_sw_calprm_axis_none(self, writer):
        parent = _parent()
        writer.setSwCalprmAxis(parent, None)
        assert len(parent) == 0

    def test_set_sw_calprm_axis_individual(self, writer):
        axis = SwCalprmAxis()
        axis.sw_axis_index = _numerical("1")
        axis.category = _literal("FIXED")
        individual = SwAxisIndividual()
        individual.setSwMaxAxisPoints(_numerical("50"))
        axis.sw_calprm_axis_type_props = individual

        parent = _parent()
        writer.setSwCalprmAxis(parent, axis)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-CALPRM-AXIS"
        assert child.find("SW-AXIS-INDEX").text == "1"
        assert child.find("CATEGORY").text == "FIXED"
        assert child.find("SW-AXIS-INDIVIDUAL") is not None
        assert child.find("SW-AXIS-INDIVIDUAL/SW-MAX-AXIS-POINTS").text == "50"

    def test_set_sw_calprm_axis_grouped(self, writer):
        axis = SwCalprmAxis()
        axis.sw_axis_index = _numerical("2")
        axis.category = _literal("STD")
        grouped = SwAxisGrouped()
        grouped.setSharedAxisTypeRef(_ref("SW-CALPRM-AXIS", "/g"))
        axis.sw_calprm_axis_type_props = grouped

        parent = _parent()
        writer.setSwCalprmAxis(parent, axis)

        child = parent[0]
        assert child.tag == "SW-CALPRM-AXIS"
        assert child.find("SW-AXIS-INDEX").text == "2"
        assert child.find("CATEGORY").text == "STD"
        assert child.find("SW-AXIS-GROUPED") is not None
        assert child.find("SW-AXIS-GROUPED/SHARED-AXIS-TYPE-REF").text == "/g"

    def test_set_sw_calprm_axis_unsupported_props_warning(self):
        w = ARXMLWriter(options={"warning": True})

        class FakeProps:
            pass

        axis = SwCalprmAxis()
        axis.sw_calprm_axis_type_props = FakeProps()

        parent = _parent()
        w.setSwCalprmAxis(parent, axis)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-CALPRM-AXIS"


class TestSwCalprmAxisSetWriter:
    def test_set_sw_calprm_axis_set_empty(self, writer):
        ax_set = SwCalprmAxisSet()
        parent = _parent()
        writer.setSwCalprmAxisSet(parent, "SW-CALPRM-AXIS-SET", ax_set)
        assert len(parent) == 0

    def test_set_sw_calprm_axis_set_with_axes(self, writer):
        ax_set = SwCalprmAxisSet()
        axis1 = SwCalprmAxis()
        axis1.category = _literal("FIXED")
        axis2 = SwCalprmAxis()
        axis2.category = _literal("STD")
        ax_set.addSwCalprmAxis(axis1)
        ax_set.addSwCalprmAxis(axis2)

        parent = _parent()
        writer.setSwCalprmAxisSet(parent, "SW-CALPRM-AXIS-SET", ax_set)

        assert len(parent) == 1
        outer = parent[0]
        assert outer.tag == "SW-CALPRM-AXIS-SET"
        axes = outer.findall("SW-CALPRM-AXIS")
        assert len(axes) == 2


class TestSwPointerTargetPropsWriter:
    def test_set_sw_pointer_target_props_none(self, writer):
        parent = _parent()
        writer.setSwPointerTargetProps(parent, "SW-POINTER-TARGET-PROPS", None)
        assert len(parent) == 0

    def test_set_sw_pointer_target_props_with_data_def(self, writer):
        props = SwPointerTargetProps()
        props.setTargetCategory(_literal("VOID"))
        sub_props = SwDataDefProps()
        sub_ref = _ref("SW-BASE-TYPE", "/bt")
        sub_props.setBaseTypeRef(sub_ref)
        sub_props.setSwCalprmAxisSet(SwCalprmAxisSet())
        props.setSwDataDefProps(sub_props)

        parent = _parent()
        writer.setSwPointerTargetProps(parent, "SW-POINTER-TARGET-PROPS", props)

        assert len(parent) == 1
        outer = parent[0]
        assert outer.tag == "SW-POINTER-TARGET-PROPS"
        assert outer.find("TARGET-CATEGORY").text == "VOID"
        sddp = outer.find("SW-DATA-DEF-PROPS")
        assert sddp is not None
        cond = sddp.find("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
        assert cond is not None
        assert cond.find("BASE-TYPE-REF").text == "/bt"


class TestSwDataDefPropsWriter:
    def test_set_sw_data_def_props_none(self, writer):
        parent = _parent()
        writer.setSwDataDefProps(parent, "SW-DATA-DEF-PROPS", None)
        assert len(parent) == 0

    def test_set_sw_data_def_props_full(self, writer):
        props = SwDataDefProps()
        props.setBaseTypeRef(_ref("SW-BASE-TYPE", "/bt"))
        props.setSwAddrMethodRef(_ref("SW-ADDR-METHOD", "/am"))
        props.setSwCalibrationAccess(_literal("READ-ONLY"))
        props.setCompuMethodRef(_ref("COMPU-METHOD", "/cm"))
        props.setStepSize(_float("0.5"))
        props.setDataConstrRef(_ref("DATA-CONSTR", "/dc"))
        props.setImplementationDataTypeRef(_ref("IMPLEMENTATION-DATA-TYPE", "/idt"))
        props.setSwImplPolicy(_literal("STANDARD"))
        props.setSwIntendedResolution(_numerical("8"))
        props.setSwRecordLayoutRef(_ref("SW-RECORD-LAYOUT", "/rl"))
        props.setValueAxisDataTypeRef(_ref("APPLICATION-PRIMITIVE-DATA-TYPE", "/vad"))
        props.setUnitRef(_ref("UNIT", "/u"))

        ax_set = SwCalprmAxisSet()
        ax = SwCalprmAxis()
        ax.category = _literal("FIXED")
        ax_set.addSwCalprmAxis(ax)
        props.setSwCalprmAxisSet(ax_set)

        ptr_props = SwPointerTargetProps()
        ptr_props.setTargetCategory(_literal("PTR"))
        props.setSwPointerTargetProps(ptr_props)

        parent = _parent()
        writer.setSwDataDefProps(parent, "SW-DATA-DEF-PROPS", props)

        outer = parent.find("SW-DATA-DEF-PROPS")
        assert outer is not None
        variants = outer.find("SW-DATA-DEF-PROPS-VARIANTS")
        assert variants is not None
        cond = variants.find("SW-DATA-DEF-PROPS-CONDITIONAL")
        assert cond is not None
        assert cond.find("BASE-TYPE-REF").text == "/bt"
        assert cond.find("SW-ADDR-METHOD-REF").text == "/am"
        assert cond.find("SW-CALIBRATION-ACCESS").text == "READ-ONLY"
        assert cond.find("COMPU-METHOD-REF").text == "/cm"
        assert cond.find("STEP-SIZE").text == "0.5"
        assert cond.find("DATA-CONSTR-REF").text == "/dc"
        assert cond.find("IMPLEMENTATION-DATA-TYPE-REF").text == "/idt"
        assert cond.find("SW-IMPL-POLICY").text == "STANDARD"
        assert cond.find("SW-INTENDED-RESOLUTION").text == "8"
        assert cond.find("SW-RECORD-LAYOUT-REF").text == "/rl"
        assert cond.find("VALUE-AXIS-DATA-TYPE-REF").text == "/vad"
        assert cond.find("UNIT-REF").text == "/u"
        assert cond.find("SW-CALPRM-AXIS-SET") is not None
        assert cond.find("SW-POINTER-TARGET-PROPS/TARGET-CATEGORY").text == "PTR"


class TestApplicationPrimitiveDataTypeWriter:
    def test_write_application_primitive_data_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        data_type = pkg.createApplicationPrimitiveDataType("Speed")

        parent = _parent()
        writer.writeApplicationPrimitiveDataType(parent, data_type)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert child.find("SHORT-NAME").text == "Speed"

    def test_write_application_primitive_data_type_with_props(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        data_type = pkg.createApplicationPrimitiveDataType("Speed")
        props = SwDataDefProps()
        props.setCompuMethodRef(_ref("COMPU-METHOD", "/cm"))
        props.setSwCalprmAxisSet(SwCalprmAxisSet())
        data_type.setSwDataDefProps(props)

        parent = _parent()
        writer.writeApplicationPrimitiveDataType(parent, data_type)

        child = parent[0]
        sddp = child.find("SW-DATA-DEF-PROPS")
        assert sddp is not None
        cond = sddp.find("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
        assert cond.find("COMPU-METHOD-REF").text == "/cm"


class TestDataPrototypeWriter:
    def test_write_dataprototype(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        record = pkg.createApplicationRecordDataType("Record")
        element = record.createApplicationRecordElement("Field")

        parent = ET.Element("ELEMENT")
        writer.writeDataPrototype(parent, element)

        assert parent.find("SHORT-NAME").text == "Field"


class TestApplicationRecordElementWriter:
    def test_write_application_record_element(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        record = pkg.createApplicationRecordDataType("Record")
        element = record.createApplicationRecordElement("Field")
        element.setTypeTRef(_ref("APPLICATION-PRIMITIVE-DATA-TYPE", "/apt"))

        parent = ET.Element("ELEMENTS")
        writer.writeApplicationRecordElement(parent, element)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-RECORD-ELEMENT"
        assert child.find("SHORT-NAME").text == "Field"
        assert child.find("TYPE-TREF").text == "/apt"


class TestApplicationRecordDataTypeWriter:
    def test_write_application_record_data_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        record = pkg.createApplicationRecordDataType("Point")
        record.createApplicationRecordElement("X")
        record.createApplicationRecordElement("Y")

        parent = _parent()
        writer.writeApplicationRecordDataType(parent, record)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-RECORD-DATA-TYPE"
        assert child.find("SHORT-NAME").text == "Point"
        elements = child.find("ELEMENTS")
        assert elements is not None
        assert len(elements.findall("APPLICATION-RECORD-ELEMENT")) == 2

    def test_write_application_record_data_type_no_elements(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        record = pkg.createApplicationRecordDataType("Empty")

        parent = _parent()
        writer.writeApplicationRecordDataType(parent, record)

        child = parent[0]
        assert child.tag == "APPLICATION-RECORD-DATA-TYPE"
        assert child.find("ELEMENTS") is None

    def test_write_application_record_data_type_unsupported_element_warning(self):
        w = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        record = pkg.createApplicationRecordDataType("WithBad")

        record.record_elements.append("not-an-element")

        parent = _parent()
        w.writeApplicationRecordDataType(parent, record)

        child = parent[0]
        assert child.tag == "APPLICATION-RECORD-DATA-TYPE"
        assert child.find("ELEMENTS") is not None


class TestSetApplicationCompositeDataTypeWriter:
    def test_set_application_composite_data_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        record = pkg.createApplicationRecordDataType("Comp")

        parent = ET.Element("WRAPPER")
        writer.setApplicationCompositeDataType(parent, record)

        assert parent.find("SW-DATA-DEF-PROPS") is None


class TestWriteApplicationDataTypesWriter:
    def test_write_application_data_types_dispatch(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        pkg.createApplicationPrimitiveDataType("Primitive")
        pkg.createApplicationRecordDataType("Record")

        parent = ET.Element("ELEMENTS")
        writer.writeApplicationDataTypes(parent, pkg)

        tags = [child.tag for child in parent]
        assert "APPLICATION-PRIMITIVE-DATA-TYPE" in tags
        assert "APPLICATION-RECORD-DATA-TYPE" in tags

    def test_write_application_data_types_unsupported_warning(self):
        w = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        pkg.createApplicationArrayDataType("Array")

        parent = ET.Element("ELEMENTS")
        w.writeApplicationDataTypes(parent, pkg)

        assert len(parent) == 0


class TestBaseTypeDirectDefinitionWriter:
    def test_set_base_type_direct_definition(self, writer):
        btd = BaseTypeDirectDefinition()
        btd.setBaseTypeSize(_numerical("32"))
        btd.setBaseTypeEncoding(_literal("IEEE754"))
        btd.setByteOrder(_literal("LITTLE-ENDIAN"))
        btd.setMemAlignment(_numerical("4"))
        btd.setNativeDeclaration(_literal("float"))

        parent = _parent()
        writer.setBaseTypeDirectDefinition(parent, btd)

        assert parent.find("BASE-TYPE-SIZE").text == "32"
        assert parent.find("BASE-TYPE-ENCODING").text == "IEEE754"
        assert parent.find("BYTE-ORDER").text == "LITTLE-ENDIAN"
        assert parent.find("MEM-ALIGNMENT").text == "4"
        assert parent.find("NATIVE-DECLARATION").text == "float"

    def test_set_base_type_direct_definition_empty(self, writer):
        btd = BaseTypeDirectDefinition()
        parent = _parent()
        writer.setBaseTypeDirectDefinition(parent, btd)
        assert len(parent) == 0


class TestSwBaseTypeWriter:
    def test_write_sw_base_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("BaseTypes")
        base = pkg.createSwBaseType("uint8")
        base.getBaseTypeDefinition().setBaseTypeSize(_numerical("8"))
        base.getBaseTypeDefinition().setNativeDeclaration(_literal("uint8_t"))

        parent = _parent()
        writer.writeSwBaseType(parent, base)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-BASE-TYPE"
        assert child.find("SHORT-NAME").text == "uint8"
        assert child.find("BASE-TYPE-SIZE").text == "8"
        assert child.find("NATIVE-DECLARATION").text == "uint8_t"


class TestCompuNominatorDenominatorWriter:
    def test_write_compu_nominator_denominator(self, writer):
        nd = CompuNominatorDenominator()
        nd.add_v("1.0")
        nd.add_v("2.0")

        parent = _parent()
        writer.writeCompuNominatorDenominator(parent, "COMPU-NUMERATOR", nd)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "COMPU-NUMERATOR"
        vs = child.findall("V")
        assert len(vs) == 2
        assert vs[0].text == "1.0"
        assert vs[1].text == "2.0"

    def test_write_compu_nominator_denominator_empty(self, writer):
        nd = CompuNominatorDenominator()
        parent = _parent()
        writer.writeCompuNominatorDenominator(parent, "COMPU-DENOMINATOR", nd)

        child = parent[0]
        assert child.tag == "COMPU-DENOMINATOR"
        assert child.findall("V") == []


class TestCompuScaleRationalFormulaWriter:
    def test_write_compu_scale_rational_formula_no_coeffs(self, writer):
        contents = CompuScaleRationalFormula()
        parent = _parent()
        writer.writeCompuScaleRationalFormula(parent, contents)
        assert len(parent) == 0

    def test_write_compu_scale_rational_formula_with_coeffs(self, writer):
        contents = CompuScaleRationalFormula()
        coeffs = CompuRationalCoeffs()
        num = CompuNominatorDenominator()
        num.add_v("1.0")
        num.add_v("2.0")
        den = CompuNominatorDenominator()
        den.add_v("3.0")
        coeffs.setCompuNumerator(num)
        coeffs.setCompuDenominator(den)
        contents.setCompuRationalCoeffs(coeffs)

        parent = _parent()
        writer.writeCompuScaleRationalFormula(parent, contents)

        assert len(parent) == 1
        coeffs_tag = parent[0]
        assert coeffs_tag.tag == "COMPU-RATIONAL-COEFFS"
        num_tag = coeffs_tag.find("COMPU-NUMERATOR")
        assert num_tag is not None
        assert [v.text for v in num_tag.findall("V")] == ["1.0", "2.0"]
        den_tag = coeffs_tag.find("COMPU-DENOMINATOR")
        assert den_tag is not None
        assert [v.text for v in den_tag.findall("V")] == ["3.0"]


class TestCompuScaleConstantContentsWriter:
    def test_write_compu_scale_constant_contents_text(self, writer):
        contents = CompuScaleConstantContents()
        const = CompuConst()
        text_content = CompuConstTextContent()
        text_content.vt = _literal("Active")
        const.setCompuConstContentType(text_content)
        contents.setCompuConst(const)

        parent = _parent()
        writer.writeCompuScaleConstantContents(parent, contents)

        assert len(parent) == 1
        const_tag = parent[0]
        assert const_tag.tag == "COMPU-CONST"
        vt = const_tag.find("VT")
        assert vt is not None
        assert vt.text == "Active"


class TestCompuScaleContentsWriter:
    def test_write_compu_scale_contents_constant(self, writer):
        scale = CompuScale()
        contents = CompuScaleConstantContents()
        const = CompuConst()
        text_content = CompuConstTextContent()
        text_content.vt = _literal("On")
        const.setCompuConstContentType(text_content)
        contents.setCompuConst(const)
        scale.compuScaleContents = contents

        parent = _parent()
        writer.writeCompuScaleContents(parent, scale)

        assert parent.find("COMPU-CONST/VT").text == "On"

    def test_write_compu_scale_contents_rational(self, writer):
        scale = CompuScale()
        contents = CompuScaleRationalFormula()
        coeffs = CompuRationalCoeffs()
        num = CompuNominatorDenominator()
        num.add_v("1.0")
        coeffs.setCompuNumerator(num)
        contents.setCompuRationalCoeffs(coeffs)
        scale.compuScaleContents = contents

        parent = _parent()
        writer.writeCompuScaleContents(parent, scale)

        assert parent.find("COMPU-RATIONAL-COEFFS/COMPU-NUMERATOR/V").text == "1.0"

    def test_write_compu_scale_contents_unsupported_warning(self):
        w = ARXMLWriter(options={"warning": True})
        scale = CompuScale()
        scale.compuScaleContents = None

        parent = _parent()
        w.writeCompuScaleContents(parent, scale)
        assert len(parent) == 0


class TestSetCompuConstContentWriter:
    def test_set_compu_const_content_none(self, writer):
        parent = _parent()
        writer.setCompuConstContent(parent, None)
        assert len(parent) == 0

    def test_set_compu_const_content_formula(self, writer):
        content = CompuConstFormulaContent()
        content.setVf(_literal("x*2"))
        parent = _parent()
        writer.setCompuConstContent(parent, content)
        assert parent.find("VF").text == "x*2"

    def test_set_compu_const_content_numeric(self, writer):
        content = CompuConstNumericContent()
        content.setV(_numerical("42"))
        parent = _parent()
        writer.setCompuConstContent(parent, content)
        assert parent.find("V").text == "42"

    def test_set_compu_const_content_text(self, writer):
        content = CompuConstTextContent()
        content.setVt(_literal("ON"))
        parent = _parent()
        writer.setCompuConstContent(parent, content)
        assert parent.find("VT").text == "ON"

    def test_set_compu_const_content_unsupported_warning(self):
        w = ARXMLWriter(options={"warning": True})

        class Fake:
            pass

        parent = _parent()
        w.setCompuConstContent(parent, Fake())
        assert len(parent) == 0


class TestWriteCompuScaleWriter:
    def test_write_compu_scale_none(self, writer):
        parent = _parent()
        writer.writeCompuScale(parent, "COMPU-SCALE", None)
        assert len(parent) == 0

    def test_write_compu_scale_full(self, writer):
        scale = CompuScale()
        scale.setShortLabel(_literal("Low"))
        scale.setSymbol(_literal("LOW"))
        mask = ARNumerical()
        mask.value = "255"
        scale.setMask(mask)
        lower = Limit()
        lower.value = "0"
        lower.intervalType = "CLOSED"
        scale.setLowerLimit(lower)
        upper = Limit()
        upper.value = "10"
        upper.intervalType = "CLOSED"
        scale.setUpperLimit(upper)

        contents = CompuScaleConstantContents()
        const = CompuConst()
        text_content = CompuConstTextContent()
        text_content.vt = _literal("Low")
        const.setCompuConstContentType(text_content)
        contents.setCompuConst(const)
        scale.setCompuScaleContents(contents)

        parent = _parent()
        writer.writeCompuScale(parent, "COMPU-SCALE", scale)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "COMPU-SCALE"
        assert child.find("SHORT-LABEL").text == "Low"
        assert child.find("SYMBOL").text == "LOW"
        assert child.find("MASK").text == "255"
        assert child.find("LOWER-LIMIT").text == "0"
        assert child.find("UPPER-LIMIT").text == "10"
        assert child.find("COMPU-CONST/VT").text == "Low"


class TestSetCompuScalesWriter:
    def test_set_compu_scales_none(self, writer):
        parent = _parent()
        writer.setCompuScales(parent, None)
        assert len(parent) == 0

    def test_set_compu_scales_empty(self, writer):
        scales = CompuScales()
        parent = _parent()
        writer.setCompuScales(parent, scales)
        assert len(parent) == 1
        assert parent[0].tag == "COMPU-SCALES"
        assert parent[0].findall("COMPU-SCALE") == []

    def test_set_compu_scales_with_entries(self, writer):
        scales = CompuScales()
        s1 = CompuScale()
        s1.setShortLabel(_literal("A"))
        s1.setCompuScaleContents(_text_scale_contents("A"))
        s2 = CompuScale()
        s2.setShortLabel(_literal("B"))
        s2.setCompuScaleContents(_text_scale_contents("B"))
        scales.addCompuScale(s1)
        scales.addCompuScale(s2)

        parent = _parent()
        writer.setCompuScales(parent, scales)

        outer = parent[0]
        assert outer.tag == "COMPU-SCALES"
        assert len(outer.findall("COMPU-SCALE")) == 2


class TestSetCompuConstWriter:
    def test_set_compu_const_none(self, writer):
        parent = _parent()
        writer.setCompuConst(parent, "COMPU-DEFAULT-VALUE", None)
        assert len(parent) == 0

    def test_set_compu_const_with_content(self, writer):
        const = CompuConst()
        content = CompuConstTextContent()
        content.setVt(_literal("Default"))
        const.setCompuConstContentType(content)

        parent = _parent()
        writer.setCompuConst(parent, "COMPU-DEFAULT-VALUE", const)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "COMPU-DEFAULT-VALUE"
        assert child.find("VT").text == "Default"


class TestSetCompuWriter:
    def test_set_compu_none(self, writer):
        parent = _parent()
        writer.setCompu(parent, "COMPU-INTERNAL-TO-PHYS", None)
        assert len(parent) == 0

    def test_set_compu_full(self, writer):
        compu = Compu()
        scales = CompuScales()
        s1 = CompuScale()
        s1.setShortLabel(_literal("Scale1"))
        s1.setCompuScaleContents(_text_scale_contents("S1"))
        scales.addCompuScale(s1)
        compu.setCompuContent(scales)

        default = CompuConst()
        content = CompuConstTextContent()
        content.setVt(_literal("Def"))
        default.setCompuConstContentType(content)
        compu.setCompuDefaultValue(default)

        parent = _parent()
        writer.setCompu(parent, "COMPU-INTERNAL-TO-PHYS", compu)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "COMPU-INTERNAL-TO-PHYS"
        assert child.find("COMPU-SCALES/COMPU-SCALE/SHORT-LABEL").text == "Scale1"
        assert child.find("COMPU-DEFAULT-VALUE/VT").text == "Def"


class TestWriteCompuMethodWriter:
    def test_write_compu_method_basic(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Compu")
        cm = pkg.createCompuMethod("SpeedConv")
        cm.setUnitRef(_ref("UNIT", "/units/kmh"))

        parent = _parent()
        writer.writeCompuMethod(parent, cm)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "COMPU-METHOD"
        assert child.find("SHORT-NAME").text == "SpeedConv"
        assert child.find("UNIT-REF").text == "/units/kmh"

    def test_write_compu_method_with_compu(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Compu")
        cm = pkg.createCompuMethod("TempConv")

        compu = Compu()
        scales = CompuScales()
        s = CompuScale()
        s.setShortLabel(_literal("Cold"))
        s.setCompuScaleContents(_text_scale_contents("Cold"))
        scales.addCompuScale(s)
        compu.setCompuContent(scales)
        cm.setCompuInternalToPhys(compu)

        parent = _parent()
        writer.writeCompuMethod(parent, cm)

        child = parent[0]
        assert child.find("COMPU-INTERNAL-TO-PHYS/COMPU-SCALES/COMPU-SCALE/SHORT-LABEL").text == "Cold"


class TestApplicationValueSpecificationWriter:
    def test_write_application_value_specification_none(self, writer):
        parent = _parent()
        writer.writeApplicationValueSpecification(parent, None)
        assert len(parent) == 0

    def test_write_application_value_specification_basic(self, writer):
        spec = ApplicationValueSpecification()
        spec.setShortLabel(_literal("Label"))
        spec.setCategory(_literal("CONST"))
        spec.setSwValueCont(None)

        parent = _parent()
        writer.writeApplicationValueSpecification(parent, spec)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-VALUE-SPECIFICATION"
        assert child.find("SHORT-LABEL").text == "Label"
        assert child.find("CATEGORY").text == "CONST"


class TestRecordValueSpecificationWriter:
    def test_write_record_value_specification_with_text_field(self, writer):
        rec = RecordValueSpecification()
        rec.setShortLabel(_literal("Rec"))
        text = TextValueSpecification()
        text.setShortLabel(_literal("T"))
        text.setValue(_literal("v"))
        rec.addField(text)

        parent = _parent()
        writer.writeRecordValueSpecification(parent, rec)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "RECORD-VALUE-SPECIFICATION"
        assert child.find("SHORT-LABEL").text == "Rec"
        fields = child.find("FIELDS")
        assert fields is not None
        assert fields.find("TEXT-VALUE-SPECIFICATION/SHORT-LABEL").text == "T"

    def test_write_record_value_specification_with_numerical_field(self, writer):
        rec = RecordValueSpecification()
        num = NumericalValueSpecification()
        num.setShortLabel(_literal("N"))
        nv = ARNumerical()
        nv.value = "5"
        num.setValue(nv)
        rec.addField(num)

        parent = _parent()
        writer.writeRecordValueSpecification(parent, rec)

        child = parent[0]
        assert child.find("FIELDS/NUMERICAL-VALUE-SPECIFICATION/SHORT-LABEL").text == "N"

    def test_write_record_value_specification_with_app_value_field(self, writer):
        rec = RecordValueSpecification()
        av = ApplicationValueSpecification()
        av.setShortLabel(_literal("A"))
        av.setCategory(_literal("CONST"))
        rec.addField(av)

        parent = _parent()
        writer.writeRecordValueSpecification(parent, rec)

        child = parent[0]
        assert child.find("FIELDS/APPLICATION-VALUE-SPECIFICATION/CATEGORY").text == "CONST"

    def test_write_record_value_specification_with_nested_record(self, writer):
        rec = RecordValueSpecification()
        rec.setShortLabel(_literal("Outer"))
        inner = RecordValueSpecification()
        inner.setShortLabel(_literal("Inner"))
        rec.addField(inner)

        parent = _parent()
        writer.writeRecordValueSpecification(parent, rec)

        child = parent[0]
        assert child.find("FIELDS/RECORD-VALUE-SPECIFICATION/SHORT-LABEL").text == "Inner"

    def test_write_record_value_specification_with_array_field(self, writer):
        rec = RecordValueSpecification()
        rec.setShortLabel(_literal("WithArray"))
        arr = ArrayValueSpecification()
        arr.setShortLabel(_literal("Arr"))
        nv = NumericalValueSpecification()
        nv.setShortLabel(_literal("Item"))
        val = ARNumerical()
        val.value = "1"
        nv.setValue(val)
        arr.addElement(nv)
        rec.addField(arr)

        parent = _parent()
        writer.writeRecordValueSpecification(parent, rec)

        child = parent[0]
        assert child.find("FIELDS/ARRAY-VALUE-SPECIFICATION/SHORT-LABEL").text == "Arr"

    def test_write_record_value_specification_unsupported_field_warning(self):
        w = ARXMLWriter(options={"warning": True})
        rec = RecordValueSpecification()
        rec.setShortLabel(_literal("WithBad"))

        class Fake:
            pass

        rec.addField(Fake())

        parent = _parent()
        w.writeRecordValueSpecification(parent, rec)

        child = parent[0]
        assert child.tag == "RECORD-VALUE-SPECIFICATION"
        assert child.find("FIELDS") is not None

    def test_write_record_value_specification_no_fields(self, writer):
        rec = RecordValueSpecification()
        parent = _parent()
        writer.writeRecordValueSpecification(parent, rec)

        child = parent[0]
        assert child.tag == "RECORD-VALUE-SPECIFICATION"
        assert child.find("FIELDS") is None


class TestConstantSpecificationWriter:
    def test_write_constant_specification_no_value(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Consts")
        spec = pkg.createConstantSpecification("MyConst")

        parent = _parent()
        writer.writeConstantSpecification(parent, spec)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CONSTANT-SPECIFICATION"
        assert child.find("SHORT-NAME").text == "MyConst"
        assert child.find("VALUE-SPEC") is None

    def test_write_constant_specification_with_value(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Consts")
        spec = pkg.createConstantSpecification("WithVal")

        nv = NumericalValueSpecification()
        nv.setShortLabel(_literal("Init"))
        val = ARNumerical()
        val.value = "10"
        nv.setValue(val)
        spec.setValueSpec(nv)

        parent = _parent()
        writer.writeConstantSpecification(parent, spec)

        child = parent[0]
        vs = child.find("VALUE-SPEC")
        assert vs is not None
        assert vs.find("NUMERICAL-VALUE-SPECIFICATION/SHORT-LABEL").text == "Init"


class TestInternalConstrsWriter:
    def test_set_internal_constrs_none(self, writer):
        parent = _parent()
        writer.setInternalConstrs(parent, None)
        assert len(parent) == 0

    def test_set_internal_constrs_with_limits(self, writer):
        constrs = InternalConstrs()
        lower = Limit()
        lower.value = "0"
        lower.intervalType = "CLOSED"
        constrs.lower_limit = lower
        upper = Limit()
        upper.value = "100"
        upper.intervalType = "CLOSED"
        constrs.upper_limit = upper

        parent = _parent()
        writer.setInternalConstrs(parent, constrs)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "INTERNAL-CONSTRS"
        assert child.find("LOWER-LIMIT").text == "0"
        assert child.find("UPPER-LIMIT").text == "100"

    def test_set_internal_constrs_no_limits(self, writer):
        constrs = InternalConstrs()
        parent = _parent()
        writer.setInternalConstrs(parent, constrs)

        child = parent[0]
        assert child.tag == "INTERNAL-CONSTRS"
        assert child.find("LOWER-LIMIT") is None
        assert child.find("UPPER-LIMIT") is None


class TestPhysConstrsWriter:
    def test_set_phys_constrs_none(self, writer):
        parent = _parent()
        writer.setPhysConstrs(parent, None)
        assert len(parent) == 0

    def test_set_phys_constrs_with_unit(self, writer):
        constrs = PhysConstrs()
        lower = Limit()
        lower.value = "-50.0"
        constrs.lower_limit = lower
        upper = Limit()
        upper.value = "150.0"
        constrs.upper_limit = upper
        constrs.unit_ref = _ref("UNIT", "/units/c")

        parent = _parent()
        writer.setPhysConstrs(parent, constrs)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "PHYS-CONSTRS"
        assert child.find("LOWER-LIMIT").text == "-50.0"
        assert child.find("UPPER-LIMIT").text == "150.0"
        assert child.find("UNIT-REF").text == "/units/c"


class TestDataConstrRulesWriter:
    def test_write_data_constr_rules_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Constrs")
        constr = pkg.createDataConstr("Empty")

        parent = _parent()
        writer.writeDataConstrRules(parent, constr)

        assert len(parent) == 0

    def test_write_data_constr_rules_with_rules(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Constrs")
        constr = pkg.createDataConstr("WithRules")

        rule = DataConstrRule()
        rule.constrLevel = _numerical("1")
        rule.physConstrs = PhysConstrs()
        rule.physConstrs.lower_limit = Limit()
        rule.physConstrs.lower_limit.value = "0"
        rule.internalConstrs = InternalConstrs()
        rule.internalConstrs.lower_limit = Limit()
        rule.internalConstrs.lower_limit.value = "0"
        constr.addDataConstrRule(rule)

        parent = _parent()
        writer.writeDataConstrRules(parent, constr)

        assert len(parent) == 1
        rules_tag = parent[0]
        assert rules_tag.tag == "DATA-CONSTR-RULES"
        rule_tag = rules_tag.find("DATA-CONSTR-RULE")
        assert rule_tag is not None
        assert rule_tag.find("CONSTR-LEVEL").text == "1"
        assert rule_tag.find("PHYS-CONSTRS/LOWER-LIMIT").text == "0"
        assert rule_tag.find("INTERNAL-CONSTRS/LOWER-LIMIT").text == "0"


class TestDataConstrWriter:
    def test_write_data_constr(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Constrs")
        constr = pkg.createDataConstr("MyConstr")

        rule = DataConstrRule()
        rule.constrLevel = _numerical("0")
        rule.physConstrs = PhysConstrs()
        upper = Limit()
        upper.value = "100"
        rule.physConstrs.upper_limit = upper
        constr.addDataConstrRule(rule)

        parent = _parent()
        writer.writeDataConstr(parent, constr)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "DATA-CONSTR"
        assert child.find("SHORT-NAME").text == "MyConstr"
        assert child.find("DATA-CONSTR-RULES/DATA-CONSTR-RULE/CONSTR-LEVEL").text == "0"
        assert child.find("DATA-CONSTR-RULES/DATA-CONSTR-RULE/PHYS-CONSTRS/UPPER-LIMIT").text == "100"


class TestUnitWriter:
    def test_write_unit_basic(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Units")
        unit = pkg.createUnit("Kilometre")

        parent = _parent()
        writer.writeUnit(parent, unit)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "UNIT"
        assert child.find("SHORT-NAME").text == "Kilometre"

    def test_write_unit_full(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Units")
        unit = pkg.createUnit("Metre")
        unit.setDisplayName(_literal("m"))
        unit.setFactorSiToUnit(_float("1.0"))
        unit.setOffsetSiToUnit(_float("0.0"))
        unit.setPhysicalDimensionRef(_ref("PHYSICAL-DIMENSION", "/pd/length"))

        parent = _parent()
        writer.writeUnit(parent, unit)

        child = parent[0]
        assert child.find("DISPLAY-NAME").text == "m"
        assert child.find("FACTOR-SI-TO-UNIT").text == "1.0"
        assert child.find("OFFSET-SI-TO-UNIT").text == "0.0"
        assert child.find("PHYSICAL-DIMENSION-REF").text == "/pd/length"
