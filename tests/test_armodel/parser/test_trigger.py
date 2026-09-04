"""
Tests for reading TRIGGER elements (Trigger, Table 4.13).

Round-trip counterpart: tests/test_armodel/writer/test_trigger.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _make_trigger() -> Trigger:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    desc = BswModuleDescription(ar_root, "MyModule")
    ar_root.addElement(desc)
    return desc.createReleasedTrigger("MyTrigger")


class TestReadTrigger:
    """
    Test readTrigger (Trigger.swImplPolicy / triggerPeriod, Table 4.13).
    """

    def test_read_sw_impl_policy_and_trigger_period(self, parser):
        """Test that SW-IMPL-POLICY and TRIGGER-PERIOD populate the model fields."""
        trigger = _make_trigger()
        element = ET.fromstring(
            f"""<TRIGGER xmlns='{NS}'>
                <SHORT-NAME>MyTrigger</SHORT-NAME>
                <SW-IMPL-POLICY>QUEUED</SW-IMPL-POLICY>
                <TRIGGER-PERIOD>
                    <CSE-CODE>1.0</CSE-CODE>
                </TRIGGER-PERIOD>
            </TRIGGER>"""
        )

        parser.readTrigger(element, trigger)

        policy = trigger.getSwImplPolicy()
        assert policy is not None
        assert policy.getValue() == "queued"
        period = trigger.getTriggerPeriod()
        assert period is not None
        assert isinstance(period, MultidimensionalTime)
        assert period.getCseCode().getValue() == "1.0"

    def test_read_absent_attributes(self, parser):
        """Test that absent SW-IMPL-POLICY / TRIGGER-PERIOD leave the fields None."""
        trigger = _make_trigger()
        element = ET.fromstring(
            f"""<TRIGGER xmlns='{NS}'>
                <SHORT-NAME>MyTrigger</SHORT-NAME>
            </TRIGGER>"""
        )

        parser.readTrigger(element, trigger)

        assert trigger.getSwImplPolicy() is None
        assert trigger.getTriggerPeriod() is None

    def test_round_trip(self):
        """Write a BswModuleDescription with a released Trigger, reparse, assert the fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "MyModule")
        ar_root.addElement(desc)
        trigger = desc.createReleasedTrigger("MyTrigger")
        trigger.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.QUEUED))
        period = MultidimensionalTime()
        period.setCseCode(ARLiteral().setValue("1.0"))
        trigger.setTriggerPeriod(period)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            from armodel.writer.arxml_writer import ARXMLWriter

            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            desc_2 = document_2.getARPackages()[0].getElement("MyModule", BswModuleDescription)
            triggers = desc_2.getReleasedTriggers()
            assert len(triggers) == 1
            assert triggers[0].getShortName() == "MyTrigger"
            policy = triggers[0].getSwImplPolicy()
            assert policy is not None
            assert policy.getValue() == "queued"
            period_2 = triggers[0].getTriggerPeriod()
            assert period_2 is not None
            assert period_2.getCseCode().getValue() == "1.0"
        finally:
            os.remove(file_path)
