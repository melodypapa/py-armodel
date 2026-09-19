"""
This module contains tests for the ClientIdDefinition class
in the AUTOSAR SystemTemplate module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinition
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import OperationInSystemInstanceRef

SPEC_NOTE = "Several clients in one client-ECU can communicate via inter-ECU client-server communication with a server on a different ECU, if a client identifier is used to distinguish the different clients. The Client Identifier of the transaction handle that is used by the RTE can be defined by this element."


class TestClientIdDefinition:
    def test_initialization(self):
        """Test that the concrete ClientIdDefinition is an Identifiable wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        id_definition = ClientIdDefinition(ar_root, "TestClientIdDefinition")

        assert isinstance(id_definition, Identifiable)
        assert isinstance(id_definition, VariationPointCapable)
        assert id_definition.getShortName() == "TestClientIdDefinition"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 2.3)"""
        assert ClientIdDefinition.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert ClientIdDefinition.__init__.__doc__ is None

    def test_get_set_client_id(self):
        """Test clientId default, guarded set chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        id_definition = ClientIdDefinition(ar_root, "TestClientId")

        assert id_definition.getClientId() is None
        assert id_definition.getVariationPoint() is None

        client_id = Numerical()
        client_id.setValue("5")
        assert id_definition == id_definition.setClientId(client_id)
        assert id_definition.getClientId() == client_id

        assert id_definition == id_definition.setClientId(None)
        assert id_definition.getClientId() == client_id

        getter_hints = typing.get_type_hints(ClientIdDefinition.getClientId)
        assert getter_hints.get("return") == typing.Optional[Numerical]

        setter_hints = typing.get_type_hints(ClientIdDefinition.setClientId)
        assert setter_hints.get("value") == typing.Optional[Numerical]
        assert setter_hints.get("return") is ClientIdDefinition

    def test_get_set_client_server_operation_iref(self):
        """Test clientServerOperationIRef default, guarded set chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        id_definition = ClientIdDefinition(ar_root, "TestIRef")

        assert id_definition.getClientServerOperationIRef() is None

        iref = OperationInSystemInstanceRef()
        assert id_definition == id_definition.setClientServerOperationIRef(iref)
        assert id_definition.getClientServerOperationIRef() == iref

        assert id_definition == id_definition.setClientServerOperationIRef(None)
        assert id_definition.getClientServerOperationIRef() == iref

        getter_hints = typing.get_type_hints(ClientIdDefinition.getClientServerOperationIRef)
        assert getter_hints.get("return") == typing.Optional[OperationInSystemInstanceRef]

        setter_hints = typing.get_type_hints(ClientIdDefinition.setClientServerOperationIRef)
        assert setter_hints.get("value") == typing.Optional[OperationInSystemInstanceRef]
        assert setter_hints.get("return") is ClientIdDefinition
