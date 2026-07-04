"""Tests for the ARPackage element dispatch in ARXMLParser.

Targets `readARPackageElements` (arxml_parser.py:5635-5893) — the 65+ branch
if/elif chain that routes AUTOSAR top-level element tags to their handler
methods. Each test feeds a minimal-but-valid XML snippet through the dispatch
and asserts the resulting object is created on the parent ARPackage via the
corresponding getter.

Goal: exercise every branch of the dispatch chain, which naturally cascades
coverage into each handler method (~30–100 lines per handler).
"""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Parser configured in warning mode so missing optional nested elements
    don't raise — keeps dispatch tests focused on routing, not full parsing."""
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


@pytest.fixture
def strict_parser():
    """Default parser (raises on errors)."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _make_parent() -> ARPackage:
    """Create a fresh ARPackage parent on the AUTOSAR singleton."""
    autosar = AUTOSAR.getInstance()
    parent = ARPackage(parent=autosar, short_name="TestPkg")
    return parent


def _dispatch(parser, parent: ARPackage, inner_xml: str) -> None:
    """Feed <AR-PACKAGE><ELEMENTS>...</ELEMENTS></AR-PACKAGE> to readARPackageElements.

    The parser's dispatch does `findall(element, "ELEMENTS/*")`, so the passed
    element must be the AR-PACKAGE wrapper, not the ELEMENTS element itself.
    """
    xml = f"<AR-PACKAGE xmlns='{NS}'><SHORT-NAME>TestPkg</SHORT-NAME><ELEMENTS>{inner_xml}</ELEMENTS></AR-PACKAGE>"
    pkg_element = ET.fromstring(xml)
    parser.readARPackageElements(pkg_element, parent)


def _snip(tag: str, short_name: str = "X", body: str = "") -> str:
    return f"<{tag}><SHORT-NAME>{short_name}</SHORT-NAME>{body}</{tag}>"


# ==================== Software components ====================


class TestSwComponentDispatch:
    def test_composition_sw_component_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("COMPOSITION-SW-COMPONENT-TYPE", "C1"))
        assert len(parent.getCompositionSwComponentTypes()) == 1

    def test_complex_device_driver_sw_component_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE", "C1"))
        assert len(parent.getComplexDeviceDriverSwComponentTypes()) == 1

    def test_application_sw_component_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("APPLICATION-SW-COMPONENT-TYPE", "A1"))
        # getAtomicSwComponentTypes includes ApplicationSwComponentType
        assert len(parent.getAtomicSwComponentTypes()) == 1

    def test_ecu_abstraction_sw_component_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("ECU-ABSTRACTION-SW-COMPONENT-TYPE", "E1"))
        assert len(parent.getSwComponentTypes()) == 1

    def test_service_sw_component_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SERVICE-SW-COMPONENT-TYPE", "S1"))
        assert len(parent.getSwComponentTypes()) == 1

    def test_sensor_actuator_sw_component_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SENSOR-ACTUATOR-SW-COMPONENT-TYPE", "SA1"))
        assert len(parent.getSensorActuatorSwComponentType()) == 1

    def test_swc_implementation(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SWC-IMPLEMENTATION", "I1"))
        assert len(parent.getSwcImplementations()) == 1

    def test_bsw_implementation(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("BSW-IMPLEMENTATION", "BI1"))
        assert len(parent.getBswImplementations()) == 1

    def test_swc_bsw_mapping(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SWC-BSW-MAPPING", "M1"))
        assert len(parent.getSwcBswMappings()) == 1


# ==================== Datatypes ====================


class TestDataTypeDispatch:
    def test_application_primitive_data_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("APPLICATION-PRIMITIVE-DATA-TYPE", "AP1"))
        assert len(parent.getApplicationPrimitiveDataTypes()) == 1

    def test_application_record_data_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("APPLICATION-RECORD-DATA-TYPE", "AR1"))
        # ApplicationRecordDataType reuses ApplicationPrimitiveDataType list
        assert len(parent.getApplicationDataType()) >= 1

    def test_application_array_data_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("APPLICATION-ARRAY-DATA-TYPE", "AA1"))
        assert len(parent.getApplicationArrayDataTypes()) == 1

    def test_implementation_data_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("IMPLEMENTATION-DATA-TYPE", "IDT1"))
        assert len(parent.getImplementationDataTypes()) == 1

    def test_sw_base_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SW-BASE-TYPE", "BT1"))
        assert len(parent.getSwBaseTypes()) == 1

    def test_compu_method(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("COMPU-METHOD", "CM1"))
        assert len(parent.getCompuMethods()) == 1

    def test_data_constr(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("DATA-CONSTR", "DC1"))
        assert len(parent.getDataConstrs()) == 1

    def test_unit(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("UNIT", "U1"))
        assert len(parent.getUnits()) == 1

    def test_constant_specification(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("CONSTANT-SPECIFICATION", "CS1"))
        assert len(parent.getConstantSpecifications()) == 1

    def test_sw_record_layout(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SW-RECORD-LAYOUT", "RL1"))
        assert len(parent.getSwRecordLayouts()) == 1

    def test_sw_addr_method(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SW-ADDR-METHOD", "AM1"))
        assert len(parent.getSwAddrMethods()) == 1

    def test_data_type_mapping_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("DATA-TYPE-MAPPING-SET", "DTS1"))
        assert len(parent.getDataTypeMappingSets()) == 1


# ==================== Port interfaces ====================


class TestPortInterfaceDispatch:
    def test_sender_receiver_interface(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SENDER-RECEIVER-INTERFACE", "SR1"))
        assert len(parent.getSenderReceiverInterfaces()) == 1

    def test_client_server_interface(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("CLIENT-SERVER-INTERFACE", "CS1"))
        assert len(parent.getClientServerInterfaces()) == 1

    def test_parameter_interface(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("PARAMETER-INTERFACE", "PI1"))
        assert len(parent.getParameterInterfaces()) == 1

    def test_nv_data_interface(self, parser):
        # No dedicated getter on ARPackage; assert via getElement.
        parent = _make_parent()
        _dispatch(parser, parent, _snip("NV-DATA-INTERFACE", "NV1"))
        # Verify it was added to package (no exception means dispatch succeeded).
        assert parent.getElement("NV1") is not None

    def test_mode_switch_interface(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("MODE-SWITCH-INTERFACE", "MS1"))
        assert len(parent.getModeSwitchInterfaces()) == 1

    def test_trigger_interface(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("TRIGGER-INTERFACE", "TI1"))
        assert len(parent.getTriggerInterfaces()) == 1


# ==================== BSW ====================


class TestBswDispatch:
    def test_bsw_module_description(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("BSW-MODULE-DESCRIPTION", "BMD1"))
        assert len(parent.getBswModuleDescriptions()) == 1

    def test_bsw_module_entry(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("BSW-MODULE-ENTRY", "BME1"))
        assert len(parent.getBswModuleEntries()) == 1


# ==================== Misc structure ====================


class TestMiscDispatch:
    def test_mode_declaration_group(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("MODE-DECLARATION-GROUP", "MDG1"))
        assert len(parent.getModeDeclarationGroups()) == 1

    def test_swc_timing(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SWC-TIMING", "ST1"))
        assert len(parent.getSwcTimings()) == 1

    def test_end_to_end_protection_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("END-TO-END-PROTECTION-SET", "E2E1"))
        # No dedicated ARPackage getter for E2E; verify dispatch succeeded.
        assert parent.getElement("E2E1") is not None

    def test_physical_dimension(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("PHYSICAL-DIMENSION", "PD1"))
        assert len(parent.getEcucPhysicalDimensions()) == 1


# ==================== Network / bus ====================


class TestNetworkDispatch:
    def test_lin_cluster(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("LIN-CLUSTER", "LC1"))
        assert len(parent.getLinClusters()) == 1

    def test_can_cluster(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("CAN-CLUSTER", "CC1"))
        assert len(parent.getCanClusters()) == 1

    def test_flexray_cluster(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("FLEXRAY-CLUSTER", "FC1"))
        # No dedicated getter for FlexrayCluster on ARPackage; verify dispatch.
        assert parent.getElement("FC1") is not None

    def test_ethernet_cluster(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("ETHERNET-CLUSTER", "EC1"))
        assert parent.getElement("EC1") is not None

    def test_lin_unconditional_frame(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("LIN-UNCONDITIONAL-FRAME", "LF1"))
        assert len(parent.getLinUnconditionalFrames()) == 1

    def test_can_frame(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("CAN-FRAME", "CF1"))
        assert len(parent.getCanFrames()) == 1

    def test_flexray_frame(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("FLEXRAY-FRAME", "FF1"))
        assert len(parent.getFlexrayFrames()) == 1

    def test_ethernet_frame(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("ETHERNET-FRAME", "EF1"))
        assert parent.getElement("EF1") is not None

    def test_nm_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("NM-PDU", "NMP1"))
        assert len(parent.getNmPdus()) == 1

    def test_n_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("N-PDU", "NP1"))
        assert len(parent.getNPdus()) == 1

    def test_dcm_i_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("DCM-I-PDU", "DIP1"))
        assert len(parent.getDcmIPdus()) == 1

    def test_secured_i_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SECURED-I-PDU", "SIP1"))
        assert len(parent.getSecuredIPdus()) == 1

    def test_i_signal(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("I-SIGNAL", "IS1"))
        assert len(parent.getISignals()) == 1

    def test_i_signal_group(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("I-SIGNAL-GROUP", "ISG1"))
        assert len(parent.getISignalGroups()) == 1

    def test_i_signal_i_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("I-SIGNAL-I-PDU", "IIP1"))
        assert len(parent.getISignalIPdus()) == 1

    def test_i_signal_i_pdu_group(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("I-SIGNAL-I-PDU-GROUP", "IIPG1"))
        assert parent.getElement("IIPG1") is not None

    def test_system_signal(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SYSTEM-SIGNAL", "SS1"))
        assert len(parent.getSystemSignals()) == 1

    def test_system_signal_group(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SYSTEM-SIGNAL-GROUP", "SSG1"))
        assert len(parent.getSystemSignalGroups()) == 1

    def test_multiplexed_i_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("MULTIPLEXED-I-PDU", "MIP1"))
        assert parent.getElement("MIP1") is not None

    def test_user_defined_i_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("USER-DEFINED-I-PDU", "UDI1"))
        assert parent.getElement("UDI1") is not None

    def test_user_defined_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("USER-DEFINED-PDU", "UDP1"))
        assert parent.getElement("UDP1") is not None

    def test_general_purpose_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("GENERAL-PURPOSE-PDU", "GPP1"))
        assert parent.getElement("GPP1") is not None

    def test_general_purpose_i_pdu(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("GENERAL-PURPOSE-I-PDU", "GPI1"))
        assert parent.getElement("GPI1") is not None


# ==================== Network management / TP / comm security ====================


class TestNmAndCommDispatch:
    def test_nm_config(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("NM-CONFIG", "NC1"))
        assert len(parent.getNmConfigs()) == 1

    def test_can_tp_config(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("CAN-TP-CONFIG", "CTP1"))
        assert len(parent.getCanTpConfigs()) == 1

    def test_lin_tp_config(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("LIN-TP-CONFIG", "LTP1"))
        assert parent.getElement("LTP1") is not None

    def test_do_ip_tp_config(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("DO-IP-TP-CONFIG", "DITP1"))
        assert parent.getElement("DITP1") is not None

    def test_secure_communication_props_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SECURE-COMMUNICATION-PROPS-SET", "SC1"))
        assert parent.getElement("SC1") is not None

    def test_so_ad_routing_group(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SO-AD-ROUTING-GROUP", "SAR1"))
        assert parent.getElement("SAR1") is not None

    def test_data_transformation_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("DATA-TRANSFORMATION-SET", "DT1"))
        assert len(parent.getDataTransformationSets()) == 1


# ==================== System ====================


class TestSystemDispatch:
    def test_system(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SYSTEM", "SYS1"))
        assert len(parent.getSystems()) == 1

    def test_ecu_instance(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("ECU-INSTANCE", "EI1"))
        assert len(parent.getEcuInstances()) == 1

    def test_gateway(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("GATEWAY", "GW1"))
        assert len(parent.getGateways()) == 1


# ==================== ECUC ====================


class TestEcucDispatch:
    def test_ecuc_value_collection(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("ECUC-VALUE-COLLECTION", "EVC1"))
        assert len(parent.getEcucValueCollections()) == 1

    def test_ecuc_module_configuration_values(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("ECUC-MODULE-CONFIGURATION-VALUES", "EMV1"))
        assert len(parent.getEcucModuleConfigurationValues()) == 1

    def test_ecuc_module_def(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("ECUC-MODULE-DEF", "EMD1"))
        assert len(parent.getEcucModuleDefs()) == 1


# ==================== Diagnostic ====================


class TestDiagnosticDispatch:
    def test_diagnostic_connection(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("DIAGNOSTIC-CONNECTION", "DC1"))
        assert parent.getElement("DC1") is not None

    def test_diagnostic_service_table(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("DIAGNOSTIC-SERVICE-TABLE", "DST1"))
        assert parent.getElement("DST1") is not None


# ==================== Variant / lifecycle ====================


class TestVariantAndLifecycleDispatch:
    def test_sw_systemconst(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SW-SYSTEMCONST", "SC1"))
        assert len(parent.getSwSystemConsts()) == 1

    def test_sw_systemconstant_value_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("SW-SYSTEMCONSTANT-VALUE-SET", "SVS1"))
        assert len(parent.getSwSystemconstantValueSets()) == 1

    def test_predefined_variant(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("PREDEFINED-VARIANT", "PV1"))
        assert len(parent.getPredefinedVariants()) == 1

    def test_life_cycle_info_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("LIFE-CYCLE-INFO-SET", "LC1"))
        assert parent.getElement("LC1") is not None

    def test_collection(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("COLLECTION", "CO1"))
        assert len(parent.getCollections()) == 1

    def test_keyword_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("KEYWORD-SET", "KS1"))
        assert len(parent.getKeywordSets()) == 1


# ==================== Mapping / blueprint ====================


class TestMappingDispatch:
    def test_flat_map(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("FLAT-MAP", "FM1"))
        assert parent.getElement("FM1") is not None

    def test_port_interface_mapping_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("PORT-INTERFACE-MAPPING-SET", "PIM1"))
        assert parent.getElement("PIM1") is not None

    def test_port_prototype_blueprint(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("PORT-PROTOTYPE-BLUEPRINT", "PPB1"))
        assert len(parent.getPortPrototypeBlueprints()) == 1

    def test_mode_declaration_mapping_set(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("MODE-DECLARATION-MAPPING-SET", "MDM1"))
        assert len(parent.getModeDeclarationMappingSets()) == 1


# ==================== HW ====================


class TestHwDispatch:
    def test_hw_element(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("HW-ELEMENT", "HE1"))
        assert len(parent.getHwElements()) == 1

    def test_hw_category(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("HW-CATEGORY", "HC1"))
        assert len(parent.getHwCategories()) == 1

    def test_hw_type(self, parser):
        parent = _make_parent()
        _dispatch(parser, parent, _snip("HW-TYPE", "HT1"))
        assert parent.getElement("HT1") is not None


# ==================== Else-branch (unsupported element) ====================


class TestUnsupportedElement:
    def test_unsupported_tag_raises_NotImplementedError_by_default(self, strict_parser):
        parent = _make_parent()
        with pytest.raises(NotImplementedError, match="Unsupported Element type"):
            _dispatch(strict_parser, parent, _snip("TOTALLY-UNKNOWN-TAG", "U1"))

    def test_unsupported_tag_logs_in_warning_mode(self, parser, caplog):
        import logging
        parent = _make_parent()
        with caplog.at_level(logging.ERROR):
            _dispatch(parser, parent, _snip("TOTALLY-UNKNOWN-TAG", "U1"))
        assert any("Unsupported Element type" in r.getMessage() for r in caplog.records)


# ==================== Top-level load() and readARPackages() edge cases ====================


class TestLoadAndReadARPackages:
    def test_load_invalid_root_tag_raises_ValueError(self, strict_parser, tmp_path):
        # File contains a non-AUTOSAR root element.
        bad = tmp_path / "bad.arxml"
        bad.write_text(f"<NOT-AUTOSAR xmlns='{NS}'></NOT-AUTOSAR>", encoding="utf-8")
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
        document = AUTOSARDoc()
        with pytest.raises(ValueError, match="Invalid ARXML file"):
            strict_parser.load(str(bad), document)

    def test_readARPackages_unknown_child_tag_raises(self, strict_parser):
        # Manually invoke readARPackages with an unexpected child.
        import xml.etree.ElementTree as ET
        xml = f"<ROOT xmlns='{NS}'><AR-PACKAGES><TOTALLY-UNKNOWN/></AR-PACKAGES></ROOT>"
        root = ET.fromstring(xml)
        parent = _make_parent()
        with pytest.raises(NotImplementedError, match="Unsupported ARPackage"):
            strict_parser.readARPackages(root, parent)

    def test_readARPackages_unknown_child_tag_warns(self, parser, caplog):
        import logging
        import xml.etree.ElementTree as ET
        xml = f"<ROOT xmlns='{NS}'><AR-PACKAGES><TOTALLY-UNKNOWN/></AR-PACKAGES></ROOT>"
        root = ET.fromstring(xml)
        parent = _make_parent()
        with caplog.at_level(logging.ERROR):
            strict_parser_warning = ARXMLParser(options={"warning": True})
            strict_parser_warning.readARPackages(root, parent)
        assert any("Unsupported ARPackage" in r.getMessage() for r in caplog.records)
