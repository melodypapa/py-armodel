"""
Test suite for BswImplementation class in armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.

This module tests the BSW (Basic Software) implementation class which extends the base Implementation class.
It includes functionality for managing BSW-specific implementation properties like release version, 
behavior references, configuration references, and vendor-specific information.
"""


from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, RevisionLabelString, Identifier
from armodel import AUTOSAR


class TestBswImplementation:
    """Test cases for BswImplementation class - represents BSW module implementation details."""
    
    def test_initialization(self):
        """Test BswImplementation initialization with default values."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        assert impl.short_name == "test_bsw_implementation"
        assert impl.getArReleaseVersion() is None
        assert impl.getBehaviorRef() is None
        assert impl.getPreconfiguredConfigurationRefs() == []
        assert impl.getRecommendedConfigurationRefs() == []
        assert impl.getVendorApiInfix() is None
        assert impl.getVendorSpecificModuleDefRefs() == []
    
    def test_get_set_ar_release_version(self):
        """Test getter and setter for AR release version."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        version = RevisionLabelString()
        version.setValue("4.3.0")
        result = impl.setArReleaseVersion(version)
        
        assert result == impl
        assert impl.getArReleaseVersion() == version
    
    def test_get_set_behavior_ref(self):
        """Test getter and setter for behavior reference."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        ref = RefType()
        ref.setValue("/path/to/behavior")
        result = impl.setBehaviorRef(ref)
        
        assert result == impl
        assert impl.getBehaviorRef() == ref
    
    def test_get_preconfigured_configuration_refs(self):
        """Test getter for preconfigured configuration references."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        assert impl.getPreconfiguredConfigurationRefs() == []
    
    def test_add_preconfigured_configuration_ref(self):
        """Test adding preconfigured configuration reference."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        ref = RefType()
        ref.setValue("/path/to/config")
        result = impl.addPreconfiguredConfigurationRef(ref)
        
        assert result == impl
        assert impl.getPreconfiguredConfigurationRefs() == [ref]
    
    def test_get_recommended_configuration_refs(self):
        """Test getter for recommended configuration references."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        assert impl.getRecommendedConfigurationRefs() == []
    
    def test_add_recommended_configuration_ref(self):
        """Test adding recommended configuration reference."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        ref = RefType()
        ref.setValue("/path/to/recommended/config")
        result = impl.addRecommendedConfigurationRef(ref)
        
        assert result == impl
        assert impl.getRecommendedConfigurationRefs() == [ref]
    
    def test_get_set_vendor_api_infix(self):
        """Test getter and setter for vendor API infix."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        infix = Identifier()
        infix.setValue("_VENDOR_")
        result = impl.setVendorApiInfix(infix)
        
        assert result == impl
        assert impl.getVendorApiInfix() == infix
    
    def test_get_vendor_specific_module_def_refs(self):
        """Test getter for vendor-specific module definition references."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        assert impl.getVendorSpecificModuleDefRefs() == []
    
    def test_add_vendor_specific_module_def_ref(self):
        """Test adding vendor-specific module definition reference."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        impl = BswImplementation(ar_root, "test_bsw_implementation")
        
        ref = RefType()
        ref.setValue("/path/to/vendor/module")
        result = impl.addVendorSpecificModuleDefRef(ref)
        
        assert result == impl
        assert impl.getVendorSpecificModuleDefRefs() == [ref]