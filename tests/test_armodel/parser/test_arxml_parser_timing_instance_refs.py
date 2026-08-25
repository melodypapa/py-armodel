"""Parser tests for the timing instance refs (MODE-IN-*-INSTANCE-REF, TIMING-MODE-INSTANCE, TIMING-EXTENSION-RESOURCE)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import ModeInBswInstanceRef, ModeInSwcInstanceRef, TimingModeInstance
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
        return element

    def test_read_timing_modes(self):
        parent = _parent()

        resource = ARXMLParser().readTimingExtensionResource(parent, _round_trip(self._build_resource_element()))
        assert resource.getShortName() == "Resource1"
        modes = resource.getTimingModes()
        assert len(modes) == 1
        mode = modes[0]
        assert isinstance(mode, TimingModeInstance)
        assert mode.getShortName() == "ModeInstance1"
        mode_instance = mode.getModeInstance()
        assert isinstance(mode_instance, ModeInSwcInstanceRef)
        assert mode_instance.getContextPortRef().getValue() == "/Pkg/Port"
        assert mode_instance.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"
        assert resource.getTimingArguments() == []
        assert resource.getTimingVariables() == []

    def test_read_empty(self):
        parent = _parent()
        element = ET.Element("TIMING-EXTENSION-RESOURCE")
        ET.SubElement(element, "SHORT-NAME").text = "Resource1"

        resource = ARXMLParser().readTimingExtensionResource(parent, _round_trip(element))
        assert resource.getShortName() == "Resource1"
        assert resource.getTimingModes() == []
