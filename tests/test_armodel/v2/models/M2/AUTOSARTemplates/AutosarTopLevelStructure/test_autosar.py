"""
Test module for AUTOSAR.py.

This file tests the AUTOSAR singleton class.

Tests cover:
- Singleton pattern
- Property getter/setter methods
- AUTOSAR-compatible method delegation
- Fluent method chaining
- Type validation
- Collection management
- Extended attributes (CODING_RULE_V2_00014)
- AUTOSAR release version management
"""
import pytest

from armodel.v2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    AUTOSAR,
)


class TestAUTOSAR:
    """Test class for AUTOSAR singleton functionality."""

    def test_autosar_can_be_instantiated(self):
        """Test that AUTOSAR can be instantiated."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR()
        assert obj is not None

    def test_autosar_singleton_pattern(self):
        """Test that AUTOSAR follows singleton pattern."""
        AUTOSAR.resetInstance()

        # Get first instance
        instance1 = AUTOSAR.getInstance()
        assert instance1 is not None

        # Get second instance - should be same object
        instance2 = AUTOSAR.getInstance()
        assert instance1 is instance2

    def test_autosar_reset_instance(self):
        """Test that resetInstance clears the singleton."""
        AUTOSAR.resetInstance()

        # Get first instance
        instance1 = AUTOSAR.getInstance()
        assert instance1 is not None

        # Reset and get new instance
        AUTOSAR.resetInstance()
        instance2 = AUTOSAR.getInstance()
        assert instance2 is not None

        # Should be different objects after reset
        assert instance1 is not instance2

    def test_autosar_ar_packages_initialization(self):
        """Test that ar_packages property is initialized to empty list."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.ar_packages == []

    def test_autosar_admin_data_initialization(self):
        """Test that admin_data property is initialized to None."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.admin_data is None

    def test_autosar_file_info_initialization(self):
        """Test that file_info property is initialized to None."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.file_info is None

    def test_autosar_introduction_initialization(self):
        """Test that introduction property is initialized to None."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.introduction is None

    def test_autosar_admin_data_setter_none(self):
        """Test admin_data property setter with None."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        obj.admin_data = None
        assert obj.admin_data is None

    def test_autosar_file_info_setter_none(self):
        """Test file_info property setter with None."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        obj.file_info = None
        assert obj.file_info is None

    def test_autosar_introduction_setter_none(self):
        """Test introduction property setter with None."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        obj.introduction = None
        assert obj.introduction is None

    def test_autosar_admin_data_type_validation(self):
        """Test admin_data property setter type validation."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        with pytest.raises(TypeError, match="adminData must be AdminData or None"):
            obj.admin_data = "invalid"  # Wrong type

    def test_autosar_file_info_type_validation(self):
        """Test file_info property setter type validation."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        with pytest.raises(TypeError, match="fileInfo must be FileInfoComment or None"):
            obj.file_info = "invalid"  # Wrong type

    def test_autosar_introduction_type_validation(self):
        """Test introduction property setter type validation."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        with pytest.raises(
            TypeError, match="introduction must be DocumentationBlock or None"
        ):
            obj.introduction = "invalid"  # Wrong type

    def test_autosar_ar_package_property(self):
        """Test ar_package property alias for ar_packages."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.ar_package == obj.ar_packages

    def test_autosar_get_admin_data_delegates_to_property(self):
        """Test that getAdminData delegates to admin_data property."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.getAdminData() is None

    def test_autosar_set_admin_data_delegates_to_property(self):
        """Test that setAdminData delegates to admin_data property."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = obj.setAdminData(None)
        assert result is obj  # Method chaining
        assert obj.getAdminData() is None

    def test_autosar_get_ar_package_delegates_to_property(self):
        """Test that getArPackage delegates to ar_package property."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.getArPackage() == []

    def test_autosar_get_file_info_delegates_to_property(self):
        """Test that getFileInfo delegates to file_info property."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.getFileInfo() is None

    def test_autosar_set_file_info_delegates_to_property(self):
        """Test that setFileInfo delegates to file_info property."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = obj.setFileInfo(None)
        assert result is obj  # Method chaining
        assert obj.getFileInfo() is None

    def test_autosar_get_introduction_delegates_to_property(self):
        """Test that getIntroduction delegates to introduction property."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.getIntroduction() is None

    def test_autosar_set_introduction_delegates_to_property(self):
        """Test that setIntroduction delegates to introduction property."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = obj.setIntroduction(None)
        assert result is obj  # Method chaining
        assert obj.getIntroduction() is None

    def test_autosar_with_admin_data_fluent_method(self):
        """Test with_admin_data fluent method (CODING_RULE_V2_00019)."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = obj.with_admin_data(None)
        assert result is obj  # Method chaining
        assert obj.admin_data is None

    def test_autosar_with_file_info_fluent_method(self):
        """Test with_file_info fluent method (CODING_RULE_V2_00019)."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = obj.with_file_info(None)
        assert result is obj  # Method chaining
        assert obj.file_info is None

    def test_autosar_with_introduction_fluent_method(self):
        """Test with_introduction fluent method (CODING_RULE_V2_00019)."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = obj.with_introduction(None)
        assert result is obj  # Method chaining
        assert obj.introduction is None

    def test_autosar_method_chaining(self):
        """Test that methods can be chained together."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = obj.setAdminData(None).setFileInfo(None).setIntroduction(None)
        assert result is obj

    def test_autosar_fluent_method_chaining(self):
        """Test that fluent methods can be chained together."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = (
            obj.with_admin_data(None)
            .with_file_info(None)
            .with_introduction(None)
        )
        assert result is obj

    def test_autosar_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        obj.setExtendedAttribute("custom_key", "custom_value")
        assert obj.getExtendedAttribute("custom_key") == "custom_value"

    def test_autosar_default_extended_attributes(self):
        """Test that AUTOSAR has default extended attributes."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.getExtendedAttribute("schema_version") == "3.2.3"
        assert obj.getExtendedAttribute("xmlns") == "http://autosar.org/3.2.3"

    def test_autosar_set_ar_release(self):
        """Test setARRelease class method."""
        AUTOSAR.resetInstance()
        AUTOSAR.getInstance()  # Create instance first
        AUTOSAR.setARRelease("R23-11")
        assert AUTOSAR.getARRelease() == "R23-11"

    def test_autosar_get_ar_release_none_before_set(self):
        """Test that getARRelease returns None before setARRelease is called."""
        AUTOSAR.resetInstance()
        AUTOSAR.getInstance()  # Create instance first
        assert AUTOSAR.getARRelease() is None

    def test_autosar_get_ar_release_after_reset(self):
        """Test that getARRelease returns None after resetInstance."""
        AUTOSAR.resetInstance()
        AUTOSAR.getInstance()  # Create instance first
        AUTOSAR.setARRelease("R23-11")
        AUTOSAR.resetInstance()
        assert AUTOSAR.getARRelease() is None

    def test_autosar_set_ar_release_multiple_versions(self):
        """Test setARRelease with multiple version updates."""
        AUTOSAR.resetInstance()
        AUTOSAR.getInstance()  # Create instance first
        AUTOSAR.setARRelease("R23-11")
        assert AUTOSAR.getARRelease() == "R23-11"

        AUTOSAR.setARRelease("R24-11")
        assert AUTOSAR.getARRelease() == "R24-11"

        AUTOSAR.setARRelease("4.0.3")
        assert AUTOSAR.getARRelease() == "4.0.3"

    def test_autosar_inherits_from_ar_object(self):
        """Test that AUTOSAR inherits from ARObject."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
            ARObject,
        )

        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert isinstance(obj, ARObject)

    def test_autosar_get_tag_name(self):
        """Test getTagName method."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        assert obj.getTagName() == "AUTOSAR"

    def test_autosar_add_package(self):
        """Test adding packages to AUTOSAR."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()

        pkg = AUTOSAR()
        pkg.shortName = "TestPackage"

        obj.ar_packages.append(pkg)

        assert len(obj.ar_packages) == 1
        assert obj.ar_packages[0] is pkg

    def test_autosar_multiple_getinstance_calls(self):
        """Test that multiple getInstance calls return the same instance."""
        AUTOSAR.resetInstance()
        instance1 = AUTOSAR.getInstance()
        instance2 = AUTOSAR.getInstance()
        instance3 = AUTOSAR.getInstance()

        assert instance1 is instance2
        assert instance2 is instance3
        assert instance1 is instance3

    def test_autosar_set_ar_release_on_instance(self):
        """Test setARRelease on instance method."""
        AUTOSAR.resetInstance()
        instance = AUTOSAR.getInstance()
        
        # Set ARRelease on instance
        instance.setExtendedAttribute("ar_release", "R23-11")
        
        # Verify it's set
        assert instance.getExtendedAttribute("ar_release") == "R23-11"
        
        # Verify class method also returns it
        assert AUTOSAR.getARRelease() == "R23-11"

    def test_autosar_mixed_method_chaining(self):
        """Test mixing setters and fluent methods."""
        AUTOSAR.resetInstance()
        obj = AUTOSAR.getInstance()
        result = (
            obj.setAdminData(None)
            .with_file_info(None)
            .setIntroduction(None)
            .with_admin_data(None)
        )
        assert result is obj