"""Writer tests for the timing instance refs (MODE-IN-*-INSTANCE-REF, TIMING-MODE-INSTANCE, TIMING-EXTENSION-RESOURCE)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    AutosarOperationArgumentInstance,
    ModeInBswInstanceRef,
    ModeInSwcInstanceRef,
    OperationArgumentInComponentInstanceRef,
    TimingExtensionResource,
    TimingModeInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    if xml_str.rstrip().endswith("/>"):
        xml_str = xml_str.rstrip()[:-2].rstrip() + ' xmlns="http://autosar.org/schema/r4.0"/>'
    else:
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestWriteTimingInstanceRefs:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_bsw_iref(self) -> ModeInBswInstanceRef:
        iref = ModeInBswInstanceRef()
        iref.setContextBswImplementationRef(RefType().setValue("/Pkg/BswImpl").setDest("BSW-IMPLEMENTATION"))
        iref.setContextModeDeclarationGroupPrototypeRef(RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE"))
        iref.setTargetModeDeclarationRef(RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION"))
        return iref

    def _build_swc_iref(self) -> ModeInSwcInstanceRef:
        iref = ModeInSwcInstanceRef()
        iref.setBaseRef(RefType().setValue("/Pkg/SwcType").setDest("SW-COMPONENT-TYPE"))
        iref.addContextComponentRef(RefType().setValue("/Pkg/SwcProto1").setDest("SW-COMPONENT-PROTOTYPE"))
        iref.addContextComponentRef(RefType().setValue("/Pkg/SwcProto2").setDest("SW-COMPONENT-PROTOTYPE"))
        iref.setContextPortRef(RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE"))
        iref.setContextModeDeclarationGroupPrototypeRef(RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE"))
        iref.setTargetModeDeclarationRef(RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION"))
        return iref

    def test_round_trip_mode_in_bsw_instance_ref(self):
        iref = self._build_bsw_iref()

        element = ET.Element("MODE-IN-BSW-INSTANCE-REF")
        ARXMLWriter().writeModeInBswInstanceRef(element, iref)
        assert element.find("CONTEXT-BSW-IMPLEMENTATION-REF") is not None

        reloaded = ARXMLParser().readModeInBswInstanceRef(_round_trip(element))
        assert isinstance(reloaded, ModeInBswInstanceRef)
        assert reloaded.getContextBswImplementationRef().getValue() == "/Pkg/BswImpl"
        assert reloaded.getContextBswImplementationRef().getDest() == "BSW-IMPLEMENTATION"
        assert reloaded.getContextModeDeclarationGroupPrototypeRef().getValue() == "/Pkg/Mdgp"
        assert reloaded.getContextModeDeclarationGroupPrototypeRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert reloaded.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"
        assert reloaded.getTargetModeDeclarationRef().getDest() == "MODE-DECLARATION"

    def test_round_trip_mode_in_swc_instance_ref(self):
        iref = self._build_swc_iref()

        element = ET.Element("MODE-IN-SWC-INSTANCE-REF")
        ARXMLWriter().writeModeInSwcInstanceRef(element, iref)

        component_refs = element.findall("CONTEXT-COMPONENT-REF")
        assert len(component_refs) == 2
        assert component_refs[0].text == "/Pkg/SwcProto1"
        assert component_refs[0].attrib["DEST"] == "SW-COMPONENT-PROTOTYPE"
        assert component_refs[1].text == "/Pkg/SwcProto2"

        reloaded = ARXMLParser().readModeInSwcInstanceRef(_round_trip(element))
        assert isinstance(reloaded, ModeInSwcInstanceRef)
        component_refs = reloaded.getContextComponentRefs()
        assert len(component_refs) == 2
        assert component_refs[0].getValue() == "/Pkg/SwcProto1"
        assert component_refs[1].getValue() == "/Pkg/SwcProto2"
        assert component_refs[1].getDest() == "SW-COMPONENT-PROTOTYPE"
        assert reloaded.getContextPortRef().getValue() == "/Pkg/Port"
        assert reloaded.getContextPortRef().getDest() == "PORT-PROTOTYPE"
        assert reloaded.getContextModeDeclarationGroupPrototypeRef().getValue() == "/Pkg/Mdgp"
        assert reloaded.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"
        assert reloaded.getTargetModeDeclarationRef().getDest() == "MODE-DECLARATION"

    def test_write_mode_in_swc_base_ref_has_no_xml_element(self):
        iref = self._build_swc_iref()

        element = ET.Element("MODE-IN-SWC-INSTANCE-REF")
        ARXMLWriter().writeModeInSwcInstanceRef(element, iref)
        assert len(element.findall("*")) == 5
        assert element.find("BASE-REF") is None

    def test_round_trip_timing_mode_instance(self):
        parent = self._parent()
        instance = TimingModeInstance(parent, "ModeInstance1")
        swc_iref = self._build_swc_iref()
        instance.setModeInstance(swc_iref)

        element = ET.Element("TIMING-MODE-INSTANCE")
        ARXMLWriter().writeTimingModeInstance(element, instance)
        mode_instance_tag = element.find("MODE-INSTANCE")
        assert mode_instance_tag is not None
        assert mode_instance_tag.find("MODE-IN-SWC-INSTANCE-REF") is not None

        reloaded = TimingModeInstance(parent, "ModeInstance1")
        ARXMLParser().readTimingModeInstance(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "ModeInstance1"
        mode_instance = reloaded.getModeInstance()
        assert isinstance(mode_instance, ModeInSwcInstanceRef)
        assert mode_instance.getContextComponentRefs()[0].getValue() == "/Pkg/SwcProto1"
        assert mode_instance.getContextPortRef().getValue() == "/Pkg/Port"
        assert mode_instance.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_write_timing_mode_instance_no_mode(self):
        parent = self._parent()
        instance = TimingModeInstance(parent, "ModeInstance1")

        element = ET.Element("TIMING-MODE-INSTANCE")
        ARXMLWriter().writeTimingModeInstance(element, instance)
        assert element.find("MODE-INSTANCE") is None
        assert element.find("SHORT-NAME").text == "ModeInstance1"

    def test_round_trip_timing_extension_resource(self):
        parent = self._parent()
        resource = TimingExtensionResource(parent, "Resource1")
        mode = resource.createTimingMode("ModeInstance1")
        bsw_iref = self._build_bsw_iref()
        mode.setModeInstance(bsw_iref)

        element = ET.Element("TIMING-EXTENSION-RESOURCE")
        ARXMLWriter().writeTimingExtensionResource(element, resource)
        modes_tag = element.find("TIMING-MODES")
        assert modes_tag is not None
        mode_tag = modes_tag.find("TIMING-MODE-INSTANCE")
        assert mode_tag is not None
        assert mode_tag.find("SHORT-NAME").text == "ModeInstance1"
        assert mode_tag.find("MODE-INSTANCE/MODE-IN-BSW-INSTANCE-REF") is not None

        reloaded = ARXMLParser().readTimingExtensionResource(parent, _round_trip(element))
        assert reloaded.getShortName() == "Resource1"
        modes = reloaded.getTimingModes()
        assert len(modes) == 1
        mode = modes[0]
        assert mode.getShortName() == "ModeInstance1"
        mode_instance = mode.getModeInstance()
        assert isinstance(mode_instance, ModeInBswInstanceRef)
        assert mode_instance.getContextBswImplementationRef().getValue() == "/Pkg/BswImpl"
        assert mode_instance.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_write_timing_extension_resource_empty_wrapper_lists(self):
        parent = self._parent()
        resource = TimingExtensionResource(parent, "Resource1")

        element = ET.Element("TIMING-EXTENSION-RESOURCE")
        ARXMLWriter().writeTimingExtensionResource(element, resource)
        assert element.find("TIMING-MODES") is None
        assert element.find("TIMING-ARGUMENTS") is None
        assert element.find("TIMING-VARIABLES") is None

        reloaded = ARXMLParser().readTimingExtensionResource(parent, _round_trip(element))
        assert reloaded.getShortName() == "Resource1"
        assert reloaded.getTimingModes() == []


class TestWriteAutosarOperationArgumentInstance:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_autosar_operation_argument_instance(self):
        parent = self._parent()
        instance = AutosarOperationArgumentInstance(parent, "Arg1")
        instance.setOperationArgumentInstanceIRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))

        element = ET.Element("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        ARXMLWriter().writeAutosarOperationArgumentInstance(element, instance)
        iref_tag = element.find("OPERATION-ARGUMENT-INSTANCE-IREF")
        assert iref_tag is not None
        target = iref_tag.find("TARGET-DATA-PROTOTYPE-REF")
        assert target is not None
        assert target.text == "/Pkg/DP"
        assert target.attrib["DEST"] == "DATA-PROTOTYPE"

        reloaded = ARXMLParser().readAutosarOperationArgumentInstance(parent, _round_trip(element))
        assert reloaded.getShortName() == "Arg1"
        iref = reloaded.getOperationArgumentInstanceIRef()
        assert iref.getValue() == "/Pkg/DP"
        assert iref.getDest() == "DATA-PROTOTYPE"

    def test_write_without_iref(self):
        parent = self._parent()
        instance = AutosarOperationArgumentInstance(parent, "Arg1")

        element = ET.Element("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        ARXMLWriter().writeAutosarOperationArgumentInstance(element, instance)
        assert element.find("OPERATION-ARGUMENT-INSTANCE-IREF") is None


class TestWriteOperationArgumentInComponentInstanceRef:
    def test_round_trip_operation_argument_in_component_instance_ref(self):
        iref = OperationArgumentInComponentInstanceRef()
        iref.addContextComponentRef(RefType().setValue("/Pkg/SwcProto1").setDest("SW-COMPONENT-PROTOTYPE"))
        iref.addContextComponentRef(RefType().setValue("/Pkg/SwcProto2").setDest("SW-COMPONENT-PROTOTYPE"))
        iref.setContextPortPrototypeRef(RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE"))
        iref.setContextOperationRef(RefType().setValue("/Pkg/Op").setDest("CLIENT-SERVER-OPERATION"))
        iref.setRootArgumentDataPrototypeRef(RefType().setValue("/Pkg/RootArg").setDest("ARGUMENT-DATA-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))

        element = ET.Element("OPERATION-ARGUMENT-INSTANCE-IREF")
        ARXMLWriter().writeOperationArgumentInComponentInstanceRef(element, iref)
        context_components = element.findall("CONTEXT-COMPONENT-REF")
        assert len(context_components) == 2
        assert context_components[0].text == "/Pkg/SwcProto1"
        assert element.find("CONTEXT-PORT-PROTOTYPE-REF").text == "/Pkg/Port"
        assert element.find("CONTEXT-OPERATION-REF").text == "/Pkg/Op"
        assert element.find("ROOT-ARGUMENT-DATA-PROTOTYPE-REF").text == "/Pkg/RootArg"
        assert element.find("TARGET-DATA-PROTOTYPE-REF").text == "/Pkg/DP"

        reloaded = ARXMLParser().readOperationArgumentInComponentInstanceRef(_round_trip(element))
        assert len(reloaded.getContextComponentRefs()) == 2
        assert reloaded.getContextComponentRefs()[1].getValue() == "/Pkg/SwcProto2"
        assert reloaded.getContextPortPrototypeRef().getValue() == "/Pkg/Port"
        assert reloaded.getContextOperationRef().getValue() == "/Pkg/Op"
        assert reloaded.getRootArgumentDataPrototypeRef().getValue() == "/Pkg/RootArg"
        assert reloaded.getTargetDataPrototypeRef().getValue() == "/Pkg/DP"

    def test_write_empty(self):
        iref = OperationArgumentInComponentInstanceRef()
        element = ET.Element("OPERATION-ARGUMENT-INSTANCE-IREF")
        ARXMLWriter().writeOperationArgumentInComponentInstanceRef(element, iref)
        assert len(element.findall("*")) == 0
