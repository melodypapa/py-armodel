"""
This module contains tests for the CalibrationParameter module in MSR.DataDictionary.
"""

import ast
import os
import typing
from inspect import cleandoc

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DisplayFormatString, Float, MonotonyEnum
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
    SwCalprmAxis,
    SwCalprmAxisSet,
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


class TestCalprmAxisCategoryEnum:
    """Test class for CalprmAxisCategoryEnum class (SWCT Table 5.48, p.353, R23-11)."""

    def test_calprm_axis_category_enum_initialization(self):
        """The enum is instantiable and its literal value can be set from a member constant."""
        enum = CalprmAxisCategoryEnum()
        enum.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        assert enum.getValue() == "stdAxis"

    def test_calprm_axis_category_enum_values(self):
        """CalprmAxisCategoryEnum shall expose the 4 spec literals in Table 5.48 order.

        Member values are the camelCase mmt.qualifiedName literals; the UPPERCASE
        XSD wire forms (CALPRM-AXIS-CATEGORY-ENUM--SIMPLE) live only in the
        consumer-side CALPRM_AXIS_CATEGORY_XML_MAP and are not model values.
        """
        assert CalprmAxisCategoryEnum.COM_AXIS == "comAxis"
        assert CalprmAxisCategoryEnum.FIX_AXIS == "fixAXIS"
        assert CalprmAxisCategoryEnum.RES_AXIS == "resAxis"
        assert CalprmAxisCategoryEnum.STD_AXIS == "stdAxis"
        assert CalprmAxisCategoryEnum().getEnumValues() == ["comAxis", "fixAXIS", "resAxis", "stdAxis"]

    def test_calprm_axis_category_enum_has_spec_note(self):
        """The class docstring carries the Table 5.48 Note verbatim."""
        assert cleandoc(CalprmAxisCategoryEnum.__doc__) == "This enum specifies the possible values of the category property within SwCalprmAxis."

    def test_calprm_axis_category_enum_validate_enum_value(self):
        """validateEnumValue accepts the model literal values and rejects non-wire forms.

        R23-11 AUTOSAR_00052.xsd CALPRM-AXIS-CATEGORY-ENUM--SIMPLE (L132080) additionally
        carries six atp.Status="removed" literals (COM-AXIS, CURVE-AXIS, CURVE_AXIS,
        FIX-AXIS, RES-AXIS, STD-AXIS) which map to no member (Rule 0001.3); the UPPERCASE
        wire forms (COM_AXIS, FIX_AXIS, RES_AXIS, STD_AXIS) live only in the
        consumer-side CALPRM_AXIS_CATEGORY_XML_MAP and are not model values.
        """
        enum_obj = CalprmAxisCategoryEnum()
        assert enum_obj.validateEnumValue("comAxis") is True
        assert enum_obj.validateEnumValue("fixAXIS") is True
        assert enum_obj.validateEnumValue("resAxis") is True
        assert enum_obj.validateEnumValue("stdAxis") is True
        assert enum_obj.validateEnumValue("COM_AXIS") is False
        assert enum_obj.validateEnumValue("COM-AXIS") is False
        assert enum_obj.validateEnumValue("CURVE_AXIS") is False
        assert enum_obj.validateEnumValue("unknown") is False

    def test_calprm_axis_category_enum_set_value_with_member(self):
        """The enum is instantiable and its literal value can be set from a member constant."""
        enum_obj = CalprmAxisCategoryEnum().setValue(CalprmAxisCategoryEnum.FIX_AXIS)
        assert enum_obj.getValue() == "fixAXIS"

    def test_calprm_axis_category_enum_set_value_none_noop(self):
        """setValue(None) is a no-op and does not overwrite an existing value."""
        enum_obj = CalprmAxisCategoryEnum().setValue(CalprmAxisCategoryEnum.RES_AXIS)
        enum_obj.setValue(None)
        assert enum_obj.getValue() == "resAxis"


