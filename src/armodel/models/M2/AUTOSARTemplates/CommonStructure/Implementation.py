"""
This module contains classes for representing AUTOSAR implementation structures
in the CommonStructure module. Implementation classes define software implementations
including code descriptors, compilers, dependencies, and resource consumption information.
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from abc import ABC
from typing import TYPE_CHECKING, List, Optional
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import McSupportData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String, RevisionLabelString, AREnum, CIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption


class DependencyUsageEnum(AREnum):
    """
    Enumeration describing the process steps a dependency is valid in.
    """

    # DependencyUsageEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.4, p.132
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The object referred by the dependency is required during the build process. Tags: atp.EnumerationLiteralIndex=0
    BUILD = "build"

    # The object referred by the dependency is required during code generation Tags: atp.EnumerationLiteralIndex=1
    CODEGENERATION = "codegeneration"

    # The object referred by the dependency is required during compilation. Tags: atp.EnumerationLiteralIndex=2
    COMPILE = "compile"

    # The object referred by the dependency is required at execution time. Tags: atp.EnumerationLiteralIndex=3
    EXECUTE = "execute"

    # The object referred by the dependency is required during linking. Tags: atp.EnumerationLiteralIndex=4
    LINK = "link"

    def __init__(self):
        super().__init__(
            (
                DependencyUsageEnum.BUILD,
                DependencyUsageEnum.CODEGENERATION,
                DependencyUsageEnum.COMPILE,
                DependencyUsageEnum.EXECUTE,
                DependencyUsageEnum.LINK,
            )
        )


class ProgramminglanguageEnum(AREnum):
    """
    Programming language the implementation was created in.
    """

    # ProgramminglanguageEnum method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.2, p.621 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # C language. Tags: atp.EnumerationLiteralIndex=0
    C = "c"

    # C++ language. Tags: atp.EnumerationLiteralIndex=1
    CPP = "cpp"

    # Java language. Tags: atp.EnumerationLiteralIndex=2
    JAVA = "java"

    def __init__(self):
        super().__init__(
            (
                ProgramminglanguageEnum.C,
                ProgramminglanguageEnum.CPP,
                ProgramminglanguageEnum.JAVA,
            )
        )


class ImplementationProps(Referrable, ABC):
    """
    Define a symbol to be used as (depending on the concrete case) either a complete
    replacement or a prefix when generating code artifacts.
    """

    # ImplementationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.20, p.287
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getSymbol                    [x] impl  [x] docstring  [x] test
    # [x] setSymbol                    [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the ImplementationProps with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this implementation properties
            short_name: The unique short name of this implementation properties
        """
        if type(self) is ImplementationProps:
            raise TypeError("ImplementationProps is an abstract class.")

        super().__init__(parent, short_name)

        # The symbol to be used as (depending on the concrete case) either a complete
        # replacement or a prefix. [constr_1909]
        self.symbol: Optional[CIdentifier] = None

    def getSymbol(self) -> Optional[CIdentifier]:
        """
        Gets the symbol to be used as (depending on the concrete case) either a complete
        replacement or a prefix when generating code artifacts. [constr_1909]

        Returns:
            CIdentifier representing the symbol
        """
        return self.symbol

    def setSymbol(self, value: Optional[CIdentifier]) -> "ImplementationProps":
        """
        Sets the symbol to be used as (depending on the concrete case) either a complete
        replacement or a prefix when generating code artifacts. A None value is a no-op
        and does not overwrite an existing symbol. [constr_1909]

        Args:
            value: The symbol to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbol = value
        return self


class Code(Identifiable):
    """
    A generic code descriptor. The type of the code (source or object) is defined via the category attribute of the associated engineering object.
    """

    # Code method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.2, p.130 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addArtifactDescriptor   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArtifactDescriptors  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getCallbackHeaderRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addCallbackHeaderRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        # Refers to the artifact belonging to this code descriptor.
        self.artifactDescriptors: List[AutosarEngineeringObject] = []

        # The association callbackHeader describes in which header files the function declarations of callback functions are provided to a service module. With this information the service module can include the appropriate header files in its configuration files.
        self.callbackHeaderRefs: List[RefType] = []

    def addArtifactDescriptor(self, desc: Optional[AutosarEngineeringObject]) -> "Code":
        """Refers to the artifact belonging to this code descriptor. A None value is a no-op and does not append anything."""
        if desc is not None:
            self.artifactDescriptors.append(desc)
        return self

    def getArtifactDescriptors(self, category: str = "") -> List[AutosarEngineeringObject]:
        """Refers to the artifact belonging to this code descriptor."""
        if category == "":
            return self.artifactDescriptors
        else:
            return list(filter(lambda a: a.getCategory().getText() == category, self.artifactDescriptors))

    def getCallbackHeaderRefs(self) -> List[RefType]:
        """The association callbackHeader describes in which header files the function declarations of callback functions are provided to a service module. With this information the service module can include the appropriate header files in its configuration files."""
        return self.callbackHeaderRefs

    def addCallbackHeaderRef(self, value: Optional[RefType]) -> "Code":
        """The association callbackHeader describes in which header files the function declarations of callback functions are provided to a service module. With this information the service module can include the appropriate header files in its configuration files. A None value is a no-op and does not append anything."""
        if value is not None:
            self.callbackHeaderRefs.append(value)
        return self


class Compiler(Identifiable):
    """
    Specifies the compiler attributes. In case of source code this specifies requirements
    how the compiler shall be invoked. In case of object code this documents the used
    compiler settings.
    """

    # Compiler method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.7, p.133 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getName    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setName    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOptions [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOptions [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVendor  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVendor  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVersion [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVersion [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        # Compiler name (like gcc).
        self.name: Optional[String] = None

        # Specifies the compiler options.
        self.options: Optional[String] = None

        # Vendor of compiler.
        self.vendor: Optional[String] = None

        # Exact version of compiler executable.
        self.version: Optional[String] = None

    def getName(self) -> Optional[String]:
        """Compiler name (like gcc)."""
        return self.name

    def setName(self, value: Optional[String]) -> "Compiler":
        """Compiler name (like gcc). Only sets the value if it is not None."""
        if value is not None:
            self.name = value
        return self

    def getOptions(self) -> Optional[String]:
        """Specifies the compiler options."""
        return self.options

    def setOptions(self, value: Optional[String]) -> "Compiler":
        """Specifies the compiler options. Only sets the value if it is not None."""
        if value is not None:
            self.options = value
        return self

    def getVendor(self) -> Optional[String]:
        """Vendor of compiler."""
        return self.vendor

    def setVendor(self, value: Optional[String]) -> "Compiler":
        """Vendor of compiler. Only sets the value if it is not None."""
        if value is not None:
            self.vendor = value
        return self

    def getVersion(self) -> Optional[String]:
        """Exact version of compiler executable."""
        return self.version

    def setVersion(self, value: Optional[String]) -> "Compiler":
        """Exact version of compiler executable. Only sets the value if it is not None."""
        if value is not None:
            self.version = value
        return self


class DependencyOnArtifact(Identifiable, VariationPointCapable):
    """
    Dependency on the existence of another artifact, e.g. a library.
    """

    # DependencyOnArtifact method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.3, p.131 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArtifactDescriptor [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArtifactDescriptor [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUsages            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addUsage             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str) -> None:

        super().__init__(parent, short_name)

        # The specified artifact needs to exist.
        self.artifactDescriptor: Optional[AutosarEngineeringObject] = None

        # Specification for which process step(s) this dependency is required.
        self.usages: List[DependencyUsageEnum] = []

    def getArtifactDescriptor(self) -> Optional[AutosarEngineeringObject]:
        """The specified artifact needs to exist."""
        return self.artifactDescriptor

    def setArtifactDescriptor(self, value: Optional[AutosarEngineeringObject]) -> "DependencyOnArtifact":
        """The specified artifact needs to exist. A None value is a no-op and does not overwrite an existing artifact."""
        if value is not None:
            self.artifactDescriptor = value
        return self

    def getUsages(self) -> List[DependencyUsageEnum]:
        """Specification for which process step(s) this dependency is required."""
        return self.usages

    def addUsage(self, value: Optional[DependencyUsageEnum]) -> "DependencyOnArtifact":
        """Specification for which process step(s) this dependency is required. A None value is a no-op and does not append anything."""
        if value is not None:
            self.usages.append(value)
        return self


class Linker(Identifiable):
    """
    Specifies the linker attributes used to describe how the linker shall be invoked.
    """

    # Linker method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.8, p.134 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getName    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setName    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOptions [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOptions [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVendor  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVendor  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVersion [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVersion [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the Linker with a parent and short name.

        Args:
            parent: The parent ARObject that contains this linker
            short_name: The unique short name of this linker
        """
        super().__init__(parent, short_name)

        # Linker name.
        self.name: Optional[String] = None

        # Specifies the linker options.
        self.options: Optional[String] = None

        # Vendor of linker.
        self.vendor: Optional[String] = None

        # Exact version of linker executable.
        self.version: Optional[String] = None

    def getName(self) -> Optional[String]:
        """Linker name."""
        return self.name

    def setName(self, value: Optional[String]) -> "Linker":
        """Linker name. A None value is a no-op and does not overwrite an existing name."""
        if value is not None:
            self.name = value
        return self

    def getOptions(self) -> Optional[String]:
        """Specifies the linker options."""
        return self.options

    def setOptions(self, value: Optional[String]) -> "Linker":
        """Specifies the linker options. A None value is a no-op and does not overwrite an existing options."""
        if value is not None:
            self.options = value
        return self

    def getVendor(self) -> Optional[String]:
        """Vendor of linker."""
        return self.vendor

    def setVendor(self, value: Optional[String]) -> "Linker":
        """Vendor of linker. A None value is a no-op and does not overwrite an existing vendor."""
        if value is not None:
            self.vendor = value
        return self

    def getVersion(self) -> Optional[String]:
        """Exact version of linker executable."""
        return self.version

    def setVersion(self, value: Optional[String]) -> "Linker":
        """Exact version of linker executable. A None value is a no-op and does not overwrite an existing version."""
        if value is not None:
            self.version = value
        return self


