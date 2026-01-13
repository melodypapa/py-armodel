"""
Test cases for the SystemSignalAnalyzer class.
These tests ensure 100% code coverage for the system signal analysis functionality.
"""

from unittest.mock import Mock, patch
from src.armodel.lib.system_signal import SystemSignalAnalyzer
from src.armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SystemSignal
from src.armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from src.armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestSystemSignalAnalyzer:
    """
    Test class for SystemSignalAnalyzer functionality.
    This class contains test methods for validating the behavior of
    the SystemSignalAnalyzer class, including its initialization,
    signal management, package parsing, data import, and output printing methods.
    """
    
    def test_initialization(self):
        """
        Test SystemSignalAnalyzer class initialization.
        Verifies that the SystemSignalAnalyzer can be properly instantiated
        and that it has the required attributes.
        """
        analyzer = SystemSignalAnalyzer()
        
        assert analyzer is not None
        assert hasattr(analyzer, 'system_signals')
        assert analyzer.system_signals == []
    
    def test_add_system_signal(self):
        """
        Test add_system_signal method.
        Verifies that the method properly adds a system signal to the internal list.
        """
        analyzer = SystemSignalAnalyzer()
        signal = Mock(spec=SystemSignal)
        
        analyzer.add_system_signal(signal)
        
        assert len(analyzer.system_signals) == 1
        assert signal in analyzer.system_signals
    
    def test_get_system_signals(self):
        """
        Test get_system_signals method.
        Verifies that the method properly returns the list of system signals.
        """
        analyzer = SystemSignalAnalyzer()
        signal = Mock(spec=SystemSignal)
        analyzer.add_system_signal(signal)
        
        signals = analyzer.get_system_signals()
        
        assert signals == [signal]
        # Verify that it returns the same list object (not a copy)
        assert signals is analyzer.system_signals
    
    def test_parse_pkg_with_empty_package(self):
        """
        Test parse_pkg method with an empty package.
        Verifies that the method handles empty packages without errors.
        """
        analyzer = SystemSignalAnalyzer()
        parent_pkg = Mock(spec=ARPackage)
        parent_pkg.getARPackages.return_value = []
        parent_pkg.getSystemSignals.return_value = []
        
        analyzer.parse_pkg(parent_pkg)
        
        # The system_signals list should remain empty
        assert analyzer.system_signals == []
    
    def test_parse_pkg_with_subpackages(self):
        """
        Test parse_pkg method with nested packages.
        Verifies that the method properly traverses nested packages.
        """
        analyzer = SystemSignalAnalyzer()
        parent_pkg = Mock(spec=ARPackage)
        
        # Create mock sub-packages
        sub_pkg = Mock(spec=ARPackage)
        parent_pkg.getARPackages.return_value = [sub_pkg]
        parent_pkg.getSystemSignals.return_value = []
        
        # Sub-package has no further sub-packages but has system signals
        sub_pkg.getARPackages.return_value = []
        sub_pkg.getSystemSignals.return_value = []
        
        analyzer.parse_pkg(parent_pkg)
        
        # The system_signals list should still be empty as no signals were added
        assert analyzer.system_signals == []
    
    def test_parse_pkg_with_system_signals(self):
        """
        Test parse_pkg method with system signals.
        Verifies that the method properly collects system signals.
        """
        analyzer = SystemSignalAnalyzer()
        parent_pkg = Mock(spec=ARPackage)
        
        # Create mock system signals
        signal1 = Mock(spec=SystemSignal)
        signal1.short_name = "Signal1"
        signal2 = Mock(spec=SystemSignal)
        signal2.short_name = "Signal2"
        
        parent_pkg.getARPackages.return_value = []
        parent_pkg.getSystemSignals.return_value = [signal1, signal2]
        
        analyzer.parse_pkg(parent_pkg)
        
        # The system_signals list should now contain the system signals
        assert len(analyzer.system_signals) == 2
        assert signal1 in analyzer.system_signals
        assert signal2 in analyzer.system_signals
    
    def test_import_data(self):
        """
        Test import_data method with AUTOSAR document.
        Verifies that the method properly imports data from a document.
        """
        analyzer = SystemSignalAnalyzer()
        document = Mock(spec=AUTOSAR)
        
        # Create mock package with system signals
        pkg = Mock(spec=ARPackage)
        signal = Mock(spec=SystemSignal)
        signal.short_name = "TestSignal"
        
        document.getARPackages.return_value = [pkg]
        pkg.getARPackages.return_value = []
        pkg.getSystemSignals.return_value = [signal]
        
        analyzer.import_data(document)
        
        # The system_signals list should contain the imported system signal
        assert len(analyzer.system_signals) == 1
        assert signal in analyzer.system_signals
    
    def test_print_out_default_format(self):
        """
        Test print_out method with default options.
        Verifies that the method properly prints system signals in default format.
        """
        analyzer = SystemSignalAnalyzer()
        
        # Add mock system signals
        signal1 = Mock(spec=SystemSignal)
        signal1.short_name = "SignalB"
        signal1.full_name = "Full.SignalB"
        signal2 = Mock(spec=SystemSignal)
        signal2.short_name = "SignalA"
        signal2.full_name = "Full.SignalA"
        
        analyzer.system_signals = [signal1, signal2]
        
        with patch('logging.getLogger') as mock_get_logger:
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger
            
            # Test with default options (should print short names in sorted order)
            analyzer.print_out({'format': 'short'})
            
            # Check that info was called with the expected messages
            calls = [call[0][0] for call in mock_logger.info.call_args_list if len(call[0]) > 0]
            info_calls = [call for call in calls if call not in ["== SYSTEM SIGNAL LIST =="]]
            
            # Should print short names in sorted order (SignalA, then SignalB)
            assert len(info_calls) == 2
            if len(info_calls) >= 2:
                assert info_calls[0] == "SignalA"
                assert info_calls[1] == "SignalB"
    
    def test_print_out_full_format(self):
        """
        Test print_out method with full format option.
        Verifies that the method properly prints system signals in full format.
        """
        analyzer = SystemSignalAnalyzer()
        
        # Add mock system signals
        signal1 = Mock(spec=SystemSignal)
        signal1.short_name = "SignalB"
        signal1.full_name = "Full.SignalB"
        signal2 = Mock(spec=SystemSignal)
        signal2.short_name = "SignalA"
        signal2.full_name = "Full.SignalA"
        
        analyzer.system_signals = [signal1, signal2]
        
        with patch('logging.getLogger') as mock_get_logger:
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger
            
            # Test with full format option
            analyzer.print_out({'format': 'full'})
            
            # Check that info was called with the expected messages
            calls = [call[0][0] for call in mock_logger.info.call_args_list if len(call[0]) > 0]
            info_calls = [call for call in calls if call not in ["== SYSTEM SIGNAL LIST =="]]
            
            # Should print full names in sorted order (SignalA, then SignalB)
            assert len(info_calls) == 2
            if len(info_calls) >= 2:
                assert info_calls[0] == "Full.SignalA"
                assert info_calls[1] == "Full.SignalB"