"""Parser tests for the EOC executable entity refs (EOC-EXECUTABLE-ENTITY-REF, EOC-EXECUTABLE-ENTITY-REF-GROUP, EOC-EVENT-REF)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCEventRef,
    EOCExecutableEntityRef,
    EOCExecutableEntityRefGroup,
    ExecutionOrderConstraint,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent():
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


class TestReadEOCExecutableEntityRefs:
    def test_read_eoc_executable_entity_ref_full(self, parser):
        parent = _parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")
        element = ET.fromstring(
            f"<EOC-EXECUTABLE-ENTITY-REF xmlns='{NS}'>"
            "<SHORT-NAME>Entity1</SHORT-NAME>"
            "<DIRECT-SUCCESSOR-REFS>"
            "<DIRECT-SUCCESSOR-REF DEST='EOC-EXECUTABLE-ENTITY-REF-GROUP'>/AUTOSAR/Group1</DIRECT-SUCCESSOR-REF>"
            "</DIRECT-SUCCESSOR-REFS>"
            "<BSW-MODULE-INSTANCE-REF DEST='BSW-IMPLEMENTATION'>/AUTOSAR/BswImpl</BSW-MODULE-INSTANCE-REF>"
            "<COMPONENT-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/AUTOSAR/Composition/ProtoCtx</CONTEXT-COMPONENT-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/AUTOSAR/SwcProto</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>"
            "<EXECUTABLE-REF DEST='RUNNABLE-ENTITY'>/AUTOSAR/Runnable</EXECUTABLE-REF>"
            "<SUCCESSOR-REFS>"
            "<SUCCESSOR-REF DEST='EOC-EXECUTABLE-ENTITY-REF'>/AUTOSAR/Entity2</SUCCESSOR-REF>"
            "</SUCCESSOR-REFS>"
            "</EOC-EXECUTABLE-ENTITY-REF>"
        )
        parser.readEOCExecutableEntityRef(element, entity_ref)
        assert entity_ref.getShortName() == "Entity1"
        direct_successors = entity_ref.getDirectSuccessorRefs()
        assert len(direct_successors) == 1
        assert direct_successors[0].getValue() == "/AUTOSAR/Group1"
        assert direct_successors[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF-GROUP"
        assert entity_ref.getBswModuleInstanceRef().getValue() == "/AUTOSAR/BswImpl"
        assert entity_ref.getBswModuleInstanceRef().getDest() == "BSW-IMPLEMENTATION"
        component_iref = entity_ref.getComponentIRef()
        assert component_iref.getContextComponentRefs()[0].getValue() == "/AUTOSAR/Composition/ProtoCtx"
        assert component_iref.getTargetComponentRef().getValue() == "/AUTOSAR/SwcProto"
        assert component_iref.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert entity_ref.getExecutableRef().getValue() == "/AUTOSAR/Runnable"
        successors = entity_ref.getSuccessorRefs()
        assert len(successors) == 1
        assert successors[0].getValue() == "/AUTOSAR/Entity2"

    def test_read_eoc_executable_entity_ref_group_full(self, parser):
        parent = _parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")
        element = ET.fromstring(
            f"<EOC-EXECUTABLE-ENTITY-REF-GROUP xmlns='{NS}'>"
            "<SHORT-NAME>Group1</SHORT-NAME>"
            "<LET-DATA-EXCHANGE-PARADIGM>INTRA-LET-EOC</LET-DATA-EXCHANGE-PARADIGM>"
            "<LET-INTERVAL-REFS>"
            "<LET-INTERVAL-REF DEST='TIMING-DESCRIPTION-EVENT-CHAIN'>/AUTOSAR/LetChain</LET-INTERVAL-REF>"
            "</LET-INTERVAL-REFS>"
            "<MAX-CYCLE-REPETITIONS>4</MAX-CYCLE-REPETITIONS>"
            "<MAX-CYCLES>12</MAX-CYCLES>"
            "<MAX-SLOTS>3</MAX-SLOTS>"
            "<MAX-SLOTS-PER-CYCLE>2</MAX-SLOTS-PER-CYCLE>"
            "<NESTED-ELEMENT-REFS>"
            "<NESTED-ELEMENT-REF DEST='EOC-EXECUTABLE-ENTITY-REF'>/AUTOSAR/Entity1</NESTED-ELEMENT-REF>"
            "</NESTED-ELEMENT-REFS>"
            "<TRIGGERING-EVENT-REF DEST='TIMING-DESCRIPTION-EVENT'>/AUTOSAR/TimingEvent</TRIGGERING-EVENT-REF>"
            "</EOC-EXECUTABLE-ENTITY-REF-GROUP>"
        )
        parser.readEOCExecutableEntityRefGroup(element, group)
        assert group.getShortName() == "Group1"
        assert group.getLetDataExchangeParadigm().getValue() == "INTRA-LET-EOC"
        let_interval_refs = group.getLetIntervalRefs()
        assert len(let_interval_refs) == 1
        assert let_interval_refs[0].getValue() == "/AUTOSAR/LetChain"
        assert group.getMaxCycleRepetitions().getValue() == 4
        assert group.getMaxCycles().getValue() == 12
        assert group.getMaxSlots().getValue() == 3
        assert group.getMaxSlotsPerCycle().getValue() == 2
        nested_refs = group.getNestedElementRefs()
        assert len(nested_refs) == 1
        assert nested_refs[0].getValue() == "/AUTOSAR/Entity1"
        assert nested_refs[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF"
        assert group.getTriggeringEventRef().getValue() == "/AUTOSAR/TimingEvent"

    def test_read_eoc_event_ref_full(self, parser):
        parent = _parent()
        event_ref = EOCEventRef(parent, "EventRef1")
        element = ET.fromstring(
            f"<EOC-EVENT-REF xmlns='{NS}'>"
            "<SHORT-NAME>EventRef1</SHORT-NAME>"
            "<BSW-MODULE-INSTANCE-REF DEST='BSW-IMPLEMENTATION'>/AUTOSAR/BswImpl</BSW-MODULE-INSTANCE-REF>"
            "<COMPONENT-IREF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/AUTOSAR/SwcProto</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>"
            "<EVENT-REF DEST='RTE-EVENT'>/AUTOSAR/RteEvent</EVENT-REF>"
            "<SUCCESSOR-REFS>"
            "<SUCCESSOR-REF DEST='EOC-EVENT-REF'>/AUTOSAR/EventRef2</SUCCESSOR-REF>"
            "</SUCCESSOR-REFS>"
            "</EOC-EVENT-REF>"
        )
        parser.readEOCEventRef(element, event_ref)
        assert event_ref.getShortName() == "EventRef1"
        assert event_ref.getBswModuleInstanceRef().getValue() == "/AUTOSAR/BswImpl"
        assert event_ref.getComponentIRef().getTargetComponentRef().getValue() == "/AUTOSAR/SwcProto"
        assert event_ref.getEventRef().getValue() == "/AUTOSAR/RteEvent"
        assert event_ref.getEventRef().getDest() == "RTE-EVENT"
        successors = event_ref.getSuccessorRefs()
        assert len(successors) == 1
        assert successors[0].getValue() == "/AUTOSAR/EventRef2"

    def test_read_execution_order_constraint_ordered_element_dispatch(self, parser):
        parent = _parent()
        constraint = ExecutionOrderConstraint(parent, "Eoc")
        element = ET.fromstring(
            f"<EXECUTION-ORDER-CONSTRAINT xmlns='{NS}'>"
            "<ORDERED-ELEMENTS>"
            "<EOC-EXECUTABLE-ENTITY-REF>"
            "<SHORT-NAME>Entity1</SHORT-NAME>"
            "<EXECUTABLE-REF DEST='RUNNABLE-ENTITY'>/AUTOSAR/Runnable</EXECUTABLE-REF>"
            "</EOC-EXECUTABLE-ENTITY-REF>"
            "<EOC-EVENT-REF>"
            "<SHORT-NAME>EventRef1</SHORT-NAME>"
            "<EVENT-REF DEST='RTE-EVENT'>/AUTOSAR/RteEvent</EVENT-REF>"
            "</EOC-EVENT-REF>"
            "<EOC-EXECUTABLE-ENTITY-REF-GROUP>"
            "<SHORT-NAME>Group1</SHORT-NAME>"
            "<MAX-SLOTS-PER-CYCLE>5</MAX-SLOTS-PER-CYCLE>"
            "</EOC-EXECUTABLE-ENTITY-REF-GROUP>"
            "</ORDERED-ELEMENTS>"
            "</EXECUTION-ORDER-CONSTRAINT>"
        )
        parser.readExecutionOrderConstraintOrderedElement(element, constraint)

        elements = constraint.getOrderedElements()
        assert len(elements) == 3
        assert isinstance(elements[0], EOCExecutableEntityRef)
        assert elements[0].getShortName() == "Entity1"
        assert elements[0].getExecutableRef().getValue() == "/AUTOSAR/Runnable"
        assert isinstance(elements[1], EOCEventRef)
        assert elements[1].getShortName() == "EventRef1"
        assert elements[1].getEventRef().getValue() == "/AUTOSAR/RteEvent"
        assert isinstance(elements[2], EOCExecutableEntityRefGroup)
        assert elements[2].getShortName() == "Group1"
        assert elements[2].getMaxSlotsPerCycle().getValue() == 5
