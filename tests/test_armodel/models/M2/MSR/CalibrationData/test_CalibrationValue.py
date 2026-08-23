"""
This module contains tests for the CalibrationValue module in MSR.CalibrationData.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalOrText
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType, VerbatimString
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
        v1 = ARNumerical().setValue("1.5")
        v2 = ARNumerical().setValue("2.5")

        assert sw_values.addV(v1) is sw_values
        sw_values.addV(v2)
        assert sw_values.getVs() == [v1, v2]

        sw_values.addV(None)
        assert sw_values.getVs() == [v1, v2]

    def test_add_get_vfs(self):
        """Test addVf/getVfs append order, chaining and None no-op."""
        sw_values = SwValues()
        vf1 = ARNumerical().setValue("0.5")
        vf2 = ARNumerical().setValue("1.5")

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

    def test_sw_value_cont_array_size_methods(self):
        """Test the swArraysize getter and setter."""
        sw_value_cont = SwValueCont()
        array_size = ValueList()

        result = sw_value_cont.setSwArraysize(array_size)
        assert sw_value_cont.getSwArraysize() == array_size
        assert result == sw_value_cont

    def test_sw_value_cont_sw_values_phys_methods(self):
        """Test the swValuesPhys getter and setter."""
        sw_value_cont = SwValueCont()
        values_phys = SwValues()

        result = sw_value_cont.setSwValuesPhys(values_phys)
        assert sw_value_cont.getSwValuesPhys() == values_phys
        assert result == sw_value_cont

    def test_sw_value_cont_unit_ref_methods(self):
        """Test the unitRef getter and setter."""
        sw_value_cont = SwValueCont()
        unit_ref = RefType()

        result = sw_value_cont.setUnitRef(unit_ref)
        assert sw_value_cont.getUnitRef() == unit_ref
        assert result == sw_value_cont

    def test_sw_value_cont_unit_display_name_methods(self):
        """Test the unitDisplayName getter and setter."""
        sw_value_cont = SwValueCont()
        unit_display_name = SingleLanguageUnitNames()

        result = sw_value_cont.setUnitDisplayName(unit_display_name)
        assert sw_value_cont.getUnitDisplayName() == unit_display_name
        assert result == sw_value_cont


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
