"""
This module contains tests for the SystemConstant module in MSR.DataDictionary.
"""
from armodel.models.M2.MSR.DataDictionary.SystemConstant import SwSystemconst
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage


class TestSwSystemconst:
    """Test class for SwSystemconst class."""

    def test_sw_systemconst_initialization(self):
        """Test that SwSystemconst initializes with expected default values."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")

        assert sw_systemconst.swDataDefProps is None

    def test_sw_systemconst_sw_data_def_props_methods(self):
        """Test the swDataDefProps getter and setter."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")
        data_def_props = SwDataDefProps()

        result = sw_systemconst.setSwDataDefProps(data_def_props)

        assert sw_systemconst.getSwDataDefProps() == data_def_props
        assert result == sw_systemconst

    def test_sw_systemconst_inherited_referrable_methods(self):
        """Test inherited Referrable getters for parent and short name."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")

        assert sw_systemconst.getShortName() == "test_name"
        assert sw_systemconst.getParent() == parent_obj
