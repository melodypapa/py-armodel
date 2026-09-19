"""Tests for writer System, Mapping, FlatMap, and Gateway handlers."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    TextValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import RtePluginProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeDeclarationGroupPrototypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (  # noqa: E501
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARLiteral,
    ARNumerical,
    Boolean,
    Identifier,
    Numerical,
    PositiveInteger,
    RefType,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutineMappingSet import (
    InterpolationRoutine,
    InterpolationRoutineMapping,
    InterpolationRoutineMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerOperationMapping,
    DataPrototypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinition, ClientIdDefinitionSet, SwComponentPrototypeAssignment
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import (  # noqa: E501
    IPduMapping,
    ISignalMapping,
    TargetIPduRef,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ComponentInSystemInstanceRef,
    OperationInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.writer.arxml_writer import ARXMLWriter


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


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _literal(value):
    lit = ARLiteral()
    lit.setValue(value)
    return lit


def _numerical(value):
    n = ARNumerical()
    n.setValue(str(value))
    return n


def _revision(value):
    r = RevisionLabelString()
    r.setValue(value)
    return r


def _boolean(val=True):
    b = Boolean()
    b.setValue(val)
    return b


def _positive_int(val=1):
    i = PositiveInteger()
    i.setValue(str(val))
    return i


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _var_iref():
    iref = VariableDataPrototypeInSystemInstanceRef()
    iref.setContextCompositionRef(_ref("/c", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    iref.setTargetDataPrototypeRef(_ref("/vdp", "VARIABLE-DATA-PROTOTYPE"))
    return iref


def _component_iref():
    iref = ComponentInSystemInstanceRef()
    iref.setContextCompositionRef(_ref("/c", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    iref.setTargetComponentRef(_ref("/swc", "SW-COMPONENT-TYPE"))
    return iref


def _any_iref():
    iref = AnyInstanceRef()
    iref.setBaseRef(_ref("/b", "SW-COMPONENT-TYPE"))
    iref.setTargetRef(_ref("/t", "VARIABLE-DATA-PROTOTYPE"))
    return iref


def _make_system():
    return _pkg().createSystem("Sys")


def _make_system_mapping():
    return _make_system().createSystemMapping("SM")


def _make_flat_map():
    return _pkg().createFlatMap("FM")


def _make_physical_dimension():
    return _pkg().createPhysicalDimension("PD")


def _make_gateway():
    return _pkg().createGateway("GW")


def _make_isignal():
    return _pkg().createISignal("ISig")


def _make_system_signal_group():
    return _pkg().createSystemSignalGroup("SSG")


def _make_mapping_set():
    return _pkg().createPortInterfaceMappingSet("PIMS")


class TestWriterSystemSignalGroup:
    def test_with_signal_refs(self, writer):
        group = _make_system_signal_group()
        group.addSystemSignalRef(_ref("/s1", "SYSTEM-SIGNAL"))
        group.addSystemSignalRef(_ref("/s2", "SYSTEM-SIGNAL"))
        parent = _parent()
        writer.writeSystemSignalGroup(parent, group)
        assert parent[0].tag == "SYSTEM-SIGNAL-GROUP"
        refs = parent[0].find("SYSTEM-SIGNAL-REFS")
        assert refs is not None
        assert len(refs.findall("SYSTEM-SIGNAL-REF")) == 2

    def test_without_signal_refs(self, writer):
        group = _make_system_signal_group()
        parent = _parent()
        writer.writeSystemSignalGroup(parent, group)
        assert parent[0].tag == "SYSTEM-SIGNAL-GROUP"
        assert parent[0].find("SYSTEM-SIGNAL-REFS") is None

    def test_with_transforming_signal_ref(self, writer):
        group = _make_system_signal_group()
        group.setTransformingSystemSignalRef(_ref("/trans", "SYSTEM-SIGNAL"))
        parent = _parent()
        writer.writeSystemSignalGroup(parent, group)
        assert parent[0].tag == "SYSTEM-SIGNAL-GROUP"
        ref = parent[0].find("TRANSFORMING-SYSTEM-SIGNAL-REF")
        assert ref is not None
        assert ref.text == "/trans"

    def test_without_transforming_signal_ref(self, writer):
        group = _make_system_signal_group()
        parent = _parent()
        writer.writeSystemSignalGroup(parent, group)
        assert parent[0].tag == "SYSTEM-SIGNAL-GROUP"
        assert parent[0].find("TRANSFORMING-SYSTEM-SIGNAL-REF") is None


class TestWriterSenderReceiverToSignalMapping:
    def test_full(self, writer):
        mapping = SenderReceiverToSignalMapping()
        mapping.setCommunicationDirection(_literal("in"))
        mapping.setDataElementIRef(_var_iref())
        mapping.setSystemSignalRef(_ref("/ss", "SYSTEM-SIGNAL"))
        parent = _parent()
        writer.writeSenderReceiverToSignalMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "SENDER-RECEIVER-TO-SIGNAL-MAPPING"
        assert m.find("COMMUNICATION-DIRECTION").text == "in"
        assert m.find("DATA-ELEMENT-IREF") is not None
        assert m.find("SYSTEM-SIGNAL-REF") is not None

    def test_minimal(self, writer):
        mapping = SenderReceiverToSignalMapping()
        parent = _parent()
        writer.writeSenderReceiverToSignalMapping(parent, mapping)
        assert parent[0].tag == "SENDER-RECEIVER-TO-SIGNAL-MAPPING"
        assert parent[0].find("COMMUNICATION-DIRECTION") is None


class TestWriterSenderRecCompositeTypeMapping:
    def test_writes_attributes(self, writer):
        mapping = SenderRecRecordTypeMapping()
        parent = _parent()
        writer.writeSenderRecCompositeTypeMapping(parent, mapping)
        assert len(parent) == 0
        # Since the uuid move (Group1.md work order), SenderRecCompositeTypeMapping
        # is a plain ARObject (spec Base = ARObject) and carries no UUID attribute.
        assert "UUID" not in parent.attrib


class TestWriterSenderRecRecordElementMapping:
    def test_none(self, writer):
        parent = _parent()
        writer.writeSenderRecRecordElementMapping(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        mapping = SenderRecRecordElementMapping()
        mapping.setApplicationRecordElementRef(_ref("/a", "APPLICATION-RECORD-ELEMENT"))
        mapping.setImplementationRecordElementRef(_ref("/i", "IMPLEMENTATION-RECORD-ELEMENT"))
        mapping.setSystemSignalRef(_ref("/ss", "SYSTEM-SIGNAL"))
        parent = _parent()
        writer.writeSenderRecRecordElementMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "SENDER-REC-RECORD-ELEMENT-MAPPING"
        assert m.find("APPLICATION-RECORD-ELEMENT-REF") is not None
        assert m.find("IMPLEMENTATION-RECORD-ELEMENT-REF") is not None
        assert m.find("SYSTEM-SIGNAL-REF") is not None


class TestWriterSenderRecArrayTypeMappingRecordElementMapping:
    def test_empty(self, writer):
        mapping = SenderRecRecordTypeMapping()
        parent = _parent()
        writer.writeSenderRecArrayTypeMappingRecordElementMapping(parent, mapping)
        assert len(parent) == 0

    def test_with_mappings(self, writer):
        mapping = SenderRecRecordTypeMapping()
        elem1 = SenderRecRecordElementMapping()
        elem1.setSystemSignalRef(_ref("/s1", "SYSTEM-SIGNAL"))
        elem2 = SenderRecRecordElementMapping()
        elem2.setSystemSignalRef(_ref("/s2", "SYSTEM-SIGNAL"))
        mapping.addRecordElementMapping(elem1)
        mapping.addRecordElementMapping(elem2)
        parent = _parent()
        writer.writeSenderRecArrayTypeMappingRecordElementMapping(parent, mapping)
        assert parent[0].tag == "RECORD-ELEMENT-MAPPINGS"
        elems = parent[0].findall("SENDER-REC-RECORD-ELEMENT-MAPPING")
        assert len(elems) == 2


class TestWriterSenderRecRecordTypeMapping:
    def test_none(self, writer):
        parent = _parent()
        writer.writeSenderRecRecordTypeMapping(parent, None)
        assert len(parent) == 0

    def test_with_mapping(self, writer):
        mapping = SenderRecRecordTypeMapping()
        elem = SenderRecRecordElementMapping()
        elem.setSystemSignalRef(_ref("/s", "SYSTEM-SIGNAL"))
        mapping.addRecordElementMapping(elem)
        parent = _parent()
        writer.writeSenderRecRecordTypeMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "SENDER-REC-RECORD-TYPE-MAPPING"
        assert m.find("RECORD-ELEMENT-MAPPINGS") is not None


class TestWriterSenderReceiverToSignalGroupMappingTypeMapping:
    def test_no_type_mapping(self, writer):
        mapping = SenderReceiverToSignalGroupMapping()
        parent = _parent()
        writer.writeSenderReceiverToSignalGroupMappingTypeMapping(parent, mapping)
        assert len(parent) == 0

    def test_with_record_type_mapping(self, writer):
        mapping = SenderReceiverToSignalGroupMapping()
        type_mapping = SenderRecRecordTypeMapping()
        elem = SenderRecRecordElementMapping()
        elem.setSystemSignalRef(_ref("/s", "SYSTEM-SIGNAL"))
        type_mapping.addRecordElementMapping(elem)
        mapping.setTypeMapping(type_mapping)
        parent = _parent()
        writer.writeSenderReceiverToSignalGroupMappingTypeMapping(parent, mapping)
        tm = parent[0]
        assert tm.tag == "TYPE-MAPPING"
        assert tm.find("SENDER-REC-RECORD-TYPE-MAPPING") is not None


class TestWriterSenderReceiverToSignalGroupMapping:
    def test_full(self, writer):
        mapping = SenderReceiverToSignalGroupMapping()
        mapping.setDataElementIRef(_var_iref())
        mapping.setSignalGroupRef(_ref("/sg", "SYSTEM-SIGNAL-GROUP"))
        type_mapping = SenderRecRecordTypeMapping()
        mapping.setTypeMapping(type_mapping)
        parent = _parent()
        writer.writeSenderReceiverToSignalGroupMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING"
        assert m.find("DATA-ELEMENT-IREF") is not None
        assert m.find("SIGNAL-GROUP-REF") is not None
        assert m.find("TYPE-MAPPING") is not None


class TestWriterSystemMappingDataMappings:
    def test_empty(self, writer):
        sm = _make_system_mapping()
        parent = _parent()
        writer.writeSystemMappingDataMappings(parent, sm)
        assert len(parent) == 0

    def test_dispatches_both_types(self, writer):
        sm = _make_system_mapping()
        sm.addDataMapping(SenderReceiverToSignalMapping())
        group = SenderReceiverToSignalGroupMapping()
        group.setTypeMapping(SenderRecRecordTypeMapping())
        sm.addDataMapping(group)
        parent = _parent()
        writer.writeSystemMappingDataMappings(parent, sm)
        assert parent[0].tag == "DATA-MAPPINGS"
        tags = {c.tag for c in parent[0]}
        assert "SENDER-RECEIVER-TO-SIGNAL-MAPPING" in tags
        assert "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING" in tags


class TestWriterSetSwcToEcuMapping:
    def test_full(self, writer):
        sm = _make_system_mapping()
        mapping = sm.createSwcToEcuMapping("SwcEcu")
        mapping.addComponentIRef(_component_iref())
        mapping.setEcuInstanceRef(_ref("/ei", "ECU-INSTANCE"))
        parent = _parent()
        writer.setSwcToEcuMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "SWC-TO-ECU-MAPPING"
        assert m.find("COMPONENT-IREFS") is not None
        assert m.find("COMPONENT-IREFS/COMPONENT-IREF") is not None
        assert m.find("ECU-INSTANCE-REF") is not None

    def test_without_irefs(self, writer):
        sm = _make_system_mapping()
        mapping = sm.createSwcToEcuMapping("SwcEcu")
        parent = _parent()
        writer.setSwcToEcuMapping(parent, mapping)
        assert parent[0].tag == "SWC-TO-ECU-MAPPING"
        assert parent[0].find("COMPONENT-IREFS") is None


class TestWriterSystemMappingSwMappings:
    def test_empty(self, writer):
        sm = _make_system_mapping()
        parent = _parent()
        writer.writeSystemMappingSwMappings(parent, sm)
        assert len(parent) == 0

    def test_with_mapping(self, writer):
        sm = _make_system_mapping()
        sm.createSwcToEcuMapping("SwcEcu")
        parent = _parent()
        writer.writeSystemMappingSwMappings(parent, sm)
        assert parent[0].tag == "SW-MAPPINGS"
        assert parent[0].find("SWC-TO-ECU-MAPPING") is not None


class TestWriterEcuMapping:
    def test_minimal(self, writer):
        sm = _make_system_mapping()
        sm.createECUMapping("EM")
        parent = _parent()
        writer.writeEcuMapping(parent, sm.getEcuResourceMappings()[0])
        m = parent[0]
        assert m.tag == "ECU-MAPPING"
        assert m.find("ECU-INSTANCE-REF") is None
        assert m.find("ECU-REF") is None

    def test_full(self, writer):
        sm = _make_system_mapping()
        mapping = sm.createECUMapping("EM")
        mapping.setEcuInstanceRef(_ref("/ei", "ECU-INSTANCE"))
        mapping.setEcuRef(_ref("/e", "ECU-INSTANCE"))
        parent = _parent()
        writer.writeEcuMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "ECU-MAPPING"
        assert m.find("ECU-INSTANCE-REF") is not None
        assert m.find("ECU-REF") is not None


class TestWriterSystemMappingEcuResourceMappings:
    def test_empty(self, writer):
        sm = _make_system_mapping()
        parent = _parent()
        writer.writeSystemMappingEcuResourceMappings(parent, sm)
        assert len(parent) == 0

    def test_with_mapping(self, writer):
        sm = _make_system_mapping()
        sm.createECUMapping("EM")
        parent = _parent()
        writer.writeSystemMappingEcuResourceMappings(parent, sm)
        assert parent[0].tag == "ECU-RESOURCE-MAPPINGS"
        assert parent[0].find("ECU-MAPPING") is not None


class TestWriterSwcToImplMapping:
    def test_none(self, writer):
        parent = _parent()
        writer.writeSwcToImplMapping(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        sm = _make_system_mapping()
        mapping = sm.createSwcToImplMapping("SwcImpl")
        mapping.setComponentImplementationRef(_ref("/ci", "SWC-IMPLEMENTATION"))
        mapping.addComponentIRef(_component_iref())
        parent = _parent()
        writer.writeSwcToImplMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "SWC-TO-IMPL-MAPPING"
        assert m.find("COMPONENT-IMPLEMENTATION-REF") is not None
        assert m.find("COMPONENT-IREFS") is not None
        assert m.find("COMPONENT-IREFS/COMPONENT-IREF") is not None


class TestWriterSystemMappingSwImplMappings:
    def test_empty(self, writer):
        sm = _make_system_mapping()
        parent = _parent()
        writer.writeSystemMappingSwImplMappings(parent, sm)
        assert len(parent) == 0

    def test_with_mapping(self, writer):
        sm = _make_system_mapping()
        sm.createSwcToImplMapping("SwcImpl")
        parent = _parent()
        writer.writeSystemMappingSwImplMappings(parent, sm)
        assert parent[0].tag == "SW-IMPL-MAPPINGS"
        assert parent[0].find("SWC-TO-IMPL-MAPPING") is not None


class TestWriterSystemMapping:
    def test_full(self, writer):
        sm = _make_system_mapping()
        sm.addDataMapping(SenderReceiverToSignalMapping())
        sm.createECUMapping("EM")
        sm.createSwcToImplMapping("SwcImpl")
        sm.createSwcToEcuMapping("SwcEcu")
        parent = _parent()
        writer.writeSystemMapping(parent, sm)
        m = parent[0]
        assert m.tag == "SYSTEM-MAPPING"
        assert m.find("DATA-MAPPINGS") is not None
        assert m.find("ECU-RESOURCE-MAPPINGS") is not None
        assert m.find("SW-IMPL-MAPPINGS") is not None
        assert m.find("SW-MAPPINGS") is not None


class TestWriterSystemMappings:
    def test_empty(self, writer):
        system = _make_system()
        parent = _parent()
        writer.writeSystemMappings(parent, system)
        assert len(parent) == 0

    def test_with_mapping(self, writer):
        system = _make_system()
        system.createSystemMapping("SM")
        parent = _parent()
        writer.writeSystemMappings(parent, system)
        assert parent[0].tag == "MAPPINGS"
        assert parent[0].find("SYSTEM-MAPPING") is not None


class TestWriterRootSwCompositionPrototype:
    def test_none(self, writer):
        system = _make_system()
        parent = _parent()
        writer.writeRootSwCompositionPrototype(parent, system)
        assert len(parent) == 0

    def test_full(self, writer):
        system = _make_system()
        root = system.createRootSoftwareComposition("Root")
        root.addCalibrationParameterValueSetRef(_ref("/a", "CALIBRATION-PARAMETER-VALUE-SET"))
        root.addCalibrationParameterValueSetRef(_ref("/b", "CALIBRATION-PARAMETER-VALUE-SET"))
        root.setFlatMapRef(_ref("/fm", "FLAT-MAP"))
        root.setSoftwareCompositionTRef(_ref("/sc", "SW-COMPONENT-TYPE"))
        parent = _parent()
        writer.writeRootSwCompositionPrototype(parent, system)
        outer = parent[0]
        assert outer.tag == "ROOT-SOFTWARE-COMPOSITIONS"
        proto = outer.find("ROOT-SW-COMPOSITION-PROTOTYPE")
        assert proto is not None
        calibration_refs = proto.find("CALIBRATION-PARAMETER-VALUE-SET-REFS")
        assert calibration_refs is not None
        assert len(calibration_refs.findall("CALIBRATION-PARAMETER-VALUE-SET-REF")) == 2
        assert proto.find("FLAT-MAP-REF") is not None
        assert proto.find("SOFTWARE-COMPOSITION-TREF") is not None

    def test_empty_calibration_refs_writes_no_wrapper(self, writer):
        system = _make_system()
        system.createRootSoftwareComposition("Root")
        parent = _parent()
        writer.writeRootSwCompositionPrototype(parent, system)
        outer = parent[0]
        proto = outer.find("ROOT-SW-COMPOSITION-PROTOTYPE")
        assert proto is not None
        assert proto.find("CALIBRATION-PARAMETER-VALUE-SET-REFS") is None


class TestWriterSystemFibexElementRefs:
    def test_empty(self, writer):
        system = _make_system()
        parent = _parent()
        writer.writeSystemFibexElementRefs(parent, system)
        assert len(parent) == 0

    def test_with_refs(self, writer):
        system = _make_system()
        system.addFibexElementRef(_ref("/f1", "I-SIGNAL-I-PDU"))
        system.addFibexElementRef(_ref("/f2", "I-SIGNAL-I-PDU"))
        parent = _parent()
        writer.writeSystemFibexElementRefs(parent, system)
        assert parent[0].tag == "FIBEX-ELEMENTS"
        conds = parent[0].findall("FIBEX-ELEMENT-REF-CONDITIONAL")
        assert len(conds) == 2
        assert conds[0].find("FIBEX-ELEMENT-REF") is not None


class TestWriterSystem:
    def test_full(self, writer):
        system = _make_system()
        system.setEcuExtractVersion(_revision("1.0.0"))
        system.addFibexElementRef(_ref("/f", "I-SIGNAL-I-PDU"))
        system.createSystemMapping("SM")
        root = system.createRootSoftwareComposition("Root")
        root.setFlatMapRef(_ref("/fm", "FLAT-MAP"))
        system.setSystemVersion(_revision("2.0.0"))
        parent = _parent()
        writer.writeSystem(parent, system)
        s = parent[0]
        assert s.tag == "SYSTEM"
        assert s.find("ECU-EXTRACT-VERSION") is not None
        assert s.find("FIBEX-ELEMENTS") is not None
        assert s.find("MAPPINGS") is not None
        assert s.find("ROOT-SOFTWARE-COMPOSITIONS") is not None
        assert s.find("SYSTEM-VERSION") is not None


class TestWriterPhysicalDimension:
    def test_full(self, writer):
        dim = _make_physical_dimension()
        dim.setLengthExp(_numerical(1))
        dim.setLuminousIntensityExp(_numerical(2))
        dim.setMassExp(_numerical(3))
        dim.setMolarAmountExp(_numerical(4))
        dim.setTemperatureExp(_numerical(5))
        dim.setTimeExp(_numerical(6))
        dim.setCurrentExp(_numerical(7))
        parent = _parent()
        writer.writePhysicalDimension(parent, dim)
        d = parent[0]
        assert d.tag == "PHYSICAL-DIMENSION"
        assert d.find("LENGTH-EXP").text == "1"
        assert d.find("LUMINOUS-INTENSITY-EXP").text == "2"
        assert d.find("MASS-EXP").text == "3"
        assert d.find("MOLAR-AMOUNT-EXP").text == "4"
        assert d.find("TEMPERATURE-EXP").text == "5"
        assert d.find("TIME-EXP").text == "6"
        assert d.find("CURRENT-EXP").text == "7"


class TestWriterSetFlatInstanceDescriptor:
    def test_empty(self, writer):
        fm = _make_flat_map()
        desc = fm.createFlatInstanceDescriptor("Desc")
        parent = _parent()
        writer.setFlatInstanceDescriptor(parent, desc)
        d = parent[0]
        assert d.tag == "FLAT-INSTANCE-DESCRIPTOR"
        assert d.find("ROLE") is None
        assert d.find("RTE-PLUGIN-PROPS") is None
        assert d.find("SW-DATA-DEF-PROPS") is None
        assert d.find("UPSTREAM-REFERENCE-IREF") is None
        assert d.find("ECU-EXTRACT-REFERENCE-IREF") is None

    def test_full(self, writer):
        fm = _make_flat_map()
        desc = fm.createFlatInstanceDescriptor("Desc")
        desc.setRole(Identifier().setValue("current"))
        desc.setRtePluginProps(RtePluginProps())
        desc.setSwDataDefProps(SwDataDefProps())
        desc.setUpstreamReferenceIRef(_any_iref())
        desc.setEcuExtractReferenceIRef(_any_iref())
        parent = _parent()
        writer.setFlatInstanceDescriptor(parent, desc)
        d = parent[0]
        assert d.tag == "FLAT-INSTANCE-DESCRIPTOR"
        tags = [c.tag for c in d]
        assert [t for t in tags if t in ("ROLE", "RTE-PLUGIN-PROPS", "SW-DATA-DEF-PROPS", "UPSTREAM-REFERENCE-IREF", "ECU-EXTRACT-REFERENCE-IREF")] == [
            "ROLE",
            "RTE-PLUGIN-PROPS",
            "SW-DATA-DEF-PROPS",
            "UPSTREAM-REFERENCE-IREF",
            "ECU-EXTRACT-REFERENCE-IREF",
        ]
        assert d.find("ROLE").text == "current"
        assert d.find("RTE-PLUGIN-PROPS") is not None
        assert d.find("SW-DATA-DEF-PROPS") is not None
        assert d.find("UPSTREAM-REFERENCE-IREF/TARGET-REF").text == "/t"
        assert d.find("ECU-EXTRACT-REFERENCE-IREF/TARGET-REF").text == "/t"


class TestWriterSetRtePluginProps:
    def test_refs(self, writer):
        props = RtePluginProps()
        props.setAssociatedCrossSwClusterComRtePluginRef(_ref("/cross", "ECUC-CONTAINER-VALUE"))
        props.setAssociatedRtePluginRef(_ref("/local", "ECUC-CONTAINER-VALUE"))
        parent = _parent()

        writer.setRtePluginProps(parent, props)

        element = parent[0]
        assert element.tag == "RTE-PLUGIN-PROPS"
        assert element.find("ASSOCIATED-CROSS-SW-CLUSTER-COM-RTE-PLUGIN-REF").text == "/cross"
        assert element.find("ASSOCIATED-CROSS-SW-CLUSTER-COM-RTE-PLUGIN-REF").get("DEST") == "ECUC-CONTAINER-VALUE"
        assert element.find("ASSOCIATED-RTE-PLUGIN-REF").text == "/local"
        assert element.find("ASSOCIATED-RTE-PLUGIN-REF").get("DEST") == "ECUC-CONTAINER-VALUE"


class TestFlatInstanceDescriptorRoundTrip:
    def test_round_trip_full(self, tmp_path):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatInstanceDescriptor
        from armodel.parser.arxml_parser import ARXMLParser

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        fm = document.createARPackage("Pkg").createFlatMap("FM")
        desc = fm.createFlatInstanceDescriptor("Desc")
        desc.setRole(Identifier().setValue("current"))
        desc.setRtePluginProps(RtePluginProps())
        sw_data_def_props = SwDataDefProps()
        sw_data_def_props.setBaseTypeRef(_ref("/BaseType", "SW-BASE-TYPE"))
        desc.setSwDataDefProps(sw_data_def_props)
        desc.setUpstreamReferenceIRef(_any_iref())
        desc.setEcuExtractReferenceIRef(_any_iref())

        file_path = str(tmp_path / "flat_instance_descriptor.arxml")
        ARXMLWriter().save(file_path, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        fm_2 = document_2.getARPackages()[0].getElement("FM")
        desc_2 = fm_2.getElement("Desc", FlatInstanceDescriptor)
        assert desc_2 is not None
        assert desc_2.getRole() is not None
        assert desc_2.getRole().getValue() == "current"
        assert isinstance(desc_2.getRtePluginProps(), RtePluginProps)
        assert isinstance(desc_2.getSwDataDefProps(), SwDataDefProps)
        assert desc_2.getSwDataDefProps().getBaseTypeRef().getValue() == "/BaseType"
        assert desc_2.getUpstreamReferenceIRef().getBaseRef().getValue() == "/b"
        assert desc_2.getUpstreamReferenceIRef().getTargetRef().getValue() == "/t"
        assert desc_2.getEcuExtractReferenceIRef().getTargetRef().getValue() == "/t"


class TestFlatMapRoundTrip:
    def test_round_trip_full(self, tmp_path):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatInstanceDescriptor
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
        from armodel.parser.arxml_parser import ARXMLParser

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        fm = document.createARPackage("Pkg").createFlatMap("FM")
        desc_second = fm.createFlatInstanceDescriptor("Second")
        desc_second.setRole(Identifier().setValue("next"))
        desc_first = fm.createFlatInstanceDescriptor("First")
        desc_first.setRole(Identifier().setValue("current"))
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP_FM"))
        fm.setVariationPoint(vp)

        file_path = str(tmp_path / "flat_map.arxml")
        ARXMLWriter().save(file_path, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        fm_2 = document_2.getARPackages()[0].getElement("FM")
        assert fm_2 is not None
        instances = fm_2.getInstances()
        assert [i.getShortName() for i in instances] == ["Second", "First"]
        assert [i.getRole().getValue() for i in instances] == ["next", "current"]
        assert isinstance(instances[0], FlatInstanceDescriptor)
        assert fm_2.getVariationPoint() is not None
        assert fm_2.getVariationPoint().getShortLabel().getValue() == "VP_FM"

    def test_round_trip_empty(self, tmp_path):
        from armodel.parser.arxml_parser import ARXMLParser

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.createARPackage("Pkg").createFlatMap("FM")

        file_path = str(tmp_path / "flat_map_empty.arxml")
        ARXMLWriter().save(file_path, document)

        tree = ET.parse(file_path)
        instances_elements = [e for e in tree.iter() if e.tag.endswith("INSTANCES")]
        assert instances_elements == []

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        fm_2 = document_2.getARPackages()[0].getElement("FM")
        assert fm_2 is not None
        assert fm_2.getInstances() == []
        assert fm_2.getVariationPoint() is None


class TestWriterFlatMapInstances:
    def test_empty(self, writer):
        fm = _make_flat_map()
        parent = _parent()
        writer.writeFlatMapInstances(parent, fm)
        assert len(parent) == 0

    def test_with_instances(self, writer):
        fm = _make_flat_map()
        fm.createFlatInstanceDescriptor("D1")
        fm.createFlatInstanceDescriptor("D2")
        parent = _parent()
        writer.writeFlatMapInstances(parent, fm)
        assert parent[0].tag == "INSTANCES"
        descs = parent[0].findall("FLAT-INSTANCE-DESCRIPTOR")
        assert len(descs) == 2


class TestWriterFlatMap:
    def test_full(self, writer):
        fm = _make_flat_map()
        fm.createFlatInstanceDescriptor("D1")
        parent = _parent()
        writer.writeFlatMap(parent, fm)
        assert parent[0].tag == "FLAT-MAP"
        assert parent[0].find("INSTANCES") is not None


class TestWriterSetDataPrototypeMapping:
    def test_full(self, writer):
        mapping = DataPrototypeMapping()
        mapping.setFirstDataPrototypeRef(_ref("/f", "VARIABLE-DATA-PROTOTYPE"))
        mapping.setFirstToSecondDataTransformationRef(_ref("/t1", "DATA-TRANSFORMATION"))
        mapping.setSecondDataPrototypeRef(_ref("/s", "VARIABLE-DATA-PROTOTYPE"))
        mapping.setSecondToFirstDataTransformationRef(_ref("/t2", "DATA-TRANSFORMATION"))
        parent = _parent()
        writer.setDataPrototypeMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "DATA-PROTOTYPE-MAPPING"
        assert m.find("FIRST-DATA-PROTOTYPE-REF") is not None
        assert m.find("FIRST-TO-SECOND-DATA-TRANSFORMATION-REF") is not None
        assert m.find("SECOND-DATA-PROTOTYPE-REF") is not None
        assert m.find("SECOND-TO-FIRST-DATA-TRANSFORMATION-REF") is not None

    def test_with_sub_element_and_text_table_mappings(self, writer):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
            ApplicationCompositeDataTypeSubElementRef,
            SubElementMapping,
            TextTableMapping,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (
            ApplicationCompositeElementInPortInterfaceInstanceRef,
        )

        mapping = DataPrototypeMapping()
        sub = SubElementMapping()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        iref.setRootDataPrototypeRef(_ref("/root", "VARIABLE-DATA-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(_ref("/target", "VARIABLE-DATA-PROTOTYPE"))
        first = ApplicationCompositeDataTypeSubElementRef()
        first.setApplicationCompositeElementIRef(iref)
        sub.setFirstElement(first)
        mapping.addSubElementMapping(sub)
        text = TextTableMapping()
        text.setBitfieldTextTableMaskFirst(_positive_int(1))
        text.setBitfieldTextTableMaskSecond(_positive_int(2))
        text.setIdenticalMapping(_boolean(True))
        text.setMappingDirection(_literal("BIDIRECTIONAL"))
        mapping.addTextTableMapping(text)
        parent = _parent()
        writer.setDataPrototypeMapping(parent, mapping)
        m = parent[0]
        sub_elements = m.find("SUB-ELEMENT-MAPPINGS")
        assert sub_elements is not None
        sub_mapping = sub_elements.find("SUB-ELEMENT-MAPPING")
        first_elements = sub_mapping.find("FIRST-ELEMENTS")
        assert first_elements is not None
        sub_ref = first_elements.find("APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF")
        assert sub_ref is not None
        iref_elem = sub_ref.find("APPLICATION-COMPOSITE-ELEMENT-IREF")
        assert iref_elem is not None
        assert iref_elem.find("ROOT-DATA-PROTOTYPE-REF") is not None
        text_elements = m.find("TEXT-TABLE-MAPPINGS")
        assert text_elements is not None
        text_mapping = text_elements.find("TEXT-TABLE-MAPPING")
        assert text_mapping is not None
        assert text_mapping.find("BITFIELD-TEXT-TABLE-MASK-FIRST") is not None
        assert text_mapping.find("BITFIELD-TEXT-TABLE-MASK-SECOND") is not None
        assert text_mapping.find("IDENTICAL-MAPPING") is not None
        assert text_mapping.find("MAPPING-DIRECTION") is not None

    def test_empty_wrapper_lists_not_emitted(self, writer):
        mapping = DataPrototypeMapping()
        parent = _parent()
        writer.setDataPrototypeMapping(parent, mapping)
        m = parent[0]
        assert m.find("SUB-ELEMENT-MAPPINGS") is None
        assert m.find("TEXT-TABLE-MAPPINGS") is None
        assert m.find("FIRST-TO-SECOND-DATA-TRANSFORMATION-REF") is None
        assert m.find("SECOND-TO-FIRST-DATA-TRANSFORMATION-REF") is None


class TestWriterSetDataPrototypeMappings:
    def test_empty(self, writer):
        parent = _parent()
        writer.setDataPrototypeMappings(parent, "DATA-MAPPINGS", [])
        assert len(parent) == 0

    def test_with_mappings(self, writer):
        m1 = DataPrototypeMapping()
        m1.setFirstDataPrototypeRef(_ref("/f1", "VARIABLE-DATA-PROTOTYPE"))
        m2 = DataPrototypeMapping()
        m2.setFirstDataPrototypeRef(_ref("/f2", "VARIABLE-DATA-PROTOTYPE"))
        parent = _parent()
        writer.setDataPrototypeMappings(parent, "DATA-MAPPINGS", [m1, m2])
        assert parent[0].tag == "DATA-MAPPINGS"
        assert len(parent[0].findall("DATA-PROTOTYPE-MAPPING")) == 2


class TestWriterVariableAndParameterInterfaceMapping:
    def test_full(self, writer):
        ms = _make_mapping_set()
        mapping = ms.createVariableAndParameterInterfaceMapping("VPIM")
        dm = DataPrototypeMapping()
        dm.setFirstDataPrototypeRef(_ref("/f", "VARIABLE-DATA-PROTOTYPE"))
        mapping.addDataMapping(dm)
        parent = _parent()
        writer.writeVariableAndParameterInterfaceMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING"
        assert m.find("DATA-MAPPINGS") is not None
        assert m.find("DATA-MAPPINGS/DATA-PROTOTYPE-MAPPING") is not None


class TestWriterClientServerOperationMapping:
    def test_full(self, writer):
        mapping = ClientServerOperationMapping()
        mapping.setFirstOperationRef(_ref("/o1", "CLIENT-SERVER-OPERATION"))
        mapping.setSecondOperationRef(_ref("/o2", "CLIENT-SERVER-OPERATION"))
        parent = _parent()
        writer.writeClientServerOperationMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "CLIENT-SERVER-OPERATION-MAPPING"
        assert m.find("FIRST-OPERATION-REF") is not None
        assert m.find("SECOND-OPERATION-REF") is not None


class TestWriterClientServerInterfaceMappingOperationMappings:
    def test_empty(self, writer):
        ms = _make_mapping_set()
        mapping = ms.createClientServerInterfaceMapping("CSIM")
        parent = _parent()
        writer.writeClientServerInterfaceMappingOperationMappings(parent, mapping)
        assert len(parent) == 0

    def test_with_mappings(self, writer):
        ms = _make_mapping_set()
        mapping = ms.createClientServerInterfaceMapping("CSIM")
        op = ClientServerOperationMapping()
        op.setFirstOperationRef(_ref("/o", "CLIENT-SERVER-OPERATION"))
        mapping.addOperationMapping(op)
        parent = _parent()
        writer.writeClientServerInterfaceMappingOperationMappings(parent, mapping)
        assert parent[0].tag == "OPERATION-MAPPINGS"
        assert parent[0].find("CLIENT-SERVER-OPERATION-MAPPING") is not None


class TestWriterClientServerInterfaceMapping:
    def test_none(self, writer):
        parent = _parent()
        writer.writeClientServerInterfaceMapping(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        ms = _make_mapping_set()
        mapping = ms.createClientServerInterfaceMapping("CSIM")
        op = ClientServerOperationMapping()
        op.setFirstOperationRef(_ref("/o", "CLIENT-SERVER-OPERATION"))
        mapping.addOperationMapping(op)
        parent = _parent()
        writer.writeClientServerInterfaceMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "CLIENT-SERVER-INTERFACE-MAPPING"
        assert m.find("OPERATION-MAPPINGS") is not None


class TestWriterModeInterfaceMappingModeMapping:
    def test_no_mode_mapping(self, writer):
        ms = _make_mapping_set()
        mapping = ms.createModeInterfaceMapping("MIM")
        parent = _parent()
        writer.writeModeInterfaceMappingModeMapping(parent, mapping)
        assert len(parent) == 0

    def test_with_mode_mapping(self, writer):
        ms = _make_mapping_set()
        mapping = ms.createModeInterfaceMapping("MIM")
        mm = ModeDeclarationGroupPrototypeMapping()
        mm.setFirstModeGroupRef(_ref("/f", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        mm.setModeDeclarationMappingSetRef(_ref("/m", "MODE-DECLARATION-MAPPING-SET"))
        mm.setSecondModeGroupRef(_ref("/s", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        mapping.setModeMapping(mm)
        parent = _parent()
        writer.writeModeInterfaceMappingModeMapping(parent, mapping)
        mm_tag = parent[0]
        assert mm_tag.tag == "MODE-MAPPING"
        assert mm_tag.find("FIRST-MODE-GROUP-REF") is not None
        assert mm_tag.find("MODE-DECLARATION-MAPPING-SET-REF") is not None
        assert mm_tag.find("SECOND-MODE-GROUP-REF") is not None


class TestWriterModeInterfaceMapping:
    def test_none(self, writer):
        parent = _parent()
        writer.writeModeInterfaceMapping(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        ms = _make_mapping_set()
        mapping = ms.createModeInterfaceMapping("MIM")
        mm = ModeDeclarationGroupPrototypeMapping()
        mm.setFirstModeGroupRef(_ref("/f", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        mapping.setModeMapping(mm)
        parent = _parent()
        writer.writeModeInterfaceMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "MODE-INTERFACE-MAPPING"
        assert m.find("MODE-MAPPING") is not None


class TestWriterPortInterfaceMappings:
    def test_empty(self, writer):
        ms = _make_mapping_set()
        parent = _parent()
        writer.writePortInterfaceMappings(parent, ms)
        assert len(parent) == 0

    def test_dispatches_all_types(self, writer):
        ms = _make_mapping_set()
        ms.createVariableAndParameterInterfaceMapping("VPIM")
        ms.createClientServerInterfaceMapping("CSIM")
        ms.createModeInterfaceMapping("MIM")
        parent = _parent()
        writer.writePortInterfaceMappings(parent, ms)
        assert parent[0].tag == "PORT-INTERFACE-MAPPINGS"
        tags = {c.tag for c in parent[0]}
        assert "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING" in tags
        assert "CLIENT-SERVER-INTERFACE-MAPPING" in tags
        assert "MODE-INTERFACE-MAPPING" in tags


class TestWriterPortInterfaceMappingSet:
    def test_full(self, writer):
        ms = _make_mapping_set()
        ms.createVariableAndParameterInterfaceMapping("VPIM")
        ms.createClientServerInterfaceMapping("CSIM")
        ms.createModeInterfaceMapping("MIM")
        parent = _parent()
        writer.writePortInterfaceMappingSet(parent, ms)
        m = parent[0]
        assert m.tag == "PORT-INTERFACE-MAPPING-SET"
        assert m.find("PORT-INTERFACE-MAPPINGS") is not None


class TestWriterSetISignalMappings:
    def test_empty(self, writer):
        parent = _parent()
        writer.setISignalMappings(parent, [])
        assert len(parent) == 0

    def test_with_mappings(self, writer):
        m1 = ISignalMapping()
        m1.setSourceSignalRef(_ref("/s1", "I-SIGNAL"))
        m1.setTargetSignalRef(_ref("/t1", "I-SIGNAL"))
        m2 = ISignalMapping()
        m2.setSourceSignalRef(_ref("/s2", "I-SIGNAL"))
        parent = _parent()
        writer.setISignalMappings(parent, [m1, m2])
        assert parent[0].tag == "SIGNAL-MAPPINGS"
        ms = parent[0].findall("I-SIGNAL-MAPPING")
        assert len(ms) == 2
        assert ms[0].find("SOURCE-SIGNAL-REF") is not None
        assert ms[0].find("TARGET-SIGNAL-REF") is not None


class TestWriterSetTargetIPduRef:
    def test_none(self, writer):
        parent = _parent()
        writer.setTargetIPduRef(parent, "TARGET-I-PDU", None)
        assert len(parent) == 0

    def test_with_ref(self, writer):
        ref = TargetIPduRef()
        ref.setTargetIPduRef(_ref("/p", "I-SIGNAL-I-PDU"))
        parent = _parent()
        writer.setTargetIPduRef(parent, "TARGET-I-PDU", ref)
        assert parent[0].tag == "TARGET-I-PDU"
        assert parent[0].find("TARGET-I-PDU-REF") is not None


class TestWriterSetIPduMappings:
    def test_empty(self, writer):
        parent = _parent()
        writer.setIPduMappings(parent, [])
        assert len(parent) == 0

    def test_with_mappings(self, writer):
        m1 = IPduMapping()
        m1.setSourceIpduRef(_ref("/s1", "I-SIGNAL-I-PDU"))
        target1 = TargetIPduRef()
        target1.setTargetIPduRef(_ref("/t1", "I-SIGNAL-I-PDU"))
        m1.setTargetIPdu(target1)
        m2 = IPduMapping()
        m2.setSourceIpduRef(_ref("/s2", "I-SIGNAL-I-PDU"))
        parent = _parent()
        writer.setIPduMappings(parent, [m1, m2])
        assert parent[0].tag == "I-PDU-MAPPINGS"
        ms = parent[0].findall("I-PDU-MAPPING")
        assert len(ms) == 2
        assert ms[0].find("SOURCE-I-PDU-REF") is not None
        assert ms[0].find("TARGET-I-PDU") is not None
        assert ms[0].find("TARGET-I-PDU/TARGET-I-PDU-REF") is not None


class TestWriterGateway:
    def test_full(self, writer):
        gw = _make_gateway()
        gw.setEcuRef(_ref("/e", "ECU-INSTANCE"))
        pdu = IPduMapping()
        pdu.setSourceIpduRef(_ref("/s", "I-SIGNAL-I-PDU"))
        gw.addIPduMapping(pdu)
        sig = ISignalMapping()
        sig.setSourceSignalRef(_ref("/ss", "I-SIGNAL"))
        gw.addSignalMapping(sig)
        parent = _parent()
        writer.writeGateway(parent, gw)
        g = parent[0]
        assert g.tag == "GATEWAY"
        assert g.find("ECU-REF") is not None
        assert g.find("I-PDU-MAPPINGS") is not None
        assert g.find("SIGNAL-MAPPINGS") is not None


class TestWriterISignal:
    def test_full(self, writer):
        sig = _make_isignal()
        sig.setDataTypePolicy(_literal("LEGACY"))
        sig.setISignalType(_literal("FIXED-LENGTH"))
        sig.setLength(_numerical(8))
        sig.setSystemSignalRef(_ref("/ss", "SYSTEM-SIGNAL"))
        sig.setDataTransformationRef(_ref("/dt", "DATA-TRANSFORMATION"))
        sig.setTimeoutSubstitutionValue(TextValueSpecification())
        props = EndToEndTransformationISignalProps()
        props.setTransformerRef(_ref("/tr", "TRANSFORMATION-PROPS"))
        sig.addTransformationISignalProps(props)
        parent = _parent()
        writer.writeISignal(parent, sig)
        s = parent[0]
        assert s.tag == "I-SIGNAL"
        assert s.find("DATA-TYPE-POLICY").text == "LEGACY"
        assert s.find("I-SIGNAL-TYPE").text == "FIXED-LENGTH"
        assert s.find("LENGTH").text == "8"
        assert s.find("SYSTEM-SIGNAL-REF") is not None
        assert s.find("DATA-TRANSFORMATIONS/DATA-TRANSFORMATION-REF-CONDITIONAL/DATA-TRANSFORMATION-REF") is not None
        assert s.find("TIMEOUT-SUBSTITUTION-VALUE") is not None
        assert s.find("TRANSFORMATION-I-SIGNAL-PROPSS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS") is not None

    def test_with_i_signal_props(self, writer):
        from armodel.models import ISignalProps

        sig = _make_isignal()
        props = ISignalProps()
        props.setHandleOutOfRange(_literal("DEFAULT"))
        sig.setISignalProps(props)
        parent = _parent()
        writer.writeISignal(parent, sig)
        s = parent[0]
        assert s.tag == "I-SIGNAL"
        assert s.find("I-SIGNAL-PROPS") is not None
        assert s.find("I-SIGNAL-PROPS/HANDLE-OUT-OF-RANGE").text == "DEFAULT"

    def test_without_i_signal_props(self, writer):
        sig = _make_isignal()
        parent = _parent()
        writer.writeISignal(parent, sig)
        s = parent[0]
        assert s.tag == "I-SIGNAL"
        assert s.find("I-SIGNAL-PROPS") is None


class TestWriterOperationInSystemInstanceRef:
    def test_full(self, writer):
        iref = OperationInSystemInstanceRef()
        iref.setBaseRef(_ref("/b", "COMPOSITION-SW-COMPONENT-TYPE"))
        iref.setContextCompositionRef(_ref("/comp", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.addContextComponentRef(_ref("/c1", "SW-COMPONENT-PROTOTYPE"))
        iref.addContextComponentRef(_ref("/c2", "SW-COMPONENT-PROTOTYPE"))
        iref.setContextPortRef(_ref("/port", "PORT-PROTOTYPE"))
        iref.setTargetOperationRef(_ref("/op", "CLIENT-SERVER-OPERATION"))

        parent = _parent()
        writer.setOperationInSystemInstanceRef(parent, "OPERATION-IREF", iref)

        child = parent.find("OPERATION-IREF")
        assert child is not None
        assert [c.tag for c in child] == [
            "BASE-REF",
            "CONTEXT-COMPOSITION-REF",
            "CONTEXT-COMPONENT-REF",
            "CONTEXT-COMPONENT-REF",
            "CONTEXT-PORT-REF",
            "TARGET-OPERATION-REF",
        ]
        assert child.find("BASE-REF").get("DEST") == "COMPOSITION-SW-COMPONENT-TYPE"
        assert child.find("BASE-REF").text == "/b"
        assert child.find("CONTEXT-COMPOSITION-REF").get("DEST") == "ROOT-SW-COMPOSITION-PROTOTYPE"
        ctx = child.findall("CONTEXT-COMPONENT-REF")
        assert [r.text for r in ctx] == ["/c1", "/c2"]
        assert all(r.get("DEST") == "SW-COMPONENT-PROTOTYPE" for r in ctx)
        assert child.find("CONTEXT-PORT-REF").get("DEST") == "PORT-PROTOTYPE"
        assert child.find("TARGET-OPERATION-REF").get("DEST") == "CLIENT-SERVER-OPERATION"
        assert child.find("TARGET-OPERATION-REF").text == "/op"

    def test_none_ref(self, writer):
        parent = _parent()
        writer.setOperationInSystemInstanceRef(parent, "OPERATION-IREF", None)
        assert len(parent) == 0

    def test_empty_context_components(self, writer):
        iref = OperationInSystemInstanceRef()
        iref.setTargetOperationRef(_ref("/op", "CLIENT-SERVER-OPERATION"))

        parent = _parent()
        writer.setOperationInSystemInstanceRef(parent, "OPERATION-IREF", iref)

        child = parent.find("OPERATION-IREF")
        assert child is not None
        assert [c.tag for c in child] == ["TARGET-OPERATION-REF"]


class TestWriterClientIdDefinition:
    def _make_id_definition(self):
        id_definition = ClientIdDefinition(parent=AUTOSAR.getInstance(), short_name="CID1")
        client_id = Numerical()
        client_id.setValue("5")
        id_definition.setClientId(client_id)
        iref = OperationInSystemInstanceRef()
        iref.setContextPortRef(_ref("/port", "R-PORT-PROTOTYPE"))
        iref.setTargetOperationRef(_ref("/op", "CLIENT-SERVER-OPERATION"))
        id_definition.setClientServerOperationIRef(iref)
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("VP_CID"))
        id_definition.setVariationPoint(variation_point)
        return id_definition

    def test_members_in_xsd_order(self, writer):
        id_definition = self._make_id_definition()
        parent = _parent()
        writer.writeClientIdDefinition(parent, id_definition)

        child = parent.find("CLIENT-ID-DEFINITION")
        assert child is not None
        tags = [c.tag for c in child]
        assert tags.index("CLIENT-ID") < tags.index("CLIENT-SERVER-OPERATION-IREF") < tags.index("VARIATION-POINT")
        assert child.find("CLIENT-ID").text == "5"
        iref_element = child.find("CLIENT-SERVER-OPERATION-IREF")
        assert iref_element.find("CONTEXT-PORT-REF").get("DEST") == "R-PORT-PROTOTYPE"
        assert iref_element.find("CONTEXT-PORT-REF").text == "/port"
        assert iref_element.find("TARGET-OPERATION-REF").get("DEST") == "CLIENT-SERVER-OPERATION"
        assert iref_element.find("TARGET-OPERATION-REF").text == "/op"
        assert child.find("VARIATION-POINT/SHORT-LABEL").text == "VP_CID"

    def test_none_members_not_emitted(self, writer):
        id_definition = ClientIdDefinition(parent=AUTOSAR.getInstance(), short_name="CID1")
        parent = _parent()
        writer.writeClientIdDefinition(parent, id_definition)

        child = parent.find("CLIENT-ID-DEFINITION")
        assert child is not None
        assert child.find("CLIENT-ID") is None
        assert child.find("CLIENT-SERVER-OPERATION-IREF") is None

    def test_client_id_only_no_iref_element(self, writer):
        id_definition = ClientIdDefinition(parent=AUTOSAR.getInstance(), short_name="CID1")
        client_id = Numerical()
        client_id.setValue("7")
        id_definition.setClientId(client_id)
        parent = _parent()
        writer.writeClientIdDefinition(parent, id_definition)

        child = parent.find("CLIENT-ID-DEFINITION")
        assert child is not None
        assert child.find("CLIENT-ID").text == "7"
        assert child.find("CLIENT-SERVER-OPERATION-IREF") is None


class TestWriterClientIdDefinitionSet:
    def _make_set(self):
        id_definition_set = ClientIdDefinitionSet(parent=AUTOSAR.getInstance(), short_name="IDS1")
        id_definition = id_definition_set.createClientIdDefinition("CID1")
        client_id = Numerical()
        client_id.setValue("5")
        id_definition.setClientId(client_id)
        id_definition_set.createClientIdDefinition("CID2")
        return id_definition_set

    def test_wrapper_and_children_in_xsd_order(self, writer):
        id_definition_set = self._make_set()
        parent = _parent()
        writer.writeClientIdDefinitionSet(parent, id_definition_set)

        child = parent.find("CLIENT-ID-DEFINITION-SET")
        assert child is not None
        wrapper = child.find("CLIENT-ID-DEFINITIONS")
        assert wrapper is not None
        definitions = wrapper.findall("CLIENT-ID-DEFINITION")
        assert len(definitions) == 2
        assert [d.find("SHORT-NAME").text for d in definitions] == ["CID1", "CID2"]
        assert definitions[0].find("CLIENT-ID").text == "5"

    def test_empty_set_no_wrapper(self, writer):
        id_definition_set = ClientIdDefinitionSet(parent=AUTOSAR.getInstance(), short_name="IDS1")
        parent = _parent()
        writer.writeClientIdDefinitionSet(parent, id_definition_set)

        child = parent.find("CLIENT-ID-DEFINITION-SET")
        assert child is not None
        assert child.find("CLIENT-ID-DEFINITIONS") is None

    def test_round_trip(self, tmp_path):
        from armodel.parser.arxml_parser import ARXMLParser

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        package = document.createARPackage("Pkg")
        package.createClientIdDefinitionSet("IDS1").createClientIdDefinition("CID1")

        file_path = str(tmp_path / "client_id_definition_set_round_trip.arxml")
        ARXMLWriter().save(file_path, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        package_2 = document_2.getARPackages()[0]
        id_definition_set_2 = package_2.getElement("IDS1", ClientIdDefinitionSet)
        assert id_definition_set_2 is not None
        definitions = id_definition_set_2.getClientIdDefinitions()
        assert len(definitions) == 1
        assert definitions[0].getShortName() == "CID1"


class TestWriterInterpolationRoutine:
    def test_full_in_xsd_order(self, writer):
        routine = InterpolationRoutine()
        short_label = Identifier()
        short_label.setValue("LinearInterpolation")
        routine.setShortLabel(short_label)
        is_default = Boolean()
        is_default.setValue(True)
        routine.setIsDefault(is_default)
        ref = RefType()
        ref.setDest("BSW-MODULE-ENTRY")
        ref.setValue("/BswM/BswEntries/InterpolationEntry")
        routine.setInterpolationRoutineRef(ref)

        parent = _parent()
        writer.writeInterpolationRoutine(parent, routine)

        child = parent.find("INTERPOLATION-ROUTINE")
        assert child is not None
        assert [e.tag for e in child] == ["SHORT-LABEL", "IS-DEFAULT", "INTERPOLATION-ROUTINE-REF"]
        assert child.find("SHORT-LABEL").text == "LinearInterpolation"
        assert child.find("IS-DEFAULT").text == "true"
        ref_element = child.find("INTERPOLATION-ROUTINE-REF")
        assert ref_element.get("DEST") == "BSW-MODULE-ENTRY"
        assert ref_element.text == "/BswM/BswEntries/InterpolationEntry"

    def test_empty_no_children(self, writer):
        routine = InterpolationRoutine()
        parent = _parent()
        writer.writeInterpolationRoutine(parent, routine)

        child = parent.find("INTERPOLATION-ROUTINE")
        assert child is not None
        assert len(child) == 0


class TestWriterInterpolationRoutineMapping:
    def test_full_in_xsd_order(self, writer):
        mapping = InterpolationRoutineMapping()

        routine = mapping.createInterpolationRoutine()
        short_label = Identifier()
        short_label.setValue("LinearInterpolation")
        routine.setShortLabel(short_label)

        routine2 = mapping.createInterpolationRoutine()
        short_label2 = Identifier()
        short_label2.setValue("TableLookup")
        routine2.setShortLabel(short_label2)

        ref = RefType()
        ref.setDest("SW-RECORD-LAYOUT")
        ref.setValue("/Package/SwRecordLayouts/Layout1")
        mapping.setSwRecordLayoutRef(ref)

        parent = _parent()
        writer.writeInterpolationRoutineMapping(parent, mapping)

        child = parent.find("INTERPOLATION-ROUTINE-MAPPING")
        assert child is not None
        assert [e.tag for e in child] == ["INTERPOLATION-ROUTINES", "SW-RECORD-LAYOUT-REF"]
        routines_wrapper = child.find("INTERPOLATION-ROUTINES")
        assert [e.tag for e in routines_wrapper] == ["INTERPOLATION-ROUTINE", "INTERPOLATION-ROUTINE"]
        assert routines_wrapper[0].find("SHORT-LABEL").text == "LinearInterpolation"
        assert routines_wrapper[1].find("SHORT-LABEL").text == "TableLookup"
        ref_element = child.find("SW-RECORD-LAYOUT-REF")
        assert ref_element.get("DEST") == "SW-RECORD-LAYOUT"
        assert ref_element.text == "/Package/SwRecordLayouts/Layout1"

    def test_empty_no_children(self, writer):
        mapping = InterpolationRoutineMapping()
        parent = _parent()
        writer.writeInterpolationRoutineMapping(parent, mapping)

        child = parent.find("INTERPOLATION-ROUTINE-MAPPING")
        assert child is not None
        assert len(child) == 0


class TestWriterInterpolationRoutineMappingSet:
    def _make_set(self):
        mapping_set = InterpolationRoutineMappingSet(parent=AUTOSAR.getInstance(), short_name="IRS1")
        mapping = mapping_set.createInterpolationRoutineMapping()
        routine = mapping.createInterpolationRoutine()
        short_label = Identifier()
        short_label.setValue("LinearInterpolation")
        routine.setShortLabel(short_label)
        ref = RefType()
        ref.setDest("SW-RECORD-LAYOUT")
        ref.setValue("/Package/SwRecordLayouts/Layout1")
        mapping.setSwRecordLayoutRef(ref)
        return mapping_set

    def test_wrapper_and_children_in_xsd_order(self, writer):
        mapping_set = self._make_set()
        parent = _parent()
        writer.writeInterpolationRoutineMappingSet(parent, mapping_set)

        child = parent.find("INTERPOLATION-ROUTINE-MAPPING-SET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "IRS1"
        wrapper = child.find("INTERPOLATION-ROUTINE-MAPPINGS")
        assert wrapper is not None
        mappings = wrapper.findall("INTERPOLATION-ROUTINE-MAPPING")
        assert len(mappings) == 1
        assert mappings[0].find("INTERPOLATION-ROUTINES/INTERPOLATION-ROUTINE/SHORT-LABEL").text == "LinearInterpolation"
        ref_element = mappings[0].find("SW-RECORD-LAYOUT-REF")
        assert ref_element.get("DEST") == "SW-RECORD-LAYOUT"
        assert ref_element.text == "/Package/SwRecordLayouts/Layout1"

    def test_empty_set_no_wrapper(self, writer):
        mapping_set = InterpolationRoutineMappingSet(parent=AUTOSAR.getInstance(), short_name="IRS1")
        parent = _parent()
        writer.writeInterpolationRoutineMappingSet(parent, mapping_set)

        child = parent.find("INTERPOLATION-ROUTINE-MAPPING-SET")
        assert child is not None
        assert child.find("INTERPOLATION-ROUTINE-MAPPINGS") is None


class TestWriterSwComponentPrototypeAssignment:
    def _make_assignment(self):
        assignment = SwComponentPrototypeAssignment()
        iref = ComponentInSystemInstanceRef()
        iref.setContextCompositionRef(_ref("/comp", "COMPOSITION-SW-COMPONENT-PROTOTYPE"))
        iref.setTargetComponentRef(_ref("/swc", "SW-COMPONENT-PROTOTYPE"))
        assignment.setSwComponentIRef(iref)
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("VP_SWCA"))
        assignment.setVariationPoint(variation_point)
        return assignment

    def test_members_in_xsd_order(self, writer):
        assignment = self._make_assignment()
        parent = _parent()
        writer.writeSwComponentPrototypeAssignment(parent, assignment)

        child = parent.find("SW-COMPONENT-PROTOTYPE-ASSIGNMENT")
        assert child is not None
        tags = [c.tag for c in child]
        assert tags.index("SW-COMPONENT-IREF") < tags.index("VARIATION-POINT")
        iref_element = child.find("SW-COMPONENT-IREF")
        assert iref_element.find("CONTEXT-COMPOSITION-REF").get("DEST") == "COMPOSITION-SW-COMPONENT-PROTOTYPE"
        assert iref_element.find("CONTEXT-COMPOSITION-REF").text == "/comp"
        assert iref_element.find("TARGET-COMPONENT-REF").get("DEST") == "SW-COMPONENT-PROTOTYPE"
        assert iref_element.find("TARGET-COMPONENT-REF").text == "/swc"
        assert child.find("VARIATION-POINT/SHORT-LABEL").text == "VP_SWCA"

    def test_none_members_not_emitted(self, writer):
        assignment = SwComponentPrototypeAssignment()
        parent = _parent()
        writer.writeSwComponentPrototypeAssignment(parent, assignment)

        child = parent.find("SW-COMPONENT-PROTOTYPE-ASSIGNMENT")
        assert child is not None
        assert child.find("SW-COMPONENT-IREF") is None
        assert child.find("VARIATION-POINT") is None
