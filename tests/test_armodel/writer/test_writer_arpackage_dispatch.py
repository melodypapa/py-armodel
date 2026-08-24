"""Tests for writer ARPackage dispatch and top-level methods."""

import os
import tempfile
import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ReferenceBase,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    ARLiteral,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion
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
    return ET.Element("ELEMENTS")


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _literal(text):
    lit = ARLiteral()
    lit.setValue(text)
    return lit


def _boolean(val):
    b = ARBoolean()
    b.setValue(val)
    return b


ELEMENT_TYPES_AND_TAGS = [
    ("ComplexDeviceDriverSwComponentType", "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE"),
    ("CompositionSwComponentType", "COMPOSITION-SW-COMPONENT-TYPE"),
    ("ApplicationPrimitiveDataType", "APPLICATION-PRIMITIVE-DATA-TYPE"),
    ("ApplicationRecordDataType", "APPLICATION-RECORD-DATA-TYPE"),
    ("SwBaseType", "SW-BASE-TYPE"),
    ("CompuMethod", "COMPU-METHOD"),
    ("ConstantSpecification", "CONSTANT-SPECIFICATION"),
    ("DataConstr", "DATA-CONSTR"),
    ("EndToEndProtectionSet", "END-TO-END-PROTECTION-SET"),
    ("SenderReceiverInterface", "SENDER-RECEIVER-INTERFACE"),
    ("Unit", "UNIT"),
    ("BswModuleDescription", "BSW-MODULE-DESCRIPTION"),
    ("BswModuleEntry", "BSW-MODULE-ENTRY"),
    ("SwcBswMapping", "SWC-BSW-MAPPING"),
    ("ImplementationDataType", "IMPLEMENTATION-DATA-TYPE"),
    ("ClientServerInterface", "CLIENT-SERVER-INTERFACE"),
    ("ApplicationSwComponentType", "APPLICATION-SW-COMPONENT-TYPE"),
    ("EcuAbstractionSwComponentType", "ECU-ABSTRACTION-SW-COMPONENT-TYPE"),
    ("SensorActuatorSwComponentType", "SENSOR-ACTUATOR-SW-COMPONENT-TYPE"),
    ("NvBlockSwComponentType", "NV-BLOCK-SW-COMPONENT-TYPE"),
    ("ServiceProxySwComponentType", "SERVICE-PROXY-SW-COMPONENT-TYPE"),
    ("ApplicationArrayDataType", "APPLICATION-ARRAY-DATA-TYPE"),
    ("SwRecordLayout", "SW-RECORD-LAYOUT"),
    ("SwAddrMethod", "SW-ADDR-METHOD"),
    ("ServiceSwComponentType", "SERVICE-SW-COMPONENT-TYPE"),
    ("DataTypeMappingSet", "DATA-TYPE-MAPPING-SET"),
    ("ModeDeclarationGroup", "MODE-DECLARATION-GROUP"),
    ("ModeSwitchInterface", "MODE-SWITCH-INTERFACE"),
    ("SwcTiming", "SWC-TIMING"),
    ("LinUnconditionalFrame", "LIN-UNCONDITIONAL-FRAME"),
    ("NmConfig", "NM-CONFIG"),
    ("NmPdu", "NM-PDU"),
    ("NPdu", "N-PDU"),
    ("DcmIPdu", "DCM-I-PDU"),
    ("SecuredIPdu", "SECURED-I-PDU"),
    ("CanTpConfig", "CAN-TP-CONFIG"),
    ("LinTpConfig", "LIN-TP-CONFIG"),
    ("LinCluster", "LIN-CLUSTER"),
    ("CanCluster", "CAN-CLUSTER"),
    ("CanFrame", "CAN-FRAME"),
    ("Gateway", "GATEWAY"),
    ("ISignal", "I-SIGNAL"),
    ("System", "SYSTEM"),
    ("EcuInstance", "ECU-INSTANCE"),
    ("ISignalIPdu", "I-SIGNAL-I-PDU"),
    ("SystemSignal", "SYSTEM-SIGNAL"),
    ("ParameterInterface", "PARAMETER-INTERFACE"),
    ("NvDataInterface", "NV-DATA-INTERFACE"),
    ("GenericEthernetFrame", "ETHERNET-FRAME"),
    ("LifeCycleInfoSet", "LIFE-CYCLE-INFO-SET"),
    ("PhysicalDimension", "PHYSICAL-DIMENSION"),
    ("FlatMap", "FLAT-MAP"),
    ("PortInterfaceMappingSet", "PORT-INTERFACE-MAPPING-SET"),
    ("EthernetCluster", "ETHERNET-CLUSTER"),
    ("ISignalIPduGroup", "I-SIGNAL-I-PDU-GROUP"),
    ("DiagnosticConnection", "DIAGNOSTIC-CONNECTION"),
    ("DiagnosticServiceTable", "DIAGNOSTIC-SERVICE-TABLE"),
    ("MultiplexedIPdu", "MULTIPLEXED-I-PDU"),
    ("UserDefinedIPdu", "USER-DEFINED-I-PDU"),
    ("UserDefinedPdu", "USER-DEFINED-PDU"),
    ("GeneralPurposePdu", "GENERAL-PURPOSE-PDU"),
    ("GeneralPurposeIPdu", "GENERAL-PURPOSE-I-PDU"),
    ("SoAdRoutingGroup", "SO-AD-ROUTING-GROUP"),
    ("SomeipSdClientServiceInstanceConfig", "SOME-IP-SD-CLIENT-SERVICE-INSTANCE-CONFIG"),
    ("SomeipSdClientEventGroupTimingConfig", "SOME-IP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG"),
    ("DoIpTpConfig", "DO-IP-TP-CONFIG"),
    ("HwElement", "HW-ELEMENT"),
    ("HwCategory", "HW-CATEGORY"),
    ("HwType", "HW-TYPE"),
    ("DataTransformationSet", "DATA-TRANSFORMATION-SET"),
    ("FlexrayFrame", "FLEXRAY-FRAME"),
    ("ISignalGroup", "I-SIGNAL-GROUP"),
    ("SystemSignalGroup", "SYSTEM-SIGNAL-GROUP"),
    ("FlexrayCluster", "FLEXRAY-CLUSTER"),
    ("Collection", "COLLECTION"),
    ("KeywordSet", "KEYWORD-SET"),
    ("PortPrototypeBlueprint", "PORT-PROTOTYPE-BLUEPRINT"),
    ("ModeDeclarationMappingSet", "MODE-DECLARATION-MAPPING-SET"),
    ("EcucModuleDef", "ECUC-MODULE-DEF"),
    ("EcucDefinitionCollection", "ECUC-DEFINITION-COLLECTION"),
    ("EcucModuleConfigurationValues", "ECUC-MODULE-CONFIGURATION-VALUES"),
    ("SwSystemConst", "SW-SYSTEMCONST"),
    ("SwSystemconstantValueSet", "SW-SYSTEMCONSTANT-VALUE-SET"),
    ("PredefinedVariant", "PREDEFINED-VARIANT"),
    ("PostBuildVariantCriterion", "POST-BUILD-VARIANT-CRITERION"),
    ("McGroup", "MC-GROUP"),
]

