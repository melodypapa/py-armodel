"""
Tests for reading COMPOSITE-NETWORK-REPRESENTATION elements — CompositeNetworkRepresentation, Table 4.74 (p.181, R23-11).

CompositeNetworkRepresentation (Base = ARObject) carries the optional LEAF-ELEMENT-IREF
(fixed-concrete iref of type APPLICATION-COMPOSITE-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF,
read flat with the inner refs directly under the element) and NETWORK-REPRESENTATION
(SW-DATA-DEF-PROPS, 0..1), in XSD group order LEAF-ELEMENT-IREF → NETWORK-REPRESENTATION.
It is aggregated by ReceiverComSpec/SenderComSpec .compositeNetworkRepresentation (the
COMPOSITE-NETWORK-REPRESENTATIONS wrapper) and read through the concrete comspec dispatch
(getQueuedReceiverComSpec → readReceiverComSpec → getCompositeNetworkRepresentation).

Round-trip counterpart: tests/test_armodel/writer/test_composite_network_representation.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestGetCompositeNetworkRepresentation:
    """Tests for getCompositeNetworkRepresentation — own element field values (Table 4.74)."""

    def test_with_both_elements(self, parser):
        """Test that LEAF-ELEMENT-IREF and NETWORK-REPRESENTATION are read with their field values."""
        element = _snip(
            "<LEAF-ELEMENT-IREF>"
            "<ROOT-DATA-PROTOTYPE-REF DEST='APPLICATION-PROTOTYPE'>/pkg/root</ROOT-DATA-PROTOTYPE-REF>"
            "<CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-DATA-PROTOTYPE'>/pkg/ctx1</CONTEXT-DATA-PROTOTYPE-REF>"
            "<CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-DATA-PROTOTYPE'>/pkg/ctx2</CONTEXT-DATA-PROTOTYPE-REF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='APPLICATION-DATA-PROTOTYPE'>/pkg/leaf</TARGET-DATA-PROTOTYPE-REF>"
            "</LEAF-ELEMENT-IREF>"
            "<NETWORK-REPRESENTATION>"
            "<SW-DATA-DEF-PROPS-VARIANTS><SW-DATA-DEF-PROPS-CONDITIONAL>"
            "<BASE-TYPE-REF DEST='SW-BASE-TYPE'>/pkg/uint8</BASE-TYPE-REF>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-VARIANTS>"
            "</NETWORK-REPRESENTATION>",
            root_tag="COMPOSITE-NETWORK-REPRESENTATION",
        )
        result = parser.getCompositeNetworkRepresentation(element)
        assert result is not None
        iref = result.getLeafElementIRef()
        assert iref is not None
        assert iref.getRootDataPrototypeRef() is not None
        assert iref.getRootDataPrototypeRef().getValue() == "/pkg/root"
        assert iref.getTargetDataPrototypeRef() is not None
        assert iref.getTargetDataPrototypeRef().getValue() == "/pkg/leaf"
        network_representation = result.getNetworkRepresentation()
        assert network_representation is not None
        assert network_representation.getBaseTypeRef() is not None
        assert network_representation.getBaseTypeRef().getValue() == "/pkg/uint8"

    def test_iref_context_ref_list_order(self, parser):
        """Test that the CONTEXT-DATA-PROTOTYPE-REF list is read in document order."""
        element = _snip(
            "<LEAF-ELEMENT-IREF>"
            "<CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-DATA-PROTOTYPE'>/pkg/first</CONTEXT-DATA-PROTOTYPE-REF>"
            "<CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-DATA-PROTOTYPE'>/pkg/second</CONTEXT-DATA-PROTOTYPE-REF>"
            "</LEAF-ELEMENT-IREF>",
            root_tag="COMPOSITE-NETWORK-REPRESENTATION",
        )
        result = parser.getCompositeNetworkRepresentation(element)
        iref = result.getLeafElementIRef()
        assert [ref.getValue() for ref in iref.getContextDataPrototypeRefs()] == ["/pkg/first", "/pkg/second"]
        assert result.getNetworkRepresentation() is None

    def test_with_leaf_element_only(self, parser):
        """Test that NETWORK-REPRESENTATION stays None when the element is absent."""
        element = _snip(
            "<LEAF-ELEMENT-IREF>" "<TARGET-DATA-PROTOTYPE-REF DEST='APPLICATION-DATA-PROTOTYPE'>/pkg/leaf</TARGET-DATA-PROTOTYPE-REF>" "</LEAF-ELEMENT-IREF>",
            root_tag="COMPOSITE-NETWORK-REPRESENTATION",
        )
        result = parser.getCompositeNetworkRepresentation(element)
        assert result.getLeafElementIRef() is not None
        assert result.getNetworkRepresentation() is None

    def test_minimal_empty_element(self, parser):
        """Test that both fields stay None when the element carries no child elements."""
        element = _snip("", root_tag="COMPOSITE-NETWORK-REPRESENTATION")
        result = parser.getCompositeNetworkRepresentation(element)
        assert result is not None
        assert result.getLeafElementIRef() is None
        assert result.getNetworkRepresentation() is None

    def test_read_via_queued_receiver_com_spec(self, parser):
        """Test that the ReceiverComSpec aggregation reads the representation list with field values."""
        element = _snip(
            "<COMPOSITE-NETWORK-REPRESENTATIONS>"
            "<COMPOSITE-NETWORK-REPRESENTATION>"
            "<LEAF-ELEMENT-IREF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='APPLICATION-DATA-PROTOTYPE'>/pkg/leaf</TARGET-DATA-PROTOTYPE-REF>"
            "</LEAF-ELEMENT-IREF>"
            "<NETWORK-REPRESENTATION>"
            "<SW-DATA-DEF-PROPS-VARIANTS><SW-DATA-DEF-PROPS-CONDITIONAL>"
            "<BASE-TYPE-REF DEST='SW-BASE-TYPE'>/pkg/uint8</BASE-TYPE-REF>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-VARIANTS>"
            "</NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATIONS>"
            "<QUEUE-LENGTH>10</QUEUE-LENGTH>",
            root_tag="QUEUED-RECEIVER-COM-SPEC",
        )
        com_spec = parser.getQueuedReceiverComSpec(element)
        assert com_spec is not None
        representations = com_spec.getCompositeNetworkRepresentations()
        assert len(representations) == 1
        representation = representations[0]
        assert representation.getLeafElementIRef() is not None
        assert representation.getLeafElementIRef().getTargetDataPrototypeRef().getValue() == "/pkg/leaf"
        assert representation.getNetworkRepresentation() is not None
        assert representation.getNetworkRepresentation().getBaseTypeRef().getValue() == "/pkg/uint8"
