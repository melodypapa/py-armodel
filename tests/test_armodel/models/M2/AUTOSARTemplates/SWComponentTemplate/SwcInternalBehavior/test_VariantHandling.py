"""
This module contains tests for the VariationPointProxy class in the
AUTOSAR SWComponentTemplate.SwcInternalBehavior module (VariantHandling.py).

Spec: R23-11 AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.61, p.613.
"""

import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import ConditionByFormula, PostBuildVariantCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
    AttributeValueVariationPoint,
    NumericalValueVariationPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy

CLASS_NOTE = (
    "The VariationPointProxy represents variation points of the C/C++ implementation. "  # noqa E501
    "In case of bindingTime = compileTime the RTE provides defines which can be used for Pre Processor directives to implement compileTime variability."  # noqa E501
)
CONDITION_ACCESS_NOTE = "This condition acts as Binding Function for the Variation Point."
IMPLEMENTATION_DATA_TYPE_NOTE = "This association to ImplementationDataType shall be taken as an implementation hint by the RTE generator."
POST_BUILD_VALUE_ACCESS_NOTE = (
    "This represents the applicable PostBuildVariantCriterion in the context of a VariationPointProxy. "  # noqa E501
    "Note that the technical details how to access the particular postBuildValueAccess are still considered internal to the RTE and are consequently not standardized."  # noqa E501
)
POST_BUILD_VARIANT_CONDITION_NOTE = "This represents that applicable PostBuoldVariant Condition in the context of aVariationPointProxy."
VALUE_ACCESS_NOTE = "This value acts as Binding Function for the VariationPoint."

FIELD_ORDER = ["conditionAccess", "implementationDataTypeRef", "postBuildValueAccessRef", "postBuildVariantConditions", "valueAccess"]
METHOD_ORDER = [
    "__init__",
    "getConditionAccess",
    "setConditionAccess",
    "getImplementationDataTypeRef",
    "setImplementationDataTypeRef",
    "getPostBuildValueAccessRef",
    "setPostBuildValueAccessRef",
    "addPostBuildVariantCondition",
    "getPostBuildVariantConditions",
    "getValueAccess",
    "setValueAccess",
]


