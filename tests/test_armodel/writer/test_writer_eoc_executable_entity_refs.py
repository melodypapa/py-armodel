"""Writer tests for the EOC executable entity refs (EOC-EXECUTABLE-ENTITY-REF, EOC-EXECUTABLE-ENTITY-REF-GROUP, EOC-EVENT-REF)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCEventRef,
    EOCExecutableEntityRef,
    EOCExecutableEntityRefGroup,
    ExecutionOrderConstraint,
    LetDataExchangeParadigmEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    RefType,
)
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


class TestWriteEOCExecutableEntityRefs:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_round_trip_eoc_executable_entity_ref(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")
        entity_ref.addDirectSuccessorRef(RefType().setValue("/AUTOSAR/Group1").setDest("EOC-EXECUTABLE-ENTITY-REF-GROUP"))
        entity_ref.setBswModuleInstanceRef(RefType().setValue("/AUTOSAR/BswImpl").setDest("BSW-IMPLEMENTATION"))
        entity_ref.setComponentIRef(RefType().setValue("/AUTOSAR/SwcProto").setDest("SW-COMPONENT-PROTOTYPE"))
        entity_ref.setExecutableRef(RefType().setValue("/AUTOSAR/Runnable").setDest("RUNNABLE-ENTITY"))
        entity_ref.addSuccessorRef(RefType().setValue("/AUTOSAR/Entity2").setDest("EOC-EXECUTABLE-ENTITY-REF"))

        wrapper = ET.Element("ROOT")
        ARXMLWriter().writeEOCExecutableEntityRef(wrapper, entity_ref)
        element = wrapper[0]
        assert element.tag == "EOC-EXECUTABLE-ENTITY-REF"
        assert element.find("BSW-MODULE-INSTANCE-REF") is not None
        assert element.find("COMPONENT-IREF/TARGET-COMPONENT-REF") is not None
        assert element.find("EXECUTABLE-REF") is not None

        reloaded = EOCExecutableEntityRef(parent, "Entity1")
        ARXMLParser().readEOCExecutableEntityRef(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Entity1"
        direct_successors = reloaded.getDirectSuccessorRefs()
        assert len(direct_successors) == 1
        assert direct_successors[0].getValue() == "/AUTOSAR/Group1"
        assert direct_successors[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF-GROUP"
        assert reloaded.getBswModuleInstanceRef().getValue() == "/AUTOSAR/BswImpl"
        assert reloaded.getBswModuleInstanceRef().getDest() == "BSW-IMPLEMENTATION"
        assert reloaded.getComponentIRef().getValue() == "/AUTOSAR/SwcProto"
        assert reloaded.getComponentIRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert reloaded.getExecutableRef().getValue() == "/AUTOSAR/Runnable"
        assert reloaded.getExecutableRef().getDest() == "RUNNABLE-ENTITY"
        successors = reloaded.getSuccessorRefs()
        assert len(successors) == 1
        assert successors[0].getValue() == "/AUTOSAR/Entity2"
        assert successors[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF"

    def test_write_eoc_executable_entity_ref_empty_optionals(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")

        wrapper = ET.Element("ROOT")
        ARXMLWriter().writeEOCExecutableEntityRef(wrapper, entity_ref)
        element = wrapper[0]
        assert element.find("DIRECT-SUCCESSOR-REFS") is None
        assert element.find("BSW-MODULE-INSTANCE-REF") is None
        assert element.find("COMPONENT-IREF") is None
        assert element.find("EXECUTABLE-REF") is None
        assert element.find("SUCCESSOR-REFS") is None
        assert element.find("SHORT-NAME").text == "Entity1"

        reloaded = EOCExecutableEntityRef(parent, "Entity1")
        ARXMLParser().readEOCExecutableEntityRef(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Entity1"
        assert reloaded.getDirectSuccessorRefs() == []
        assert reloaded.getBswModuleInstanceRef() is None
        assert reloaded.getComponentIRef() is None
        assert reloaded.getExecutableRef() is None
        assert reloaded.getSuccessorRefs() == []

    def test_round_trip_eoc_executable_entity_ref_group(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")
        group.setLetDataExchangeParadigm(LetDataExchangeParadigmEnum().setValue(LetDataExchangeParadigmEnum.INTRA_LET_EOC))
        group.addLetIntervalRef(RefType().setValue("/AUTOSAR/LetChain").setDest("TIMING-DESCRIPTION-EVENT-CHAIN"))
        group.setMaxCycleRepetitions(PositiveInteger().setValue("4"))
        group.setMaxCycles(Integer().setValue("12"))
        group.setMaxSlots(Integer().setValue("3"))
        group.setMaxSlotsPerCycle(PositiveInteger().setValue("2"))
        group.addNestedElementRef(RefType().setValue("/AUTOSAR/Entity1").setDest("EOC-EXECUTABLE-ENTITY-REF"))
        group.addNestedElementRef(RefType().setValue("/AUTOSAR/Group2").setDest("EOC-EXECUTABLE-ENTITY-REF-GROUP"))
        group.addDirectSuccessorRef(RefType().setValue("/AUTOSAR/Entity3").setDest("EOC-EXECUTABLE-ENTITY-REF"))
        group.addSuccessorRef(RefType().setValue("/AUTOSAR/Entity4").setDest("EOC-EVENT-REF"))
        group.setTriggeringEventRef(RefType().setValue("/AUTOSAR/TimingEvent").setDest("TIMING-DESCRIPTION-EVENT"))

        wrapper = ET.Element("ROOT")
        ARXMLWriter().writeEOCExecutableEntityRefGroup(wrapper, group)
        element = wrapper[0]
        assert element.tag == "EOC-EXECUTABLE-ENTITY-REF-GROUP"
        assert element.find("LET-DATA-EXCHANGE-PARADIGM") is not None

        reloaded = EOCExecutableEntityRefGroup(parent, "Group1")
        ARXMLParser().readEOCExecutableEntityRefGroup(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "Group1"
        assert reloaded.getLetDataExchangeParadigm().getValue() == "intraLetEOC"
        let_interval_refs = reloaded.getLetIntervalRefs()
        assert len(let_interval_refs) == 1
        assert let_interval_refs[0].getValue() == "/AUTOSAR/LetChain"
        assert let_interval_refs[0].getDest() == "TIMING-DESCRIPTION-EVENT-CHAIN"
        assert reloaded.getMaxCycleRepetitions().getValue() == 4
        assert reloaded.getMaxCycles().getValue() == 12
        assert reloaded.getMaxSlots().getValue() == 3
        assert reloaded.getMaxSlotsPerCycle().getValue() == 2
        nested_refs = reloaded.getNestedElementRefs()
        assert len(nested_refs) == 2
        assert nested_refs[0].getValue() == "/AUTOSAR/Entity1"
        assert nested_refs[1].getValue() == "/AUTOSAR/Group2"
        direct_successors = reloaded.getDirectSuccessorRefs()
        assert len(direct_successors) == 1
        assert direct_successors[0].getValue() == "/AUTOSAR/Entity3"
        successors = reloaded.getSuccessorRefs()
        assert len(successors) == 1
        assert successors[0].getValue() == "/AUTOSAR/Entity4"
        assert reloaded.getTriggeringEventRef().getValue() == "/AUTOSAR/TimingEvent"

    def test_write_eoc_executable_entity_ref_group_empty_wrapper_lists(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        wrapper = ET.Element("ROOT")
        ARXMLWriter().writeEOCExecutableEntityRefGroup(wrapper, group)
        element = wrapper[0]
        assert element.find("DIRECT-SUCCESSOR-REFS") is None
        assert element.find("LET-DATA-EXCHANGE-PARADIGM") is None
        assert element.find("LET-INTERVAL-REFS") is None
        assert element.find("MAX-CYCLE-REPETITIONS") is None
        assert element.find("MAX-CYCLES") is None
        assert element.find("MAX-SLOTS") is None
        assert element.find("MAX-SLOTS-PER-CYCLE") is None
        assert element.find("NESTED-ELEMENT-REFS") is None
        assert element.find("SUCCESSOR-REFS") is None
        assert element.find("TRIGGERING-EVENT-REF") is None

        reloaded = EOCExecutableEntityRefGroup(parent, "Group1")
        ARXMLParser().readEOCExecutableEntityRefGroup(_round_trip(element), reloaded)
        assert reloaded.getLetDataExchangeParadigm() is None
        assert reloaded.getLetIntervalRefs() == []
        assert reloaded.getMaxCycleRepetitions() is None
        assert reloaded.getMaxCycles() is None
        assert reloaded.getMaxSlots() is None
        assert reloaded.getMaxSlotsPerCycle() is None
        assert reloaded.getNestedElementRefs() == []
        assert reloaded.getSuccessorRefs() == []
        assert reloaded.getTriggeringEventRef() is None

    def test_round_trip_eoc_event_ref(self):
        parent = self._parent()
        event_ref = EOCEventRef(parent, "EventRef1")
        event_ref.addDirectSuccessorRef(RefType().setValue("/AUTOSAR/Entity1").setDest("EOC-EXECUTABLE-ENTITY-REF"))
        event_ref.setBswModuleInstanceRef(RefType().setValue("/AUTOSAR/BswImpl").setDest("BSW-IMPLEMENTATION"))
        event_ref.setComponentIRef(RefType().setValue("/AUTOSAR/SwcProto").setDest("SW-COMPONENT-PROTOTYPE"))
        event_ref.setEventRef(RefType().setValue("/AUTOSAR/RteEvent").setDest("RTE-EVENT"))
        event_ref.addSuccessorRef(RefType().setValue("/AUTOSAR/Entity2").setDest("EOC-EVENT-REF"))

        wrapper = ET.Element("ROOT")
        ARXMLWriter().writeEOCEventRef(wrapper, event_ref)
        element = wrapper[0]
        assert element.tag == "EOC-EVENT-REF"
        assert element.find("EVENT-REF") is not None

        reloaded = EOCEventRef(parent, "EventRef1")
        ARXMLParser().readEOCEventRef(_round_trip(element), reloaded)
        assert reloaded.getShortName() == "EventRef1"
        assert reloaded.getBswModuleInstanceRef().getValue() == "/AUTOSAR/BswImpl"
        assert reloaded.getComponentIRef().getValue() == "/AUTOSAR/SwcProto"
        assert reloaded.getEventRef().getValue() == "/AUTOSAR/RteEvent"
        assert reloaded.getEventRef().getDest() == "RTE-EVENT"
        successors = reloaded.getSuccessorRefs()
        assert len(successors) == 1
        assert successors[0].getValue() == "/AUTOSAR/Entity2"
        direct_successors = reloaded.getDirectSuccessorRefs()
        assert len(direct_successors) == 1
        assert direct_successors[0].getValue() == "/AUTOSAR/Entity1"

    def test_round_trip_ordered_elements_dispatch_all_subtypes(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "Eoc")

        entity_ref = constraint.createEOCExecutableEntityRef("Entity1")
        entity_ref.setExecutableRef(RefType().setValue("/AUTOSAR/Runnable").setDest("RUNNABLE-ENTITY"))

        event_ref = constraint.createEOCEventRef("EventRef1")
        event_ref.setEventRef(RefType().setValue("/AUTOSAR/RteEvent").setDest("RTE-EVENT"))

        group = constraint.createEOCExecutableEntityRefGroup("Group1")
        group.setMaxSlotsPerCycle(PositiveInteger().setValue("5"))
        group.addNestedElementRef(RefType().setValue("/AUTOSAR/Entity1").setDest("EOC-EXECUTABLE-ENTITY-REF"))

        wrapper = ET.Element("EXECUTION-ORDER-CONSTRAINT")
        ARXMLWriter().writeExecutionOrderConstraintOrderedElement(wrapper, constraint)
        ordered_element_tag = wrapper.find("ORDERED-ELEMENTS")
        assert ordered_element_tag is not None
        assert len(ordered_element_tag) == 3

        reloaded_constraint = ExecutionOrderConstraint(parent, "Eoc")
        ARXMLParser().readExecutionOrderConstraintOrderedElement(_round_trip(wrapper), reloaded_constraint)

        elements = reloaded_constraint.getOrderedElements()
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
        assert elements[2].getNestedElementRefs()[0].getValue() == "/AUTOSAR/Entity1"
