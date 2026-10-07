"""Writer round-trip tests for RteEventInSystemSeparation (Table 5.21, p.214).

Serialized through the RTE-EVENT-IN-SYSTEM-SEPARATION element and the
RTE-EVENT-SEPARATIONS wrapper of SystemMapping
(XSD group RTE-EVENT-IN-SYSTEM-SEPARATION, AUTOSAR_00052.xsd l.100676:
RTE-EVENT-IREFS wrapper emitted only when non-empty).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInSystemSeparation
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


class TestWriteRteEventInSystemSeparation:
    def test_empty_no_wrapper(self):
        separation = RteEventInSystemSeparation(MockParent(), "Sep")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInSystemSeparation(parent, separation)

        node = parent.find("RTE-EVENT-IN-SYSTEM-SEPARATION")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Sep"
        assert node.find("RTE-EVENT-IREFS") is None

    def test_full(self):
        separation = RteEventInSystemSeparation(MockParent(), "Sep")
        iref1 = RteEventInSystemInstanceRef()
        iref1.setTargetRteEventRef(_ref("/Root/SwcA/Ev1", "RTE-EVENT"))
        iref2 = RteEventInSystemInstanceRef()
        iref2.setTargetRteEventRef(_ref("/Root/SwcB/Ev2", "RTE-EVENT"))
        separation.addRteEventIRef(iref1)
        separation.addRteEventIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInSystemSeparation(parent, separation)

        node = parent.find("RTE-EVENT-IN-SYSTEM-SEPARATION")
        wrapper = node.find("RTE-EVENT-IREFS")
        assert wrapper is not None
        items = wrapper.findall("RTE-EVENT-IREF")
        assert len(items) == 2
        assert items[0].find("TARGET-RTE-EVENT-REF").text == "/Root/SwcA/Ev1"
        assert items[1].find("TARGET-RTE-EVENT-REF").text == "/Root/SwcB/Ev2"

    def test_round_trip_full(self):
        separation = RteEventInSystemSeparation(MockParent(), "Sep")
        iref1 = RteEventInSystemInstanceRef()
        iref1.setContextRootCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref1.setTargetRteEventRef(_ref("/Root/SwcA/Ev1", "RTE-EVENT"))
        iref2 = RteEventInSystemInstanceRef()
        iref2.setTargetRteEventRef(_ref("/Root/SwcB/Ev2", "RTE-EVENT"))
        separation.addRteEventIRef(iref1)
        separation.addRteEventIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInSystemSeparation(parent, separation)

        reloaded = RteEventInSystemSeparation(MockParent(), "Sep")
        ARXMLParser().readRteEventInSystemSeparation(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Sep"
        irefs = reloaded.getRteEventIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextRootCompositionRef().getValue() == "/Root"
        assert irefs[0].getTargetRteEventRef().getValue() == "/Root/SwcA/Ev1"
        assert irefs[0].getTargetRteEventRef().getDest() == "RTE-EVENT"
        assert irefs[1].getTargetRteEventRef().getValue() == "/Root/SwcB/Ev2"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        separation = RteEventInSystemSeparation(system_mapping, "Sep1")
        iref = RteEventInSystemInstanceRef()
        iref.setTargetRteEventRef(_ref("/Root/SwcA/Ev1", "RTE-EVENT"))
        separation.addRteEventIRef(iref)
        system_mapping.addRteEventSeparation(separation)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingRteEventSeparations(parent, system_mapping)

        wrapper = parent.find("RTE-EVENT-SEPARATIONS")
        assert wrapper is not None
        assert len(wrapper.findall("RTE-EVENT-IN-SYSTEM-SEPARATION")) == 1

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingRteEventSeparations(_with_ns(parent), reloaded_mapping)
        separations = reloaded_mapping.getRteEventSeparations()
        assert len(separations) == 1
        assert separations[0].getShortName() == "Sep1"
        assert separations[0].getRteEventIRefs()[0].getTargetRteEventRef().getValue() == "/Root/SwcA/Ev1"

    def test_empty_aggregation_no_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingRteEventSeparations(parent, system_mapping)

        assert parent.find("RTE-EVENT-SEPARATIONS") is None
