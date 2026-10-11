"""
Test suite for BinaryManifestItem (CP_TPS_SystemTemplate Table 11.22, p.919, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the BinaryManifestItem model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    BinaryManifestItemNumericalValue,
    BinaryManifestItemPointerValue,
    BinaryManifestItemValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestAddressableObject,
    BinaryManifestItem,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Numerical,
)

CLASS_NOTE = "This meta-class represents the ability to describe a specific handle or auxiliary field in the context of binary manifest resource."

AUXILIARY_FIELD_NOTE = "This aggregation is used to define structured BinaryManifestItems. Tags: xml.sequenceOffset=20"
DEFAULT_VALUE_NOTE = "This aggregation represents the definition of a default value for a binary manifest handle or an auxiliaryField. This value shall be taken if no connection for this resource is possible. Tags: xml.sequenceOffset=10"
IS_UNUSED_NOTE = "If true, the handle or auxiliary field in the context of binary manifest resource relates to an optional BinaryManifestItemDefinition and is not used."
VALUE_NOTE = "This aggregation represents the definition of a value for a binary manifest handle or an auxiliaryField. This value shall be taken to establish a connection."


class TestBinaryManifestItem:
    def test_inheritance(self):
        assert issubclass(BinaryManifestItem, BinaryManifestAddressableObject)
        assert issubclass(BinaryManifestAddressableObject, Identifiable)

    def _create_item(self) -> BinaryManifestItem:
        return BinaryManifestItem(AUTOSAR.getInstance(), "Item1")

    def test_concrete_class_instantiable(self):
        item = self._create_item()
        assert isinstance(item, BinaryManifestAddressableObject)
        assert item.getShortName() == "Item1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BinaryManifestItem.__doc__) == CLASS_NOTE

    def test_initialization(self):
        item = self._create_item()

        assert item.getShortName() == "Item1"
        assert item.getAuxiliaryFields() == []
        assert item.getDefaultValue() is None
        assert item.getIsUnused() is None
        assert item.getValue() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BinaryManifestItem")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("auxiliaryFields", "List[BinaryManifestItem]"),
            ("defaultValue", "Optional[BinaryManifestItemValue]"),
            ("isUnused", "Optional[Boolean]"),
            ("value", "Optional[BinaryManifestItemValue]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BinaryManifestItem.createAuxiliaryField).get("return") is BinaryManifestItem
        assert typing.get_type_hints(BinaryManifestItem.getAuxiliaryFields).get("return") == typing.List[BinaryManifestItem]
        assert typing.get_type_hints(BinaryManifestItem.getDefaultValue).get("return") == typing.Optional[BinaryManifestItemValue]
        assert typing.get_type_hints(BinaryManifestItem.setDefaultValue).get("value") == typing.Optional[BinaryManifestItemValue]
        assert typing.get_type_hints(BinaryManifestItem.setDefaultValue).get("return") is BinaryManifestItem
        assert typing.get_type_hints(BinaryManifestItem.getIsUnused).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(BinaryManifestItem.setIsUnused).get("value") == typing.Optional[Boolean]
        assert typing.get_type_hints(BinaryManifestItem.setIsUnused).get("return") is BinaryManifestItem
        assert typing.get_type_hints(BinaryManifestItem.getValue).get("return") == typing.Optional[BinaryManifestItemValue]
        assert typing.get_type_hints(BinaryManifestItem.setValue).get("value") == typing.Optional[BinaryManifestItemValue]
        assert typing.get_type_hints(BinaryManifestItem.setValue).get("return") is BinaryManifestItem

    def test_member_docstrings_are_verbatim_spec_notes(self):
        note = AUXILIARY_FIELD_NOTE
        assert inspect.cleandoc(BinaryManifestItem.createAuxiliaryField.__doc__) == note
        assert inspect.cleandoc(BinaryManifestItem.getAuxiliaryFields.__doc__) == note
        assert inspect.cleandoc(BinaryManifestItem.getDefaultValue.__doc__) == DEFAULT_VALUE_NOTE
        assert inspect.cleandoc(BinaryManifestItem.setDefaultValue.__doc__) == DEFAULT_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing defaultValue."
        assert inspect.cleandoc(BinaryManifestItem.getIsUnused.__doc__) == IS_UNUSED_NOTE
        assert inspect.cleandoc(BinaryManifestItem.setIsUnused.__doc__) == IS_UNUSED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing isUnused."
        assert inspect.cleandoc(BinaryManifestItem.getValue.__doc__) == VALUE_NOTE
        assert inspect.cleandoc(BinaryManifestItem.setValue.__doc__) == VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing value."

    def test_create_auxiliary_field(self):
        item = self._create_item()

        auxiliary_field = item.createAuxiliaryField("Field1")
        assert isinstance(auxiliary_field, BinaryManifestItem)
        assert auxiliary_field.getShortName() == "Field1"
        assert auxiliary_field.getParent() is item
        assert [field.getShortName() for field in item.getAuxiliaryFields()] == ["Field1"]

        duplicate = item.createAuxiliaryField("Field1")
        assert duplicate is auxiliary_field
        assert len(item.getAuxiliaryFields()) == 1

    def test_get_set_default_value(self):
        item = self._create_item()

        value = BinaryManifestItemNumericalValue()
        value.setValue(Numerical().setValue("4096"))
        assert item.setDefaultValue(value) is item
        assert item.getDefaultValue() is value
        assert item.getDefaultValue().getValue().getValue() == 4096

        assert item.setDefaultValue(None) is item
        assert item.getDefaultValue() is value

    def test_get_set_is_unused(self):
        item = self._create_item()

        flag = Boolean().setValue("true")
        assert item.setIsUnused(flag) is item
        assert item.getIsUnused() is flag
        assert item.getIsUnused().getValue() is True

        assert item.setIsUnused(None) is item
        assert item.getIsUnused() is flag

    def test_get_set_value(self):
        item = self._create_item()

        value = BinaryManifestItemPointerValue()
        assert item.setValue(value) is item
        assert item.getValue() is value

        assert item.setValue(None) is item
        assert item.getValue() is value
