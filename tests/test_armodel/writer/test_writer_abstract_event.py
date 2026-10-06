"""Writer/reader round-trip tests for AbstractEvent (Table 7.8, p.541, R23-11).

AbstractEvent is an abstract XML-bearing base: its ACTIVATION-REASON-REPRESENTATION-REF
element (XSD group ABSTRACT-EVENT) is serialized through the reusable
readAbstractEvent/writeAbstractEvent helpers that the BswEvent and RTEEvent
branches call. Exercise the abstract class via the concrete InitEvent (RTEEvent
branch) and BswModeSwitchEvent (BswEvent branch).

Round-trip counterpart: tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/test_AbstractEvent.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswModeSwitchEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import TimingEvent
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _make_timing_event():
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    behavior = swc.createSwcInternalBehavior("Behavior")
    return behavior.createTimingEvent("TimingEvt")


def test_write_abstract_event_field_values():
    event = _make_timing_event()
    event.setActivationReasonRepresentationRef(_ref("EXECUTABLE-ENTITY-ACTIVATION-REASON", "/Pkg/Swc_IB/Cyclic/ReasonA"))

    element = ET.Element("TIMING-EVENT")
    ARXMLWriter().writeAbstractEvent(element, event)

    ref_tag = element.find("ACTIVATION-REASON-REPRESENTATION-REF")
    assert ref_tag is not None
    assert ref_tag.get("DEST") == "EXECUTABLE-ENTITY-ACTIVATION-REASON"
    assert ref_tag.text == "/Pkg/Swc_IB/Cyclic/ReasonA"


def test_write_abstract_event_omitted_when_none():
    event = _make_timing_event()
    element = ET.Element("TIMING-EVENT")
    ARXMLWriter().writeAbstractEvent(element, event)
    assert element.find("ACTIVATION-REASON-REPRESENTATION-REF") is None


def test_read_abstract_event_field_values():
    xml_content = """
        <TIMING-EVENT>
          <SHORT-NAME>TimingEvt</SHORT-NAME>
          <ACTIVATION-REASON-REPRESENTATION-REF DEST="EXECUTABLE-ENTITY-ACTIVATION-REASON">/Pkg/Swc_IB/Cyclic/ReasonA</ACTIVATION-REASON-REPRESENTATION-REF>
        </TIMING-EVENT>
    """
    element = ET.fromstring(xml_content)
    document = AUTOSAR.getInstance()
    event = TimingEvent(document, "TimingEvt")
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": ""}
    parser.readAbstractEvent(element, event)

    ref = event.getActivationReasonRepresentationRef()
    assert ref is not None
    assert ref.getDest() == "EXECUTABLE-ENTITY-ACTIVATION-REASON"
    assert ref.getValue() == "/Pkg/Swc_IB/Cyclic/ReasonA"


def test_read_bsw_event_via_abstract_event_helper():
    xml_content = """
        <BSW-MODE-SWITCH-EVENT>
          <SHORT-NAME>BswEvt</SHORT-NAME>
          <ACTIVATION-REASON-REPRESENTATION-REF DEST="EXECUTABLE-ENTITY-ACTIVATION-REASON">/Bsw/Behavior/Entity/ReasonB</ACTIVATION-REASON-REPRESENTATION-REF>
        </BSW-MODE-SWITCH-EVENT>
    """
    element = ET.fromstring(xml_content)
    document = AUTOSAR.getInstance()
    event = BswModeSwitchEvent(document, "BswEvt")
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": ""}
    parser.readBswEvent(element, event)

    assert event.getShortName() == "BswEvt"
    ref = event.getActivationReasonRepresentationRef()
    assert ref is not None
    assert ref.getValue() == "/Bsw/Behavior/Entity/ReasonB"


def test_write_bsw_event_activation_reason_representation():
    event = BswModeSwitchEvent(AUTOSAR.getInstance(), "BswEvt")
    event.setActivationReasonRepresentationRef(_ref("EXECUTABLE-ENTITY-ACTIVATION-REASON", "/Bsw/Behavior/Entity/ReasonB"))

    element = ET.Element("BSW-MODE-SWITCH-EVENT")
    ARXMLWriter().writeBswEvent(element, event)

    ref_tag = element.find("ACTIVATION-REASON-REPRESENTATION-REF")
    assert ref_tag is not None
    assert ref_tag.get("DEST") == "EXECUTABLE-ENTITY-ACTIVATION-REASON"
    assert ref_tag.text == "/Bsw/Behavior/Entity/ReasonB"
    short_name_tag = element.find("SHORT-NAME")
    assert short_name_tag is not None
    assert short_name_tag.text == "BswEvt"


def test_round_trip_preserves_field_values():
    event = _make_timing_event()
    event.setActivationReasonRepresentationRef(_ref("EXECUTABLE-ENTITY-ACTIVATION-REASON", "/Pkg/Swc_IB/Cyclic/ReasonA"))

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
        ref = event_2.getActivationReasonRepresentationRef()
        assert ref is not None
        assert ref.getDest() == "EXECUTABLE-ENTITY-ACTIVATION-REASON"
        assert ref.getValue() == "/Pkg/Swc_IB/Cyclic/ReasonA"
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
