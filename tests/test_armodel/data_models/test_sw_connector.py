"""
Test suite for sw_connector module

This module tests the SwConnectorData and its subclasses including:
- SwConnectorData
- DelegationSwConnectorData
- AssemblySwConnectorData
"""

import pytest
from armodel.data_models.sw_connector import SwConnectorData, DelegationSwConnectorData, AssemblySwConnectorData


class TestSwConnectorData:
    """Test cases for the SwConnectorData class."""
    
    def test_sw_connector_data_initialization(self):
        """Test that SwConnectorData initializes with correct default values."""
        connector = SwConnectorData()
        assert connector.short_name == ""
    
    def test_sw_connector_data_short_name_assignment(self):
        """Test that short_name can be assigned and retrieved."""
        connector = SwConnectorData()
        connector.short_name = "TestConnector"
        assert connector.short_name == "TestConnector"


class TestDelegationSwConnectorData:
    """Test cases for the DelegationSwConnectorData class."""
    
    def test_delegation_sw_connector_data_initialization(self):
        """Test that DelegationSwConnectorData initializes with correct default values."""
        connector = DelegationSwConnectorData()
        
        # Check inherited attribute
        assert connector.short_name == ""
        
        # Check specific attributes
        assert connector.inner_swc == ""
        assert connector.inner_pport == ""
        assert connector.inner_rport == ""
        assert connector.outer_pport == ""
        assert connector.outer_rport == ""
    
    def test_delegation_sw_connector_data_attribute_assignment(self):
        """Test that all attributes can be assigned and retrieved."""
        connector = DelegationSwConnectorData()
        
        # Assign values to attributes
        connector.short_name = "TestDelegation"
        connector.inner_swc = "InnerSwc"
        connector.inner_pport = "InnerPport"
        connector.inner_rport = "InnerRport"
        connector.outer_pport = "OuterPport"
        connector.outer_rport = "OuterRport"
        
        # Verify assignments
        assert connector.short_name == "TestDelegation"
        assert connector.inner_swc == "InnerSwc"
        assert connector.inner_pport == "InnerPport"
        assert connector.inner_rport == "InnerRport"
        assert connector.outer_pport == "OuterPport"
        assert connector.outer_rport == "OuterRport"


class TestAssemblySwConnectorData:
    """Test cases for the AssemblySwConnectorData class."""
    
    def test_assembly_sw_connector_data_initialization(self):
        """Test that AssemblySwConnectorData initializes with correct default values."""
        connector = AssemblySwConnectorData()
        
        # Check inherited attribute
        assert connector.short_name == ""
        
        # Check specific attributes
        assert connector.provider_swc == ""
        assert connector.p_port == ""
        assert connector.r_swc == ""
        assert connector.r_port == ""
    
    def test_assembly_sw_connector_data_attribute_assignment(self):
        """Test that all attributes can be assigned and retrieved."""
        connector = AssemblySwConnectorData()
        
        # Assign values to attributes
        connector.short_name = "TestAssembly"
        connector.provider_swc = "ProviderSwc"
        connector.p_port = "Pport"
        connector.r_swc = "Rswc"
        connector.r_port = "Rport"
        
        # Verify assignments
        assert connector.short_name == "TestAssembly"
        assert connector.provider_swc == "ProviderSwc"
        assert connector.p_port == "Pport"
        assert connector.r_swc == "Rswc"
        assert connector.r_port == "Rport"