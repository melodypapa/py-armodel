"""
AUTOSAR Package - AuxillaryObjects

Package: M2::MSR::DataDictionary::AuxillaryObjects
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SwAddrMethod(ARElement):
    """
    Used to assign a common addressing method, e.g. common memory section, to
    data or code objects. These objects could actually live in different modules
    or components.
    
    Package: M2::MSR::DataDictionary::AuxillaryObjects::SwAddrMethod
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 144, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 413, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 209, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Enumeration to specify the name pattern of the Memory Allocation Keyword.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._memory: Optional["MemoryAllocation"] = None

    @property
    def memory(self) -> Optional["MemoryAllocation"]:
        """Get memory (Pythonic accessor)."""
        return self._memory

    @memory.setter
    def memory(self, value: Optional["MemoryAllocation"]) -> None:
        """
        Set memory with validation.
        
        Args:
            value: The memory to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memory = None
            return

        if not isinstance(value, MemoryAllocation):
            raise TypeError(
                f"memory must be MemoryAllocation or None, got {type(value).__name__}"
            )
        self._memory = value
        # This attribute introduces the ability to specify further of the MemorySection
                # in with the shall be placed.
        # are handled as to be selected.
        # The are mentioned in the list.
        # Memory Mapping configuration, this option list is determine an appropriate
                # MemMapAddressing.
        self._option: List["Identifier"] = []

    @property
    def option(self) -> List["Identifier"]:
        """Get option (Pythonic accessor)."""
        return self._option
        # Specifies the expected initialization of the variables (inclusive those which
        # are implementing VariableData Therefore this is an implementation
        # initialization code of BSW modules as well as the start-up code which memory
        # segment to which the AutosarData to the SwAddrMethod’s are later on attribute
        # is not defined it has the identical semantic attribute value "INIT".
        self._section: Optional["SectionInitialization"] = None

    @property
    def section(self) -> Optional["SectionInitialization"]:
        """Get section (Pythonic accessor)."""
        return self._section

    @section.setter
    def section(self, value: Optional["SectionInitialization"]) -> None:
        """
        Set section with validation.
        
        Args:
            value: The section to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._section = None
            return

        if not isinstance(value, SectionInitialization):
            raise TypeError(
                f"section must be SectionInitialization or None, got {type(value).__name__}"
            )
        self._section = value
        # Defines the type of memory sections which can be this addressing method.
        self._sectionType: Optional["MemorySectionType"] = None

    @property
    def section_type(self) -> Optional["MemorySectionType"]:
        """Get sectionType (Pythonic accessor)."""
        return self._sectionType

    @section_type.setter
    def section_type(self, value: Optional["MemorySectionType"]) -> None:
        """
        Set sectionType with validation.
        
        Args:
            value: The sectionType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sectionType = None
            return

        if not isinstance(value, MemorySectionType):
            raise TypeError(
                f"sectionType must be MemorySectionType or None, got {type(value).__name__}"
            )
        self._sectionType = value

    def with_option(self, value):
        """
        Set option and return self for chaining.

        Args:
            value: The option to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_option("value")
        """
        self.option = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMemory(self) -> "MemoryAllocation":
        """
        AUTOSAR-compliant getter for memory.
        
        Returns:
            The memory value
        
        Note:
            Delegates to memory property (CODING_RULE_V2_00017)
        """
        return self.memory  # Delegates to property

    def setMemory(self, value: "MemoryAllocation") -> "SwAddrMethod":
        """
        AUTOSAR-compliant setter for memory with method chaining.
        
        Args:
            value: The memory to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to memory property setter (gets validation automatically)
        """
        self.memory = value  # Delegates to property setter
        return self

    def getOption(self) -> List["Identifier"]:
        """
        AUTOSAR-compliant getter for option.
        
        Returns:
            The option value
        
        Note:
            Delegates to option property (CODING_RULE_V2_00017)
        """
        return self.option  # Delegates to property

    def getSection(self) -> "SectionInitialization":
        """
        AUTOSAR-compliant getter for section.
        
        Returns:
            The section value
        
        Note:
            Delegates to section property (CODING_RULE_V2_00017)
        """
        return self.section  # Delegates to property

    def setSection(self, value: "SectionInitialization") -> "SwAddrMethod":
        """
        AUTOSAR-compliant setter for section with method chaining.
        
        Args:
            value: The section to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to section property setter (gets validation automatically)
        """
        self.section = value  # Delegates to property setter
        return self

    def getSectionType(self) -> "MemorySectionType":
        """
        AUTOSAR-compliant getter for sectionType.
        
        Returns:
            The sectionType value
        
        Note:
            Delegates to section_type property (CODING_RULE_V2_00017)
        """
        return self.section_type  # Delegates to property

    def setSectionType(self, value: "MemorySectionType") -> "SwAddrMethod":
        """
        AUTOSAR-compliant setter for sectionType with method chaining.
        
        Args:
            value: The sectionType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to section_type property setter (gets validation automatically)
        """
        self.section_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_memory(self, value: Optional["MemoryAllocation"]) -> "SwAddrMethod":
        """
        Set memory and return self for chaining.
        
        Args:
            value: The memory to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_memory("value")
        """
        self.memory = value  # Use property setter (gets validation)
        return self

    def with_section(self, value: Optional["SectionInitialization"]) -> "SwAddrMethod":
        """
        Set section and return self for chaining.
        
        Args:
            value: The section to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_section("value")
        """
        self.section = value  # Use property setter (gets validation)
        return self

    def with_section_type(self, value: Optional["MemorySectionType"]) -> "SwAddrMethod":
        """
        Set sectionType and return self for chaining.
        
        Args:
            value: The sectionType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_section_type("value")
        """
        self.section_type = value  # Use property setter (gets validation)
        return self


class MemoryAllocationKeywordPolicyType(AREnum):
    """
    MemoryAllocationKeywordPolicyType enumeration

