"""
This module contains tests for the SystemConstant module in MSR.DataDictionary.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, ARPackage
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.MSR.DataDictionary.SystemConstant import SwSystemconst


class TestSwSystemconst:
    """Test class for SwSystemconst class."""

    def test_sw_systemconst_inheritance_is_arelement(self):
        """Test that SwSystemconst is an ARElement subclass per the Table 5.120 Base row."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")

        assert isinstance(sw_systemconst, ARElement)

    def test_sw_systemconst_initialization(self):
        """Test that SwSystemconst initializes with expected default values."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")

        assert sw_systemconst.swDataDefProps is None

    def test_sw_systemconst_accessor_annotations(self):
        """Test the Optional type hints of the swDataDefProps accessors."""
        getter_hints = typing.get_type_hints(SwSystemconst.getSwDataDefProps)
        assert getter_hints["return"] == typing.Optional[SwDataDefProps]

        setter_hints = typing.get_type_hints(SwSystemconst.setSwDataDefProps)
        assert setter_hints["sw_data_def_props"] == typing.Optional[SwDataDefProps]
        assert setter_hints["return"] == SwSystemconst

    def test_sw_systemconst_sw_data_def_props_methods(self):
        """Test the swDataDefProps getter and setter."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")
        data_def_props = SwDataDefProps()

        result = sw_systemconst.setSwDataDefProps(data_def_props)

        assert sw_systemconst.getSwDataDefProps() == data_def_props
        assert result == sw_systemconst

    def test_sw_systemconst_set_sw_data_def_props_none_noop(self):
        """Test that setSwDataDefProps(None) does not overwrite an existing value."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")
        data_def_props = SwDataDefProps()
        sw_systemconst.setSwDataDefProps(data_def_props)

        sw_systemconst.setSwDataDefProps(None)

        assert sw_systemconst.getSwDataDefProps() is data_def_props

    def test_sw_systemconst_inherited_referrable_methods(self):
        """Test inherited Referrable getters for parent and short name."""
        parent_obj = ARPackage(None, "parent_test")
        sw_systemconst = SwSystemconst(parent_obj, "test_name")

        assert sw_systemconst.getShortName() == "test_name"
        assert sw_systemconst.getParent() == parent_obj
