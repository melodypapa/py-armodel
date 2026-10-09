"""
This module contains tests for the FMAttributeValue class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, RefType


class TestFMAttributeValue:
    """
    Test class for FMAttributeValue functionality.
    """

    def test_initialization(self):
        obj = FMAttributeValue()
        assert isinstance(obj, FMAttributeValue)
        assert obj.getDefinitionRef() is None
        assert obj.getValue() is None

    def test_get_set_definition_ref(self):
        obj = FMAttributeValue()
        ref = RefType().setValue("/Pkg/FMAttributeDef").setDest("FM-ATTRIBUTE-DEF")
        assert obj.setDefinitionRef(ref) is obj
        assert obj.getDefinitionRef() is ref
        assert obj.getDefinitionRef().getValue() == "/Pkg/FMAttributeDef"

    def test_set_definition_ref_none_noop(self):
        obj = FMAttributeValue()
        ref = RefType().setValue("/Pkg/FMAttributeDef").setDest("FM-ATTRIBUTE-DEF")
        obj.setDefinitionRef(ref)
        assert obj.setDefinitionRef(None) is obj
        assert obj.getDefinitionRef() is ref

    def test_get_set_value(self):
        obj = FMAttributeValue()
        numerical = Numerical()
        numerical.setValue(1.5)
        assert obj.setValue(numerical) is obj
        assert obj.getValue() is numerical

    def test_set_value_none_noop(self):
        obj = FMAttributeValue()
        numerical = Numerical()
        numerical.setValue(1.5)
        obj.setValue(numerical)
        assert obj.setValue(None) is obj
        assert obj.getValue() is numerical
