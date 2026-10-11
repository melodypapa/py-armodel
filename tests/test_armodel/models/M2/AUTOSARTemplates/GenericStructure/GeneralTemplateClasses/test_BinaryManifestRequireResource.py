"""
Test suite for BinaryManifestRequireResource (CP_TPS_SystemTemplate Table 11.20, p.916, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note, the member declaration order (markdown
displayed row order) and the inherited BinaryManifestResource base accessors
of the BinaryManifestRequireResource model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestItem,
    BinaryManifestRequireResource,
    BinaryManifestResource,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)

CLASS_NOTE = "This meta-class represents a required resource in the binary manifest."

CONNECTION_IS_MANDATORY_NOTE = "This attribute indicates whether the connection of the enclosing BinaryManifestResource is mandatory."


class TestBinaryManifestRequireResource:
    def test_inheritance(self):
        assert issubclass(BinaryManifestRequireResource, BinaryManifestResource)
        assert issubclass(BinaryManifestRequireResource, Identifiable)

    def _create_require_resource(self) -> BinaryManifestRequireResource:
        return BinaryManifestRequireResource(AUTOSAR.getInstance(), "RequireResource1")

    def test_concrete_class_instantiable(self):
        require_resource = self._create_require_resource()
        assert isinstance(require_resource, BinaryManifestResource)
        assert require_resource.getShortName() == "RequireResource1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BinaryManifestRequireResource.__doc__) == CLASS_NOTE

    def test_initialization(self):
        require_resource = self._create_require_resource()

        assert require_resource.getShortName() == "RequireResource1"
        assert require_resource.getConnectionIsMandatory() is None
        assert require_resource.getItems() == []

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BinaryManifestRequireResource")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("connectionIsMandatory", "Optional[Boolean]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BinaryManifestRequireResource.getConnectionIsMandatory).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(BinaryManifestRequireResource.setConnectionIsMandatory).get("return") is BinaryManifestRequireResource

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(BinaryManifestRequireResource.getConnectionIsMandatory.__doc__) == CONNECTION_IS_MANDATORY_NOTE
        setter_docstring = inspect.cleandoc(BinaryManifestRequireResource.setConnectionIsMandatory.__doc__)
        assert setter_docstring.startswith(CONNECTION_IS_MANDATORY_NOTE)
        assert setter_docstring == CONNECTION_IS_MANDATORY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing connectionIsMandatory."

    def test_get_set_connection_is_mandatory(self):
        require_resource = self._create_require_resource()

        result = require_resource.setConnectionIsMandatory(Boolean().setValue("true"))
        assert result is require_resource
        assert require_resource.getConnectionIsMandatory().getValue() is True

        require_resource.setConnectionIsMandatory(None)
        assert require_resource.getConnectionIsMandatory().getValue() is True

    def test_inherited_base_accessors(self):
        require_resource = self._create_require_resource()

        require_resource.setGlobalResourceId(PositiveInteger().setValue("1"))
        assert require_resource.getGlobalResourceId().getValue() == 1

        item = require_resource.createItem("Item1")
        assert isinstance(item, BinaryManifestItem)
        assert [element.getShortName() for element in require_resource.getItems()] == ["Item1"]

        duplicate = require_resource.createItem("Item1")
        assert duplicate is item
        assert len(require_resource.getItems()) == 1
