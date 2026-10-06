"""Writer round-trip tests for PncMapping (Table 5.45, p.266).

Serialized through the PNC-MAPPING element (DESCRIBABLE content + the
PNC-MAPPING group) and the PNC-MAPPINGS wrapper of SystemMapping
(AUTOSAR_00052.xsd l.119560).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import PortGroupInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping import PncMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWritePncMapping:
    def test_empty(self):
        mapping = PncMapping()
        parent = ET.Element("PARENT")
        ARXMLWriter().writePncMapping(parent, mapping)

        node = parent.find("PNC-MAPPING")
        assert node is not None
        assert node.find("IDENT") is None
        assert node.find("PNC-IDENTIFIER") is None
        assert node.find("SHORT-LABEL") is None
        assert node.find("VFC-IREFS") is None

    def test_full_element_order(self):
        mapping = PncMapping()
        mapping.addDynamicPncMappingPduGroupRef(_ref("/Groups/DynGroup1", "I-SIGNAL-I-PDU-GROUP"))
        mapping.createIdent("PncIdent1")
        mapping.addPhysicalChannelRef(_ref("/Topology/Can1", "CAN-PHYSICAL-CHANNEL"))
        mapping.addPncConsumedProvidedServiceInstanceGroupRef(_ref("/ServiceInstances/Group1", "CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP"))
        mapping.addPncGroupRef(_ref("/Groups/PncGroup1", "I-SIGNAL-I-PDU-GROUP"))
        pnc_identifier = PositiveInteger()
        pnc_identifier.setValue("8")
        mapping.setPncIdentifier(pnc_identifier)
        mapping.addPncPdurGroupRef(_ref("/Groups/PdurGroup1", "PDUR-I-PDU-GROUP"))
        wakeup = Boolean()
        wakeup.setValue(True)
        mapping.setPncWakeupEnable(wakeup)
        mapping.addRelevantForDynamicPncMappingRef(_ref("/Ecu/Gateway1", "ECU-INSTANCE"))
        short_label = Identifier()
        short_label.setValue("PNC_1")
        mapping.setShortLabel(short_label)
        iref = PortGroupInSystemInstanceRef()
        iref.setBaseRef(_ref("/System/PortGroup1", "PORT-GROUP"))
        mapping.addVfcIRef(iref)
        mapping.addWakeupFrameRef(_ref("/Frames/Frame1", "CAN-FRAME-TRIGGERING"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writePncMapping(parent, mapping)

        node = parent.find("PNC-MAPPING")
        children = [child.tag for child in node]
        assert children == [
            "DYNAMIC-PNC-MAPPING-PDU-GROUP-REFS",
            "IDENT",
            "PHYSICAL-CHANNEL-REFS",
            "PNC-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS",
            "PNC-GROUP-REFS",
            "PNC-IDENTIFIER",
            "PNC-PDUR-GROUP-REFS",
            "PNC-WAKEUP-ENABLE",
            "RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REFS",
            "SHORT-LABEL",
            "VFC-IREFS",
            "WAKEUP-FRAME-REFS",
        ]
        assert node.find("IDENT/SHORT-NAME").text == "PncIdent1"
        assert node.find("PNC-IDENTIFIER").text == "8"
        assert node.find("PNC-WAKEUP-ENABLE").text == "true"
        assert (
            node.find("PNC-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS/CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL/CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF").text
            == "/ServiceInstances/Group1"
        )
        assert node.find("VFC-IREFS/VFC-IREF/BASE-REF").text == "/System/PortGroup1"

    def test_round_trip_full(self):
        mapping = PncMapping()
        mapping.addDynamicPncMappingPduGroupRef(_ref("/Groups/DynGroup1", "I-SIGNAL-I-PDU-GROUP"))
        mapping.createIdent("PncIdent1")
        mapping.addPhysicalChannelRef(_ref("/Topology/Can1", "CAN-PHYSICAL-CHANNEL"))
        mapping.addPncGroupRef(_ref("/Groups/PncGroup1", "I-SIGNAL-I-PDU-GROUP"))
        pnc_identifier = PositiveInteger()
        pnc_identifier.setValue("8")
        mapping.setPncIdentifier(pnc_identifier)
        wakeup = Boolean()
        wakeup.setValue(True)
        mapping.setPncWakeupEnable(wakeup)
        short_label = Identifier()
        short_label.setValue("PNC_1")
        mapping.setShortLabel(short_label)
        iref = PortGroupInSystemInstanceRef()
        iref.setBaseRef(_ref("/System/PortGroup1", "PORT-GROUP"))
        mapping.addVfcIRef(iref)
        mapping.addWakeupFrameRef(_ref("/Frames/Frame1", "CAN-FRAME-TRIGGERING"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writePncMapping(parent, mapping)

        reloaded = PncMapping()
        ARXMLParser().readPncMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getDynamicPncMappingPduGroupRefs()[0].getValue() == "/Groups/DynGroup1"
        assert reloaded.getIdent().getShortName() == "PncIdent1"
        assert reloaded.getPhysicalChannelRefs()[0].getValue() == "/Topology/Can1"
        assert reloaded.getPncGroupRefs()[0].getValue() == "/Groups/PncGroup1"
        assert reloaded.getPncIdentifier().getValue() == 8
        assert reloaded.getPncWakeupEnable().getValue() is True
        assert reloaded.getShortLabel().getValue() == "PNC_1"
        assert reloaded.getVfcIRefs()[0].getBaseRef().getValue() == "/System/PortGroup1"
        assert reloaded.getWakeupFrameRefs()[0].getValue() == "/Frames/Frame1"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = PncMapping()
        short_label = Identifier()
        short_label.setValue("PNC_3")
        mapping.setShortLabel(short_label)
        system_mapping.addPncMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingPncMappings(parent, system_mapping)

        wrapper = parent.find("PNC-MAPPINGS")
        assert wrapper is not None
        assert wrapper.find("PNC-MAPPING") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingPncMappings(_with_ns(parent), reloaded_mapping)
        pnc_mappings = reloaded_mapping.getPncMappings()
        assert len(pnc_mappings) == 1
        assert pnc_mappings[0].getShortLabel().getValue() == "PNC_3"

    def test_empty_aggregation_no_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingPncMappings(parent, system_mapping)

        assert parent.find("PNC-MAPPINGS") is None
