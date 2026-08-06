"""
This module contains comprehensive tests for the AccessCount module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the AccessCount.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint, AccessCount, AccessCountSet
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, PositiveInteger, RefType


class TestAbstractAccessPoint:
    """Test class for AbstractAccessPoint abstract class."""

    def test_abstract_access_point_initialization(self):
        """Test AbstractAccessPoint initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            AbstractAccessPoint(ar_root, "TestAbstractAccessPoint")


class TestAccessCount:
    """Test class for AccessCount."""

    def test_initialization(self):
        """Test AccessCount initialization."""
        count = AccessCount()
        assert count is not None
        assert count.getAccessPoint() is None
        assert count.getValue() is None

    def test_access_point_setter_getter(self):
        """Test accessPoint setter and getter."""
        count = AccessCount()
        ref = RefType().setValue("/AccessPoint")
        result = count.setAccessPoint(ref)
        assert result is count
        assert count.getAccessPoint() == ref

    def test_value_setter_getter(self):
        """Test value setter and getter."""
        count = AccessCount()
        value = PositiveInteger().setValue(5)
        result = count.setValue(value)
        assert result is count
        assert count.getValue() == value

    def test_access_point_setter_none_noop(self):
        """Test accessPoint setter with None is a no-op."""
        count = AccessCount()
        ref = RefType().setValue("/AccessPoint")
        count.setAccessPoint(ref)
        count.setAccessPoint(None)
        assert count.getAccessPoint() == ref

    def test_value_setter_none_noop(self):
        """Test value setter with None is a no-op."""
        count = AccessCount()
        value = PositiveInteger().setValue(5)
        count.setValue(value)
        count.setValue(None)
        assert count.getValue() == value

    def test_all_properties(self):
        """Test setting all properties."""
        count = AccessCount()
        ref = RefType().setValue("/AccessPoint")
        value = PositiveInteger().setValue(7)
        count.setAccessPoint(ref).setValue(value)
        assert count.getAccessPoint() == ref
        assert count.getValue() == value


class TestAccessCountSet:
    """Test class for AccessCountSet."""

    def test_initialization(self):
        """Test AccessCountSet initialization."""
        acs = AccessCountSet()
        assert acs is not None
        assert acs.getAccessCounts() == []
        assert acs.getCountProfile() is None

    def test_add_access_count(self):
        """Test addAccessCount."""
        acs = AccessCountSet()
        count = AccessCount()
        result = acs.addAccessCount(count)
        assert result is acs  # Method chaining
        assert acs.getAccessCounts() == [count]

    def test_add_access_count_none_is_noop(self):
        """Test addAccessCount with None is a no-op."""
        acs = AccessCountSet()
        acs.addAccessCount(None)
        assert acs.getAccessCounts() == []

    def test_count_profile_setter_getter(self):
        """Test countProfile setter and getter."""
        acs = AccessCountSet()
        profile = NameToken().setValue("PROFILE_1")
        result = acs.setCountProfile(profile)
        assert result is acs
        assert acs.getCountProfile() == profile

    def test_count_profile_setter_none_noop(self):
        """Test countProfile setter with None is a no-op."""
        acs = AccessCountSet()
        profile = NameToken().setValue("PROFILE_1")
        acs.setCountProfile(profile)
        acs.setCountProfile(None)
        assert acs.getCountProfile() == profile
