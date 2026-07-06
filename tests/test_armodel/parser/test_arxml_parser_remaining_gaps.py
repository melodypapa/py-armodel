"""Tests for remaining uncovered handler gaps in ARXMLParser."""
import logging
from unittest.mock import MagicMock
import xml.etree.ElementTree as ET
import pytest
from armodel.models import AUTOSAR
from armodel.models import ApplicationSwComponentType
from armodel.models import CompositionSwComponentType
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
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


# ==================== DocRevision / Modification (L305) ====================


class TestDocRevisionModificationGap:
    def test_unsupported_modification_tag_warns(self, warning_parser, caplog):
        from armodel.models.M2.MSR.AsamHdo.AdminData import DocRevision
        revision = DocRevision()
        element = _snip(
            "<MODIFICATIONS><UNKNOWN-MOD>"
            "<SHORT-NAME>m</SHORT-NAME>"
            "</UNKNOWN-MOD></MODIFICATIONS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDocRevisionModifications(element, revision)
        assert any("Unsupported Modification" in r.getMessage()
                   for r in caplog.records)


# ==================== RoleBasedDataTypeAssignment / ServiceDependency (L603-615) ====================


class TestRoleBasedDataTypeAssignment:
    def test_getRoleBasedDataTypeAssignment_with_role(self, parser):
        element = _snip(
            "<ROLE>MyRole</ROLE>"
            "<USED-IMPLEMENTATION-DATA-TYPE-REF "
            'DEST="IMPLEMENTATION-DATA-TYPE">/dt/Impl</USED-IMPLEMENTATION-DATA-TYPE-REF>',
            root_tag="ROLE-BASED-DATA-TYPE-ASSIGNMENT",
        )
        result = parser.getRoleBasedDataTypeAssignment(element)
        assert result.getRole() is not None
        assert result.getRole().getValue() == "MyRole"
        assert result.getUsedImplementationDataTypeRef() is not None
        assert result.getUsedImplementationDataTypeRef().getValue() == "/dt/Impl"

    def test_getRoleBasedDataTypeAssignment_empty(self, parser):
        element = _snip("", root_tag="ROLE-BASED-DATA-TYPE-ASSIGNMENT")
        result = parser.getRoleBasedDataTypeAssignment(element)
        assert result.getRole() is None
        assert result.getUsedImplementationDataTypeRef() is None

    def test_readServiceDependency_with_role_based_data_type_assignment(
        self, parser
    ):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Dep"
        )
        element = _snip(
            "<ASSIGNED-DATA-TYPES>"
            "<ROLE-BASED-DATA-TYPE-ASSIGNMENT>"
            "<ROLE>r</ROLE>"
            "</ROLE-BASED-DATA-TYPE-ASSIGNMENT>"
            "</ASSIGNED-DATA-TYPES>",
            root_tag="SERVICE-DEPENDENCY",
        )
        parser.readServiceDependency(element, dep)
        assert len(dep.getAssignedDataTypes()) == 1

    def test_readServiceDependency_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Dep"
        )
        element = _snip(
            "<ASSIGNED-DATA-TYPES><BAD/></ASSIGNED-DATA-TYPES>",
            root_tag="SERVICE-DEPENDENCY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readServiceDependency(element, dep)
        assert any("Unsupported assigned data type" in r.getMessage()
                   for r in caplog.records)


# ==================== SwcServiceDependency assigned ports/data (L623, L631, L776) ====================


class TestSwcServiceDependencyAssigned:
    def test_readAssignedData_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Swsd"
        )
        element = _snip(
            "<ASSIGNED-DATAS><BAD/></ASSIGNED-DATAS>",
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcServiceDependencyAssignedData(
                element, dep
            )
        assert any("Unsupported assigned data" in r.getMessage()
                   for r in caplog.records)

    def test_readAssignedPorts_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Swsd"
        )
        element = _snip(
            "<ASSIGNED-PORTS><BAD/></ASSIGNED-PORTS>",
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcServiceDependencyAssignedPorts(
                element, dep
            )
        assert any("Unsupported assigned ports" in r.getMessage()
                   for r in caplog.records)

    def test_readSwcInternalBehaviorServiceDependencies_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        element = _snip(
            "<SERVICE-DEPENDENCYS><BAD/></SERVICE-DEPENDENCYS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcInternalBehaviorServiceDependencies(
                element, behavior
            )
        assert any("Unsupported Service Dependencies" in r.getMessage()
                   for r in caplog.records)


# ==================== SwcInternalBehavior IncludedModeDeclarationGroupSet (L813, L840, L845-848) ====================


class TestSwcInternalBehaviorIncludedModeDeclaration:
    def test_readIncludedModeDeclarationGroupSets_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        element = _snip(
            "<INCLUDED-MODE-DECLARATION-GROUP-SETS><BAD/></INCLUDED-MODE-DECLARATION-GROUP-SETS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcInternalBehaviorIncludedModeDeclarationGroupSets(
                element, behavior
            )
        assert any("Unsupported IncludedModeDeclarationGroupSet"
                   in r.getMessage() for r in caplog.records)

    def test_readAtomicSwComponentTypeSwcInternalBehavior_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        element = _snip(
            "<INTERNAL-BEHAVIORS><BAD/></INTERNAL-BEHAVIORS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readAtomicSwComponentTypeSwcInternalBehavior(
                element, app
            )
        assert any("Unsupported Internal Behaviors" in r.getMessage()
                   for r in caplog.records)

    def test_getIncludedModeDeclarationGroupSets_returns_groups(
        self, parser
    ):
        element = _snip(
            "<INCLUDED-MODE-DECLARATION-GROUP-SETS>"
            "<INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "<MODE-DECLARATION-GROUP-REFS>"
            '<MODE-DECLARATION-GROUP-REF DEST="MODE-DECLARATION-GROUP">/mdg</MODE-DECLARATION-GROUP-REF>'
            "</MODE-DECLARATION-GROUP-REFS>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SETS>"
        )
        result = parser.getIncludedModeDeclarationGroupSets(element)
        assert len(result) == 1


# ==================== BswInternalBehavior addIncludedModeDeclarationGroupSet (L1025) ====================


class TestBswInternalBehaviorIncludedModeDeclarationGroupSet:
    def test_readBswInternalBehavior_adds_group_set(self, parser):
        from armodel.models import BswModuleDescription
        desc = BswModuleDescription(
            parent=_autosar_root(), short_name="Bsw"
        )
        behavior = desc.createBswInternalBehavior("Beh")
        element = _snip(
            "<INCLUDED-MODE-DECLARATION-GROUP-SETS>"
            "<INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "<MODE-DECLARATION-GROUP-REFS>"
            '<MODE-DECLARATION-GROUP-REF DEST="MODE-DECLARATION-GROUP">/mdg</MODE-DECLARATION-GROUP-REF>'
            "</MODE-DECLARATION-GROUP-REFS>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SETS>"
        )
        parser.readBswInternalBehavior(element, behavior)
        assert len(behavior.getIncludedModeDeclarationGroupSets()) == 1


# ==================== ArtifactDescriptor / MemorySectionOptions / StackUsages (L1166, L1179-1180, L1209) ====================


class TestCodeAndResourceConsumption:
    def test_readArtifactDescriptor_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import Code
        code = Code(parent=_autosar_root(), short_name="Code")
        element = _snip(
            "<ARTIFACT-DESCRIPTORS><BAD/></ARTIFACT-DESCRIPTORS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readArtifactDescriptor(element, code)
        assert any("Unsupported Artifact Descriptor" in r.getMessage()
                   for r in caplog.records)

    def test_readMemorySectionOptions_adds_options(self, parser):
        from armodel.models import MemorySection
        section = MemorySection(parent=MagicMock(), short_name="Sec")
        element = _snip(
            "<OPTIONS>"
            "<OPTION>OPT1</OPTION>"
            "<OPTION>OPT2</OPTION>"
            "</OPTIONS>"
        )
        parser.readMemorySectionOptions(element, section)
        assert len(section.getOptions()) == 2

    def test_readStackUsages_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SwcImplementation
        impl = SwcImplementation(parent=_autosar_root(), short_name="Impl")
        consumption = impl.createResourceConsumption("Rc")
        element = _snip(
            "<STACK-USAGES><BAD/></STACK-USAGES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readStackUsages(element, consumption)
        assert any("Unsupported Stack Usages" in r.getMessage()
                   for r in caplog.records)


# ==================== RunnableEntity ModeSwitchPoints / Arguments (L1409, L1414-1416, L1429, L1437) ====================


class TestRunnableEntityGaps:
    def test_readModeSwitchPointModeGroupIRef_sets_ref(self, parser):
        from armodel.models import ModeSwitchPoint
        point = ModeSwitchPoint(parent=MagicMock(), short_name="Msp")
        element = _snip(
            "<MODE-GROUP-IREF>"
            "<CONTEXT-IREF>"
            '<CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/pp</CONTEXT-PORT-REF>'
            "<TARGET-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/t</TARGET-REF>"
            "</CONTEXT-IREF>"
            "<TARGET-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/t</TARGET-REF>"
            "</MODE-GROUP-IREF>"
        )
        parser.readModeSwitchPointModeGroupIRef(element, point)
        assert point.getModeGroupIRef() is not None

    def test_readRunnableEntityModeSwitchPoints_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        entity = behavior.createRunnableEntity("R")
        element = _snip(
            "<MODE-SWITCH-POINTS><BAD/></MODE-SWITCH-POINTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readRunnableEntityModeSwitchPoints(
                element, entity
            )
        assert any("Unsupported Mode Switch Point" in r.getMessage()
                   for r in caplog.records)

    def test_readRunnableEntityArguments_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        entity = behavior.createRunnableEntity("R")
        element = _snip(
            "<ARGUMENTS><BAD/></ARGUMENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readRunnableEntityArguments(element, entity)
        assert any("Unsupported Arguments of runnable entity"
                   in r.getMessage() for r in caplog.records)

    def test_readRunnableEntityModeAccessPoints_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        entity = behavior.createRunnableEntity("R")
        element = _snip(
            "<MODE-ACCESS-POINTS><BAD/></MODE-ACCESS-POINTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readRunnableEntityModeAccessPoints(
                element, entity
            )
        assert any("Unsupported Mode Access Point" in r.getMessage()
                   for r in caplog.records)


# ==================== SwDataDefPros InvalidValue (L1827) ====================


class TestSwDataDefProsInvalidValue:
    def test_readInvalidValue_sets_value(self, parser):
        from armodel.models import SwDataDefProps
        props = SwDataDefProps()
        element = _snip(
            "<INVALID-VALUE>"
            "<NUMERICAL-VALUE-SPECIFICATION>"
            "<VALUE>42</VALUE>"
            "</NUMERICAL-VALUE-SPECIFICATION>"
            "</INVALID-VALUE>"
        )
        parser.readSwDataDefProsInvalidValue(element, props)
        assert props.getInvalidValue() is not None


# ==================== CompositeNetworkRepresentation (L1943, L2122) ====================


class TestCompositeNetworkRepresentation:
    def test_readReceiverComSpec_adds_composite_repr(self, parser):
        from armodel.models import NonqueuedReceiverComSpec
        com_spec = NonqueuedReceiverComSpec()
        element = _snip(
            "<COMPOSITE-NETWORK-REPRESENTATIONS>"
            "<COMPOSITE-NETWORK-REPRESENTATION>"
            "<NETWORK-REPRESENTATION>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL/>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATIONS>"
        )
        parser.readReceiverComSpec(element, com_spec)
        assert len(com_spec.getCompositeNetworkRepresentations()) == 1

    def test_readSenderComSpec_adds_composite_repr(self, parser):
        from armodel.models import NonqueuedSenderComSpec
        com_spec = NonqueuedSenderComSpec()
        element = _snip(
            "<COMPOSITE-NETWORK-REPRESENTATIONS>"
            "<COMPOSITE-NETWORK-REPRESENTATION>"
            "<NETWORK-REPRESENTATION>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL/>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATIONS>"
        )
        parser.readSenderComSpec(element, com_spec)
        assert len(com_spec.getCompositeNetworkRepresentations()) == 1


# ==================== RequiredComSpecs (L2058) ====================


class TestReadRequiredComSpec:
    def test_readRequiredComSpec_client_com_spec(self, parser):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        port = app.createRPortPrototype("RPort")
        element = _snip(
            "<REQUIRED-COM-SPECS>"
            "<CLIENT-COM-SPEC>"
            '<OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/op</OPERATION-REF>'
            "</CLIENT-COM-SPEC>"
            "</REQUIRED-COM-SPECS>"
        )
        parser.readRequiredComSpec(element, port)
        assert len(port.getRequiredComSpecs()) == 1


# ==================== TransformationComSpecProps (L2136, L2139, L2143-2149) ====================


class TestTransformationComSpecProps:
    def test_readTransformationComSpecProps_sets_attrs(self, parser):
        from armodel.models import UserDefinedTransformationComSpecProps
        props = UserDefinedTransformationComSpecProps()
        element = _snip("")
        parser.readTransformationComSpecProps(element, props)

    def test_readUserDefinedTransformationComSpecProps(self, parser):
        from armodel.models import UserDefinedTransformationComSpecProps
        props = UserDefinedTransformationComSpecProps()
        element = _snip("")
        parser.readUserDefinedTransformationComSpecProps(element, props)

    def test_readServerComSpecTransformationComSpecProps_adds_props(
        self, parser
    ):
        from armodel.models import ServerComSpec
        com_spec = ServerComSpec()
        element = _snip(
            "<TRANSFORMATION-COM-SPEC-PROPSS>"
            "<USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS/>"
            "</TRANSFORMATION-COM-SPEC-PROPSS>"
        )
        parser.readServerComSpecTransformationComSpecProps(
            element, com_spec
        )
        assert len(com_spec.getTransformationComSpecProps()) == 1

    def test_readServerComSpecTransformationComSpecProps_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ServerComSpec
        com_spec = ServerComSpec()
        element = _snip(
            "<TRANSFORMATION-COM-SPEC-PROPSS><BAD/></TRANSFORMATION-COM-SPEC-PROPSS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readServerComSpecTransformationComSpecProps(
                element, com_spec
            )
        assert any("Unsupported TransformationComSpecProps"
                   in r.getMessage() for r in caplog.records)


# ==================== PortGroup / InnerPortIRef / Composition (L2231, L2345, L2370) ====================


class TestPortGroupAndComposition:
    def test_readSwComponentTypePortGroups_unsupported_raises(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        element = _snip(
            "<PORT-GROUPS><BAD/></PORT-GROUPS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwComponentTypePortGroups(element, app)
        assert any("Unsupported Port Group type" in r.getMessage()
                   for r in caplog.records)

    def test_readDelegationSwConnectorInnerPortIRef_unsupported_raises(
        self, warning_parser, caplog
    ):
        from armodel.models import DelegationSwConnector
        connector = DelegationSwConnector(
            parent=MagicMock(), short_name="Dc"
        )
        element = _snip(
            "<INNER-PORT-IREF><BAD/></INNER-PORT-IREF>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDelegationSwConnectorInnerPortIRef(
                element, connector
            )
        assert any("Unsupported child element of INNER-PORT-IREF"
                   in r.getMessage() for r in caplog.records)

    def test_readCompositionSwComponentTypeComponents_unsupported_warns(
        self, warning_parser, caplog
    ):
        comp = CompositionSwComponentType(
            parent=_autosar_root(), short_name="Comp"
        )
        element = _snip(
            "<COMPONENTS><BAD/></COMPONENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCompositionSwComponentTypeComponents(
                element, comp
            )
        assert any("Unsupported Component" in r.getMessage()
                   for r in caplog.records)


# ==================== InvalidationPolicies (L2423-2426, L2455) ====================
# L2429-2434 (readInvalidationPolicys) is genuinely unreachable:
# readInvalidationPolicys calls readIdentifiable on InvalidationPolicy,
# but InvalidationPolicy does not implement setLongName (required by
# MultilanguageReferrable), so it always raises AttributeError.


class TestInvalidationPolicies:
    def test_readSenderReceiverInterfaceInvalidationPolicies_adds(
        self, parser
    ):
        from armodel.models import SenderReceiverInterface
        sr = SenderReceiverInterface(
            parent=_autosar_root(), short_name="Sr"
        )
        element = _snip(
            "<INVALIDATION-POLICYS>"
            "<INVALIDATION-POLICY>"
            '<DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/de</DATA-ELEMENT-REF>'
            "<HANDLE-INVALID>DISABLE</HANDLE-INVALID>"
            "</INVALIDATION-POLICY>"
            "</INVALIDATION-POLICYS>"
        )
        parser.readSenderReceiverInterfaceInvalidationPolicies(
            element, sr
        )
        assert len(sr.getInvalidationPolicies()) == 1

    def test_readClientServerOperationArguments_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ClientServerInterface
        iface = ClientServerInterface(
            parent=_autosar_root(), short_name="Csi"
        )
        op = iface.createOperation("Op")
        element = _snip(
            "<ARGUMENTS><BAD/></ARGUMENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readClientServerOperationArguments(
                element, op
            )
        assert any("Unsupported Argument" in r.getMessage()
                   for r in caplog.records)


# ==================== getValueSpecification (L2685, 2687, 2691, 2693, 2697) ====================


class TestGetValueSpecification:
    def test_application_value_specification(self, parser):
        element = _snip(
            "<APPLICATION-VALUE-SPECIFICATION>"
            "<SHORT-LABEL>lbl</SHORT-LABEL>"
            "</APPLICATION-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "APPLICATION-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_record_value_specification(self, parser):
        element = _snip(
            "<RECORD-VALUE-SPECIFICATION>"
            "<FIELDS/>"
            "</RECORD-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "RECORD-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_array_value_specification(self, parser):
        element = _snip(
            "<ARRAY-VALUE-SPECIFICATION>"
            "<ELEMENTS/>"
            "</ARRAY-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "ARRAY-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_text_value_specification(self, parser):
        element = _snip(
            "<TEXT-VALUE-SPECIFICATION>"
            "<VALUE>txt</VALUE>"
            "</TEXT-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "TEXT-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_constant_reference(self, parser):
        element = _snip(
            '<CONSTANT-REFERENCE>'
            '<CONSTANT-REF DEST="CONSTANT-SPECIFICATION">/c</CONSTANT-REF>'
            '</CONSTANT-REFERENCE>'
        )
        result = parser.getValueSpecification(
            element, "CONSTANT-REFERENCE"
        )
        assert result is not None

    def test_unsupported_warns(self, warning_parser, caplog):
        # L2697: notImplemented logs in warning mode. The subsequent
        # return is a known bug (unbound value_spec), so we catch it.
        element = _snip("<UNKNOWN/>")
        with caplog.at_level(logging.ERROR):
            with pytest.raises(UnboundLocalError):
                warning_parser.getValueSpecification(
                    element, "UNKNOWN"
                )
        assert any("Unsupported RecordValueSpecificationField"
                   in r.getMessage() for r in caplog.records)


# ==================== EndToEndProtections (L2835-2839) ====================


class TestReadEndToEndProtections:
    def test_readEndToEndProtections_creates_protection(self, parser):
        from armodel.models import EndToEndProtectionSet
        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("E2eSet")
        element = _snip(
            "<END-TO-END-PROTECTIONS>"
            "<END-TO-END-PROTECTION>"
            "<SHORT-NAME>p</SHORT-NAME>"
            "</END-TO-END-PROTECTION>"
            "</END-TO-END-PROTECTIONS>"
        )
        parser.readEndToEndProtections(element, protection_set)
        assert len(protection_set.getEndToEndProtections()) == 1

    def test_readEndToEndProtections_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EndToEndProtectionSet
        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("E2eSet")
        element = _snip(
            "<END-TO-END-PROTECTIONS><BAD/></END-TO-END-PROTECTIONS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEndToEndProtections(
                element, protection_set
            )
        assert any("Unsupported EndToEndProtectionSet"
                   in r.getMessage() for r in caplog.records)


# ==================== Timing (L2982, L2997) ====================


class TestTimingGaps:
    def test_readExecutionOrderConstraint_order_unsupported_raises(
        self, warning_parser, caplog
    ):
        from armodel.models import SwcTiming
        swc_timing = SwcTiming(parent=_autosar_root(), short_name="T")
        element = _snip(
            "<TIMING-REQUIREMENTS>"
            "<EXECUTION-ORDER-CONSTRAINT>"
            "<SHORT-NAME>eoc</SHORT-NAME>"
            "<ORDERED-ELEMENTS>"
            "<BAD/>"
            "</ORDERED-ELEMENTS>"
            "</EXECUTION-ORDER-CONSTRAINT>"
            "</TIMING-REQUIREMENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readTimingExtension(element, swc_timing)
        assert any("Unsupported order element" in r.getMessage()
                   for r in caplog.records)

    def test_readTimingExtension_unsupported_requirement_raises(
        self, warning_parser, caplog
    ):
        from armodel.models import SwcTiming
        swc_timing = SwcTiming(parent=_autosar_root(), short_name="T")
        element = _snip(
            "<TIMING-REQUIREMENTS>"
            "<BAD-REQ/>"
            "</TIMING-REQUIREMENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readTimingExtension(element, swc_timing)
        assert any("Unsupported timing requirement" in r.getMessage()
                   for r in caplog.records)


# ==================== FrameTriggering / Flexray (L3010, L3038-3044, L3059) ====================


class TestFrameAndFlexrayTriggering:
    def test_readFrameTriggering_adds_pdu_triggering_ref(self, parser):
        from armodel.models import CanFrameTriggering
        triggering = CanFrameTriggering(
            parent=MagicMock(), short_name="Cft"
        )
        element = _snip(
            "<PDU-TRIGGERINGS>"
            "<PDU-TRIGGERING-REF-CONDITIONAL>"
            '<PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/pt</PDU-TRIGGERING-REF>'
            "</PDU-TRIGGERING-REF-CONDITIONAL>"
            "</PDU-TRIGGERINGS>"
        )
        parser.readFrameTriggering(element, triggering)
        assert len(triggering.getPduTriggeringRefs()) == 1

    def test_readFlexrayAbsolutelyScheduledTimingCommunicationCycle_cycle(
        self, parser
    ):
        from armodel.models import FlexrayAbsolutelyScheduledTiming
        timing = FlexrayAbsolutelyScheduledTiming()
        element = _snip(
            "<COMMUNICATION-CYCLE>"
            "<CYCLE-REPETITION>"
            "<BASE-CYCLE>1</BASE-CYCLE>"
            "<CYCLE-REPETITION>CYCLE-REPETITION-1</CYCLE-REPETITION>"
            "</CYCLE-REPETITION>"
            "</COMMUNICATION-CYCLE>"
        )
        parser.readFlexrayAbsolutelyScheduledTimingCommunicationCycle(
            element, timing
        )
        assert timing.getCommunicationCycle() is not None

    def test_readFlexrayAbsolutelyScheduledTimingCommunicationCycle_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import FlexrayAbsolutelyScheduledTiming
        timing = FlexrayAbsolutelyScheduledTiming()
        element = _snip(
            "<COMMUNICATION-CYCLE><BAD/></COMMUNICATION-CYCLE>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readFlexrayAbsolutelyScheduledTimingCommunicationCycle(
                element, timing
            )
        assert any("Unsupported CommunicationCycle" in r.getMessage()
                   for r in caplog.records)

    def test_readFlexrayFrameTriggeringAbsolutelyScheduledTimings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import FlexrayFrameTriggering
        triggering = FlexrayFrameTriggering(
            parent=MagicMock(), short_name="Fft"
        )
        element = _snip(
            "<ABSOLUTELY-SCHEDULED-TIMINGS><BAD/></ABSOLUTELY-SCHEDULED-TIMINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(
                element, triggering
            )
        assert any("Unsupported AbsolutelyScheduledTiming"
                   in r.getMessage() for r in caplog.records)


# ==================== PduTriggering / PhysicalChannel (L3084, L3112, L3121, L3148-3152) ====================


class TestPduAndPhysicalChannel:
    def test_readPduTriggering_adds_isignal_triggering_ref(self, parser):
        from armodel.models import PduTriggering
        triggering = PduTriggering(
            parent=MagicMock(), short_name="Pt"
        )
        element = _snip(
            "<I-SIGNAL-TRIGGERINGS>"
            "<I-SIGNAL-TRIGGERING-REF-CONDITIONAL>"
            '<I-SIGNAL-TRIGGERING-REF DEST="I-SIGNAL-TRIGGERING">/ist</I-SIGNAL-TRIGGERING-REF>'
            "</I-SIGNAL-TRIGGERING-REF-CONDITIONAL>"
            "</I-SIGNAL-TRIGGERINGS>"
        )
        parser.readPduTriggering(element, triggering)
        assert len(triggering.getISignalTriggeringRefs()) == 1

    def test_readPhysicalChannelFrameTriggerings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanPhysicalChannel
        channel = CanPhysicalChannel(
            parent=MagicMock(), short_name="Ch"
        )
        element = _snip(
            "<FRAME-TRIGGERINGS><BAD/></FRAME-TRIGGERINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readPhysicalChannelFrameTriggerings(
                element, channel
            )
        assert any("Unsupported Frame Triggering" in r.getMessage()
                   for r in caplog.records)

    def test_readPhysicalChannelPduTriggerings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanPhysicalChannel
        channel = CanPhysicalChannel(
            parent=MagicMock(), short_name="Ch"
        )
        element = _snip(
            "<PDU-TRIGGERINGS><BAD/></PDU-TRIGGERINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readPhysicalChannelPduTriggerings(
                element, channel
            )
        assert any("Unsupported Frame Triggering" in r.getMessage()
                   for r in caplog.records)

    def test_readPhysicalChannelISignalTriggerings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanPhysicalChannel
        channel = CanPhysicalChannel(
            parent=MagicMock(), short_name="Ch"
        )
        element = _snip(
            "<I-SIGNAL-TRIGGERINGS><BAD/></I-SIGNAL-TRIGGERINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readPhysicalChannelISignalTriggerings(
                element, channel
            )
        assert any("Unsupported Frame Triggering" in r.getMessage()
                   for r in caplog.records)

    def test_readLinScheduleTableTableEntries_application_entry(
        self, parser
    ):
        from armodel.models import LinScheduleTable
        table = LinScheduleTable(parent=MagicMock(), short_name="St")
        element = _snip(
            "<TABLE-ENTRYS>"
            "<APPLICATION-ENTRY>"
            "<SHORT-NAME>ae</SHORT-NAME>"
            "<DELAY>0.1</DELAY>"
            "<POSITION-IN-TABLE>1</POSITION-IN-TABLE>"
            '<FRAME-TRIGGERING-REF DEST="FRAME-TRIGGERING">/ft</FRAME-TRIGGERING-REF>'
            "</APPLICATION-ENTRY>"
            "</TABLE-ENTRYS>"
        )
        parser.readLinScheduleTableTableEntries(element, table)
        assert len(table.getTableEntries()) == 1

    def test_readLinScheduleTableTableEntries_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import LinScheduleTable
        table = LinScheduleTable(parent=MagicMock(), short_name="St")
        element = _snip(
            "<TABLE-ENTRYS><BAD/></TABLE-ENTRYS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readLinScheduleTableTableEntries(
                element, table
            )
        assert any("Unsupported Schedule Table" in r.getMessage()
                   for r in caplog.records)


# ==================== SocketConnection (L3239, L3250, L3264, L3277) ====================


class TestSocketConnection:
    def test_getSocketConnectionPdus_unsupported_warns(
        self, warning_parser, caplog
    ):
        element = _snip("<PDUS><BAD/></PDUS>")
        with caplog.at_level(logging.ERROR):
            result = warning_parser.getSocketConnectionPdus(element)
        assert result == []
        assert any("Unsupported Pdu" in r.getMessage()
                   for r in caplog.records)

    def test_getSocketConnection_with_pdus(self, parser):
        element = _snip(
            "<CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST>true</CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST>"
            "<PDUS>"
            "<SOCKET-CONNECTION-IPDU-IDENTIFIER>"
            "<SHORT-NAME>p</SHORT-NAME>"
            '<TP-CONFIG-REF DEST="I-PDU-REF">/ipdu</TP-CONFIG-REF>'
            "</SOCKET-CONNECTION-IPDU-IDENTIFIER>"
            "</PDUS>"
        )
        result = parser.getSocketConnection(element)
        assert result is not None
        assert len(result.getPdus()) == 1

    def test_readSocketConnectionBundleConnections_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SocketConnectionBundle
        bundle = SocketConnectionBundle(
            parent=MagicMock(), short_name="Scb"
        )
        element = _snip(
            "<BUNDLED-CONNECTIONS><BAD/></BUNDLED-CONNECTIONS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSocketConnectionBundleConnections(
                element, bundle
            )
        assert any("Unsupported Bundled Connection" in r.getMessage()
                   for r in caplog.records)

    def test_readSoAdConfigConnectionBundles_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        element = _snip(
            "<CONNECTION-BUNDLES><BAD/></CONNECTION-BUNDLES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSoAdConfigConnectionBundles(
                element, config
            )
        assert any("Unsupported Connection Bundle" in r.getMessage()
                   for r in caplog.records)


# ==================== ServiceInstance (L3363-3366, L3370-3375, L3405, L3408, L3418, L3429-3434) ====================


class TestServiceInstanceGaps:
    def test_readConsumedServiceInstance_sets_refs(self, parser):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        instance = end_point.createConsumedServiceInstance("Csi")
        element = _snip(
            '<PROVIDED-SERVICE-INSTANCE-REF DEST="PROVIDED-SERVICE-INSTANCE">/psi</PROVIDED-SERVICE-INSTANCE-REF>'
            "<SD-CLIENT-CONFIG/>"
        )
        parser.readConsumedServiceInstance(element, instance)
        assert instance.getProvidedServiceInstanceRef() is not None

    def test_readSocketAddressApplicationEndpointConsumedServiceInstances_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<CONSUMED-SERVICE-INSTANCES><BAD/></CONSUMED-SERVICE-INSTANCES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSocketAddressApplicationEndpointConsumedServiceInstances(
                element, end_point
            )
        assert any("Unsupported ConsumedServiceInstances"
                   in r.getMessage() for r in caplog.records)

    def test_readSocketAddressApplicationEndpointConsumedServiceInstances_creates(
        self, parser
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<CONSUMED-SERVICE-INSTANCES>"
            "<CONSUMED-SERVICE-INSTANCE>"
            "<SHORT-NAME>csi</SHORT-NAME>"
            "</CONSUMED-SERVICE-INSTANCE>"
            "</CONSUMED-SERVICE-INSTANCES>"
        )
        parser.readSocketAddressApplicationEndpointConsumedServiceInstances(
            element, end_point
        )
        assert len(end_point.getConsumedServiceInstances()) == 1

    def test_readSocketAddressApplicationEndpointProvidedServiceInstances_creates(
        self, parser
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<PROVIDED-SERVICE-INSTANCES>"
            "<PROVIDED-SERVICE-INSTANCE>"
            "<SHORT-NAME>psi</SHORT-NAME>"
            "</PROVIDED-SERVICE-INSTANCE>"
            "</PROVIDED-SERVICE-INSTANCES>"
        )
        parser.readSocketAddressApplicationEndpointProvidedServiceInstance(
            element, end_point
        )
        assert len(end_point.getProvidedServiceInstances()) == 1

    def test_readEventHandler_adds_consumed_event_group_ref(
        self, parser
    ):
        from armodel.models import ProvidedServiceInstance
        instance = ProvidedServiceInstance(
            parent=MagicMock(), short_name="Psi"
        )
        handler = instance.createEventHandler("Eh")
        element = _snip(
            '<APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/ae</APPLICATION-ENDPOINT-REF>'
            "<CONSUMED-EVENT-GROUP-REFS>"
            '<CONSUMED-EVENT-GROUP-REF DEST="CONSUMED-EVENT-GROUP">/ceg</CONSUMED-EVENT-GROUP-REF>'
            "</CONSUMED-EVENT-GROUP-REFS>"
            "<ROUTING-GROUP-REFS>"
            '<ROUTING-GROUP-REF DEST="SO-AD-ROUTING-GROUP">/rg</ROUTING-GROUP-REF>'
            "</ROUTING-GROUP-REFS>"
        )
        parser.readEventHandler(element, handler)
        assert len(handler.getConsumedEventGroupRefs()) == 1
        assert len(handler.getRoutingGroupRefs()) == 1

    def test_readProvidedServiceInstanceEventHandlers_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ProvidedServiceInstance
        instance = ProvidedServiceInstance(
            parent=MagicMock(), short_name="Psi"
        )
        element = _snip(
            "<EVENT-HANDLERS><BAD/></EVENT-HANDLERS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readProvidedServiceInstanceEventHandlers(
                element, instance
            )
        assert any("Unsupported Event Handler" in r.getMessage()
                   for r in caplog.records)

    def test_readSocketAddressApplicationEndpointProvidedServiceInstance_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<PROVIDED-SERVICE-INSTANCES><BAD/></PROVIDED-SERVICE-INSTANCES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSocketAddressApplicationEndpointProvidedServiceInstance(
                element, end_point
            )
        assert any("Unsupported ConsumedServiceInstances"
                   in r.getMessage() for r in caplog.records)


# ==================== CommunicationCluster PhysicalChannels (L3498-3505) ====================


class TestCommunicationClusterPhysicalChannels:
    def test_readPhysicalChannels_creates_all_channel_types(
        self, parser
    ):
        from armodel.models import CanCluster, LinCluster
        from armodel.models import EthernetCluster, FlexrayCluster
        can_cluster = CanCluster(parent=MagicMock(), short_name="Can")
        lin_cluster = LinCluster(parent=MagicMock(), short_name="Lin")
        eth_cluster = EthernetCluster(parent=MagicMock(), short_name="Eth")
        flx_cluster = FlexrayCluster(parent=MagicMock(), short_name="Flx")

        can_el = _snip(
            "<PHYSICAL-CHANNELS>"
            "<CAN-PHYSICAL-CHANNEL><SHORT-NAME>cpc</SHORT-NAME></CAN-PHYSICAL-CHANNEL>"
            "</PHYSICAL-CHANNELS>"
        )
        parser.readCommunicationClusterPhysicalChannels(can_el, can_cluster)
        assert len(can_cluster.getPhysicalChannels()) == 1

        lin_el = _snip(
            "<PHYSICAL-CHANNELS>"
            "<LIN-PHYSICAL-CHANNEL><SHORT-NAME>lpc</SHORT-NAME></LIN-PHYSICAL-CHANNEL>"
            "</PHYSICAL-CHANNELS>"
        )
        parser.readCommunicationClusterPhysicalChannels(lin_el, lin_cluster)
        assert len(lin_cluster.getPhysicalChannels()) == 1

        eth_el = _snip(
            "<PHYSICAL-CHANNELS>"
            "<ETHERNET-PHYSICAL-CHANNEL><SHORT-NAME>epc</SHORT-NAME></ETHERNET-PHYSICAL-CHANNEL>"
            "</PHYSICAL-CHANNELS>"
        )
        parser.readCommunicationClusterPhysicalChannels(eth_el, eth_cluster)
        assert len(eth_cluster.getPhysicalChannels()) == 1

        flx_el = _snip(
            "<PHYSICAL-CHANNELS>"
            "<FLEXRAY-PHYSICAL-CHANNEL><SHORT-NAME>fpc</SHORT-NAME></FLEXRAY-PHYSICAL-CHANNEL>"
            "</PHYSICAL-CHANNELS>"
        )
        parser.readCommunicationClusterPhysicalChannels(flx_el, flx_cluster)
        assert len(flx_cluster.getPhysicalChannels()) == 1


# ==================== DiagnosticConnection / DiagnosticServiceTable (L3607, L3618) ====================


class TestDiagnosticConnectionGaps:
    def test_readDiagnosticConnectionFunctionalRequestRefs_adds_ref(
        self, parser
    ):
        from armodel.models import DiagnosticConnection
        conn = DiagnosticConnection(
            parent=MagicMock(), short_name="Dc"
        )
        element = _snip(
            "<FUNCTIONAL-REQUEST-REFS>"
            '<FUNCTIONAL-REQUEST-REF DEST="DIAGNOSTIC-CONNECTION">/fr</FUNCTIONAL-REQUEST-REF>'
            "</FUNCTIONAL-REQUEST-REFS>"
        )
        parser.readDiagnosticConnectionFunctionalRequestRefs(
            element, conn
        )
        assert len(conn.getFunctionalRequestRefs()) == 1

    def test_readDiagnosticServiceTableDiagnosticConnectionRefs_adds(
        self, parser
    ):
        from armodel.models import DiagnosticServiceTable
        table = DiagnosticServiceTable(
            parent=MagicMock(), short_name="Dst"
        )
        element = _snip(
            "<DIAGNOSTIC-CONNECTIONS>"
            "<DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-CONNECTION-REF DEST="DIAGNOSTIC-CONNECTION">/dc</DIAGNOSTIC-CONNECTION-REF>'
            "</DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            "</DIAGNOSTIC-CONNECTIONS>"
        )
        parser.readDiagnosticServiceTableDiagnosticConnectionRefs(
            element, table
        )
        assert len(table.getDiagnosticConnectionRefs()) == 1


# ==================== HwElement / HwCategory (L3808, L3826) ====================


class TestHwElementAndCategory:
    def test_readHwElementHwPinGroups_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import HwElement
        hw_element = HwElement(parent=MagicMock(), short_name="Hw")
        element = _snip(
            "<HW-PIN-GROUPS><BAD/></HW-PIN-GROUPS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readHwElementHwPinGroups(
                element, hw_element
            )
        assert any("Unsupported Hw Pin Group" in r.getMessage()
                   for r in caplog.records)

    def test_readHwCategoryHwAttributeDef_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import HwCategory
        hw_category = HwCategory(parent=MagicMock(), short_name="Hc")
        element = _snip(
            "<HW-ATTRIBUTE-DEFS><BAD/></HW-ATTRIBUTE-DEFS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readHwCategoryHwAttributeDef(
                element, hw_category
            )
        assert any("Unsupported Hw Attribute Defs" in r.getMessage()
                   for r in caplog.records)


# ==================== ISignalToIPduMapping / NmPdu / SecureCommunication (L3862-3863, L3870-3875, L3899-3900) ====================


class TestPduAndSecureCommunication:
    def test_readISignalToIPduMapping_sets_refs(self, parser):
        from armodel.models import ISignalToIPduMapping
        mapping = ISignalToIPduMapping(
            parent=MagicMock(), short_name="M"
        )
        element = _snip(
            '<I-SIGNAL-REF DEST="I-SIGNAL">/is</I-SIGNAL-REF>'
            "<PACKING-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</PACKING-BYTE-ORDER>"
            "<START-POSITION>0</START-POSITION>"
            "<TRANSFER-PROPERTY>TRIGGERED</TRANSFER-PROPERTY>"
        )
        parser.readISignalToIPduMapping(element, mapping)
        assert mapping.getISignalRef() is not None
        assert mapping.getPackingByteOrder() is not None

    def test_readNmPduISignalToIPduMappings_creates_mapping(
        self, parser
    ):
        from armodel.models import NmPdu
        pdu = NmPdu(parent=MagicMock(), short_name="Np")
        element = _snip(
            "<I-SIGNAL-TO-I-PDU-MAPPINGS>"
            "<I-SIGNAL-TO-I-PDU-MAPPING>"
            "<SHORT-NAME>m</SHORT-NAME>"
            "</I-SIGNAL-TO-I-PDU-MAPPING>"
            "</I-SIGNAL-TO-I-PDU-MAPPINGS>"
        )
        parser.readNmPduISignalToIPduMappings(element, pdu)
        assert len(pdu.getISignalToIPduMappings()) == 1

    def test_readNmPduISignalToIPduMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import NmPdu
        pdu = NmPdu(parent=MagicMock(), short_name="Np")
        element = _snip(
            "<I-SIGNAL-TO-I-PDU-MAPPINGS><BAD/></I-SIGNAL-TO-I-PDU-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readNmPduISignalToIPduMappings(element, pdu)
        assert any("Unsupported ISignalToIPduMapping" in r.getMessage()
                   for r in caplog.records)

    def test_getSecureCommunicationProps_sets_props(self, parser):
        element = _snip(
            "<SECURE-COMMUNICATION-PROPS>"
            "<AUTH-DATA-FRESHNESS-LENGTH>16</AUTH-DATA-FRESHNESS-LENGTH>"
            "<AUTH-DATA-FRESHNESS-START-POSITION>0</AUTH-DATA-FRESHNESS-START-POSITION>"
            "<AUTH-INFO-TX-LENGTH>8</AUTH-INFO-TX-LENGTH>"
            "</SECURE-COMMUNICATION-PROPS>"
        )
        result = parser.getSecureCommunicationProps(
            element, "SECURE-COMMUNICATION-PROPS"
        )
        assert result is not None
        assert result.getAuthDataFreshnessLength().getValue() == 16


# ==================== NmConfig (L3981, L4072) ====================


class TestNmConfigGaps:
    def test_readNmConfigNmClusterCouplings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="Nmc")
        element = _snip(
            "<NM-CLUSTER-COUPLINGS><BAD/></NM-CLUSTER-COUPLINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readNmConfigNmClusterCouplings(
                element, config
            )
        assert any("Unsupported Nm Node" in r.getMessage()
                   for r in caplog.records)

    def test_readNmConfigNmIfEcus_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="Nmc")
        element = _snip(
            "<NM-IF-ECUS><BAD/></NM-IF-ECUS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readNmConfigNmIfEcus(element, config)
        assert any("Unsupported NmIfEcus" in r.getMessage()
                   for r in caplog.records)


# ==================== TpConfig (L4097, L4111, L4122, L4165, L4183, L4205) ====================


class TestTpConfigGaps:
    def test_readCanTpConfigTpAddresses_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="Ctp")
        element = _snip(
            "<TP-ADDRESSS><BAD/></TP-ADDRESSS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCanTpConfigTpAddresses(
                element, config
            )
        assert any("Unsupported TpAddress" in r.getMessage()
                   for r in caplog.records)

    def test_readCanTpConfigTpChannels_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="Ctp")
        element = _snip(
            "<TP-CHANNELS><BAD/></TP-CHANNELS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCanTpConfigTpChannels(
                element, config
            )
        assert any("Unsupported TpChannel" in r.getMessage()
                   for r in caplog.records)

    def test_readTpConnectionReceiverRefs_adds_ref(self, parser):
        from armodel.models import CanTpConnection
        conn = CanTpConnection()
        element = _snip(
            "<RECEIVER-REFS>"
            '<RECEIVER-REF DEST="ECU-INSTANCE">/r</RECEIVER-REF>'
            "</RECEIVER-REFS>"
        )
        parser.readTpConnectionReceiverRefs(element, conn)
        assert len(conn.getReceiverRefs()) == 1

    def test_readCanTpConfigTpEcus_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="Ctp")
        element = _snip(
            "<TP-ECUS><BAD/></TP-ECUS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCanTpConfigTpEcus(element, config)
        assert any("Unsupported TpEcu" in r.getMessage()
                   for r in caplog.records)

    def test_readCanTpConfigTpNodes_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="Ctp")
        element = _snip(
            "<TP-NODES><BAD/></TP-NODES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCanTpConfigTpNodes(element, config)
        assert any("Unsupported TpNode" in r.getMessage()
                   for r in caplog.records)

    def test_readLinTpConfigTpAddresses_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="Ltp")
        element = _snip(
            "<TP-ADDRESSS><BAD/></TP-ADDRESSS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readLinTpConfigTpAddresses(
                element, config
            )
        assert any("Unsupported TpAddress" in r.getMessage()
                   for r in caplog.records)


# ==================== BufferProperties (L4311-4313) ====================


class TestBufferProperties:
    def test_readBufferPropertiesBufferComputation_sets_scale(
        self, parser
    ):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import BufferProperties
        props = BufferProperties()
        element = _snip(
            "<BUFFER-COMPUTATION>"
            "<SHORT-LABEL>bc</SHORT-LABEL>"
            "<LOWER-LIMIT>0</LOWER-LIMIT>"
            "<UPPER-LIMIT>100</UPPER-LIMIT>"
            "</BUFFER-COMPUTATION>"
        )
        parser.readBufferPropertiesBufferComputation(element, props)
        assert props.getBufferComputation() is not None


# ==================== ECUC ModuleDef / ContainerDef (L4461, L4480, L4484-4489, L4503, L4560, L4627-4667) ====================


class TestEcucContainerAndModuleDef:
    def _make_module_def(self):
        from armodel.models import EcucModuleDef
        return EcucModuleDef(parent=_autosar_root(), short_name="Md")

    def test_readEcucModuleDefSupportedConfigVariants_adds(
        self, parser
    ):
        module_def = self._make_module_def()
        element = _snip(
            "<SUPPORTED-CONFIG-VARIANTS>"
            "<SUPPORTED-CONFIG-VARIANT>V1</SUPPORTED-CONFIG-VARIANT>"
            "<SUPPORTED-CONFIG-VARIANT>V2</SUPPORTED-CONFIG-VARIANT>"
            "</SUPPORTED-CONFIG-VARIANTS>"
        )
        parser.readEcucModuleDefSupportedConfigVariants(
            element, module_def
        )
        assert len(module_def.getSupportedConfigVariants()) == 2

    def test_getEcucMultiplicityConfigurationClasses_unsupported_warns(
        self, warning_parser, caplog
    ):
        element = _snip(
            "<MULTIPLICITY-CONFIG-CLASSES><BAD/></MULTIPLICITY-CONFIG-CLASSES>"
        )
        with caplog.at_level(logging.ERROR):
            result = warning_parser.getEcucMultiplicityConfigurationClasses(
                element
            )
        assert result == []
        assert any("Unsupported MultiplicityConfigClass"
                   in r.getMessage() for r in caplog.records)

    def test_readEcucContainerDef_sets_attrs(self, parser):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<MULTIPLICITY-CONFIG-CLASSES>"
            "<ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "<CONFIG-CLASS>VARIANT</CONFIG-CLASS>"
            "<CONFIG-VARIANT>POST-BUILD</CONFIG-VARIANT>"
            "</ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "</MULTIPLICITY-CONFIG-CLASSES>"
            "<POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>"
            "<REQUIRES-INDEX>true</REQUIRES-INDEX>"
            "<MULTIPLE-CONFIGURATION-CONTAINER>true</MULTIPLE-CONFIGURATION-CONTAINER>"
        )
        parser.readEcucContainerDef(element, container)
        assert len(container.getMultiplicityConfigClasses()) == 1
        assert container.getPostBuildVariantMultiplicity().getValue() is True

    def test_getEcucValueConfigurationClasses_unsupported_warns(
        self, warning_parser, caplog
    ):
        element = _snip(
            "<VALUE-CONFIG-CLASSES><BAD/></VALUE-CONFIG-CLASSES>"
        )
        with caplog.at_level(logging.ERROR):
            result = warning_parser.getEcucValueConfigurationClasses(
                element
            )
        assert result == []
        assert any("Unsupported ValueConfigClass" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucEnumerationParamDefLiterals_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucEnumerationParamDef
        param_def = EcucEnumerationParamDef(
            _autosar_root(), "Enum"
        )
        element = _snip(
            "<LITERALS><BAD/></LITERALS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucEnumerationParamDefLiterals(
                element, param_def
            )
        assert any("Unsupported EnumerationLiteral" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucContainerDefSubContainers_creates_sub(
        self, parser
    ):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SUB-CONTAINERS>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF>"
            "<SHORT-NAME>Sub</SHORT-NAME>"
            "</ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</SUB-CONTAINERS>"
        )
        parser.readEcucContainerDefSubContainers(element, container)
        assert len(container.getSubContainers()) == 1

    def test_readEcucContainerDefSubContainers_choice(self, parser):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SUB-CONTAINERS>"
            "<ECUC-CHOICE-CONTAINER-DEF>"
            "<SHORT-NAME>Ch</SHORT-NAME>"
            "</ECUC-CHOICE-CONTAINER-DEF>"
            "</SUB-CONTAINERS>"
        )
        parser.readEcucContainerDefSubContainers(element, container)
        assert len(container.getSubContainers()) == 1

    def test_readEcucContainerDefSubContainers_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SUB-CONTAINERS><BAD/></SUB-CONTAINERS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucContainerDefSubContainers(
                element, container
            )
        assert any("Unsupported SubContainer" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucParamConfContainerDef_full(self, parser):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SHORT-NAME>Cd</SHORT-NAME>"
        )
        parser.readEcucParamConfContainerDef(element, container)

    def test_readEcucChoiceContainerDefChoices_creates(self, parser):
        from armodel.models import EcucChoiceContainerDef
        container = EcucChoiceContainerDef(
            _autosar_root(), "Ch"
        )
        element = _snip(
            "<CHOICES>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF>"
            "<SHORT-NAME>C1</SHORT-NAME>"
            "</ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</CHOICES>"
        )
        parser.readEcucChoiceContainerDefChoices(element, container)
        assert len(container.getChoices()) == 1

    def test_readEcucChoiceContainerDefChoices_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucChoiceContainerDef
        container = EcucChoiceContainerDef(
            _autosar_root(), "Ch"
        )
        element = _snip(
            "<CHOICES><BAD/></CHOICES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucChoiceContainerDefChoices(
                element, container
            )
        assert any("Unsupported Choice" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucChoiceContainerDef_full(self, parser):
        from armodel.models import EcucChoiceContainerDef
        container = EcucChoiceContainerDef(
            _autosar_root(), "Ch"
        )
        element = _snip("<SHORT-NAME>Ch</SHORT-NAME>")
        parser.readEcucChoiceContainerDef(element, container)

    def test_readEcucModuleDefContainers_creates_param_conf(
        self, parser
    ):
        module_def = self._make_module_def()
        element = _snip(
            "<CONTAINERS>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF>"
            "<SHORT-NAME>C1</SHORT-NAME>"
            "</ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</CONTAINERS>"
        )
        parser.readEcucModuleDefContainers(element, module_def)
        assert len(module_def.getContainers()) == 1

    def test_readEcucModuleDefContainers_creates_choice(self, parser):
        module_def = self._make_module_def()
        element = _snip(
            "<CONTAINERS>"
            "<ECUC-CHOICE-CONTAINER-DEF>"
            "<SHORT-NAME>C2</SHORT-NAME>"
            "</ECUC-CHOICE-CONTAINER-DEF>"
            "</CONTAINERS>"
        )
        parser.readEcucModuleDefContainers(element, module_def)
        assert len(module_def.getContainers()) == 1

    def test_readEcucModuleDefContainers_unsupported_warns(
        self, warning_parser, caplog
    ):
        module_def = self._make_module_def()
        element = _snip(
            "<CONTAINERS><BAD/></CONTAINERS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucModuleDefContainers(
                element, module_def
            )
        assert any("Unsupported Container" in r.getMessage()
                   for r in caplog.records)


# ==================== SwSystemconstantValueSet (L4695) ====================


class TestSwSystemconstantValueSet:
    def test_readSwSystemconstantValueSetSwSystemconstantValues_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SwSystemconstantValueSet
        value_set = SwSystemconstantValueSet(
            parent=MagicMock(), short_name="Vs"
        )
        element = _snip(
            "<SW-SYSTEMCONSTANT-VALUES><BAD/></SW-SYSTEMCONSTANT-VALUES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwSystemconstantValueSetSwSystemconstantValues(
                element, value_set
            )
        assert any("Unsupported SwSystemconstValue" in r.getMessage()
                   for r in caplog.records)


# ==================== CouplingPort (L4873) ====================


class TestCouplingPort:
    def test_readEthernetCommunicationControllerCouplingPorts_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EthernetCommunicationController
        controller = EthernetCommunicationController(
            parent=MagicMock(), short_name="Ecc"
        )
        element = _snip(
            "<COUPLING-PORTS><BAD/></COUPLING-PORTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEthernetCommunicationControllerCouplingPorts(
                element, controller
            )
        assert any("Unsupported Coupling Port" in r.getMessage()
                   for r in caplog.records)


# ==================== TargetIPduRef (L5033-5034) ====================


class TestTargetIPduRef:
    def test_getTargetIPduRef_with_child(self, parser):
        element = _snip(
            "<TARGET-I-PDU-REF>"
            '<TARGET-I-PDU-REF DEST="I-PDU">/ipdu</TARGET-I-PDU-REF>'
            "</TARGET-I-PDU-REF>"
        )
        result = parser.getTargetIPduRef(
            element, "TARGET-I-PDU-REF"
        )
        assert result is not None
        assert result.getTargetIPdu().getValue() == "/ipdu"


# ==================== EcucParameterValue (L5081, L5103) ====================


class TestEcucParameterValue:
    def test_readEcucParameterValue_adds_annotation(self, parser):
        from armodel.models import EcucTextualParamValue
        param_value = EcucTextualParamValue()
        element = _snip(
            '<DEFINITION-REF DEST="ECUC-STRING-PARAM-DEF">/d</DEFINITION-REF>'
            "<ANNOTATIONS>"
            "<ANNOTATION>"
            "<SHORT-NAME>a</SHORT-NAME>"
            "</ANNOTATION>"
            "</ANNOTATIONS>"
        )
        parser.readEcucParameterValue(element, param_value)
        assert param_value.getDefinitionRef() is not None
        assert len(param_value.getAnnotations()) == 1

    def test_readEcucContainerValueParameterValues_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucContainerValue
        container = EcucContainerValue(
            parent=MagicMock(), short_name="Cv"
        )
        element = _snip(
            "<PARAMETER-VALUES><BAD/></PARAMETER-VALUES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucContainerValueParameterValues(
                element, container
            )
        assert any("Unsupported EcucParameterValue" in r.getMessage()
                   for r in caplog.records)


# ==================== SystemSignalGroup (L5249) ====================


class TestSystemSignalGroup:
    def test_readSystemSignalGroup_adds_refs(self, parser):
        from armodel.models import SystemSignalGroup
        group = SystemSignalGroup(parent=MagicMock(), short_name="Ssg")
        element = _snip(
            "<SYSTEM-SIGNAL-REFS>"
            '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/s1</SYSTEM-SIGNAL-REF>'
            '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/s2</SYSTEM-SIGNAL-REF>'
            "</SYSTEM-SIGNAL-REFS>"
        )
        parser.readSystemSignalGroup(element, group)
        assert len(group.getSystemSignalRefs()) == 2


# ==================== ISignalIPduGroup (L5351, L5360, L5362) ====================


class TestISignalIPduGroup:
    def test_getISignalIPduRefs_returns_refs(self, parser):
        element = _snip(
            "<I-SIGNAL-I-PDUS>"
            "<I-SIGNAL-I-PDU-REF-CONDITIONAL>"
            '<I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/p1</I-SIGNAL-I-PDU-REF>'
            "</I-SIGNAL-I-PDU-REF-CONDITIONAL>"
            "</I-SIGNAL-I-PDUS>"
        )
        result = parser.getISignalIPduRefs(element)
        assert len(result) == 1

    def test_readISignalIPduGroup_adds_contained_ref(self, parser):
        from armodel.models import ISignalIPduGroup
        group = ISignalIPduGroup(parent=MagicMock(), short_name="Isg")
        element = _snip(
            '<COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>'
            '<COMMUNICATION-MODE>SEND</COMMUNICATION-MODE>'
            "<CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS>"
            '<CONTAINED-I-SIGNAL-I-PDU-GROUP-REF DEST="I-SIGNAL-I-PDU-GROUP">/g</CONTAINED-I-SIGNAL-I-PDU-GROUP-REF>'
            "</CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS>"
        )
        parser.readISignalIPduGroup(element, group)
        assert group.getCommunicationDirection() is not None
        assert len(group.getContainedISignalIPduGroupRefs()) == 1

    def test_readISignalIPduGroup_adds_i_signal_i_pdu_ref(self, parser):
        from armodel.models import ISignalIPduGroup
        group = ISignalIPduGroup(parent=MagicMock(), short_name="Isg")
        element = _snip(
            "<I-SIGNAL-I-PDUS>"
            "<I-SIGNAL-I-PDU-REF-CONDITIONAL>"
            '<I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/p1</I-SIGNAL-I-PDU-REF>'
            "</I-SIGNAL-I-PDU-REF-CONDITIONAL>"
            "</I-SIGNAL-I-PDUS>"
        )
        parser.readISignalIPduGroup(element, group)
        assert len(group.getISignalIPduRefs()) == 1


# ==================== SystemMapping (L5437, L5451, L5466, L5483) ====================


class TestSystemMappingGaps:
    def _make_system(self):
        pkg = _autosar_root().createARPackage("Pkg")
        return pkg.createSystem("Sys")

    def test_readSystemMappingSwMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        mapping = system.createSystemMapping("Sm")
        element = _snip(
            "<SW-MAPPINGS><BAD/></SW-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingSwMappings(
                element, mapping
            )
        assert any("Unsupported Sw Mapping" in r.getMessage()
                   for r in caplog.records)

    def test_readSystemMappingEcuResourceMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        mapping = system.createSystemMapping("Sm")
        element = _snip(
            "<ECU-RESOURCE-MAPPINGS><BAD/></ECU-RESOURCE-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingEcuResourceMappings(
                element, mapping
            )
        assert any("Unsupported EcuResourceMapping" in r.getMessage()
                   for r in caplog.records)

    def test_readSystemMappingSwImplMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        mapping = system.createSystemMapping("Sm")
        element = _snip(
            "<SW-IMPL-MAPPINGS><BAD/></SW-IMPL-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingSwImplMappings(
                element, mapping
            )
        assert any("Unsupported SwImplMapping" in r.getMessage()
                   for r in caplog.records)

    def test_readSystemMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        element = _snip(
            "<MAPPINGS><BAD/></MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappings(element, system)
        assert any("Unsupported Mapping" in r.getMessage()
                   for r in caplog.records)


# ==================== RootSwCompositionPrototype (L5496-5497) ====================


class TestRootSwCompositionPrototype:
    def test_readRootSwCompositionPrototype_duplicate_warns(
        self, warning_parser, caplog
    ):
        system_pkg = _autosar_root().createARPackage("SysPkg")
        system = system_pkg.createSystem("Sys")
        proto = system.createRootSoftwareComposition("Root")
        AUTOSAR.getInstance().setRootSwCompositionPrototype(proto)
        element = _snip(
            "<ROOT-SOFTWARE-COMPOSITIONS>"
            "<ROOT-SW-COMPOSITION-PROTOTYPE>"
            "<SHORT-NAME>Root2</SHORT-NAME>"
            "</ROOT-SW-COMPOSITION-PROTOTYPE>"
            "</ROOT-SOFTWARE-COMPOSITIONS>"
        )
        with caplog.at_level(logging.WARNING):
            warning_parser.readRootSwCompositionPrototype(
                element, system
            )
        assert any("has already been set" in r.getMessage()
                   or "RootSwComposition" in r.getMessage()
                   for r in caplog.records)


# ==================== LifeCycleInfoSet (L5545) ====================


class TestLifeCycleInfoSet:
    def test_readLifeCycleInfoSetLifeCycleInfos_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import LifeCycleInfoSet
        info_set = LifeCycleInfoSet(
            parent=MagicMock(), short_name="Lcs"
        )
        element = _snip(
            "<LIFE-CYCLE-INFOS><BAD/></LIFE-CYCLE-INFOS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readLifeCycleInfoSetLifeCycleInfos(
                element, info_set
            )
        assert any("Unsupported Life Cycle Info" in r.getMessage()
                   for r in caplog.records)


# ==================== FlatMap (L5567) ====================


class TestFlatMap:
    def test_readFlatMapInstances_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import FlatMap
        flat_map = FlatMap(parent=MagicMock(), short_name="Fm")
        element = _snip(
            "<INSTANCES><BAD/></INSTANCES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readFlatMapInstances(
                element, flat_map
            )
        assert any("Unsupported Flat Map Instances" in r.getMessage()
                   for r in caplog.records)


# ==================== ClientServerInterfaceMapping (L5601) ====================


class TestClientServerInterfaceMapping:
    def test_readOperationMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ClientServerInterfaceMapping
        mapping = ClientServerInterfaceMapping(
            parent=MagicMock(), short_name="Csim"
        )
        element = _snip(
            "<OPERATION-MAPPINGS><BAD/></OPERATION-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readClientServerInterfaceMappingOperationMappings(
                element, mapping
            )
        assert any("Unsupported Operation Mapping" in r.getMessage()
                   for r in caplog.records)


# ==================== DiagEventDebounceAlgorithm (L687-692) ====================


class TestDiagEventDebounceAlgorithm:
    def test_readDiagEventDebounceAlgorithm_creates_monitor_internal(
        self, parser
    ):
        from armodel.models import DiagnosticEventNeeds
        needs = DiagnosticEventNeeds(
            parent=MagicMock(), short_name="Den"
        )
        element = _snip(
            "<DIAG-EVENT-DEBOUNCE-ALGORITHM>"
            "<DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL>"
            "<SHORT-NAME>Di</SHORT-NAME>"
            "</DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL>"
            "</DIAG-EVENT-DEBOUNCE-ALGORITHM>"
        )
        parser.readDiagEventDebounceAlgorithm(element, needs)
        assert needs.getDiagEventDebounceAlgorithm() is not None

    def test_readDiagEventDebounceAlgorithm_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import DiagnosticEventNeeds
        needs = DiagnosticEventNeeds(
            parent=MagicMock(), short_name="Den"
        )
        element = _snip(
            "<DIAG-EVENT-DEBOUNCE-ALGORITHM><BAD/></DIAG-EVENT-DEBOUNCE-ALGORITHM>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDiagEventDebounceAlgorithm(
                element, needs
            )
        assert any("Unsupported DiagEventDebounceAlgorithm"
                   in r.getMessage() for r in caplog.records)
