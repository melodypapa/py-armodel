"""
Tests for the EvaluatedVariantSet class (VariantHandling module).
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    EvaluatedVariantSet,
)

_APPROVAL_STATUS_NOTE = (
    'Defines the approval status of a predefined variant. Two values are predefined: "APPROVED" and "REJECTED": '
    "• Approved variants are known to work. • Rejected variants are known NOT to work. Further values can be approved "
    'on a per-company basis; within AUTOSAR only "APPROVED" and "REJECTED" should be recognized.'
)

_EVALUATED_ELEMENT_NOTE = (
    "This represents a particular element which is evaluated in context of the EvaluatedVariants. The approvalStatus "
    "applies to this element (and all of its descendants). In other words, the referenced elements are those that "
    "were considered when the predefined variant was evaluated."
)

_EVALUATED_VARIANT_NOTE = "This metaclass represents one particular variant which was evaluated. LowerMultiplicity is set to 0 to support a stepwise approach."


class TestEvaluatedVariantSet:
    """
    Test class for EvaluatedVariantSet functionality (Table 7.23).
    """

    def _make(self) -> EvaluatedVariantSet:
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        return ar_root.createEvaluatedVariantSet("MyEvaluatedVariantSet")

    def test_initialization(self):
        variant_set = self._make()
        assert variant_set is not None
        assert variant_set.getShortName() == "MyEvaluatedVariantSet"
        assert variant_set.getApprovalStatus() is None
        assert variant_set.getEvaluatedElementRefs() == []
        assert variant_set.getEvaluatedVariantRefs() == []

    def test_set_approval_status(self):
        variant_set = self._make()
        status = NameToken().setValue("APPROVED")
        assert variant_set.setApprovalStatus(status) is variant_set
        assert variant_set.getApprovalStatus() is status

    def test_set_approval_status_none_is_noop(self):
        variant_set = self._make()
        status = NameToken().setValue("APPROVED")
        variant_set.setApprovalStatus(status)
        variant_set.setApprovalStatus(None)
        assert variant_set.getApprovalStatus() is status

    def test_add_refs(self):
        variant_set = self._make()
        element_ref = RefType().setValue("/AUTOSAR/Foo")
        variant_ref = RefType().setValue("/AUTOSAR/MyVariant")

        assert variant_set.addEvaluatedElementRef(element_ref) is variant_set
        assert variant_set.addEvaluatedVariantRef(variant_ref) is variant_set
        assert variant_set.getEvaluatedElementRefs() == [element_ref]
        assert variant_set.getEvaluatedVariantRefs() == [variant_ref]

    def test_add_refs_ignore_none(self):
        variant_set = self._make()
        element_ref = RefType().setValue("/AUTOSAR/Foo")
        variant_ref = RefType().setValue("/AUTOSAR/MyVariant")
        variant_set.addEvaluatedElementRef(element_ref)
        variant_set.addEvaluatedVariantRef(variant_ref)

        variant_set.addEvaluatedElementRef(None)
        variant_set.addEvaluatedVariantRef(None)

        assert variant_set.getEvaluatedElementRefs() == [element_ref]
        assert variant_set.getEvaluatedVariantRefs() == [variant_ref]


class TestEvaluatedVariantSetSpecContract:
    """Table 7.23 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.257) spec contract
    for EvaluatedVariantSet."""

    def test_class_docstring_verbatim(self):
        assert EvaluatedVariantSet.__doc__.strip() == (
            "This meta class represents the ability to express if a set of ARElements is able to support one or more "
            "particular variants. In other words, for a given set of evaluatedElements this meta class represents a "
            "table of evaluated variants, where each PredefinedVariant represents one column. In this column each "
            "descendant sw SystemconstantValue resp. postbuildVariantCriterionValue represents one entry. In a "
            "graphical representation each swSystemconstantValueSet / postBuildVariantCriterionValueSet could be used "
            'as an intermediate headline in the table column. If the approvalStatus is "APPROVED" it expresses that '
            "the collection of CollectableElements is known be valid for the given evaluatedVariants. Note that the "
            "EvaluatedVariantSet is a CollectableElement. This allows to establish a hierarchy of EvaluatedVariantSets. "
            "Tags: atp.recommendedPackage=EvaluatedVariantSets"
        )

    def test_init_has_no_docstring(self):
        assert EvaluatedVariantSet.__init__.__doc__ is None

    def test_base_is_arelement(self):
        assert issubclass(EvaluatedVariantSet, ARElement)

    def test_approval_status_typed_optional_name_token(self):
        getter_hints = typing.get_type_hints(EvaluatedVariantSet.getApprovalStatus)
        assert getter_hints.get("return") == typing.Optional[NameToken]

        setter_hints = typing.get_type_hints(EvaluatedVariantSet.setApprovalStatus)
        assert setter_hints.get("value") == typing.Optional[NameToken]
        assert setter_hints.get("return") is EvaluatedVariantSet

    def test_evaluated_element_refs_typed_list_ref_type(self):
        getter_hints = typing.get_type_hints(EvaluatedVariantSet.getEvaluatedElementRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = typing.get_type_hints(EvaluatedVariantSet.addEvaluatedElementRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is EvaluatedVariantSet

    def test_evaluated_variant_refs_typed_list_ref_type(self):
        getter_hints = typing.get_type_hints(EvaluatedVariantSet.getEvaluatedVariantRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = typing.get_type_hints(EvaluatedVariantSet.addEvaluatedVariantRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is EvaluatedVariantSet

    def test_getter_docstrings_are_notes_verbatim(self):
        assert EvaluatedVariantSet.getApprovalStatus.__doc__.strip() == _APPROVAL_STATUS_NOTE
        assert EvaluatedVariantSet.getEvaluatedElementRefs.__doc__.strip() == _EVALUATED_ELEMENT_NOTE
        assert EvaluatedVariantSet.getEvaluatedVariantRefs.__doc__.strip() == _EVALUATED_VARIANT_NOTE

    def test_setter_docstrings_are_notes_with_none_noop(self):
        assert EvaluatedVariantSet.setApprovalStatus.__doc__.strip() == (_APPROVAL_STATUS_NOTE + " A None value is a no-op and does not overwrite an existing approvalStatus.")
        assert EvaluatedVariantSet.addEvaluatedElementRef.__doc__.strip() == (_EVALUATED_ELEMENT_NOTE + " A None value is a no-op and is not appended.")
        assert EvaluatedVariantSet.addEvaluatedVariantRef.__doc__.strip() == (_EVALUATED_VARIANT_NOTE + " A None value is a no-op and is not appended.")
