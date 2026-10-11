"""
Test suite for BinaryManifestItemDefinition (CP_TPS_SystemTemplate Table 11.23, p.920, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the BinaryManifestItemDefinition model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestItemDefinition,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)

CLASS_NOTE = "This meta-class provides the ability to define the handle definition or an auxiliary field of a binary manifest resource."

AUXILIARY_FIELD_DEFINITION_NOTE = "This aggregation is used to define structured BinaryManifestItemDefinitions."
IS_OPTIONAL_NOTE = (
    "If true, the handle definition or auxiliary field of a binary manifest resource is optional and may not be used in all BinaryManifestResources referring to this BinaryManifestResourceDefinition."
)
SIZE_NOTE = "This attribute provides the ability to specify the size of the enclosing BinaryManifestResourceDefinition."


class TestBinaryManifestItemDefinition:
    def test_inheritance(self):
        assert issubclass(BinaryManifestItemDefinition, Identifiable)

    def _create_item_definition(self) -> BinaryManifestItemDefinition:
        return BinaryManifestItemDefinition(AUTOSAR.getInstance(), "ItemDefinition1")

    def test_concrete_class_instantiable(self):
        item_definition = self._create_item_definition()
        assert isinstance(item_definition, Identifiable)
        assert item_definition.getShortName() == "ItemDefinition1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BinaryManifestItemDefinition.__doc__) == CLASS_NOTE

    def test_initialization(self):
        item_definition = self._create_item_definition()

        assert item_definition.getShortName() == "ItemDefinition1"
        assert item_definition.getAuxiliaryFieldDefinitions() == []
        assert item_definition.getIsOptional() is None
        assert item_definition.getSize() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BinaryManifestItemDefinition")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("auxiliaryFieldDefinitions", "List[BinaryManifestItemDefinition]"),
            ("isOptional", "Optional[Boolean]"),
            ("size", "Optional[PositiveInteger]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BinaryManifestItemDefinition.createAuxiliaryFieldDefinition).get("return") is BinaryManifestItemDefinition
        assert typing.get_type_hints(BinaryManifestItemDefinition.getAuxiliaryFieldDefinitions).get("return") == typing.List[BinaryManifestItemDefinition]
        assert typing.get_type_hints(BinaryManifestItemDefinition.getIsOptional).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(BinaryManifestItemDefinition.setIsOptional).get("value") == typing.Optional[Boolean]
        assert typing.get_type_hints(BinaryManifestItemDefinition.setIsOptional).get("return") is BinaryManifestItemDefinition
        assert typing.get_type_hints(BinaryManifestItemDefinition.getSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(BinaryManifestItemDefinition.setSize).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(BinaryManifestItemDefinition.setSize).get("return") is BinaryManifestItemDefinition

    def test_member_docstrings_are_verbatim_spec_notes(self):
        note = AUXILIARY_FIELD_DEFINITION_NOTE
        assert inspect.cleandoc(BinaryManifestItemDefinition.createAuxiliaryFieldDefinition.__doc__) == note
        assert inspect.cleandoc(BinaryManifestItemDefinition.getAuxiliaryFieldDefinitions.__doc__) == note
        assert inspect.cleandoc(BinaryManifestItemDefinition.getIsOptional.__doc__) == IS_OPTIONAL_NOTE
        assert inspect.cleandoc(BinaryManifestItemDefinition.setIsOptional.__doc__) == IS_OPTIONAL_NOTE + "\n\nA None value is a no-op and does not overwrite an existing isOptional."
        assert inspect.cleandoc(BinaryManifestItemDefinition.getSize.__doc__) == SIZE_NOTE
        assert inspect.cleandoc(BinaryManifestItemDefinition.setSize.__doc__) == SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing size."

    def test_create_auxiliary_field_definition(self):
        item_definition = self._create_item_definition()

        auxiliary_field_definition = item_definition.createAuxiliaryFieldDefinition("FieldDef1")
        assert isinstance(auxiliary_field_definition, BinaryManifestItemDefinition)
        assert auxiliary_field_definition.getShortName() == "FieldDef1"
        assert auxiliary_field_definition.getParent() is item_definition
        assert [field.getShortName() for field in item_definition.getAuxiliaryFieldDefinitions()] == ["FieldDef1"]

        duplicate = item_definition.createAuxiliaryFieldDefinition("FieldDef1")
        assert duplicate is auxiliary_field_definition
        assert len(item_definition.getAuxiliaryFieldDefinitions()) == 1

    def test_get_set_is_optional(self):
        item_definition = self._create_item_definition()

        flag = Boolean().setValue("true")
        assert item_definition.setIsOptional(flag) is item_definition
        assert item_definition.getIsOptional() is flag
        assert item_definition.getIsOptional().getValue() is True

        assert item_definition.setIsOptional(None) is item_definition
        assert item_definition.getIsOptional() is flag

    def test_get_set_size(self):
        item_definition = self._create_item_definition()

        size = PositiveInteger().setValue("4096")
        assert item_definition.setSize(size) is item_definition
        assert item_definition.getSize() is size
        assert item_definition.getSize().getValue() == 4096

        assert item_definition.setSize(None) is item_definition
        assert item_definition.getSize() is size