class Implementation(ARElement, ABC):
    """
    Description of an implementation a single software component or module.
    """

    # Implementation method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.1, p.128 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBuildActionManifestRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBuildActionManifestRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCodeDescriptors               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCodeDescriptor             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCompilers                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCompiler                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getGeneratedArtifacts            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createGeneratedArtifact          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHwElementRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addHwElementRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLinkers                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createLinker                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMcSupport                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMcSupport                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProgrammingLanguage           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProgrammingLanguage           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredArtifacts             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRequiredArtifact           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredGeneratorTools        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRequiredGeneratorTool      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResourceConsumption           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createResourceConsumption        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcBswMappingRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcBswMappingRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwVersion                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwVersion                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUsedCodeGenerator             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUsedCodeGenerator             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVendorId                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVendorId                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # Spec verified: R23-11

    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is Implementation:
            raise TypeError("Implementation is an abstract class.")

        super().__init__(parent, short_name)

        # A manifest specifying the intended build actions for the software delivered with this implementation.
        self.buildActionManifestRef: Optional[RefType] = None

        # Specifies the provided implementation code.
        self.codeDescriptors: List[Code] = []

        # Specifies the compiler for which this implementation has been released.
        self.compilers: List[Compiler] = []

        # Relates to an artifact that will be generated during the integration of this Implementation by an associated generator tool.
        self.generatedArtifacts: List[DependencyOnArtifact] = []

        # The hardware elements (e.g. the processor) required for this implementation.
        self.hwElementRefs: List[RefType] = []

        # Specifies the linker for which this implementation has been released.
        self.linkers: List[Linker] = []

        # The measurement & calibration support data belonging to this implementation.
        self.mcSupport: Optional[McSupportData] = None

        # Programming language the implementation was created in.
        self.programmingLanguage: Optional[ProgramminglanguageEnum] = None

        # Specifies that this Implementation depends on the existence of another artifact (e.g. a library).
        self.requiredArtifacts: List[DependencyOnArtifact] = []

        # Relates this Implementation to a generator tool in order to generate additional artifacts during integration.
        self.requiredGeneratorTools: List[DependencyOnArtifact] = []

        # All static and dynamic resources for each implementation are described within the ResourceConsumption class.
        self.resourceConsumption: Optional[ResourceConsumption] = None

        # This allows a mapping between an SWC and a BSW behavior to be attached to an implementation description (for AUTOSAR Service, ECU Abstraction and Complex Driver Components). It is up to the methodology to define whether this reference has to be set for the Swc- or BswImplementtion or for both.
        self.swcBswMappingRef: Optional[RefType] = None

        # Software version of this implementation. The numbering contains three levels (like major, minor, patch), its values are vendor specific.
        self.swVersion: Optional[RevisionLabelString] = None

        # Optional: code generator used.
        self.usedCodeGenerator: Optional[String] = None

        # Vendor ID of this Implementation according to the AUTOSAR vendor list.
        self.vendorId: Optional[PositiveInteger] = None

    def getBuildActionManifestRef(self) -> Optional[RefType]:
        """A manifest specifying the intended build actions for the software delivered with this implementation."""
        return self.buildActionManifestRef

    def setBuildActionManifestRef(self, value: Optional[RefType]) -> "Implementation":
        """A manifest specifying the intended build actions for the software delivered with this implementation. A None value is a no-op and does not overwrite the existing reference."""
        if value is not None:
            self.buildActionManifestRef = value
        return self

    def getCodeDescriptors(self) -> List[Code]:
        """Specifies the provided implementation code."""
        return self.codeDescriptors

    def createCodeDescriptor(self, short_name: str) -> Code:
        """
        Creates and adds a Code descriptor to this implementation.

        Args:
            short_name: The short name for the new code descriptor

        Returns:
            The created Code instance
        """
        if not self.IsElementExists(short_name, Code):
            code_descriptor = Code(self, short_name)
            self.addElement(code_descriptor)
            self.codeDescriptors.append(code_descriptor)
        return self.getElement(short_name, Code)

    def getCompilers(self) -> List[Compiler]:
        """Specifies the compiler for which this implementation has been released."""
        return self.compilers

    def createCompiler(self, short_name: str) -> Compiler:
        """
        Creates and adds a Compiler to this implementation.

        Args:
            short_name: The short name for the new compiler

        Returns:
            The created Compiler instance
        """
        if not self.IsElementExists(short_name, Compiler):
            compiler = Compiler(self, short_name)
            self.addElement(compiler)
            self.compilers.append(compiler)
        return self.getElement(short_name, Compiler)

    def getGeneratedArtifacts(self) -> List[DependencyOnArtifact]:
        """Relates to an artifact that will be generated during the integration of this Implementation by an associated generator tool."""
        return self.generatedArtifacts

    def createGeneratedArtifact(self, short_name: str) -> DependencyOnArtifact:
        """
        Creates and adds a generated artifact to this implementation.

        Args:
            short_name: The short name for the new generated artifact

        Returns:
            The created DependencyOnArtifact instance
        """
        if not self.IsElementExists(short_name, DependencyOnArtifact):
            artifact = DependencyOnArtifact(self, short_name)
            self.addElement(artifact)
            self.generatedArtifacts.append(artifact)
        return self.getElement(short_name, DependencyOnArtifact)

    def getHwElementRefs(self) -> List[RefType]:
        """The hardware elements (e.g. the processor) required for this implementation."""
        return self.hwElementRefs

    def addHwElementRef(self, value: Optional[RefType]) -> "Implementation":
        """The hardware elements (e.g. the processor) required for this implementation. A None value is a no-op and is not appended."""
        if value is not None:
            self.hwElementRefs.append(value)
        return self

    def getLinkers(self) -> List[Linker]:
        """Specifies the linker for which this implementation has been released."""
        return self.linkers

    def createLinker(self, short_name: str) -> Linker:
        """
        Creates and adds a Linker to this implementation.

        Args:
            short_name: The short name for the new linker

        Returns:
            The created Linker instance
        """
        if not self.IsElementExists(short_name, Linker):
            linker = Linker(self, short_name)
            self.addElement(linker)
            self.linkers.append(linker)
        return self.getElement(short_name, Linker)

    def getMcSupport(self) -> Optional[McSupportData]:
        """The measurement & calibration support data belonging to this implementation."""
        return self.mcSupport

    def setMcSupport(self, value: Optional[McSupportData]) -> "Implementation":
        """The measurement & calibration support data belonging to this implementation. A None value is a no-op and does not overwrite the existing value."""
        if value is not None:
            self.mcSupport = value
        return self

    def getProgrammingLanguage(self) -> Optional[ProgramminglanguageEnum]:
        """Programming language the implementation was created in."""
        return self.programmingLanguage

    def setProgrammingLanguage(self, value: Optional[ProgramminglanguageEnum]) -> "Implementation":
        """Programming language the implementation was created in. A None value is a no-op and does not overwrite the existing value."""
        if value is not None:
            self.programmingLanguage = value
        return self

    def getRequiredArtifacts(self) -> List[DependencyOnArtifact]:
        """Specifies that this Implementation depends on the existence of another artifact (e.g. a library)."""
        return self.requiredArtifacts

    def createRequiredArtifact(self, short_name: str) -> DependencyOnArtifact:
        """
        Creates and adds a required artifact to this implementation.

        Args:
            short_name: The short name for the new required artifact

        Returns:
            The created DependencyOnArtifact instance
        """
        if not self.IsElementExists(short_name, DependencyOnArtifact):
            artifact = DependencyOnArtifact(self, short_name)
            self.addElement(artifact)
            self.requiredArtifacts.append(artifact)
        return self.getElement(short_name, DependencyOnArtifact)

    def getRequiredGeneratorTools(self) -> List[DependencyOnArtifact]:
        """Relates this Implementation to a generator tool in order to generate additional artifacts during integration."""
        return self.requiredGeneratorTools

    def createRequiredGeneratorTool(self, short_name: str) -> DependencyOnArtifact:
        """
        Creates and adds a required generator tool to this implementation.

        Args:
            short_name: The short name for the new required generator tool

        Returns:
            The created DependencyOnArtifact instance
        """
        if not self.IsElementExists(short_name, DependencyOnArtifact):
            tool = DependencyOnArtifact(self, short_name)
            self.addElement(tool)
            self.requiredGeneratorTools.append(tool)
        return self.getElement(short_name, DependencyOnArtifact)

    def getResourceConsumption(self) -> Optional[ResourceConsumption]:
        """All static and dynamic resources for each implementation are described within the ResourceConsumption class."""
        return self.resourceConsumption

    def createResourceConsumption(self, short_name: str) -> ResourceConsumption:
        """
        Creates and adds a ResourceConsumption to this implementation.

        Args:
            short_name: The short name for the new resource consumption

        Returns:
            The created ResourceConsumption instance
        """
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption

        if not self.IsElementExists(short_name, ResourceConsumption):
            consumption = ResourceConsumption(self, short_name)
            self.addElement(consumption)
            self.resourceConsumption = consumption
        return self.getElement(short_name, ResourceConsumption)

    def getSwcBswMappingRef(self) -> Optional[RefType]:
        """This allows a mapping between an SWC and a BSW behavior to be attached to an implementation description (for AUTOSAR Service, ECU Abstraction and Complex Driver Components). It is up to the methodology to define whether this reference has to be set for the Swc- or BswImplementtion or for both."""
        return self.swcBswMappingRef

    def setSwcBswMappingRef(self, value: Optional[RefType]) -> "Implementation":
        """This allows a mapping between an SWC and a BSW behavior to be attached to an implementation description (for AUTOSAR Service, ECU Abstraction and Complex Driver Components). It is up to the methodology to define whether this reference has to be set for the Swc- or BswImplementtion or for both. A None value is a no-op and does not overwrite the existing reference."""
        if value is not None:
            self.swcBswMappingRef = value
        return self

    def getSwVersion(self) -> Optional[RevisionLabelString]:
        """Software version of this implementation. The numbering contains three levels (like major, minor, patch), its values are vendor specific."""
        return self.swVersion

    def setSwVersion(self, value: Optional[RevisionLabelString]) -> "Implementation":
        """Software version of this implementation. The numbering contains three levels (like major, minor, patch), its values are vendor specific. A None value is a no-op and does not overwrite the existing version."""
        if value is not None:
            self.swVersion = value
        return self

    def getUsedCodeGenerator(self) -> Optional[String]:
        """Optional: code generator used."""
        return self.usedCodeGenerator

    def setUsedCodeGenerator(self, value: Optional[String]) -> "Implementation":
        """Optional: code generator used. A None value is a no-op and does not overwrite the existing value."""
        if value is not None:
            self.usedCodeGenerator = value
        return self

    def getVendorId(self) -> Optional[PositiveInteger]:
        """Vendor ID of this Implementation according to the AUTOSAR vendor list."""
        return self.vendorId

    def setVendorId(self, value: Optional[PositiveInteger]) -> "Implementation":
        """Vendor ID of this Implementation according to the AUTOSAR vendor list. A None value is a no-op and does not overwrite the existing vendor ID."""
        if value is not None:
            self.vendorId = value
        return self
