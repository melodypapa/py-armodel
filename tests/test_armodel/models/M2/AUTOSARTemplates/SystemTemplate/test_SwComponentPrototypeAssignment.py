"""
This module contains tests for the SwComponentPrototypeAssignment class
in the AUTOSAR SystemTemplate module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwComponentPrototypeAssignment
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef

SPEC_NOTE = "This meta-class is only required to allow for the variant modeling of an instanceRef."


class TestSwComponentPrototypeAssignment:
    def test_initialization(self):
        """Test that the SwComponentPrototypeAssignment is an ARObject with VariationPointCapable and no SHORT-NAME"""
        assignment = SwComponentPrototypeAssignment()

        assert isinstance(assignment, ARObject)
        assert isinstance(assignment, VariationPointCapable)
        assert assignment.getSwComponentIRef() is None
        assert assignment.getVariationPoint() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 11.2)"""
        assert SwComponentPrototypeAssignment.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert SwComponentPrototypeAssignment.__init__.__doc__ is None

    def test_get_set_sw_component_iref(self):
        """Test swComponentIRef default, guarded set chaining, None no-op and typing"""
        assignment = SwComponentPrototypeAssignment()

        assert assignment.getSwComponentIRef() is None

        iref = ComponentInSystemInstanceRef()
        assert assignment == assignment.setSwComponentIRef(iref)
        assert assignment.getSwComponentIRef() == iref

        assert assignment == assignment.setSwComponentIRef(None)
        assert assignment.getSwComponentIRef() == iref

        getter_hints = typing.get_type_hints(SwComponentPrototypeAssignment.getSwComponentIRef)
        assert getter_hints.get("return") == typing.Optional[ComponentInSystemInstanceRef]

        setter_hints = typing.get_type_hints(SwComponentPrototypeAssignment.setSwComponentIRef)
        assert setter_hints.get("value") == typing.Optional[ComponentInSystemInstanceRef]
        assert setter_hints.get("return") is SwComponentPrototypeAssignment
