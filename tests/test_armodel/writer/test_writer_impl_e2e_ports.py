"""Tests for writer implementation, E2E, and port interface handlers."""
import xml.etree.cElementTree as ET
from unittest.mock import MagicMock
import pytest
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    AUTOSAR,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Code,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import (  # noqa: E501
    ResourceConsumption,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import (  # noqa: E501
    MemorySection,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import (  # noqa: E501
    SwcImplementation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (  # noqa: E501
    EndToEndDescription,
    EndToEndProtectionISignalIPdu,
    EndToEndProtectionVariablePrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (  # noqa: E501
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (  # noqa: E501
    ModeDeclarationGroupPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (  # noqa: E501
    VariableDataPrototypeInSystemInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARBoolean, ARLiteral, PositiveInteger, RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (  # noqa: E501
    AutosarEngineeringObject,
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


def _make_literal(text):
    literal = ARLiteral()
    literal.setValue(text)
    return literal


def _make_positive_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _make_ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteArtifactDescriptors:
    def test_write_artifact_descriptors_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        code = Code(pkg, "Code")
        parent = _parent()
        writer.writeArtifactDescriptors(parent, code)
        assert len(parent) == 0

    def test_write_artifact_descriptors_with_objects(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        code = Code(pkg, "Code")
        obj = AutosarEngineeringObject()
        obj.setShortLabel(_make_literal("Label"))
        obj.setCategory(_make_literal("Cat"))
        code.addArtifactDescriptor(obj)
        parent = _parent()
        writer.writeArtifactDescriptors(parent, code)
        assert len(parent) == 1
        descs = parent[0]
        assert descs.tag == "ARTIFACT-DESCRIPTORS"
        assert len(descs) == 1
        eng_obj = descs[0]
        assert eng_obj.tag == "AUTOSAR-ENGINEERING-OBJECT"
        assert eng_obj.find("SHORT-LABEL").text == "Label"
        assert eng_obj.find("CATEGORY").text == "Cat"


class TestWriteCode:
    def test_write_code_basic(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        code = Code(pkg, "MyCode")
        parent = _parent()
        writer.writeCode(parent, code)
        assert len(parent) == 1
        code_tag = parent[0]
        assert code_tag.tag == "CODE"
        assert code_tag.find("SHORT-NAME").text == "MyCode"

    def test_write_code_with_artifact_descriptor(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        code = Code(pkg, "MyCode")
        obj = AutosarEngineeringObject()
        obj.setShortLabel(_make_literal("L1"))
        code.addArtifactDescriptor(obj)
        parent = _parent()
        writer.writeCode(parent, code)
        code_tag = parent[0]
        descs = code_tag.find("ARTIFACT-DESCRIPTORS")
        assert descs is not None
        assert descs[0].tag == "AUTOSAR-ENGINEERING-OBJECT"


class TestWriteCodeDescriptors:
    def test_write_code_descriptors_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = SwcImplementation(pkg, "Impl")
        parent = _parent()
        writer.writeCodeDescriptors(parent, impl)
        assert len(parent) == 0

    def test_write_code_descriptors_with_code(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = SwcImplementation(pkg, "Impl")
        impl.createCodeDescriptor("C1")
        parent = _parent()
        writer.writeCodeDescriptors(parent, impl)
        assert len(parent) == 1
        descs = parent[0]
        assert descs.tag == "CODE-DESCRIPTORS"
        assert descs[0].tag == "CODE"

    def test_write_code_descriptors_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        impl = MagicMock()
        impl.getCodeDescriptors.return_value = ["not_a_code"]
        parent = _parent()
        w.writeCodeDescriptors(parent, impl)
        assert len(parent) == 1
        assert parent[0].tag == "CODE-DESCRIPTORS"


class TestSetMemorySectionOptions:
    def test_set_memory_section_options_empty(self, writer):
        section = MemorySection(None, "Sec")
        parent = _parent()
        writer.setMemorySectionOptions(parent, section.getOptions())
        assert len(parent) == 0

    def test_set_memory_section_options_with_values(self, writer):
        section = MemorySection(None, "Sec")
        section.addOption(_make_literal("OPT1"))
        section.addOption(_make_literal("OPT2"))
        parent = _parent()
        writer.setMemorySectionOptions(parent, section.getOptions())
        assert len(parent) == 1
        options_tag = parent[0]
        assert options_tag.tag == "OPTIONS"
        opts = options_tag.findall("OPTION")
        assert [o.text for o in opts] == ["OPT1", "OPT2"]


class TestWriteMemorySections:
    def test_write_memory_sections_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        consumption = ResourceConsumption(pkg, "RC")
        parent = _parent()
        writer.writeMemorySections(parent, consumption)
        assert len(parent) == 0

    def test_write_memory_sections_with_section(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        consumption = ResourceConsumption(pkg, "RC")
        section = consumption.createMemorySection("Mem")
        section.setAlignment(_make_literal("UNKNOWN"))
        section.setMemClassSymbol(_make_literal("SYM"))
        section.addOption(_make_literal("OPT"))
        section.setSize(_make_positive_int("128"))
        section.setSwAddrMethodRef(_make_ref("SW-ADDR-METHOD", "/Addr"))
        section.setSymbol(_make_literal("Sym"))
        parent = _parent()
        writer.writeMemorySections(parent, consumption)
        assert len(parent) == 1
        sections_tag = parent[0]
        assert sections_tag.tag == "MEMORY-SECTIONS"
        mem = sections_tag[0]
        assert mem.tag == "MEMORY-SECTION"
        assert mem.find("SHORT-NAME").text == "Mem"
        assert mem.find("ALIGNMENT").text == "UNKNOWN"
        assert mem.find("MEM-CLASS-SYMBOL").text == "SYM"
        assert mem.find("OPTIONS/OPTION").text == "OPT"
        assert mem.find("SIZE").text == "128"
        assert mem.find("SW-ADDRMETHOD-REF").text == "/Addr"
        assert mem.find("SYMBOL").text == "Sym"


class TestSetRoughEstimateStackUsage:
    def test_set_rough_estimate_stack_usage_none(self, writer):
        parent = _parent()
        writer.setRoughEstimateStackUsage(parent, None)
        assert len(parent) == 0

    def test_set_rough_estimate_stack_usage_with_value(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        consumption = ResourceConsumption(pkg, "RC")
        usage = consumption.createRoughEstimateStackUsage("U1")
        usage.setMemoryConsumption(_make_positive_int("256"))
        parent = _parent()
        writer.setRoughEstimateStackUsage(parent, usage)
        assert len(parent) == 1
        rough = parent[0]
        assert rough.tag == "ROUGH-ESTIMATE-STACK-USAGE"
        assert rough.find("SHORT-NAME").text == "U1"
        assert rough.find("MEMORY-CONSUMPTION").text == "256"

    def test_set_stack_usage_directly(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        consumption = ResourceConsumption(pkg, "RC")
        usage = consumption.createRoughEstimateStackUsage("Direct")
        parent = _parent()
        writer.setStackUsage(parent, usage)
        assert parent.find("SHORT-NAME").text == "Direct"


class TestWriteStackUsages:
    def test_write_stack_usages_empty(self, writer):
        parent = _parent()
        writer.writeStackUsages(parent, [])
        assert len(parent) == 0

    def test_write_stack_usages_with_rough_estimate(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        consumption = ResourceConsumption(pkg, "RC")
        usage = consumption.createRoughEstimateStackUsage("U1")
        usage.setMemoryConsumption(_make_positive_int("100"))
        parent = _parent()
        writer.writeStackUsages(parent, [usage])
        assert len(parent) == 1
        usages_tag = parent[0]
        assert usages_tag.tag == "STACK-USAGES"
        assert usages_tag[0].tag == "ROUGH-ESTIMATE-STACK-USAGE"

    def test_write_stack_usages_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        parent = _parent()
        w.writeStackUsages(parent, ["unsupported"])
        assert len(parent) == 1
        assert parent[0].tag == "STACK-USAGES"


class TestSetResourceConsumption:
    def test_set_resource_consumption_none(self, writer):
        parent = _parent()
        writer.setResourceConsumption(parent, None)
        assert len(parent) == 0

    def test_set_resource_consumption_with_value(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        consumption = ResourceConsumption(pkg, "RC")
        consumption.createMemorySection("Sec")
        consumption.createRoughEstimateStackUsage("U")
        parent = _parent()
        writer.setResourceConsumption(parent, consumption)
        assert len(parent) == 1
        rc = parent[0]
        assert rc.tag == "RESOURCE-CONSUMPTION"
        assert rc.find("SHORT-NAME").text == "RC"
        assert rc.find("MEMORY-SECTIONS") is not None
        assert rc.find("STACK-USAGES") is not None


class TestWriteImplementation:
    def test_write_implementation_basic(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = SwcImplementation(pkg, "Impl")
        impl.setProgrammingLanguage(_make_literal("C"))
        impl.setSwVersion(_make_literal("1.0"))
        impl.setUsedCodeGenerator(_make_literal("Gen"))
        impl.setVendorId(_make_positive_int("10"))
        impl.setSwcBswMappingRef(_make_ref("SWC-BSW-MAPPING", "/Map"))
        parent = _parent()
        writer.writeImplementation(parent, impl)
        assert parent.find("SHORT-NAME").text == "Impl"
        assert parent.find("PROGRAMMING-LANGUAGE").text == "C"
        assert parent.find("SW-VERSION").text == "1.0"
        assert parent.find("USED-CODE-GENERATOR").text == "Gen"
        assert parent.find("VENDOR-ID").text == "10"
        assert parent.find("SWC-BSW-MAPPING-REF").text == "/Map"

    def test_write_implementation_with_code_and_resource(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = SwcImplementation(pkg, "Impl")
        impl.swVersion = None
        impl.vendorId = None
        impl.createCodeDescriptor("Code1")
        impl.createResourceConsumption("RC")
        parent = _parent()
        writer.writeImplementation(parent, impl)
        assert parent.find("CODE-DESCRIPTORS/CODE/SHORT-NAME").text == "Code1"
        assert parent.find("RESOURCE-CONSUMPTION/SHORT-NAME").text == "RC"


class TestWriteSwcImplementation:
    def test_write_swc_implementation(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        impl = SwcImplementation(pkg, "Impl")
        impl.swVersion = None
        impl.vendorId = None
        impl.setBehaviorRef(_make_ref("SWC-INTERNAL-BEHAVIOR", "/Beh"))
        parent = _parent()
        writer.writeSwcImplementation(parent, impl)
        assert len(parent) == 1
        swc = parent[0]
        assert swc.tag == "SWC-IMPLEMENTATION"
        assert swc.find("SHORT-NAME").text == "Impl"
        assert swc.find("BEHAVIOR-REF").text == "/Beh"


class TestWriteEndToEndDescriptionDataIds:
    def test_write_e2e_data_ids_empty(self, writer):
        desc = EndToEndDescription()
        parent = _parent()
        writer.writeEndToEndDescriptionDataIds(parent, desc)
        assert len(parent) == 0

    def test_write_e2e_data_ids_with_values(self, writer):
        desc = EndToEndDescription()
        desc.addDataId(_make_positive_int("1"))
        desc.addDataId(_make_positive_int("2"))
        parent = _parent()
        writer.writeEndToEndDescriptionDataIds(parent, desc)
        assert len(parent) == 1
        ids_tag = parent[0]
        assert ids_tag.tag == "DATA-IDS"
        ids = ids_tag.findall("DATA-ID")
        assert [i.text for i in ids] == ["1", "2"]


class TestSetEndToEndDescription:
    def test_set_e2e_description_none(self, writer):
        parent = _parent()
        writer.setEndToEndDescription(parent, "KEY", None)
        assert len(parent) == 0

    def test_set_e2e_description_with_value(self, writer):
        desc = EndToEndDescription()
        desc.setCategory(_make_literal("Cat"))
        desc.addDataId(_make_positive_int("5"))
        desc.setDataIdMode(_make_positive_int("2"))
        desc.setDataLength(_make_positive_int("64"))
        desc.setMaxDeltaCounterInit(_make_positive_int("3"))
        desc.setCrcOffset(_make_positive_int("0"))
        desc.setCounterOffset(_make_positive_int("4"))
        parent = _parent()
        writer.setEndToEndDescription(parent, "END-TO-END-PROFILE", desc)
        assert len(parent) == 1
        profile = parent[0]
        assert profile.tag == "END-TO-END-PROFILE"
        assert profile.find("CATEGORY").text == "Cat"
        assert profile.find("DATA-IDS/DATA-ID").text == "5"
        assert profile.find("DATA-ID-MODE").text == "2"
        assert profile.find("DATA-LENGTH").text == "64"
        assert profile.find("MAX-DELTA-COUNTER-INIT").text == "3"
        assert profile.find("CRC-OFFSET").text == "0"
        assert profile.find("COUNTER-OFFSET").text == "4"


class TestSetVariableDataPrototypeInSystemInstanceRef:
    def test_set_variable_ref_none(self, writer):
        parent = _parent()
        writer.setVariableDataPrototypeInSystemInstanceRef(
            parent, "KEY", None
        )
        assert len(parent) == 0

    def test_set_variable_ref_with_value(self, writer):
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.addContextComponentRef(_make_ref("SW-COMPONENT-PROTOTYPE", "/c1"))
        iref.setContextCompositionRef(_make_ref("COMPOSITION-SW-COMPONENT-TYPE", "/comp"))  # noqa: E501
        iref.setContextPortRef(_make_ref("P-PORT-PROTOTYPE", "/port"))
        iref.setTargetDataPrototypeRef(_make_ref("VARIABLE-DATA-PROTOTYPE", "/t"))  # noqa: E501
        parent = _parent()
        writer.setVariableDataPrototypeInSystemInstanceRef(
            parent, "SENDER-IREF", iref
        )
        assert len(parent) == 1
        ref_tag = parent[0]
        assert ref_tag.tag == "SENDER-IREF"
        ctx_refs = ref_tag.findall("CONTEXT-COMPONENT-REF")
        assert len(ctx_refs) == 1
        assert ctx_refs[0].text == "/c1"
        assert ref_tag.find("CONTEXT-COMPOSITION-REF").text == "/comp"
        assert ref_tag.find("CONTEXT-PORT-REF").text == "/port"
        assert ref_tag.find("TARGET-DATA-PROTOTYPE-REF").text == "/t"


class TestWriteEndToEndProtectionVariablePrototype:
    def test_write_e2e_prototype_none(self, writer):
        parent = _parent()
        writer.writeEndToEndProtectionVariablePrototype(parent, None)
        assert len(parent) == 0

    def test_write_e2e_prototype_with_sender_and_receivers(self, writer):
        prototype = EndToEndProtectionVariablePrototype()
        sender = VariableDataPrototypeInSystemInstanceRef()
        sender.setTargetDataPrototypeRef(_make_ref("VARIABLE-DATA-PROTOTYPE", "/s"))  # noqa: E501
        prototype.senderIRef = sender
        receiver = VariableDataPrototypeInSystemInstanceRef()
        receiver.setTargetDataPrototypeRef(_make_ref("VARIABLE-DATA-PROTOTYPE", "/r"))  # noqa: E501
        prototype.addReceiverIref(receiver)
        parent = _parent()
        writer.writeEndToEndProtectionVariablePrototype(parent, prototype)
        assert len(parent) == 1
        proto_tag = parent[0]
        assert proto_tag.tag == "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE"
        assert proto_tag.find(".//SENDER-IREF") is not None
        receivers = proto_tag.find("RECEIVER-IREFS")
        assert receivers is not None
        assert receivers.find("RECEIVER-IREF") is not None


class TestWriteEndToEndProtectionVariablePrototypes:
    def test_write_e2e_prototypes_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        prot = set_.createEndToEndProtection("P")
        parent = _parent()
        writer.writeEndToEndProtectionEndToEndProtectionVariablePrototypes(
            parent, prot
        )
        assert len(parent) == 0

    def test_write_e2e_prototypes_with_prototype(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        prot = set_.createEndToEndProtection("P")
        prototype = EndToEndProtectionVariablePrototype()
        prototype.senderIRef = VariableDataPrototypeInSystemInstanceRef()
        prot.addEndToEndProtectionVariablePrototype(prototype)
        parent = _parent()
        writer.writeEndToEndProtectionEndToEndProtectionVariablePrototypes(
            parent, prot
        )
        assert len(parent) == 1
        assert parent[0].tag == "END-TO-END-PROTECTION-VARIABLE-PROTOTYPES"

    def test_write_e2e_prototypes_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        prot = set_.createEndToEndProtection("P")
        prot.addEndToEndProtectionVariablePrototype("bad")
        parent = _parent()
        w.writeEndToEndProtectionEndToEndProtectionVariablePrototypes(
            parent, prot
        )
        assert len(parent) == 1


class TestWriteEndToEndProtectionISignalIPdu:
    def test_write_e2e_ipdu_none(self, writer):
        parent = _parent()
        writer.writeEndToEndProtectionISignalIPdu(parent, None)
        assert len(parent) == 0

    def test_write_e2e_ipdu_with_value(self, writer):
        ipdu = EndToEndProtectionISignalIPdu()
        ipdu.setDataOffset(_make_positive_int("8"))
        ipdu.setISignalGroupRef(_make_ref("I-SIGNAL-GROUP", "/sg"))
        ipdu.setISignalIPduRef(_make_ref("I-SIGNAL-I-PDU", "/ipdu"))
        parent = _parent()
        writer.writeEndToEndProtectionISignalIPdu(parent, ipdu)
        assert len(parent) == 1
        ipdu_tag = parent[0]
        assert ipdu_tag.tag == "END-TO-END-PROTECTION-I-SIGNAL-I-PDU"
        assert ipdu_tag.find("DATA-OFFSET").text == "8"
        assert ipdu_tag.find("I-SIGNAL-GROUP-REF").text == "/sg"
        assert ipdu_tag.find("I-SIGNAL-I-PDU-REF").text == "/ipdu"


class TestWriteEndToEndProtectionISignalIPdus:
    def test_write_e2e_ipdus_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        prot = set_.createEndToEndProtection("P")
        parent = _parent()
        writer.writeEndToEndProtectionEndToEndProtectionISignalIPdus(
            parent, prot
        )
        assert len(parent) == 0

    def test_write_e2e_ipdus_with_ipdu(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        prot = set_.createEndToEndProtection("P")
        ipdu = EndToEndProtectionISignalIPdu()
        ipdu.setDataOffset(_make_positive_int("4"))
        prot.addEndToEndProtectionISignalIPdu(ipdu)
        parent = _parent()
        writer.writeEndToEndProtectionEndToEndProtectionISignalIPdus(
            parent, prot
        )
        assert len(parent) == 1
        assert parent[0].tag == "END-TO-END-PROTECTION-I-SIGNAL-I-PDUS"

    def test_write_e2e_ipdus_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        prot = set_.createEndToEndProtection("P")
        prot.addEndToEndProtectionISignalIPdu("bad")
        parent = _parent()
        w.writeEndToEndProtectionEndToEndProtectionISignalIPdus(
            parent, prot
        )
        assert len(parent) == 1


class TestWriteEndToEndProtection:
    def test_write_e2e_protection_none(self, writer):
        parent = _parent()
        writer.writeEndToEndProtection(parent, None)
        assert len(parent) == 0

    def test_write_e2e_protection_full(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        prot = set_.createEndToEndProtection("P")
        profile = EndToEndDescription()
        profile.setCategory(_make_literal("Cat"))
        prot.setEndToEndProfile(profile)
        ipdu = EndToEndProtectionISignalIPdu()
        ipdu.setDataOffset(_make_positive_int("2"))
        prot.addEndToEndProtectionISignalIPdu(ipdu)
        prototype = EndToEndProtectionVariablePrototype()
        prototype.senderIRef = VariableDataPrototypeInSystemInstanceRef()
        prot.addEndToEndProtectionVariablePrototype(prototype)
        parent = _parent()
        writer.writeEndToEndProtection(parent, prot)
        assert len(parent) == 1
        prot_tag = parent[0]
        assert prot_tag.tag == "END-TO-END-PROTECTION"
        assert prot_tag.find("SHORT-NAME").text == "P"
        assert prot_tag.find("END-TO-END-PROFILE/CATEGORY").text == "Cat"
        assert prot_tag.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS") is not None  # noqa: E501
        assert prot_tag.find("END-TO-END-PROTECTION-VARIABLE-PROTOTYPES") is not None  # noqa: E501


class TestWriteEndToEndProtections:
    def test_write_e2e_protections_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        parent = _parent()
        writer.writeEndToEndProtections(parent, set_)
        assert len(parent) == 0

    def test_write_e2e_protections_with_protection(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("Set")
        set_.createEndToEndProtection("Prot1")
        parent = _parent()
        writer.writeEndToEndProtections(parent, set_)
        assert len(parent) == 1
        assert parent[0].tag == "END-TO-END-PROTECTIONS"
        assert parent[0][0].tag == "END-TO-END-PROTECTION"


class TestWriteEndToEndProtectionSet:
    def test_write_e2e_protection_set(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        set_ = pkg.createEndToEndProtectionSet("MySet")
        set_.createEndToEndProtection("Prot1")
        parent = _parent()
        writer.writeEndToEndProtectionSet(parent, set_)
        assert len(parent) == 1
        set_tag = parent[0]
        assert set_tag.tag == "END-TO-END-PROTECTION-SET"
        assert set_tag.find("SHORT-NAME").text == "MySet"
        assert set_tag.find("END-TO-END-PROTECTIONS") is not None


class TestWriteAutosarDataPrototype:
    def test_write_autosar_data_prototype(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        proto = VariableDataPrototype(pkg, "Var")
        proto.setTypeTRef(_make_ref("SW-BASE-TYPE", "/Type"))
        parent = _parent()
        writer.writeAutosarDataPrototype(parent, proto)
        assert parent.find("SHORT-NAME").text == "Var"
        assert parent.find("TYPE-TREF").text == "/Type"


class TestWriteVariableDataPrototype:
    def test_write_variable_data_prototype(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        proto = VariableDataPrototype(pkg, "Var")
        proto.setTypeTRef(_make_ref("SW-BASE-TYPE", "/Type"))
        parent = _parent()
        writer.writeVariableDataPrototype(parent, proto)
        assert len(parent) == 1
        var_tag = parent[0]
        assert var_tag.tag == "VARIABLE-DATA-PROTOTYPE"
        assert var_tag.find("SHORT-NAME").text == "Var"
        assert var_tag.find("TYPE-TREF").text == "/Type"


class TestWriteSenderReceiverInterfaceDataElements:
    def test_write_sr_data_elements_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        parent = _parent()
        writer.writeSenderReceiverInterfaceDataElements(parent, sr)
        assert len(parent) == 0

    def test_write_sr_data_elements_with_element(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        sr.createDataElement("Elem")
        parent = _parent()
        writer.writeSenderReceiverInterfaceDataElements(parent, sr)
        assert len(parent) == 1
        elements = parent[0]
        assert elements.tag == "DATA-ELEMENTS"
        assert elements[0].tag == "VARIABLE-DATA-PROTOTYPE"

    def test_write_sr_data_elements_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        sr = MagicMock()
        sr.getDataElements.return_value = ["unsupported"]
        parent = _parent()
        w.writeSenderReceiverInterfaceDataElements(parent, sr)
        assert len(parent) == 1


class TestWriteSenderReceiverInterfaceInvalidationPolicies:
    def test_write_sr_invalidation_policies_empty(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        parent = _parent()
        writer.writeSenderReceiverInterfaceInvalidationPolicies(parent, sr)
        assert len(parent) == 0

    def test_write_sr_invalidation_policies_with_policy(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        policy = sr.createInvalidationPolicy()
        policy.setDataElementRef(_make_ref("VARIABLE-DATA-PROTOTYPE", "/de"))
        policy.setHandleInvalid(_make_literal("DISABLE"))
        parent = _parent()
        writer.writeSenderReceiverInterfaceInvalidationPolicies(parent, sr)
        assert len(parent) == 1
        policies_tag = parent[0]
        assert policies_tag.tag == "INVALIDATION-POLICYS"
        policy_tag = policies_tag[0]
        assert policy_tag.tag == "INVALIDATION-POLICY"
        assert policy_tag.find("DATA-ELEMENT-REF").text == "/de"
        assert policy_tag.find("HANDLE-INVALID").text == "DISABLE"


class TestWriteSenderReceiverInterface:
    def test_write_sr_interface(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        is_service = ARBoolean()
        is_service.setValue("true")
        sr.setIsService(is_service)
        sr.createDataElement("Elem")
        sr.createInvalidationPolicy()
        parent = _parent()
        writer.writeSenderReceiverInterface(parent, sr)
        assert len(parent) == 1
        sr_tag = parent[0]
        assert sr_tag.tag == "SENDER-RECEIVER-INTERFACE"
        assert sr_tag.find("SHORT-NAME").text == "SR"
        assert sr_tag.find("IS-SERVICE").text == "true"
        assert sr_tag.find("DATA-ELEMENTS") is not None
        assert sr_tag.find("INVALIDATION-POLICYS") is not None


class TestWriteModeDeclarationGroupPrototype:
    def test_write_mode_declaration_group_prototype(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        proto = ModeDeclarationGroupPrototype(pkg, "Mode")
        proto.setTypeTRef(_make_ref("MODE-DECLARATION-GROUP", "/Mode"))
        parent = _parent()
        writer.writeModeDeclarationGroupPrototype(parent, proto)
        assert len(parent) == 1
        mode_tag = parent[0]
        assert mode_tag.tag == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert mode_tag.find("SHORT-NAME").text == "Mode"
        assert mode_tag.find("TYPE-TREF").text == "/Mode"
