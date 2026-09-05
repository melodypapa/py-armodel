"""
Tests for reading TRIGGER-MAPPING elements (TriggerMapping, Table 4.31) via
the TriggerInterfaceMapping TRIGGER-MAPPINGS wrapper.

Round-trip counterpart: tests/test_armodel/writer/test_trigger_mapping.py
"""

import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TriggerInterfaceMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTriggerMapping:
    """
    Test TriggerMapping ref population via readTriggerInterfaceMapping (Table 4.31).
    """

    def test_read_field_values(self, parser):
        """Test that FIRST-TRIGGER-REF/SECOND-TRIGGER-REF populate both refs with DEST."""
        tim = TriggerInterfaceMapping(AUTOSAR.getInstance(), "tim")
        element = ET.fromstring(
            f"""<TRIGGER-INTERFACE-MAPPING xmlns='{NS}'>
                <SHORT-NAME>tim</SHORT-NAME>
                <TRIGGER-MAPPINGS>
                    <TRIGGER-MAPPING>
                        <FIRST-TRIGGER-REF DEST='TRIGGER'>/pkg/trigger1</FIRST-TRIGGER-REF>
                        <SECOND-TRIGGER-REF DEST='TRIGGER'>/pkg/trigger2</SECOND-TRIGGER-REF>
                    </TRIGGER-MAPPING>
                    <TRIGGER-MAPPING>
                        <FIRST-TRIGGER-REF DEST='TRIGGER'>/pkg/trigger3</FIRST-TRIGGER-REF>
                    </TRIGGER-MAPPING>
                </TRIGGER-MAPPINGS>
            </TRIGGER-INTERFACE-MAPPING>"""
        )

        parser.readTriggerInterfaceMapping(element, tim)

        trigger_mappings = tim.getTriggerMappings()
        assert len(trigger_mappings) == 2

        first = trigger_mappings[0]
        assert first.getFirstTriggerRef().getValue() == "/pkg/trigger1"
        assert first.getFirstTriggerRef().getDest() == "TRIGGER"
        assert first.getSecondTriggerRef().getValue() == "/pkg/trigger2"
        assert first.getSecondTriggerRef().getDest() == "TRIGGER"

        second = trigger_mappings[1]
        assert second.getFirstTriggerRef().getValue() == "/pkg/trigger3"
        assert second.getSecondTriggerRef() is None

    def test_read_absent_refs(self, parser):
        """Test that a TRIGGER-MAPPING without ref elements leaves both refs None."""
        tim = TriggerInterfaceMapping(AUTOSAR.getInstance(), "tim")
        element = ET.fromstring(
            f"""<TRIGGER-INTERFACE-MAPPING xmlns='{NS}'>
                <SHORT-NAME>tim</SHORT-NAME>
                <TRIGGER-MAPPINGS>
                    <TRIGGER-MAPPING/>
                </TRIGGER-MAPPINGS>
            </TRIGGER-INTERFACE-MAPPING>"""
        )

        parser.readTriggerInterfaceMapping(element, tim)

        trigger_mapping = tim.getTriggerMappings()[0]
        assert trigger_mapping.getFirstTriggerRef() is None
        assert trigger_mapping.getSecondTriggerRef() is None

    def test_round_trip(self):
        """Write a package with a TriggerInterfaceMapping, reparse, assert both TriggerMapping refs survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        pkg = ar_root.createARPackage("Mappings")
        pims = pkg.createPortInterfaceMappingSet("Pims")
        tim = pims.createTriggerInterfaceMapping("tim")

        from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        trigger_mapping = TriggerMapping()
        trigger_mapping.setFirstTriggerRef(RefType().setValue("/Types/Trig1"))
        trigger_mapping.getFirstTriggerRef().setDest("TRIGGER")
        trigger_mapping.setSecondTriggerRef(RefType().setValue("/Types/Trig2"))
        trigger_mapping.getSecondTriggerRef().setDest("TRIGGER")
        tim.addTriggerMapping(trigger_mapping)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            from armodel.writer.arxml_writer import ARXMLWriter

            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            pkg_2 = document_2.getARPackages()[0].getARPackages()[0]
            pims_2 = pkg_2.getElement("Pims")
            assert pims_2 is not None

            tim_2 = pims_2.getPortInterfaceMappings()[0]
            assert tim_2.getShortName() == "tim"

            trigger_mappings_2 = tim_2.getTriggerMappings()
            assert len(trigger_mappings_2) == 1
            first_2 = trigger_mappings_2[0].getFirstTriggerRef()
            assert first_2.getValue() == "/Types/Trig1"
            assert first_2.getDest() == "TRIGGER"
            second_2 = trigger_mappings_2[0].getSecondTriggerRef()
            assert second_2.getValue() == "/Types/Trig2"
            assert second_2.getDest() == "TRIGGER"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
