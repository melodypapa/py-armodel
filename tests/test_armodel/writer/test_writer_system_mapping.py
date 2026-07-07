"""Tests for writer System, Mapping, FlatMap, and Gateway handlers."""
import xml.etree.cElementTree as ET
import pytest

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import (
    SwcToEcuMapping,
    System,
    SystemMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import (
    ECUMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    SwcToImplMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ComponentInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (  # noqa: E501
    ISignal,
    SystemSignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import (  # noqa: E501
    Gateway,
    IPduMapping,
    ISignalMapping,
    TargetIPduRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import (
    FlatInstanceDescriptor,
    FlatMap,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeDeclarationGroupPrototypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerInterfaceMapping,
    ClientServerOperationMapping,
    DataPrototypeMapping,
    ModeInterfaceMapping,
    PortInterfaceMappingSet,
    VariableAndParameterInterfaceMapping,
)
from armodel.models.M2.MSR.AsamHdo.Units import PhysicalDimension
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (  # noqa: E501
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARLiteral,
    ARNumerical,
    RefType,
    RevisionLabelString,
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
        group.addSystemSignalRefs(_ref("/s1", "SYSTEM-SIGNAL"))
        group.addSystemSignalRefs(_ref("/s2", "SYSTEM-SIGNAL"))
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
        mapping.uuid = "abc-123"
        parent = _parent()
        writer.writeSenderRecCompositeTypeMapping(parent, mapping)
        assert len(parent) == 0
        assert parent.attrib.get("UUID") == "abc-123"


class TestWriterSenderRecRecordElementMapping:
    def test_none(self, writer):
        parent = _parent()
        writer.writeSenderRecRecordElementMapping(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        mapping = SenderRecRecordElementMapping()
        mapping.setApplicationRecordElementRef(_ref("/a", "APPLICATION-RECORD-ELEMENT"))
        mapping.setImplementationRecordElementRef(
            _ref("/i", "IMPLEMENTATION-RECORD-ELEMENT")
        )
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
        mapping.setComponentImplementationRef(
            _ref("/ci", "SWC-IMPLEMENTATION")
        )
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
        root.setFlatMapRef(_ref("/fm", "FLAT-MAP"))
        root.setSoftwareCompositionTRef(_ref("/sc", "SW-COMPONENT-TYPE"))
        parent = _parent()
        writer.writeRootSwCompositionPrototype(parent, system)
        outer = parent[0]
        assert outer.tag == "ROOT-SOFTWARE-COMPOSITIONS"
        proto = outer.find("ROOT-SW-COMPOSITION-PROTOTYPE")
        assert proto is not None
        assert proto.find("FLAT-MAP-REF") is not None
        assert proto.find("SOFTWARE-COMPOSITION-TREF") is not None


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
    def test_full(self, writer):
        fm = _make_flat_map()
        desc = fm.createFlatInstanceDescriptor("Desc")
        desc.setUpstreamReferenceIRef(_any_iref())
        desc.setEcuExtractReferenceIRef(_any_iref())
        parent = _parent()
        writer.setFlatInstanceDescriptor(parent, desc)
        d = parent[0]
        assert d.tag == "FLAT-INSTANCE-DESCRIPTOR"
        assert d.find("UPSTREAM-REFERENCE-IREF") is not None
        assert d.find("ECU-EXTRACT-REFERENCE-IREF") is not None


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
        mapping.setSecondDataPrototypeRef(_ref("/s", "VARIABLE-DATA-PROTOTYPE"))
        parent = _parent()
        writer.setDataPrototypeMapping(parent, mapping)
        m = parent[0]
        assert m.tag == "DATA-PROTOTYPE-MAPPING"
        assert m.find("FIRST-DATA-PROTOTYPE-REF") is not None
        assert m.find("SECOND-DATA-PROTOTYPE-REF") is not None


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
        ref.setTargetIPdu(_ref("/p", "I-SIGNAL-I-PDU"))
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
        target1.setTargetIPdu(_ref("/t1", "I-SIGNAL-I-PDU"))
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
        parent = _parent()
        writer.writeISignal(parent, sig)
        s = parent[0]
        assert s.tag == "I-SIGNAL"
        assert s.find("DATA-TYPE-POLICY").text == "LEGACY"
        assert s.find("I-SIGNAL-TYPE").text == "FIXED-LENGTH"
        assert s.find("LENGTH").text == "8"
        assert s.find("SYSTEM-SIGNAL-REF") is not None
