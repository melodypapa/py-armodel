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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ArgumentDirectionEnum,
    Boolean,
    Integer,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ApplicationError,
    ClientServerInterface,
    DataPrototypeMapping,
    ServerArgumentImplPolicyEnum,
    SubElementMapping,
    TextTableMapping,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum
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
        assert mode_group_element.find("{%s}SW-CALIBRATION-ACCESS" % NS).text == "READ-ONLY"

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


class TestModeDeclarationMappingRoundTrip:
    def _ref(self, dest, value):
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_mode_declaration_mapping_field_values_and_order(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ModeDeclarationMapping, ModeDeclarationMappingSet

        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        mapping_set = pkg.createModeDeclarationMappingSet("MDMS")
        mapping = mapping_set.createModeDeclarationMapping("MDM")
        mapping.addFirstModeRef(self._ref("MODE-DECLARATION", "/Pkg/UserMode"))
        mapping.addFirstModeRef(self._ref("MODE-DECLARATION", "/Pkg/UserMode2"))
        mapping.setSecondModeRef(self._ref("MODE-DECLARATION", "/Pkg/ManagerMode"))

        root = _serialize(ET.Element("AR-PACKAGE"), mapping_set)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}MODE-DECLARATION-MAPPING-SET" % tuple([NS] * 3))
        mdm = element.find("{%s}MODE-DECLARATION-MAPPINGS/{%s}MODE-DECLARATION-MAPPING" % (NS, NS))
        assert [child.tag.split("}")[-1] for child in mdm] == [
            "SHORT-NAME",
            "FIRST-MODE-REFS",
            "SECOND-MODE-REF",
        ]
        first_refs = mdm.findall("{%s}FIRST-MODE-REFS/{%s}FIRST-MODE-REF" % (NS, NS))
        assert [ref.text for ref in first_refs] == ["/Pkg/UserMode", "/Pkg/UserMode2"]
        assert all(ref.get("DEST") == "MODE-DECLARATION" for ref in first_refs)
        assert mdm.find("{%s}SECOND-MODE-REF" % NS).text == "/Pkg/ManagerMode"

        parsed = _reparse(root)
        parsed_set = parsed.getModeDeclarationMappingSets()[0]
        assert isinstance(parsed_set, ModeDeclarationMappingSet)
        parsed_mapping = parsed_set.getModeDeclarationMappings()[0]
        assert isinstance(parsed_mapping, ModeDeclarationMapping)
        assert parsed_mapping.getShortName() == "MDM"
        assert [ref.getValue() for ref in parsed_mapping.getFirstModeRefs()] == ["/Pkg/UserMode", "/Pkg/UserMode2"]
        assert parsed_mapping.getSecondModeRef().getValue() == "/Pkg/ManagerMode"

    def test_empty_mode_declaration_mapping_set_round_trip(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        mapping_set = pkg.createModeDeclarationMappingSet("MDMS")

        root = _serialize(ET.Element("AR-PACKAGE"), mapping_set)
        element = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}MODE-DECLARATION-MAPPING-SET" % tuple([NS] * 3))
        assert element.find("{%s}MODE-DECLARATION-MAPPINGS" % NS) is None

        parsed = _reparse(root)
        parsed_set = parsed.getModeDeclarationMappingSets()[0]
        assert parsed_set.getModeDeclarationMappings() == []


