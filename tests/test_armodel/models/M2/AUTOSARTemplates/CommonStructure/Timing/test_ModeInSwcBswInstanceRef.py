"""
This module contains tests for the ModeInSwcBswInstanceRef abstract base class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.

Spec basis: XSD-only class (no own AUTOSAR table in either corpus) — derived from the
MODE-IN-SWC-BSW-INSTANCE-REF group (AUTOSAR_00052.xsd line 82683): abstract, atpObject,
empty sequence (no own attributes), never serialized directly.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    ModeInBswInstanceRef,
    ModeInSwcBswInstanceRef,
    ModeInSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

XSD_DOCUMENTATION = "Abstract class representing an instance reference to be capable of referencing a specific ModeDeclaration utilized by a SW-C or BSW module."


class TestModeInSwcBswInstanceRef:
    """
    Test class for ModeInSwcBswInstanceRef functionality.
    """

    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            ModeInSwcBswInstanceRef()

    def test_is_abstract_subclass_of_ar_object(self):
        assert issubclass(ModeInSwcBswInstanceRef, ARObject)
        assert issubclass(ModeInSwcBswInstanceRef, ModeInSwcBswInstanceRef)

    def test_subclasses_are_instances(self):
        assert isinstance(ModeInBswInstanceRef(), ModeInSwcBswInstanceRef)
        assert isinstance(ModeInSwcInstanceRef(), ModeInSwcBswInstanceRef)

    def test_class_docstring_verbatim_xsd_documentation(self):
        assert ModeInSwcBswInstanceRef.__doc__.strip() == XSD_DOCUMENTATION

    def test_init_has_no_docstring(self):
        assert ModeInSwcBswInstanceRef.__init__.__doc__ is None

    def test_no_own_attributes(self):
        class _Probe(ModeInSwcBswInstanceRef):
            pass

        probe = _Probe()
        assert set(vars(probe).keys()) == {"parent", "checksum", "timestamp"}
