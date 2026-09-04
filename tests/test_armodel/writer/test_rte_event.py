"""
Tests for writing RTEEvent members — Table 7.9 (p.541, R23-11).

RTEEvent is abstract; exercised via the concrete DataSendCompletedEvent.
DISABLED-MODE-IREFS (wrapper of DISABLED-MODE-IREF, type R-MODE-IN-ATOMIC-SWC-INSTANCE-REF)
is written before START-ON-EVENT-REF per the XSD RTE-EVENT group order.

Round-trip counterpart: tests/test_armodel/parser/test_rte_event.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataSendCompletedEvent
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _event_with_members(with_members=True):
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    event = DataSendCompletedEvent(ar_root, "dse")

    if with_members:
        iref1 = RModeInAtomicSwcInstanceRef()
        iref1.setContextPortRef(_ref("R-PORT-PROTOTYPE", "/MyComponents/rp_mode_port"))
        iref1.setContextModeDeclarationGroupPrototypeRef(_ref("MODE-DECLARATION-GROUP-PROTOTYPE", "/MyComponents/mdg_prototype"))
        iref1.setTargetModeDeclarationRef(_ref("MODE-DECLARATION", "/Mdgs/MyModeGroup/MyMode"))
        iref2 = RModeInAtomicSwcInstanceRef()
        iref2.setTargetModeDeclarationRef(_ref("MODE-DECLARATION", "/Mdgs/MyModeGroup/MyOtherMode"))
        event.addDisabledModeIRef(iref1)
        event.addDisabledModeIRef(iref2)
        event.setStartOnEventRef(_ref("RUNNABLE-ENTITY", "/MyComponents/MySwc_IB/re_disabled"))

    return event


class TestWriteRTEEvent:
    """
    Test setRTEEvent → DISABLED-MODE-IREFS + START-ON-EVENT-REF (Table 7.9).
    """

    def test_write_field_values(self):
        event = _event_with_members()

        writer = ARXMLWriter()
        element = ET.Element("DATA-SEND-COMPLETED-EVENT")
        writer.setRTEEvent(element, event)

        wrapper = element.find("DISABLED-MODE-IREFS")
        assert wrapper is not None
        irefs = wrapper.findall("DISABLED-MODE-IREF")
        assert len(irefs) == 2

        iref1 = irefs[0]
        context_port = iref1.find("CONTEXT-PORT-REF")
        assert context_port.get("DEST") == "R-PORT-PROTOTYPE"
        assert context_port.text == "/MyComponents/rp_mode_port"
        context_group = iref1.find("CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")
        assert context_group.get("DEST") == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert context_group.text == "/MyComponents/mdg_prototype"
        target_mode = iref1.find("TARGET-MODE-DECLARATION-REF")
        assert target_mode.get("DEST") == "MODE-DECLARATION"
        assert target_mode.text == "/Mdgs/MyModeGroup/MyMode"

        iref2 = irefs[1]
        assert iref2.find("CONTEXT-PORT-REF") is None
        assert iref2.find("TARGET-MODE-DECLARATION-REF").text == "/Mdgs/MyModeGroup/MyOtherMode"

        start_ref = element.find("START-ON-EVENT-REF")
        assert start_ref is not None
        assert start_ref.get("DEST") == "RUNNABLE-ENTITY"
        assert start_ref.text == "/MyComponents/MySwc_IB/re_disabled"

        # XSD RTE-EVENT group order: DISABLED-MODE-IREFS before START-ON-EVENT-REF
        children = [child.tag for child in element]
        assert children.index("DISABLED-MODE-IREFS") < children.index("START-ON-EVENT-REF")

    def test_write_empty_event(self):
        event = _event_with_members(with_members=False)

        writer = ARXMLWriter()
        element = ET.Element("DATA-SEND-COMPLETED-EVENT")
        writer.setRTEEvent(element, event)

        assert element.find("DISABLED-MODE-IREFS") is None
        assert element.find("START-ON-EVENT-REF") is None
