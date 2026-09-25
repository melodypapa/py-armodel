from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeDef,
    HwAttributeLiteralDef,
    HwAttributeValue,
    HwCategory,
    HwType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Numerical,
    RefType,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.MSR.Documentation.Annotation import Annotation


def make_ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


"""
Test cases for the HwElementCategory module.
These tests ensure 100% code coverage for the HwType, HwAttributeDef, and HwCategory classes.
"""


def test_hw_type_init():
    """
    Test initialization of HwType class.

    Test Steps:
    1. Create a HwType instance with parent and short_name
    2. Verify basic attributes are set correctly
    """
    # Create a mock parent object
    parent = object()

    # Initialize HwType
    hw_type = HwType(parent, "test_hw_type")

    # Verify initial values
    assert hw_type.parent == parent
    assert hw_type.short_name == "test_hw_type"


def test_hw_type_is_concrete():
    """HwType must be instantiable although its base HwDescriptionEntity is abstract."""
    parent = object()
    hw_type = HwType(parent, "concrete_hw_type")
    assert isinstance(hw_type, HwType)


def test_hw_type_inherited_members_round_trip():
    """
    HwType inherits the HwDescriptionEntity aggregations/associations. Verify they
    round-trip through a HwType instance (herit/marker-subclass behavior).
    """
    hw_type = HwType(None, "typed")

    attr_value = HwAttributeValue()
    attr_value.setHwAttributeDefRef(make_ref("/Hw/Cat/AttrDef", "HW-ATTRIBUTE-DEF")).setVt("v")
    hw_type.addHwAttributeValue(attr_value)
    assert hw_type.getHwAttributeValues() == [attr_value]

    hw_type.addHwCategoryRef("cat_ref_a")
    hw_type.addHwCategoryRef("cat_ref_b")
    assert hw_type.getHwCategoryRefs() == ["cat_ref_a", "cat_ref_b"]

    return_value = hw_type.setHwTypeRef("type_ref")
    assert return_value == hw_type  # method chaining
    assert hw_type.getHwTypeRef() == "type_ref"


def test_hw_type_inherited_members_none_noop():
    """Setters inherited from HwDescriptionEntity must ignore None (no-op)."""
    hw_type = HwType(None, "typed")

    original_refs = hw_type.getHwCategoryRefs()
    hw_type.addHwCategoryRef(None)
    assert hw_type.getHwCategoryRefs() == original_refs

    hw_type.setHwTypeRef("type_ref")
    original_type_ref = hw_type.getHwTypeRef()
    hw_type.setHwTypeRef(None)
    assert hw_type.getHwTypeRef() == original_type_ref


HW_ATTRIBUTE_DEF_NOTE = (
    "This metaclass represents the ability to define a particular hardware attribute. "
    "The category of this element defines the type of the attributeValue. "
    "If the category is Enumeration the hwAttributeEnumerationLiterals specify the available literals."
)


def test_hw_attribute_def_docstring_verbatim():
    """Class docstring must equal the Table 2.13 Note verbatim (XSD authoritative)."""
    assert HwAttributeDef.__doc__.strip() == HW_ATTRIBUTE_DEF_NOTE


def test_hw_attribute_def_init_doc_is_none():
    assert HwAttributeDef.__init__.__doc__ is None


def test_hw_attribute_def_is_concrete_identifiable_subclass():
    hw_attr_def = HwAttributeDef(None, "attr_def")
    assert isinstance(hw_attr_def, HwAttributeDef)
    assert issubclass(HwAttributeDef, Identifiable)


def test_hw_attribute_def_defaults():
    """
    Test initialization of HwAttributeDef class (Table 2.13 displayed order:
    hwAttributeLiteral (* aggr), isRequired (0..1 attr), unit (0..1 ref)).
    """
    parent = object()
    hw_attr_def = HwAttributeDef(parent, "test_hw_attr_def")

    assert hw_attr_def.parent == parent
    assert hw_attr_def.short_name == "test_hw_attr_def"
    assert hw_attr_def.hwAttributeLiterals == []
    assert hw_attr_def.isRequired is None
    assert hw_attr_def.unitRef is None


