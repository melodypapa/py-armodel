"""Writer round-trip tests for RteEventInCompositionSeparation (Table 5.19, p.212).

Serialized through the RTE-EVENT-IN-COMPOSITION-SEPARATION element
(XSD group RTE-EVENT-IN-COMPOSITION-SEPARATION, AUTOSAR_00052.xsd l.100465:
RTE-EVENT-IREFS wrapper emitted only when non-empty). The aggregator
SwComponentMappingConstraints is not yet implemented, so the element-level
writer is exercised directly.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInCompositionSeparation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteRteEventInCompositionSeparation:
    def test_empty_no_wrapper(self):
        separation = RteEventInCompositionSeparation(MockParent(), "Sep")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInCompositionSeparation(parent, separation)

        node = parent.find("RTE-EVENT-IN-COMPOSITION-SEPARATION")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Sep"
        assert node.find("RTE-EVENT-IREFS") is None

    def test_full(self):
        separation = RteEventInCompositionSeparation(MockParent(), "Sep")
        iref1 = RteEventInCompositionInstanceRef()
        iref1.addContextSwComponentRef(_ref("/Comps/SwcA", "SW-COMPONENT-PROTOTYPE"))
        iref1.setTargetRteEventRef(_ref("/Comps/SwcA/Ev1", "RTE-EVENT"))
        iref2 = RteEventInCompositionInstanceRef()
        iref2.setTargetRteEventRef(_ref("/Comps/SwcB/Ev2", "RTE-EVENT"))
        separation.addRteEventIRef(iref1)
        separation.addRteEventIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInCompositionSeparation(parent, separation)

        node = parent.find("RTE-EVENT-IN-COMPOSITION-SEPARATION")
        wrapper = node.find("RTE-EVENT-IREFS")
        assert wrapper is not None
        items = wrapper.findall("RTE-EVENT-IREF")
        assert len(items) == 2
        assert items[0].find("TARGET-RTE-EVENT-REF").text == "/Comps/SwcA/Ev1"
        assert items[1].find("TARGET-RTE-EVENT-REF").text == "/Comps/SwcB/Ev2"

    def test_round_trip_full(self):
        separation = RteEventInCompositionSeparation(MockParent(), "Sep")
        iref1 = RteEventInCompositionInstanceRef()
        iref1.addContextSwComponentRef(_ref("/Comps/SwcA", "SW-COMPONENT-PROTOTYPE"))
        iref1.setTargetRteEventRef(_ref("/Comps/SwcA/Ev1", "RTE-EVENT"))
        iref2 = RteEventInCompositionInstanceRef()
        iref2.setTargetRteEventRef(_ref("/Comps/SwcB/Ev2", "RTE-EVENT"))
        separation.addRteEventIRef(iref1)
        separation.addRteEventIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInCompositionSeparation(parent, separation)

        reloaded = RteEventInCompositionSeparation(MockParent(), "Sep")
        ARXMLParser().readRteEventInCompositionSeparation(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Sep"
        irefs = reloaded.getRteEventIRefs()
        assert len(irefs) == 2
        assert irefs[0].getTargetRteEventRef().getValue() == "/Comps/SwcA/Ev1"
        assert irefs[0].getTargetRteEventRef().getDest() == "RTE-EVENT"
        assert irefs[0].getContextSwComponentRefs()[0].getValue() == "/Comps/SwcA"
        assert irefs[1].getTargetRteEventRef().getValue() == "/Comps/SwcB/Ev2"
