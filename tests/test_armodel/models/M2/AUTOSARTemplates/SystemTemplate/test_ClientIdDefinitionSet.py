"""
This module contains tests for the ClientIdDefinitionSet class
in the AUTOSAR SystemTemplate module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinition, ClientIdDefinitionSet

SPEC_NOTE = "Set of Client Identifiers that are used for inter-ECU client-server communication in the System. Tags: atp.recommendedPackage=ClientIdDefinitionSets"


class TestClientIdDefinitionSet:
    def test_initialization(self):
        """Test that the concrete ClientIdDefinitionSet is an ARElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        id_definition_set = ClientIdDefinitionSet(ar_root, "TestClientIdDefinitionSet")

        assert isinstance(id_definition_set, ARElement)
        assert id_definition_set.getShortName() == "TestClientIdDefinitionSet"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 2.2)"""
        assert ClientIdDefinitionSet.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert ClientIdDefinitionSet.__init__.__doc__ is None

    def test_add_get_client_id_definitions(self):
        """Test clientIdDefinitions default, add chaining and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        id_definition_set = ClientIdDefinitionSet(ar_root, "TestDefinitions")

        assert id_definition_set.getClientIdDefinitions() == []

        id_definition = ClientIdDefinition(id_definition_set, "CID1")
        assert id_definition_set == id_definition_set.addClientIdDefinition(id_definition)
        assert id_definition_set.getClientIdDefinitions() == [id_definition]

        getter_hints = typing.get_type_hints(ClientIdDefinitionSet.getClientIdDefinitions)
        assert getter_hints.get("return") == typing.List[ClientIdDefinition]

        setter_hints = typing.get_type_hints(ClientIdDefinitionSet.addClientIdDefinition)
        assert setter_hints.get("value") is ClientIdDefinition
        assert setter_hints.get("return") is ClientIdDefinitionSet

    def test_create_client_id_definition(self):
        """Test createClientIdDefinition registers the child and returns the existing one on duplicate"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        id_definition_set = ClientIdDefinitionSet(ar_root, "TestCreate")

        created = id_definition_set.createClientIdDefinition("CID1")
        assert isinstance(created, ClientIdDefinition)
        assert created.getShortName() == "CID1"
        assert id_definition_set.getClientIdDefinitions() == [created]
        assert id_definition_set.getElement("CID1", ClientIdDefinition) is created

        duplicate = id_definition_set.createClientIdDefinition("CID1")
        assert duplicate is created
        assert len(id_definition_set.getClientIdDefinitions()) == 1
