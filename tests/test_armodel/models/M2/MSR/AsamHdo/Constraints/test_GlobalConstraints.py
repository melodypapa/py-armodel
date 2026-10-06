"""
This module contains tests for the GlobalConstraints module in MSR.AsamHdo.Constraints.
"""

import ast
import typing
from inspect import cleandoc, getsource

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    Limit,
    MonotonyEnum,
    Numerical,
    RefType,
)
from armodel.models.M2.MSR.AsamHdo.Constraints import GlobalConstraints
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import (
    DataConstr,
    DataConstrRule,
    InternalConstrs,
    PhysConstrs,
    ScaleConstr,
    ScaleConstrValidityEnum,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class TestInternalConstrs:
    """Test class for InternalConstrs class."""

    def test_internal_constrs_initialization(self):
        """Test that an InternalConstrs object can be initialized with default values."""
        internal_constrs = InternalConstrs()
        assert internal_constrs.getLowerLimit() is None
        assert internal_constrs.getMaxDiff() is None
        assert internal_constrs.getMaxGradient() is None
        assert internal_constrs.getMonotony() is None
        assert internal_constrs.getScaleConstrs() == []
        assert internal_constrs.getUpperLimit() is None

    def test_internal_constrs_lower_limit_methods(self):
        """Test the lowerLimit getter and setter including None no-op."""
        internal_constrs = InternalConstrs()
        limit = Limit()

        result = internal_constrs.setLowerLimit(limit)
        assert internal_constrs.getLowerLimit() == limit
        assert result == internal_constrs
        assert internal_constrs.setLowerLimit(None) is internal_constrs
        assert internal_constrs.getLowerLimit() == limit

    def test_internal_constrs_max_diff_methods(self):
        """Test the maxDiff getter and setter including None no-op."""
        internal_constrs = InternalConstrs()
        max_diff = Numerical()

        result = internal_constrs.setMaxDiff(max_diff)
        assert internal_constrs.getMaxDiff() == max_diff
        assert result == internal_constrs
        assert internal_constrs.setMaxDiff(None) is internal_constrs
        assert internal_constrs.getMaxDiff() == max_diff

    def test_internal_constrs_max_gradient_methods(self):
        """Test the maxGradient getter and setter including None no-op."""
        internal_constrs = InternalConstrs()
        max_gradient = Numerical()

        result = internal_constrs.setMaxGradient(max_gradient)
        assert internal_constrs.getMaxGradient() == max_gradient
        assert result == internal_constrs
        assert internal_constrs.setMaxGradient(None) is internal_constrs
        assert internal_constrs.getMaxGradient() == max_gradient

    def test_internal_constrs_monotony_methods(self):
        """Test the monotony getter and setter including None no-op."""
        internal_constrs = InternalConstrs()
        monotony = MonotonyEnum.INCREASING

        result = internal_constrs.setMonotony(monotony)
        assert internal_constrs.getMonotony() == monotony
        assert result == internal_constrs
        assert internal_constrs.setMonotony(None) is internal_constrs
        assert internal_constrs.getMonotony() == monotony

    def test_internal_constrs_scale_constr_methods(self):
        """Test addScaleConstr/getScaleConstrs including None no-op."""
        internal_constrs = InternalConstrs()
        scale1 = ScaleConstr()
        scale2 = ScaleConstr()

        result = internal_constrs.addScaleConstr(scale1)
        internal_constrs.addScaleConstr(scale2)
        assert internal_constrs.getScaleConstrs() == [scale1, scale2]
        assert result == internal_constrs
        assert internal_constrs.addScaleConstr(None) is internal_constrs
        assert internal_constrs.getScaleConstrs() == [scale1, scale2]

    def test_internal_constrs_upper_limit_methods(self):
        """Test the upperLimit getter and setter including None no-op."""
        internal_constrs = InternalConstrs()
        limit = Limit()

        result = internal_constrs.setUpperLimit(limit)
        assert internal_constrs.getUpperLimit() == limit
        assert result == internal_constrs
        assert internal_constrs.setUpperLimit(None) is internal_constrs
        assert internal_constrs.getUpperLimit() == limit


class TestScaleConstr:
    """Test class for ScaleConstr class."""

    def test_scale_constr_initialization(self):
        """Test that a ScaleConstr object can be initialized with default values."""
        scale_constr = ScaleConstr()
        assert scale_constr.getDesc() is None
        assert scale_constr.getLowerLimit() is None
        assert scale_constr.getShortLabel() is None
        assert scale_constr.getUpperLimit() is None
        assert scale_constr.getValidity() is None

    def test_scale_constr_methods(self):
        """Test ScaleConstr setter/getter chaining."""
        scale_constr = ScaleConstr()
        limit = Limit()
        scale_constr.setUpperLimit(limit)
        assert scale_constr.getUpperLimit() is limit
        assert scale_constr.setShortLabel(None) is scale_constr

    def test_scale_constr_validity_methods(self):
        """Test the validity getter and setter including None no-op."""
        from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import ScaleConstrValidityEnum

        scale_constr = ScaleConstr()
        validity = ScaleConstrValidityEnum().setValue(ScaleConstrValidityEnum.VALID)

        result = scale_constr.setValidity(validity)
        assert scale_constr.getValidity() == validity
        assert result == scale_constr
        assert scale_constr.setValidity(None) is scale_constr
        assert scale_constr.getValidity() == validity

    def test_scale_constr_desc_methods(self):
        """Test the desc getter and setter including None no-op."""
        scale_constr = ScaleConstr()
        desc = MultiLanguageOverviewParagraph()

        result = scale_constr.setDesc(desc)
        assert scale_constr.getDesc() == desc
        assert result == scale_constr
        assert scale_constr.setDesc(None) is scale_constr
        assert scale_constr.getDesc() == desc

    def test_scale_constr_lower_limit_methods(self):
        """Test the lowerLimit getter and setter including None no-op."""
        scale_constr = ScaleConstr()
        limit = Limit()

        result = scale_constr.setLowerLimit(limit)
        assert scale_constr.getLowerLimit() == limit
        assert result == scale_constr
        assert scale_constr.setLowerLimit(None) is scale_constr
        assert scale_constr.getLowerLimit() == limit


class TestScaleConstrValidityEnum:
    """Test class for ScaleConstrValidityEnum (R4.3.1 AUTOSAR_TPS_SoftwareComponentTemplate.pdf, Table 5.95, p.417)."""

    def test_scale_constr_validity_enum_has_spec_note(self):
        assert cleandoc(ScaleConstrValidityEnum.__doc__) == "This enumerator specifies the possible values of a scale."

    def test_scale_constr_validity_enum_initialization(self):
        """Test that a ScaleConstrValidityEnum object can be instantiated."""
        enum_obj = ScaleConstrValidityEnum()
        assert enum_obj is not None
        assert isinstance(enum_obj, ScaleConstrValidityEnum)

    def test_scale_constr_validity_enum_spec_literals(self):
        """ScaleConstrValidityEnum shall expose the 4 spec literals with their wire values (Table 5.95)."""
        enum_obj = ScaleConstrValidityEnum()
        expected = {
            ScaleConstrValidityEnum.NOT_AVAILABLE: "notAvailable",
            ScaleConstrValidityEnum.NOT_DEFINED: "notDefined",
            ScaleConstrValidityEnum.NOT_VALID: "notValid",
            ScaleConstrValidityEnum.VALID: "valid",
        }
        for const, value in expected.items():
            assert const == value
        assert enum_obj.getEnumValues() == ["notAvailable", "notDefined", "notValid", "valid"]

    def test_scale_constr_validity_enum_validate_enum_value(self):
        """validateEnumValue accepts the wire values and rejects non-wire forms.

        Neither XSD (R23-11 AUTOSAR_00052.xsd L142112, R4.3.1 AUTOSAR_00044.xsd L101206)
        carries atp.Status="removed" literals for this enum, so no legacy forms are valid.
        """
        enum_obj = ScaleConstrValidityEnum()
        assert enum_obj.validateEnumValue("notAvailable") is True
        assert enum_obj.validateEnumValue("notDefined") is True
        assert enum_obj.validateEnumValue("notValid") is True
        assert enum_obj.validateEnumValue("valid") is True
        assert enum_obj.validateEnumValue("NOT-AVAILABLE") is False
        assert enum_obj.validateEnumValue("unknown") is False

    def test_scale_constr_validity_enum_set_value_with_member(self):
        """The enum is instantiable and its literal value can be set from a member constant."""
        enum_obj = ScaleConstrValidityEnum().setValue(ScaleConstrValidityEnum.NOT_AVAILABLE)
        assert enum_obj.getValue() == "notAvailable"


class TestPhysConstrs:
    """Test class for PhysConstrs class."""

    def test_phys_constrs_initialization(self):
        """Test that a PhysConstrs object can be initialized with default values."""
        phys_constrs = PhysConstrs()
        assert phys_constrs.getLowerLimit() is None
        assert phys_constrs.getUpperLimit() is None
        assert phys_constrs.getMaxDiff() is None
        assert phys_constrs.getMaxGradient() is None
        assert phys_constrs.getMonotony() is None
        assert phys_constrs.getScaleConstrs() == []
        assert phys_constrs.getUnitRef() is None

    def test_phys_constrs_methods(self):
        """Test PhysConstrs setter/getter chaining and the ordered scaleConstrs list."""
        phys_constrs = PhysConstrs()

        lower = Limit()
        phys_constrs.setLowerLimit(lower)
        assert phys_constrs.getLowerLimit() is lower

        upper = Limit()
        phys_constrs.setUpperLimit(upper)
        assert phys_constrs.getUpperLimit() is upper

        monotony = MonotonyEnum.INCREASING
        phys_constrs.setMonotony(monotony)
        assert phys_constrs.getMonotony() is monotony

        unit_ref = RefType()
        phys_constrs.setUnitRef(unit_ref)
        assert phys_constrs.getUnitRef() is unit_ref

        scale1 = ScaleConstr()
        scale2 = ScaleConstr()
        phys_constrs.addScaleConstr(scale1)
        phys_constrs.addScaleConstr(scale2)
        assert phys_constrs.getScaleConstrs() == [scale1, scale2]

        assert phys_constrs.setLowerLimit(None) is phys_constrs


class TestDataConstrRule:
    """Test class for DataConstrRule class."""

    def test_data_constr_rule_has_spec_note(self):
        assert cleandoc(DataConstrRule.__doc__) == "This meta-class represents the ability to express one specific data constraint rule."

    def test_data_constr_rule_initialization(self):
        """Test that a DataConstrRule object can be initialized with default values."""
        data_constr_rule = DataConstrRule()
        assert data_constr_rule.constrLevel is None
        assert data_constr_rule.internalConstrs is None
        assert data_constr_rule.physConstrs is None

    def test_data_constr_rule_accessors_preserve_values_on_none(self):
        rule = DataConstrRule()
        constr_level = Integer()
        internal = InternalConstrs()
        physical = PhysConstrs()

        assert rule.setConstrLevel(constr_level) is rule
        assert rule.setInternalConstrs(internal) is rule
        assert rule.setPhysConstrs(physical) is rule
        assert rule.setConstrLevel(None) is rule
        assert rule.setInternalConstrs(None) is rule
        assert rule.setPhysConstrs(None) is rule
        assert rule.getConstrLevel() is constr_level
        assert rule.getInternalConstrs() is internal
        assert rule.getPhysConstrs() is physical


class TestDataConstr:
    """Test class for DataConstr class."""

    def test_data_constr_has_spec_note(self):
        assert cleandoc(DataConstr.__doc__) == "This meta-class represents the ability to specify constraints on data. Tags: atp.recommendedPackage=DataConstrs"

    def test_data_constr_initialization(self):
        """Test that a DataConstr object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        data_constr = DataConstr(parent_obj, "test_name")
        assert data_constr.data_constr_rule == []

    def test_data_constr_rule_methods(self):
        """Test adding and getting data constraint rules."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        data_constr = DataConstr(parent_obj, "test_name")
        rule = DataConstrRule()

        # Test addDataConstrRule and getDataConstrRules
        assert data_constr.addDataConstrRule(rule) is data_constr
        rules = data_constr.getDataConstrRules()
        assert rules == [rule]
        assert data_constr.addDataConstrRule(None) is data_constr
        assert data_constr.getDataConstrRules() == [rule]


class TestPhysConstrsSpecSync:
    """Spec-sync pins for PhysConstrs (SWCT Table 5.84, p.406, R23-11)."""

    SPEC_MEMBER_ORDER = [
        "lowerLimit",
        "maxDiff",
        "maxGradient",
        "monotony",
        "scaleConstrs",
        "unitRef",
        "upperLimit",
    ]

    CLASS_NOTE = "This meta-class represents the ability to express physical constraints. Therefore it has (in opposite to InternalConstrs) a reference to a Unit."
    LOWER_LIMIT_NOTE = "This specifies the lower limit of the constraint. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=20"
    MAX_DIFF_NOTE = "Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis. Tags: xml.sequenceOffset=60"
    MAX_GRADIENT_NOTE = "This element specifies the maximum slope that may be used in curves and maps. Tags: xml.sequenceOffset=50"
    MONOTONY_NOTE = "This specifies the monotony constraints on the data object. Note that this applies only to curves and maps. Tags: xml.sequenceOffset=70"
    SCALE_CONSTR_NOTE = "This is one particular scale which contributes to the data constraints. Tags: atp.Status=obsolete xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=40 xml.typeElement=false xml.typeWrapperElement=false"
    UNIT_NOTE = "This is the unit to which the physical constraints relate to. In particular, it is the physical unit of the specified limits. Tags: xml.sequenceOffset=80"
    UPPER_LIMIT_NOTE = "This specifies the upper limit of the constraint. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=30"

    def _init_field_order(self):
        tree = ast.parse(open(GlobalConstraints.__file__, encoding="utf-8").read())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "PhysConstrs")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_phys_constrs_inheritance_is_arobject(self):
        """PhysConstrs derives from ARObject per the Table 5.84 Base row."""
        assert issubclass(PhysConstrs, ARObject)

    def test_phys_constrs_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.84 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_phys_constrs_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime with the spec shapes (Rule 0003)."""
        hints = typing.get_type_hints(PhysConstrs.getLowerLimit)
        assert hints["return"] == typing.Optional[Limit]
        hints = typing.get_type_hints(PhysConstrs.setLowerLimit)
        assert hints["value"] == typing.Optional[Limit]
        assert hints["return"] == PhysConstrs
        for getter in ("getMaxDiff", "getMaxGradient"):
            hints = typing.get_type_hints(getattr(PhysConstrs, getter))
            assert hints["return"] == typing.Optional[Numerical], getter
        hints = typing.get_type_hints(PhysConstrs.getMonotony)
        assert hints["return"] == typing.Optional[MonotonyEnum]
        hints = typing.get_type_hints(PhysConstrs.getScaleConstrs)
        assert hints["return"] == typing.List[ScaleConstr]
        hints = typing.get_type_hints(PhysConstrs.getUnitRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(PhysConstrs.getUpperLimit)
        assert hints["return"] == typing.Optional[Limit]

    def test_phys_constrs_class_docstring_is_spec_note_verbatim(self):
        """The class docstring is the Table 5.84 Note verbatim."""
        assert cleandoc(PhysConstrs.__doc__) == self.CLASS_NOTE

    def test_phys_constrs_init_has_no_docstring(self):
        assert PhysConstrs.__init__.__doc__ is None

    def test_phys_constrs_members_are_pep526_annotated(self):
        source = getsource(PhysConstrs.__init__)
        assert "# type:" not in source
        assert "self.lowerLimit: Optional[Limit] = None" in source
        assert "self.maxDiff: Optional[Numerical] = None" in source
        assert "self.maxGradient: Optional[Numerical] = None" in source
        assert "self.monotony: Optional[MonotonyEnum] = None" in source
        assert "self.scaleConstrs: List[ScaleConstr] = []" in source
        assert "self.unitRef: Optional[RefType] = None" in source
        assert "self.upperLimit: Optional[Limit] = None" in source

    def test_phys_constrs_inline_comments_match_spec_notes(self):
        source = getsource(PhysConstrs.__init__)
        for note in (self.LOWER_LIMIT_NOTE, self.MAX_DIFF_NOTE, self.MAX_GRADIENT_NOTE, self.MONOTONY_NOTE, self.SCALE_CONSTR_NOTE, self.UNIT_NOTE, self.UPPER_LIMIT_NOTE):
            assert "# " + note in source

    def test_phys_constrs_getter_docstrings_match_spec_notes(self):
        assert cleandoc(PhysConstrs.getLowerLimit.__doc__) == self.LOWER_LIMIT_NOTE
        assert cleandoc(PhysConstrs.getMaxDiff.__doc__) == self.MAX_DIFF_NOTE
        assert cleandoc(PhysConstrs.getMaxGradient.__doc__) == self.MAX_GRADIENT_NOTE
        assert cleandoc(PhysConstrs.getMonotony.__doc__) == self.MONOTONY_NOTE
        assert cleandoc(PhysConstrs.getScaleConstrs.__doc__) == self.SCALE_CONSTR_NOTE
        assert cleandoc(PhysConstrs.getUnitRef.__doc__) == self.UNIT_NOTE
        assert cleandoc(PhysConstrs.getUpperLimit.__doc__) == self.UPPER_LIMIT_NOTE

    def test_phys_constrs_setter_docstrings_match_spec_notes(self):
        assert cleandoc(PhysConstrs.setLowerLimit.__doc__) == self.LOWER_LIMIT_NOTE + " A None value is a no-op and does not overwrite an existing lowerLimit."
        assert cleandoc(PhysConstrs.setMaxDiff.__doc__) == self.MAX_DIFF_NOTE + " A None value is a no-op and does not overwrite an existing maxDiff."
        assert cleandoc(PhysConstrs.setMaxGradient.__doc__) == self.MAX_GRADIENT_NOTE + " A None value is a no-op and does not overwrite an existing maxGradient."
        assert cleandoc(PhysConstrs.setMonotony.__doc__) == self.MONOTONY_NOTE + " A None value is a no-op and does not overwrite an existing monotony."
        assert cleandoc(PhysConstrs.getScaleConstrs.__doc__) == self.SCALE_CONSTR_NOTE
        assert cleandoc(PhysConstrs.setUnitRef.__doc__) == self.UNIT_NOTE + " A None value is a no-op and does not overwrite an existing unitRef."
        assert cleandoc(PhysConstrs.setUpperLimit.__doc__) == self.UPPER_LIMIT_NOTE + " A None value is a no-op and does not overwrite an existing upperLimit."

    def test_phys_constrs_accessor_none_no_ops(self):
        phys_constrs = PhysConstrs()
        monotony = MonotonyEnum().setValue(MonotonyEnum.DECREASING)
        assert phys_constrs.setMonotony(monotony) is phys_constrs
        phys_constrs.setMonotony(None)
        assert phys_constrs.getMonotony() is monotony

        phys_constrs.setMaxDiff(None)
        assert phys_constrs.getMaxDiff() is None
        phys_constrs.setMaxGradient(None)
        assert phys_constrs.getMaxGradient() is None

        unit_ref = RefType()
        assert phys_constrs.setUnitRef(unit_ref) is phys_constrs
        phys_constrs.setUnitRef(None)
        assert phys_constrs.getUnitRef() is unit_ref

        assert phys_constrs.addScaleConstr(None) is phys_constrs
        assert phys_constrs.getScaleConstrs() == []


class TestInternalConstrsSpecSync:
    """Spec-sync pins for InternalConstrs (SWCT Table 5.85, p.407, R23-11)."""

    SPEC_MEMBER_ORDER = [
        "lowerLimit",
        "maxDiff",
        "maxGradient",
        "monotony",
        "scaleConstrs",
        "upperLimit",
    ]

    CLASS_NOTE = "This meta-class represents the ability to express internal constraints."
    LOWER_LIMIT_NOTE = "This specifies the lower limit of the constraint. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=20"
    MAX_DIFF_NOTE = "Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis. Tags: xml.sequenceOffset=60"
    MAX_GRADIENT_NOTE = "This element specifies the maximum slope that may be used in maps and curves. Tags: xml.sequenceOffset=50"
    MONOTONY_NOTE = 'This element specifies the monotony characteristics of the current internal or physical limits. The following table shows the monotony characteristics which are to be filled through the corresponding values. If the element has no contents or if it is omitted, "no Monotony" is the default content. Tags: xml.sequenceOffset=70'
    SCALE_CONSTR_NOTE = (
        "This is one particular scale which contributes to the data constraints. Tags: atp.Status=obsolete xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=40 xml.typeElement=false"
    )
    UPPER_LIMIT_NOTE = "This specifies the upper limit defined by the constraint. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=30"

    def _init_field_order(self):
        tree = ast.parse(open(GlobalConstraints.__file__, encoding="utf-8").read())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "InternalConstrs")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_internal_constrs_inheritance_is_arobject(self):
        """InternalConstrs derives from ARObject per the Table 5.85 Base row."""
        assert issubclass(InternalConstrs, ARObject)

    def test_internal_constrs_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.85 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_internal_constrs_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime with the spec shapes (Rule 0003)."""
        hints = typing.get_type_hints(InternalConstrs.getLowerLimit)
        assert hints["return"] == typing.Optional[Limit]
        hints = typing.get_type_hints(InternalConstrs.setLowerLimit)
        assert hints["value"] == typing.Optional[Limit]
        assert hints["return"] == InternalConstrs
        for getter in ("getMaxDiff", "getMaxGradient"):
            hints = typing.get_type_hints(getattr(InternalConstrs, getter))
            assert hints["return"] == typing.Optional[Numerical], getter
        hints = typing.get_type_hints(InternalConstrs.getMonotony)
        assert hints["return"] == typing.Optional[MonotonyEnum]
        hints = typing.get_type_hints(InternalConstrs.getScaleConstrs)
        assert hints["return"] == typing.List[ScaleConstr]
        hints = typing.get_type_hints(InternalConstrs.getUpperLimit)
        assert hints["return"] == typing.Optional[Limit]

    def test_internal_constrs_class_docstring_is_spec_note_verbatim(self):
        """The class docstring is the Table 5.85 Note verbatim."""
        assert cleandoc(InternalConstrs.__doc__) == self.CLASS_NOTE

    def test_internal_constrs_init_has_no_docstring(self):
        assert InternalConstrs.__init__.__doc__ is None

    def test_internal_constrs_members_are_pep526_annotated(self):
        source = getsource(InternalConstrs.__init__)
        assert "# type:" not in source
        assert "self.lowerLimit: Optional[Limit] = None" in source
        assert "self.maxDiff: Optional[Numerical] = None" in source
        assert "self.maxGradient: Optional[Numerical] = None" in source
        assert "self.monotony: Optional[MonotonyEnum] = None" in source
        assert "self.scaleConstrs: List[ScaleConstr] = []" in source
        assert "self.upperLimit: Optional[Limit] = None" in source

    def test_internal_constrs_inline_comments_match_spec_notes(self):
        source = getsource(InternalConstrs.__init__)
        for note in (self.LOWER_LIMIT_NOTE, self.MAX_DIFF_NOTE, self.MAX_GRADIENT_NOTE, self.MONOTONY_NOTE, self.SCALE_CONSTR_NOTE, self.UPPER_LIMIT_NOTE):
            assert "# " + note in source

    def test_internal_constrs_getter_docstrings_match_spec_notes(self):
        assert cleandoc(InternalConstrs.getLowerLimit.__doc__) == self.LOWER_LIMIT_NOTE
        assert cleandoc(InternalConstrs.getMaxDiff.__doc__) == self.MAX_DIFF_NOTE
        assert cleandoc(InternalConstrs.getMaxGradient.__doc__) == self.MAX_GRADIENT_NOTE
        assert cleandoc(InternalConstrs.getMonotony.__doc__) == self.MONOTONY_NOTE
        assert cleandoc(InternalConstrs.getScaleConstrs.__doc__) == self.SCALE_CONSTR_NOTE
        assert cleandoc(InternalConstrs.getUpperLimit.__doc__) == self.UPPER_LIMIT_NOTE

    def test_internal_constrs_setter_docstrings_match_spec_notes(self):
        assert cleandoc(InternalConstrs.setLowerLimit.__doc__) == self.LOWER_LIMIT_NOTE + " A None value is a no-op and does not overwrite an existing lowerLimit."
        assert cleandoc(InternalConstrs.setMaxDiff.__doc__) == self.MAX_DIFF_NOTE + " A None value is a no-op and does not overwrite an existing maxDiff."
        assert cleandoc(InternalConstrs.setMaxGradient.__doc__) == self.MAX_GRADIENT_NOTE + " A None value is a no-op and does not overwrite an existing maxGradient."
        assert cleandoc(InternalConstrs.setMonotony.__doc__) == self.MONOTONY_NOTE + " A None value is a no-op and does not overwrite an existing monotony."
        assert cleandoc(InternalConstrs.getScaleConstrs.__doc__) == self.SCALE_CONSTR_NOTE
        assert cleandoc(InternalConstrs.setUpperLimit.__doc__) == self.UPPER_LIMIT_NOTE + " A None value is a no-op and does not overwrite an existing upperLimit."

    def test_internal_constrs_accessor_none_no_ops(self):
        internal_constrs = InternalConstrs()
        monotony = MonotonyEnum().setValue(MonotonyEnum.DECREASING)
        assert internal_constrs.setMonotony(monotony) is internal_constrs
        internal_constrs.setMonotony(None)
        assert internal_constrs.getMonotony() is monotony

        internal_constrs.setMaxDiff(None)
        assert internal_constrs.getMaxDiff() is None
        internal_constrs.setMaxGradient(None)
        assert internal_constrs.getMaxGradient() is None

        assert internal_constrs.addScaleConstr(None) is internal_constrs
        assert internal_constrs.getScaleConstrs() == []
