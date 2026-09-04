"""
This module contains comprehensive tests for the PerInstanceMemory module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the PerInstanceMemory.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import PerInstanceMemory
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestPerInstanceMemory:
    """Test class for PerInstanceMemory class."""

    def test_per_instance_memory_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        memory = PerInstanceMemory(ar_root, "TestPerInstanceMemory")

        assert memory.parent == ar_root
        assert memory.short_name == "TestPerInstanceMemory"
        assert memory.initValue is None
        assert memory.swDataDefProps is None
        assert memory.type is None
        assert memory.typeDefinition is None
        assert memory.__class__.__doc__.strip() == (
            "Defines a 'C' typed memory-block that needs to be available for each instance of the SW-component. "
            'This is typically only useful if supportsMultipleInstantiation is set to "true" or if the '
            "software-component defines NVRAM access via permanent blocks."
        )

        init_val = String()
        init_val.setValue("test_init")
        assert memory.setInitValue(init_val) is memory
        assert memory.getInitValue() == init_val
        assert memory.setInitValue(None) is memory
        assert memory.getInitValue() == init_val

        sw_data_def = SwDataDefProps()
        assert memory.setSwDataDefProps(sw_data_def) is memory
        assert memory.getSwDataDefProps() == sw_data_def
        assert memory.setSwDataDefProps(None) is memory
        assert memory.getSwDataDefProps() == sw_data_def

        type_val = CIdentifier()
        type_val.setValue("test_type")
        assert memory.setType(type_val) is memory
        assert memory.getType() == type_val
        assert memory.setType(None) is memory
        assert memory.getType() == type_val

        type_def = String()
        type_def.setValue("test_type_def")
        assert memory.setTypeDefinition(type_def) is memory
        assert memory.getTypeDefinition() == type_def
        assert memory.setTypeDefinition(None) is memory
        assert memory.getTypeDefinition() == type_def
