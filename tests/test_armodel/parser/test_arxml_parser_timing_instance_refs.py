"""Parser tests for the timing instance refs (MODE-IN-*-INSTANCE-REF, TIMING-MODE-INSTANCE, TIMING-EXTENSION-RESOURCE)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    ModeInBswInstanceRef,
    ModeInSwcInstanceRef,
    OperationArgumentInComponentInstanceRef,
    TimingModeInstance,
    VariableInComponentInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser


def _parent():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document.createARPackage("AUTOSAR")


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    if xml_str.rstrip().endswith("/>"):
        xml_str = xml_str.rstrip()[:-2].rstrip() + ' xmlns="http://autosar.org/schema/r4.0"/>'
    else:
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestReadModeInBswInstanceRef:
    def test_read_all_members(self):
        element = ET.Element("MODE-IN-BSW-INSTANCE-REF")
        bsw_ref = ET.SubElement(element, "CONTEXT-BSW-IMPLEMENTATION-REF")
        bsw_ref.attrib["DEST"] = "BSW-IMPLEMENTATION"
        bsw_ref.text = "/Pkg/BswImpl"
        mdgp_ref = ET.SubElement(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")
        mdgp_ref.attrib["DEST"] = "MODE-DECLARATION-GROUP-PROTOTYPE"
        mdgp_ref.text = "/Pkg/Mdgp"
        mode_ref = ET.SubElement(element, "TARGET-MODE-DECLARATION-REF")
        mode_ref.attrib["DEST"] = "MODE-DECLARATION"
        mode_ref.text = "/Pkg/Mode"

        iref = ARXMLParser().readModeInBswInstanceRef(_round_trip(element))
        assert isinstance(iref, ModeInBswInstanceRef)
        assert iref.getContextBswImplementationRef().getValue() == "/Pkg/BswImpl"
        assert iref.getContextBswImplementationRef().getDest() == "BSW-IMPLEMENTATION"
        assert iref.getContextModeDeclarationGroupPrototypeRef().getValue() == "/Pkg/Mdgp"
        assert iref.getContextModeDeclarationGroupPrototypeRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert iref.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"
        assert iref.getTargetModeDeclarationRef().getDest() == "MODE-DECLARATION"

    def test_read_minimal(self):
        element = ET.Element("MODE-IN-BSW-INSTANCE-REF")

        iref = ARXMLParser().readModeInBswInstanceRef(_round_trip(element))
        assert isinstance(iref, ModeInBswInstanceRef)
        assert iref.getContextBswImplementationRef() is None
        assert iref.getContextModeDeclarationGroupPrototypeRef() is None
        assert iref.getTargetModeDeclarationRef() is None


class TestReadModeInSwcInstanceRef:
    def test_read_all_members(self):
        element = ET.Element("MODE-IN-SWC-INSTANCE-REF")
        comp1 = ET.SubElement(element, "CONTEXT-COMPONENT-REF")
        comp1.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp1.text = "/Pkg/SwcProto1"
        comp2 = ET.SubElement(element, "CONTEXT-COMPONENT-REF")
        comp2.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp2.text = "/Pkg/SwcProto2"
        port_ref = ET.SubElement(element, "CONTEXT-PORT-REF")
        port_ref.attrib["DEST"] = "PORT-PROTOTYPE"
        port_ref.text = "/Pkg/Port"
        mdgp_ref = ET.SubElement(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")
        mdgp_ref.attrib["DEST"] = "MODE-DECLARATION-GROUP-PROTOTYPE"
        mdgp_ref.text = "/Pkg/Mdgp"
        mode_ref = ET.SubElement(element, "TARGET-MODE-DECLARATION-REF")
        mode_ref.attrib["DEST"] = "MODE-DECLARATION"
        mode_ref.text = "/Pkg/Mode"

        iref = ARXMLParser().readModeInSwcInstanceRef(_round_trip(element))
        assert isinstance(iref, ModeInSwcInstanceRef)
        component_refs = iref.getContextComponentRefs()
        assert len(component_refs) == 2
        assert component_refs[0].getValue() == "/Pkg/SwcProto1"
        assert component_refs[0].getDest() == "SW-COMPONENT-PROTOTYPE"
        assert component_refs[1].getValue() == "/Pkg/SwcProto2"
        assert iref.getContextPortRef().getValue() == "/Pkg/Port"
        assert iref.getContextPortRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getContextModeDeclarationGroupPrototypeRef().getValue() == "/Pkg/Mdgp"
        assert iref.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_read_minimal(self):
        element = ET.Element("MODE-IN-SWC-INSTANCE-REF")

        iref = ARXMLParser().readModeInSwcInstanceRef(_round_trip(element))
        assert iref.getContextComponentRefs() == []
        assert iref.getContextPortRef() is None
        assert iref.getContextModeDeclarationGroupPrototypeRef() is None
        assert iref.getTargetModeDeclarationRef() is None

    def test_read_base_ref_absent_no_xml_element(self):
        element = ET.Element("MODE-IN-SWC-INSTANCE-REF")

        iref = ARXMLParser().readModeInSwcInstanceRef(_round_trip(element))
        assert iref.getBaseRef() is None


class TestReadTimingModeInstance:
    def test_read_mode_instance_swc(self):
        parent = _parent()
        element = ET.Element("TIMING-MODE-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "ModeInstance1"
        mode_instance_tag = ET.SubElement(element, "MODE-INSTANCE")
        swc_iref_tag = ET.SubElement(mode_instance_tag, "MODE-IN-SWC-INSTANCE-REF")
        port_ref = ET.SubElement(swc_iref_tag, "CONTEXT-PORT-REF")
        port_ref.attrib["DEST"] = "PORT-PROTOTYPE"
        port_ref.text = "/Pkg/Port"
        mode_ref = ET.SubElement(swc_iref_tag, "TARGET-MODE-DECLARATION-REF")
        mode_ref.attrib["DEST"] = "MODE-DECLARATION"
        mode_ref.text = "/Pkg/Mode"

        instance = TimingModeInstance(parent, "ModeInstance1")
        ARXMLParser().readTimingModeInstance(_round_trip(element), instance)
        assert instance.getShortName() == "ModeInstance1"
        mode_instance = instance.getModeInstance()
        assert isinstance(mode_instance, ModeInSwcInstanceRef)
        assert mode_instance.getContextPortRef().getValue() == "/Pkg/Port"
        assert mode_instance.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_read_mode_instance_bsw(self):
        parent = _parent()
        element = ET.Element("TIMING-MODE-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "ModeInstance1"
        mode_instance_tag = ET.SubElement(element, "MODE-INSTANCE")
        bsw_iref_tag = ET.SubElement(mode_instance_tag, "MODE-IN-BSW-INSTANCE-REF")
        bsw_ref = ET.SubElement(bsw_iref_tag, "CONTEXT-BSW-IMPLEMENTATION-REF")
        bsw_ref.attrib["DEST"] = "BSW-IMPLEMENTATION"
        bsw_ref.text = "/Pkg/BswImpl"
        mode_ref = ET.SubElement(bsw_iref_tag, "TARGET-MODE-DECLARATION-REF")
        mode_ref.attrib["DEST"] = "MODE-DECLARATION"
        mode_ref.text = "/Pkg/Mode"

        instance = TimingModeInstance(parent, "ModeInstance1")
        ARXMLParser().readTimingModeInstance(_round_trip(element), instance)
        mode_instance = instance.getModeInstance()
        assert isinstance(mode_instance, ModeInBswInstanceRef)
        assert mode_instance.getContextBswImplementationRef().getValue() == "/Pkg/BswImpl"
        assert mode_instance.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_read_no_mode_instance(self):
        parent = _parent()
        element = ET.Element("TIMING-MODE-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "ModeInstance1"

        instance = TimingModeInstance(parent, "ModeInstance1")
        ARXMLParser().readTimingModeInstance(_round_trip(element), instance)
        assert instance.getModeInstance() is None


class TestReadTimingExtensionResource:
    def _build_resource_element(self) -> ET.Element:
        element = ET.Element("TIMING-EXTENSION-RESOURCE")
        ET.SubElement(element, "SHORT-NAME").text = "Resource1"
        arguments_tag = ET.SubElement(element, "TIMING-ARGUMENTS")
        argument_tag = ET.SubElement(arguments_tag, "AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        ET.SubElement(argument_tag, "SHORT-NAME").text = "Arg1"
        arg_iref_tag = ET.SubElement(argument_tag, "OPERATION-ARGUMENT-INSTANCE-IREF")
        op_ref = ET.SubElement(arg_iref_tag, "CONTEXT-OPERATION-REF")
        op_ref.attrib["DEST"] = "CLIENT-SERVER-OPERATION"
        op_ref.text = "/Pkg/Op"
        target_arg_ref = ET.SubElement(arg_iref_tag, "TARGET-DATA-PROTOTYPE-REF")
        target_arg_ref.attrib["DEST"] = "DATA-PROTOTYPE"
        target_arg_ref.text = "/Pkg/DP"
        modes_tag = ET.SubElement(element, "TIMING-MODES")
        mode_tag = ET.SubElement(modes_tag, "TIMING-MODE-INSTANCE")
        ET.SubElement(mode_tag, "SHORT-NAME").text = "ModeInstance1"
        mode_instance_tag = ET.SubElement(mode_tag, "MODE-INSTANCE")
        swc_iref_tag = ET.SubElement(mode_instance_tag, "MODE-IN-SWC-INSTANCE-REF")
        port_ref = ET.SubElement(swc_iref_tag, "CONTEXT-PORT-REF")
        port_ref.attrib["DEST"] = "PORT-PROTOTYPE"
        port_ref.text = "/Pkg/Port"
        mode_ref = ET.SubElement(swc_iref_tag, "TARGET-MODE-DECLARATION-REF")
        mode_ref.attrib["DEST"] = "MODE-DECLARATION"
        mode_ref.text = "/Pkg/Mode"
        variables_tag = ET.SubElement(element, "TIMING-VARIABLES")
        variable_tag = ET.SubElement(variables_tag, "AUTOSAR-VARIABLE-INSTANCE")
        ET.SubElement(variable_tag, "SHORT-NAME").text = "Var1"
        var_iref_tag = ET.SubElement(variable_tag, "VARIABLE-INSTANCE-IREF")
        target_var_ref = ET.SubElement(var_iref_tag, "TARGET-DATA-PROTOTYPE-REF")
        target_var_ref.attrib["DEST"] = "DATA-PROTOTYPE"
        target_var_ref.text = "/Pkg/VarDP"
        return element

    def test_read_timing_modes(self):
        parent = _parent()

        resource = ARXMLParser().readTimingExtensionResource(parent, _round_trip(self._build_resource_element()))
        assert resource.getShortName() == "Resource1"
        arguments = resource.getTimingArguments()
        assert len(arguments) == 1
        argument = arguments[0]
        assert isinstance(argument, AutosarOperationArgumentInstance)
        assert argument.getShortName() == "Arg1"
        arg_iref = argument.getOperationArgumentInstanceIRef()
        assert isinstance(arg_iref, OperationArgumentInComponentInstanceRef)
        assert arg_iref.getContextOperationRef().getValue() == "/Pkg/Op"
        assert arg_iref.getTargetDataPrototypeRef().getValue() == "/Pkg/DP"
        modes = resource.getTimingModes()
        assert len(modes) == 1
        mode = modes[0]
        assert isinstance(mode, TimingModeInstance)
        assert mode.getShortName() == "ModeInstance1"
        mode_instance = mode.getModeInstance()
        assert isinstance(mode_instance, ModeInSwcInstanceRef)
        assert mode_instance.getContextPortRef().getValue() == "/Pkg/Port"
        assert mode_instance.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"
        variables = resource.getTimingVariables()
        assert len(variables) == 1
        variable = variables[0]
        assert isinstance(variable, AutosarVariableInstance)
        assert variable.getShortName() == "Var1"
        var_iref = variable.getVariableInstanceIRef()
        assert isinstance(var_iref, VariableInComponentInstanceRef)
        assert var_iref.getTargetDataPrototypeRef().getValue() == "/Pkg/VarDP"

    def test_read_empty(self):
        parent = _parent()
        element = ET.Element("TIMING-EXTENSION-RESOURCE")
        ET.SubElement(element, "SHORT-NAME").text = "Resource1"

        resource = ARXMLParser().readTimingExtensionResource(parent, _round_trip(element))
        assert resource.getShortName() == "Resource1"
        assert resource.getTimingModes() == []


class TestReadAutosarOperationArgumentInstance:
    def _build_element(self) -> ET.Element:
        element = ET.Element("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "Arg1"
        iref_tag = ET.SubElement(element, "OPERATION-ARGUMENT-INSTANCE-IREF")
        comp = ET.SubElement(iref_tag, "CONTEXT-COMPONENT-REF")
        comp.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp.text = "/Pkg/SwcProto"
        op = ET.SubElement(iref_tag, "CONTEXT-OPERATION-REF")
        op.attrib["DEST"] = "CLIENT-SERVER-OPERATION"
        op.text = "/Pkg/Op"
        target = ET.SubElement(iref_tag, "TARGET-DATA-PROTOTYPE-REF")
        target.attrib["DEST"] = "DATA-PROTOTYPE"
        target.text = "/Pkg/DP"
        return element

    def test_read_with_iref(self):
        parent = _parent()
        instance = AutosarOperationArgumentInstance(parent, "Arg1")
        ARXMLParser().readAutosarOperationArgumentInstance(_round_trip(self._build_element()), instance)
        assert isinstance(instance, AutosarOperationArgumentInstance)
        assert instance.getShortName() == "Arg1"
        iref = instance.getOperationArgumentInstanceIRef()
        assert isinstance(iref, OperationArgumentInComponentInstanceRef)
        assert iref.getContextComponentRefs()[0].getValue() == "/Pkg/SwcProto"
        assert iref.getContextOperationRef().getValue() == "/Pkg/Op"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Pkg/DP"

    def test_read_without_iref(self):
        parent = _parent()
        element = ET.Element("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "Arg1"

        instance = AutosarOperationArgumentInstance(parent, "Arg1")
        ARXMLParser().readAutosarOperationArgumentInstance(_round_trip(element), instance)
        assert instance.getOperationArgumentInstanceIRef() is None


class TestReadAutosarVariableInstance:
    def _build_element(self) -> ET.Element:
        element = ET.Element("AUTOSAR-VARIABLE-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "Var1"
        iref_tag = ET.SubElement(element, "VARIABLE-INSTANCE-IREF")
        comp = ET.SubElement(iref_tag, "CONTEXT-COMPONENT-REF")
        comp.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp.text = "/Pkg/SwcProto"
        port = ET.SubElement(iref_tag, "CONTEXT-PORT-PROTOTYPE-REF")
        port.attrib["DEST"] = "PORT-PROTOTYPE"
        port.text = "/Pkg/Port"
        target = ET.SubElement(iref_tag, "TARGET-DATA-PROTOTYPE-REF")
        target.attrib["DEST"] = "DATA-PROTOTYPE"
        target.text = "/Pkg/DP"
        return element

    def test_read_with_iref(self):
        parent = _parent()
        instance = AutosarVariableInstance(parent, "Var1")
        ARXMLParser().readAutosarVariableInstance(_round_trip(self._build_element()), instance)
        assert isinstance(instance, AutosarVariableInstance)
        assert instance.getShortName() == "Var1"
        iref = instance.getVariableInstanceIRef()
        assert isinstance(iref, VariableInComponentInstanceRef)
        assert iref.getContextComponentRefs()[0].getValue() == "/Pkg/SwcProto"
        assert iref.getContextPortPrototypeRef().getValue() == "/Pkg/Port"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Pkg/DP"

    def test_read_without_iref(self):
        parent = _parent()
        element = ET.Element("AUTOSAR-VARIABLE-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "Var1"

        instance = AutosarVariableInstance(parent, "Var1")
        ARXMLParser().readAutosarVariableInstance(_round_trip(element), instance)
        assert instance.getVariableInstanceIRef() is None


class TestReadOperationArgumentInComponentInstanceRef:
    def _build_element(self) -> ET.Element:
        element = ET.Element("OPERATION-ARGUMENT-INSTANCE-IREF")
        comp1 = ET.SubElement(element, "CONTEXT-COMPONENT-REF")
        comp1.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp1.text = "/Pkg/SwcProto1"
        comp2 = ET.SubElement(element, "CONTEXT-COMPONENT-REF")
        comp2.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp2.text = "/Pkg/SwcProto2"
        port_ref = ET.SubElement(element, "CONTEXT-PORT-PROTOTYPE-REF")
        port_ref.attrib["DEST"] = "PORT-PROTOTYPE"
        port_ref.text = "/Pkg/Port"
        op_ref = ET.SubElement(element, "CONTEXT-OPERATION-REF")
        op_ref.attrib["DEST"] = "CLIENT-SERVER-OPERATION"
        op_ref.text = "/Pkg/Op"
        root_ref = ET.SubElement(element, "ROOT-ARGUMENT-DATA-PROTOTYPE-REF")
        root_ref.attrib["DEST"] = "ARGUMENT-DATA-PROTOTYPE"
        root_ref.text = "/Pkg/RootArg"
        target = ET.SubElement(element, "TARGET-DATA-PROTOTYPE-REF")
        target.attrib["DEST"] = "DATA-PROTOTYPE"
        target.text = "/Pkg/DP"
        return element

    def test_read_all_members(self):
        iref = ARXMLParser().readOperationArgumentInComponentInstanceRef(_round_trip(self._build_element()))
        assert isinstance(iref, OperationArgumentInComponentInstanceRef)
        context_components = iref.getContextComponentRefs()
        assert len(context_components) == 2
        assert context_components[0].getValue() == "/Pkg/SwcProto1"
        assert context_components[0].getDest() == "SW-COMPONENT-PROTOTYPE"
        assert iref.getContextPortPrototypeRef().getValue() == "/Pkg/Port"
        assert iref.getContextPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getContextOperationRef().getValue() == "/Pkg/Op"
        assert iref.getContextOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert iref.getRootArgumentDataPrototypeRef().getValue() == "/Pkg/RootArg"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Pkg/DP"
        assert iref.getTargetDataPrototypeRef().getDest() == "DATA-PROTOTYPE"

    def test_read_empty(self):
        element = ET.Element("OPERATION-ARGUMENT-INSTANCE-IREF")
        iref = ARXMLParser().readOperationArgumentInComponentInstanceRef(_round_trip(element))
        assert iref.getContextComponentRefs() == []
        assert iref.getContextPortPrototypeRef() is None
        assert iref.getContextOperationRef() is None
        assert iref.getRootArgumentDataPrototypeRef() is None
        assert iref.getContextDataPrototypeRefs() == []
        assert iref.getTargetDataPrototypeRef() is None


class TestReadVariableInComponentInstanceRef:
    def _build_element(self) -> ET.Element:
        element = ET.Element("VARIABLE-INSTANCE-IREF")
        comp1 = ET.SubElement(element, "CONTEXT-COMPONENT-REF")
        comp1.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp1.text = "/Pkg/SwcProto1"
        comp2 = ET.SubElement(element, "CONTEXT-COMPONENT-REF")
        comp2.attrib["DEST"] = "SW-COMPONENT-PROTOTYPE"
        comp2.text = "/Pkg/SwcProto2"
        port_ref = ET.SubElement(element, "CONTEXT-PORT-PROTOTYPE-REF")
        port_ref.attrib["DEST"] = "PORT-PROTOTYPE"
        port_ref.text = "/Pkg/Port"
        root_ref = ET.SubElement(element, "ROOT-VARIABLE-DATA-PROTOTYPE-REF")
        root_ref.attrib["DEST"] = "VARIABLE-DATA-PROTOTYPE"
        root_ref.text = "/Pkg/Var"
        cdp = ET.SubElement(element, "CONTEXT-DATA-PROTOTYPE-REF")
        cdp.attrib["DEST"] = "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"
        cdp.text = "/Pkg/CDP"
        target = ET.SubElement(element, "TARGET-DATA-PROTOTYPE-REF")
        target.attrib["DEST"] = "DATA-PROTOTYPE"
        target.text = "/Pkg/DP"
        return element

    def test_read_all_members(self):
        iref = ARXMLParser().readVariableInComponentInstanceRef(_round_trip(self._build_element()))
        assert isinstance(iref, VariableInComponentInstanceRef)
        context_components = iref.getContextComponentRefs()
        assert len(context_components) == 2
        assert context_components[0].getValue() == "/Pkg/SwcProto1"
        assert context_components[0].getDest() == "SW-COMPONENT-PROTOTYPE"
        assert iref.getContextPortPrototypeRef().getValue() == "/Pkg/Port"
        assert iref.getContextPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getRootVariableDataPrototypeRef().getValue() == "/Pkg/Var"
        assert iref.getRootVariableDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert iref.getContextDataPrototypeRefs()[0].getValue() == "/Pkg/CDP"
        assert iref.getContextDataPrototypeRefs()[0].getDest() == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Pkg/DP"
        assert iref.getTargetDataPrototypeRef().getDest() == "DATA-PROTOTYPE"

    def test_read_empty(self):
        element = ET.Element("VARIABLE-INSTANCE-IREF")
        iref = ARXMLParser().readVariableInComponentInstanceRef(_round_trip(element))
        assert iref.getContextComponentRefs() == []
        assert iref.getContextPortPrototypeRef() is None
        assert iref.getRootVariableDataPrototypeRef() is None
        assert iref.getContextDataPrototypeRefs() == []
        assert iref.getTargetDataPrototypeRef() is None
