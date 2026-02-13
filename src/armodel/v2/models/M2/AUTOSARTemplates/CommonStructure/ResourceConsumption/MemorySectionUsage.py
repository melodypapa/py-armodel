"""
AUTOSAR Package - MemorySectionUsage

Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ImplementationProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class MemorySection(Identifiable):
    """
    Provides a description of an abstract memory section used in the
    Implementation for code or data. It shall be declared by the Implementation
    Description of the module or component, which actually allocates the memory
    in its code. This means in case of data prototypes which are allocated by
    the RTE, that the generated Implementation Description of the RTE shall
    contain the corresponding MemorySections. The attribute "symbol" (if symbol
    is missing: "shortName") defines the module or component specific section
    name used in the code. For details see the document "Specification of Memory
    Mapping". Typically the section name is build according the pattern:
    <SwAddrMethod shortName>[_<further specialization nominator>][_<alignment>]
    where • [<SwAddrMethod shortName>] is the shortName of the referenced
    SwAddrMethod • [_<further specialization nominator>] is an optional infix to
    indicate the specialization in the case that several MemorySections for
    different purpose of the same Implementation Description referring to the
    same or equally named SwAddrMethods. • [_<alignment>] is the alignment
    attributes value and is only applicable in the case that the memory
    AllocationKeywordPolicy value of the referenced SwAddrMethod is set to
    addrMethodShortNameAnd Alignment MemorySection used to Implement the code of
    RunnableEntitys and BswSchedulableEntitys shall have a symbol (if missing:
    shortName) identical to the referred SwAddrMethod to conform to the
    generated RTE header files. In addition to the section name described above,
    a prefix is used in the corresponding macro code in order to define a name
    space. This prefix is by default given by the shortName of the BswModule
    Description resp. the SwComponentType. It can be superseded by the prefix
    attribute.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage::MemorySection

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 143, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 411, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2036, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The attribute describes the typical alignment of objects memory section.
        self._alignment: Optional[AlignmentType] = None

    @property
    def alignment(self) -> Optional[AlignmentType]:
        """Get alignment (Pythonic accessor)."""
        return self._alignment

    @alignment.setter
    def alignment(self, value: Optional[AlignmentType]) -> None:
        """
        Set alignment with validation.

        Args:
            value: The alignment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alignment = None
            return

        if not isinstance(value, AlignmentType):
            raise TypeError(
                f"alignment must be AlignmentType or None, got {type(value).__name__}"
            )
        self._alignment = value
                # different Executable different sections even if the associated Sw the same.
        # applicable to code sections only.
        self._executableEntity: List["ExecutableEntity"] = []

    @property
    def executable_entity(self) -> List["ExecutableEntity"]:
        """Get executableEntity (Pythonic accessor)."""
        return self._executableEntity
        # The service (in AUTOSAR: BswModuleEntry) is a way that it either resolves to
                # aninline to a standard function depending on at a later point in time.
        # two values are standardized (to be used for only and exclusively to each
                # other): - The code section is declared with the keyword - The code section is
                # declared with the inline".
        # cases (INLINE and LOCAL_INLINE) the inline on the compiler.
        # Depending on this, section either corresponds to an actual section or is put
                # into the section of the caller.
        self._option: List["Identifier"] = []

    @property
    def option(self) -> List["Identifier"]:
        """Get option (Pythonic accessor)."""
        return self._option
        # The prefix used to set the memory section’s namespace code.
        # The existence of a prefix element for a default prefix (such as the Bsw This
                # allows the user to name spaces for memory sections within of one module,
                # cluster or SWC.
        self._prefix: Optional[SectionNamePrefix] = None

    @property
    def prefix(self) -> Optional[SectionNamePrefix]:
        """Get prefix (Pythonic accessor)."""
        return self._prefix

    @prefix.setter
    def prefix(self, value: Optional[SectionNamePrefix]) -> None:
        """
        Set prefix with validation.

        Args:
            value: The prefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._prefix = None
            return

        if not isinstance(value, SectionNamePrefix):
            raise TypeError(
                f"prefix must be SectionNamePrefix or None, got {type(value).__name__}"
            )
        self._prefix = value
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._size: Optional[PositiveInteger] = None

    @property
    def size(self) -> Optional[PositiveInteger]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set size with validation.

        Args:
            value: The size to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"size must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._size = value
                # overall SwAddr by the upstream declarations (e.
        # g.
        # data element prototypes, code share a common addressing strategy.
        # This evaluated for the ECU configuration of the build shall always be
                # declared by the of the module or component, the memory in its code.
        # This means in data prototypes which are allocated by the RTE, software
                # components only declare the grouping data prototypes to SwAddrMethods, and
                # the Description of the RTE actually this association.
        self._swAddrmethod: Optional["SwAddrMethod"] = None

    @property
    def sw_addrmethod(self) -> Optional["SwAddrMethod"]:
        """Get swAddrmethod (Pythonic accessor)."""
        return self._swAddrmethod

    @sw_addrmethod.setter
    def sw_addrmethod(self, value: Optional["SwAddrMethod"]) -> None:
        """
        Set swAddrmethod with validation.

        Args:
            value: The swAddrmethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAddrmethod = None
            return

        if not isinstance(value, SwAddrMethod):
            raise TypeError(
                f"swAddrmethod must be SwAddrMethod or None, got {type(value).__name__}"
            )
        self._swAddrmethod = value
                # code generation the shortName) it is possible to define several having the
                # same name - e.
        # g.
        # CODE - but using different sectionName.
        self._symbol: Optional["Identifier"] = None

    @property
    def symbol(self) -> Optional["Identifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["Identifier"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"symbol must be Identifier or str or None, got {type(value).__name__}"
            )
        self._symbol = value

    def with_executable_entity(self, value):
        """
        Set executable_entity and return self for chaining.

        Args:
            value: The executable_entity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_executable_entity("value")
        """
        self.executable_entity = value  # Use property setter (gets validation)
        return self

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

    def getAlignment(self) -> AlignmentType:
        """
        AUTOSAR-compliant getter for alignment.

        Returns:
            The alignment value

        Note:
            Delegates to alignment property (CODING_RULE_V2_00017)
        """
        return self.alignment  # Delegates to property

    def setAlignment(self, value: AlignmentType) -> MemorySection:
        """
        AUTOSAR-compliant setter for alignment with method chaining.

        Args:
            value: The alignment to set

        Returns:
            self for method chaining

        Note:
            Delegates to alignment property setter (gets validation automatically)
        """
        self.alignment = value  # Delegates to property setter
        return self

    def getExecutableEntity(self) -> List["ExecutableEntity"]:
        """
        AUTOSAR-compliant getter for executableEntity.

        Returns:
            The executableEntity value

        Note:
            Delegates to executable_entity property (CODING_RULE_V2_00017)
        """
        return self.executable_entity  # Delegates to property

    def getOption(self) -> List["Identifier"]:
        """
        AUTOSAR-compliant getter for option.

        Returns:
            The option value

        Note:
            Delegates to option property (CODING_RULE_V2_00017)
        """
        return self.option  # Delegates to property

    def getPrefix(self) -> SectionNamePrefix:
        """
        AUTOSAR-compliant getter for prefix.

        Returns:
            The prefix value

        Note:
            Delegates to prefix property (CODING_RULE_V2_00017)
        """
        return self.prefix  # Delegates to property

    def setPrefix(self, value: SectionNamePrefix) -> MemorySection:
        """
        AUTOSAR-compliant setter for prefix with method chaining.

        Args:
            value: The prefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to prefix property setter (gets validation automatically)
        """
        self.prefix = value  # Delegates to property setter
        return self

    def getSize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: PositiveInteger) -> MemorySection:
        """
        AUTOSAR-compliant setter for size with method chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    def getSwAddrmethod(self) -> "SwAddrMethod":
        """
        AUTOSAR-compliant getter for swAddrmethod.

        Returns:
            The swAddrmethod value

        Note:
            Delegates to sw_addrmethod property (CODING_RULE_V2_00017)
        """
        return self.sw_addrmethod  # Delegates to property

    def setSwAddrmethod(self, value: "SwAddrMethod") -> MemorySection:
        """
        AUTOSAR-compliant setter for swAddrmethod with method chaining.

        Args:
            value: The swAddrmethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_addrmethod property setter (gets validation automatically)
        """
        self.sw_addrmethod = value  # Delegates to property setter
        return self

    def getSymbol(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "Identifier") -> MemorySection:
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alignment(self, value: Optional[AlignmentType]) -> MemorySection:
        """
        Set alignment and return self for chaining.

        Args:
            value: The alignment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alignment("value")
        """
        self.alignment = value  # Use property setter (gets validation)
        return self

    def with_prefix(self, value: Optional[SectionNamePrefix]) -> MemorySection:
        """
        Set prefix and return self for chaining.

        Args:
            value: The prefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prefix("value")
        """
        self.prefix = value  # Use property setter (gets validation)
        return self

    def with_size(self, value: Optional[PositiveInteger]) -> MemorySection:
        """
        Set size and return self for chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self

    def with_sw_addrmethod(self, value: Optional["SwAddrMethod"]) -> MemorySection:
        """
        Set swAddrmethod and return self for chaining.

        Args:
            value: The swAddrmethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_addrmethod("value")
        """
        self.sw_addrmethod = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["Identifier"]) -> MemorySection:
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self



class SectionNamePrefix(ImplementationProps):
    """
    A prefix to be used for generated code artifacts defining a memory section
    name in the source code of the using module or SWC.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage::SectionNamePrefix

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 147, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 412, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional reference that allows to Indicate the code artifact containing the
                # preprocessor implementation sections with this prefix.
        # of this link supersedes the usage of a memory with the default name (derived
                # from the.
        self._implementedIn: Optional[RefType] = None

    @property
    def implemented_in(self) -> Optional[RefType]:
        """Get implementedIn (Pythonic accessor)."""
        return self._implementedIn

    @implemented_in.setter
    def implemented_in(self, value: Optional[RefType]) -> None:
        """
        Set implementedIn with validation.

        Args:
            value: The implementedIn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementedIn = None
            return

        self._implementedIn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementedIn(self) -> RefType:
        """
        AUTOSAR-compliant getter for implementedIn.

        Returns:
            The implementedIn value

        Note:
            Delegates to implemented_in property (CODING_RULE_V2_00017)
        """
        return self.implemented_in  # Delegates to property

    def setImplementedIn(self, value: RefType) -> SectionNamePrefix:
        """
        AUTOSAR-compliant setter for implementedIn with method chaining.

        Args:
            value: The implementedIn to set

        Returns:
            self for method chaining

        Note:
            Delegates to implemented_in property setter (gets validation automatically)
        """
        self.implemented_in = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implemented_in(self, value: Optional[RefType]) -> SectionNamePrefix:
        """
        Set implementedIn and return self for chaining.

        Args:
            value: The implementedIn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implemented_in("value")
        """
        self.implemented_in = value  # Use property setter (gets validation)
        return self
