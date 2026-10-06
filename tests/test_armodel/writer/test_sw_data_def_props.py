"""
Writer tests for SW-DATA-DEF-PROPS — SWCT Table 5.39 (p.332, R23-11).

Builds a fully populated SwDataDefProps on an ImplementationDataType, saves, reloads and asserts
every field value round-trips. Also pins the writer's emission order inside
SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL to the AUTOSAR_00052.xsd group
SW-DATA-DEF-PROPS-CONTENT element order (sequenceOffset 20..355 plus the unoffset leading
elements DISPLAY-PRESENTATION, STEP-SIZE, SW-VALUE-BLOCK-SIZE-MULTS).

Round-trip counterpart: tests/test_armodel/parser/test_sw_data_def_props.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    Boolean,
    DisplayFormatString,
    Float,
    Identifier,
    Integer,
    NativeDeclarationString,
    Numerical,
    PrimitiveIdentifier,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import CompuGenericMath
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxis, SwCalprmAxisSet
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    DisplayPresentationEnum,
    SwBitRepresentation,
    SwCalibrationAccessEnum,
    SwDataDefProps,
    SwDataDependency,
    SwDataDependencyArgs,
    SwImplPolicyEnum,
    SwPointerTargetProps,
    SwTextProps,
    SwVariableRefProxy,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CONDITIONAL_ORDER = [
    "DISPLAY-PRESENTATION",
    "STEP-SIZE",
    "SW-VALUE-BLOCK-SIZE-MULTS",
    "ANNOTATIONS",
    "SW-ADDR-METHOD-REF",
    "SW-ALIGNMENT",
    "BASE-TYPE-REF",
    "SW-BIT-REPRESENTATION",
    "SW-CALIBRATION-ACCESS",
    "SW-VALUE-BLOCK-SIZE",
    "SW-CALPRM-AXIS-SET",
    "SW-TEXT-PROPS",
    "SW-COMPARISON-VARIABLES",
    "COMPU-METHOD-REF",
    "DATA-CONSTR-REF",
    "SW-DATA-DEPENDENCY",
    "DISPLAY-FORMAT",
    "IMPLEMENTATION-DATA-TYPE-REF",
    "SW-HOST-VARIABLE",
    "SW-IMPL-POLICY",
    "ADDITIONAL-NATIVE-TYPE-QUALIFIER",
    "SW-INTENDED-RESOLUTION",
    "SW-INTERPOLATION-METHOD",
    "INVALID-VALUE",
    "SW-IS-VIRTUAL",
    "SW-POINTER-TARGET-PROPS",
    "SW-RECORD-LAYOUT-REF",
    "SW-REFRESH-TIMING",
    "UNIT-REF",
    "VALUE-AXIS-DATA-TYPE-REF",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    return RefType().setDest(dest).setValue(value)


def _build_props():
    props = SwDataDefProps()
    props.setAdditionalNativeTypeQualifier(NativeDeclarationString().setValue("volatile"))
    annotation = Annotation()
    annotation.setAnnotationOrigin(String().setValue("sync-test"))
    props.addAnnotation(annotation)
    props.setBaseTypeRef(_ref("SW-BASE-TYPE", "/BaseTypes/uint8"))
    props.setCompuMethodRef(_ref("COMPU-METHOD", "/CompuMethods/cm"))
    props.setDataConstrRef(_ref("DATA-CONSTR", "/DataConstrs/dc"))
    props.setDisplayFormat(DisplayFormatString().setValue("%5.2f"))
    props.setDisplayPresentation(DisplayPresentationEnum().setValue(DisplayPresentationEnum.PRESENTATION_CONTINUOUS))
    props.setImplementationDataTypeRef(_ref("IMPLEMENTATION-DATA-TYPE", "/ImplementationDataTypes/idt"))
    invalid_value = NumericalValueSpecification()
    invalid_value.setValue(Numerical().setValue("42"))
    props.setInvalidValue(invalid_value)
    props.setStepSize(Float().setValue("0.5"))
    props.setSwAddrMethodRef(_ref("SW-ADDR-METHOD", "/SwAddrMethods/ram"))
    props.setSwAlignment(AlignmentType().setValue("8"))
    bit_repr = SwBitRepresentation()
    bit_repr.setBitPosition(Integer().setValue("3"))
    bit_repr.setNumberOfBits(Integer().setValue("5"))
    props.setSwBitRepresentation(bit_repr)
    props.setSwCalibrationAccess(SwCalibrationAccessEnum().setValue(SwCalibrationAccessEnum.READ_WRITE))
    axis_set = SwCalprmAxisSet()
    axis = SwCalprmAxis()
    axis.setSwAxisIndex(AxisIndexType().setValue("1"))
    axis_set.addSwCalprmAxis(axis)
    props.setSwCalprmAxisSet(axis_set)
    comparison = SwVariableRefProxy()
    comparison.setMcDataInstanceVarRef(_ref("MC-DATA-INSTANCE", "/McDataInstances/v"))
    props.addSwComparisonVariable(comparison)
    dependency = SwDataDependency()
    args = SwDataDependencyArgs()
    arg_variable = SwVariableRefProxy()
    arg_variable.setMcDataInstanceVarRef(_ref("MC-DATA-INSTANCE", "/McDataInstances/input1"))
    args.setSwVariable(arg_variable)
    dependency.setSwDataDependencyArgs(args)
    formula = CompuGenericMath()
    formula.setMixedString("input1 + input2")
    formula.setLevel(PrimitiveIdentifier().setValue("ASAMHDO"))
    dependency.setSwDataDependencyFormula(formula)
    props.setSwDataDependency(dependency)
    props.setSwHostVariable(SwVariableRefProxy().setMcDataInstanceVarRef(_ref("MC-DATA-INSTANCE", "/McDataInstances/host")))
    props.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.STANDARD))
    props.setSwIntendedResolution(Numerical().setValue("0.01"))
    props.setSwInterpolationMethod(Identifier().setValue("linear"))
    props.setSwIsVirtual(Boolean().setValue("true"))
    pointer_props = SwPointerTargetProps()
    pointer_props.setTargetCategory(Identifier().setValue("VALUE"))
    pointer_props.setFunctionPointerSignatureRef(_ref("BSW-MODULE-ENTRY", "/BswEntries/entry"))
    nested = SwDataDefProps()
    nested.setBaseTypeRef(_ref("SW-BASE-TYPE", "/BaseTypes/uint16"))
    pointer_props.setSwDataDefProps(nested)
    props.setSwPointerTargetProps(pointer_props)
    props.setSwRecordLayoutRef(_ref("SW-RECORD-LAYOUT", "/RecordLayouts/rl"))
    refresh_timing = MultidimensionalTime()
    refresh_timing.setCseCodeFactor(Integer().setValue("2"))
    props.setSwRefreshTiming(refresh_timing)
    text_props = SwTextProps()
    text_props.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE))
    text_props.setBaseTypeRef(_ref("SW-BASE-TYPE", "/BaseTypes/char"))
    text_props.setSwMaxTextSize(Integer().setValue("200"))
    props.setSwTextProps(text_props)
    props.setSwValueBlockSize(Numerical().setValue("16"))
    props.addSwValueBlockSizeMult(Numerical().setValue("3"))
    props.addSwValueBlockSizeMult(Numerical().setValue("5"))
    props.setUnitRef(_ref("UNIT", "/Units/second"))
    props.setValueAxisDataTypeRef(_ref("APPLICATION-PRIMITIVE-DATA-TYPE", "/ApplicationDataTypes/adt"))
    return props


def _save_and_reload():
    with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
        tmp_path = tmp.name
    try:
        ARXMLWriter().save(tmp_path, AUTOSAR.getInstance())
        with open(tmp_path, encoding="utf-8") as f:
            raw = f.read()
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        ARXMLParser().load(tmp_path, AUTOSAR.getInstance())
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
    return raw


def _build_owner():
    package = AUTOSAR.getInstance().createARPackage("DataDefProps")
    data_type = package.createImplementationDataType("MyDataType")
    data_type.setSwDataDefProps(_build_props())
    return data_type


def _conditional_tags(raw):
    root = ET.fromstring(raw)
    conditional = None
    for element in root.iter():
        if element.tag.split("}")[-1] == "SW-DATA-DEF-PROPS-CONDITIONAL":
            conditional = element
            break
    assert conditional is not None
    return [child.tag.split("}")[-1] for child in conditional]


class TestWriteSwDataDefProps:
    """Writer coverage for SW-DATA-DEF-PROPS (Table 5.39) + XSD element order."""

    def test_write_sw_data_def_props_element_order_follows_xsd(self):
        _build_owner()
        raw = _save_and_reload()
        tags = _conditional_tags(raw)
        assert tags == XSD_CONDITIONAL_ORDER

    def test_write_sw_data_def_props_roundtrip_scalar_attrs(self):
        _build_owner()
        _save_and_reload()
        data_type = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0]
        props = data_type.getSwDataDefProps()
        assert props is not None
        assert props.getAdditionalNativeTypeQualifier().getValue() == "volatile"
        assert props.getDisplayFormat().getValue() == "%5.2f"
        assert props.getDisplayPresentation().getValue() == "presentationContinuous"
        assert props.getStepSize().getValue() == 0.5
        assert props.getSwAlignment().getValue() == "8"
        assert props.getSwCalibrationAccess().getValue() == "readWrite"
        assert props.getSwImplPolicy().getValue() == "standard"
        assert props.getSwInterpolationMethod().getValue() == "linear"
        assert props.getSwIsVirtual().getValue() is True
        assert props.getSwIntendedResolution().getValue() == 0.01
        assert props.getSwValueBlockSize().getValue() == 16

    def test_write_sw_data_def_props_roundtrip_refs(self):
        _build_owner()
        _save_and_reload()
        props = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0].getSwDataDefProps()
        assert props.getBaseTypeRef().getValue() == "/BaseTypes/uint8"
        assert props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert props.getCompuMethodRef().getValue() == "/CompuMethods/cm"
        assert props.getDataConstrRef().getValue() == "/DataConstrs/dc"
        assert props.getImplementationDataTypeRef().getValue() == "/ImplementationDataTypes/idt"
        assert props.getSwAddrMethodRef().getValue() == "/SwAddrMethods/ram"
        assert props.getSwRecordLayoutRef().getValue() == "/RecordLayouts/rl"
        assert props.getUnitRef().getValue() == "/Units/second"
        assert props.getValueAxisDataTypeRef().getValue() == "/ApplicationDataTypes/adt"

    def test_write_sw_data_def_props_roundtrip_aggregates(self):
        _build_owner()
        _save_and_reload()
        props = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0].getSwDataDefProps()

        annotations = props.getAnnotations()
        assert len(annotations) == 1
        assert annotations[0].getAnnotationOrigin().getValue() == "sync-test"

        bit_repr = props.getSwBitRepresentation()
        assert bit_repr.getBitPosition().getValue() == 3
        assert bit_repr.getNumberOfBits().getValue() == 5

        assert [m.getValue() for m in props.getSwValueBlockSizeMults()] == [3, 5]

        axes = props.getSwCalprmAxisSet().getSwCalprmAxises()
        assert len(axes) == 1
        assert axes[0].getSwAxisIndex().getValue() == "1"

        text_props = props.getSwTextProps()
        assert text_props.getSwMaxTextSize().getValue() == 200
        assert text_props.getBaseTypeRef().getValue() == "/BaseTypes/char"

        assert len(props.getSwComparisonVariables()) == 1
        assert props.getSwComparisonVariables()[0].getMcDataInstanceVarRef().getValue() == "/McDataInstances/v"

        dependency = props.getSwDataDependency()
        assert dependency is not None
        assert dependency.getSwDataDependencyArgs().getSwVariable().getMcDataInstanceVarRef().getValue() == "/McDataInstances/input1"
        assert dependency.getSwDataDependencyFormula().getMixedString() == "input1 + input2"
        assert dependency.getSwDataDependencyFormula().getLevel().getValue() == "ASAMHDO"

        assert props.getSwHostVariable().getMcDataInstanceVarRef().getValue() == "/McDataInstances/host"

        assert props.getInvalidValue().getValue().getValue() == 42

        pointer_props = props.getSwPointerTargetProps()
        assert pointer_props.getTargetCategory().getValue() == "VALUE"
        assert pointer_props.getFunctionPointerSignatureRef().getValue() == "/BswEntries/entry"
        assert pointer_props.getSwDataDefProps().getBaseTypeRef().getValue() == "/BaseTypes/uint16"

        assert props.getSwRefreshTiming().getCseCodeFactor().getValue() == 2

    def test_no_props_emits_no_wrapper(self):
        package = AUTOSAR.getInstance().createARPackage("NoProps")
        package.createImplementationDataType("Bare")
        raw = _save_and_reload()
        assert "SW-DATA-DEF-PROPS" not in raw

    def test_write_sw_bit_representation_partial_fields_roundtrip(self):
        """Only NUMBER-OF-BITS set: BIT-POSITION absent from the XML and None after reload (Table 5.41, both attrs 0..1)."""
        package = AUTOSAR.getInstance().createARPackage("PartialBits")
        data_type = package.createImplementationDataType("Partial")
        props = SwDataDefProps()
        bit_repr = SwBitRepresentation()
        bit_repr.setNumberOfBits(Integer().setValue("5"))
        props.setSwBitRepresentation(bit_repr)
        data_type.setSwDataDefProps(props)
        raw = _save_and_reload()
        assert "BIT-POSITION" not in raw
        assert "NUMBER-OF-BITS" in raw
        reloaded = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0].getSwDataDefProps().getSwBitRepresentation()
        assert isinstance(reloaded, SwBitRepresentation)
        assert reloaded.getBitPosition() is None
        assert reloaded.getNumberOfBits().getValue() == 5

    def test_write_sw_bit_representation_empty_roundtrip(self):
        """An empty SwBitRepresentation emits the wrapper with no children and reloads with both fields None."""
        package = AUTOSAR.getInstance().createARPackage("EmptyBits")
        data_type = package.createImplementationDataType("Empty")
        props = SwDataDefProps()
        props.setSwBitRepresentation(SwBitRepresentation())
        data_type.setSwDataDefProps(props)
        raw = _save_and_reload()
        assert "SW-BIT-REPRESENTATION" in raw
        assert "BIT-POSITION" not in raw
        assert "NUMBER-OF-BITS" not in raw
        reloaded = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0].getSwDataDefProps().getSwBitRepresentation()
        assert isinstance(reloaded, SwBitRepresentation)
        assert reloaded.getBitPosition() is None
        assert reloaded.getNumberOfBits() is None

    def test_empty_props_roundtrip(self):
        package = AUTOSAR.getInstance().createARPackage("EmptyProps")
        data_type = package.createImplementationDataType("Empty")
        data_type.setSwDataDefProps(SwDataDefProps())
        _save_and_reload()
        data_type = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0]
        props = data_type.getSwDataDefProps()
        assert props is not None
        assert props.getBaseTypeRef() is None
        assert props.getAnnotations() == []
        assert props.getSwValueBlockSizeMults() == []
        assert props.getSwComparisonVariables() == []


class TestWriteSwDataDependencyArgs:
    """Writer coverage for SW-DATA-DEPENDENCY-ARGS (SWCT Table 5.59, p.374, R23-11).

    The atpMixed container writes the SW-CALPRM-REF-PROXY (AR-PARAMETER, MC-DATA-INSTANCE-REF)
    and SW-VARIABLE-REF-PROXY (AUTOSAR-VARIABLE, MC-DATA-INSTANCE-VAR-REF) group members
    inline under SW-DATA-DEPENDENCY-ARGS — no proxy-named wrapper elements.
    """

    def _build_args(self, args):
        package = AUTOSAR.getInstance().createARPackage("DataDependencyArgs")
        data_type = package.createImplementationDataType("ArgsDt")
        props = SwDataDefProps()
        dependency = SwDataDependency()
        dependency.setSwDataDependencyArgs(args)
        props.setSwDataDependency(dependency)
        data_type.setSwDataDefProps(props)
        return data_type

    def _args_element(self, raw):
        root = ET.fromstring(raw)
        for element in root.iter():
            if element.tag.split("}")[-1] == "SW-DATA-DEPENDENCY-ARGS":
                return element
        return None

    def test_write_sw_data_dependency_args_roundtrip_full_form(self):
        args = SwDataDependencyArgs()
        calprm = SwCalprmRefProxy()
        ar_parameter = AutosarParameterRef()
        ar_parameter.setLocalParameterRef(_ref("PARAMETER-DATA-PROTOTYPE", "/Pkg/paramA"))
        calprm.setArParameter(ar_parameter)
        calprm.setMcDataInstanceRef(_ref("MC-DATA-INSTANCE", "/McDataInstances/axis"))
        args.setSwCalprmRef(calprm)
        variable = SwVariableRefProxy()
        autosar_variable = AutosarVariableRef()
        autosar_variable.setLocalVariableRef(_ref("VARIABLE-DATA-PROTOTYPE", "/Pkg/varB"))
        variable.setAutosarVariable(autosar_variable)
        variable.setMcDataInstanceVarRef(_ref("MC-DATA-INSTANCE", "/McDataInstances/input1"))
        args.setSwVariable(variable)

        self._build_args(args)
        _save_and_reload()
        props = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0].getSwDataDefProps()
        reloaded = props.getSwDataDependency().getSwDataDependencyArgs()

        calprm = reloaded.getSwCalprmRef()
        assert isinstance(calprm, SwCalprmRefProxy)
        assert calprm.getArParameter().getLocalParameterRef().getValue() == "/Pkg/paramA"
        assert calprm.getArParameter().getLocalParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        assert calprm.getMcDataInstanceRef().getValue() == "/McDataInstances/axis"
        assert calprm.getMcDataInstanceRef().getDest() == "MC-DATA-INSTANCE"

        variable = reloaded.getSwVariable()
        assert isinstance(variable, SwVariableRefProxy)
        assert variable.getAutosarVariable().getLocalVariableRef().getValue() == "/Pkg/varB"
        assert variable.getAutosarVariable().getLocalVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert variable.getMcDataInstanceVarRef().getValue() == "/McDataInstances/input1"

    def test_write_sw_data_dependency_args_inline_group_order(self):
        args = SwDataDependencyArgs()
        calprm = SwCalprmRefProxy()
        ar_parameter = AutosarParameterRef()
        ar_parameter.setLocalParameterRef(_ref("PARAMETER-DATA-PROTOTYPE", "/Pkg/paramA"))
        calprm.setArParameter(ar_parameter)
        calprm.setMcDataInstanceRef(_ref("MC-DATA-INSTANCE", "/McDataInstances/axis"))
        args.setSwCalprmRef(calprm)
        variable = SwVariableRefProxy()
        autosar_variable = AutosarVariableRef()
        autosar_variable.setLocalVariableRef(_ref("VARIABLE-DATA-PROTOTYPE", "/Pkg/varB"))
        variable.setAutosarVariable(autosar_variable)
        variable.setMcDataInstanceVarRef(_ref("MC-DATA-INSTANCE", "/McDataInstances/input1"))
        args.setSwVariable(variable)

        self._build_args(args)
        raw = _save_and_reload()
        args_element = self._args_element(raw)
        assert args_element is not None
        tags = [child.tag.split("}")[-1] for child in args_element]
        assert tags == ["AR-PARAMETER", "MC-DATA-INSTANCE-REF", "AUTOSAR-VARIABLE", "MC-DATA-INSTANCE-VAR-REF"]
        assert "SW-CALPRM-REF-PROXY" not in raw
        assert "SW-VARIABLE-REF-PROXY" not in raw

    def test_write_sw_data_dependency_args_empty_container_roundtrip(self):
        """An empty SwDataDependencyArgs still emits its element (0..1 container) and reloads with both proxies None."""
        self._build_args(SwDataDependencyArgs())
        raw = _save_and_reload()
        args_element = self._args_element(raw)
        assert args_element is not None
        assert len(list(args_element)) == 0
        reloaded = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0].getSwDataDefProps().getSwDataDependency().getSwDataDependencyArgs()
        assert reloaded is not None
        assert reloaded.getSwCalprmRef() is None
        assert reloaded.getSwVariable() is None

    def test_write_no_args_emits_no_wrapper(self):
        package = AUTOSAR.getInstance().createARPackage("NoArgs")
        data_type = package.createImplementationDataType("NoArgsDt")
        props = SwDataDefProps()
        props.setSwDataDependency(SwDataDependency())
        data_type.setSwDataDefProps(props)
        raw = _save_and_reload()
        assert self._args_element(raw) is None


class TestWriteSwDataDependency:
    """Writer coverage for SW-DATA-DEPENDENCY (SWCT Table 5.58, p.374, R23-11).

    XSD child order inside SW-DATA-DEPENDENCY follows the sequenceOffsets —
    SW-DATA-DEPENDENCY-FORMULA (30) before SW-DATA-DEPENDENCY-ARGS (40) —
    independent of the class member order (markdown display: args row first).
    """

    def _dependency_element(self, raw):
        root = ET.fromstring(raw)
        for element in root.iter():
            if element.tag.split("}")[-1] == "SW-DATA-DEPENDENCY":
                return element
        return None

    def test_write_sw_data_dependency_child_order_follows_xsd(self):
        package = AUTOSAR.getInstance().createARPackage("DataDependency")
        data_type = package.createImplementationDataType("DependencyDt")
        props = SwDataDefProps()
        dependency = SwDataDependency()
        dependency.setSwDataDependencyArgs(SwDataDependencyArgs())
        formula = CompuGenericMath()
        formula.setMixedString("input1 + input2")
        formula.setLevel(PrimitiveIdentifier().setValue("ASAMHDO"))
        dependency.setSwDataDependencyFormula(formula)
        props.setSwDataDependency(dependency)
        data_type.setSwDataDefProps(props)
        raw = _save_and_reload()
        dependency_element = self._dependency_element(raw)
        assert dependency_element is not None
        tags = [child.tag.split("}")[-1] for child in dependency_element]
        assert tags == ["SW-DATA-DEPENDENCY-FORMULA", "SW-DATA-DEPENDENCY-ARGS"]

    def test_write_sw_data_dependency_formula_only_roundtrip(self):
        package = AUTOSAR.getInstance().createARPackage("FormulaOnly")
        data_type = package.createImplementationDataType("FormulaDt")
        props = SwDataDefProps()
        dependency = SwDataDependency()
        formula = CompuGenericMath()
        formula.setMixedString("B = sqrt(1 - A*A)")
        formula.setLevel(PrimitiveIdentifier().setValue("INFORMAL"))
        dependency.setSwDataDependencyFormula(formula)
        props.setSwDataDependency(dependency)
        data_type.setSwDataDefProps(props)
        _save_and_reload()
        reloaded = AUTOSAR.getInstance().getARPackages()[0].getImplementationDataTypes()[0].getSwDataDefProps().getSwDataDependency()
        assert reloaded is not None
        assert reloaded.getSwDataDependencyArgs() is None
        formula = reloaded.getSwDataDependencyFormula()
        assert isinstance(formula, CompuGenericMath)
        assert formula.getMixedString() == "B = sqrt(1 - A*A)"
        assert formula.getLevel().getValue() == "INFORMAL"
