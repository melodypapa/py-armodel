"""
Test suite for BinaryManifestProvideResource (CP_TPS_SystemTemplate Table 11.18, p.914, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note, the member declaration order (markdown
displayed row order) and the inherited BinaryManifestResource base accessors
of the BinaryManifestProvideResource model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestItem,
    BinaryManifestProvideResource,
    BinaryManifestResource,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)

CLASS_NOTE = "This meta-class represents a provided resource in the binary manifest."

NUMBER_OF_NOTIFIER_SETS_NOTE = "This attribute provides an upper limit for the number of notifiers for this resource."

SUPPORTS_MULTIPLE_NOTIFIER_SETS_NOTE = "This attribute indicates whether the enclosing BinaryManifestResource supports multiple notifiers sets."


class TestBinaryManifestProvideResource:
    def test_inheritance(self):
        assert issubclass(BinaryManifestProvideResource, BinaryManifestResource)
        assert issubclass(BinaryManifestProvideResource, Identifiable)

    def _create_provide_resource(self) -> BinaryManifestProvideResource:
        return BinaryManifestProvideResource(AUTOSAR.getInstance(), "ProvideResource1")

    def test_concrete_class_instantiable(self):
        provide_resource = self._create_provide_resource()
        assert isinstance(provide_resource, BinaryManifestResource)
        assert provide_resource.getShortName() == "ProvideResource1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BinaryManifestProvideResource.__doc__) == CLASS_NOTE

    def test_initialization(self):
        provide_resource = self._create_provide_resource()

        assert provide_resource.getShortName() == "ProvideResource1"
        assert provide_resource.getNumberOfNotifierSets() is None
        assert provide_resource.getSupportsMultipleNotifierSets() is None
        assert provide_resource.getItems() == []

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BinaryManifestProvideResource")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("numberOfNotifierSets", "Optional[PositiveInteger]"),
            ("supportsMultipleNotifierSets", "Optional[Boolean]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BinaryManifestProvideResource.getNumberOfNotifierSets).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(BinaryManifestProvideResource.setNumberOfNotifierSets).get("return") is BinaryManifestProvideResource
        assert typing.get_type_hints(BinaryManifestProvideResource.getSupportsMultipleNotifierSets).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(BinaryManifestProvideResource.setSupportsMultipleNotifierSets).get("return") is BinaryManifestProvideResource

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(BinaryManifestProvideResource.getNumberOfNotifierSets.__doc__) == NUMBER_OF_NOTIFIER_SETS_NOTE
        setter_docstring = inspect.cleandoc(BinaryManifestProvideResource.setNumberOfNotifierSets.__doc__)
        assert setter_docstring.startswith(NUMBER_OF_NOTIFIER_SETS_NOTE)
        assert setter_docstring == NUMBER_OF_NOTIFIER_SETS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing numberOfNotifierSets."
        assert inspect.cleandoc(BinaryManifestProvideResource.getSupportsMultipleNotifierSets.__doc__) == SUPPORTS_MULTIPLE_NOTIFIER_SETS_NOTE
        setter_docstring = inspect.cleandoc(BinaryManifestProvideResource.setSupportsMultipleNotifierSets.__doc__)
        assert setter_docstring.startswith(SUPPORTS_MULTIPLE_NOTIFIER_SETS_NOTE)
        assert setter_docstring == SUPPORTS_MULTIPLE_NOTIFIER_SETS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing supportsMultipleNotifierSets."

    def test_get_set_number_of_notifier_sets(self):
        provide_resource = self._create_provide_resource()

        result = provide_resource.setNumberOfNotifierSets(PositiveInteger().setValue("4"))
        assert result is provide_resource
        assert provide_resource.getNumberOfNotifierSets().getValue() == 4

        provide_resource.setNumberOfNotifierSets(None)
        assert provide_resource.getNumberOfNotifierSets().getValue() == 4

    def test_get_set_supports_multiple_notifier_sets(self):
        provide_resource = self._create_provide_resource()

        result = provide_resource.setSupportsMultipleNotifierSets(Boolean().setValue("true"))
        assert result is provide_resource
        assert provide_resource.getSupportsMultipleNotifierSets().getValue() is True

        provide_resource.setSupportsMultipleNotifierSets(None)
        assert provide_resource.getSupportsMultipleNotifierSets().getValue() is True

    def test_inherited_base_accessors(self):
        provide_resource = self._create_provide_resource()

        provide_resource.setGlobalResourceId(PositiveInteger().setValue("1"))
        assert provide_resource.getGlobalResourceId().getValue() == 1

        item = provide_resource.createItem("Item1")
        assert isinstance(item, BinaryManifestItem)
        assert [element.getShortName() for element in provide_resource.getItems()] == ["Item1"]

        duplicate = provide_resource.createItem("Item1")
        assert duplicate is item
        assert len(provide_resource.getItems()) == 1
