"""
Test suite for BinaryManifestResourceDefinition (CP_TPS_SystemTemplate Table 11.21, p.917, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the BinaryManifestResourceDefinition model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestItemDefinition,
    BinaryManifestResourceDefinition,
    Identifiable,
)

CLASS_NOTE = "This meta-class represents the ability to specify a resource definition that provides information that can be shared by all resources that refer to the respective resource definition."

ITEM_DEFINITION_NOTE = "This aggregation specifies the collection of handle definitions in the context of the enclosing binary manifest resource definitions."


class TestBinaryManifestResourceDefinition:
    def test_inheritance(self):
        assert issubclass(BinaryManifestResourceDefinition, Identifiable)

    def _create_resource_definition(self) -> BinaryManifestResourceDefinition:
        return BinaryManifestResourceDefinition(AUTOSAR.getInstance(), "ResourceDefinition1")

    def test_concrete_class_instantiable(self):
        resource_definition = self._create_resource_definition()
        assert isinstance(resource_definition, Identifiable)
        assert resource_definition.getShortName() == "ResourceDefinition1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BinaryManifestResourceDefinition.__doc__) == CLASS_NOTE

    def test_initialization(self):
        resource_definition = self._create_resource_definition()

        assert resource_definition.getShortName() == "ResourceDefinition1"
        assert resource_definition.getItemDefinitions() == []

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BinaryManifestResourceDefinition")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("itemDefinitions", "List[BinaryManifestItemDefinition]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BinaryManifestResourceDefinition.createItemDefinition).get("return") is BinaryManifestItemDefinition
        assert typing.get_type_hints(BinaryManifestResourceDefinition.getItemDefinitions).get("return") == typing.List[BinaryManifestItemDefinition]

    def test_member_docstrings_are_verbatim_spec_notes(self):
        note = ITEM_DEFINITION_NOTE
        assert inspect.cleandoc(BinaryManifestResourceDefinition.createItemDefinition.__doc__) == note
        assert inspect.cleandoc(BinaryManifestResourceDefinition.getItemDefinitions.__doc__) == note

    def test_create_item_definition(self):
        resource_definition = self._create_resource_definition()

        item_definition = resource_definition.createItemDefinition("ItemDef1")
        assert isinstance(item_definition, BinaryManifestItemDefinition)
        assert item_definition.getShortName() == "ItemDef1"
        assert item_definition.getParent() is resource_definition
        assert [item.getShortName() for item in resource_definition.getItemDefinitions()] == ["ItemDef1"]

        duplicate = resource_definition.createItemDefinition("ItemDef1")
        assert duplicate is item_definition
        assert len(resource_definition.getItemDefinitions()) == 1
