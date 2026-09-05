"""
Tests for writing TRIGGER-INTERFACE elements (TriggerInterface, Table 4.12).

Round-trip counterpart: tests/test_armodel/parser/test_trigger_interface.py
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TriggerInterface
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteTriggerInterface:
    """
    Test writeTriggerInterface (TriggerInterface.trigger, Table 4.12).
    """

    def test_write_triggers_wrapper(self):
        """Test that triggers are written as TRIGGER-INTERFACE > TRIGGERS > TRIGGER in order."""
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        trigger_if = TriggerInterface(ar_root, "MyTriggerInterface")
        trigger1 = trigger_if.createTrigger("Trig1")
        trigger1.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.QUEUED))
        trigger_if.createTrigger("Trig2")

        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")
        writer.writeTriggerInterface(element, trigger_if)

        trigger_if_tag = element.find("TRIGGER-INTERFACE")
        assert trigger_if_tag is not None
        triggers_tag = trigger_if_tag.find("TRIGGERS")
        assert triggers_tag is not None
        trigger_tags = triggers_tag.findall("TRIGGER")
        assert len(trigger_tags) == 2
        assert trigger_tags[0].find("SHORT-NAME").text == "Trig1"
        assert trigger_tags[0].find("SW-IMPL-POLICY").text == "QUEUED"
        assert trigger_tags[1].find("SHORT-NAME").text == "Trig2"

    def test_write_absent_triggers(self):
        """Test that a TriggerInterface with no triggers writes no TRIGGERS wrapper."""
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        trigger_if = TriggerInterface(ar_root, "MyTriggerInterface")

        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")
        writer.writeTriggerInterface(element, trigger_if)

        trigger_if_tag = element.find("TRIGGER-INTERFACE")
        assert trigger_if_tag is not None
        assert trigger_if_tag.find("TRIGGERS") is None