def test_hw_attribute_def_setters_round_trip():
    """Get/set round-trips must return the same instance and support chaining."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    required = Boolean()
    required.setValue(True)
    assert hw_attr_def.setIsRequired(required) is hw_attr_def
    assert hw_attr_def.getIsRequired() is required

    unit_ref = make_ref("/Units/Length", "UNIT")
    assert hw_attr_def.setUnitRef(unit_ref) is hw_attr_def
    assert hw_attr_def.getUnitRef() is unit_ref

    literals = [HwAttributeLiteralDef(None, "literal1"), HwAttributeLiteralDef(None, "literal2")]
    assert hw_attr_def.setHwAttributeLiterals(literals) is hw_attr_def
    assert hw_attr_def.getHwAttributeLiterals() is literals


def test_hw_attribute_def_setters_none_noop():
    """A None value is a no-op and does not overwrite an existing value."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    required = Boolean()
    required.setValue(True)
    hw_attr_def.setIsRequired(required)
    hw_attr_def.setIsRequired(None)
    assert hw_attr_def.getIsRequired() is required

    unit_ref = make_ref("/Units/Length", "UNIT")
    hw_attr_def.setUnitRef(unit_ref)
    hw_attr_def.setUnitRef(None)
    assert hw_attr_def.getUnitRef() is unit_ref

    literals = [HwAttributeLiteralDef(None, "literal1")]
    hw_attr_def.setHwAttributeLiterals(literals)
    hw_attr_def.setHwAttributeLiterals(None)
    assert hw_attr_def.getHwAttributeLiterals() is literals


def test_hw_attribute_def_add_hw_attribute_literal():
    """The * add accessor must append, ignore None and return self."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    literal1 = HwAttributeLiteralDef(None, "literal1")
    assert hw_attr_def.addHwAttributeLiteral(literal1) is hw_attr_def
    assert hw_attr_def.getHwAttributeLiterals() == [literal1]

    literal2 = HwAttributeLiteralDef(None, "literal2")
    hw_attr_def.addHwAttributeLiteral(literal2)
    assert hw_attr_def.getHwAttributeLiterals() == [literal1, literal2]

    hw_attr_def.addHwAttributeLiteral(None)
    assert hw_attr_def.getHwAttributeLiterals() == [literal1, literal2]


def test_hw_attribute_def_create_hw_attribute_literal():
    """createHwAttributeLiteral must guard duplicates via IsElementExists."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    literal = hw_attr_def.createHwAttributeLiteral("literal1")
    assert literal.short_name == "literal1"
    assert literal in hw_attr_def.getHwAttributeLiterals()

    assert hw_attr_def.createHwAttributeLiteral("literal1") is literal
    assert len(hw_attr_def.getHwAttributeLiterals()) == 1


HW_CATEGORY_NOTE = "This metaclass represents the ability to declare hardware categories and its particular attributes. " "Tags: atp.recommendedPackage=HwCategorys"


def test_hw_category_docstring_verbatim():
    """Class docstring must equal the Table 2.11 Note verbatim."""
    assert HwCategory.__doc__.strip() == HW_CATEGORY_NOTE


def test_hw_category_init_doc_is_none():
    assert HwCategory.__init__.__doc__ is None


def test_hw_category_is_concrete_arelement_subclass():
    """Base closure (ARElement, AtpDefinition, CollectableElement, ...) collapses to ARElement."""
    hw_category = HwCategory(None, "cat")
    assert isinstance(hw_category, HwCategory)
    assert issubclass(HwCategory, ARElement)
    assert issubclass(HwCategory, Identifiable)
    assert issubclass(HwCategory, CollectableElement)


def test_hw_category_defaults():
    """Table 2.11 single attribute: hwAttributeDef (HwAttributeDef, * aggr)."""
    parent = object()
    hw_category = HwCategory(parent, "test_hw_category")

    assert hw_category.parent == parent
    assert hw_category.short_name == "test_hw_category"
    assert hw_category.hwAttributeDefs == []


def test_hw_category_add_hw_attribute_def():
    """The * add accessor must append, ignore None and return self."""
    hw_category = HwCategory(None, "test_hw_category")

    attr_def1 = HwAttributeDef(None, "attr_def1")
    assert hw_category.addHwAttributeDef(attr_def1) is hw_category
    assert hw_category.getHwAttributeDefs() == [attr_def1]

    attr_def2 = HwAttributeDef(None, "attr_def2")
    hw_category.addHwAttributeDef(attr_def2)
    assert hw_category.getHwAttributeDefs() == [attr_def1, attr_def2]

    hw_category.addHwAttributeDef(None)
    assert hw_category.getHwAttributeDefs() == [attr_def1, attr_def2]


def test_hw_category_create_hw_attribute_def():
    """createHwAttributeDef must guard duplicates via IsElementExists."""
    hw_category = HwCategory(None, "test_hw_category")

    attr_def = hw_category.createHwAttributeDef("attr_def1")
    assert attr_def.short_name == "attr_def1"
    assert attr_def in hw_category.getHwAttributeDefs()

    assert hw_category.createHwAttributeDef("attr_def1") is attr_def
    assert len(hw_category.getHwAttributeDefs()) == 1


"""
Test cases for the HwAttributeValue and HwAttributeLiteralDef classes
(AUTOSAR_CP_TPS_ECUResourceTemplate Table 2.2 p.16 and Table 2.14 p.26).
"""

