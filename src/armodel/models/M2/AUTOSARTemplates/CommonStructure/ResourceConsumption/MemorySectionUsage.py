"""
This module contains the MemorySection and SectionNamePrefix classes for representing
memory section usage in AUTOSAR resource consumption models.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AlignmentType, CIdentifier, Identifier, PositiveInteger, RefType
from typing import List, Optional


class MemorySection(Identifiable, VariationPointCapable):
    """
    Provides a description of an abstract memory section used in the Implementation for code or data. It shall be declared by the Implementation Description of the module or component, which actually allocates the memory in its code. This means in case of data prototypes which are allocated by the RTE, that the generated Implementation Description of the RTE shall contain the corresponding MemorySections. The attribute "symbol" (if symbol is missing: "shortName") defines the module or component specific section name used in the code. For details see the document "Specification of Memory Mapping". Typically the section name is build according the pattern: <SwAddrMethod shortName>[_<further specialization nominator>][_<alignment>] where • [<SwAddrMethod shortName>] is the shortName of the referenced SwAddrMethod • [_<further specialization nominator>] is an optional infix to indicate the specialization in the case that several MemorySections for different purpose of the same Implementation Description referring to the same or equally named SwAddrMethods. • [_<alignment>] is the alignment attributes value and is only applicable in the case that the memory AllocationKeywordPolicy value of the referenced SwAddrMethod is set to addrMethodShortNameAnd Alignment
    """

    # MemorySection method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.2, p.144 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.2, p.145 (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAlignment                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlignment                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addExecutableEntityRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExecutableEntityRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMemClassSymbol            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setMemClassSymbol            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] addOption                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOptions                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPrefixRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrefixRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSize                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSize                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwAddrMethodRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwAddrMethodRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSymbol                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSymbol                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The attribute describes the typical alignment of objects within this memory section.
        self.alignment: Optional[AlignmentType] = None

        # Reference to the ExecutableEntitites located in this section. This allows to locate different Executable Entitities in different sections even if the associated Sw Addrmethod is the same. This is applicable to code sections only.
        self.executableEntityRefs: List[RefType] = []

        # Defines a specific symbol in order to generate the compiler abstraction "memclass" code for this MemorySection. The existence of this attribute supersedes the usage of swAddrmethod.shortName for this purpose. The complete name of the "memclass" preprocessor symbol is constructed as <prefix>_<memClassSymbol> where prefix is defined in the same way as for the enclosing MemorySection. See also AUTOSAR_SWS_CompilerAbstraction SWS_COMPILER_00040.
        self.memClassSymbol: Optional[CIdentifier] = None

        # The service (in AUTOSAR: BswModuleEntry) is implemented in a way that it either resolves to aninline function or to a standard function depending on conditions set at a later point in time. The following two values are standardized (to be used for code sections only and exclusively to each other): • INLINE - The code section is declared with the keyword "inline". • LOCAL_INLINE - The code section is declared with the keyword "static inline". In both cases (INLINE and LOCAL_INLINE) the inline expansion depends on the compiler. Depending on this, the code section either corresponds to an actual section in memory or is put into the section of the caller.
        self.options: List[Identifier] = []

        # The prefix used to set the memory section's namespace in the code. The existence of a prefix element supersedes rules for a default prefix (such as the Bsw ModuleDescription's shortName). This allows the user to define several name spaces for memory sections within the scope of one module, cluster or SWC.
        self.prefixRef: Optional[RefType] = None

        # The size in bytes of the section.
        self.size: Optional[PositiveInteger] = None

        # This association indicates that this module specific (abstract) memory section is part of an overall SwAddr Method, referred by the upstream declarations (e.g. calibration parameters, data element prototypes, code entities) which share a common addressing strategy. This can be evaluated for the ECU configuration of the build support. This association shall always be declared by the Implementation description of the module or component, which allocates the memory in its code. This means in case of data prototypes which are allocated by the RTE, that the software components only declare the grouping of its data prototypes to SwAddrMethods, and the generated Implementation Description of the RTE actually sets up this association.
        self.swAddrMethodRef: Optional[RefType] = None

        # Defines the section name as explained in the main description. By using this attribute for code generation (instead of the shortName) it is possible to define several different MemorySections having the same name - e.g. symbol = CODE - but using different sectionName Prefixes.
        self.symbol: Optional[Identifier] = None

    def getAlignment(self) -> Optional[AlignmentType]:
        """
        The attribute describes the typical alignment of objects within this memory section.
        """
        return self.alignment

    def setAlignment(self, value: Optional[AlignmentType]) -> "MemorySection":
        """
        The attribute describes the typical alignment of objects within this memory section.
        A None value is a no-op and does not overwrite an existing alignment.
        """
        if value is not None:
            self.alignment = value
        return self

    def addExecutableEntityRef(self, value: Optional[RefType]) -> "MemorySection":
        """
        Reference to the ExecutableEntitites located in this section. This allows to locate different Executable Entitities in different sections even if the associated Sw Addrmethod is the same. This is applicable to code sections only.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.executableEntityRefs.append(value)
        return self

    def getExecutableEntityRefs(self) -> List[RefType]:
        """
        Reference to the ExecutableEntitites located in this section. This allows to locate different Executable Entitities in different sections even if the associated Sw Addrmethod is the same. This is applicable to code sections only.
        """
        return self.executableEntityRefs

    def getMemClassSymbol(self) -> Optional[CIdentifier]:
        """
        Defines a specific symbol in order to generate the compiler abstraction "memclass" code for this MemorySection. The existence of this attribute supersedes the usage of swAddrmethod.shortName for this purpose. The complete name of the "memclass" preprocessor symbol is constructed as <prefix>_<memClassSymbol> where prefix is defined in the same way as for the enclosing MemorySection. See also AUTOSAR_SWS_CompilerAbstraction SWS_COMPILER_00040.
        """
        return self.memClassSymbol

    def setMemClassSymbol(self, value: Optional[CIdentifier]) -> "MemorySection":
        """
        Defines a specific symbol in order to generate the compiler abstraction "memclass" code for this MemorySection. The existence of this attribute supersedes the usage of swAddrmethod.shortName for this purpose. The complete name of the "memclass" preprocessor symbol is constructed as <prefix>_<memClassSymbol> where prefix is defined in the same way as for the enclosing MemorySection. See also AUTOSAR_SWS_CompilerAbstraction SWS_COMPILER_00040.
        A None value is a no-op and does not overwrite an existing memClassSymbol.
        """
        if value is not None:
            self.memClassSymbol = value
        return self

    def addOption(self, option: Optional[Identifier]) -> "MemorySection":
        """
        The service (in AUTOSAR: BswModuleEntry) is implemented in a way that it either resolves to aninline function or to a standard function depending on conditions set at a later point in time. The following two values are standardized (to be used for code sections only and exclusively to each other): • INLINE - The code section is declared with the keyword "inline". • LOCAL_INLINE - The code section is declared with the keyword "static inline". In both cases (INLINE and LOCAL_INLINE) the inline expansion depends on the compiler. Depending on this, the code section either corresponds to an actual section in memory or is put into the section of the caller.
        A None value is a no-op and does not append anything.
        """
        if option is not None:
            self.options.append(option)
        return self

    def getOptions(self) -> List[Identifier]:
        """
        The service (in AUTOSAR: BswModuleEntry) is implemented in a way that it either resolves to aninline function or to a standard function depending on conditions set at a later point in time. The following two values are standardized (to be used for code sections only and exclusively to each other): • INLINE - The code section is declared with the keyword "inline". • LOCAL_INLINE - The code section is declared with the keyword "static inline". In both cases (INLINE and LOCAL_INLINE) the inline expansion depends on the compiler. Depending on this, the code section either corresponds to an actual section in memory or is put into the section of the caller.
        """
        return self.options

    def getPrefixRef(self) -> Optional[RefType]:
        """
        The prefix used to set the memory section's namespace in the code. The existence of a prefix element supersedes rules for a default prefix (such as the Bsw ModuleDescription's shortName). This allows the user to define several name spaces for memory sections within the scope of one module, cluster or SWC.
        """
        return self.prefixRef

    def setPrefixRef(self, value: Optional[RefType]) -> "MemorySection":
        """
        The prefix used to set the memory section's namespace in the code. The existence of a prefix element supersedes rules for a default prefix (such as the Bsw ModuleDescription's shortName). This allows the user to define several name spaces for memory sections within the scope of one module, cluster or SWC.
        A None value is a no-op and does not overwrite an existing prefixRef.
        """
        if value is not None:
            self.prefixRef = value
        return self

    def getSize(self) -> Optional[PositiveInteger]:
        """
        The size in bytes of the section.
        """
        return self.size

    def setSize(self, value: Optional[PositiveInteger]) -> "MemorySection":
        """
        The size in bytes of the section.
        A None value is a no-op and does not overwrite an existing size.
        """
        if value is not None:
            self.size = value
        return self

    def getSwAddrMethodRef(self) -> Optional[RefType]:
        """
        This association indicates that this module specific (abstract) memory section is part of an overall SwAddr Method, referred by the upstream declarations (e.g. calibration parameters, data element prototypes, code entities) which share a common addressing strategy. This can be evaluated for the ECU configuration of the build support. This association shall always be declared by the Implementation description of the module or component, which allocates the memory in its code. This means in case of data prototypes which are allocated by the RTE, that the software components only declare the grouping of its data prototypes to SwAddrMethods, and the generated Implementation Description of the RTE actually sets up this association.
        """
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value: Optional[RefType]) -> "MemorySection":
        """
        This association indicates that this module specific (abstract) memory section is part of an overall SwAddr Method, referred by the upstream declarations (e.g. calibration parameters, data element prototypes, code entities) which share a common addressing strategy. This can be evaluated for the ECU configuration of the build support. This association shall always be declared by the Implementation description of the module or component, which allocates the memory in its code. This means in case of data prototypes which are allocated by the RTE, that the software components only declare the grouping of its data prototypes to SwAddrMethods, and the generated Implementation Description of the RTE actually sets up this association.
        A None value is a no-op and does not overwrite an existing swAddrMethodRef.
        """
        if value is not None:
            self.swAddrMethodRef = value
        return self

    def getSymbol(self) -> Optional[Identifier]:
        """
        Defines the section name as explained in the main description. By using this attribute for code generation (instead of the shortName) it is possible to define several different MemorySections having the same name - e.g. symbol = CODE - but using different sectionName Prefixes.
        """
        return self.symbol

    def setSymbol(self, value: Optional[Identifier]) -> "MemorySection":
        """
        Defines the section name as explained in the main description. By using this attribute for code generation (instead of the shortName) it is possible to define several different MemorySections having the same name - e.g. symbol = CODE - but using different sectionName Prefixes.
        A None value is a no-op and does not overwrite an existing symbol.
        """
        if value is not None:
            self.symbol = value
        return self