class TestVariationPointProxy:
    def _make(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        return VariationPointProxy(ar_root, "TestVariationPointProxy")

    def test_base_shape(self):
        """Identifiable base, (parent, short_name) constructor and typed accessor signatures"""
        assert issubclass(VariationPointProxy, Identifiable)
        proxy = self._make()
        assert proxy.getShortName() == "TestVariationPointProxy"

        hints = typing.get_type_hints(VariationPointProxy.getConditionAccess)
        assert hints["return"] == typing.Optional[ConditionByFormula]
        hints = typing.get_type_hints(VariationPointProxy.setConditionAccess)
        assert hints["value"] == typing.Optional[ConditionByFormula]
        assert hints["return"] is VariationPointProxy

        hints = typing.get_type_hints(VariationPointProxy.getImplementationDataTypeRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(VariationPointProxy.setImplementationDataTypeRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is VariationPointProxy

        hints = typing.get_type_hints(VariationPointProxy.getPostBuildValueAccessRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(VariationPointProxy.setPostBuildValueAccessRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is VariationPointProxy

        hints = typing.get_type_hints(VariationPointProxy.addPostBuildVariantCondition)
        assert hints["value"] == typing.Optional[PostBuildVariantCondition]
        assert hints["return"] is VariationPointProxy
        hints = typing.get_type_hints(VariationPointProxy.getPostBuildVariantConditions)
        assert hints["return"] == typing.List[PostBuildVariantCondition]

        hints = typing.get_type_hints(VariationPointProxy.getValueAccess)
        assert hints["return"] == typing.Optional[AttributeValueVariationPoint]
        hints = typing.get_type_hints(VariationPointProxy.setValueAccess)
        assert hints["value"] == typing.Optional[AttributeValueVariationPoint]
        assert hints["return"] is VariationPointProxy

    def test_spec_notes_are_verbatim(self):
        """The class docstring and every accessor docstring is the Table 7.61 Note verbatim"""
        assert VariationPointProxy.__doc__.strip() == CLASS_NOTE
        assert VariationPointProxy.getConditionAccess.__doc__.strip() == CONDITION_ACCESS_NOTE
        assert VariationPointProxy.setConditionAccess.__doc__.strip() == (CONDITION_ACCESS_NOTE + " A None value is a no-op and does not overwrite an existing conditionAccess.")
        assert VariationPointProxy.getImplementationDataTypeRef.__doc__.strip() == IMPLEMENTATION_DATA_TYPE_NOTE
        assert VariationPointProxy.setImplementationDataTypeRef.__doc__.strip() == (
            IMPLEMENTATION_DATA_TYPE_NOTE + " A None value is a no-op and does not overwrite an existing implementationDataTypeRef."
        )
        assert VariationPointProxy.getPostBuildValueAccessRef.__doc__.strip() == POST_BUILD_VALUE_ACCESS_NOTE
        assert VariationPointProxy.setPostBuildValueAccessRef.__doc__.strip() == (POST_BUILD_VALUE_ACCESS_NOTE + " A None value is a no-op and does not overwrite an existing postBuildValueAccessRef.")
        assert VariationPointProxy.addPostBuildVariantCondition.__doc__.strip() == (POST_BUILD_VARIANT_CONDITION_NOTE + " A None value is a no-op and does not append to postBuildVariantConditions.")
        assert VariationPointProxy.getPostBuildVariantConditions.__doc__.strip() == POST_BUILD_VARIANT_CONDITION_NOTE
        assert VariationPointProxy.getValueAccess.__doc__.strip() == VALUE_ACCESS_NOTE
        assert VariationPointProxy.setValueAccess.__doc__.strip() == (VALUE_ACCESS_NOTE + " A None value is a no-op and does not overwrite an existing valueAccess.")

    def test_init_has_no_docstring(self):
        """__init__ carries no docstring (Rule 0012.2.4)"""
        assert VariationPointProxy.__init__.__doc__ is None

    def test_member_order_follows_spec_row_order(self):
        """Fields and accessor methods follow the displayed Table 7.61 row order; the list pair is mutator-first"""
        init_src = inspect.getsource(VariationPointProxy.__init__)
        fields = re.findall(r"self\.(\w+):", init_src)
        assert fields == FIELD_ORDER

        class_src = inspect.getsource(VariationPointProxy)
        methods = re.findall(r"def (\w+)\(self", class_src)
        assert methods == METHOD_ORDER

    def test_initialization(self):
        proxy = self._make()
        assert proxy.conditionAccess is None
        assert proxy.implementationDataTypeRef is None
        assert proxy.postBuildValueAccessRef is None
        assert proxy.postBuildVariantConditions == []
        assert proxy.valueAccess is None

    def test_get_set_condition_access(self):
        proxy = self._make()
        value = ConditionByFormula()
        assert proxy.setConditionAccess(value) is proxy
        assert proxy.getConditionAccess() is value
        proxy.setConditionAccess(None)
        assert proxy.getConditionAccess() is value

    def test_get_set_implementation_data_type_ref(self):
        proxy = self._make()
        value = RefType().setValue("/impl")
        assert proxy.setImplementationDataTypeRef(value) is proxy
        assert proxy.getImplementationDataTypeRef() is value
        proxy.setImplementationDataTypeRef(None)
        assert proxy.getImplementationDataTypeRef() is value

    def test_get_set_post_build_value_access_ref(self):
        proxy = self._make()
        value = RefType().setValue("/pb")
        assert proxy.setPostBuildValueAccessRef(value) is proxy
        assert proxy.getPostBuildValueAccessRef() is value
        proxy.setPostBuildValueAccessRef(None)
        assert proxy.getPostBuildValueAccessRef() is value

    def test_add_get_post_build_variant_conditions(self):
        proxy = self._make()
        first = PostBuildVariantCondition()
        second = PostBuildVariantCondition()
        assert proxy.addPostBuildVariantCondition(first) is proxy
        assert proxy.addPostBuildVariantCondition(second) is proxy
        assert proxy.getPostBuildVariantConditions() == [first, second]
        proxy.addPostBuildVariantCondition(None)
        assert proxy.getPostBuildVariantConditions() == [first, second]

    def test_get_set_value_access(self):
        proxy = self._make()
        value = NumericalValueVariationPoint()
        assert proxy.setValueAccess(value) is proxy
        assert proxy.getValueAccess() is value
        proxy.setValueAccess(None)
        assert proxy.getValueAccess() is value
