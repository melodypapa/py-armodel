"""
This module contains tests for the Units module in MSR.AsamHdo.
"""

import ast
import os
import typing
from inspect import cleandoc, getsource
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    Numerical,
    RefType,
    String,  # noqa: F401
)
from armodel.models.M2.MSR.AsamHdo.Units import (
    PhysicalDimension,
    SingleLanguageUnitNames,
    Unit,
    UnitGroup,
)


class TestPhysicalDimension:
    """Test class for PhysicalDimension class."""

    def _make(self) -> PhysicalDimension:
        parent_obj = ARPackage(None, "parent_test")
        return PhysicalDimension(parent_obj, "test_name")

    def test_physical_dimension_initialization(self):
        """Test that a PhysicalDimension object can be initialized with default values."""
        physical_dimension = self._make()
        assert physical_dimension.getCurrentExp() is None
        assert physical_dimension.getLengthExp() is None
        assert physical_dimension.getLuminousIntensityExp() is None
        assert physical_dimension.getMassExp() is None
        assert physical_dimension.getMolarAmountExp() is None
        assert physical_dimension.getTemperatureExp() is None
        assert physical_dimension.getTimeExp() is None

    def test_physical_dimension_current_exp_methods(self):
        """Test the currentExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = Numerical()

        result = physical_dimension.setCurrentExp(exp_value)
        assert physical_dimension.getCurrentExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setCurrentExp(None) is physical_dimension
        assert physical_dimension.getCurrentExp() == exp_value

    def test_physical_dimension_length_exp_methods(self):
        """Test the lengthExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = Numerical()

        result = physical_dimension.setLengthExp(exp_value)
        assert physical_dimension.getLengthExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setLengthExp(None) is physical_dimension
        assert physical_dimension.getLengthExp() == exp_value

    def test_physical_dimension_luminous_intensity_exp_methods(self):
        """Test the luminousIntensityExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = Numerical()

        result = physical_dimension.setLuminousIntensityExp(exp_value)
        assert physical_dimension.getLuminousIntensityExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setLuminousIntensityExp(None) is physical_dimension
        assert physical_dimension.getLuminousIntensityExp() == exp_value

    def test_physical_dimension_mass_exp_methods(self):
        """Test the massExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = Numerical()

        result = physical_dimension.setMassExp(exp_value)
        assert physical_dimension.getMassExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setMassExp(None) is physical_dimension
        assert physical_dimension.getMassExp() == exp_value

    def test_physical_dimension_molar_amount_exp_methods(self):
        """Test the molarAmountExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = Numerical()

        result = physical_dimension.setMolarAmountExp(exp_value)
        assert physical_dimension.getMolarAmountExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setMolarAmountExp(None) is physical_dimension
        assert physical_dimension.getMolarAmountExp() == exp_value

    def test_physical_dimension_temperature_exp_methods(self):
        """Test the temperatureExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = Numerical()

        result = physical_dimension.setTemperatureExp(exp_value)
        assert physical_dimension.getTemperatureExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setTemperatureExp(None) is physical_dimension
        assert physical_dimension.getTemperatureExp() == exp_value

    def test_physical_dimension_time_exp_methods(self):
        """Test the timeExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = Numerical()

        result = physical_dimension.setTimeExp(exp_value)
        assert physical_dimension.getTimeExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setTimeExp(None) is physical_dimension
        assert physical_dimension.getTimeExp() == exp_value


class TestSingleLanguageUnitNames:
    """Test class for SingleLanguageUnitNames class."""

    def test_single_language_unit_names_initialization(self):
        """Test that a SingleLanguageUnitNames object can be initialized with its own __init__ (zero own members — Table 5.80 Attribute column "-")."""
        single_lang_unit_names = SingleLanguageUnitNames()
        assert single_lang_unit_names is not None
        assert SingleLanguageUnitNames.__init__.__qualname__ == "SingleLanguageUnitNames.__init__"
        assert single_lang_unit_names.sub is None
        assert single_lang_unit_names.sup is None
        assert single_lang_unit_names.getMixedString() is None

    def test_single_language_unit_names_mixed_string(self):
        """Test that a SingleLanguageUnitNames object can carry the mixed text (AtpMixedString mixin)."""
        single_lang_unit_names = SingleLanguageUnitNames().setMixedString("m")
        assert single_lang_unit_names.getMixedString() == "m"


class TestUnit:
    """Test class for Unit class."""

    def _make(self) -> Unit:
        parent_obj = ARPackage(None, "parent_test")
        return Unit(parent_obj, "test_name")

    def test_unit_initialization(self):
        """Test that a Unit object can be initialized with default values."""
        unit = self._make()
        assert unit.getDisplayName() is None
        assert unit.getFactorSiToUnit() is None
        assert unit.getOffsetSiToUnit() is None
        assert unit.getPhysicalDimensionRef() is None

    def test_unit_display_name_methods(self):
        """Test the displayName getter and setter including None no-op."""
        unit = self._make()
        display_name = SingleLanguageUnitNames()

        result = unit.setDisplayName(display_name)
        assert unit.getDisplayName() == display_name
        assert result == unit
        assert unit.setDisplayName(None) is unit
        assert unit.getDisplayName() == display_name

    def test_unit_factor_si_to_unit_methods(self):
        """Test the factorSiToUnit getter and setter including None no-op."""
        unit = self._make()
        factor = Float()

        result = unit.setFactorSiToUnit(factor)
        assert unit.getFactorSiToUnit() == factor
        assert result == unit
        assert unit.setFactorSiToUnit(None) is unit
        assert unit.getFactorSiToUnit() == factor

    def test_unit_offset_si_to_unit_methods(self):
        """Test the offsetSiToUnit getter and setter including None no-op."""
        unit = self._make()
        offset = Float()

        result = unit.setOffsetSiToUnit(offset)
        assert unit.getOffsetSiToUnit() == offset
        assert result == unit
        assert unit.setOffsetSiToUnit(None) is unit
        assert unit.getOffsetSiToUnit() == offset

    def test_unit_physical_dimension_ref_methods(self):
        """Test the physicalDimensionRef getter and setter including None no-op."""
        unit = self._make()
        ref = RefType()

        result = unit.setPhysicalDimensionRef(ref)
        assert unit.getPhysicalDimensionRef() == ref
        assert result == unit
        assert unit.setPhysicalDimensionRef(None) is unit
        assert unit.getPhysicalDimensionRef() == ref


class TestUnitGroup:
    """Test class for UnitGroup class (Table 5.81)."""

    def _make(self) -> UnitGroup:
        parent_obj = ARPackage(None, "parent_test")
        return UnitGroup(parent_obj, "test_name")

    def test_unit_group_inheritance_is_arelement(self):
        """Test that UnitGroup derives from ARElement per the Table 5.81 Base row."""
        unit_group = self._make()
        assert isinstance(unit_group, ARElement)

    def test_unit_group_initialization(self):
        """Test that a UnitGroup object can be initialized with default values."""
        unit_group = self._make()
        assert unit_group.getUnitRefs() == []

    def test_unit_group_ref_annotations(self):
        """Test that the unit ref accessors carry the spec Optional/List[RefType] hints."""
        hints_get = typing.get_type_hints(UnitGroup.getUnitRefs)
        assert hints_get["return"] == List[RefType]

        hints_add = typing.get_type_hints(UnitGroup.addUnitRef)
        assert hints_add["value"] == typing.Optional[RefType]
        assert hints_add["return"] == UnitGroup

    def test_unit_group_add_unit_ref(self):
        """Test that addUnitRef appends refs and returns self for chaining."""
        unit_group = self._make()
        ref = RefType()
        ref.setValue("/Units/KmPerHour")

        result = unit_group.addUnitRef(ref)
        assert result == unit_group
        assert unit_group.getUnitRefs() == [ref]

        second = RefType()
        second.setValue("/Units/MilesPerHour")
        unit_group.addUnitRef(second)
        assert unit_group.getUnitRefs() == [ref, second]

    def test_unit_group_add_unit_ref_none_noop(self):
        """Test that addUnitRef(None) is a no-op."""
        unit_group = self._make()
        ref = RefType()
        unit_group.addUnitRef(ref)

        assert unit_group.addUnitRef(None) is unit_group
        assert unit_group.getUnitRefs() == [ref]


class TestPhysicalDimensionSpecSync:
    """Spec-sync pins for PhysicalDimension (SWCT Table 5.76, p.398, R23-11)."""

    # Member order per Rule 0001.11: the markdown/PDF displayed row order of
    # SWCT Table 5.76 (R23-11).
    SPEC_MEMBER_ORDER = [
        "currentExp",
        "lengthExp",
        "luminousIntensityExp",
        "massExp",
        "molarAmountExp",
        "temperatureExp",
        "timeExp",
    ]

    CLASS_NOTE = (
        "This class represents a physical dimension. If the physical dimension of two units is identical, then a conversion between them is possible. "
        "The conversion between units is related to the definition of the physical dimension. Note that the equivalence of the exponents does not per se define the convertibility. "
        "For example Energy and Torque share the same exponents (Nm). Please note further the value of an exponent does not necessarily have to be an integer number. "
        "It is also possible that the value yields a rational number, e.g. to compute the square root of a given physical quantity. "
        "In this case the exponent value would be a rational number where the numerator value is 1 and the denominator value is 2. "
        "Tags: atp.recommendedPackage=PhysicalDimensions"
    )
    CURRENT_EXP_NOTE = 'This attribute represents the exponent of the physical dimension "electric current". Tags: xml.sequenceOffset=50'
    LENGTH_EXP_NOTE = 'The exponent of the physical dimension "length". Tags: xml.sequenceOffset=20'
    LUMINOUS_INTENSITY_EXP_NOTE = 'The exponent of the physical dimension "luminous intensity". Tags: xml.sequenceOffset=80'
    MASS_EXP_NOTE = 'The exponent of the physical dimension "mass". Tags: xml.sequenceOffset=30'
    MOLAR_AMOUNT_EXP_NOTE = 'The exponent of the physical dimension "quantity of substance". Tags: xml.sequenceOffset=70'
    TEMPERATURE_EXP_NOTE = 'The exponent of the physical dimension "temperature". Tags: xml.sequenceOffset=60'
    TIME_EXP_NOTE = 'The exponent of the physical dimension "time". Tags: xml.sequenceOffset=40'

    def _init_field_order(self):
        src = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "..",
            "..",
            "src",
            "armodel",
            "models",
            "M2",
            "MSR",
            "AsamHdo",
            "Units.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "PhysicalDimension")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_physical_dimension_inheritance_is_arelement(self):
        """PhysicalDimension derives from ARElement per the Table 5.76 Base row."""
        assert issubclass(PhysicalDimension, ARElement)

    def test_physical_dimension_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.76 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_physical_dimension_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime and is Optional[Numerical] (0..1 attr rows)."""
        for name in (
            "getCurrentExp",
            "setCurrentExp",
            "getLengthExp",
            "setLengthExp",
            "getLuminousIntensityExp",
            "setLuminousIntensityExp",
            "getMassExp",
            "setMassExp",
            "getMolarAmountExp",
            "setMolarAmountExp",
            "getTemperatureExp",
            "setTemperatureExp",
            "getTimeExp",
            "setTimeExp",
        ):
            hints = typing.get_type_hints(getattr(PhysicalDimension, name))
            assert hints, f"no annotations resolved for {name}"
            if name.startswith("get"):
                assert hints["return"] == typing.Optional[Numerical], name
            else:
                assert hints["value"] == typing.Optional[Numerical], name
                assert hints["return"] == PhysicalDimension, name

    def test_physical_dimension_class_docstring_is_spec_note_verbatim(self):
        """The class docstring is the Table 5.76 Note verbatim incl. the Tags tail."""
        assert cleandoc(PhysicalDimension.__doc__) == self.CLASS_NOTE

    def test_physical_dimension_init_has_no_docstring(self):
        assert PhysicalDimension.__init__.__doc__ is None

    def test_physical_dimension_members_are_pep526_annotated(self):
        source = getsource(PhysicalDimension.__init__)
        assert "# type:" not in source
        for field in self.SPEC_MEMBER_ORDER:
            assert f"self.{field}: Optional[Numerical] = None" in source

    def test_physical_dimension_inline_comments_match_spec_notes(self):
        source = getsource(PhysicalDimension.__init__)
        for note in (self.CURRENT_EXP_NOTE, self.LENGTH_EXP_NOTE, self.LUMINOUS_INTENSITY_EXP_NOTE, self.MASS_EXP_NOTE, self.MOLAR_AMOUNT_EXP_NOTE, self.TEMPERATURE_EXP_NOTE, self.TIME_EXP_NOTE):
            assert "# " + note in source

    def test_physical_dimension_getter_docstrings_match_spec_notes(self):
        assert cleandoc(PhysicalDimension.getCurrentExp.__doc__) == self.CURRENT_EXP_NOTE
        assert cleandoc(PhysicalDimension.getLengthExp.__doc__) == self.LENGTH_EXP_NOTE
        assert cleandoc(PhysicalDimension.getLuminousIntensityExp.__doc__) == self.LUMINOUS_INTENSITY_EXP_NOTE
        assert cleandoc(PhysicalDimension.getMassExp.__doc__) == self.MASS_EXP_NOTE
        assert cleandoc(PhysicalDimension.getMolarAmountExp.__doc__) == self.MOLAR_AMOUNT_EXP_NOTE
        assert cleandoc(PhysicalDimension.getTemperatureExp.__doc__) == self.TEMPERATURE_EXP_NOTE
        assert cleandoc(PhysicalDimension.getTimeExp.__doc__) == self.TIME_EXP_NOTE

    def test_physical_dimension_setter_docstrings_match_spec_notes(self):
        assert cleandoc(PhysicalDimension.setCurrentExp.__doc__) == self.CURRENT_EXP_NOTE + " A None value is a no-op and does not overwrite an existing currentExp."
        assert cleandoc(PhysicalDimension.setLengthExp.__doc__) == self.LENGTH_EXP_NOTE + " A None value is a no-op and does not overwrite an existing lengthExp."
        assert cleandoc(PhysicalDimension.setLuminousIntensityExp.__doc__) == self.LUMINOUS_INTENSITY_EXP_NOTE + " A None value is a no-op and does not overwrite an existing luminousIntensityExp."
        assert cleandoc(PhysicalDimension.setMassExp.__doc__) == self.MASS_EXP_NOTE + " A None value is a no-op and does not overwrite an existing massExp."
        assert cleandoc(PhysicalDimension.setMolarAmountExp.__doc__) == self.MOLAR_AMOUNT_EXP_NOTE + " A None value is a no-op and does not overwrite an existing molarAmountExp."
        assert cleandoc(PhysicalDimension.setTemperatureExp.__doc__) == self.TEMPERATURE_EXP_NOTE + " A None value is a no-op and does not overwrite an existing temperatureExp."
        assert cleandoc(PhysicalDimension.setTimeExp.__doc__) == self.TIME_EXP_NOTE + " A None value is a no-op and does not overwrite an existing timeExp."
