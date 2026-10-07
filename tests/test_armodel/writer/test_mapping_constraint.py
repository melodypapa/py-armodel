"""Writer round-trip tests for MappingConstraint (Table 5.8, p.202) and ComponentClustering (Table 5.9, p.203).

Serialized through the MAPPING-CONSTRAINTS wrapper of SystemMapping; child
element order = XSD group MAPPING-CONSTRAINT sequence (AUTOSAR_00052.xsd
l.79829): INTRODUCTION, VARIATION-POINT (last, sequenceOffset=10000).
ComponentClustering own children follow the XSD group COMPONENT-CLUSTERING
sequence (AUTOSAR_00052.xsd l.20609): CLUSTERED-COMPONENT-IREFS,
MAPPING-SCOPE — emitted after the abstract MAPPING-CONSTRAINT group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ComponentClustering, ComponentSeparation, MappingScopeEnum
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _introduction(text: str) -> DocumentationBlock:
    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setValue(text)
    paragraph.addL1(l1)
    block.addP(paragraph)
    return block


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _mapping_scope(value: str) -> MappingScopeEnum:
    scope = MappingScopeEnum()
    scope.setValue(value)
    return scope


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteMappingConstraint:
    def test_round_trip_via_system_mapping(self):
        """Test write -> re-parse round trip with introduction field values and XSD element order"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        clustering = ComponentClustering()
        clustering.setIntroduction(_introduction("The clustering introduction."))
        mapping.addMappingConstraint(clustering)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        assert node is not None
        wrappers = node.find("MAPPING-CONSTRAINTS")
        assert wrappers is not None
        children = list(wrappers)
        assert len(children) == 1
        clustering_node = children[0]
        assert clustering_node.tag == "COMPONENT-CLUSTERING"
        assert [child.tag for child in clustering_node] == ["INTRODUCTION"]
        assert clustering_node.find("INTRODUCTION/P/L-1").text == "The clustering introduction."

        reloaded = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        ARXMLParser().readSystemMapping(_with_ns(parent)[0], reloaded)

        constraints = reloaded.getMappingConstraints()
        assert len(constraints) == 1
        round_tripped = constraints[0]
        assert isinstance(round_tripped, ComponentClustering)
        assert round_tripped.getIntroduction().getPs()[0].getL1s()[0].getValue() == "The clustering introduction."

    def test_variation_point_emitted_after_introduction(self):
        """Test that VARIATION-POINT is emitted after INTRODUCTION (XSD sequenceOffset=10000)"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        separation = ComponentSeparation()
        separation.setIntroduction(_introduction("The separation introduction."))
        separation.setVariationPoint(VariationPoint())
        mapping.addMappingConstraint(separation)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        separation_node = parent.find("SYSTEM-MAPPING/MAPPING-CONSTRAINTS/COMPONENT-SEPARATION")
        assert separation_node is not None
        assert [child.tag for child in separation_node] == ["INTRODUCTION", "VARIATION-POINT"]

        reloaded = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        ARXMLParser().readSystemMapping(_with_ns(parent)[0], reloaded)

        round_tripped = reloaded.getMappingConstraints()[0]
        assert isinstance(round_tripped, ComponentSeparation)
        assert round_tripped.getVariationPoint() is not None
        assert round_tripped.getIntroduction().getPs()[0].getL1s()[0].getValue() == "The separation introduction."

    def test_empty_wrapper_not_emitted(self):
        """Test that a childless SystemMapping emits no MAPPING-CONSTRAINTS wrapper"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        assert node is not None
        assert node.find("MAPPING-CONSTRAINTS") is None

    def test_fields_absent_not_emitted(self):
        """Test that unset optional fields emit no elements on a populated constraint"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        mapping.addMappingConstraint(ComponentClustering())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        clustering_node = parent.find("SYSTEM-MAPPING/MAPPING-CONSTRAINTS/COMPONENT-CLUSTERING")
        assert clustering_node is not None
        assert len(list(clustering_node)) == 0


class TestWriteComponentClustering:
    def _clustered_component_iref(self, context: str, target: str) -> ComponentInSystemInstanceRef:
        iref = ComponentInSystemInstanceRef()
        if context is not None:
            iref.setContextCompositionRef(_ref(context, "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.setTargetComponentRef(_ref(target, "SW-COMPONENT-PROTOTYPE"))
        return iref

    def test_round_trip_full_element_order(self):
        """Test write -> re-parse round trip with field values and the XSD element order INTRODUCTION, CLUSTERED-COMPONENT-IREFS, MAPPING-SCOPE"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        clustering = ComponentClustering()
        clustering.setIntroduction(_introduction("The clustering introduction."))
        clustering.addClusteredComponentIRef(self._clustered_component_iref("/CanSystem/TopLevelComposition", "/DemoApplication/SWC_ModifyEcho"))
        clustering.addClusteredComponentIRef(self._clustered_component_iref(None, "/DemoApplication/SWC_CyclicCounter"))
        clustering.setMappingScope(_mapping_scope(MappingScopeEnum.MAPPING_SCOPE_ECU))
        mapping.addMappingConstraint(clustering)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        clustering_node = parent.find("SYSTEM-MAPPING/MAPPING-CONSTRAINTS/COMPONENT-CLUSTERING")
        assert clustering_node is not None
        assert [child.tag for child in clustering_node] == ["INTRODUCTION", "CLUSTERED-COMPONENT-IREFS", "MAPPING-SCOPE"]
        assert clustering_node.find("INTRODUCTION/P/L-1").text == "The clustering introduction."
        iref_nodes = clustering_node.findall("CLUSTERED-COMPONENT-IREFS/CLUSTERED-COMPONENT-IREF")
        assert len(iref_nodes) == 2
        assert iref_nodes[0].find("CONTEXT-COMPOSITION-REF").text == "/CanSystem/TopLevelComposition"
        assert iref_nodes[0].find("CONTEXT-COMPOSITION-REF").get("DEST") == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert iref_nodes[0].find("TARGET-COMPONENT-REF").text == "/DemoApplication/SWC_ModifyEcho"
        assert iref_nodes[1].find("TARGET-COMPONENT-REF").text == "/DemoApplication/SWC_CyclicCounter"
        assert iref_nodes[1].find("CONTEXT-COMPOSITION-REF") is None
        assert clustering_node.find("MAPPING-SCOPE").text == "MAPPING-SCOPE-ECU"

        reloaded = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        ARXMLParser().readSystemMapping(_with_ns(parent)[0], reloaded)

        constraints = reloaded.getMappingConstraints()
        assert len(constraints) == 1
        round_tripped = constraints[0]
        assert isinstance(round_tripped, ComponentClustering)
        assert round_tripped.getIntroduction().getPs()[0].getL1s()[0].getValue() == "The clustering introduction."
        irefs = round_tripped.getClusteredComponentIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/CanSystem/TopLevelComposition"
        assert irefs[0].getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert irefs[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"
        assert irefs[1].getTargetComponentRef().getValue() == "/DemoApplication/SWC_CyclicCounter"
        assert irefs[1].getContextCompositionRef() is None
        assert round_tripped.getMappingScope() is not None
        assert round_tripped.getMappingScope().getValue() == "MAPPING-SCOPE-ECU"

    def test_empty_clustered_component_irefs_wrapper_not_emitted(self):
        """Test that an empty iref list emits no CLUSTERED-COMPONENT-IREFS wrapper while the mappingScope survives the round trip"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        clustering = ComponentClustering()
        clustering.setMappingScope(_mapping_scope(MappingScopeEnum.MAPPING_SCOPE_PARTITION))
        mapping.addMappingConstraint(clustering)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        clustering_node = parent.find("SYSTEM-MAPPING/MAPPING-CONSTRAINTS/COMPONENT-CLUSTERING")
        assert clustering_node is not None
        assert clustering_node.find("CLUSTERED-COMPONENT-IREFS") is None
        assert clustering_node.find("MAPPING-SCOPE").text == "MAPPING-SCOPE-PARTITION"

        reloaded = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        ARXMLParser().readSystemMapping(_with_ns(parent)[0], reloaded)

        round_tripped = reloaded.getMappingConstraints()[0]
        assert isinstance(round_tripped, ComponentClustering)
        assert round_tripped.getClusteredComponentIRefs() == []
        assert round_tripped.getMappingScope().getValue() == "MAPPING-SCOPE-PARTITION"
