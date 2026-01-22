"""
Test cases for the SwComponentAnalyzer class.
These tests ensure 100% code coverage for the software component analysis functionality.
"""

from unittest.mock import Mock, patch
from src.armodel.lib.sw_component import SwComponentAnalyzer
from src.armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from src.armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from src.armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType


class TestSwComponentAnalyzer:
    """
    Test class for SwComponentAnalyzer functionality.
    This class contains test methods for validating the behavior of
    the SwComponentAnalyzer class, including its initialization,
    package parsing, data import, and output printing methods.
    """
    
    def test_initialization(self):
        """
        Test SwComponentAnalyzer class initialization.
        Verifies that the SwComponentAnalyzer can be properly instantiated
        and that it has the required attributes.
        """
        analyzer = SwComponentAnalyzer()
        
        assert analyzer is not None
        assert hasattr(analyzer, 'swcs')
        assert analyzer.swcs == []
    
    def test_parse_pkg_with_empty_package(self):
        """
        Test parse_pkg method with an empty package.
        Verifies that the method handles empty packages without errors.
        """
        analyzer = SwComponentAnalyzer()
        parent_pkg = Mock(spec=ARPackage)
        parent_pkg.getARPackages.return_value = []
        parent_pkg.getSwComponentTypes.return_value = []
        
        analyzer.parse_pkg(parent_pkg)
        
        # The swcs list should remain empty
        assert analyzer.swcs == []
    
    def test_parse_pkg_with_subpackages(self):
        """
        Test parse_pkg method with nested packages.
        Verifies that the method properly traverses nested packages.
        """
        analyzer = SwComponentAnalyzer()
        parent_pkg = Mock(spec=ARPackage)
        
        # Create mock sub-packages
        sub_pkg1 = Mock(spec=ARPackage)
        sub_pkg2 = Mock(spec=ARPackage)
        parent_pkg.getARPackages.return_value = [sub_pkg1, sub_pkg2]
        parent_pkg.getSwComponentTypes.return_value = []
        
        # Sub-packages have no further sub-packages but have SWCs
        sub_pkg1.getARPackages.return_value = []
        sub_pkg1.getSwComponentTypes.return_value = []
        sub_pkg2.getARPackages.return_value = []
        sub_pkg2.getSwComponentTypes.return_value = []
        
        analyzer.parse_pkg(parent_pkg)
        
        # The swcs list should still be empty as no SWCs were added
        assert analyzer.swcs == []
    
    def test_parse_pkg_with_sw_component_types(self):
        """
        Test parse_pkg method with SW component types.
        Verifies that the method properly collects SW component types.
        """
        analyzer = SwComponentAnalyzer()
        parent_pkg = Mock(spec=ARPackage)
        
        # Create mock SW components
        swc1 = Mock(spec=AtomicSwComponentType)
        swc1.short_name = "Component1"
        swc2 = Mock(spec=AtomicSwComponentType)
        swc2.short_name = "Component2"
        
        parent_pkg.getARPackages.return_value = []
        parent_pkg.getSwComponentTypes.return_value = [swc1, swc2]
        
        analyzer.parse_pkg(parent_pkg)
        
        # The swcs list should now contain the SW components
        assert len(analyzer.swcs) == 2
        assert swc1 in analyzer.swcs
        assert swc2 in analyzer.swcs
    
    def test_import_data(self):
        """
        Test import_data method with AUTOSAR document.
        Verifies that the method properly imports data from a document.
        """
        analyzer = SwComponentAnalyzer()
        document = Mock(spec=AUTOSAR)
        
        # Create mock package with SW components
        pkg = Mock(spec=ARPackage)
        swc = Mock(spec=AtomicSwComponentType)
        swc.short_name = "TestComponent"
        
        document.getARPackages.return_value = [pkg]
        pkg.getARPackages.return_value = []
        pkg.getSwComponentTypes.return_value = [swc]
        
        analyzer.import_data(document)
        
        # The swcs list should contain the imported SW component
        assert len(analyzer.swcs) == 1
        assert swc in analyzer.swcs
    
    def test_print_out_default_format(self):
        """
        Test print_out method with default options.
        Verifies that the method properly prints SWCs in default format.
        """
        analyzer = SwComponentAnalyzer()
        
        # Add mock SW components
        swc1 = Mock(spec=AtomicSwComponentType)
        swc1.short_name = "ComponentB"
        swc1.full_name = "Full.ComponentB"
        swc2 = Mock(spec=AtomicSwComponentType)
        swc2.short_name = "ComponentA"
        swc2.full_name = "Full.ComponentA"
        
        analyzer.swcs = [swc1, swc2]
        
        with patch('logging.getLogger') as mock_get_logger:
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger
            
            # Test with default options (should print short names in sorted order)
            # The original code expects 'filter' and 'format' keys, so provide defaults
            analyzer.print_out({'filter': None, 'format': 'short'})
            
            # Check that info was called with the expected messages
            calls = [call[0][0] for call in mock_logger.info.call_args_list if len(call[0]) > 0]
            info_calls = [call for call in calls if call not in ["== SW-C LIST =="]]
            
            # Should print short names in sorted order (ComponentA, then ComponentB)
            assert len(info_calls) == 2
            if len(info_calls) >= 2:
                assert info_calls[0] == "ComponentA" 
                assert info_calls[1] == "ComponentB"
    
    def test_print_out_long_format(self):
        """
        Test print_out method with long format option.
        Verifies that the method properly prints SWCs in long format.
        """
        analyzer = SwComponentAnalyzer()
        
        # Add mock SW components
        swc1 = Mock(spec=AtomicSwComponentType)
        swc1.short_name = "ComponentB"
        swc1.full_name = "Full.ComponentB"
        swc2 = Mock(spec=AtomicSwComponentType)
        swc2.short_name = "ComponentA"
        swc2.full_name = "Full.ComponentA"
        
        analyzer.swcs = [swc1, swc2]
        
        with patch('logging.getLogger') as mock_get_logger:
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger
            
            # Test with long format option
            analyzer.print_out({'filter': None, 'format': 'long'})
            
            # Check that info was called with the expected messages
            calls = [call[0][0] for call in mock_logger.info.call_args_list if len(call[0]) > 0]
            info_calls = [call for call in calls if call not in ["== SW-C LIST =="]]
            
            # Should print full names in sorted order (ComponentA, then ComponentB)
            assert len(info_calls) == 2
            if len(info_calls) >= 2:
                assert info_calls[0] == "Full.ComponentA"
                assert info_calls[1] == "Full.ComponentB"
    
    def test_print_out_composition_filter(self):
        """
        Test print_out method with CompositionSwComponent filter.
        Verifies that the method properly filters SWCs by type.
        """
        analyzer = SwComponentAnalyzer()
        
        # Create mock SW components of different types but make them properly recognizable
        # We'll set up the mock to return True/False for isinstance checks with specific types
        atomic_swc = Mock()
        atomic_swc.short_name = "AtomicComponent"
        atomic_swc.full_name = "Full.AtomicComponent"
        type(atomic_swc).return_value = False  # isinstance(atomic_swc, CompositionSwComponentType) should return False
        
        composition_swc = Mock()
        composition_swc.short_name = "CompositionComponent"
        composition_swc.full_name = "Full.CompositionComponent"
        type(composition_swc).return_value = True  # isinstance(composition_swc, CompositionSwComponentType) should return True
        
        analyzer.swcs = [atomic_swc, composition_swc]
        
        with patch('logging.getLogger') as mock_get_logger:
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger
            
            # For this test, we'll mock the isinstance check within the print_out method context
            # Since the method uses isinstance(), we need to make it return our desired values
            with patch('src.armodel.lib.sw_component.isinstance') as mock_isinstance:
                # Configure the mock to return appropriate values for our test case
                def side_effect(obj, class_info):
                    if class_info.__name__ == 'CompositionSwComponentType':
                        if obj == composition_swc:
                            return True
                        elif obj == atomic_swc:
                            return False
                    return isinstance(obj, class_info)
                
                mock_isinstance.side_effect = side_effect
                
                # Test with composition filter
                analyzer.print_out({'filter': 'CompositionSwComponent', 'format': 'short'})
                
                # Check that info was called with the expected messages
                calls = [call[0][0] for call in mock_logger.info.call_args_list if len(call[0]) > 0]
                info_calls = [call for call in calls if call not in ["== SW-C LIST =="]]
                
                # Should only print the CompositionSwComponent
                assert len(info_calls) == 1
                assert info_calls[0] == "CompositionComponent"