from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARElement import ARElement
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class Implementation(ARElement, ABC):
    """
    Description of an implementation a single software component or module.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Implementation::Implementation
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 126, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 619, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2029, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 449, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is Implementation:
            raise TypeError("Implementation is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A manifest specifying the intended build actions for the delivered with this
                # implementation.
        # atpVariation.
        self._buildAction: Optional["BuildActionManifest"] = None

    @property
    def build_action(self) -> Optional["BuildActionManifest"]:
        """Get buildAction (Pythonic accessor)."""
        return self._buildAction

    @build_action.setter
    def build_action(self, value: Optional["BuildActionManifest"]) -> None:
        """
        Set buildAction with validation.
        
        Args:
            value: The buildAction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._buildAction = None
            return

        if not isinstance(value, BuildActionManifest):
            raise TypeError(
                f"buildAction must be BuildActionManifest or None, got {type(value).__name__}"
            )
        self._buildAction = value
        # Specifies the provided implementation code.
        self._codeDescriptor: List["Code"] = []

    @property
    def code_descriptor(self) -> List["Code"]:
        """Get codeDescriptor (Pythonic accessor)."""
        return self._codeDescriptor
        # Specifies the compiler for which this implementation has 381 Document ID 89:
        # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._compiler: List["Compiler"] = []

    @property
    def compiler(self) -> List["Compiler"]:
        """Get compiler (Pythonic accessor)."""
        return self._compiler
        # Relates to an artifact that will be generated during the of this
                # Implementation by an associated Note that this is an optional information
                # might not always be in the scope of a single component to provide this
                # information.
        # atpVariation.
        self._generated: List[RefType] = []

    @property
    def generated(self) -> List[RefType]:
        """Get generated (Pythonic accessor)."""
        return self._generated
        # The hardware elements (e.
        # g.
        # the processor) required for.
        self._hwElement: List["HwElement"] = []

    @property
    def hw_element(self) -> List["HwElement"]:
        """Get hwElement (Pythonic accessor)."""
        return self._hwElement
        # Specifies the linker for which this implementation has.
        self._linker: List["Linker"] = []

    @property
    def linker(self) -> List["Linker"]:
        """Get linker (Pythonic accessor)."""
        return self._linker
        # The measurement & calibration support data belonging to The aggregtion is
        # <<atpSplitable>> case of an already exisiting BSW this description will be
        # added later process, namely at code generation time.
        self._mcSupport: Optional["McSupportData"] = None

    @property
    def mc_support(self) -> Optional["McSupportData"]:
        """Get mcSupport (Pythonic accessor)."""
        return self._mcSupport

    @mc_support.setter
    def mc_support(self, value: Optional["McSupportData"]) -> None:
        """
        Set mcSupport with validation.
        
        Args:
            value: The mcSupport to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mcSupport = None
            return

        if not isinstance(value, McSupportData):
            raise TypeError(
                f"mcSupport must be McSupportData or None, got {type(value).__name__}"
            )
        self._mcSupport = value
        # Programming language the implementation was created in.
        self._programming: Optional["Programminglanguage"] = None

    @property
    def programming(self) -> Optional["Programminglanguage"]:
        """Get programming (Pythonic accessor)."""
        return self._programming

    @programming.setter
    def programming(self, value: Optional["Programminglanguage"]) -> None:
        """
        Set programming with validation.
        
        Args:
            value: The programming to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._programming = None
            return

        if not isinstance(value, Programminglanguage):
            raise TypeError(
                f"programming must be Programminglanguage or None, got {type(value).__name__}"
            )
        self._programming = value
        # Specifies that this Implementation depends on the another artifact (e.
        # g.
        # a library).
        # This DependencyOnArtifact is subject to the purpose to support variability in
                # the algorithms in the cause different dependencies, e.
        # g.
        # of used libraries.
        # atpVariation.
        self._requiredArtifact: List[RefType] = []

    @property
    def required_artifact(self) -> List[RefType]:
        """Get requiredArtifact (Pythonic accessor)."""
        return self._requiredArtifact
        # Relates this Implementation to a generator tool in order to additional
                # artifacts during integration.
        # atpVariation.
        self._required: List[RefType] = []

    @property
    def required(self) -> List[RefType]:
        """Get required (Pythonic accessor)."""
        return self._required
        # All static and dynamic resources for each implementation described within the
        # ResourceConsumption class.
        self._resource: Optional["ResourceConsumption"] = None

    @property
    def resource(self) -> Optional["ResourceConsumption"]:
        """Get resource (Pythonic accessor)."""
        return self._resource

    @resource.setter
    def resource(self, value: Optional["ResourceConsumption"]) -> None:
        """
        Set resource with validation.
        
        Args:
            value: The resource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resource = None
            return

        if not isinstance(value, ResourceConsumption):
            raise TypeError(
                f"resource must be ResourceConsumption or None, got {type(value).__name__}"
            )
        self._resource = value
        # This allows a mapping between an SWC and a BSW to be attached to an
        # implementation description Service, ECU Abstraction and Complex It is up to
        # the methodology to define reference has to be set for the Swc- or Bsw for
        # both.
        self._swcBsw: RefType = None

    @property
    def swc_bsw(self) -> RefType:
        """Get swcBsw (Pythonic accessor)."""
        return self._swcBsw

    @swc_bsw.setter
    def swc_bsw(self, value: RefType) -> None:
        """
        Set swcBsw with validation.
        
        Args:
            value: The swcBsw to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcBsw = None
            return

        self._swcBsw = value
        # Software version of this implementation.
        # The numbering levels (like major, minor, patch), its values specific.
        self._swVersion: Optional["RevisionLabelString"] = None

    @property
    def sw_version(self) -> Optional["RevisionLabelString"]:
        """Get swVersion (Pythonic accessor)."""
        return self._swVersion

    @sw_version.setter
    def sw_version(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set swVersion with validation.
        
        Args:
            value: The swVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swVersion = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"swVersion must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._swVersion = value
        # Optional: code generator used.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._usedCodeGenerator: Optional["String"] = None

    @property
    def used_code_generator(self) -> Optional["String"]:
        """Get usedCodeGenerator (Pythonic accessor)."""
        return self._usedCodeGenerator

    @used_code_generator.setter
    def used_code_generator(self, value: Optional["String"]) -> None:
        """
        Set usedCodeGenerator with validation.
        
        Args:
            value: The usedCodeGenerator to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedCodeGenerator = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"usedCodeGenerator must be String or None, got {type(value).__name__}"
            )
        self._usedCodeGenerator = value
        # Vendor ID of this Implementation according to the list.
        self._vendorId: Optional["PositiveInteger"] = None

    @property
    def vendor_id(self) -> Optional["PositiveInteger"]:
        """Get vendorId (Pythonic accessor)."""
        return self._vendorId

    @vendor_id.setter
    def vendor_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set vendorId with validation.
        
        Args:
            value: The vendorId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vendorId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"vendorId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._vendorId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBuildAction(self) -> "BuildActionManifest":
        """
        AUTOSAR-compliant getter for buildAction.
        
        Returns:
            The buildAction value
        
        Note:
            Delegates to build_action property (CODING_RULE_V2_00017)
        """
        return self.build_action  # Delegates to property

    def setBuildAction(self, value: "BuildActionManifest") -> "Implementation":
        """
        AUTOSAR-compliant setter for buildAction with method chaining.
        
        Args:
            value: The buildAction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to build_action property setter (gets validation automatically)
        """
        self.build_action = value  # Delegates to property setter
        return self

    def getCodeDescriptor(self) -> List["Code"]:
        """
        AUTOSAR-compliant getter for codeDescriptor.
        
        Returns:
            The codeDescriptor value
        
        Note:
            Delegates to code_descriptor property (CODING_RULE_V2_00017)
        """
        return self.code_descriptor  # Delegates to property

    def getCompiler(self) -> List["Compiler"]:
        """
        AUTOSAR-compliant getter for compiler.
        
        Returns:
            The compiler value
        
        Note:
            Delegates to compiler property (CODING_RULE_V2_00017)
        """
        return self.compiler  # Delegates to property

    def getGenerated(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for generated.
        
        Returns:
            The generated value
        
        Note:
            Delegates to generated property (CODING_RULE_V2_00017)
        """
        return self.generated  # Delegates to property

    def getHwElement(self) -> List["HwElement"]:
        """
        AUTOSAR-compliant getter for hwElement.
        
        Returns:
            The hwElement value
        
        Note:
            Delegates to hw_element property (CODING_RULE_V2_00017)
        """
        return self.hw_element  # Delegates to property

    def getLinker(self) -> List["Linker"]:
        """
        AUTOSAR-compliant getter for linker.
        
        Returns:
            The linker value
        
        Note:
            Delegates to linker property (CODING_RULE_V2_00017)
        """
        return self.linker  # Delegates to property

    def getMcSupport(self) -> "McSupportData":
        """
        AUTOSAR-compliant getter for mcSupport.
        
        Returns:
            The mcSupport value
        
        Note:
            Delegates to mc_support property (CODING_RULE_V2_00017)
        """
        return self.mc_support  # Delegates to property

    def setMcSupport(self, value: "McSupportData") -> "Implementation":
        """
        AUTOSAR-compliant setter for mcSupport with method chaining.
        
        Args:
            value: The mcSupport to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mc_support property setter (gets validation automatically)
        """
        self.mc_support = value  # Delegates to property setter
        return self

    def getProgramming(self) -> "Programminglanguage":
        """
        AUTOSAR-compliant getter for programming.
        
        Returns:
            The programming value
        
        Note:
            Delegates to programming property (CODING_RULE_V2_00017)
        """
        return self.programming  # Delegates to property

    def setProgramming(self, value: "Programminglanguage") -> "Implementation":
        """
        AUTOSAR-compliant setter for programming with method chaining.
        
        Args:
            value: The programming to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to programming property setter (gets validation automatically)
        """
        self.programming = value  # Delegates to property setter
        return self

    def getRequiredArtifact(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for requiredArtifact.
        
        Returns:
            The requiredArtifact value
        
        Note:
            Delegates to required_artifact property (CODING_RULE_V2_00017)
        """
        return self.required_artifact  # Delegates to property

    def getRequired(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for required.
        
        Returns:
            The required value
        
        Note:
            Delegates to required property (CODING_RULE_V2_00017)
        """
        return self.required  # Delegates to property

    def getResource(self) -> "ResourceConsumption":
        """
        AUTOSAR-compliant getter for resource.
        
        Returns:
            The resource value
        
        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def setResource(self, value: "ResourceConsumption") -> "Implementation":
        """
        AUTOSAR-compliant setter for resource with method chaining.
        
        Args:
            value: The resource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to resource property setter (gets validation automatically)
        """
        self.resource = value  # Delegates to property setter
        return self

    def getSwcBsw(self) -> RefType:
        """
        AUTOSAR-compliant getter for swcBsw.
        
        Returns:
            The swcBsw value
        
        Note:
            Delegates to swc_bsw property (CODING_RULE_V2_00017)
        """
        return self.swc_bsw  # Delegates to property

    def setSwcBsw(self, value: RefType) -> "Implementation":
        """
        AUTOSAR-compliant setter for swcBsw with method chaining.
        
        Args:
            value: The swcBsw to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to swc_bsw property setter (gets validation automatically)
        """
        self.swc_bsw = value  # Delegates to property setter
        return self

    def getSwVersion(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for swVersion.
        
        Returns:
            The swVersion value
        
        Note:
            Delegates to sw_version property (CODING_RULE_V2_00017)
        """
        return self.sw_version  # Delegates to property

    def setSwVersion(self, value: "RevisionLabelString") -> "Implementation":
        """
        AUTOSAR-compliant setter for swVersion with method chaining.
        
        Args:
            value: The swVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_version property setter (gets validation automatically)
        """
        self.sw_version = value  # Delegates to property setter
        return self

    def getUsedCodeGenerator(self) -> "String":
        """
        AUTOSAR-compliant getter for usedCodeGenerator.
        
        Returns:
            The usedCodeGenerator value
        
        Note:
            Delegates to used_code_generator property (CODING_RULE_V2_00017)
        """
        return self.used_code_generator  # Delegates to property

    def setUsedCodeGenerator(self, value: "String") -> "Implementation":
        """
        AUTOSAR-compliant setter for usedCodeGenerator with method chaining.
        
        Args:
            value: The usedCodeGenerator to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to used_code_generator property setter (gets validation automatically)
        """
        self.used_code_generator = value  # Delegates to property setter
        return self

    def getVendorId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for vendorId.
        
        Returns:
            The vendorId value
        
        Note:
            Delegates to vendor_id property (CODING_RULE_V2_00017)
        """
        return self.vendor_id  # Delegates to property

    def setVendorId(self, value: "PositiveInteger") -> "Implementation":
        """
        AUTOSAR-compliant setter for vendorId with method chaining.
        
        Args:
            value: The vendorId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vendor_id property setter (gets validation automatically)
        """
        self.vendor_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_build_action(self, value: Optional["BuildActionManifest"]) -> "Implementation":
        """
        Set buildAction and return self for chaining.
        
        Args:
            value: The buildAction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_build_action("value")
        """
        self.build_action = value  # Use property setter (gets validation)
        return self

    def with_mc_support(self, value: Optional["McSupportData"]) -> "Implementation":
        """
        Set mcSupport and return self for chaining.
        
        Args:
            value: The mcSupport to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mc_support("value")
        """
        self.mc_support = value  # Use property setter (gets validation)
        return self

    def with_programming(self, value: Optional["Programminglanguage"]) -> "Implementation":
        """
        Set programming and return self for chaining.
        
        Args:
            value: The programming to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_programming("value")
        """
        self.programming = value  # Use property setter (gets validation)
        return self

    def with_resource(self, value: Optional["ResourceConsumption"]) -> "Implementation":
        """
        Set resource and return self for chaining.
        
        Args:
            value: The resource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_resource("value")
        """
        self.resource = value  # Use property setter (gets validation)
        return self

    def with_swc_bsw(self, value: Optional[RefType]) -> "Implementation":
        """
        Set swcBsw and return self for chaining.
        
        Args:
            value: The swcBsw to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_swc_bsw("value")
        """
        self.swc_bsw = value  # Use property setter (gets validation)
        return self

    def with_sw_version(self, value: Optional["RevisionLabelString"]) -> "Implementation":
        """
        Set swVersion and return self for chaining.
        
        Args:
            value: The swVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_version("value")
        """
        self.sw_version = value  # Use property setter (gets validation)
        return self

    def with_used_code_generator(self, value: Optional["String"]) -> "Implementation":
        """
        Set usedCodeGenerator and return self for chaining.
        
        Args:
            value: The usedCodeGenerator to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_used_code_generator("value")
        """
        self.used_code_generator = value  # Use property setter (gets validation)
        return self

    def with_vendor_id(self, value: Optional["PositiveInteger"]) -> "Implementation":
        """
        Set vendorId and return self for chaining.
        
        Args:
            value: The vendorId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vendor_id("value")
        """
        self.vendor_id = value  # Use property setter (gets validation)
        return self