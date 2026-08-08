"""
This module contains the MemorySection and SectionNamePrefix classes for representing
memory section usage in AUTOSAR resource consumption models.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AlignmentType, CIdentifier, Identifier, PositiveInteger, RefType


class MemorySection(Identifiable):
    """
    Provides a description of an abstract memory section used in the Implementation for
    code or data. It shall be declared by the Implementation Description of the module or
    component, which actually allocates the memory in its code.
    """

    # MemorySection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.2, p.143
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAlignment                 [x] impl  [x] docstring  [x] test
    # [x] setAlignment                 [x] impl  [x] docstring  [x] test
    # [x] addExecutableEntityRef       [x] impl  [x] docstring  [x] test
    # [x] getExecutableEntityRefs      [x] impl  [x] docstring  [x] test
    # [x] getMemClassSymbol            [x] impl  [x] docstring  [x] test
    # [x] setMemClassSymbol            [x] impl  [x] docstring  [x] test
    # [x] addOption                    [x] impl  [x] docstring  [x] test
    # [x] getOptions                   [x] impl  [x] docstring  [x] test
    # [x] getPrefixRef                 [x] impl  [x] docstring  [x] test
    # [x] setPrefixRef                 [x] impl  [x] docstring  [x] test
    # [x] getSize                      [x] impl  [x] docstring  [x] test
    # [x] setSize                      [x] impl  [x] docstring  [x] test
    # [x] getSwAddrMethodRef           [x] impl  [x] docstring  [x] test
    # [x] setSwAddrMethodRef           [x] impl  [x] docstring  [x] test
    # [x] getSymbol                    [x] impl  [x] docstring  [x] test
    # [x] setSymbol                    [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the MemorySection with a parent and short name.

        Args:
            parent: The parent ARObject that contains this memory section
            short_name: The unique short name of this memory section
        """
        super().__init__(parent, short_name)

        # The attribute describes the typical alignment of objects within this memory section.
        self.alignment: Optional[AlignmentType] = None

        # Reference to the ExecutableEntities located in this section. This allows to locate
        # different ExecutableEntities in different sections even if the associated
        # SwAddrMethod is the same. This is applicable to code sections only.
        self.executableEntityRefs: List[RefType] = []

        # Defines a specific symbol in order to generate the compiler abstraction "memclass"
        # code for this MemorySection. The existence of this attribute supersedes the usage
        # of swAddrmethod.shortName for this purpose.
        self.memClassSymbol: Optional[CIdentifier] = None

        # The service (in AUTOSAR: BswModuleEntry) is implemented in a way that it either
        # resolves to an inline function or to a standard function depending on conditions
        # set at a later point in time. Standardized values (to be used for code sections
        # only and exclusively to each other): INLINE - the code section is declared with
        # the keyword "inline"; LOCAL_INLINE - the code section is declared with the keyword
        # "static inline".
        self.options: List[Identifier] = []

        # The prefix used to set the memory section's namespace in the code. The existence
        # of a prefix element supersedes rules for a default prefix (such as the
        # BswModuleDescription's shortName).
        self.prefixRef: Optional[RefType] = None

        # The size in bytes of the section.
        self.size: Optional[PositiveInteger] = None

        # This association indicates that this module specific (abstract) memory section is
        # part of an overall SwAddrMethod, referred by the upstream declarations (e.g.
        # calibration parameters, data element prototypes, code entities) which share a
        # common addressing strategy.
        self.swAddrMethodRef: Optional[RefType] = None

        # Defines the section name as explained in the main description. By using this
        # attribute for code generation (instead of the shortName) it is possible to define
        # several different MemorySections having the same name - e.g. symbol = CODE - but
        # using different sectionNamePrefixes.
        self.symbol: Optional[Identifier] = None

    def getAlignment(self) -> Optional[AlignmentType]:
        """
        Gets the typical alignment of objects within this memory section.

        Returns:
            AlignmentType: Alignment value, or None if not set
        """
        return self.alignment

    def setAlignment(self, value: Optional[AlignmentType]) -> "MemorySection":
        """
        Sets the typical alignment of objects within this memory section.
        A None value is a no-op and does not overwrite an existing alignment.

        Args:
            value: The alignment value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.alignment = value
        return self

    def addExecutableEntityRef(self, value: Optional[RefType]) -> "MemorySection":
        """
        Adds a reference to an ExecutableEntity located in this section.
        This is applicable to code sections only.

        Args:
            value: The executable entity reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.executableEntityRefs.append(value)
        return self

    def getExecutableEntityRefs(self) -> List[RefType]:
        """
        Gets the references to the ExecutableEntities located in this section. This allows
        to locate different ExecutableEntities in different sections even if the associated
        SwAddrMethod is the same. This is applicable to code sections only.

        Returns:
            List of RefType references to executable entities
        """
        return self.executableEntityRefs

    def getMemClassSymbol(self) -> Optional[CIdentifier]:
        """
        Gets the specific symbol used to generate the compiler abstraction "memclass" code
        for this MemorySection. The existence of this symbol supersedes the usage of
        swAddrmethod.shortName for this purpose.

        Returns:
            CIdentifier: Memory class symbol, or None if not set
        """
        return self.memClassSymbol

    def setMemClassSymbol(self, value: Optional[CIdentifier]) -> "MemorySection":
        """
        Sets the specific symbol used to generate the compiler abstraction "memclass" code
        for this MemorySection. The existence of this symbol supersedes the usage of
        swAddrmethod.shortName for this purpose.
        A None value is a no-op and does not overwrite an existing symbol.

        Args:
            value: The memory class symbol to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.memClassSymbol = value
        return self

    def addOption(self, option: Optional[Identifier]) -> "MemorySection":
        """
        Adds an option to the list of options for this memory section. Standardized values
        are INLINE - the code section is declared with the keyword "inline" - and
        LOCAL_INLINE - the code section is declared with the keyword "static inline".
        Both are to be used for code sections only and exclusively to each other.

        Args:
            option: The option to add

        Returns:
            self for method chaining
        """
        if option is not None:
            self.options.append(option)
        return self

    def getOptions(self) -> List[Identifier]:
        """
        Gets the list of options for this memory section. Standardized values are INLINE -
        the code section is declared with the keyword "inline" - and LOCAL_INLINE - the
        code section is declared with the keyword "static inline".

        Returns:
            List of Identifier options
        """
        return self.options

    def getPrefixRef(self) -> Optional[RefType]:
        """
        Gets the reference to the SectionNamePrefix used to set the memory section's
        namespace in the code. The existence of a prefix element supersedes rules for a
        default prefix (such as the BswModuleDescription's shortName).

        Returns:
            RefType referencing the SectionNamePrefix, or None if not set
        """
        return self.prefixRef

    def setPrefixRef(self, value: Optional[RefType]) -> "MemorySection":
        """
        Sets the reference to the SectionNamePrefix used to set the memory section's
        namespace in the code. The existence of a prefix element supersedes rules for a
        default prefix (such as the BswModuleDescription's shortName).
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The SectionNamePrefix reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.prefixRef = value
        return self

    def getSize(self) -> Optional[PositiveInteger]:
        """
        Gets the size in bytes of the section.

        Returns:
            PositiveInteger size value of the memory section, or None if not set
        """
        return self.size

    def setSize(self, value: Optional[PositiveInteger]) -> "MemorySection":
        """
        Sets the size in bytes of the section.
        A None value is a no-op and does not overwrite an existing size.

        Args:
            value: The size value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.size = value
        return self

    def getSwAddrMethodRef(self) -> Optional[RefType]:
        """
        Gets the reference to the SwAddrMethod this module specific (abstract) memory
        section is part of. Upstream declarations (e.g. calibration parameters, data
        element prototypes, code entities) refer to this SwAddrMethod to share a common
        addressing strategy.

        Returns:
            RefType referencing the SwAddrMethod, or None if not set
        """
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value: Optional[RefType]) -> "MemorySection":
        """
        Sets the reference to the SwAddrMethod this module specific (abstract) memory
        section is part of. Upstream declarations (e.g. calibration parameters, data
        element prototypes, code entities) refer to this SwAddrMethod to share a common
        addressing strategy.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The reference to the software address method to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swAddrMethodRef = value
        return self

    def getSymbol(self) -> Optional[Identifier]:
        """
        Gets the section name used for code generation. By using this attribute instead of
        the shortName it is possible to define several different MemorySections having the
        same name - e.g. symbol = CODE - but using different sectionNamePrefixes.

        Returns:
            Identifier: Section name symbol, or None if not set
        """
        return self.symbol

    def setSymbol(self, value: Optional[Identifier]) -> "MemorySection":
        """
        Sets the section name used for code generation. By using this attribute instead of
        the shortName it is possible to define several different MemorySections having the
        same name - e.g. symbol = CODE - but using different sectionNamePrefixes.
        A None value is a no-op and does not overwrite an existing symbol.

        Args:
            value: The section name symbol to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbol = value
        return self


class SectionNamePrefix(ImplementationProps):
    """
    A prefix to be used for generated code artifacts defining a memory section name in
    the source code of the using module or SWC.

    [constr_4103] In case a BSW module is split into allocatable memory parts the
    SectionNamePrefix.symbol shall be set in the <MIP>_<FEATURE> form, where <MIP> is
    the capitalized module implementation prefix and <FEATURE> is the name of the
    sub-feature in the BSW module denoting the allocatable memory part.
    """

    # SectionNamePrefix method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.8, p.147
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getImplementedInRef          [x] impl  [x] docstring  [x] test
    # [x] setImplementedInRef          [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SectionNamePrefix with a parent and short name.

        Args:
            parent: The parent ARObject that contains this section name prefix
            short_name: The unique short name of this section name prefix
        """
        super().__init__(parent, short_name)

        # Optional reference that allows to indicate the code artifact (header file)
        # containing the preprocessor implementation of memory sections with this prefix.
        # The usage of this link supersedes the usage of a memory mapping header with the
        # default name (derived from the BswModuleDescription's shortName).
        # [constr_4072] The SectionNamePrefix and the DependencyOnArtifact connected via
        # this link shall belong to the same BswImplementation; the DependencyOnArtifact
        # shall be aggregated by BswImplementation in the role requiredArtifact and shall
        # have the category value set to MEMMAP.
        self.implementedInRef: Optional[RefType] = None

    def getImplementedInRef(self) -> Optional[RefType]:
        """
        Gets the reference to the code artifact (header file) containing the preprocessor
        implementation of memory sections with this prefix. The usage of this link
        supersedes the usage of a memory mapping header with the default name (derived
        from the BswModuleDescription's shortName). [constr_4072]

        Returns:
            RefType referencing the implemented-in artifact, or None if not set
        """
        return self.implementedInRef

    def setImplementedInRef(self, value: Optional[RefType]) -> "SectionNamePrefix":
        """
        Sets the reference to the code artifact (header file) containing the preprocessor
        implementation of memory sections with this prefix. The usage of this link
        supersedes the usage of a memory mapping header with the default name (derived
        from the BswModuleDescription's shortName). [constr_4072]
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The implemented-in artifact reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.implementedInRef = value
        return self
