"""
Tests for writing TRIGGER elements (Trigger, Table 4.13).

Round-trip counterpart: tests/test_armodel/parser/test_trigger.py
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteTrigger:
    """
    Test writeTrigger (Trigger.swImplPolicy / triggerPeriod, Table 4.13).
    """

    def test_write_sw_impl_policy_and_trigger_period(self):
        """Test that swImplPolicy and triggerPeriod are written in XSD order (SW-IMPL-POLICY < TRIGGER-PERIOD)."""
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "MyTrigger")
        trigger.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.QUEUED))
        period = MultidimensionalTime()
        period.setCseCode(ARLiteral().setValue("1.0"))
        trigger.setTriggerPeriod(period)

        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")
        writer.writeTrigger(element, trigger)

        trigger_tag = element.find("TRIGGER")
        assert trigger_tag is not None
        own_tags = [tag for tag in (child.tag for child in trigger_tag) if tag in ("SW-IMPL-POLICY", "TRIGGER-PERIOD")]
        assert own_tags == ["SW-IMPL-POLICY", "TRIGGER-PERIOD"]
        assert trigger_tag.find("SW-IMPL-POLICY").text == "QUEUED"
        assert trigger_tag.find("TRIGGER-PERIOD").find("CSE-CODE").text == "1.0"

    def test_write_absent_attributes(self):
        """Test that a Trigger with no own attributes writes no own elements."""
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "MyTrigger")

        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")
        writer.writeTrigger(element, trigger)

        trigger_tag = element.find("TRIGGER")
        assert trigger_tag is not None
        own_tags = [tag for tag in (child.tag for child in trigger_tag) if tag in ("SW-IMPL-POLICY", "TRIGGER-PERIOD")]
        assert own_tags == []
