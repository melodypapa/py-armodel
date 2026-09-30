"""
Tests for the SpecialDataDef module (SdgDef family, Tables 4.24-4.35).
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    FullBindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Limit,
    NameToken,
    PositiveInteger,
    RefType,
    RegularExpression,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef import (
    SdgAbstractForeignReference,
    SdgAbstractPrimitiveAttribute,
    SdgAggregationWithVariation,
    SdgAttribute,
    SdgClass,
    SdgDef,
    SdgElementWithGid,
    SdgForeignReference,
    SdgForeignReferenceWithVariation,
    SdgPrimitiveAttribute,
    SdgPrimitiveAttributeWithVariation,
    SdgReference,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _make_sdg_def() -> SdgDef:
    root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return root.createSdgDef("MySdgDef")


class TestAbstractRejection:
    """
    The abstract classes of the family reject direct instantiation.
    """

    def test_rejections(self):
        # SdgElementWithGid is mixin-style (class-level gid default, VariationPointCapable
        # pattern) and therefore has no instantiation guard.
        with pytest.raises(TypeError):
            SdgAttribute(None, "A")
        with pytest.raises(TypeError):
            SdgAbstractPrimitiveAttribute(None, "A")
        with pytest.raises(TypeError):
            SdgAbstractForeignReference(None, "A")


class TestSdgDef:
    """
    Test class for SdgDef functionality (Table 4.24).
    """

    def test_initialization(self):
        sdg_def = _make_sdg_def()
        assert sdg_def is not None
        assert sdg_def.getShortName() == "MySdgDef"
        assert sdg_def.getSdgClasses() == []

    def test_add_sdg_class(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        assert sdg_def.addSdgClass(sdg_class) is sdg_def
        assert sdg_def.getSdgClasses() == [sdg_class]


class TestSdgClass:
    """
    Test class for SdgClass functionality (Table 4.26).
    """

    def test_initialization(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        assert sdg_class.getExtendsMetaClass() is None
        assert sdg_class.getCaption() is None
        assert sdg_class.getAttributes() == []
        assert sdg_class.getSdgConstraintRefs() == []

    def test_members(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        assert sdg_class.setExtendsMetaClass("ArPackage") is sdg_class
        assert sdg_class.getExtendsMetaClass() == "ArPackage"
        caption = Boolean().setValue(True)
        assert sdg_class.setCaption(caption) is sdg_class
        assert sdg_class.getCaption() is caption
        assert sdg_class.setGid(NameToken().setValue("MY-GID")) is sdg_class
        assert sdg_class.getGid().getValue() == "MY-GID"

    def test_add_attribute(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        attribute = SdgPrimitiveAttribute(sdg_class, "Attr")
        assert sdg_class.addAttribute(attribute) is sdg_class
        assert sdg_class.getAttributes() == [attribute]

    def test_add_sdg_constraint_ref(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        ref = RefType().setValue("/AUTOSAR/Constraint")
        assert sdg_class.addSdgConstraintRef(ref) is sdg_class
        assert sdg_class.getSdgConstraintRefs() == [ref]


class TestSdgAttributes:
    """
    Test the concrete Sdg attribute classes (Tables 4.28-4.35).
    """

    def test_sdg_primitive_attribute(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        attribute = SdgPrimitiveAttribute(sdg_class, "Attr")
        assert attribute.setGid(NameToken().setValue("ATTR-GID")) is attribute
        assert attribute.setMax(Limit().setValue("10.0")) is attribute
        assert attribute.setMaxLength(PositiveInteger().setValue(5)) is attribute
        assert attribute.setPattern(RegularExpression().setValue("[0-9]+")) is attribute
        assert attribute.getMax().getValue() == "10.0"
        assert attribute.getGid().getValue() == "ATTR-GID"

    def test_sdg_primitive_attribute_with_variation(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        attribute = SdgPrimitiveAttributeWithVariation(sdg_class, "Attr")
        assert attribute.addValidBindingTime(FullBindingTimeEnum().setValue(FullBindingTimeEnum.POST_BUILD)) is attribute
        assert len(attribute.getValidBindingTimes()) == 1

    def test_sdg_aggregation_with_variation(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        attribute = SdgAggregationWithVariation(sdg_class, "Agg")
        ref = RefType().setValue("/AUTOSAR/MySdgDef/TargetClass")
        assert attribute.setSubSdgRef(ref) is attribute
        assert attribute.getSubSdgRef() is ref

    def test_sdg_reference(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        attribute = SdgReference(sdg_class, "Ref")
        ref = RefType().setValue("/AUTOSAR/MySdgDef/DestClass")
        assert attribute.setDestSdgRef(ref) is attribute
        assert attribute.getDestSdgRef() is ref

    def test_sdg_foreign_references(self):
        sdg_def = _make_sdg_def()
        sdg_class = SdgClass(sdg_def, "MySdgClass")
        attribute = SdgForeignReference(sdg_class, "FRef")
        assert attribute.setDestMetaClass("ArPackage") is attribute
        assert attribute.getDestMetaClass() == "ArPackage"

        wv = SdgForeignReferenceWithVariation(sdg_class, "FRefWV")
        wv.setDestMetaClass("ARPackage")
        wv.setVariation(Boolean().setValue(False))
        assert wv.getVariation().getValue() is False
