"""
Tests for reading MODE-SWITCH-SENDER-COM-SPEC elements — ModeSwitchSenderComSpec, Table 4.79 (p.190, R23-11).

ModeSwitchSenderComSpec (Base = PPortComSpec) carries the optional attributes
enhancedModeApi (BOOLEAN 0..1), modeGroup (MODE-GROUP-REF 0..1),
modeSwitchedAck (MODE-SWITCHED-ACK 0..1 aggregation) and queueLength
(QUEUE-LENGTH 0..1 PositiveInteger). It is aggregated by
AbstractProvidedPortPrototype.providedComSpec and read through
readProvidedComSpec → getModeSwitchSenderComSpec.

Round-trip counterpart: tests/test_armodel/writer/test_mode_switch_sender_com_spec.py
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ModeSwitchSenderComSpec
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestGetModeSwitchSenderComSpec:
    """Tests for getModeSwitchSenderComSpec — own element field values (Table 4.79)."""

    def test_own_elements_field_values(self, parser):
        """Test that all four elements are read with their field values."""
        element = _snip(
            """
            <ENHANCED-MODE-API>true</ENHANCED-MODE-API>
            <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
            <MODE-SWITCHED-ACK>
                <TIMEOUT>0.5</TIMEOUT>
            </MODE-SWITCHED-ACK>
            <QUEUE-LENGTH>4</QUEUE-LENGTH>
            """,
            root_tag="MODE-SWITCH-SENDER-COM-SPEC",
        )
        result = parser.getModeSwitchSenderComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is not None
        assert result.getEnhancedModeApi().getValue() is True
        assert result.getModeGroupRef() is not None
        assert result.getModeGroupRef().getValue() == "/mdg/Group"
        assert result.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert result.getModeSwitchedAck() is not None
        assert result.getModeSwitchedAck().getTimeout() is not None
        assert result.getModeSwitchedAck().getTimeout().getValue() == 0.5
        assert result.getQueueLength() is not None
        assert isinstance(result.getQueueLength(), PositiveInteger)
        assert result.getQueueLength().getValue() == 4

    def test_empty_element(self, parser):
        """Test that an empty MODE-SWITCH-SENDER-COM-SPEC element yields an instance with all fields None."""
        element = _snip("", root_tag="MODE-SWITCH-SENDER-COM-SPEC")
        result = parser.getModeSwitchSenderComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is None
        assert result.getModeGroupRef() is None
        assert result.getModeSwitchedAck() is None
        assert result.getQueueLength() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(
            '<MODE-SWITCH-SENDER-COM-SPEC xmlns="http://autosar.org/schema/r4.0" S="abc123" T="2024-01-01T12:00:00+00:00"><ENHANCED-MODE-API>true</ENHANCED-MODE-API></MODE-SWITCH-SENDER-COM-SPEC>'
        )
        result = parser.getModeSwitchSenderComSpec(element)
        assert result is not None
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "abc123"
        assert result.getTimestamp() is not None

    def test_read_via_provided_com_spec_dispatch(self, parser):
        """Test that the AbstractProvidedPortPrototype.providedComSpec aggregation reads the com spec with field values."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
        p_port = app.createPPortPrototype("PPort")
        element = _snip("""
            <PROVIDED-COM-SPECS>
                <MODE-SWITCH-SENDER-COM-SPEC>
                    <ENHANCED-MODE-API>true</ENHANCED-MODE-API>
                    <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
                </MODE-SWITCH-SENDER-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """)
        parser.readProvidedComSpec(element, p_port)
        specs = p_port.getProvidedComSpecs()
        assert len(specs) == 1
        com_spec = specs[0]
        assert isinstance(com_spec, ModeSwitchSenderComSpec)
        assert com_spec.getEnhancedModeApi() is not None
        assert com_spec.getEnhancedModeApi().getValue() is True
        assert com_spec.getModeGroupRef() is not None
        assert com_spec.getModeGroupRef().getValue() == "/mdg/Group"
