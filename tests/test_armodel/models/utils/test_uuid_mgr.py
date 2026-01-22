"""
Test suite for uuid_mgr module

This module tests the UUIDMgr class and its functionality including:
- addObject method
- getObjects method
- getDuplicateUUIDs method
"""

from armodel.models.utils.uuid_mgr import UUIDMgr
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockARObject(ARObject):
    """Mock ARObject for testing purposes."""
    def __init__(self, uuid=None):
        super().__init__()
        self.uuid = uuid


class TestUUIDMgr:
    """Test cases for the UUIDMgr class."""
    
    def test_uuid_mgr_initialization(self):
        """Test that UUIDMgr initializes with an empty dictionary."""
        uuid_mgr = UUIDMgr()
        assert uuid_mgr.uuid_object_mappings == {}
    
    def test_add_object_with_none_uuid(self):
        """Test that addObject handles objects with None uuid correctly."""
        uuid_mgr = UUIDMgr()
        obj = MockARObject(uuid=None)
        uuid_mgr.addObject(obj)
        # Should not add the object since uuid is None
        assert uuid_mgr.uuid_object_mappings == {}
    
    def test_add_object_with_valid_uuid(self):
        """Test that addObject adds objects with valid uuid correctly."""
        uuid_mgr = UUIDMgr()
        uuid_val = "test-uuid-123"
        obj = MockARObject(uuid=uuid_val)
        
        uuid_mgr.addObject(obj)
        
        assert uuid_val in uuid_mgr.uuid_object_mappings
        assert obj in uuid_mgr.uuid_object_mappings[uuid_val]
        assert len(uuid_mgr.uuid_object_mappings[uuid_val]) == 1
    
    def test_add_multiple_objects_same_uuid(self):
        """Test that multiple objects with same uuid are added to the same list."""
        uuid_mgr = UUIDMgr()
        uuid_val = "test-uuid-123"
        obj1 = MockARObject(uuid=uuid_val)
        obj2 = MockARObject(uuid=uuid_val)
        
        uuid_mgr.addObject(obj1)
        uuid_mgr.addObject(obj2)
        
        assert uuid_val in uuid_mgr.uuid_object_mappings
        assert len(uuid_mgr.uuid_object_mappings[uuid_val]) == 2
        assert obj1 in uuid_mgr.uuid_object_mappings[uuid_val]
        assert obj2 in uuid_mgr.uuid_object_mappings[uuid_val]
    
    def test_add_objects_different_uuids(self):
        """Test that objects with different uuids are stored separately."""
        uuid_mgr = UUIDMgr()
        uuid1 = "test-uuid-1"
        uuid2 = "test-uuid-2"
        obj1 = MockARObject(uuid=uuid1)
        obj2 = MockARObject(uuid=uuid2)
        
        uuid_mgr.addObject(obj1)
        uuid_mgr.addObject(obj2)
        
        assert uuid1 in uuid_mgr.uuid_object_mappings
        assert uuid2 in uuid_mgr.uuid_object_mappings
        assert len(uuid_mgr.uuid_object_mappings[uuid1]) == 1
        assert len(uuid_mgr.uuid_object_mappings[uuid2]) == 1
        assert obj1 in uuid_mgr.uuid_object_mappings[uuid1]
        assert obj2 in uuid_mgr.uuid_object_mappings[uuid2]
    
    def test_get_objects_with_existing_uuid(self):
        """Test that getObjects returns objects for existing uuid."""
        uuid_mgr = UUIDMgr()
        uuid_val = "test-uuid-123"
        obj = MockARObject(uuid=uuid_val)
        
        uuid_mgr.addObject(obj)
        result = uuid_mgr.getObjects(uuid_val)
        
        assert result == [obj]
    
    def test_get_objects_with_nonexistent_uuid(self):
        """Test that getObjects returns empty list for nonexistent uuid."""
        uuid_mgr = UUIDMgr()
        result = uuid_mgr.getObjects("nonexistent-uuid")
        
        assert result == []
    
    def test_get_duplicate_uuids_empty(self):
        """Test that getDuplicateUUIDs returns empty list when no objects."""
        uuid_mgr = UUIDMgr()
        result = uuid_mgr.getDuplicateUUIDs()
        # This method returns all UUIDs in the mappings, not just duplicates
        assert result == []
    
    def test_get_duplicate_uuids_with_objects(self):
        """Test that getDuplicateUUIDs returns all UUIDs when objects are added."""
        uuid_mgr = UUIDMgr()
        uuid1 = "test-uuid-1"
        uuid2 = "test-uuid-2"
        obj1 = MockARObject(uuid=uuid1)
        obj2 = MockARObject(uuid=uuid2)
        
        uuid_mgr.addObject(obj1)
        uuid_mgr.addObject(obj2)
        
        result = uuid_mgr.getDuplicateUUIDs()
        
        # The method returns all UUIDs, not just duplicates
        assert uuid1 in result
        assert uuid2 in result
        assert len(result) == 2