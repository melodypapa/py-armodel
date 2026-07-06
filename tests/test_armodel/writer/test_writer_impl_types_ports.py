"""Tests for writer implementation types, port interfaces, and mappings."""
import xml.etree.cElementTree as ET
from unittest.mock import MagicMock
import pytest

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    AUTOSAR,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARBoolean,
    ARFloat,
    RefType,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import (
    SwcBswMapping,
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Code,
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ImplementationDataType,
    ImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    SymbolProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    DataTypeMap,
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeDeclaration,
    ModeDeclarationGroup,
    ModeRequestTypeMap,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    SwRecordLayout,
    SwRecordLayoutGroup,
    SwRecordLayoutGroupContent,
    SwRecordLayoutV,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import (
    SwcTiming,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRef,
    ExecutionOrderConstraint,
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


@pytest.fixture
def warning_writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter(options={"warning": True})


def _parent():
    return ET.Element("PARENT")


def _make_ref(value, dest="REF-TYPE"):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _make_literal(text):
    literal = ARLiteral()
    literal.setValue(text)
    return literal


def _make_bool(text):
    val = ARBoolean()
    val.setValue(text)
    return val


def _make_float(num, text):
    val = ARFloat()
    val.setValue(num)
    val._text = text
    return val


class TestSwcBswMappingWriter:
    """Tests for SWC-BSW mapping writer methods."""

    def test_set_swc_bsw_runnable_mapping(self, writer):
        mapping = SwcBswRunnableMapping()
        mapping.setBswEntityRef(_make_ref("/Bsw/Entity", "BSW"))
        mapping.setSwcRunnableRef(_make_ref("/Swc/Run", "RUNNABLE"))

        parent = _parent()
        writer.setSwcBswRunnableMapping(parent, mapping)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SWC-BSW-RUNNABLE-MAPPING"
        bsw_ref = child.find("BSW-ENTITY-REF")
        assert bsw_ref is not None
        assert bsw_ref.text == "/Bsw/Entity"
        swc_ref = child.find("SWC-RUNNABLE-REF")
        assert swc_ref is not None
        assert swc_ref.text == "/Swc/Run"

    def test_set_swc_bsw_runnable_mapping_no_refs(self, writer):
        mapping = SwcBswRunnableMapping()
        parent = _parent()
        writer.setSwcBswRunnableMapping(parent, mapping)

        child = parent[0]
        assert child.tag == "SWC-BSW-RUNNABLE-MAPPING"
        assert child.find("BSW-ENTITY-REF") is None
        assert child.find("SWC-RUNNABLE-REF") is None

    def test_write_swc_bsw_runnable_mappings(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping = pkg.createSwcBswMapping("Map")
        runnable_map = SwcBswRunnableMapping()
        runnable_map.setBswEntityRef(_make_ref("/Bsw", "BSW"))
        mapping.addRunnableMapping(runnable_map)

        parent = _parent()
        writer.writeSwcBswRunnableMappings(parent, mapping)

        assert len(parent) == 1
        assert parent[0].tag == "RUNNABLE-MAPPINGS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "SWC-BSW-RUNNABLE-MAPPING"

    def test_write_swc_bsw_runnable_mappings_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping = pkg.createSwcBswMapping("Map")

        parent = _parent()
        writer.writeSwcBswRunnableMappings(parent, mapping)
        assert len(parent) == 0

    def test_write_swc_bsw_runnable_mappings_unsupported(
        self, warning_writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping = pkg.createSwcBswMapping("Map")
        mapping.addRunnableMapping("not-a-mapping")

        parent = _parent()
        warning_writer.writeSwcBswRunnableMappings(parent, mapping)
        assert parent[0].tag == "RUNNABLE-MAPPINGS"
        assert len(parent[0]) == 0

    def test_write_swc_bsw_mapping(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping = pkg.createSwcBswMapping("SwcBswMap")
        mapping.setBswBehaviorRef(_make_ref("/Bsw/Beh", "BSW"))
        mapping.setSwcBehaviorRef(_make_ref("/Swc/Beh", "SWC"))
        runnable_map = SwcBswRunnableMapping()
        mapping.addRunnableMapping(runnable_map)

        parent = _parent()
        writer.writeSwcBswMapping(parent, mapping)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SWC-BSW-MAPPING"
        assert child.find("SHORT-NAME").text == "SwcBswMap"
        assert child.find("BSW-BEHAVIOR-REF").text == "/Bsw/Beh"
        assert child.find("SWC-BEHAVIOR-REF").text == "/Swc/Beh"
        assert child.find("RUNNABLE-MAPPINGS") is not None


class TestEngineeringObjectWriter:
    """Tests for engineering object and BSW implementation writers."""

    def test_write_engineering_object(self, writer):
        obj = AutosarEngineeringObject()
        obj.setShortLabel(_make_literal("label"))
        obj.setCategory(_make_literal("cat"))

        parent = _parent()
        writer.writeEngineeringObject(parent, obj)

        assert parent.find("SHORT-LABEL").text == "label"
        assert parent.find("CATEGORY").text == "cat"

    def test_write_engineering_object_no_fields(self, writer):
        obj = AutosarEngineeringObject()
        parent = _parent()
        writer.writeEngineeringObject(parent, obj)
        assert parent.find("SHORT-LABEL") is None
        assert parent.find("CATEGORY") is None

    def test_write_autosar_engineering_object(self, writer):
        obj = AutosarEngineeringObject()
        obj.setShortLabel(_make_literal("lbl"))

        parent = _parent()
        writer.writeAutosarEngineeringObject(parent, obj)

        assert len(parent) == 1
        assert parent[0].tag == "AUTOSAR-ENGINEERING-OBJECT"
        assert parent[0].find("SHORT-LABEL").text == "lbl"

    def test_write_artifact_descriptor(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        code = Code(pkg, "Code")
        obj = AutosarEngineeringObject()
        obj.setShortLabel(_make_literal("lbl"))
        code.addArtifactDescriptor(obj)

        parent = _parent()
        writer.writeArtifactDescriptor(parent, code)

        assert len(parent) == 1
        assert parent[0].tag == "ARTIFACT-DESCRIPTORS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "AUTOSAR-ENGINEERING-OBJECT"

    def test_write_artifact_descriptor_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        code = Code(pkg, "Code")

        parent = _parent()
        writer.writeArtifactDescriptor(parent, code)
        assert len(parent) == 0

    def test_write_artifact_descriptor_unsupported(self, warning_writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        code = Code(pkg, "Code")
        code.addArtifactDescriptor("not-an-object")

        parent = _parent()
        warning_writer.writeArtifactDescriptor(parent, code)
        assert parent[0].tag == "ARTIFACT-DESCRIPTORS"
        assert len(parent[0]) == 0

    def test_write_bsw_impl_vendor_specific_refs(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = pkg.createBswImplementation("BswImpl")
        impl.addVendorSpecificModuleDefRef(
            _make_ref("/Vend/Mod", "BSW-MODULE-DEF")
        )

        parent = _parent()
        writer.writeBswImplementationVendorSpecificModuleDefRefs(
            parent, impl
        )

        assert len(parent) == 1
        assert parent[0].tag == "VENDOR-SPECIFIC-MODULE-DEF-REFS"
        ref = parent[0].find("VENDOR-SPECIFIC-MODULE-DEF-REF")
        assert ref is not None
        assert ref.text == "/Vend/Mod"

    def test_write_bsw_impl_vendor_specific_refs_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = pkg.createBswImplementation("BswImpl")

        parent = _parent()
        writer.writeBswImplementationVendorSpecificModuleDefRefs(
            parent, impl
        )
        assert len(parent) == 0

    def test_write_bsw_implementation(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = pkg.createBswImplementation("BswImpl")
        version = RevisionLabelString()
        version.setValue("R23-11")
        impl.setArReleaseVersion(version)
        impl.setBehaviorRef(_make_ref("/Beh", "BSW"))
        impl.setVendorApiInfix(_make_literal("Api"))
        impl.addVendorSpecificModuleDefRef(
            _make_ref("/Vend/Mod", "BSW-MODULE-DEF")
        )
        impl.swVersion = None
        impl.vendorId = None

        parent = _parent()
        writer.writeBswImplementation(parent, impl)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "BSW-IMPLEMENTATION"
        assert child.find("SHORT-NAME").text == "BswImpl"
        assert child.find("AR-RELEASE-VERSION").text == "R23-11"
        assert child.find("BEHAVIOR-REF").text == "/Beh"
        assert child.find("VENDOR-API-INFIX").text == "Api"
        assert child.find(
            "VENDOR-SPECIFIC-MODULE-DEF-REFS"
        ) is not None


class TestImplementationDataTypeWriter:
    """Tests for implementation data type writer methods."""

    def test_write_abstract_impl_data_type_element(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        elem = ImplementationDataTypeElement(pkg, "Elem")

        parent = _parent()
        writer.writeAbstractImplementationDataTypeElement(
            parent, elem
        )
        assert parent.find("SHORT-NAME").text == "Elem"

    def test_write_impl_data_type_element_sub_elements(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        parent_elem = ImplementationDataTypeElement(pkg, "Parent")
        parent_elem.createImplementationDataTypeElement("Child")

        parent = _parent()
        writer.writeImplementationDataTypeElementSubElements(
            parent, parent_elem
        )

        assert len(parent) == 1
        assert parent[0].tag == "SUB-ELEMENTS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

    def test_write_impl_data_type_element_sub_elements_empty(
        self, writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        parent_elem = ImplementationDataTypeElement(pkg, "Parent")

        parent = _parent()
        writer.writeImplementationDataTypeElementSubElements(
            parent, parent_elem
        )
        assert len(parent) == 0

    def test_write_impl_data_type_element_sub_elements_unsupported(
        self, warning_writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        parent_elem = ImplementationDataTypeElement(pkg, "Parent")
        parent_elem.subElements.append("not-an-element")

        parent = _parent()
        warning_writer.writeImplementationDataTypeElementSubElements(
            parent, parent_elem
        )
        assert parent[0].tag == "SUB-ELEMENTS"
        assert len(parent[0]) == 0

    def test_write_impl_data_type_element(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        elem = ImplementationDataTypeElement(pkg, "Elem")
        elem.setArraySize(_make_float(4, "4"))
        elem.setArraySizeHandling(_make_literal("handling"))
        elem.setArraySizeSemantics(_make_literal("semantics"))
        elem.createImplementationDataTypeElement("Sub")

        parent = _parent()
        writer.writeImplementationDataTypeElement(parent, elem)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert child.find("SHORT-NAME").text == "Elem"
        assert child.find("ARRAY-SIZE").text == "4"
        assert child.find("ARRAY-SIZE-HANDLING").text == "handling"
        assert child.find("ARRAY-SIZE-SEMANTICS").text == "semantics"
        assert child.find("SUB-ELEMENTS") is not None

    def test_write_impl_data_type_sub_elements(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        data_type.createImplementationDataTypeElement("Sub")

        parent = _parent()
        writer.writeImplementationDataTypeSubElements(
            parent, data_type
        )

        assert len(parent) == 1
        assert parent[0].tag == "SUB-ELEMENTS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

    def test_write_impl_data_type_sub_elements_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")

        parent = _parent()
        writer.writeImplementationDataTypeSubElements(
            parent, data_type
        )
        assert len(parent) == 0

    def test_write_impl_data_type_sub_elements_unsupported(
        self, warning_writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        data_type.subElements.append("not-an-element")

        parent = _parent()
        warning_writer.writeImplementationDataTypeSubElements(
            parent, data_type
        )
        assert parent[0].tag == "SUB-ELEMENTS"
        assert len(parent[0]) == 0

    def test_write_implementation_props(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        props = data_type.createSymbolProps("Sym")
        props.setSymbol(_make_literal("symbol"))

        parent = _parent()
        writer.writeImplementationProps(parent, props)

        assert parent.find("SHORT-NAME").text == "Sym"
        assert parent.find("SYMBOL").text == "symbol"

    def test_write_symbol_props(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        props = data_type.createSymbolProps("Sym")
        props.setSymbol(_make_literal("sym"))

        parent = _parent()
        writer.writeSymbolProps(parent, props)

        assert len(parent) == 1
        assert parent[0].tag == "SYMBOL-PROPS"
        assert parent[0].find("SHORT-NAME").text == "Sym"
        assert parent[0].find("SYMBOL").text == "sym"

    def test_write_symbol_props_none(self, writer):
        parent = _parent()
        writer.writeSymbolProps(parent, None)
        assert len(parent) == 0

    def test_write_impl_data_type_symbol_props(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        props = data_type.createSymbolProps("Sym")
        props.setSymbol(_make_literal("sym"))

        parent = _parent()
        writer.writeImplementationDataTypeSymbolProps(
            parent, data_type
        )

        assert len(parent) == 1
        assert parent[0].tag == "SYMBOL-PROPS"

    def test_write_impl_data_type_symbol_props_none(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")

        parent = _parent()
        writer.writeImplementationDataTypeSymbolProps(
            parent, data_type
        )
        assert len(parent) == 0

    def test_write_implementation_data_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        data_type.setDynamicArraySizeProfile(_make_literal("prof"))
        data_type.typeEmitter = _make_literal("Emitter")
        data_type.createImplementationDataTypeElement("Sub")
        props = data_type.createSymbolProps("Sym")
        props.setSymbol(_make_literal("sym"))

        parent = _parent()
        writer.writeImplementationDataType(parent, data_type)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "IMPLEMENTATION-DATA-TYPE"
        assert child.find("SHORT-NAME").text == "ImplType"
        assert child.find(
            "DYNAMIC-ARRAY-SIZE-PROFILE"
        ).text == "prof"
        assert child.find("TYPE-EMITTER").text == "Emitter"
        assert child.find("SYMBOL-PROPS") is not None
        assert child.find("SUB-ELEMENTS") is not None


class TestClientServerOperationWriter:
    """Tests for client/server operation writer methods."""

    def test_write_argument_data_prototype(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        op = cs_if.createOperation("Op")
        arg = op.createArgumentDataPrototype("Arg")
        arg.setDirection(_make_literal("IN"))
        arg.setServerArgumentImplPolicy(_make_literal("policy"))

        parent = _parent()
        writer.writeArgumentDataPrototype(parent, arg)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "ARGUMENT-DATA-PROTOTYPE"
        assert child.find("SHORT-NAME").text == "Arg"
        assert child.find("DIRECTION").text == "IN"
        assert child.find(
            "SERVER-ARGUMENT-IMPL-POLICY"
        ).text == "policy"

    def test_write_cs_operation_arguments(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        op = cs_if.createOperation("Op")
        op.createArgumentDataPrototype("Arg")

        parent = _parent()
        writer.writeClientServerOperationArguments(parent, op)

        assert len(parent) == 1
        assert parent[0].tag == "ARGUMENTS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "ARGUMENT-DATA-PROTOTYPE"

    def test_write_cs_operation_arguments_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        op = cs_if.createOperation("Op")

        parent = _parent()
        writer.writeClientServerOperationArguments(parent, op)
        assert len(parent) == 0

    def test_write_cs_operation_arguments_unsupported(
        self, warning_writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        op = cs_if.createOperation("Op")
        op.arguments.append("not-an-arg")

        parent = _parent()
        warning_writer.writeClientServerOperationArguments(parent, op)
        assert parent[0].tag == "ARGUMENTS"
        assert len(parent[0]) == 0

    def test_write_cs_operation_possible_error_refs(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        op = cs_if.createOperation("Op")
        op.addPossibleErrorRef(_make_ref("/Err", "APPLICATION-ERROR"))

        parent = _parent()
        writer.writeClientServerOperationPossibleErrorRefs(parent, op)

        assert len(parent) == 1
        assert parent[0].tag == "POSSIBLE-ERROR-REFS"
        ref = parent[0].find("POSSIBLE-ERROR-REF")
        assert ref is not None
        assert ref.text == "/Err"

    def test_write_cs_operation_possible_error_refs_empty(
        self, writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        op = cs_if.createOperation("Op")

        parent = _parent()
        writer.writeClientServerOperationPossibleErrorRefs(parent, op)
        assert len(parent) == 0

    def test_write_client_server_operation(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        op = cs_if.createOperation("Op")
        op.createArgumentDataPrototype("Arg")
        op.addPossibleErrorRef(_make_ref("/Err", "APPLICATION-ERROR"))

        parent = _parent()
        writer.writeClientServerOperation(parent, op)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CLIENT-SERVER-OPERATION"
        assert child.find("SHORT-NAME").text == "Op"
        assert child.find("ARGUMENTS") is not None
        assert child.find("POSSIBLE-ERROR-REFS") is not None

    def test_write_cs_interface_operations(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        cs_if.createOperation("Op")

        parent = _parent()
        writer.writeClientServerInterfaceOperations(parent, cs_if)

        assert len(parent) == 1
        assert parent[0].tag == "OPERATIONS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "CLIENT-SERVER-OPERATION"

    def test_write_cs_interface_operations_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")

        parent = _parent()
        writer.writeClientServerInterfaceOperations(parent, cs_if)
        assert len(parent) == 0

    def test_write_cs_interface_operations_unsupported(
        self, warning_writer
    ):
        mock_if = MagicMock()
        mock_if.getOperations.return_value = ["not-an-op"]

        parent = _parent()
        warning_writer.writeClientServerInterfaceOperations(
            parent, mock_if
        )
        assert parent[0].tag == "OPERATIONS"
        assert len(parent[0]) == 0


class TestPortInterfaceWriter:
    """Tests for port interface writer methods."""

    def test_write_application_error(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        error = cs_if.createApplicationError("Err")
        error.error_code = _make_float(42, "42")

        parent = _parent()
        writer.writeApplicationError(parent, error)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-ERROR"
        assert child.find("SHORT-NAME").text == "Err"
        assert child.find("ERROR-CODE").text == "42"

    def test_write_application_error_no_code(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        error = cs_if.createApplicationError("Err")

        parent = _parent()
        writer.writeApplicationError(parent, error)
        assert parent[0].tag == "APPLICATION-ERROR"
        assert parent[0].find("ERROR-CODE") is None

    def test_write_possible_errors(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        cs_if.createApplicationError("Err")

        parent = _parent()
        writer.writePossibleErrors(parent, cs_if)

        assert len(parent) == 1
        assert parent[0].tag == "POSSIBLE-ERRORS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "APPLICATION-ERROR"

    def test_write_possible_errors_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")

        parent = _parent()
        writer.writePossibleErrors(parent, cs_if)
        assert len(parent) == 0

    def test_write_possible_errors_unsupported(self, warning_writer):
        mock_if = MagicMock()
        mock_if.getPossibleErrors.return_value = ["not-an-error"]

        parent = _parent()
        warning_writer.writePossibleErrors(parent, mock_if)
        assert parent[0].tag == "POSSIBLE-ERRORS"
        assert len(parent[0]) == 0

    def test_write_port_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        cs_if.setIsService(_make_bool("true"))
        cs_if.setServiceKind(_make_literal("SERVICE"))

        parent = _parent()
        writer.writePortInterface(parent, cs_if)

        assert parent.find("SHORT-NAME").text == "CsIf"
        assert parent.find("IS-SERVICE").text == "true"
        assert parent.find("SERVICE-KIND").text == "SERVICE"

    def test_write_data_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        nv_if = pkg.createNvDataInterface("NvIf")

        parent = _parent()
        writer.writeDataInterface(parent, nv_if)
        assert parent.find("SHORT-NAME").text == "NvIf"

    def test_write_parameter_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        param_if = pkg.createParameterInterface("ParamIf")

        parent = _parent()
        writer.writeParameterInterface(parent, param_if)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "PARAMETER-INTERFACE"
        assert child.find("SHORT-NAME").text == "ParamIf"

    def test_write_nv_data_interface_nv_datas(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        nv_if = pkg.createNvDataInterface("NvIf")
        nv_if.createNvData("NvBlock")

        parent = _parent()
        writer.writeNvDataInterfaceNvDatas(parent, nv_if)

        assert len(parent) == 1
        assert parent[0].tag == "NV-DATAS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "VARIABLE-DATA-PROTOTYPE"

    def test_write_nv_data_interface_nv_datas_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        nv_if = pkg.createNvDataInterface("NvIf")

        parent = _parent()
        writer.writeNvDataInterfaceNvDatas(parent, nv_if)
        assert len(parent) == 0

    def test_write_nv_data_interface_nv_datas_unsupported(
        self, warning_writer
    ):
        mock_if = MagicMock()
        mock_if.getNvDatas.return_value = ["not-a-nvdata"]

        parent = _parent()
        warning_writer.writeNvDataInterfaceNvDatas(parent, mock_if)
        assert parent[0].tag == "NV-DATAS"
        assert len(parent[0]) == 0

    def test_write_nv_data_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        nv_if = pkg.createNvDataInterface("NvIf")
        nv_if.createNvData("NvBlock")

        parent = _parent()
        writer.writeNvDataInterface(parent, nv_if)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "NV-DATA-INTERFACE"
        assert child.find("SHORT-NAME").text == "NvIf"
        assert child.find("NV-DATAS") is not None

    def test_write_client_server_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        cs_if = pkg.createClientServerInterface("CsIf")
        cs_if.createOperation("Op")
        cs_if.createApplicationError("Err")

        parent = _parent()
        writer.writeClientServerInterface(parent, cs_if)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CLIENT-SERVER-INTERFACE"
        assert child.find("SHORT-NAME").text == "CsIf"
        assert child.find("OPERATIONS") is not None
        assert child.find("POSSIBLE-ERRORS") is not None


class TestSwComponentWriter:
    """Tests for SW component type writer methods."""

    def test_write_application_sw_component_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        swc = pkg.createApplicationSwComponentType("AppSwc")

        parent = _parent()
        writer.writeApplicationSwComponentType(parent, swc)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-SW-COMPONENT-TYPE"
        assert child.find("SHORT-NAME").text == "AppSwc"

    def test_write_ecu_abstraction_sw_component_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        swc = pkg.createEcuAbstractionSwComponentType("EcuSwc")

        parent = _parent()
        writer.writeEcuAbstractionSwComponentType(parent, swc)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "ECU-ABSTRACTION-SW-COMPONENT-TYPE"
        assert child.find("SHORT-NAME").text == "EcuSwc"

    def test_set_application_array_element(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        array_type = pkg.createApplicationArrayDataType("ArrType")
        elem = array_type.createApplicationArrayElement("Elem")
        elem.setArraySizeHandling(_make_literal("handling"))
        elem.setArraySizeSemantics(_make_literal("semantics"))
        elem.setMaxNumberOfElements(_make_float(8, "8"))

        parent = _parent()
        writer.setApplicationArrayElement(parent, elem)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "ELEMENT"
        assert child.find("SHORT-NAME").text == "Elem"
        assert child.find("ARRAY-SIZE-HANDLING").text == "handling"
        assert child.find("ARRAY-SIZE-SEMANTICS").text == "semantics"
        assert child.find(
            "MAX-NUMBER-OF-ELEMENTS"
        ).text == "8"

    def test_set_application_array_element_none(self, writer):
        parent = _parent()
        writer.setApplicationArrayElement(parent, None)
        assert len(parent) == 0

    def test_write_application_array_data_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        array_type = pkg.createApplicationArrayDataType("ArrType")
        array_type.setDynamicArraySizeProfile(
            _make_literal("profile")
        )
        array_type.createApplicationArrayElement("Elem")

        parent = _parent()
        writer.writeApplicationArrayDataType(parent, array_type)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-ARRAY-DATA-TYPE"
        assert child.find("SHORT-NAME").text == "ArrType"
        assert child.find(
            "DYNAMIC-ARRAY-SIZE-PROFILE"
        ).text == "profile"
        assert child.find("ELEMENT") is not None


class TestSwRecordLayoutWriter:
    """Tests for SW record layout and address method writers."""

    def test_set_sw_record_layout_v(self, writer):
        layout_v = SwRecordLayoutV()
        layout_v.setShortLabel(_make_literal("lbl"))
        layout_v.setBaseTypeRef(_make_ref("/BT", "SW-BASE-TYPE"))
        layout_v.swRecordLayoutVAxis = _make_float(1, "1")
        layout_v.swRecordLayoutVProp = _make_literal("prop")
        layout_v.swRecordLayoutVIndex = _make_literal("idx")

        parent = _parent()
        writer.setSwRecordLayoutV(parent, "SW-RECORD-LAYOUT-V", layout_v)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-RECORD-LAYOUT-V"
        assert child.find("SHORT-LABEL").text == "lbl"
        assert child.find("BASE-TYPE-REF").text == "/BT"
        assert child.find("SW-RECORD-LAYOUT-V-AXIS").text == "1"
        assert child.find("SW-RECORD-LAYOUT-V-PROP").text == "prop"
        assert child.find("SW-RECORD-LAYOUT-V-INDEX").text == "idx"

    def test_set_sw_record_layout_v_none(self, writer):
        parent = _parent()
        writer.setSwRecordLayoutV(parent, "SW-RECORD-LAYOUT-V", None)
        assert len(parent) == 0

    def test_set_sw_record_layout_group(self, writer):
        group = SwRecordLayoutGroup()
        group.setShortLabel(_make_literal("lbl"))
        group.setCategory(_make_literal("cat"))
        group.swRecordLayoutGroupAxis = _make_float(2, "2")
        group.swRecordLayoutGroupIndex = _make_literal("idx")
        group.swRecordLayoutGroupFrom = _make_literal("from")
        group.swRecordLayoutGroupTo = _make_literal("to")
        group.swRecordLayoutGroupStep = _make_float(3, "3")
        group.swRecordLayoutGroupContentType = (
            SwRecordLayoutGroupContent()
        )

        parent = _parent()
        writer.setSwRecordLayoutGroup(
            parent, "SW-RECORD-LAYOUT-GROUP", group
        )

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-RECORD-LAYOUT-GROUP"
        assert child.find("SHORT-LABEL").text == "lbl"
        assert child.find("CATEGORY").text == "cat"
        assert child.find(
            "SW-RECORD-LAYOUT-GROUP-AXIS"
        ).text == "2"
        assert child.find(
            "SW-RECORD-LAYOUT-GROUP-INDEX"
        ).text == "idx"
        assert child.find(
            "SW-RECORD-LAYOUT-GROUP-FROM"
        ).text == "from"
        assert child.find(
            "SW-RECORD-LAYOUT-GROUP-TO"
        ).text == "to"
        assert child.find(
            "SW-RECORD-LAYOUT-GROUP-STEP"
        ).text == "3"

    def test_set_sw_record_layout_group_none(self, writer):
        parent = _parent()
        writer.setSwRecordLayoutGroup(
            parent, "SW-RECORD-LAYOUT-GROUP", None
        )
        assert len(parent) == 0

    def test_write_sw_record_layout_group_content_type(self, writer):
        group = SwRecordLayoutGroup()
        content = SwRecordLayoutGroupContent()
        sub_group = SwRecordLayoutGroup()
        sub_group.setShortLabel(_make_literal("sub"))
        sub_group.swRecordLayoutGroupContentType = (
            SwRecordLayoutGroupContent()
        )
        content.setSwRecordLayoutGroup(sub_group)
        layout_v = SwRecordLayoutV()
        layout_v.setShortLabel(_make_literal("v"))
        content.setSwRecordLayoutV(layout_v)
        group.swRecordLayoutGroupContentType = content

        parent = _parent()
        writer.writeSwRecordLayoutGroupSwRecordLayoutGroupContentType(
            parent, group
        )

        assert parent.find("SW-RECORD-LAYOUT-GROUP") is not None
        assert parent.find("SW-RECORD-LAYOUT-V") is not None

    def test_write_sw_record_layout(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        layout = pkg.createSwRecordLayout("Layout")
        group = SwRecordLayoutGroup()
        group.setShortLabel(_make_literal("grp"))
        group.swRecordLayoutGroupContentType = (
            SwRecordLayoutGroupContent()
        )
        layout.setSwRecordLayoutGroup(group)

        parent = _parent()
        writer.writeSwRecordLayout(parent, layout)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-RECORD-LAYOUT"
        assert child.find("SHORT-NAME").text == "Layout"
        assert child.find("SW-RECORD-LAYOUT-GROUP") is not None

    def test_write_sw_addr_method(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        method = pkg.createSwAddrMethod("Method")
        method.setMemoryAllocationKeywordPolicy(
            _make_literal("policy")
        )
        method.addOption(_make_literal("opt1"))
        method.addOption(_make_literal("opt2"))
        method.setSectionInitializationPolicy(_make_literal("init"))
        method.setSectionType(_make_literal("section"))

        parent = _parent()
        writer.writeSwAddrMethod(parent, method)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-ADDR-METHOD"
        assert child.find("SHORT-NAME").text == "Method"
        assert child.find(
            "MEMORY-ALLOCATION-KEYWORD-POLICY"
        ).text == "policy"
        options = child.find("OPTIONS")
        assert options is not None
        assert len(options) == 2
        assert child.find(
            "SECTION-INITIALIZATION-POLICY"
        ).text == "init"
        assert child.find("SECTION-TYPE").text == "section"

    def test_write_sw_addr_method_no_options(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        method = pkg.createSwAddrMethod("Method")

        parent = _parent()
        writer.writeSwAddrMethod(parent, method)

        child = parent[0]
        assert child.tag == "SW-ADDR-METHOD"
        assert child.find("OPTIONS") is None

    def test_write_trigger_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        trigger_if = pkg.createTriggerInterface("TrigIf")

        parent = _parent()
        writer.writeTriggerInterface(parent, trigger_if)
        assert len(parent) == 0

    def test_write_service_sw_component_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        swc = pkg.createServiceSwComponentType("SvcSwc")

        parent = _parent()
        writer.writeServiceSwComponentType(parent, swc)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SERVICE-SW-COMPONENT-TYPE"
        assert child.find("SHORT-NAME").text == "SvcSwc"


class TestDataTypeMappingWriter:
    """Tests for data type mapping set writer methods."""

    def test_write_data_type_maps(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping_set = pkg.createDataTypeMappingSet("MapSet")
        data_map = DataTypeMap()
        data_map.timestamp = None
        data_map.uuid = None
        data_map.setApplicationDataTypeRef(
            _make_ref("/App", "APPLICATION-DATA-TYPE")
        )
        data_map.setImplementationDataTypeRef(
            _make_ref("/Impl", "IMPLEMENTATION-DATA-TYPE")
        )
        mapping_set.addDataTypeMap(data_map)

        parent = _parent()
        writer.writeDataTypeMaps(parent, mapping_set)

        assert len(parent) == 1
        assert parent[0].tag == "DATA-TYPE-MAPS"
        assert len(parent[0]) == 1
        dt_map = parent[0][0]
        assert dt_map.tag == "DATA-TYPE-MAP"
        assert dt_map.find(
            "APPLICATION-DATA-TYPE-REF"
        ).text == "/App"
        assert dt_map.find(
            "IMPLEMENTATION-DATA-TYPE-REF"
        ).text == "/Impl"

    def test_write_data_type_maps_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping_set = pkg.createDataTypeMappingSet("MapSet")

        parent = _parent()
        writer.writeDataTypeMaps(parent, mapping_set)
        assert len(parent) == 0

    def test_write_mode_request_type_maps(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping_set = pkg.createDataTypeMappingSet("MapSet")
        mode_map = ModeRequestTypeMap()
        mode_map.setImplementationDataTypeRef(
            _make_ref("/Impl", "IMPLEMENTATION-DATA-TYPE")
        )
        mode_map.setModeGroupRef(
            _make_ref("/Mode", "MODE-DECLARATION-GROUP")
        )
        mapping_set.addModeRequestTypeMap(mode_map)

        parent = _parent()
        writer.writeModeRequestTypeMaps(parent, mapping_set)

        assert len(parent) == 1
        assert parent[0].tag == "MODE-REQUEST-TYPE-MAPS"
        assert len(parent[0]) == 1
        mr_map = parent[0][0]
        assert mr_map.tag == "MODE-REQUEST-TYPE-MAP"
        assert mr_map.find(
            "IMPLEMENTATION-DATA-TYPE-REF"
        ).text == "/Impl"
        assert mr_map.find("MODE-GROUP-REF").text == "/Mode"

    def test_write_mode_request_type_maps_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping_set = pkg.createDataTypeMappingSet("MapSet")

        parent = _parent()
        writer.writeModeRequestTypeMaps(parent, mapping_set)
        assert len(parent) == 0

    def test_write_data_type_mapping_set(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mapping_set = pkg.createDataTypeMappingSet("MapSet")
        data_map = DataTypeMap()
        data_map.timestamp = None
        data_map.uuid = None
        data_map.setApplicationDataTypeRef(
            _make_ref("/App", "APPLICATION-DATA-TYPE")
        )
        mapping_set.addDataTypeMap(data_map)
        mode_map = ModeRequestTypeMap()
        mapping_set.addModeRequestTypeMap(mode_map)

        parent = _parent()
        writer.writeDataTypeMappingSet(parent, mapping_set)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "DATA-TYPE-MAPPING-SET"
        assert child.find("SHORT-NAME").text == "MapSet"
        assert child.find("DATA-TYPE-MAPS") is not None
        assert child.find("MODE-REQUEST-TYPE-MAPS") is not None


class TestModeDeclarationWriter:
    """Tests for mode declaration and mode switch interface writers."""

    def test_set_mode_declaration(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        group = pkg.createModeDeclarationGroup("Group")
        decl = group.createModeDeclaration("Mode")
        decl.setValue(_make_float(1, "1"))

        parent = _parent()
        writer.setModeDeclaration(parent, decl)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "MODE-DECLARATION"
        assert child.find("SHORT-NAME").text == "Mode"
        assert child.find("VALUE").text == "1"

    def test_set_mode_declaration_no_value(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        group = pkg.createModeDeclarationGroup("Group")
        decl = group.createModeDeclaration("Mode")

        parent = _parent()
        writer.setModeDeclaration(parent, decl)
        assert parent[0].tag == "MODE-DECLARATION"
        assert parent[0].find("VALUE") is None

    def test_write_mode_declaration_group_mode_declaration(
        self, writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        group = pkg.createModeDeclarationGroup("Group")
        group.createModeDeclaration("Mode1")
        group.createModeDeclaration("Mode2")

        parent = _parent()
        writer.writeModeDeclarationGroupModeDeclaration(parent, group)

        assert len(parent) == 1
        assert parent[0].tag == "MODE-DECLARATIONS"
        assert len(parent[0]) == 2
        assert parent[0][0].tag == "MODE-DECLARATION"

    def test_write_mode_declaration_group_mode_declaration_empty(
        self, writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        group = pkg.createModeDeclarationGroup("Group")

        parent = _parent()
        writer.writeModeDeclarationGroupModeDeclaration(parent, group)
        assert len(parent) == 0

    def test_write_mode_declaration_group(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        group = pkg.createModeDeclarationGroup("Group")
        group.setInitialModeRef(
            _make_ref("/Init", "MODE-DECLARATION")
        )
        group.createModeDeclaration("Mode")
        group.setOnTransitionValue(_make_float(5, "5"))

        parent = _parent()
        writer.writeModeDeclarationGroup(parent, group)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "MODE-DECLARATION-GROUP"
        assert child.find("SHORT-NAME").text == "Group"
        assert child.find("INITIAL-MODE-REF").text == "/Init"
        assert child.find("MODE-DECLARATIONS") is not None
        assert child.find("ON-TRANSITION-VALUE").text == "5"

    def test_write_mode_switch_interface_mode_group(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mode_if = pkg.createModeSwitchInterface("ModeIf")
        mode_group = mode_if.createModeGroup("ModeGroup")
        mode_group.type_tref = _make_ref(
            "/ModeGrp", "MODE-DECLARATION-GROUP"
        )

        parent = _parent()
        writer.writeModeSwitchInterfaceModeGroup(parent, mode_if)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "MODE-GROUP"
        assert child.find("SHORT-NAME").text == "ModeGroup"
        assert child.find("TYPE-TREF").text == "/ModeGrp"

    def test_write_mode_switch_interface_mode_group_empty(
        self, writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mode_if = pkg.createModeSwitchInterface("ModeIf")

        parent = _parent()
        writer.writeModeSwitchInterfaceModeGroup(parent, mode_if)
        assert len(parent) == 0

    def test_write_mode_switch_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        mode_if = pkg.createModeSwitchInterface("ModeIf")
        mode_group = mode_if.createModeGroup("ModeGroup")
        mode_group.type_tref = None

        parent = _parent()
        writer.writeModeSwitchInterface(parent, mode_if)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "MODE-SWITCH-INTERFACE"
        assert child.find("SHORT-NAME").text == "ModeIf"
        assert child.find("MODE-GROUP") is not None


class TestTimingWriter:
    """Tests for timing and execution order constraint writers."""

    def test_set_eoc_executable_entity_ref_successor_refs(
        self, writer
    ):
        refs = [
            _make_ref("/Succ1", "RUNNABLE-ENTITY"),
            _make_ref("/Succ2", "RUNNABLE-ENTITY"),
        ]

        parent = _parent()
        writer.setEOCExecutableEntityRefSuccessorRefs(parent, refs)

        assert len(parent) == 1
        assert parent[0].tag == "SUCCESSOR-REFS"
        assert len(parent[0]) == 2
        assert parent[0][0].tag == "SUCCESSOR-REF"
        assert parent[0][0].text == "/Succ1"

    def test_set_eoc_executable_entity_ref_successor_refs_empty(
        self, writer
    ):
        parent = _parent()
        writer.setEOCExecutableEntityRefSuccessorRefs(parent, [])
        assert len(parent) == 0

    def test_write_eoc_executable_entity_ref(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        constraint = timing.createExecutionOrderConstraint("Eoc")
        entity_ref = constraint.createEOCExecutableEntityRef("Entity")
        entity_ref.addSuccessorRef(
            _make_ref("/Succ", "RUNNABLE-ENTITY")
        )

        parent = _parent()
        writer.writeEOCExecutableEntityRef(parent, entity_ref)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "EOC-EXECUTABLE-ENTITY-REF"
        assert child.find("SHORT-NAME").text == "Entity"
        assert child.find("SUCCESSOR-REFS") is not None

    def test_write_execution_order_constraint_ordered_element(
        self, writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        constraint = timing.createExecutionOrderConstraint("Eoc")
        constraint.createEOCExecutableEntityRef("Entity")

        parent = _parent()
        writer.writeExecutionOrderConstraintOrderedElement(
            parent, constraint
        )

        assert len(parent) == 1
        assert parent[0].tag == "ORDERED-ELEMENTS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "EOC-EXECUTABLE-ENTITY-REF"

    def test_write_eoc_ordered_element_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        constraint = timing.createExecutionOrderConstraint("Eoc")

        parent = _parent()
        writer.writeExecutionOrderConstraintOrderedElement(
            parent, constraint
        )
        assert len(parent) == 0

    def test_write_eoc_ordered_element_unsupported(
        self, warning_writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        constraint = timing.createExecutionOrderConstraint("Eoc")
        constraint.ordered_elements.append("not-an-entity")

        parent = _parent()
        warning_writer.writeExecutionOrderConstraintOrderedElement(
            parent, constraint
        )
        assert parent[0].tag == "ORDERED-ELEMENTS"
        assert len(parent[0]) == 0

    def test_write_execution_order_constraint(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        constraint = timing.createExecutionOrderConstraint("Eoc")
        constraint.createEOCExecutableEntityRef("Entity")

        parent = _parent()
        writer.writeExecutionOrderConstraint(parent, constraint)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "EXECUTION-ORDER-CONSTRAINT"
        assert child.find("SHORT-NAME").text == "Eoc"
        assert child.find("ORDERED-ELEMENTS") is not None

    def test_write_timing_requirements(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        timing.createExecutionOrderConstraint("Eoc")

        parent = _parent()
        writer.writeTimingRequirements(parent, timing)

        assert len(parent) == 1
        assert parent[0].tag == "TIMING-REQUIREMENTS"
        assert len(parent[0]) == 1
        assert parent[0][0].tag == "EXECUTION-ORDER-CONSTRAINT"

    def test_write_timing_requirements_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")

        parent = _parent()
        writer.writeTimingRequirements(parent, timing)
        assert len(parent) == 0

    def test_write_timing_requirements_unsupported(
        self, warning_writer
    ):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        timing.timing_requirements.append("not-a-constraint")

        parent = _parent()
        warning_writer.writeTimingRequirements(parent, timing)
        assert parent[0].tag == "TIMING-REQUIREMENTS"
        assert len(parent[0]) == 0

    def test_write_timing_extension(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("Timing")
        timing.createExecutionOrderConstraint("Eoc")

        parent = _parent()
        writer.writeTimingExtension(parent, timing)

        assert len(parent) == 1
        assert parent[0].tag == "TIMING-REQUIREMENTS"

    def test_write_swc_timing(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        timing = pkg.createSwcTiming("SwcTiming")
        timing.createExecutionOrderConstraint("Eoc")

        parent = _parent()
        writer.writeSwcTiming(parent, timing)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SWC-TIMING"
        assert child.find("SHORT-NAME").text == "SwcTiming"
        assert child.find("TIMING-REQUIREMENTS") is not None
