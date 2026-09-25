"""
Tests for reading MODE-SWITCH-RECEIVER-COM-SPEC elements — ModeSwitchReceiverComSpec, Table 4.81 (p.191, R23-11).

ModeSwitchReceiverComSpec (Base = RPortComSpec) carries the optional attributes
enhancedModeApi (BOOLEAN 0..1), modeGroup (MODE-GROUP-REF 0..1) and
supportsAsynchronousModeSwitch (BOOLEAN 0..1). It is aggregated by
AbstractRequiredPortPrototype.requiredComSpec and read through
readRequiredComSpec → getModeSwitchReceiverComSpec.

Round-trip counterpart: tests/test_armodel/writer/test_mode_switch_receiver_com_spec.py
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ModeSwitchReceiverComSpec
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestGetModeSwitchReceiverComSpec:
    """Tests for getModeSwitchReceiverComSpec — own element field values (Table 4.81)."""

    def test_own_elements_field_values(self, parser):
        """Test that all three elements are read with their field values."""
        element = _snip(
            """
            <ENHANCED-MODE-API>true</ENHANCED-MODE-API>
            <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
            <SUPPORTS-ASYNCHRONOUS-MODE-SWITCH>false</SUPPORTS-ASYNCHRONOUS-MODE-SWITCH>
            """,
            root_tag="MODE-SWITCH-RECEIVER-COM-SPEC",
        )
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is not None
        assert result.getEnhancedModeApi().getValue() is True
        assert result.getModeGroupRef() is not None
        assert result.getModeGroupRef().getValue() == "/mdg/Group"
        assert result.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert result.getSupportsAsynchronousModeSwitch() is not None
        assert result.getSupportsAsynchronousModeSwitch().getValue() is False

    def test_empty_element(self, parser):
        """Test that an empty MODE-SWITCH-RECEIVER-COM-SPEC element yields an instance with all fields None."""
        element = _snip("", root_tag="MODE-SWITCH-RECEIVER-COM-SPEC")
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is None
        assert result.getModeGroupRef() is None
        assert result.getSupportsAsynchronousModeSwitch() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(
            '<MODE-SWITCH-RECEIVER-COM-SPEC xmlns="http://autosar.org/schema/r4.0" S="abc123" T="2024-01-01T12:00:00+00:00"><ENHANCED-MODE-API>true</ENHANCED-MODE-API></MODE-SWITCH-RECEIVER-COM-SPEC>'
        )
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "abc123"
        assert result.getTimestamp() is not None

    def test_read_via_required_com_spec_dispatch(self, parser):
        """Test that the AbstractRequiredPortPrototype.requiredComSpec aggregation reads the com spec with field values."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
        r_port = app.createRPortPrototype("RPort")
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <MODE-SWITCH-RECEIVER-COM-SPEC>
                    <ENHANCED-MODE-API>true</ENHANCED-MODE-API>
                    <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
                </MODE-SWITCH-RECEIVER-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        parser.readRequiredComSpec(element, r_port)
        specs = r_port.getRequiredComSpecs()
        assert len(specs) == 1
        com_spec = specs[0]
        assert isinstance(com_spec, ModeSwitchReceiverComSpec)
        assert com_spec.getEnhancedModeApi() is not None
        assert com_spec.getEnhancedModeApi().getValue() is True
        assert com_spec.getModeGroupRef() is not None
        assert com_spec.getModeGroupRef().getValue() == "/mdg/Group"
