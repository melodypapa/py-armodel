import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SignalPathConstraint
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class ConcreteSignalPathConstraint(SignalPathConstraint):
    pass


class TestSignalPathConstraint:
    """Test cases for SignalPathConstraint (Table F.114)."""

    MEMBERS = [
        "introduction",
    ]

    def test_inheritance(self):
        assert issubclass(SignalPathConstraint, ARObject)

    def test_abstract(self):
        with pytest.raises(TypeError):
            SignalPathConstraint()

    def test_class_docstring_note(self):
        expected = "Additional guidelines for the System Generator, which specific way a signal between two Software Components should take in the network without defining in which frame and with which timing it is transmitted."
        assert inspect.cleandoc(SignalPathConstraint.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SignalPathConstraint.__init__.__doc__ is None

    def test_initialization_defaults(self):
        constraint = ConcreteSignalPathConstraint()
        assert constraint.getIntroduction() is None

    def test_member_order(self):
        constraint = ConcreteSignalPathConstraint()
        members = [k for k in vars(constraint) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_introduction(self):
        constraint = ConcreteSignalPathConstraint()
        block = DocumentationBlock()
        result = constraint.setIntroduction(block)
        assert result is constraint
        assert constraint.getIntroduction() is block
        constraint.setIntroduction(None)
        assert constraint.getIntroduction() is block

    def test_type_hints(self):
        hints = typing.get_type_hints(SignalPathConstraint.getIntroduction)
        assert hints["return"] == typing.Optional[DocumentationBlock]
        hints = typing.get_type_hints(SignalPathConstraint.setIntroduction)
        assert hints["value"] == typing.Optional[DocumentationBlock]
        assert hints["return"] is SignalPathConstraint
