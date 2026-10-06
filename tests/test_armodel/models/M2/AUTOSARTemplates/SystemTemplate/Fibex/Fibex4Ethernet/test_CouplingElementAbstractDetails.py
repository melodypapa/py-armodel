"""Model unit tests for CouplingElementAbstractDetails (R23-11 CP_TPS_SystemTemplate, Table 3.82, p.133).

The spec table defines no Attribute rows (abstract class; Base = ARObject,
Identifiable, MultilanguageReferrable, Referrable) — the class body stays
__init__-only and carries the atpVariation capability via VariationPointCapable.
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElementAbstractDetails,
    CouplingElementSwitchDetails,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class ConcreteDetails(CouplingElementAbstractDetails):
    pass


class TestCouplingElementAbstractDetails:
    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            CouplingElementAbstractDetails(MockParent(), "Details")

    def test_abstract_guard_message(self):
        with pytest.raises(TypeError, match="CouplingElementAbstractDetails is an abstract class."):
            CouplingElementAbstractDetails(MockParent(), "Details")

    def test_class_docstring_is_verbatim_spec_note(self):
        assert inspect.cleandoc(CouplingElementAbstractDetails.__doc__) == "Collection of specific details for the CouplingElement."

    def test_hierarchy(self):
        assert issubclass(CouplingElementAbstractDetails, Identifiable)
        assert issubclass(CouplingElementAbstractDetails, VariationPointCapable)
        assert issubclass(CouplingElementSwitchDetails, CouplingElementAbstractDetails)

    def test_no_own_members(self):
        """Table 3.82 defines no Attribute rows: no own methods beyond __init__, no own annotations."""
        own_callables = [name for name, value in vars(CouplingElementAbstractDetails).items() if callable(value) and not name.startswith("__")]
        assert own_callables == []
        assert vars(CouplingElementAbstractDetails).get("__annotations__", {}) == {}

    def test_concrete_subclass_initialization_defaults(self):
        parent = MockParent()
        details = ConcreteDetails(parent, "Details")

        assert details.getShortName() == "Details"
        assert details.getParent() is parent
        assert details.getLongName() is None
        assert details.getAdminData() is None
        assert details.getAnnotations() == []
        assert details.getCategory() is None
        assert details.getDesc() is None
        assert details.getIntroduction() is None
        assert details.getUuid() is None
        assert details.getVariationPoint() is None

    def test_builtin_concrete_subclass_instantiable(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")
        assert isinstance(details, CouplingElementAbstractDetails)
        assert details.getShortName() == "SwitchDetails"

    def test_variation_point_get_set_round_trip_and_none_noop(self):
        details = ConcreteDetails(MockParent(), "Details")

        variation_point = VariationPoint()
        assert details.setVariationPoint(variation_point) is details
        assert details.getVariationPoint() is variation_point

        assert details.setVariationPoint(None) is details
        assert details.getVariationPoint() is variation_point

    def test_base_accessors_round_trip_and_none_noop(self):
        details = ConcreteDetails(MockParent(), "Details")

        category = CategoryString().setValue("switch")
        assert details.setCategory(category) is details
        assert details.getCategory() is category

        assert details.setCategory(None) is details
        assert details.getCategory() is category

        assert details.setUuid(None) is details
