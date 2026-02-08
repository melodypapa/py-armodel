"""
Test cases for the AdminDataTransformer class.
These tests ensure 100% code coverage for the admin data transformer functionality.
"""

from unittest.mock import MagicMock, patch

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Identifiable,
)
from armodel.transformer.admin_data import AdminDataTransformer


class TestAdminDataTransformer:
    """
    Test class for AdminDataTransformer functionality.
    This class contains test methods for validating the behavior of
    the AdminDataTransformer class, including its initialization,
    process_pkg method, and remove method.
    """

    def test_initialization(self):
        """
        Test AdminDataTransformer class initialization.
        Verifies that the AdminDataTransformer can be properly instantiated
        and that it has the required logger attribute.
        """
        transformer = AdminDataTransformer()
        assert transformer is not None
        assert hasattr(transformer, 'logger')

    def test_process_pkg_with_empty_package(self):
        """
        Test process_pkg method with an empty package.
        Verifies that the method handles empty packages without errors.
        """
        transformer = AdminDataTransformer()
        root = AUTOSAR.getInstance()
        pkg = root.createARPackage("TestPackage")

        # This should not raise any exceptions
        transformer.process_pkg(pkg)

    def test_process_pkg_with_subpackages(self):
        """
        Test process_pkg method with nested packages.
        Verifies that the method properly processes nested packages.
        """
        transformer = AdminDataTransformer()
        root = AUTOSAR.getInstance()
        root_pkg = root.createARPackage("RootPackage")
        sub_pkg = root_pkg.createARPackage("SubPackage")

        with patch.object(sub_pkg, 'removeAdminData') as mock_remove_admin_data:
            transformer.process_pkg(root_pkg)
            # The method should process nested packages
            mock_remove_admin_data.assert_called_once()

    def test_process_pkg_with_describable_element(self):
        """
        Test process_pkg method with describable elements.
        Verifies that the method properly handles Describable elements.
        """
        transformer = AdminDataTransformer()
        root = AUTOSAR.getInstance()
        pkg = root.createARPackage("TestPackage")

        # Create a mock element that will be treated as Describable
        mock_element = MagicMock()
        mock_element.getShortName.return_value = "test_element"

        with patch.object(pkg, 'getElements', return_value=[mock_element]), \
             patch('armodel.transformer.admin_data.isinstance') as mock_isinstance, \
             patch.object(transformer.logger, 'debug'):
            # Mock isinstance to return True for Describable check, False for Identifiable
            def mock_isinstance_func(obj, class_info):
                if class_info == Describable:
                    return True
                return False

            mock_isinstance.side_effect = mock_isinstance_func
            transformer.process_pkg(pkg)
            # Verify that removeAdminData was called on the element
            mock_element.removeAdminData.assert_called_once()

    def test_process_pkg_with_identifiable_element(self):
        """
        Test process_pkg method with identifiable elements that are not Describable.
        Verifies that the method properly handles Identifiable elements.
        """
        transformer = AdminDataTransformer()
        root = AUTOSAR.getInstance()
        pkg = root.createARPackage("TestPackage")

        # Create a mock element that will be treated as Identifiable but not Describable
        mock_element = MagicMock()
        mock_element.getShortName.return_value = "test_element"

        with patch.object(pkg, 'getElements', return_value=[mock_element]), \
             patch('armodel.transformer.admin_data.isinstance') as mock_isinstance, \
             patch.object(transformer.logger, 'debug'):
            # Mock isinstance to return False for Describable check, True for Identifiable
            def mock_isinstance_func(obj, class_info):
                if class_info == Describable:
                    return False
                elif class_info == Identifiable:
                    return True
                return False

            mock_isinstance.side_effect = mock_isinstance_func
            transformer.process_pkg(pkg)
            # Verify that removeAdminData was called on the element
            mock_element.removeAdminData.assert_called_once()

    def test_remove_method(self):
        """
        Test remove method with AUTOSAR root object.
        Verifies that the method properly removes admin data from the root
        and processes all packages.
        """
        transformer = AdminDataTransformer()
        root = AUTOSAR.getInstance()
        pkg = root.createARPackage("TestPkg")  # Add a package to the root

        with patch.object(root, 'removeAdminData') as mock_remove_admin_data, \
             patch.object(transformer, 'process_pkg') as mock_process_pkg:
            # Mock getARPackages to return a list with our package
            transformer.remove(root)
            # Verify that removeAdminData was called on the root
            mock_remove_admin_data.assert_called_once()
            # Verify that process_pkg was called for the package in root
            mock_process_pkg.assert_called()
