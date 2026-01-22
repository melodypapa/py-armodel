"""
This module contains comprehensive tests for the PerInstanceMemory module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the PerInstanceMemory.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import (
    PerInstanceMemory
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestPerInstanceMemory:
    """Test class for PerInstanceMemory class."""
    
    def test_per_instance_memory_initialization(self):
        """Test PerInstanceMemory initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        memory = PerInstanceMemory(ar_root, "TestPerInstanceMemory")
        
        assert memory.parent == ar_root
        assert memory.short_name == "TestPerInstanceMemory"
        assert memory.initValue is None
        assert memory.swDataDefProps is None
        assert memory.type is None
        assert memory.typeDefinition is None
        
        # Test initValue methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        init_val = ARLiteral()
        init_val.setValue("test_init")
        memory.setInitValue(init_val)
        assert memory.getInitValue() == init_val
        
        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        sw_data_def = SwDataDefProps()
        memory.setSwDataDefProps(sw_data_def)
        assert memory.getSwDataDefProps() == sw_data_def
        
        # Test type methods
        type_val = ARLiteral()
        type_val.setValue("test_type")
        memory.setType(type_val)
        assert memory.getType() == type_val
        
        # Test typeDefinition methods
        type_def = ARLiteral()
        type_def.setValue("test_type_def")
        memory.setTypeDefinition(type_def)
        assert memory.getTypeDefinition() == type_def