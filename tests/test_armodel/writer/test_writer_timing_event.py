"""Writer/reader round-trip tests for TimingEvent (Table 7.4, p.532, R23-11).

Element order per the XSD complexType TIMING-EVENT: ABSTRACT-EVENT group
(ACTIVATION-REASON-REPRESENTATION-REF), RTE-EVENT group (DISABLED-MODE-IREFS,
START-ON-EVENT-REF), TIMING-EVENT group (OFFSET, PERIOD).

Round-trip counterpart: tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/test_RTEEvents.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import TimingEvent
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _make_timing_event():
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    behavior = swc.createSwcInternalBehavior("Behavior")
    return behavior.createTimingEvent("TimingEvt")


def test_write_element_order_matches_xsd_group():
    event = _make_timing_event()
    ref = RefType()
    ref.setDest("EXECUTABLE-ENTITY-ACTIVATION-REASON")
    ref.setValue("/Pkg/Swc_IB/Cyclic/ReasonA")
    event.setActivationReasonRepresentationRef(ref)
    event.setStartOnEventRef(RefType().setValue("/Pkg/Swc_IB/Cyclic"))
    offset = TimeValue()
    offset.setValue(1.5)
    event.setOffset(offset)
    period = TimeValue()
    period.setValue(10.0)
    event.setPeriod(period)

    parent = ET.Element("EVENTS")
    ARXMLWriter().writeTimingEvent(parent, event)

    element = parent.find("TIMING-EVENT")
    expected = ["ACTIVATION-REASON-REPRESENTATION-REF", "START-ON-EVENT-REF", "OFFSET", "PERIOD"]
    children = [child.tag for child in element if child.tag in expected]
    assert children == expected
    assert element.find("OFFSET").text == "1.5"
    assert element.find("PERIOD").text == "10.0"


def test_round_trip_preserves_field_values():
    event = _make_timing_event()
    offset = TimeValue()
    offset.setValue(2.5)
    event.setOffset(offset)
    period = TimeValue()
    period.setValue(20.0)
    event.setPeriod(period)

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, AUTOSAR.getInstance())
        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        package_2 = document_2.getARPackages()[0]
        swc_2 = package_2.getReferrableElement("Swc")
        behavior_2 = swc_2.getReferrableElement("Behavior")
        event_2 = behavior_2.getReferrableElement("TimingEvt")
        assert isinstance(event_2, TimingEvent)
        assert event_2.getOffset() is not None
        assert event_2.getOffset().getValue() == 2.5
        assert event_2.getPeriod() is not None
        assert event_2.getPeriod().getValue() == 20.0
        assert event_2.periodMs == 20000
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def test_round_trip_empty_timing_event():
    _make_timing_event()

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, AUTOSAR.getInstance())
        raw = open(file_path, encoding="utf-8").read()
        assert "<OFFSET" not in raw
        assert "<PERIOD" not in raw

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)
        event_2 = document_2.getARPackages()[0].getReferrableElement("Swc").getReferrableElement("Behavior").getReferrableElement("TimingEvt")
        assert event_2.getOffset() is None
        assert event_2.getPeriod() is None
        assert event_2.periodMs is None
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