class TestImplementationDataTypeSubElementRefRoundTrip:
    def _ref(self, dest, value):
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_implementation_data_type_sub_element_ref_field_values(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
            ImplementationDataTypeSubElementRef,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
            ArParameterInImplementationDataInstanceRef,
            ArVariableInImplementationDataInstanceRef,
        )

        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        map_set = pkg.createPortInterfaceMappingSet("PIMS")
        mapping = map_set.createVariableAndParameterInterfaceMapping("VAPIM")
        data_mapping = DataPrototypeMapping()
        sub_mapping = SubElementMapping()

        first = ImplementationDataTypeSubElementRef()
        variable_iref = ArVariableInImplementationDataInstanceRef()
        variable_iref.setPortPrototypeRef(self._ref("PORT-PROTOTYPE", "/Pkg/PPort"))
        variable_iref.setRootVariableDataPrototypeRef(self._ref("VARIABLE-DATA-PROTOTYPE", "/Pkg/RootVar"))
        variable_iref.addContextDataPrototypeRef(self._ref("IMPLEMENTATION-DATA-TYPE-ELEMENT", "/Pkg/Ctx1"))
        variable_iref.setTargetDataPrototypeRef(self._ref("IMPLEMENTATION-DATA-TYPE-ELEMENT", "/Pkg/Elem"))
        first.setImplementationDataTypeElement(variable_iref)

        second = ImplementationDataTypeSubElementRef()
        parameter_iref = ArParameterInImplementationDataInstanceRef()
        parameter_iref.setRootParameterDataPrototypeRef(self._ref("PARAMETER-DATA-PROTOTYPE", "/Pkg/RootParam"))
        parameter_iref.setTargetDataPrototypeRef(self._ref("IMPLEMENTATION-DATA-TYPE-ELEMENT", "/Pkg/ParamElem"))
        second.setParameterImplementationDataTypeElement(parameter_iref)

        sub_mapping.setFirstElement(first)
        sub_mapping.setSecondElement(second)
        data_mapping.addSubElementMapping(sub_mapping)
        mapping.addDataMapping(data_mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeVariableAndParameterInterfaceMapping(parent, mapping)
        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

        first_element = reparsed.find(
            "{%s}VARIABLE-AND-PARAMETER-INTERFACE-MAPPING/{%s}DATA-MAPPINGS/{%s}DATA-PROTOTYPE-MAPPING/"
            "{%s}SUB-ELEMENT-MAPPINGS/{%s}SUB-ELEMENT-MAPPING/{%s}FIRST-ELEMENTS/{%s}IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF" % (NS, NS, NS, NS, NS, NS, NS)
        )
        assert [child.tag.split("}")[-1] for child in first_element] == ["IMPLEMENTATION-DATA-TYPE-ELEMENT"]
        impl_element = first_element.find("{%s}IMPLEMENTATION-DATA-TYPE-ELEMENT" % NS)
        assert [child.tag.split("}")[-1] for child in impl_element] == [
            "PORT-PROTOTYPE-REF",
            "ROOT-VARIABLE-DATA-PROTOTYPE-REF",
            "CONTEXT-DATA-PROTOTYPE-REFS",
            "TARGET-DATA-PROTOTYPE-REF",
        ]
        assert impl_element.find("{%s}ROOT-VARIABLE-DATA-PROTOTYPE-REF" % NS).text == "/Pkg/RootVar"
        ctx_refs = impl_element.findall("{%s}CONTEXT-DATA-PROTOTYPE-REFS/{%s}CONTEXT-DATA-PROTOTYPE-REF" % (NS, NS))
        assert [ref.text for ref in ctx_refs] == ["/Pkg/Ctx1"]

        second_element = reparsed.find(
            "{%s}VARIABLE-AND-PARAMETER-INTERFACE-MAPPING/{%s}DATA-MAPPINGS/{%s}DATA-PROTOTYPE-MAPPING/"
            "{%s}SUB-ELEMENT-MAPPINGS/{%s}SUB-ELEMENT-MAPPING/{%s}SECOND-ELEMENTS/{%s}IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF" % (NS, NS, NS, NS, NS, NS, NS)
        )
        param_element = second_element.find("{%s}PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT" % NS)
        assert [child.tag.split("}")[-1] for child in param_element] == [
            "ROOT-PARAMETER-DATA-PROTOTYPE-REF",
            "TARGET-DATA-PROTOTYPE-REF",
        ]
        assert param_element.find("{%s}ROOT-PARAMETER-DATA-PROTOTYPE-REF" % NS).text == "/Pkg/RootParam"
        assert param_element.find("{%s}CONTEXT-DATA-PROTOTYPE-REFS" % NS) is None

        mapping2 = map_set.createVariableAndParameterInterfaceMapping("VAPIM2")
        ARXMLParser().readVariableAndParameterInterfaceMapping(reparsed[0], mapping2)
        parsed_sub = mapping2.getDataMappings()[0].getSubElementMappings()[0]
        parsed_first = parsed_sub.getFirstElement()
        assert isinstance(parsed_first, ImplementationDataTypeSubElementRef)
        parsed_variable_iref = parsed_first.getImplementationDataTypeElement()
        assert isinstance(parsed_variable_iref, ArVariableInImplementationDataInstanceRef)
        assert parsed_variable_iref.getPortPrototypeRef().getValue() == "/Pkg/PPort"
        assert parsed_variable_iref.getRootVariableDataPrototypeRef().getValue() == "/Pkg/RootVar"
        assert parsed_variable_iref.getContextDataPrototypeRefs()[0].getValue() == "/Pkg/Ctx1"
        assert parsed_variable_iref.getTargetDataPrototypeRef().getValue() == "/Pkg/Elem"
        parsed_second = parsed_sub.getSecondElement()
        assert isinstance(parsed_second, ImplementationDataTypeSubElementRef)
        parsed_parameter_iref = parsed_second.getParameterImplementationDataTypeElement()
        assert isinstance(parsed_parameter_iref, ArParameterInImplementationDataInstanceRef)
        assert parsed_parameter_iref.getRootParameterDataPrototypeRef().getValue() == "/Pkg/RootParam"
        assert parsed_parameter_iref.getTargetDataPrototypeRef().getValue() == "/Pkg/ParamElem"

    def test_application_composite_sub_element_ref_still_round_trips(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
            ApplicationCompositeDataTypeSubElementRef,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (
            ApplicationCompositeElementInPortInterfaceInstanceRef,
        )

        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        map_set = pkg.createPortInterfaceMappingSet("PIMS")
        mapping = map_set.createVariableAndParameterInterfaceMapping("VAPIM")
        data_mapping = DataPrototypeMapping()
        sub_mapping = SubElementMapping()
        first = ApplicationCompositeDataTypeSubElementRef()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        iref.setRootDataPrototypeRef(self._ref("APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE", "/Pkg/Root"))
        iref.setTargetDataPrototypeRef(self._ref("APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE", "/Pkg/Target"))
        first.setApplicationCompositeElementIRef(iref)
        sub_mapping.setFirstElement(first)
        data_mapping.addSubElementMapping(sub_mapping)
        mapping.addDataMapping(data_mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeVariableAndParameterInterfaceMapping(parent, mapping)
        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

        mapping2 = map_set.createVariableAndParameterInterfaceMapping("VAPIM2")
        ARXMLParser().readVariableAndParameterInterfaceMapping(reparsed[0], mapping2)
        parsed_first = mapping2.getDataMappings()[0].getSubElementMappings()[0].getFirstElement()
        assert isinstance(parsed_first, ApplicationCompositeDataTypeSubElementRef)
        assert parsed_first.getApplicationCompositeElementIRef().getRootDataPrototypeRef().getValue() == "/Pkg/Root"
        assert parsed_first.getApplicationCompositeElementIRef().getTargetDataPrototypeRef().getValue() == "/Pkg/Target"