class TestSwCalprmAxisTypeProps:
    """Test class for SwCalprmAxisTypeProps abstract class (SWCT Table 5.49, p.353, R23-11)."""

    SPEC_MEMBER_ORDER = ["maxGradient", "monotony"]

    SPEC_NOTES = {
        "maxGradient": "This attribute defines the maximum permissible gradient for an adjustable object (curve, map or cuboid) with respect to a specific axis. MaxGrad = maximum( absolute((Value i,k - Value i-1,k)/(Axis Point i - Axis Point i-1)) )",
        "monotony": "This attribute specifies the monotony constraint for an adjustable object (curve, map or cuboid) with respect to a specific axis. This information can be used by MCD system to verify whether the monotony constraint is fulfilled and to prevent from changes violating the constraint.",
    }

    def _init_field_order(self) -> list:
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
            "DataDictionary",
            "CalibrationParameter.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SwCalprmAxisTypeProps")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_sw_calprm_axis_type_props_abstract_class(self):
        """Test that SwCalprmAxisTypeProps cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            SwCalprmAxisTypeProps()

    def test_sw_calprm_axis_type_props_class_note_verbatim(self):
        """The class docstring carries the Table 5.49 Note verbatim."""
        assert (
            cleandoc(SwCalprmAxisTypeProps.__doc__)
            == "Base class for the type of the calibration axis. This provides the particular model of the specialization. If the specialization would be the directly from SwCalPrmAxis, the sequence of common properties and the specializes ones would be different."
        )

    def test_sw_calprm_axis_type_props_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.49 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_sw_calprm_axis_type_props_accessors_follow_member_order(self):
        """Accessor groups per attribute, in spec row order; scalars getter-first."""
        expected = [
            "getMaxGradient",
            "setMaxGradient",
            "getMonotony",
            "setMonotony",
        ]
        for name in expected:
            assert hasattr(SwCalprmAxisTypeProps, name), f"missing accessor {name}"

    def test_sw_calprm_axis_type_props_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime (Rule 0003 — no TYPE_CHECKING-only names)."""
        for name in ("getMaxGradient", "setMaxGradient", "getMonotony", "setMonotony"):
            hints = typing.get_type_hints(getattr(SwCalprmAxisTypeProps, name))
            assert hints, f"no annotations resolved for {name}"
            assert "return" in hints
        assert typing.get_type_hints(SwCalprmAxisTypeProps.setMaxGradient)["value"] == typing.Optional[Float]
        assert typing.get_type_hints(SwCalprmAxisTypeProps.setMonotony)["value"] == typing.Optional[MonotonyEnum]
        assert typing.get_type_hints(SwCalprmAxisTypeProps.getMaxGradient)["return"] == typing.Optional[Float]
        assert typing.get_type_hints(SwCalprmAxisTypeProps.getMonotony)["return"] == typing.Optional[MonotonyEnum]

    def test_sw_calprm_axis_type_props_accessor_docstrings_verbatim(self):
        """Getter docstrings carry the Table 5.49 Notes verbatim; setters append the None-no-op sentence."""
        for attr, note in self.SPEC_NOTES.items():
            getter = "get" + attr[0].upper() + attr[1:]
            setter = "set" + attr[0].upper() + attr[1:]
            assert cleandoc(getattr(SwCalprmAxisTypeProps, getter).__doc__) == note
            assert cleandoc(getattr(SwCalprmAxisTypeProps, setter).__doc__) == (note + " A None value is a no-op and does not overwrite an existing %s." % attr)

    def test_sw_calprm_axis_type_props_initialization(self):
        """Test that a concrete subclass can be initialized with default values."""

        # Create a concrete subclass for testing
        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        concrete_axis_type_props = ConcreteSwCalprmAxisTypeProps()
        assert concrete_axis_type_props.getMaxGradient() is None
        assert concrete_axis_type_props.getMonotony() is None

    def test_sw_calprm_axis_type_props_max_gradient(self):
        """Test getMaxGradient/setMaxGradient (spec Table 5.49, maxGradient: Float 0..1 attr)."""

        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        props = ConcreteSwCalprmAxisTypeProps()
        gradient = Float()
        gradient.setValue(1.5)
        assert props.setMaxGradient(gradient) is props
        assert props.getMaxGradient() is gradient
        assert props.getMaxGradient().getValue() == 1.5

    def test_sw_calprm_axis_type_props_monotony(self):
        """Test getMonotony/setMonotony (spec Table 5.49, monotony: MonotonyEnum 0..1 attr)."""

        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        props = ConcreteSwCalprmAxisTypeProps()
        monotony = MonotonyEnum()
        monotony.setValue(MonotonyEnum.STRICTLY_INCREASING)
        assert props.setMonotony(monotony) is props
        assert props.getMonotony() is monotony
        assert props.getMonotony().getValue() == "strictlyIncreasing"

    def test_sw_calprm_axis_type_props_none_no_op(self):
        """Test that setMaxGradient(None)/setMonotony(None) do not overwrite existing values."""

        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        props = ConcreteSwCalprmAxisTypeProps()
        gradient = Float()
        gradient.setValue(1.5)
        props.setMaxGradient(gradient)
        monotony = MonotonyEnum()
        monotony.setValue(MonotonyEnum.STRICTLY_INCREASING)
        props.setMonotony(monotony)

        assert props.setMaxGradient(None) is props
        assert props.setMonotony(None) is props
        assert props.getMaxGradient() is gradient
        assert props.getMonotony() is monotony