class SectionNamePrefix(ImplementationProps, VariationPointCapable):
    """
    A prefix to be used for generated code artifacts defining a memory section name in the source code of the using module or SWC.
    """

    # SectionNamePrefix method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.8, p.147
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getImplementedInRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImplementedInRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Optional reference that allows to Indicate the code artifact (header file) containing the preprocessor implementation of memory sections with this prefix. The usage of this link supersedes the usage of a memory mapping header with the default name (derived from the BswModuleDescription's shortName).
        self.implementedInRef: Optional[RefType] = None

    def getImplementedInRef(self) -> Optional[RefType]:
        """
        Optional reference that allows to Indicate the code artifact (header file) containing the preprocessor implementation of memory sections with this prefix. The usage of this link supersedes the usage of a memory mapping header with the default name (derived from the BswModuleDescription's shortName).
        """
        return self.implementedInRef

    def setImplementedInRef(self, value: Optional[RefType]) -> "SectionNamePrefix":
        """
        Optional reference that allows to Indicate the code artifact (header file) containing the preprocessor implementation of memory sections with this prefix. The usage of this link supersedes the usage of a memory mapping header with the default name (derived from the BswModuleDescription's shortName).
        A None value is a no-op and does not overwrite an existing implementedInRef.
        """
        if value is not None:
            self.implementedInRef = value
        return self
