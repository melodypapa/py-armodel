"""
Tests for the VariantHandling module classes.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    EvaluatedVariantSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
)




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

    def test_add_refs(self):
        variant_set = self._make()
        element_ref = RefType().setValue("/AUTOSAR/Foo")
        variant_ref = RefType().setValue("/AUTOSAR/MyVariant")

        assert variant_set.addEvaluatedElementRef(element_ref) is variant_set
        assert variant_set.addEvaluatedVariantRef(variant_ref) is variant_set
        assert variant_set.getEvaluatedElementRefs() == [element_ref]
        assert variant_set.getEvaluatedVariantRefs() == [variant_ref]