HW_ATTRIBUTE_VALUE_NOTE = "This metaclass represents the ability to assign a hardware attribute value. " "Note that v and vt are mutually exclusive."

HW_ATTRIBUTE_LITERAL_DEF_NOTE = "One available EnumerationLiteral of the Enumeration definition. " "Only applicable if the category of the HwAttributeDef equals Enumeration."


def test_hw_attribute_value_docstring_verbatim():
    """Class docstring must equal the Table 2.2 Note verbatim (XSD authoritative)."""
    assert HwAttributeValue.__doc__.strip() == HW_ATTRIBUTE_VALUE_NOTE


def test_hw_attribute_value_init_doc_is_none():
    assert HwAttributeValue.__init__.__doc__ is None


def test_hw_attribute_value_is_concrete_arobject_subclass():
    """Base per Table 2.2 is ARObject; VariationPointCapable carries the XSD VARIATION-POINT element."""
    hw_attr_value = HwAttributeValue()
    assert isinstance(hw_attr_value, HwAttributeValue)
    assert issubclass(HwAttributeValue, ARObject)
    assert issubclass(HwAttributeValue, VariationPointCapable)


def test_hw_attribute_value_defaults():
    """
    Test initialization of HwAttributeValue class (Table 2.2 displayed order:
    annotation (0..1 aggr), hwAttributeDef (0..1 ref), v (0..1 attr), vt (0..1 attr)).
    """
    hw_attr_value = HwAttributeValue()

    assert hw_attr_value.annotation is None
    assert hw_attr_value.hwAttributeDefRef is None
    assert hw_attr_value.v is None
    assert hw_attr_value.vt is None


def test_hw_attribute_value_setters_round_trip():
    """Get/set round-trips must return the same instance and support chaining."""
    hw_attr_value = HwAttributeValue()

    annotation = Annotation()
    assert hw_attr_value.setAnnotation(annotation) is hw_attr_value
    assert hw_attr_value.getAnnotation() is annotation

    def_ref = make_ref("/Hw/Cat/AttrDef", "HW-ATTRIBUTE-DEF")
    assert hw_attr_value.setHwAttributeDefRef(def_ref) is hw_attr_value
    assert hw_attr_value.getHwAttributeDefRef() is def_ref

    v = Numerical()
    v.setValue("4.2")
    assert hw_attr_value.setV(v) is hw_attr_value
    assert hw_attr_value.getV() is v

    vt = VerbatimString()
    vt.setValue("some textual value")
    assert hw_attr_value.setVt(vt) is hw_attr_value
    assert hw_attr_value.getVt() is vt


def test_hw_attribute_value_setters_none_noop():
    """A None value is a no-op and does not overwrite an existing value."""
    hw_attr_value = HwAttributeValue()

    annotation = Annotation()
    hw_attr_value.setAnnotation(annotation)
    hw_attr_value.setAnnotation(None)
    assert hw_attr_value.getAnnotation() is annotation

    def_ref = make_ref("/Hw/Cat/AttrDef", "HW-ATTRIBUTE-DEF")
    hw_attr_value.setHwAttributeDefRef(def_ref)
    hw_attr_value.setHwAttributeDefRef(None)
    assert hw_attr_value.getHwAttributeDefRef() is def_ref

    v = Numerical()
    v.setValue("4.2")
    hw_attr_value.setV(v)
    hw_attr_value.setV(None)
    assert hw_attr_value.getV() is v

    vt = VerbatimString()
    vt.setValue("some textual value")
    hw_attr_value.setVt(vt)
    hw_attr_value.setVt(None)
    assert hw_attr_value.getVt() is vt


def test_hw_attribute_literal_def_docstring_verbatim():
    """Class docstring must equal the Table 2.14 Note verbatim (XSD authoritative)."""
    assert HwAttributeLiteralDef.__doc__.strip() == HW_ATTRIBUTE_LITERAL_DEF_NOTE


def test_hw_attribute_literal_def_init_doc_is_none():
    assert HwAttributeLiteralDef.__init__.__doc__ is None


def test_hw_attribute_literal_def_is_concrete_identifiable_subclass():
    hw_attr_literal = HwAttributeLiteralDef(None, "literal1")
    assert isinstance(hw_attr_literal, HwAttributeLiteralDef)
    assert issubclass(HwAttributeLiteralDef, Identifiable)


def test_hw_attribute_literal_def_no_spec_attributes():
    """Table 2.14 defines no attributes (row '-') — the fabricated value/getValue/setValue must not exist."""
    hw_attr_literal = HwAttributeLiteralDef(None, "literal1")

    assert not hasattr(hw_attr_literal, "value")
    assert not hasattr(HwAttributeLiteralDef, "getValue")
    assert not hasattr(HwAttributeLiteralDef, "setValue")
