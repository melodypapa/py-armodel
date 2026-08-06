"""
This module contains classes for representing AUTOSAR implementation structures
in the CommonStructure module. Implementation classes define software implementations
including code descriptors, compilers, dependencies, and resource consumption information.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, List, Optional
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.McSupportData import McSupportData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable, ARElement
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
    # [x] __init__                     [x] impl  [x] docstring  [ ] test

    # The object referred by the dependency is required during the build process. atp.EnumerationLiteralIndex=0
    BUILD = "build"

    # The object referred by the dependency is required during code generation. atp.EnumerationLiteralIndex=1
    CODEGENERATION = "codegeneration"

    # The object referred by the dependency is required during compilation. atp.EnumerationLiteralIndex=2
    COMPILE = "compile"

    # The object referred by the dependency is required at execution time. atp.EnumerationLiteralIndex=3
    EXECUTE = "execute"

    # The object referred by the dependency is required during linking. atp.EnumerationLiteralIndex=4
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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.2, p.621
    # [x] __init__                     [x] impl  [x] docstring  [ ] test

    # C language. atp.EnumerationLiteralIndex=0
    C = "c"

    # C++ language. atp.EnumerationLiteralIndex=1
    CPP = "cpp"

    # Java language. atp.EnumerationLiteralIndex=2
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
    Represents code descriptor in AUTOSAR models.
    A generic code descriptor; the type of the code (source or object) is defined via the
    category attribute of the associated engineering object.
    """

    # Code method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.5, p.622
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] addArtifactDescriptor        [x] impl  [x] docstring  [x] test
    # [x] getArtifactDescriptors       [x] impl  [x] docstring  [x] test
    # [x] getCallbackHeaderRefs        [x] impl  [x] docstring  [x] test
    # [x] addCallbackHeaderRef         [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the Code with a parent and short name.

        Args:
            parent: The parent ARObject that contains this code descriptor
            short_name: The unique short name of this code descriptor
        """
        super().__init__(parent, short_name)

        # Refers to the artifact belonging to this code descriptor.
        self.artifactDescriptors: List[AutosarEngineeringObject] = []

        # Describes in which header files the function declarations of callback functions
        # are provided to a service module, so it can include the appropriate header files.
        self.callbackHeaderRefs: List[RefType] = []

    def addArtifactDescriptor(self, desc: Optional[AutosarEngineeringObject]) -> "Code":
        """
        Adds an artifact descriptor to this code descriptor.
        A None value is a no-op and is not appended. [TPS_BSWMDT_04040]

        Args:
            desc: The artifact descriptor to add

        Returns:
            self for method chaining
        """
        if desc is not None:
            self.artifactDescriptors.append(desc)
        return self

    def getArtifactDescriptors(self, category: str = "") -> List[AutosarEngineeringObject]:
        """
        Gets the list of artifact descriptors, optionally filtered by category.
        For each codeDescriptor all relevant artifacts are referenced through
        artifactDescriptor. [TPS_BSWMDT_04040]

        Args:
            category: Optional category to filter descriptors by (returns all if empty)

        Returns:
            List of AutosarEngineeringObject instances matching the criteria
        """
        if category == "":
            return self.artifactDescriptors
        else:
            return list(filter(lambda a: a.getCategory().getText() == category, self.artifactDescriptors))

    def getCallbackHeaderRefs(self) -> List[RefType]:
        """
        Gets the list of references to the header files that declare the callback functions
        of this code descriptor.

        Returns:
            List of RefType to the callback header files
        """
        return self.callbackHeaderRefs

    def addCallbackHeaderRef(self, value: Optional[RefType]) -> "Code":
        """
        Adds a reference to a header file that declares callback functions of this code
        descriptor. A None value is a no-op and is not appended.

        Args:
            value: The callback header reference to add

        Returns:
            self for method chaining
        """
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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.3, p.621
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getName                      [x] impl  [x] docstring  [x] test
    # [x] setName                      [x] impl  [x] docstring  [x] test
    # [x] getOptions                   [x] impl  [x] docstring  [x] test
    # [x] setOptions                   [x] impl  [x] docstring  [x] test
    # [x] getVendor                    [x] impl  [x] docstring  [x] test
    # [x] setVendor                    [x] impl  [x] docstring  [x] test
    # [x] getVersion                   [x] impl  [x] docstring  [x] test
    # [x] setVersion                   [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the Compiler with a parent and short name.

        Args:
            parent: The parent ARObject that contains this compiler
            short_name: The unique short name of this compiler
        """
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
        """
        Gets the compiler name (like gcc).

        Returns:
            String: The compiler name
        """
        return self.name

    def setName(self, value: Optional[String]) -> "Compiler":
        """
        Sets the compiler name (like gcc). A None value is a no-op and does not overwrite
        an existing name.

        Args:
            value: The compiler name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.name = value
        return self

    def getOptions(self) -> Optional[String]:
        """
        Gets the compiler options.

        Returns:
            String: The compiler options
        """
        return self.options

    def setOptions(self, value: Optional[String]) -> "Compiler":
        """
        Sets the compiler options. A None value is a no-op and does not overwrite the
        existing options.

        Args:
            value: The compiler options to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.options = value
        return self

    def getVendor(self) -> Optional[String]:
        """
        Gets the vendor of the compiler.

        Returns:
            String: The compiler vendor
        """
        return self.vendor

    def setVendor(self, value: Optional[String]) -> "Compiler":
        """
        Sets the vendor of the compiler. A None value is a no-op and does not overwrite the
        existing vendor.

        Args:
            value: The compiler vendor to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.vendor = value
        return self

    def getVersion(self) -> Optional[String]:
        """
        Gets the exact version of the compiler executable.

        Returns:
            String: The compiler version
        """
        return self.version

    def setVersion(self, value: Optional[String]) -> "Compiler":
        """
        Sets the exact version of the compiler executable. A None value is a no-op and does
        not overwrite the existing version.

        Args:
            value: The compiler version to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.version = value
        return self


