"""Writer/reader round-trip tests for PortElementToCommunicationResourceMapping (Table 11.15, p.905)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PortElementToCommunicationResourceMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ModeDeclarationGroupPrototypeInSystemInstanceRef,
    OperationInSystemInstanceRef,
    ParameterDataPrototypeInSystemInstanceRef,
    TriggerInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterMappingSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_mapping(short_name: str = "mapping1") -> PortElementToCommunicationResourceMapping:
    mapping = PortElementToCommunicationResourceMapping(None, short_name)

    op_iref = OperationInSystemInstanceRef()
    op_iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    op_iref.addContextComponentRef(_ref("/Root/SwcA", "SW-COMPONENT-PROTOTYPE"))
    op_iref.setContextPortRef(_ref("/Root/SwcA/rp1", "R-PORT-PROTOTYPE"))
    op_iref.setTargetOperationRef(_ref("/Root/SwcA/rp1/op1", "CLIENT-SERVER-OPERATION"))
    mapping.setClientServerOperationIRef(op_iref)

    mapping.setCommunicationResourceRef(_ref("/Resources/MyResource", "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"))

    mode_iref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
    mode_iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    mode_iref.addContextComponentRef(_ref("/Root/SwcB", "SW-COMPONENT-PROTOTYPE"))
    mode_iref.setContextPortRef(_ref("/Root/SwcB/pp1", "P-PORT-PROTOTYPE"))
    mode_iref.setTargetModeDeclarationGroupPrototypeRef(_ref("/Root/SwcB/pp1/mg1", "MODE-DECLARATION-GROUP-PROTOTYPE"))
    mapping.setModeDeclarationGroupPrototypeIRef(mode_iref)

    prm_iref = ParameterDataPrototypeInSystemInstanceRef()
    prm_iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    prm_iref.addContextComponentRef(_ref("/Root/SwcC", "SW-COMPONENT-PROTOTYPE"))
    prm_iref.setContextPortRef(_ref("/Root/SwcC/rp2", "R-PORT-PROTOTYPE"))
    prm_iref.setTargetParameterDataPrototypeRef(_ref("/Root/SwcC/rp2/prm1", "PARAMETER-DATA-PROTOTYPE"))
    mapping.setParameterDataPrototypeIRef(prm_iref)

    trg_iref = TriggerInSystemInstanceRef()
    trg_iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    trg_iref.addContextComponentRef(_ref("/Root/SwcD", "SW-COMPONENT-PROTOTYPE"))
    trg_iref.setContextPortRef(_ref("/Root/SwcD/pp2", "P-PORT-PROTOTYPE"))
    trg_iref.setTargetTriggerRef(_ref("/Root/SwcD/pp2/trg1", "TRIGGER"))
    mapping.setTriggerIRef(trg_iref)

    var_iref = VariableDataPrototypeInSystemInstanceRef()
    var_iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    var_iref.addContextComponentRef(_ref("/Root/SwcE", "SW-COMPONENT-PROTOTYPE"))
    var_iref.setContextPortRef(_ref("/Root/SwcE/pp3", "P-PORT-PROTOTYPE"))
    var_iref.setTargetDataPrototypeRef(_ref("/Root/SwcE/pp3/var1", "VARIABLE-DATA-PROTOTYPE"))
    mapping.setVariableDataPrototypeIRef(var_iref)

    return mapping


def _assert_all_fields(mapping: PortElementToCommunicationResourceMapping):
    op_iref = mapping.getClientServerOperationIRef()
    assert op_iref is not None
    assert op_iref.getContextCompositionRef().getValue() == "/Root"
    assert [ref.getValue() for ref in op_iref.getContextComponentRefs()] == ["/Root/SwcA"]
    assert op_iref.getContextPortRef().getValue() == "/Root/SwcA/rp1"
    assert op_iref.getTargetOperationRef().getValue() == "/Root/SwcA/rp1/op1"

    assert mapping.getCommunicationResourceRef().getValue() == "/Resources/MyResource"
    assert mapping.getCommunicationResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"

    mode_iref = mapping.getModeDeclarationGroupPrototypeIRef()
    assert mode_iref is not None
    assert mode_iref.getTargetModeDeclarationGroupPrototypeRef().getValue() == "/Root/SwcB/pp1/mg1"

    prm_iref = mapping.getParameterDataPrototypeIRef()
    assert prm_iref is not None
    assert prm_iref.getTargetParameterDataPrototypeRef().getValue() == "/Root/SwcC/rp2/prm1"

    trg_iref = mapping.getTriggerIRef()
    assert trg_iref is not None
    assert trg_iref.getTargetTriggerRef().getValue() == "/Root/SwcD/pp2/trg1"

    var_iref = mapping.getVariableDataPrototypeIRef()
    assert var_iref is not None
    assert var_iref.getTargetDataPrototypeRef().getValue() == "/Root/SwcE/pp3/var1"


class TestWritePortElementToCommunicationResourceMapping:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: the SHORT-NAME first via the
        Identifiable base group, then the six Table 11.15 rows in the XSD group order
        (AUTOSAR_00052.xsd l.92033).
        """
        element = ET.Element("PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING")
        writer.writePortElementToCommunicationResourceMapping(element, _new_mapping())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[1:] == [
            "CLIENT-SERVER-OPERATION-IREF",
            "COMMUNICATION-RESOURCE-REF",
            "MODE-DECLARATION-GROUP-PROTOTYPE-IREF",
            "PARAMETER-DATA-PROTOTYPE-IREF",
            "TRIGGER-IREF",
            "VARIABLE-DATA-PROTOTYPE-IREF",
        ]
        assert element.find("COMMUNICATION-RESOURCE-REF").text == "/Resources/MyResource"
        assert element.find("COMMUNICATION-RESOURCE-REF").attrib["DEST"] == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"
        assert element.find("CLIENT-SERVER-OPERATION-IREF/TARGET-OPERATION-REF").text == "/Root/SwcA/rp1/op1"
        assert element.find("MODE-DECLARATION-GROUP-PROTOTYPE-IREF/TARGET-MODE-DECLARATION-GROUP-PROTOTYPE-REF").text == "/Root/SwcB/pp1/mg1"
        assert element.find("PARAMETER-DATA-PROTOTYPE-IREF/TARGET-PARAMETER-DATA-PROTOTYPE-REF").text == "/Root/SwcC/rp2/prm1"
        assert element.find("TRIGGER-IREF/TARGET-TRIGGER-REF").text == "/Root/SwcD/pp2/trg1"
        assert element.find("VARIABLE-DATA-PROTOTYPE-IREF/TARGET-DATA-PROTOTYPE-REF").text == "/Root/SwcE/pp3/var1"

    def test_write_empty_element(self, writer):
        """
        A mapping without members emits no reference/instance-ref elements.
        """
        element = ET.Element("PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING")
        writer.writePortElementToCommunicationResourceMapping(element, PortElementToCommunicationResourceMapping(None, "mapping2"))

        tags = [child.tag for child in element]
        assert tags == ["SHORT-NAME"]


