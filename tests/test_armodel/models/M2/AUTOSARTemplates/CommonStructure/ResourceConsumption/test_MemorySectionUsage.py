"""
This module contains tests for the MemorySection and SectionNamePrefix classes
(MemorySectionUsage) against the AUTOSAR spec tables
(AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate, Tables 8.2 / 8.8).
"""

import inspect
from typing import List, Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import (
    MemorySection,
    SectionNamePrefix,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    CIdentifier,
    Identifier,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import (
    VariationPointCapable,
)

MEMORY_SECTION_NOTE = (
    "Provides a description of an abstract memory section used in the Implementation for code or data. "
    "It shall be declared by the Implementation Description of the module or component, which actually allocates the memory in its code. "
    "This means in case of data prototypes which are allocated by the RTE, that the generated Implementation Description of the RTE shall contain the corresponding MemorySections. "
    'The attribute "symbol" (if symbol is missing: "shortName") defines the module or component specific section name used in the code. '
    'For details see the document "Specification of Memory Mapping". '
    "Typically the section name is build according the pattern: "
    "<SwAddrMethod shortName>[_<further specialization nominator>][_<alignment>] "
    "where "
    "• [<SwAddrMethod shortName>] is the shortName of the referenced SwAddrMethod "
    "• [_<further specialization nominator>] is an optional infix to indicate the specialization in the case that several MemorySections for different purpose of the same Implementation Description referring to the same or equally named SwAddrMethods. "
    "• [_<alignment>] is the alignment attributes value and is only applicable in the case that the memory AllocationKeywordPolicy value of the referenced SwAddrMethod is set to addrMethodShortNameAnd Alignment"
)

ALIGNMENT_NOTE = "The attribute describes the typical alignment of objects within this memory section."

EXECUTABLE_ENTITY_NOTE = (
    "Reference to the ExecutableEntitites located in this section. "
    "This allows to locate different Executable Entitities in different sections even if the associated Sw Addrmethod is the same. "
    "This is applicable to code sections only."
)

OPTION_NOTE = (
    "The service (in AUTOSAR: BswModuleEntry) is implemented in a way that it either resolves to aninline function or to a standard function "
    "depending on conditions set at a later point in time. "
    "The following two values are standardized (to be used for code sections only and exclusively to each other): "
    '• INLINE - The code section is declared with the keyword "inline". '
    '• LOCAL_INLINE - The code section is declared with the keyword "static inline". '
    "In both cases (INLINE and LOCAL_INLINE) the inline expansion depends on the compiler. "
    "Depending on this, the code section either corresponds to an actual section in memory or is put into the section of the caller."
)

PREFIX_NOTE = (
    "The prefix used to set the memory section's namespace in the code. "
    "The existence of a prefix element supersedes rules for a default prefix (such as the Bsw ModuleDescription's shortName). "
    "This allows the user to define several name spaces for memory sections within the scope of one module, cluster or SWC."
)

SIZE_NOTE = "The size in bytes of the section."

SW_ADDRMETHOD_NOTE = (
    "This association indicates that this module specific (abstract) memory section is part of an overall SwAddr Method, "
    "referred by the upstream declarations (e.g. calibration parameters, data element prototypes, code entities) which share a common addressing strategy. "
    "This can be evaluated for the ECU configuration of the build support. "
    "This association shall always be declared by the Implementation description of the module or component, which allocates the memory in its code. "
    "This means in case of data prototypes which are allocated by the RTE, that the software components only declare the grouping of its data prototypes to SwAddrMethods, "
    "and the generated Implementation Description of the RTE actually sets up this association."
)

SYMBOL_NOTE = (
    "Defines the section name as explained in the main description. "
    "By using this attribute for code generation (instead of the shortName) it is possible to define several different MemorySections "
    "having the same name - e.g. symbol = CODE - but using different sectionName Prefixes."
)

MEM_CLASS_SYMBOL_NOTE = (
    'Defines a specific symbol in order to generate the compiler abstraction "memclass" code for this MemorySection. '
    "The existence of this attribute supersedes the usage of swAddrmethod.shortName for this purpose. "
    'The complete name of the "memclass" preprocessor symbol is constructed as <prefix>_<memClassSymbol> '
    "where prefix is defined in the same way as for the enclosing MemorySection. "
    "See also AUTOSAR_SWS_CompilerAbstraction SWS_COMPILER_00040."
)

SECTION_NAME_PREFIX_NOTE = "A prefix to be used for generated code artifacts defining a memory section name in the source code of the using module or SWC."

IMPLEMENTED_IN_NOTE = (
    "Optional reference that allows to Indicate the code artifact (header file) containing the preprocessor implementation of memory sections with this prefix. "
    "The usage of this link supersedes the usage of a memory mapping header with the default name (derived from the BswModuleDescription's shortName)."
)


def _setter_tail(name):
    return "A None value is a no-op and does not overwrite an existing %s." % name


APPEND_TAIL = "A None value is a no-op and does not append anything."


def _doc(method):
    return inspect.cleandoc(method.__doc__)


def _make_ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestMemorySection:
    """
    Test class for MemorySection functionality (Table 8.2).
    """

    def test_base_chain(self):
        assert issubclass(MemorySection, Identifiable)
        assert issubclass(MemorySection, VariationPointCapable)

    def test_class_docstring_verbatim(self):
        assert inspect.cleandoc(MemorySection.__doc__) == MEMORY_SECTION_NOTE

    def test_initialization(self):
        obj = _instantiate(MemorySection, "MemorySection")
        assert obj.getShortName() == "MemorySection"
        assert obj.getAlignment() is None
        assert obj.getExecutableEntityRefs() == []
        assert obj.getMemClassSymbol() is None
        assert obj.getOptions() == []
        assert obj.getPrefixRef() is None
        assert obj.getSize() is None
        assert obj.getSwAddrMethodRef() is None
        assert obj.getSymbol() is None

    def test_annotations_match_spec_types(self):
        hints = get_type_hints(MemorySection.getAlignment)
        assert hints["return"] == Optional[AlignmentType]
        hints = get_type_hints(MemorySection.getSymbol)
        assert hints["return"] == Optional[Identifier]
        hints = get_type_hints(MemorySection.getMemClassSymbol)
        assert hints["return"] == Optional[CIdentifier]
        hints = get_type_hints(MemorySection.getSize)
        assert hints["return"] == Optional[PositiveInteger]
        hints = get_type_hints(MemorySection.getSwAddrMethodRef)
        assert hints["return"] == Optional[RefType]
        hints = get_type_hints(MemorySection.getExecutableEntityRefs)
        assert hints["return"] == List[RefType]

    def test_get_set_alignment(self):
        obj = _instantiate(MemorySection, "MS")
        assert obj.setAlignment(AlignmentType().setValue("16")) is obj
        assert isinstance(obj.getAlignment(), AlignmentType)
        assert obj.getAlignment().getValue() == "16"
        obj.setAlignment(None)
        assert obj.getAlignment().getValue() == "16"

    def test_get_set_mem_class_symbol(self):
        obj = _instantiate(MemorySection, "MS")
        obj.setMemClassSymbol(CIdentifier().setValue("MEMCLASS"))
        assert obj.getMemClassSymbol().getValue() == "MEMCLASS"
        obj.setMemClassSymbol(None)
        assert obj.getMemClassSymbol().getValue() == "MEMCLASS"

    def test_get_set_prefix_ref(self):
        obj = _instantiate(MemorySection, "MS")
        obj.setPrefixRef(_make_ref("SECTION-NAME-PREFIX", "/Pkg/Prefix"))
        assert obj.getPrefixRef().getValue() == "/Pkg/Prefix"
        assert obj.getPrefixRef().getDest() == "SECTION-NAME-PREFIX"
        obj.setPrefixRef(None)
        assert obj.getPrefixRef().getValue() == "/Pkg/Prefix"

    def test_get_set_size(self):
        obj = _instantiate(MemorySection, "MS")
        obj.setSize(PositiveInteger().setValue("4096"))
        assert obj.getSize().getValue() == 4096
        obj.setSize(None)
        assert obj.getSize().getValue() == 4096

    def test_get_set_sw_addr_method_ref(self):
        obj = _instantiate(MemorySection, "MS")
        obj.setSwAddrMethodRef(_make_ref("SW-ADDR-METHOD", "/Pkg/AddrMethod"))
        assert obj.getSwAddrMethodRef().getValue() == "/Pkg/AddrMethod"
        obj.setSwAddrMethodRef(None)
        assert obj.getSwAddrMethodRef().getValue() == "/Pkg/AddrMethod"

    def test_get_set_symbol(self):
        obj = _instantiate(MemorySection, "MS")
        obj.setSymbol(Identifier().setValue("CODE"))
        assert obj.getSymbol().getValue() == "CODE"
        obj.setSymbol(None)
        assert obj.getSymbol().getValue() == "CODE"

    def test_add_executable_entity_ref(self):
        obj = _instantiate(MemorySection, "MS")
        assert obj.addExecutableEntityRef(_make_ref("EXECUTABLE-ENTITY", "/Pkg/EE1")) is obj
        assert obj.addExecutableEntityRef(_make_ref("EXECUTABLE-ENTITY", "/Pkg/EE2")) is obj
        refs = obj.getExecutableEntityRefs()
        assert [ref.getValue() for ref in refs] == ["/Pkg/EE1", "/Pkg/EE2"]
        obj.addExecutableEntityRef(None)
        assert len(obj.getExecutableEntityRefs()) == 2

    def test_add_option(self):
        obj = _instantiate(MemorySection, "MS")
        assert obj.addOption(Identifier().setValue("INLINE")) is obj
        assert obj.addOption(Identifier().setValue("LOCAL_INLINE")) is obj
        assert [option.getValue() for option in obj.getOptions()] == ["INLINE", "LOCAL_INLINE"]
        obj.addOption(None)
        assert len(obj.getOptions()) == 2

    def test_docstrings_verbatim(self):
        assert _doc(MemorySection.getAlignment) == ALIGNMENT_NOTE
        assert _doc(MemorySection.setAlignment) == ALIGNMENT_NOTE + "\n" + _setter_tail("alignment")
        assert _doc(MemorySection.getExecutableEntityRefs) == EXECUTABLE_ENTITY_NOTE
        assert _doc(MemorySection.addExecutableEntityRef) == EXECUTABLE_ENTITY_NOTE + "\n" + APPEND_TAIL
        assert _doc(MemorySection.getOptions) == OPTION_NOTE
        assert _doc(MemorySection.addOption) == OPTION_NOTE + "\n" + APPEND_TAIL
        assert _doc(MemorySection.getPrefixRef) == PREFIX_NOTE
        assert _doc(MemorySection.setPrefixRef) == PREFIX_NOTE + "\n" + _setter_tail("prefixRef")
        assert _doc(MemorySection.getSize) == SIZE_NOTE
        assert _doc(MemorySection.setSize) == SIZE_NOTE + "\n" + _setter_tail("size")
        assert _doc(MemorySection.getSwAddrMethodRef) == SW_ADDRMETHOD_NOTE
        assert _doc(MemorySection.setSwAddrMethodRef) == SW_ADDRMETHOD_NOTE + "\n" + _setter_tail("swAddrMethodRef")
        assert _doc(MemorySection.getSymbol) == SYMBOL_NOTE
        assert _doc(MemorySection.setSymbol) == SYMBOL_NOTE + "\n" + _setter_tail("symbol")
        assert _doc(MemorySection.getMemClassSymbol) == MEM_CLASS_SYMBOL_NOTE
        assert _doc(MemorySection.setMemClassSymbol) == MEM_CLASS_SYMBOL_NOTE + "\n" + _setter_tail("memClassSymbol")


class TestSectionNamePrefix:
    """
    Test class for SectionNamePrefix functionality (Table 8.8).
    """

    def test_base_chain(self):
        assert issubclass(SectionNamePrefix, ImplementationProps)
        assert issubclass(SectionNamePrefix, VariationPointCapable)

    def test_class_docstring_verbatim(self):
        assert inspect.cleandoc(SectionNamePrefix.__doc__) == SECTION_NAME_PREFIX_NOTE

    def test_initialization(self):
        obj = _instantiate(SectionNamePrefix, "SectionNamePrefix")
        assert obj.getShortName() == "SectionNamePrefix"
        assert obj.getImplementedInRef() is None
        assert obj.getSymbol() is None

    def test_get_set_implemented_in_ref(self):
        obj = _instantiate(SectionNamePrefix, "SNP")
        assert obj.setImplementedInRef(_make_ref("DEPENDENCY-ON-ARTIFACT", "/Pkg/Artifact")) is obj
        assert obj.getImplementedInRef().getValue() == "/Pkg/Artifact"
        assert obj.getImplementedInRef().getDest() == "DEPENDENCY-ON-ARTIFACT"
        obj.setImplementedInRef(None)
        assert obj.getImplementedInRef().getValue() == "/Pkg/Artifact"

    def test_docstrings_verbatim(self):
        assert _doc(SectionNamePrefix.getImplementedInRef) == IMPLEMENTED_IN_NOTE
        assert _doc(SectionNamePrefix.setImplementedInRef) == IMPLEMENTED_IN_NOTE + "\n" + _setter_tail("implementedInRef")