class TestSwCalprmAxis:
    """Test class for SwCalprmAxis class."""

    SPEC_MEMBER_ORDER = ["category", "displayFormat", "swAxisIndex", "swCalibrationAccess", "swCalprmAxisTypeProps"]

    SPEC_NOTES = {
        "category": "This property specifies the category of a particular axis.",
        "displayFormat": "This property specifies how the axis values shall be displayed e.g. in documents or in measurement and calibration tools.",
        "swAxisIndex": 'This attribute specifies which axis is specified by the containing SwCalprmAxis. For example in a curve this is usually "1". In a map this is "1" or "2".',
        "swCalibrationAccess": "Describes the applicability of parameters and variables.",
        "swCalprmAxisTypeProps": "specific properties depending on the type of the axis.",
    }

    def _init_field_order(self) -> list:
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
            "DataDictionary",
            "CalibrationParameter.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SwCalprmAxis")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_sw_calprm_axis_class_note_verbatim(self):
        """The class docstring carries the Table 5.47 Note verbatim."""
        assert cleandoc(SwCalprmAxis.__doc__) == "This element specifies an individual input parameter axis (abscissa)."

    def test_sw_calprm_axis_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.47 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_sw_calprm_axis_accessors_follow_member_order(self):
        """Accessor groups per attribute, in spec row order; scalars getter-first."""
        expected = [
            "getCategory",
            "setCategory",
            "getDisplayFormat",
            "setDisplayFormat",
            "getSwAxisIndex",
            "setSwAxisIndex",
            "getSwCalibrationAccess",
            "setSwCalibrationAccess",
            "getSwCalprmAxisTypeProps",
            "setSwCalprmAxisTypeProps",
        ]
        for name in expected:
            assert hasattr(SwCalprmAxis, name), f"missing accessor {name}"

    def test_sw_calprm_axis_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime (Rule 0003 — no TYPE_CHECKING-only names)."""
        for name in (
            "getCategory",
            "setCategory",
            "getDisplayFormat",
            "setDisplayFormat",
            "getSwAxisIndex",
            "setSwAxisIndex",
            "getSwCalibrationAccess",
            "setSwCalibrationAccess",
            "getSwCalprmAxisTypeProps",
            "setSwCalprmAxisTypeProps",
        ):
            hints = typing.get_type_hints(getattr(SwCalprmAxis, name))
            assert hints, f"no annotations resolved for {name}"
            assert "return" in hints
        assert typing.get_type_hints(SwCalprmAxis.setSwAxisIndex)["value"] == typing.Optional[AxisIndexType]
        assert typing.get_type_hints(SwCalprmAxis.setSwCalibrationAccess)["value"] == typing.Optional[SwCalibrationAccessEnum]
        assert typing.get_type_hints(SwCalprmAxis.setCategory)["value"] == typing.Optional[CalprmAxisCategoryEnum]
        assert typing.get_type_hints(SwCalprmAxis.getSwCalprmAxisTypeProps)["return"] == typing.Optional[SwCalprmAxisTypeProps]

    def test_sw_calprm_axis_accessor_docstrings_verbatim(self):
        """Getter docstrings carry the Table 5.47 Notes verbatim; setters append the None-no-op sentence."""
        for attr, note in self.SPEC_NOTES.items():
            getter = "get" + attr[0].upper() + attr[1:]
            setter = "set" + attr[0].upper() + attr[1:]
            assert cleandoc(getattr(SwCalprmAxis, getter).__doc__) == note
            assert cleandoc(getattr(SwCalprmAxis, setter).__doc__) == (note + " A None value is a no-op and does not overwrite an existing %s." % attr)

    def test_sw_calprm_axis_initialization(self):
        """Test that a SwCalprmAxis object can be initialized with default values."""
        sw_calprm_axis = SwCalprmAxis()
        assert sw_calprm_axis.getCategory() is None
        assert sw_calprm_axis.getDisplayFormat() is None
        assert sw_calprm_axis.getSwAxisIndex() is None
        assert sw_calprm_axis.getSwCalibrationAccess() is None
        assert sw_calprm_axis.getSwCalprmAxisTypeProps() is None

    def test_sw_calprm_axis_category(self):
        """Test getCategory/setCategory (spec Table 5.47, category: CalprmAxisCategoryEnum 0..1 attr)."""
        axis = SwCalprmAxis()
        category = CalprmAxisCategoryEnum()
        category.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        assert axis.setCategory(category) is axis
        assert axis.getCategory() is category
        assert axis.getCategory().getValue() == "stdAxis"

    def test_sw_calprm_axis_display_format(self):
        """Test getDisplayFormat/setDisplayFormat (spec Table 5.47, displayFormat: DisplayFormatString 0..1 attr)."""
        axis = SwCalprmAxis()
        display_format = DisplayFormatString()
        display_format.setValue("%.2f")
        assert axis.setDisplayFormat(display_format) is axis
        assert axis.getDisplayFormat() is display_format
        assert axis.getDisplayFormat().getValue() == "%.2f"

    def test_sw_calprm_axis_sw_axis_index(self):
        """Test getSwAxisIndex/setSwAxisIndex (spec Table 5.47, swAxisIndex: AxisIndexType 0..1 attr)."""
        axis = SwCalprmAxis()
        index = AxisIndexType()
        index.setValue("1")
        assert axis.setSwAxisIndex(index) is axis
        assert axis.getSwAxisIndex() is index
        assert axis.getSwAxisIndex().getValue() == "1"

    def test_sw_calprm_axis_sw_calibration_access(self):
        """Test getSwCalibrationAccess/setSwCalibrationAccess (spec Table 5.47, swCalibrationAccess: SwCalibrationAccessEnum 0..1 attr)."""
        axis = SwCalprmAxis()
        access = SwCalibrationAccessEnum()
        access.setValue(SwCalibrationAccessEnum.READ_ONLY)
        assert axis.setSwCalibrationAccess(access) is axis
        assert axis.getSwCalibrationAccess() is access

    def test_sw_calprm_axis_sw_calprm_axis_type_props(self):
        """Test getSwCalprmAxisTypeProps/setSwCalprmAxisTypeProps (spec Table 5.47, swCalprmAxisTypeProps: SwCalprmAxisTypeProps 0..1 aggr)."""

        class ConcreteProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        axis = SwCalprmAxis()
        props = ConcreteProps()
        assert axis.setSwCalprmAxisTypeProps(props) is axis
        assert axis.getSwCalprmAxisTypeProps() is props

    def test_sw_calprm_axis_none_no_op(self):
        """Test that None setters do not overwrite existing values."""

        class ConcreteProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        axis = SwCalprmAxis()
        category = CalprmAxisCategoryEnum()
        category.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        axis.setCategory(category)
        display_format = DisplayFormatString()
        display_format.setValue("%.2f")
        axis.setDisplayFormat(display_format)
        index = AxisIndexType()
        index.setValue("1")
        axis.setSwAxisIndex(index)
        access = SwCalibrationAccessEnum()
        access.setValue(SwCalibrationAccessEnum.READ_ONLY)
        axis.setSwCalibrationAccess(access)
        props = ConcreteProps()
        axis.setSwCalprmAxisTypeProps(props)

        assert axis.setCategory(None) is axis
        assert axis.setDisplayFormat(None) is axis
        assert axis.setSwAxisIndex(None) is axis
        assert axis.setSwCalibrationAccess(None) is axis
        assert axis.setSwCalprmAxisTypeProps(None) is axis
        assert axis.getCategory() is category
        assert axis.getDisplayFormat() is display_format
        assert axis.getSwAxisIndex() is index
        assert axis.getSwCalibrationAccess() is access
        assert axis.getSwCalprmAxisTypeProps() is props


class TestSwCalprmAxisSet:
    """Test class for SwCalprmAxisSet class."""

    def test_sw_calprm_axis_set_initialization(self):
        """Test that a SwCalprmAxisSet object can be initialized with default values."""
        sw_calprm_axis_set = SwCalprmAxisSet()
        assert sw_calprm_axis_set.swCalprmAxis == []
        assert isinstance(sw_calprm_axis_set, ARObject)
        assert sw_calprm_axis_set.__class__.__doc__.strip() == ("This element specifies the input parameter axes (abscissas) of parameters (and variables, if these used adaptively).")

    def test_sw_calprm_axis_set_methods(self):
        """Test adding and getting calibration axis."""
        sw_calprm_axis_set = SwCalprmAxisSet()
        axis = SwCalprmAxis()

        assert sw_calprm_axis_set.addSwCalprmAxis(axis) is sw_calprm_axis_set
        axises = sw_calprm_axis_set.getSwCalprmAxises()
        assert axis in axises
        assert len(axises) == 1
        assert sw_calprm_axis_set.addSwCalprmAxis(None) is sw_calprm_axis_set
        assert sw_calprm_axis_set.getSwCalprmAxises() == [axis]