ELEMENTS_WITH_SPECIAL_SETUP = {
    "SwcImplementation": lambda elem: (
        setattr(elem, "swVersion", None),
        setattr(elem, "vendorId", None),
    ),
    "BswImplementation": lambda elem: (
        setattr(elem, "swVersion", None),
        setattr(elem, "vendorId", None),
    ),
}


class TestWriteARPackageElementDispatch:
    @pytest.mark.parametrize("element_type,expected_tag", ELEMENT_TYPES_AND_TAGS)
    def test_dispatch_creates_correct_xml_tag(self, writer, element_type, expected_tag):
        pkg = _pkg()
        create_method = f"create{element_type}"
        if hasattr(pkg, create_method):
            element = getattr(pkg, create_method)("Elem")
        else:
            raise AttributeError(f"ARPackage has no method {create_method}")
        if element_type in ELEMENTS_WITH_SPECIAL_SETUP:
            ELEMENTS_WITH_SPECIAL_SETUP[element_type](element)
        parent = _parent()
        writer.writeARPackageElement(parent, element)
        assert len(parent) == 1
        assert parent[0].tag == expected_tag
        assert parent[0].find("SHORT-NAME").text == "Elem"


class TestWriteSwcImplementationDispatch:
    def test_swc_implementation_with_setup(self, writer):
        pkg = _pkg()
        impl = pkg.createSwcImplementation("SwcImpl")
        impl.swVersion = None
        impl.vendorId = None
        parent = _parent()
        writer.writeARPackageElement(parent, impl)
        assert len(parent) == 1
        assert parent[0].tag == "SWC-IMPLEMENTATION"


