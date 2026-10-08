import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpNode


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _node(short_name: str) -> FlexrayArTpNode:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return FlexrayArTpNode(package, short_name)


class Test_FlexrayArTpNode:
    # Table 6.247, p.603 — class Note verbatim from the markdown; attribute notes from the XSD
    # (the PDF table has no Note column)
    NOTE_CONNECTOR_REFS = "Association  to one or more physical connectors (max number of connectors for FlexRay: 2)."
    NOTE_TP_ADDRESS_REF = "Reference to the TP Address that is used by the TpNode. " "This reference is optional in case that the multicast TP Address is used (reference from TpConnection)."

    def test_docstring_is_spec_note_verbatim(self):
        assert cleandoc(FlexrayArTpNode.__doc__) == "TP Node (Sender or Receiver) provides the TP Address and the connection to the Topology"

    def test_init_has_no_docstring(self):
        assert FlexrayArTpNode.__init__.__doc__ is None

    def test_heritage(self):
        node = _node("Node1")
        assert isinstance(node, Identifiable)

    def test_initialization(self):
        node = _node("Node1")
        assert node.getConnectorRefs() == []
        assert node.getTpAddressRef() is None

    def test_add_connector_ref(self):
        node = _node("Node1")
        ref1 = _ref("/Connectors/C1", "FLEXRAY-COMMUNICATION-CONNECTOR")
        ref2 = _ref("/Connectors/C2", "FLEXRAY-COMMUNICATION-CONNECTOR")
        assert node.addConnectorRef(ref1) is node
        node.addConnectorRef(ref2)
        assert node.getConnectorRefs() == [ref1, ref2]
        node.addConnectorRef(None)
        assert node.getConnectorRefs() == [ref1, ref2]

    def test_get_set_tp_address_ref(self):
        node = _node("Node1")
        value = _ref("/TpAddresses/Addr1", "TP-ADDRESS")
        assert node.setTpAddressRef(value) is node
        assert node.getTpAddressRef() is value
        node.setTpAddressRef(None)
        assert node.getTpAddressRef() is value

    def test_type_hints_pins(self):
        assert typing.get_type_hints(FlexrayArTpNode.getConnectorRefs).get("return") == List[RefType]
        add_hints = typing.get_type_hints(FlexrayArTpNode.addConnectorRef)
        assert add_hints.get("value") == Optional[RefType]
        assert add_hints.get("return") is FlexrayArTpNode
        assert typing.get_type_hints(FlexrayArTpNode.getTpAddressRef).get("return") == Optional[RefType]
        assert typing.get_type_hints(FlexrayArTpNode.setTpAddressRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(FlexrayArTpNode.setTpAddressRef).get("return") is FlexrayArTpNode

    def test_docstrings_are_spec_note_verbatim(self):
        assert cleandoc(FlexrayArTpNode.addConnectorRef.__doc__).split("\n")[0] == self.NOTE_CONNECTOR_REFS
        assert cleandoc(FlexrayArTpNode.getConnectorRefs.__doc__) == self.NOTE_CONNECTOR_REFS
        assert cleandoc(FlexrayArTpNode.getTpAddressRef.__doc__) == self.NOTE_TP_ADDRESS_REF
        assert cleandoc(FlexrayArTpNode.setTpAddressRef.__doc__).split("\n")[0] == self.NOTE_TP_ADDRESS_REF

    def test_variation_point_capable(self):
        node = _node("Node1")
        assert node.getVariationPoint() is None