Enumeration to specify the name pattern of the Memory Allocation Keyword. Aggregated by SwAddrMethod.memoryAllocationKeywordPolicy

Package: M2::MSR::DataDictionary::AuxillaryObjects
    """
    # The MemorySection shortNames of referring MemorySections and therefore the belonging Memory
    addrMethodShort = "None"

    # Allocation Keywords in the code are build with the shortName of the SwAddrMethod. This is the default value if the attribute does not exist.
    Name = "0"

    # The MemorySection shortNames of referring MemorySections and therefore the belonging Memory
    addrMethodShort = "None"

    # Allocation Keywords in the code are build with the shortName of the SwAddrMethod and a variable alignment postfix. Thereby the alignment postfix needs to be consistent with the alignment attribute of the related
    NameAndAlignment = "1"



class MemorySectionType(AREnum):
    """
    MemorySectionType enumeration

Enumeration to specify the essential nature of the data which can be allocated in a common memory class by the means of the AUTOSAR Memory Mapping. Aggregated by SwAddrMethod.sectionType

Package: M2::MSR::DataDictionary::AuxillaryObjects
    """
    # This memory section is reserved for "virtual variables" that are computed by an MCD system during a measurement session but do not exist in the ECU memory.
    calibrationVariables = "2"

    # To be used for calibratable constants of ECU-functions.
    calprm = "3"

    # To be used for mapping code to application block, boot block, external flash etc.
    code = "4"

    # Constants with attributes that show that they reside in one segment for module configuration.
    configData = "5"

    # To be used for global or static constants.
    const = "6"

    # This memory section is reserved for "virtual parameters" that are taken for computing the values of Virtual parameters, on the other hand, are not allocated in the ECU memory. Virtual parameters exist in the ECU Hex file for the purpose of being considered (for computing the values of dependent
    excludeFromFlashtime = "7"

    # To be used for global or static variables. The expected initialization is specified with the attribute
    var = "9"