class TestPortElementToCommunicationResourceMappingRoundTrip:
    def test_round_trip_via_cp_software_cluster_mapping_set(self, writer, parser):
        """
        Write -> serialize -> re-parse through the CpSoftwareClusterMappingSet parent
        dispatch keeps every field value.
        """
        mapping_set = CpSoftwareClusterMappingSet(None, "mapping_set")
        mapping_set.createPortElementToComResourceMapping("port_mapping")
        mapping = mapping_set.getPortElementToComResourceMappings()[0]
        populated = _new_mapping("port_mapping")
        mapping.setClientServerOperationIRef(populated.getClientServerOperationIRef())
        mapping.setCommunicationResourceRef(populated.getCommunicationResourceRef())
        mapping.setModeDeclarationGroupPrototypeIRef(populated.getModeDeclarationGroupPrototypeIRef())
        mapping.setParameterDataPrototypeIRef(populated.getParameterDataPrototypeIRef())
        mapping.setTriggerIRef(populated.getTriggerIRef())
        mapping.setVariableDataPrototypeIRef(populated.getVariableDataPrototypeIRef())

        parent = ET.Element("PARENT")
        writer.writeCpSoftwareClusterMappingSet(parent, mapping_set)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = CpSoftwareClusterMappingSet(None, "mapping_set")
        parser.readCpSoftwareClusterMappingSet(root[0], reloaded)

        port_mappings = reloaded.getPortElementToComResourceMappings()
        assert len(port_mappings) == 1
        assert port_mappings[0].getShortName() == "port_mapping"
        _assert_all_fields(port_mappings[0])

    def test_round_trip_via_system_mapping(self, writer, parser):
        """
        Write -> serialize -> re-parse through the SystemMapping parent dispatch keeps
        every field value.
        """
        mapping = SystemMapping(AUTOSAR.getInstance(), "mapping")
        mapping.createPortElementToComResourceMapping("port_mapping")
        populated = _new_mapping("port_mapping")
        stored = mapping.getPortElementToComResourceMappings()[0]
        stored.setClientServerOperationIRef(populated.getClientServerOperationIRef())
        stored.setCommunicationResourceRef(populated.getCommunicationResourceRef())
        stored.setModeDeclarationGroupPrototypeIRef(populated.getModeDeclarationGroupPrototypeIRef())
        stored.setParameterDataPrototypeIRef(populated.getParameterDataPrototypeIRef())
        stored.setTriggerIRef(populated.getTriggerIRef())
        stored.setVariableDataPrototypeIRef(populated.getVariableDataPrototypeIRef())

        parent = ET.Element("PARENT")
        writer.writeSystemMapping(parent, mapping)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = SystemMapping(AUTOSAR.getInstance(), "mapping")
        parser.readSystemMapping(root[0], reloaded)

        port_mappings = reloaded.getPortElementToComResourceMappings()
        assert len(port_mappings) == 1
        assert port_mappings[0].getShortName() == "port_mapping"
        _assert_all_fields(port_mappings[0])

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: a mapping set without port element mappings emits no
        PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS wrapper, and a mapping without members
        re-parses to unset fields.
        """
        mapping_set = CpSoftwareClusterMappingSet(None, "mapping_set")
        parent = ET.Element("PARENT")
        writer.writeCpSoftwareClusterMappingSet(parent, mapping_set)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = CpSoftwareClusterMappingSet(None, "mapping_set")
        parser.readCpSoftwareClusterMappingSet(root[0], reloaded)
        assert reloaded.getPortElementToComResourceMappings() == []

        element = ET.Element("PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING")
        writer.writePortElementToCommunicationResourceMapping(element, PortElementToCommunicationResourceMapping(None, "mapping2"))
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        mapping = parser.readPortElementToCommunicationResourceMapping(parsed_element, PortElementToCommunicationResourceMapping(None, "mapping2"))
        assert mapping.getClientServerOperationIRef() is None
        assert mapping.getCommunicationResourceRef() is None
        assert mapping.getModeDeclarationGroupPrototypeIRef() is None
        assert mapping.getParameterDataPrototypeIRef() is None
        assert mapping.getTriggerIRef() is None
        assert mapping.getVariableDataPrototypeIRef() is None
