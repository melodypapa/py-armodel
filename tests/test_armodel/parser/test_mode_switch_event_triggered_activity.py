"""
Tests for reading MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY elements — ModeSwitchEventTriggeredActivity, Table 11.7 (p.675, R23-11).

ModeSwitchEventTriggeredActivity (Base = ARObject) carries two own attributes in XSD
group order (AUTOSAR_00052.xsd group MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY): ROLE,
SWC-MODE-SWITCH-EVENT-REF. It is aggregated by
NvBlockDescriptor.modeSwitchEventTriggeredActivity and read through
readNvBlockDescriptor → getModeSwitchEventTriggeredActivity.

Round-trip counterpart: tests/test_armodel/writer/test_mode_switch_event_triggered_activity.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity, NvBlockDescriptor
from tests.test_armodel.parser._helpers import _snip

NS = "http://autosar.org/schema/r4.0"


class TestGetModeSwitchEventTriggeredActivity:
    """Tests for getModeSwitchEventTriggeredActivity — own element field values (Table 11.7)."""

    def test_own_element_field_values(self, parser):
        """Test that both attribute elements are read with their field values."""
        element = _snip(
            "<ROLE>WriteBlock</ROLE>" "<SWC-MODE-SWITCH-EVENT-REF DEST='SWC-MODE-SWITCH-EVENT'>/SwcModeSwitchEvent</SWC-MODE-SWITCH-EVENT-REF>",
            root_tag="MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY",
        )

        activity = parser.getModeSwitchEventTriggeredActivity(element)

        assert activity is not None
        assert isinstance(activity, ModeSwitchEventTriggeredActivity)
        assert isinstance(activity.getRole(), Identifier)
        assert activity.getRole().getValue() == "WriteBlock"
        assert isinstance(activity.getSwcModeSwitchEventRef(), RefType)
        assert activity.getSwcModeSwitchEventRef().getValue() == "/SwcModeSwitchEvent"
        assert activity.getSwcModeSwitchEventRef().getDest() == "SWC-MODE-SWITCH-EVENT"

    def test_empty_element(self, parser):
        """Test that an empty element yields an instance with all fields unset."""
        element = _snip("", root_tag="MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")

        activity = parser.getModeSwitchEventTriggeredActivity(element)

        assert activity is not None
        assert activity.getRole() is None
        assert activity.getSwcModeSwitchEventRef() is None

    def test_absent_role(self, parser):
        """Test that an absent ROLE element leaves role unset while the reference is read."""
        element = _snip(
            "<SWC-MODE-SWITCH-EVENT-REF DEST='SWC-MODE-SWITCH-EVENT'>/SwcModeSwitchEvent</SWC-MODE-SWITCH-EVENT-REF>",
            root_tag="MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY",
        )

        activity = parser.getModeSwitchEventTriggeredActivity(element)

        assert activity.getRole() is None
        assert activity.getSwcModeSwitchEventRef().getValue() == "/SwcModeSwitchEvent"

    def test_absent_ref(self, parser):
        """Test that an absent SWC-MODE-SWITCH-EVENT-REF element leaves the reference unset while role is read."""
        element = _snip(
            "<ROLE>WriteBlock</ROLE>",
            root_tag="MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY",
        )

        activity = parser.getModeSwitchEventTriggeredActivity(element)

        assert activity.getRole().getValue() == "WriteBlock"
        assert activity.getSwcModeSwitchEventRef() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring("<MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY xmlns='%s' S='abc123' T='2024-01-01T12:00:00+00:00'></MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY>" % NS)

        activity = parser.getModeSwitchEventTriggeredActivity(element)

        assert activity is not None
        assert activity.getChecksum() is not None
        assert activity.getChecksum().getValue() == "abc123"
        assert activity.getTimestamp() is not None


class TestReadNvBlockDescriptorActivityDispatch:
    """Tests for the NvBlockDescriptor.modeSwitchEventTriggeredActivity aggregation dispatch."""

    def test_dispatch_via_read_nv_block_descriptor(self, parser):
        """Test that readNvBlockDescriptor reads the activity with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        element = _snip(
            "<SHORT-NAME>NvBlockDesc</SHORT-NAME>"
            "<MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS><MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY>"
            "<ROLE>WriteBlock</ROLE>"
            "<SWC-MODE-SWITCH-EVENT-REF DEST='SWC-MODE-SWITCH-EVENT'>/SwcModeSwitchEvent</SWC-MODE-SWITCH-EVENT-REF>"
            "</MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY></MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS>",
            root_tag="NV-BLOCK-DESCRIPTOR",
        )

        parser.readNvBlockDescriptor(element, descriptor)

        activities = descriptor.getModeSwitchEventTriggeredActivitys()
        assert len(activities) == 1
        assert isinstance(activities[0], ModeSwitchEventTriggeredActivity)
        assert activities[0].getRole().getValue() == "WriteBlock"
        assert activities[0].getSwcModeSwitchEventRef().getValue() == "/SwcModeSwitchEvent"
        assert activities[0].getSwcModeSwitchEventRef().getDest() == "SWC-MODE-SWITCH-EVENT"

    def test_dispatch_absent_activities_yield_empty(self, parser):
        """Test that a descriptor without activities yields an empty list."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        element = _snip("<SHORT-NAME>NvBlockDesc</SHORT-NAME>", root_tag="NV-BLOCK-DESCRIPTOR")

        parser.readNvBlockDescriptor(element, descriptor)

        assert descriptor.getModeSwitchEventTriggeredActivitys() == []
