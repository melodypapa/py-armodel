"""Reader tests for MappingConstraint (Table 5.8, p.202) and ComponentClustering (Table 5.9, p.203).

XML group MAPPING-CONSTRAINT (AUTOSAR_00052.xsd l.79829): INTRODUCTION
(DOCUMENTATION-BLOCK) + VARIATION-POINT (atpVariation via
SystemMapping.mappingConstraint). Abstract class — exercised through the
concrete choice members; the helper is reused by ComponentClustering and
ComponentSeparation. ComponentClustering own children (XSD group
COMPONENT-CLUSTERING, AUTOSAR_00052.xsd l.20609): CLUSTERED-COMPONENT-IREFS,
MAPPING-SCOPE — read after the abstract MAPPING-CONSTRAINT group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ComponentClustering, ComponentSeparation
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


class TestReadMappingConstraint:
    def test_read_introduction_via_system_mapping(self):
        """Test that the introduction field values survive the MAPPING-CONSTRAINTS dispatch"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<MAPPING-CONSTRAINTS>"
            "<COMPONENT-CLUSTERING S='7' T='2024-01-01T00:00:00Z'>"
            "<INTRODUCTION>"
            "<P><L-1>The clustering introduction.</L-1></P>"
            "</INTRODUCTION>"
            "</COMPONENT-CLUSTERING>"
            "</MAPPING-CONSTRAINTS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        constraints = mapping.getMappingConstraints()
        assert len(constraints) == 1
        clustering = constraints[0]
        assert isinstance(clustering, ComponentClustering)
        assert clustering.getChecksum().getValue() == "7"
        assert clustering.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

        introduction = clustering.getIntroduction()
        assert introduction is not None
        assert introduction.getPs()[0].getL1s()[0].getValue() == "The clustering introduction."

    def test_read_variation_point_via_system_mapping(self):
        """Test that the VARIATION-POINT anchor of the MAPPING-CONSTRAINT group is read"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<MAPPING-CONSTRAINTS>"
            "<COMPONENT-SEPARATION>"
            "<VARIATION-POINT/>"
            "</COMPONENT-SEPARATION>"
            "</MAPPING-CONSTRAINTS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        constraints = mapping.getMappingConstraints()
        assert len(constraints) == 1
        separation = constraints[0]
        assert isinstance(separation, ComponentSeparation)
        assert separation.getVariationPoint() is not None

    def test_read_empty_wrapper(self):
        """Test that an empty MAPPING-CONSTRAINTS wrapper leaves the list empty"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip("<SYSTEM-MAPPING>" "<SHORT-NAME>SystemMapping</SHORT-NAME>" "<MAPPING-CONSTRAINTS/>" "</SYSTEM-MAPPING>")
        ARXMLParser().readSystemMapping(root[0], mapping)

        assert mapping.getMappingConstraints() == []


class TestReadComponentClustering:
    def test_read_clustered_component_irefs_and_mapping_scope(self):
        """Test that the COMPONENT-CLUSTERING own children round-trip field values through the MAPPING-CONSTRAINTS dispatch"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<MAPPING-CONSTRAINTS>"
            "<COMPONENT-CLUSTERING>"
            "<INTRODUCTION>"
            "<P><L-1>The clustering introduction.</L-1></P>"
            "</INTRODUCTION>"
            "<CLUSTERED-COMPONENT-IREFS>"
            "<CLUSTERED-COMPONENT-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/CanSystem/TopLevelComposition</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/DemoApplication/SWC_ModifyEcho</TARGET-COMPONENT-REF>"
            "</CLUSTERED-COMPONENT-IREF>"
            "<CLUSTERED-COMPONENT-IREF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/DemoApplication/SWC_CyclicCounter</TARGET-COMPONENT-REF>"
            "</CLUSTERED-COMPONENT-IREF>"
            "</CLUSTERED-COMPONENT-IREFS>"
            "<MAPPING-SCOPE>MAPPING-SCOPE-CORE</MAPPING-SCOPE>"
            "</COMPONENT-CLUSTERING>"
            "</MAPPING-CONSTRAINTS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        constraints = mapping.getMappingConstraints()
        assert len(constraints) == 1
        clustering = constraints[0]
        assert isinstance(clustering, ComponentClustering)

        assert clustering.getIntroduction() is not None
        assert clustering.getIntroduction().getPs()[0].getL1s()[0].getValue() == "The clustering introduction."

        irefs = clustering.getClusteredComponentIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/CanSystem/TopLevelComposition"
        assert irefs[0].getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert irefs[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"
        assert irefs[0].getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert irefs[1].getTargetComponentRef().getValue() == "/DemoApplication/SWC_CyclicCounter"
        assert irefs[1].getContextCompositionRef() is None

        assert clustering.getMappingScope() is not None
        assert clustering.getMappingScope().getValue() == "MAPPING-SCOPE-CORE"

    def test_read_mapping_scope_only(self):
        """Test that a COMPONENT-CLUSTERING without the irefs wrapper reads the mappingScope alone"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<MAPPING-CONSTRAINTS>"
            "<COMPONENT-CLUSTERING>"
            "<MAPPING-SCOPE>MAPPING-SCOPE-ECU</MAPPING-SCOPE>"
            "</COMPONENT-CLUSTERING>"
            "</MAPPING-CONSTRAINTS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        constraints = mapping.getMappingConstraints()
        assert len(constraints) == 1
        clustering = constraints[0]
        assert isinstance(clustering, ComponentClustering)
        assert clustering.getClusteredComponentIRefs() == []
        assert clustering.getMappingScope() is not None
        assert clustering.getMappingScope().getValue() == "MAPPING-SCOPE-ECU"
        assert clustering.getIntroduction() is None

    def test_read_empty_clustered_component_irefs_wrapper(self):
        """Test that an empty CLUSTERED-COMPONENT-IREFS wrapper leaves the iref list empty"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<MAPPING-CONSTRAINTS>"
            "<COMPONENT-CLUSTERING>"
            "<CLUSTERED-COMPONENT-IREFS/>"
            "</COMPONENT-CLUSTERING>"
            "</MAPPING-CONSTRAINTS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        constraints = mapping.getMappingConstraints()
        assert len(constraints) == 1
        clustering = constraints[0]
        assert isinstance(clustering, ComponentClustering)
        assert clustering.getClusteredComponentIRefs() == []
        assert clustering.getMappingScope() is None
