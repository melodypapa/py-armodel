import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import MappingConstraint
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class _ConcreteMappingConstraint(MappingConstraint):
    """Minimal concrete test double: the real subclasses ComponentClustering (Table 5.9) and ComponentSeparation (Table 5.11) are queued for their own sync passes."""

    pass


class TestMappingConstraint:
    """Test cases for MappingConstraint (Table 5.8, p.202)."""

    MEMBERS = [
        "introduction",
    ]

    def test_inheritance(self):
        assert issubclass(MappingConstraint, ARObject)
        assert issubclass(MappingConstraint, VariationPointCapable)

    def test_abstract(self):
        with pytest.raises(TypeError):
            MappingConstraint()
        constraint = _ConcreteMappingConstraint()
        assert isinstance(constraint, MappingConstraint)

    def test_class_docstring_note(self):
        expected = "Different constraints that may be used to limit the mapping of SW components to applicable ECUs, " "Partitions or Cores depending on the mappingScope attribute."
        assert inspect.cleandoc(MappingConstraint.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert MappingConstraint.__init__.__doc__ is None

    def test_initialization_defaults(self):
        constraint = _ConcreteMappingConstraint()
        assert constraint.getIntroduction() is None

    def test_member_order(self):
        constraint = _ConcreteMappingConstraint()
        members = [k for k in vars(constraint) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_introduction(self):
        constraint = _ConcreteMappingConstraint()
        block = DocumentationBlock()
        result = constraint.setIntroduction(block)
        assert result is constraint
        assert constraint.getIntroduction() is block
        constraint.setIntroduction(None)
        assert constraint.getIntroduction() is block

    def test_type_hints(self):
        hints = typing.get_type_hints(MappingConstraint.getIntroduction)
        assert hints.get("return") == typing.Optional[DocumentationBlock]
        hints = typing.get_type_hints(MappingConstraint.setIntroduction)
        assert hints.get("value") == typing.Optional[DocumentationBlock]
        assert hints.get("return") is MappingConstraint
