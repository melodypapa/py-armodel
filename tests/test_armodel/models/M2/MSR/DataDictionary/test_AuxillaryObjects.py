"""
This module contains tests for the AuxillaryObjects module in MSR.DataDictionary.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, SectionInitializationPolicyType
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import MemoryAllocationKeywordPolicyType, MemorySectionType, SwAddrMethod


class TestMemoryAllocationKeywordPolicyType:
    """
    Test class for MemoryAllocationKeywordPolicyType functionality.
    """

    def test_initialization(self):
        enum = MemoryAllocationKeywordPolicyType()

        assert enum is not None
        assert enum.getEnumValues() == (
            MemoryAllocationKeywordPolicyType.ADDR_METHOD_SHORT_NAME,
            MemoryAllocationKeywordPolicyType.ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT,
        )

    def test_enum_values(self):
        enum = MemoryAllocationKeywordPolicyType()

        assert MemoryAllocationKeywordPolicyType.ADDR_METHOD_SHORT_NAME == "ADDR-METHOD-SHORT-NAME"
        assert MemoryAllocationKeywordPolicyType.ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT == "ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT"

        assert enum.validateEnumValue("ADDR-METHOD-SHORT-NAME") is True
        assert enum.validateEnumValue("ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT") is True
        assert enum.validateEnumValue("invalid") is False


class TestMemorySectionType:
    """
    Test class for MemorySectionType functionality.
    """

    def test_initialization(self):
        enum = MemorySectionType()

        assert enum is not None
        assert enum.getEnumValues() == (
            MemorySectionType.CALIBRATION_VARIABLES,
            MemorySectionType.CALPRM,
            MemorySectionType.CODE,
            MemorySectionType.CONFIG_DATA,
            "CONST",
            MemorySectionType.EXCLUDE_FROM_FLASH,
            MemorySectionType.VAR,
        )

    def test_enum_values(self):
        enum = MemorySectionType()

        assert MemorySectionType.CALIBRATION_VARIABLES == "CALIBRATION-VARIABLES"
        assert MemorySectionType.CALPRM == "CALPRM"
        assert MemorySectionType.CODE == "CODE"
        assert MemorySectionType.CONFIG_DATA == "CONFIG-DATA"
        assert MemorySectionType.CONST == "CONST"
        assert MemorySectionType.EXCLUDE_FROM_FLASH == "EXCLUDE-FROM-FLASH"
        assert MemorySectionType.VAR == "VAR"

        assert enum.validateEnumValue("CODE") is True
        assert enum.validateEnumValue("CONST") is True
        assert enum.validateEnumValue("invalid") is False


class TestSwAddrMethod:
    """
    Test class for SwAddrMethod functionality.
    """

    def test_initialization(self):
        sw_addr_method = SwAddrMethod(None, "test_name")
        assert sw_addr_method.memoryAllocationKeywordPolicy is None
        assert sw_addr_method.options == []
        assert sw_addr_method.sectionInitializationPolicy is None
        assert sw_addr_method.sectionType is None

    def test_get_set_memory_allocation_keyword_policy(self):
        sw_addr_method = SwAddrMethod(None, "test_name")
        policy = MemoryAllocationKeywordPolicyType().setValue(MemoryAllocationKeywordPolicyType.ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT)

        result = sw_addr_method.setMemoryAllocationKeywordPolicy(policy)
        assert sw_addr_method.getMemoryAllocationKeywordPolicy() == policy
        assert result == sw_addr_method

        result = sw_addr_method.setMemoryAllocationKeywordPolicy(None)
        assert sw_addr_method.getMemoryAllocationKeywordPolicy() == policy
        assert result == sw_addr_method

    def test_get_add_options(self):
        sw_addr_method = SwAddrMethod(None, "test_name")
        option = Identifier().setValue("resetSafe")

        result = sw_addr_method.addOption(option)
        assert option in sw_addr_method.getOptions()
        assert result == sw_addr_method

    def test_get_set_section_initialization_policy(self):
        sw_addr_method = SwAddrMethod(None, "test_name")
        policy = SectionInitializationPolicyType().setValue(SectionInitializationPolicyType.INIT)

        result = sw_addr_method.setSectionInitializationPolicy(policy)
        assert sw_addr_method.getSectionInitializationPolicy() == policy
        assert result == sw_addr_method

        result = sw_addr_method.setSectionInitializationPolicy(None)
        assert sw_addr_method.getSectionInitializationPolicy() == policy
        assert result == sw_addr_method

    def test_get_set_section_type(self):
        sw_addr_method = SwAddrMethod(None, "test_name")
        section_type = MemorySectionType().setValue(MemorySectionType.VAR)

        result = sw_addr_method.setSectionType(section_type)
        assert sw_addr_method.getSectionType() == section_type
        assert result == sw_addr_method

        result = sw_addr_method.setSectionType(None)
        assert sw_addr_method.getSectionType() == section_type
        assert result == sw_addr_method
