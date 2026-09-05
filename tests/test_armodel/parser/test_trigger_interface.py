"""
Tests for reading TRIGGER-INTERFACE elements (TriggerInterface, Table 4.12).

Round-trip counterpart: tests/test_armodel/writer/test_trigger_interface.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TriggerInterface
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTriggerInterface:
    """
    Test readTriggerInterface (TriggerInterface.trigger, Table 4.12).
    """

    def test_read_triggers(self, parser):
        """Test that TRIGGERS/TRIGGER children populate the triggers list."""
        trigger_if = TriggerInterface(AUTOSAR.getInstance(), "MyTriggerInterface")
        element = ET.fromstring(
            f"""<TRIGGER-INTERFACE xmlns='{NS}'>
                <SHORT-NAME>MyTriggerInterface</SHORT-NAME>
                <TRIGGERS>
                    <TRIGGER>
                        <SHORT-NAME>Trig1</SHORT-NAME>
                        <SW-IMPL-POLICY>QUEUED</SW-IMPL-POLICY>
                    </TRIGGER>
                    <TRIGGER>
                        <SHORT-NAME>Trig2</SHORT-NAME>
                    </TRIGGER>
                </TRIGGERS>
            </TRIGGER-INTERFACE>"""
        )

        parser.readTriggerInterface(element, trigger_if)

        triggers = trigger_if.getTriggers()
        assert len(triggers) == 2
        assert triggers[0].getShortName() == "Trig1"
        policy = triggers[0].getSwImplPolicy()
        assert policy is not None
        assert policy.getValue() == "queued"
        assert triggers[1].getShortName() == "Trig2"
        assert triggers[1].getSwImplPolicy() is None

    def test_read_absent_triggers(self, parser):
        """Test that an absent TRIGGERS wrapper leaves the triggers list empty."""
        trigger_if = TriggerInterface(AUTOSAR.getInstance(), "MyTriggerInterface")
        element = ET.fromstring(
            f"""<TRIGGER-INTERFACE xmlns='{NS}'>
                <SHORT-NAME>MyTriggerInterface</SHORT-NAME>
            </TRIGGER-INTERFACE>"""
        )

        parser.readTriggerInterface(element, trigger_if)

        assert trigger_if.getTriggers() == []

    def test_round_trip(self):
        """Write a package with a TriggerInterface, reparse, assert the triggers survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        pkg = ar_root.createARPackage("PortInterfaces")
        trigger_if = TriggerInterface(pkg, "MyTriggerInterface")
        pkg.addElement(trigger_if)
        trigger1 = trigger_if.createTrigger("Trig1")
        trigger1.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.QUEUED))
        trigger_if.createTrigger("Trig2")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            from armodel.writer.arxml_writer import ARXMLWriter

            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            pkg_2 = document_2.getARPackages()[0].getARPackages()[0]
            trigger_if_2 = pkg_2.getElement("MyTriggerInterface", TriggerInterface)
            assert trigger_if_2 is not None
            triggers = trigger_if_2.getTriggers()
            assert len(triggers) == 2
            assert triggers[0].getShortName() == "Trig1"
            policy = triggers[0].getSwImplPolicy()
            assert policy is not None
            assert policy.getValue() == "queued"
            assert triggers[1].getShortName() == "Trig2"
        finally:
            os.remove(file_path)
