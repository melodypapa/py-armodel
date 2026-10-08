"""
Test suite for BinaryManifestMetaDataField (CP_TPS_SystemTemplate Table 11.28, p.923, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the BinaryManifestMetaDataField model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestAddressableObject,
    BinaryManifestMetaDataField,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    VerbatimString,
)

CLASS_NOTE = "This meta-class provides the ability to define a meta-data field for the binary manifest descriptor."

SIZE_NOTE = "The value of this attribute represents the size of the meta-data field in bytes."
VALUE_NOTE = "This attribute specifies the value of the meta-data field."


class TestBinaryManifestMetaDataField:
    def test_inheritance(self):
        assert issubclass(BinaryManifestMetaDataField, BinaryManifestAddressableObject)
        assert issubclass(BinaryManifestAddressableObject, Identifiable)

    def _create_field(self) -> BinaryManifestMetaDataField:
        return BinaryManifestMetaDataField(AUTOSAR.getInstance(), "MetaDataField1")

    def test_concrete_class_instantiable(self):
        field = self._create_field()
        assert isinstance(field, BinaryManifestAddressableObject)
        assert field.getShortName() == "MetaDataField1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BinaryManifestMetaDataField.__doc__) == CLASS_NOTE

    def test_initialization(self):
        field = self._create_field()

        assert field.getShortName() == "MetaDataField1"
        assert field.getSize() is None
        assert field.getValue() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BinaryManifestMetaDataField")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("size", "Optional[PositiveInteger]"),
            ("value", "Optional[VerbatimString]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BinaryManifestMetaDataField.getSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(BinaryManifestMetaDataField.setSize).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(BinaryManifestMetaDataField.setSize).get("return") is BinaryManifestMetaDataField
        assert typing.get_type_hints(BinaryManifestMetaDataField.getValue).get("return") == typing.Optional[VerbatimString]
        assert typing.get_type_hints(BinaryManifestMetaDataField.setValue).get("value") == typing.Optional[VerbatimString]
        assert typing.get_type_hints(BinaryManifestMetaDataField.setValue).get("return") is BinaryManifestMetaDataField

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(BinaryManifestMetaDataField.getSize.__doc__) == SIZE_NOTE
        assert inspect.cleandoc(BinaryManifestMetaDataField.setSize.__doc__) == SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing size."
        assert inspect.cleandoc(BinaryManifestMetaDataField.getValue.__doc__) == VALUE_NOTE
        assert inspect.cleandoc(BinaryManifestMetaDataField.setValue.__doc__) == VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing value."

    def test_get_set_size(self):
        field = self._create_field()

        value = PositiveInteger().setValue("4096")
        assert field.setSize(value) is field
        assert field.getSize() is value
        assert field.getSize().getValue() == 4096

        assert field.setSize(None) is field
        assert field.getSize() is value

    def test_get_set_value(self):
        field = self._create_field()

        value = VerbatimString().setValue("CHECKSUM_TABLE_V1")
        assert field.setValue(value) is field
        assert field.getValue() is value
        assert field.getValue().getValue() == "CHECKSUM_TABLE_V1"

        assert field.setValue(None) is field
        assert field.getValue() is value
