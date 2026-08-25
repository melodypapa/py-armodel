"""
This module contains tests for the ModeInSwcBswInstanceRef abstract base class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    ModeInBswInstanceRef,
    ModeInSwcBswInstanceRef,
    ModeInSwcInstanceRef,
)


class TestModeInSwcBswInstanceRef:
    """
    Test class for ModeInSwcBswInstanceRef functionality.
    """

    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            ModeInSwcBswInstanceRef()

    def test_subclasses_are_instances(self):
        assert isinstance(ModeInBswInstanceRef(), ModeInSwcBswInstanceRef)
        assert isinstance(ModeInSwcInstanceRef(), ModeInSwcBswInstanceRef)

    def test_bsw_subclass_keeps_attrs(self):
        ref = ModeInBswInstanceRef()
        assert isinstance(ref, ModeInSwcBswInstanceRef)
        ref.setTargetModeDeclarationRef("target")
        assert ref.getTargetModeDeclarationRef() == "target"
