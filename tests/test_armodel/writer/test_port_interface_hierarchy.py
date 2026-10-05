"""Writer/parser round-trip tests for the PortInterface hierarchy
(CP_TPS_SoftwareComponentTemplate Tables 3.18, 3.20, 4.6, 4.7, 4.8, 4.10, 4.11).

XML element order per the XSD groups PORT-INTERFACE / CLIENT-SERVER-INTERFACE /
CLIENT-SERVER-OPERATION / ARGUMENT-DATA-PROTOTYPE / APPLICATION-ERROR
(AUTOSAR_00052.xsd): IS-SERVICE, SERVICE-KIND; OPERATIONS, POSSIBLE-ERRORS;
ARGUMENTS, DIAG-ARG-INTEGRITY, POSSIBLE-ERROR-REFS; DIRECTION,
SERVER-ARGUMENT-IMPL-POLICY; ERROR-CODE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceProviderEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ArgumentDirectionEnum,
    Boolean,
    Integer,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ApplicationError,
    ClientServerInterface,
    ServerArgumentImplPolicyEnum,
    SubElementMapping,
    TextTableMapping,
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


def _serialize(element: ET.Element, obj) -> ET.Element:
    ARXMLWriter().writeARPackageElements(element, obj.parent)
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _reparse(root: ET.Element):
    parser = ARXMLParser(options={"warning": True})
    pkg = AUTOSAR.getInstance().createARPackage("Reparsed")
    parser.readARPackageElements(root.find("{%s}AR-PACKAGE" % NS), pkg)
    return pkg


class TestPortInterfaceRoundTrip:
    def test_is_service_and_service_kind_field_values_and_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        interface = pkg.createTriggerInterface("TI")
        is_service = Boolean()
        is_service.setValue("true")
        interface.setIsService(is_service)
        interface.setServiceKind(ServiceProviderEnum().setValue(ServiceProviderEnum.COM_MANAGER))

        root = _serialize(ET.Element("AR-PACKAGE"), interface)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}TRIGGER-INTERFACE" % tuple([NS] * 3))
        assert [child.tag.split("}")[-1] for child in element] == ["SHORT-NAME", "IS-SERVICE", "SERVICE-KIND"]
        assert element.find("{%s}IS-SERVICE" % NS).text == "true"
        assert element.find("{%s}SERVICE-KIND" % NS).text == "comManager"

        parsed = _reparse(root)
        parsed_interface = parsed.getTriggerInterfaces()[0]
        assert parsed_interface.getIsService().getValue() is True
        assert parsed_interface.getServiceKind().getValue() == "comManager"

    def test_absent_elements_round_trip_to_none(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        interface = pkg.createTriggerInterface("TI")

        root = _serialize(ET.Element("AR-PACKAGE"), interface)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}TRIGGER-INTERFACE" % tuple([NS] * 3))
        assert element.find("{%s}IS-SERVICE" % NS) is None
        assert element.find("{%s}SERVICE-KIND" % NS) is None

        parsed = _reparse(root)
        parsed_interface = parsed.getTriggerInterfaces()[0]
        assert parsed_interface.getIsService() is None
        assert parsed_interface.getServiceKind() is None


class TestClientServerInterfaceRoundTrip:
    def _build_interface(self, pkg) -> ClientServerInterface:
        cs = pkg.createClientServerInterface("CSI")
        operation = cs.createOperation("Op")
        argument = operation.createArgumentDataPrototype("Arg")
        argument.setDirection(ArgumentDirectionEnum().setValue(ArgumentDirectionEnum.IN))
        argument.setServerArgumentImplPolicy(ServerArgumentImplPolicyEnum().setValue(ServerArgumentImplPolicyEnum.USE_VOID))
        operation.setDiagArgIntegrity(self._boolean("true"))
        operation.addPossibleErrorRef(self._ref("/Pkg/CSI/E1"))
        error = cs.createApplicationError("E1")
        code = Integer()
        code.setValue("42")
        error.setErrorCode(code)
        return cs

    @staticmethod
    def _boolean(value):
        boolean = Boolean()
        boolean.setValue(value)
        return boolean

    @staticmethod
    def _ref(value):
        ref = RefType()
        ref.setValue(value)
        return ref

    def test_operations_and_possible_errors_field_values_and_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        cs = self._build_interface(pkg)

        root = _serialize(ET.Element("AR-PACKAGE"), cs)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}CLIENT-SERVER-INTERFACE" % tuple([NS] * 3))
        assert [child.tag.split("}")[-1] for child in element] == [
            "SHORT-NAME",
            "OPERATIONS",
            "POSSIBLE-ERRORS",
        ]
        operation_element = element.find("{%s}OPERATIONS/{%s}CLIENT-SERVER-OPERATION" % (NS, NS))
        assert [child.tag.split("}")[-1] for child in operation_element] == [
            "SHORT-NAME",
            "ARGUMENTS",
            "DIAG-ARG-INTEGRITY",
            "POSSIBLE-ERROR-REFS",
        ]
        argument_element = operation_element.find("{%s}ARGUMENTS/{%s}ARGUMENT-DATA-PROTOTYPE" % (NS, NS))
        assert [child.tag.split("}")[-1] for child in argument_element] == [
            "SHORT-NAME",
            "DIRECTION",
            "SERVER-ARGUMENT-IMPL-POLICY",
        ]
        assert argument_element.find("{%s}DIRECTION" % NS).text == "in"
        assert argument_element.find("{%s}SERVER-ARGUMENT-IMPL-POLICY" % NS).text == "useVoid"
        assert operation_element.find("{%s}DIAG-ARG-INTEGRITY" % NS).text == "true"
        assert operation_element.find("{%s}POSSIBLE-ERROR-REFS/{%s}POSSIBLE-ERROR-REF" % (NS, NS)).text == "/Pkg/CSI/E1"
        error_element = element.find("{%s}POSSIBLE-ERRORS/{%s}APPLICATION-ERROR" % (NS, NS))
        assert error_element.find("{%s}ERROR-CODE" % NS).text == "42"

        parsed = _reparse(root)
        parsed_cs = parsed.getClientServerInterfaces()[0]
        parsed_operation = parsed_cs.getOperations()[0]
        assert parsed_operation.getShortName() == "Op"
        assert parsed_operation.getDiagArgIntegrity().getValue() is True
        assert parsed_operation.getPossibleErrorRefs()[0].getValue() == "/Pkg/CSI/E1"
        parsed_argument = parsed_operation.getArguments()[0]
        assert parsed_argument.getDirection().getValue() == "in"
        assert parsed_argument.getServerArgumentImplPolicy().getValue() == "useVoid"
        parsed_error = parsed_cs.getPossibleErrors()[0]
        assert isinstance(parsed_error, ApplicationError)
        assert parsed_error.getErrorCode().getValue() == 42

    def test_empty_wrappers_not_serialized(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        cs = pkg.createClientServerInterface("CSI")

        root = _serialize(ET.Element("AR-PACKAGE"), cs)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}CLIENT-SERVER-INTERFACE" % tuple([NS] * 3))
        assert [child.tag.split("}")[-1] for child in element] == ["SHORT-NAME"]

        parsed = _reparse(root)
        parsed_cs = parsed.getClientServerInterfaces()[0]
        assert parsed_cs.getOperations() == []
        assert parsed_cs.getPossibleErrors() == []


class TestModeSwitchInterfaceRoundTrip:
    def test_mode_group_field_values_and_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        interface = pkg.createModeSwitchInterface("MSI")
        mode_group = interface.createModeGroup("ModeGrp")
        access = SwCalibrationAccessEnum()
        access.setValue(SwCalibrationAccessEnum.READ_ONLY)
        mode_group.setSwCalibrationAccess(access)
        type_tref = RefType()
        type_tref.setDest("MODE-DECLARATION-GROUP")
        type_tref.setValue("/Pkg/ModeDclGrp")
        mode_group.setTypeTRef(type_tref)

        root = _serialize(ET.Element("AR-PACKAGE"), interface)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}MODE-SWITCH-INTERFACE" % tuple([NS] * 3))
        assert [child.tag.split("}")[-1] for child in element] == [
            "SHORT-NAME",
            "MODE-GROUP",
        ]
        mode_group_element = element.find("{%s}MODE-GROUP" % NS)
        assert mode_group_element.find("{%s}SHORT-NAME" % NS).text == "ModeGrp"
        assert mode_group_element.find("{%s}TYPE-TREF" % NS).text == "/Pkg/ModeDclGrp"
        assert mode_group_element.find("{%s}SW-CALIBRATION-ACCESS" % NS).text == "readOnly"

        parsed = _reparse(root)
        parsed_interface = parsed.getModeSwitchInterfaces()[0]
        parsed_mode_group = parsed_interface.getModeGroup()
        assert isinstance(parsed_mode_group, ModeDeclarationGroupPrototype)
        assert parsed_mode_group.getShortName() == "ModeGrp"
        assert parsed_mode_group.getTypeTRef().getValue() == "/Pkg/ModeDclGrp"
        assert parsed_mode_group.getSwCalibrationAccess().getValue() == "readOnly"

    def test_absent_mode_group_round_trips_to_none(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        interface = pkg.createModeSwitchInterface("MSI")

        root = _serialize(ET.Element("AR-PACKAGE"), interface)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}MODE-SWITCH-INTERFACE" % tuple([NS] * 3))
        assert element.find("{%s}MODE-GROUP" % NS) is None

        parsed = _reparse(root)
        parsed_interface = parsed.getModeSwitchInterfaces()[0]
        assert parsed_interface.getModeGroup() is None


class TestDataPrototypeMappingRoundTrip:
    def _ref(self, dest, value):
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_data_prototype_mapping_field_values_and_order(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
            DataPrototypeMapping,
            VariableAndParameterInterfaceMapping,
        )

        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        map_set = pkg.createPortInterfaceMappingSet("PIMS")
        mapping = map_set.createVariableAndParameterInterfaceMapping("VAPIM")
        assert isinstance(mapping, VariableAndParameterInterfaceMapping)

        data_mapping = DataPrototypeMapping()
        data_mapping.setFirstDataPrototypeRef(self._ref("VARIABLE-DATA-PROTOTYPE", "/Pkg/First"))
        data_mapping.setFirstToSecondDataTransformationRef(self._ref("DATA-TRANSFORMATION", "/Pkg/DT"))
        data_mapping.setSecondDataPrototypeRef(self._ref("VARIABLE-DATA-PROTOTYPE", "/Pkg/Second"))
        data_mapping.setSecondToFirstDataTransformationRef(self._ref("DATA-TRANSFORMATION", "/Pkg/DTInv"))
        data_mapping.addSubElementMapping(SubElementMapping())
        data_mapping.addTextTableMapping(TextTableMapping())
        mapping.addDataMapping(data_mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeVariableAndParameterInterfaceMapping(parent, mapping)
        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))
        dpm = reparsed.find("{%s}VARIABLE-AND-PARAMETER-INTERFACE-MAPPING/{%s}DATA-MAPPINGS/{%s}DATA-PROTOTYPE-MAPPING" % (NS, NS, NS))
        assert [child.tag.split("}")[-1] for child in dpm] == [
            "FIRST-DATA-PROTOTYPE-REF",
            "FIRST-TO-SECOND-DATA-TRANSFORMATION-REF",
            "SECOND-DATA-PROTOTYPE-REF",
            "SECOND-TO-FIRST-DATA-TRANSFORMATION-REF",
            "SUB-ELEMENT-MAPPINGS",
            "TEXT-TABLE-MAPPINGS",
        ]
        assert dpm.find("{%s}FIRST-DATA-PROTOTYPE-REF" % NS).text == "/Pkg/First"
        assert dpm.find("{%s}FIRST-TO-SECOND-DATA-TRANSFORMATION-REF" % NS).text == "/Pkg/DT"
        assert dpm.find("{%s}SECOND-DATA-PROTOTYPE-REF" % NS).text == "/Pkg/Second"
        assert dpm.find("{%s}SECOND-TO-FIRST-DATA-TRANSFORMATION-REF" % NS).text == "/Pkg/DTInv"

        mapping2 = map_set.createVariableAndParameterInterfaceMapping("VAPIM2")
        ARXMLParser().readVariableAndParameterInterfaceMapping(reparsed[0], mapping2)
        parsed_dpm = mapping2.getDataMappings()[0]
        assert isinstance(parsed_dpm, DataPrototypeMapping)
        assert parsed_dpm.getFirstDataPrototypeRef().getValue() == "/Pkg/First"
        assert parsed_dpm.getFirstToSecondDataTransformationRef().getValue() == "/Pkg/DT"
        assert parsed_dpm.getSecondDataPrototypeRef().getValue() == "/Pkg/Second"
        assert parsed_dpm.getSecondToFirstDataTransformationRef().getValue() == "/Pkg/DTInv"
        assert len(parsed_dpm.getSubElementMappings()) == 1
        assert len(parsed_dpm.getTextTableMappings()) == 1

    def test_empty_data_prototype_mapping_wrappers_not_serialized(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import DataPrototypeMapping

        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        map_set = pkg.createPortInterfaceMappingSet("PIMS")
        mapping = map_set.createVariableAndParameterInterfaceMapping("VAPIM")
        mapping.addDataMapping(DataPrototypeMapping())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeVariableAndParameterInterfaceMapping(parent, mapping)
        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))
        dpm = reparsed.find("{%s}VARIABLE-AND-PARAMETER-INTERFACE-MAPPING/{%s}DATA-MAPPINGS/{%s}DATA-PROTOTYPE-MAPPING" % (NS, NS, NS))
        assert dpm is not None
        assert len(list(dpm)) == 0

        mapping2 = map_set.createVariableAndParameterInterfaceMapping("VAPIM2")
        ARXMLParser().readVariableAndParameterInterfaceMapping(reparsed[0], mapping2)
        parsed_dpm = mapping2.getDataMappings()[0]
        assert parsed_dpm.getSubElementMappings() == []
        assert parsed_dpm.getTextTableMappings() == []