class TestWriteBswImplementationDispatch:
    def test_bsw_implementation_with_setup(self, writer):
        pkg = _pkg()
        impl = pkg.createBswImplementation("BswImpl")
        impl.swVersion = None
        impl.vendorId = None
        parent = _parent()
        writer.writeARPackageElement(parent, impl)
        assert len(parent) == 1
        assert parent[0].tag == "BSW-IMPLEMENTATION"


class TestWriteTriggerInterfaceDispatch:
    def test_trigger_interface_dispatch(self, writer):
        pkg = _pkg()
        trigger_if = pkg.createTriggerInterface("TriggerIf")
        parent = _parent()
        writer.writeARPackageElement(parent, trigger_if)
        assert len(parent) == 0


class TestWriteSecureCommunicationPropsSetDispatch:
    def test_secure_comm_props_set_dispatch(self, writer):
        pkg = _pkg()
        props = pkg.createSecureCommunicationPropsSet("Props")
        parent = _parent()
        writer.writeARPackageElement(parent, props)
        child = parent.find("SECURE-COMMUNICATION-PROPS-SET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Props"


class TestWriteReferenceBases:
    def test_empty_reference_bases(self, writer):
        parent = ET.Element("AR-PACKAGE")
        writer.writeReferenceBases(parent, [])
        assert parent.find("REFERENCE-BASES") is None

    def test_single_reference_base(self, writer):
        parent = ET.Element("AR-PACKAGE")
        base = ReferenceBase()
        base.setShortLabel(_literal("base1"))
        base.setIsDefault(_boolean(True))
        base.setBaseIsThisPackage(_boolean(True))
        writer.writeReferenceBases(parent, [base])
        bases_tag = parent.find("REFERENCE-BASES")
        assert bases_tag is not None
        ref_base = bases_tag.find("REFERENCE-BASE")
        assert ref_base is not None
        assert ref_base.find("SHORT-LABEL").text == "base1"

    def test_multiple_reference_bases(self, writer):
        parent = ET.Element("AR-PACKAGE")
        base1 = ReferenceBase()
        base1.setShortLabel(_literal("base1"))
        base2 = ReferenceBase()
        base2.setShortLabel(_literal("base2"))
        writer.writeReferenceBases(parent, [base1, base2])
        bases_tag = parent.find("REFERENCE-BASES")
        assert bases_tag is not None
        ref_bases = bases_tag.findall("REFERENCE-BASE")
        assert len(ref_bases) == 2


class TestWriteARPackage:
    def test_basic_arpackage(self, writer):
        parent = ET.Element("AUTOSAR")
        pkg = _pkg()
        writer.writeARPackage(parent, pkg)
        assert parent.find("AR-PACKAGE") is not None
        pkg_tag = parent.find("AR-PACKAGE")
        assert pkg_tag.find("SHORT-NAME").text == "Pkg"

    def test_arpackage_with_reference_bases(self, writer):
        parent = ET.Element("AUTOSAR")
        pkg = _pkg()
        base = ReferenceBase()
        base.setShortLabel(_literal("base1"))
        pkg.addReferenceBase(base)
        writer.writeARPackage(parent, pkg)
        pkg_tag = parent.find("AR-PACKAGE")
        assert pkg_tag.find("REFERENCE-BASES") is not None

    def test_arpackage_with_sub_packages(self, writer):
        parent = ET.Element("AUTOSAR")
        pkg = _pkg()
        _sub_pkg = pkg.createARPackage("SubPkg")
        writer.writeARPackage(parent, pkg)
        pkg_tag = parent.find("AR-PACKAGE")
        packages_tag = pkg_tag.find("AR-PACKAGES")
        assert packages_tag is not None
        sub_pkg_tag = packages_tag.find("AR-PACKAGE")
        assert sub_pkg_tag.find("SHORT-NAME").text == "SubPkg"

    def test_arpackage_with_elements(self, writer):
        parent = ET.Element("AUTOSAR")
        pkg = _pkg()
        pkg.createSwBaseType("BaseType")
        writer.writeARPackage(parent, pkg)
        pkg_tag = parent.find("AR-PACKAGE")
        elements_tag = pkg_tag.find("ELEMENTS")
        assert elements_tag is not None
        assert elements_tag.find("SW-BASE-TYPE") is not None


class TestWriteARPackageElements:
    def test_empty_package(self, writer):
        parent = ET.Element("AR-PACKAGE")
        pkg = _pkg()
        writer.writeARPackageElements(parent, pkg)
        assert parent.find("ELEMENTS") is None

    def test_single_element(self, writer):
        parent = ET.Element("AR-PACKAGE")
        pkg = _pkg()
        pkg.createApplicationPrimitiveDataType("DataType")
        writer.writeARPackageElements(parent, pkg)
        elements_tag = parent.find("ELEMENTS")
        assert elements_tag is not None
        assert len(elements_tag) == 1

    def test_multiple_elements(self, writer):
        parent = ET.Element("AR-PACKAGE")
        pkg = _pkg()
        pkg.createSwBaseType("BaseType1")
        pkg.createSwBaseType("BaseType2")
        pkg.createCompuMethod("Compu")
        writer.writeARPackageElements(parent, pkg)
        elements_tag = parent.find("ELEMENTS")
        assert elements_tag is not None
        assert len(elements_tag) == 3
        tags = {child.tag for child in elements_tag}
        assert "SW-BASE-TYPE" in tags
        assert "COMPU-METHOD" in tags


class TestWritePostBuildVariantCriterionRoundTrip:
    def test_round_trip_preserves_compu_method_ref(self, writer, tmp_path):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        criterion = pkg.createPostBuildVariantCriterion("MyCriterion")
        compu_ref = RefType().setValue("/Pkg/CompuMethods/MyCompuMethod")
        compu_ref.setDest("COMPU-METHOD")
        criterion.setCompuMethodRef(compu_ref)

        out_file = str(tmp_path / "postbuild.arxml")
        writer.save(out_file, AUTOSAR.getInstance())

        AUTOSAR.getInstance().new()
        parser = ARXMLParser(options={"warning": True})
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        parser.load(out_file, document)

        re_pkg = document.find("Pkg")
        re_criterion = re_pkg.getElement("MyCriterion", PostBuildVariantCriterion)
        assert re_criterion is not None
        assert re_criterion.getCompuMethodRef().getValue() == "/Pkg/CompuMethods/MyCompuMethod"

    def test_empty_compu_method_ref(self, writer):
        pkg = _pkg()
        criterion = pkg.createPostBuildVariantCriterion("NoRefCriterion")
        parent = _parent()
        writer.writePostBuildVariantCriterion(parent, criterion)
        assert parent[0].find("COMPU-METHOD-REF") is None

    def test_skips_arpackage_elements(self, writer):
        parent = ET.Element("AR-PACKAGE")
        pkg = _pkg()
        pkg.createSwBaseType("BaseType")
        pkg.createARPackage("SubPkg")
        writer.writeARPackageElements(parent, pkg)
        elements_tag = parent.find("ELEMENTS")
        assert elements_tag is not None
        assert len(elements_tag) == 1


class TestWriteARPackages:
    def test_empty_list(self, writer):
        parent = ET.Element("AUTOSAR")
        writer.writeARPackages(parent, [])
        assert parent.find("AR-PACKAGES") is None

    def test_single_package(self, writer):
        parent = ET.Element("AUTOSAR")
        pkg = _pkg()
        writer.writeARPackages(parent, [pkg])
        packages_tag = parent.find("AR-PACKAGES")
        assert packages_tag is not None
        assert len(packages_tag) == 1
        assert packages_tag.find("AR-PACKAGE").find("SHORT-NAME").text == "Pkg"

    def test_multiple_packages(self, writer):
        parent = ET.Element("AUTOSAR")
        autosar = AUTOSAR.getInstance()
        pkg1 = autosar.createARPackage("Pkg1")
        pkg2 = autosar.createARPackage("Pkg2")
        writer.writeARPackages(parent, [pkg1, pkg2])
        packages_tag = parent.find("AR-PACKAGES")
        assert packages_tag is not None
        pkgs = packages_tag.findall("AR-PACKAGE")
        assert len(pkgs) == 2
        names = [p.find("SHORT-NAME").text for p in pkgs]
        assert names == ["Pkg1", "Pkg2"]


class TestSave:
    def _find_child(self, parent, tag_name):
        for child in parent:
            if tag_name in child.tag:
                return child
        return None

    def test_save_creates_file(self, writer):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("TestPkg")
        pkg.createSwBaseType("MyBaseType")
        pkg.createApplicationPrimitiveDataType("MyDataType")
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            writer.save(tmp_path, autosar)
            assert os.path.exists(tmp_path)
            tree = ET.parse(tmp_path)
            root = tree.getroot()
            assert "AUTOSAR" in root.tag
            pkgs = self._find_child(root, "AR-PACKAGES")
            assert pkgs is not None
            pkg_tag = self._find_child(pkgs, "AR-PACKAGE")
            assert pkg_tag is not None
            short_name = self._find_child(pkg_tag, "SHORT-NAME")
            assert short_name.text == "TestPkg"
            elements_tag = self._find_child(pkg_tag, "ELEMENTS")
            assert elements_tag is not None
            assert len(elements_tag) >= 2
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    def test_save_with_nested_packages(self, writer):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg1 = autosar.createARPackage("RootPkg")
        pkg2 = pkg1.createARPackage("SubPkg")
        pkg2.createSwBaseType("NestedType")
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            writer.save(tmp_path, autosar)
            tree = ET.parse(tmp_path)
            root = tree.getroot()
            pkgs = self._find_child(root, "AR-PACKAGES")
            root_pkg = self._find_child(pkgs, "AR-PACKAGE")
            short_name = self._find_child(root_pkg, "SHORT-NAME")
            assert short_name.text == "RootPkg"
            sub_pkgs = self._find_child(root_pkg, "AR-PACKAGES")
            assert sub_pkgs is not None
            sub_pkg = self._find_child(sub_pkgs, "AR-PACKAGE")
            short_name = self._find_child(sub_pkg, "SHORT-NAME")
            assert short_name.text == "SubPkg"
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    def test_save_with_schema_location(self, writer):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        autosar.schema_location = "http://autosar.org/schema/r4.0 custom.xsd"
        pkg = autosar.createARPackage("Pkg")
        pkg.createSwBaseType("Base")
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            writer.save(tmp_path, autosar)
            tree = ET.parse(tmp_path)
            root = tree.getroot()
            schema_loc = None
            for key in root.attrib:
                if "schemaLocation" in key:
                    schema_loc = root.attrib[key]
                    break
            assert schema_loc is not None
            assert "custom.xsd" in schema_loc
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    def test_save_with_multiple_element_types(self, writer):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("MixedPkg")
        pkg.createSwBaseType("BaseType")
        pkg.createCompuMethod("CompuMethod")
        pkg.createUnit("Unit")
        pkg.createSenderReceiverInterface("SRInterface")
        pkg.createClientServerInterface("CSInterface")
        pkg.createApplicationPrimitiveDataType("AppDataType")
        pkg.createImplementationDataType("ImplDataType")
        pkg.createConstantSpecification("ConstSpec")
        pkg.createDataConstr("DataConstr")
        pkg.createBswModuleDescription("BswDesc")
        pkg.createEndToEndProtectionSet("E2ESet")
        pkg.createDataTypeMappingSet("DataTypeMap")
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            writer.save(tmp_path, autosar)
            tree = ET.parse(tmp_path)
            root = tree.getroot()
            pkgs = self._find_child(root, "AR-PACKAGES")
            pkg_tag = self._find_child(pkgs, "AR-PACKAGE")
            elements = self._find_child(pkg_tag, "ELEMENTS")
            assert elements is not None
            child_tags = {child.tag for child in elements}
            expected_tags = {
                "SW-BASE-TYPE",
                "COMPU-METHOD",
                "UNIT",
                "SENDER-RECEIVER-INTERFACE",
                "CLIENT-SERVER-INTERFACE",
                "APPLICATION-PRIMITIVE-DATA-TYPE",
                "IMPLEMENTATION-DATA-TYPE",
                "CONSTANT-SPECIFICATION",
                "DATA-CONSTR",
                "BSW-MODULE-DESCRIPTION",
                "END-TO-END-PROTECTION-SET",
                "DATA-TYPE-MAPPING-SET",
            }
            found_tags = set()
            for tag in child_tags:
                for expected in expected_tags:
                    if expected in tag:
                        found_tags.add(expected)
            assert expected_tags.issubset(found_tags)
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
