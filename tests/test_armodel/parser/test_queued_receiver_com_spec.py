"""
Tests for reading QUEUED-RECEIVER-COM-SPEC elements — QueuedReceiverComSpec, Table 4.63 (p.173, R23-11).

QueuedReceiverComSpec (Base = ARObject + RPortComSpec + ReceiverComSpec) carries the
single own attribute queueLength (QUEUE-LENGTH 0..1 PositiveInteger). It is aggregated
by AbstractRequiredPortPrototype.requiredComSpec and PortPrototypeBlueprint.requiredComSpec
and read through readRequiredComSpec → getQueuedReceiverComSpec; the inherited
ReceiverComSpec elements arrive through readReceiverComSpec.

Round-trip counterpart: tests/test_armodel/writer/test_queued_receiver_com_spec.py
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import QueuedReceiverComSpec
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestGetQueuedReceiverComSpec:
    """Tests for getQueuedReceiverComSpec — own element field values (Table 4.63)."""

    def test_own_element_field_value(self, parser):
        """Test that QUEUE-LENGTH is read as a spec-typed PositiveInteger with its value."""
        element = _snip("<QUEUE-LENGTH>5</QUEUE-LENGTH>", root_tag="QUEUED-RECEIVER-COM-SPEC")
        result = parser.getQueuedReceiverComSpec(element)
        assert result is not None
        assert isinstance(result.getQueueLength(), PositiveInteger)
        assert result.getQueueLength().getValue() == 5

    def test_inherited_and_own_elements_read(self, parser):
        """Test that inherited ReceiverComSpec elements and the own QUEUE-LENGTH are both read."""
        element = _snip(
            """
            <DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/pkg/Interface/Data</DATA-ELEMENT-REF>
            <QUEUE-LENGTH>5</QUEUE-LENGTH>
            """,
            root_tag="QUEUED-RECEIVER-COM-SPEC",
        )
        result = parser.getQueuedReceiverComSpec(element)
        assert result is not None
        assert result.getDataElementRef() is not None
        assert result.getDataElementRef().getValue() == "/pkg/Interface/Data"
        assert result.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert result.getQueueLength() is not None
        assert result.getQueueLength().getValue() == 5

    def test_empty_element(self, parser):
        """Test that an empty QUEUED-RECEIVER-COM-SPEC element yields an instance with queueLength None."""
        element = _snip("", root_tag="QUEUED-RECEIVER-COM-SPEC")
        result = parser.getQueuedReceiverComSpec(element)
        assert result is not None
        assert result.getQueueLength() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring('<QUEUED-RECEIVER-COM-SPEC xmlns="http://autosar.org/schema/r4.0" S="abc123" T="2024-01-01T12:00:00+00:00"><QUEUE-LENGTH>5</QUEUE-LENGTH></QUEUED-RECEIVER-COM-SPEC>')
        result = parser.getQueuedReceiverComSpec(element)
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
                <QUEUED-RECEIVER-COM-SPEC>
                    <QUEUE-LENGTH>5</QUEUE-LENGTH>
                </QUEUED-RECEIVER-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        parser.readRequiredComSpec(element, r_port)
        specs = r_port.getRequiredComSpecs()
        assert len(specs) == 1
        com_spec = specs[0]
        assert isinstance(com_spec, QueuedReceiverComSpec)
        assert isinstance(com_spec.getQueueLength(), PositiveInteger)
        assert com_spec.getQueueLength().getValue() == 5
