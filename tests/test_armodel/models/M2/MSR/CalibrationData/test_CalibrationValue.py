"""
This module contains tests for the CalibrationValue module in MSR.CalibrationData.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalOrText
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, RefType, VerbatimString
from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont, SwValues, ValueGroup
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName


class TestSwValues:
    """Test class for SwValues class."""

    def test_initialization(self):
        """Test SwValues initialization defaults and inheritance."""
        sw_values = SwValues()
        assert isinstance(sw_values, ARObject)
        assert sw_values.getVs() == []
        assert sw_values.getVfs() == []
        assert sw_values.getVg() is None
        assert sw_values.getVt() is None
        assert sw_values.getVtfs() == []

    def test_add_get_vs(self):
        """Test addV/getVs append order, chaining and None no-op."""
        sw_values = SwValues()
        v1 = Numerical().setValue("1.5")
        v2 = Numerical().setValue("2.5")

        assert sw_values.addV(v1) is sw_values
        sw_values.addV(v2)
        assert sw_values.getVs() == [v1, v2]

        sw_values.addV(None)
        assert sw_values.getVs() == [v1, v2]

    def test_add_get_vfs(self):
        """Test addVf/getVfs append order, chaining and None no-op."""
        sw_values = SwValues()
        vf1 = Numerical().setValue("0.5")
        vf2 = Numerical().setValue("1.5")

        assert sw_values.addVf(vf1) is sw_values
        sw_values.addVf(vf2)
        assert sw_values.getVfs() == [vf1, vf2]

        sw_values.addVf(None)
        assert sw_values.getVfs() == [vf1, vf2]

    def test_get_set_vg(self):
        """Test getVg/setVg round-trip, chaining and None no-op."""
        sw_values = SwValues()
        vg = ValueGroup()

        assert sw_values.setVg(vg) is sw_values
        assert sw_values.getVg() is vg

        sw_values.setVg(None)
        assert sw_values.getVg() is vg

    def test_get_set_vt(self):
        """Test getVt/setVt round-trip, chaining and None no-op."""
        sw_values = SwValues()
        vt = VerbatimString().setValue("a|b")

        assert sw_values.setVt(vt) is sw_values
        assert sw_values.getVt() is vt

        sw_values.setVt(None)
        assert sw_values.getVt() is vt

    def test_add_get_vtfs(self):
        """Test addVtf/getVtfs append order, chaining and None no-op."""
        sw_values = SwValues()
        vtf1 = NumericalOrText()
        vtf2 = NumericalOrText()

        assert sw_values.addVtf(vtf1) is sw_values
        sw_values.addVtf(vtf2)
        assert sw_values.getVtfs() == [vtf1, vtf2]

        sw_values.addVtf(None)
        assert sw_values.getVtfs() == [vtf1, vtf2]


class TestSwValueCont:
    """Test class for SwValueCont class."""

    def test_sw_value_cont_initialization(self):
        """Test that a SwValueCont object can be initialized with default values."""
        sw_value_cont = SwValueCont()
        assert sw_value_cont.swArraysize is None
        assert sw_value_cont.swValuesPhys is None
        assert sw_value_cont.unitRef is None
        assert sw_value_cont.unitDisplayName is None
        assert isinstance(sw_value_cont, ARObject)
        assert sw_value_cont.__class__.__doc__.strip() == "This metaclass represents the content of one particular SwInstance."

    def test_sw_value_cont_array_size_methods(self):
        """Test the swArraysize getter and setter."""
        sw_value_cont = SwValueCont()
        array_size = ValueList()

        result = sw_value_cont.setSwArraysize(array_size)
        assert sw_value_cont.getSwArraysize() == array_size
        assert result == sw_value_cont
        assert sw_value_cont.setSwArraysize(None) is sw_value_cont
        assert sw_value_cont.getSwArraysize() is array_size

    def test_sw_value_cont_sw_values_phys_methods(self):
        """Test the swValuesPhys getter and setter."""
        sw_value_cont = SwValueCont()
        values_phys = SwValues()

        result = sw_value_cont.setSwValuesPhys(values_phys)
        assert sw_value_cont.getSwValuesPhys() == values_phys
        assert result == sw_value_cont
        assert sw_value_cont.setSwValuesPhys(None) is sw_value_cont
        assert sw_value_cont.getSwValuesPhys() is values_phys

    def test_sw_value_cont_unit_ref_methods(self):
        """Test the unitRef getter and setter."""
        sw_value_cont = SwValueCont()
        unit_ref = RefType()

        result = sw_value_cont.setUnitRef(unit_ref)
        assert sw_value_cont.getUnitRef() == unit_ref
        assert result == sw_value_cont
        assert sw_value_cont.setUnitRef(None) is sw_value_cont
        assert sw_value_cont.getUnitRef() is unit_ref

    def test_sw_value_cont_unit_display_name_methods(self):
        """Test the unitDisplayName getter and setter."""
        sw_value_cont = SwValueCont()
        unit_display_name = SingleLanguageUnitNames()

        result = sw_value_cont.setUnitDisplayName(unit_display_name)
        assert sw_value_cont.getUnitDisplayName() == unit_display_name
        assert result == sw_value_cont
        assert sw_value_cont.setUnitDisplayName(None) is sw_value_cont
        assert sw_value_cont.getUnitDisplayName() is unit_display_name


class TestValueGroup:
    """Test class for ValueGroup class."""

    def test_initialization(self):
        """Test ValueGroup initialization defaults and inheritance."""
        vg = ValueGroup()
        assert isinstance(vg, ARObject)
        assert vg.getLabel() is None
        assert vg.getVgContents() is None

    def test_get_set_label(self):
        """Test getLabel/setLabel round-trip, chaining and None no-op."""
        vg = ValueGroup()
        label = MultilanguageLongName()
        assert vg.setLabel(label) is vg
        assert vg.getLabel() is label

        vg.setLabel(None)
        assert vg.getLabel() is label

    def test_get_set_vg_contents(self):
        """Test getVgContents/setVgContents round-trip, chaining and None no-op."""
        vg = ValueGroup()
        contents = SwValues()
        assert vg.setVgContents(contents) is vg
        assert vg.getVgContents() is contents

        vg.setVgContents(None)
        assert vg.getVgContents() is contents


CLASS_NOTE_SW_AXIS_CONT = (
    "This represents the values for the axis of a compound primitive (curve, map). For standard and fix axes, "
    "SwAxisCont contains the values of the axis directly. The axis values of SwAxisCont with the category "
    "COM_AXIS, RES_AXIS are for display only. For editing and processing, only the values in the related "
    "GroupAxis are binding."
)

CATEGORY_NOTE = "This category specifies the particular axis types: " "\u2022 STD_AXIS \u2022 COM_AXIS \u2022 RES_AXIS (swArraysize necessary) Tags: xml.sequenceOffset=20"

SW_ARRAYSIZE_NOTE = (
    "For multidimensional compound primitivies (curve, map ...) it is necessary to know the dimensions." "They are specified using swArraySize. " "\u2022 RES_AXIS Tags: xml.sequenceOffset=70"
)

SW_AXIS_INDEX_NOTE = (
    "This property allows to explicitly assign the axis contents to a particular axis. It is specified by "
    "numbers where 1 corresponds to the x-axis. It is also possible to derive the axis association from the "
    "sequence of the parent. Tags: xml.sequenceOffset=50"
)

SW_VALUES_PHYS_NOTE = "swValuesPhys represents the values in the physical domain. Tags: xml.sequenceOffset=80"

UNIT_NOTE = "This represents the physical unit of the provided values. Tags: xml.sequenceOffset=30"

UNIT_DISPLAY_NAME_NOTE = "This represents the display name which is used for the physical unit of the axis. Tags: xml.sequenceOffset=40"


class TestSwAxisCont:
    def test_import_location_and_inheritance(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        axis_cont = SwAxisCont()
        assert isinstance(axis_cont, ARObject)

    def test_initialization(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        axis_cont = SwAxisCont()
        assert axis_cont.getCategory() is None
        assert axis_cont.getSwArraysize() is None
        assert axis_cont.getSwAxisIndex() is None
        assert axis_cont.getSwValuesPhys() is None
        assert axis_cont.getUnitRef() is None
        assert axis_cont.getUnitDisplayName() is None

    def test_class_docstring_verbatim(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        docstring = (SwAxisCont.__doc__ or "").strip()
        assert docstring.startswith(CLASS_NOTE_SW_AXIS_CONT)
        assert "[constr_2050]" in docstring

    def test_get_set_category(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont
        from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum

        axis_cont = SwAxisCont()
        category = CalprmAxisCategoryEnum().setValue(CalprmAxisCategoryEnum.STD_AXIS)

        assert axis_cont.setCategory(category) is axis_cont
        assert axis_cont.getCategory() is category

        axis_cont.setCategory(None)
        assert axis_cont.getCategory() is category

    def test_get_set_sw_arraysize(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        axis_cont = SwAxisCont()
        arraysize = ValueList()

        assert axis_cont.setSwArraysize(arraysize) is axis_cont
        assert axis_cont.getSwArraysize() is arraysize

        axis_cont.setSwArraysize(None)
        assert axis_cont.getSwArraysize() is arraysize

    def test_get_set_sw_axis_index(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont
        from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType

        axis_cont = SwAxisCont()
        axis_index = AxisIndexType().setValue("1")

        assert axis_cont.setSwAxisIndex(axis_index) is axis_cont
        assert axis_cont.getSwAxisIndex() is axis_index

        axis_cont.setSwAxisIndex(None)
        assert axis_cont.getSwAxisIndex() is axis_index

    def test_get_set_sw_values_phys(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        axis_cont = SwAxisCont()
        values = SwValues()

        assert axis_cont.setSwValuesPhys(values) is axis_cont
        assert axis_cont.getSwValuesPhys() is values

        axis_cont.setSwValuesPhys(None)
        assert axis_cont.getSwValuesPhys() is values

    def test_get_set_unit_ref(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        axis_cont = SwAxisCont()
        unit_ref = RefType().setValue("/Units/Nm")
        unit_ref.setDest("UNIT")

        assert axis_cont.setUnitRef(unit_ref) is axis_cont
        assert axis_cont.getUnitRef() is unit_ref

        axis_cont.setUnitRef(None)
        assert axis_cont.getUnitRef() is unit_ref

    def test_get_set_unit_display_name(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        axis_cont = SwAxisCont()
        display_name = SingleLanguageUnitNames()

        assert axis_cont.setUnitDisplayName(display_name) is axis_cont
        assert axis_cont.getUnitDisplayName() is display_name

        axis_cont.setUnitDisplayName(None)
        assert axis_cont.getUnitDisplayName() is display_name

    def test_member_docstrings_verbatim(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwAxisCont

        axis_cont = SwAxisCont()
        assert (axis_cont.getCategory.__doc__ or "").strip() == CATEGORY_NOTE
        assert (axis_cont.setCategory.__doc__ or "").strip().split("\n")[0] == CATEGORY_NOTE
        assert (axis_cont.getSwArraysize.__doc__ or "").strip() == SW_ARRAYSIZE_NOTE
        assert (axis_cont.setSwArraysize.__doc__ or "").strip().split("\n")[0] == SW_ARRAYSIZE_NOTE
        assert (axis_cont.getSwAxisIndex.__doc__ or "").strip() == SW_AXIS_INDEX_NOTE
        assert (axis_cont.setSwAxisIndex.__doc__ or "").strip().split("\n")[0] == SW_AXIS_INDEX_NOTE
        assert (axis_cont.getSwValuesPhys.__doc__ or "").strip() == SW_VALUES_PHYS_NOTE
        assert (axis_cont.setSwValuesPhys.__doc__ or "").strip().split("\n")[0] == SW_VALUES_PHYS_NOTE
        assert (axis_cont.getUnitRef.__doc__ or "").strip() == UNIT_NOTE
        assert (axis_cont.setUnitRef.__doc__ or "").strip().split("\n")[0] == UNIT_NOTE
        assert (axis_cont.getUnitDisplayName.__doc__ or "").strip() == UNIT_DISPLAY_NAME_NOTE
        assert (axis_cont.setUnitDisplayName.__doc__ or "").strip().split("\n")[0] == UNIT_DISPLAY_NAME_NOTE
