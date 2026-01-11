"""
This module contains comprehensive tests for the EndToEndProtection module in SWComponentTemplate.
Tests cover all classes and methods in the EndToEndProtection.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndDescription, EndToEndProtectionVariablePrototype, EndToEndProtectionISignalIPdu,
    EndToEndProtection, EndToEndProtectionSet
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType, NameToken, PositiveInteger
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef


class TestEndToEndDescription:
    """Test class for EndToEndDescription class."""
    
    def test_end_to_end_description_initialization(self):
        """Test EndToEndDescription initialization and methods."""
        description = EndToEndDescription()
        assert description.category is None
        assert description.counterOffset is None
        assert description.crcOffset is None
        assert description.dataIds == []
        assert description.dataIdMode is None
        assert description.dataIdNibbleOffset is None
        assert description.dataLength is None
        assert description.maxDeltaCounterInit is None
        assert description.maxNoNewOrRepeatedData is None
        assert description.syncCounterInit is None
        
        # Test setters and getters
        category = NameToken()
        category.setValue("TestCategory")
        description.setCategory(category)
        assert description.getCategory() == category
        
        counter_offset = PositiveInteger()
        counter_offset.setValue(5)
        description.setCounterOffset(counter_offset)
        assert description.getCounterOffset() == counter_offset
        
        crc_offset = PositiveInteger()
        crc_offset.setValue(10)
        description.setCrcOffset(crc_offset)
        assert description.getCrcOffset() == crc_offset
        
        # Test data IDs methods
        data_id = PositiveInteger()
        data_id.setValue(100)
        description.addDataId(data_id)
        assert data_id in description.getDataIds()
        
        data_id_mode = PositiveInteger()
        data_id_mode.setValue(2)
        description.setDataIdMode(data_id_mode)
        assert description.getDataIdMode() == data_id_mode
        
        data_id_nibble = PositiveInteger()
        data_id_nibble.setValue(3)
        description.setDataIdNibbleOffset(data_id_nibble)
        assert description.getDataIdNibbleOffset() == data_id_nibble
        
        data_length = PositiveInteger()
        data_length.setValue(255)
        description.setDataLength(data_length)
        assert description.getDataLength() == data_length
        
        max_delta = PositiveInteger()
        max_delta.setValue(50)
        description.setMaxDeltaCounterInit(max_delta)
        assert description.getMaxDeltaCounterInit() == max_delta
        
        max_no_new = 100  # int value
        description.setMaxNoNewOrRepeatedData(max_no_new)
        assert description.getMaxNoNewOrRepeatedData() == max_no_new
        
        sync_counter = PositiveInteger()
        sync_counter.setValue(25)
        description.setSyncCounterInit(sync_counter)
        assert description.getSyncCounterInit() == sync_counter


class TestEndToEndProtectionVariablePrototype:
    """Test class for EndToEndProtectionVariablePrototype class."""
    
    def test_end_to_end_protection_variable_prototype_initialization(self):
        """Test EndToEndProtectionVariablePrototype initialization and methods."""
        prototype = EndToEndProtectionVariablePrototype()
        assert prototype._receiverIRefs == []
        assert prototype.senderIRef is None
        assert prototype.shortLabel is None
        
        # Test receiver IRef methods
        iref = VariableDataPrototypeInSystemInstanceRef()
        prototype.addReceiverIref(iref)
        assert iref in prototype.getReceiverIrefs()


class TestEndToEndProtectionISignalIPdu:
    """Test class for EndToEndProtectionISignalIPdu class."""
    
    def test_end_to_end_protection_i_signal_i_pdu_initialization(self):
        """Test EndToEndProtectionISignalIPdu initialization and methods."""
        pdu = EndToEndProtectionISignalIPdu()
        assert pdu.dataOffset is None
        assert pdu.iSignalGroupRef is None
        assert pdu.iSignalIPduRef is None
        
        # Test setters and getters
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
        offset = Integer()
        offset.setValue(10)
        pdu.setDataOffset(offset)
        assert pdu.getDataOffset() == offset
        
        group_ref = RefType()
        group_ref.setValue("/Test/ISignalGroup")
        pdu.setISignalGroupRef(group_ref)
        assert pdu.getISignalGroupRef() == group_ref
        
        pdu_ref = RefType()
        pdu_ref.setValue("/Test/ISignalIPdu")
        pdu.setISignalIPduRef(pdu_ref)
        assert pdu.getISignalIPduRef() == pdu_ref


class TestEndToEndProtection:
    """Test class for EndToEndProtection class."""
    
    def test_end_to_end_protection_initialization(self):
        """Test EndToEndProtection initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection = EndToEndProtection(ar_root, "TestProtection")
        
        assert protection.parent == ar_root
        assert protection.short_name == "TestProtection"
        assert protection.endToEndProfile is None
        assert protection.endToEndProtectionISignalIPdus == []
        assert protection.endToEndProtectionVariablePrototypes == []
        
        # Test setters and getters
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndDescription
        profile = EndToEndDescription()
        protection.setEndToEndProfile(profile)
        assert protection.getEndToEndProfile() == profile
        
        # Test EndToEndProtectionISignalIPdu methods
        pdu = EndToEndProtectionISignalIPdu()
        protection.addEndToEndProtectionISignalIPdu(pdu)
        assert pdu in protection.getEndToEndProtectionISignalIPdus()
        
        # Test EndToEndProtectionVariablePrototype methods
        var_prototype = EndToEndProtectionVariablePrototype()
        protection.addEndToEndProtectionVariablePrototype(var_prototype)
        assert var_prototype in protection.getEndToEndProtectionVariablePrototypes()


class TestEndToEndProtectionSet:
    """Test class for EndToEndProtectionSet class."""
    
    def test_end_to_end_protection_set_initialization(self):
        """Test EndToEndProtectionSet initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection_set = EndToEndProtectionSet(ar_root, "TestProtectionSet")
        
        assert protection_set.parent == ar_root
        assert protection_set.short_name == "TestProtectionSet"
        
        # Test create and get methods
        protection = protection_set.createEndToEndProtection("TestProtection")
        assert protection is not None
        assert protection.short_name == "TestProtection"
        assert protection.parent == protection_set
        
        protections = protection_set.getEndToEndProtections()
        assert len(protections) == 1
        assert protections[0] == protection