class DependencyOnArtifact(Identifiable):
    """
    Represents a dependency on the existence of another artifact, e.g. a library.
    """

    # DependencyOnArtifact method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.91, p.413
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getArtifactDescriptor        [x] impl  [x] docstring  [x] test
    # [x] setArtifactDescriptor        [x] impl  [x] docstring  [x] test
    # [x] getUsages                    [x] impl  [x] docstring  [x] test
    # [x] addUsage                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the DependencyOnArtifact with a parent and short name.

        Args:
            parent: The parent ARObject that contains this dependency
            short_name: The unique short name of this dependency
        """
        super().__init__(parent, short_name)

        # The specified artifact needs to exist.
        self.artifactDescriptor: Optional[AutosarEngineeringObject] = None

        # Specification for which process step(s) this dependency is required.
        self.usages: List[DependencyUsageEnum] = []

    def getArtifactDescriptor(self) -> Optional[AutosarEngineeringObject]:
        """
        Gets the artifact that needs to exist for this dependency.

        Returns:
            AutosarEngineeringObject: The artifact descriptor
        """
        return self.artifactDescriptor

    def setArtifactDescriptor(self, value: Optional[AutosarEngineeringObject]) -> "DependencyOnArtifact":
        """
        Sets the artifact that needs to exist for this dependency. A None value is a no-op
        and does not overwrite the existing artifact.

        Args:
            value: The artifact descriptor to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.artifactDescriptor = value
        return self

    def getUsages(self) -> List[DependencyUsageEnum]:
        """
        Gets the list of process steps for which this dependency is required.
        [constr_10304]

        Returns:
            List of DependencyUsageEnum for the process steps
        """
        return self.usages

    def addUsage(self, value: Optional[DependencyUsageEnum]) -> "DependencyOnArtifact":
        """
        Adds a process step for which this dependency is required. A None value is a no-op
        and is not appended. [constr_10304]

        Args:
            value: The process step to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usages.append(value)
        return self


class Linker(Identifiable):
    """
    Specifies the linker attributes used to describe how the linker shall be invoked.
    """

    # Linker method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.4, p.622
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getName                      [x] impl  [x] docstring  [x] test
    # [x] setName                      [x] impl  [x] docstring  [x] test
    # [x] getOptions                   [x] impl  [x] docstring  [x] test
    # [x] setOptions                   [x] impl  [x] docstring  [x] test
    # [x] getVendor                    [x] impl  [x] docstring  [x] test
    # [x] setVendor                    [x] impl  [x] docstring  [x] test
    # [x] getVersion                   [x] impl  [x] docstring  [x] test
    # [x] setVersion                   [x] impl  [x] docstring  [x] test

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
        """
        Gets the linker name.

        Returns:
            String: The linker name
        """
        return self.name

    def setName(self, value: Optional[String]) -> "Linker":
        """
        Sets the linker name. A None value is a no-op and does not overwrite an existing
        name.

        Args:
            value: The linker name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.name = value
        return self

    def getOptions(self) -> Optional[String]:
        """
        Gets the linker options.

        Returns:
            String: The linker options
        """
        return self.options

    def setOptions(self, value: Optional[String]) -> "Linker":
        """
        Sets the linker options. A None value is a no-op and does not overwrite the
        existing options.

        Args:
            value: The linker options to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.options = value
        return self

    def getVendor(self) -> Optional[String]:
        """
        Gets the vendor of the linker.

        Returns:
            String: The linker vendor
        """
        return self.vendor

    def setVendor(self, value: Optional[String]) -> "Linker":
        """
        Sets the vendor of the linker. A None value is a no-op and does not overwrite the
        existing vendor.

        Args:
            value: The linker vendor to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.vendor = value
        return self

    def getVersion(self) -> Optional[String]:
        """
        Gets the exact version of the linker executable.

        Returns:
            String: The linker version
        """
        return self.version

    def setVersion(self, value: Optional[String]) -> "Linker":
        """
        Sets the exact version of the linker executable. A None value is a no-op and does
        not overwrite the existing version.

        Args:
            value: The linker version to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.version = value
        return self


class Implementation(ARElement, ABC):
    """
    Abstract base class for implementations in AUTOSAR models.
    Description of an implementation of a single software component or module.
    """

    # Implementation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.1, p.619
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getBuildActionManifestRef    [x] impl  [x] docstring  [x] test
    # [x] setBuildActionManifestRef    [x] impl  [x] docstring  [x] test
    # [x] getCodeDescriptors           [x] impl  [x] docstring  [x] test
    # [x] createCodeDescriptor         [x] impl  [x] docstring  [x] test
    # [x] getCompilers                 [x] impl  [x] docstring  [x] test
    # [x] createCompiler               [x] impl  [x] docstring  [x] test
    # [x] getGeneratedArtifacts        [x] impl  [x] docstring  [x] test
    # [x] createGeneratedArtifact      [x] impl  [x] docstring  [x] test
    # [x] getHwElementRefs             [x] impl  [x] docstring  [x] test
    # [x] addHwElementRef              [x] impl  [x] docstring  [x] test
    # [x] getLinkers                   [x] impl  [x] docstring  [x] test
    # [x] createLinker                 [x] impl  [x] docstring  [x] test
    # [x] getMcSupport                 [x] impl  [x] docstring  [x] test
    # [x] setMcSupport                 [x] impl  [x] docstring  [x] test
    # [x] getProgrammingLanguage       [x] impl  [x] docstring  [x] test
    # [x] setProgrammingLanguage       [x] impl  [x] docstring  [x] test
    # [x] getRequiredArtifacts         [x] impl  [x] docstring  [x] test
    # [x] createRequiredArtifact       [x] impl  [x] docstring  [x] test
    # [x] getRequiredGeneratorTools    [x] impl  [x] docstring  [x] test
    # [x] createRequiredGeneratorTool  [x] impl  [x] docstring  [x] test
    # [x] getResourceConsumption       [x] impl  [x] docstring  [x] test
    # [x] createResourceConsumption    [x] impl  [x] docstring  [x] test
    # [x] getSwcBswMappingRef          [x] impl  [x] docstring  [x] test
    # [x] setSwcBswMappingRef          [x] impl  [x] docstring  [x] test
    # [x] getSwVersion                 [x] impl  [x] docstring  [x] test
    # [x] setSwVersion                 [x] impl  [x] docstring  [x] test
    # [x] getUsedCodeGenerator         [x] impl  [x] docstring  [x] test
    # [x] setUsedCodeGenerator         [x] impl  [x] docstring  [x] test
    # [x] getVendorId                  [x] impl  [x] docstring  [x] test
    # [x] setVendorId                  [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the Implementation with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this implementation
            short_name: The unique short name of this implementation
        """
        if type(self) is Implementation:
            raise TypeError("Implementation is an abstract class.")

        super().__init__(parent, short_name)

        # A manifest specifying the intended build actions for the software delivered with
        # this implementation.
        self.buildActionManifestRef: Optional[RefType] = None

        # Specifies the provided implementation code. [constr_1968]
        self.codeDescriptors: List[Code] = []

        # Specifies the compiler for which this implementation has been released.
        self.compilers: List[Compiler] = []

        # Relates to an artifact that will be generated during the integration of this
        # Implementation by an associated generator tool.
        self.generatedArtifacts: List[DependencyOnArtifact] = []

        # The hardware elements (e.g. the processor) required for this implementation.
        self.hwElementRefs: List[RefType] = []

        # Specifies the linker for which this implementation has been released.
        self.linkers: List[Linker] = []

        # The measurement & calibration support data belonging to this implementation.
        self.mcSupport: Optional[McSupportData] = None

        # Programming language the implementation was created in.
        self.programmingLanguage: Optional[ProgramminglanguageEnum] = None

        # Specifies that this Implementation depends on the existence of another artifact
        # (e.g. a library).
        self.requiredArtifacts: List[DependencyOnArtifact] = []

        # Relates this Implementation to a generator tool in order to generate additional
        # artifacts during integration.
        self.requiredGeneratorTools: List[DependencyOnArtifact] = []

        # All static and dynamic resources for each implementation are described within the
        # ResourceConsumption class.
        self.resourceConsumption: Optional[ResourceConsumption] = None

        # Allows a mapping between an SWC and a BSW behavior to be attached to an
        # implementation description.
        self.swcBswMappingRef: Optional[RefType] = None

        # Software version of this implementation. The numbering contains three levels
        # (like major, minor, patch), its values are vendor specific. [constr_1966]
        self.swVersion: Optional[RevisionLabelString] = None

        # Optional: code generator used.
        self.usedCodeGenerator: Optional[String] = None

        # Vendor ID of this Implementation according to the AUTOSAR vendor list. [constr_1967]
        self.vendorId: Optional[PositiveInteger] = None

    def getBuildActionManifestRef(self) -> Optional[RefType]:
        """
        Gets the reference to the manifest specifying the intended build actions for the
        software delivered with this implementation.

        Returns:
            RefType: The build action manifest reference
        """
        return self.buildActionManifestRef

    def setBuildActionManifestRef(self, value: Optional[RefType]) -> "Implementation":
        """
        Sets the reference to the manifest specifying the intended build actions for the
        software delivered with this implementation. A None value is a no-op and does not
        overwrite an existing reference.

        Args:
            value: The build action manifest reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.buildActionManifestRef = value
        return self

    def getCodeDescriptors(self) -> List[Code]:
        """
        Gets all code descriptors from the elements list in this implementation.

        Returns:
            List of Code instances in this implementation
        """
        return list(filter(lambda a: isinstance(a, Code), self.elements))

    def createCodeDescriptor(self, short_name: str) -> Code:
        """
        Creates and adds a Code descriptor to this implementation.

        Args:
            short_name: The short name for the new code descriptor

        Returns:
            The created Code instance
        """
        if short_name not in self.elements:
            code_descriptor = Code(self, short_name)
            self.addElement(code_descriptor)
            self.codeDescriptors.append(code_descriptor)
        return self.getElement(short_name)

    def getCompilers(self) -> List[Compiler]:
        """
        Gets the list of compilers for which this implementation has been released.

        Returns:
            List of Compiler instances
        """
        return self.compilers

    def createCompiler(self, short_name: str) -> Compiler:
        """
        Creates and adds a Compiler to this implementation.

        Args:
            short_name: The short name for the new compiler

        Returns:
            The created Compiler instance
        """
        if short_name not in self.elements:
            compiler = Compiler(self, short_name)
            self.addElement(compiler)
            self.compilers.append(compiler)
        return self.getElement(short_name)

    def getGeneratedArtifacts(self) -> List[DependencyOnArtifact]:
        """
        Gets the list of artifacts that will be generated during the integration of this
        Implementation by an associated generator tool.

        Returns:
            List of DependencyOnArtifact instances
        """
        return self.generatedArtifacts

    def createGeneratedArtifact(self, short_name: str) -> DependencyOnArtifact:
        """
        Creates and adds a generated artifact to this implementation.

        Args:
            short_name: The short name for the new generated artifact

        Returns:
            The created DependencyOnArtifact instance
        """
        if short_name not in self.elements:
            artifact = DependencyOnArtifact(self, short_name)
            self.addElement(artifact)
            self.generatedArtifacts.append(artifact)
        return self.getElement(short_name)

    def getHwElementRefs(self) -> List[RefType]:
        """
        Gets the list of references to the hardware elements (e.g. the processor) required
        for this implementation.

        Returns:
            List of RefType instances
        """
        return self.hwElementRefs

    def addHwElementRef(self, value: Optional[RefType]) -> "Implementation":
        """
        Adds a reference to a hardware element (e.g. the processor) required for this
        implementation. A None value is a no-op and is not appended.

        Args:
            value: The hardware element reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwElementRefs.append(value)
        return self

    def getLinkers(self) -> List[Linker]:
        """
        Gets the list of linkers for which this implementation has been released.

        Returns:
            List of Linker instances
        """
        return self.linkers

    def createLinker(self, short_name: str) -> Linker:
        """
        Creates and adds a Linker to this implementation.

        Args:
            short_name: The short name for the new linker

        Returns:
            The created Linker instance
        """
        if short_name not in self.elements:
            linker = Linker(self, short_name)
            self.addElement(linker)
            self.linkers.append(linker)
        return self.getElement(short_name)

    def getMcSupport(self) -> Optional[McSupportData]:
        """
        Gets the measurement & calibration support data belonging to this implementation.

        Returns:
            McSupportData: The microcontroller support information
        """
        return self.mcSupport

    def setMcSupport(self, value: Optional[McSupportData]) -> "Implementation":
        """
        Sets the measurement & calibration support data belonging to this implementation.
        A None value is a no-op and does not overwrite the existing value.

        Args:
            value: The measurement & calibration support data to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcSupport = value
        return self

    def getProgrammingLanguage(self) -> Optional[ProgramminglanguageEnum]:
        """
        Gets the programming language in which the implementation was created in.

        Returns:
            ProgramminglanguageEnum: The programming language
        """
        return self.programmingLanguage

    def setProgrammingLanguage(self, value: Optional[ProgramminglanguageEnum]) -> "Implementation":
        """
        Sets the programming language in which the implementation was created in.
        A None value is a no-op and does not overwrite the existing value.

        Args:
            value: The programming language to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.programmingLanguage = value
        return self

    def getRequiredArtifacts(self) -> List[DependencyOnArtifact]:
        """
        Gets the list of artifacts this implementation depends on (e.g. a library).

        Returns:
            List of DependencyOnArtifact instances
        """
        return self.requiredArtifacts

    def createRequiredArtifact(self, short_name: str) -> DependencyOnArtifact:
        """
        Creates and adds a required artifact to this implementation.

        Args:
            short_name: The short name for the new required artifact

        Returns:
            The created DependencyOnArtifact instance
        """
        if short_name not in self.elements:
            artifact = DependencyOnArtifact(self, short_name)
            self.addElement(artifact)
            self.requiredArtifacts.append(artifact)
        return self.getElement(short_name)

    def getRequiredGeneratorTools(self) -> List[DependencyOnArtifact]:
        """
        Gets the list of generator tools that generate additional artifacts during
        integration of this implementation.

        Returns:
            List of DependencyOnArtifact instances
        """
        return self.requiredGeneratorTools

    def createRequiredGeneratorTool(self, short_name: str) -> DependencyOnArtifact:
        """
        Creates and adds a required generator tool to this implementation.

        Args:
            short_name: The short name for the new required generator tool

        Returns:
            The created DependencyOnArtifact instance
        """
        if short_name not in self.elements:
            tool = DependencyOnArtifact(self, short_name)
            self.addElement(tool)
            self.requiredGeneratorTools.append(tool)
        return self.getElement(short_name)

    def getResourceConsumption(self) -> Optional[ResourceConsumption]:
        """
        Gets all static and dynamic resources for each implementation as described within
        the ResourceConsumption class.

        Returns:
            ResourceConsumption: The resource consumption information
        """
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

        if short_name not in self.elements:
            consumption = ResourceConsumption(self, short_name)
            self.addElement(consumption)
            self.resourceConsumption = consumption
        return self.getElement(short_name)

    def getSwcBswMappingRef(self) -> Optional[RefType]:
        """
        Gets the reference to the mapping between an SWC and a BSW behavior attached to an
        implementation description.

        Returns:
            RefType: The SWC/BSW mapping reference
        """
        return self.swcBswMappingRef

    def setSwcBswMappingRef(self, value: Optional[RefType]) -> "Implementation":
        """
        Sets the reference to the mapping between an SWC and a BSW behavior. A None value
        is a no-op and does not overwrite the existing reference.

        Args:
            value: The SWC/BSW mapping reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swcBswMappingRef = value
        return self

    def getSwVersion(self) -> Optional[RevisionLabelString]:
        """
        Gets the software version of this implementation. The numbering contains three
        levels (like major, minor, patch), its values are vendor specific. [constr_1966]

        Returns:
            RevisionLabelString: The software version information
        """
        return self.swVersion

    def setSwVersion(self, value: Optional[RevisionLabelString]) -> "Implementation":
        """
        Sets the software version of this implementation. The numbering contains three
        levels (like major, minor, patch), its values are vendor specific.
        A None value is a no-op and does not overwrite the existing version. [constr_1966]

        Args:
            value: The software version to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swVersion = value
        return self

    def getUsedCodeGenerator(self) -> Optional[String]:
        """
        Gets the optional code generator used for this implementation.

        Returns:
            String: The used code generator
        """
        return self.usedCodeGenerator

    def setUsedCodeGenerator(self, value: Optional[String]) -> "Implementation":
        """
        Sets the optional code generator used for this implementation. A None value is a
        no-op and does not overwrite the existing value.

        Args:
            value: The used code generator to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usedCodeGenerator = value
        return self

    def getVendorId(self) -> Optional[PositiveInteger]:
        """
        Gets the vendor ID of this Implementation according to the AUTOSAR vendor list.
        [constr_1967]

        Returns:
            PositiveInteger: The vendor ID
        """
        return self.vendorId

    def setVendorId(self, value: Optional[PositiveInteger]) -> "Implementation":
        """
        Sets the vendor ID of this Implementation according to the AUTOSAR vendor list.
        A None value is a no-op and does not overwrite the existing vendor ID. [constr_1967]

        Args:
            value: The vendor ID to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.vendorId = value
        return self
