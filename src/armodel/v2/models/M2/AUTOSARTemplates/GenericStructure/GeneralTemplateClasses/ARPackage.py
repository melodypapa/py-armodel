"""
AUTOSAR Package - ARPackage

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    CollectableElement,
)


# Manually maintained: ARPackage needs multiple inheritance support
# This class is manually maintained to add shortName support for test compatibility
# Marked with base class marker to prevent regeneration
class ARPackage_ManuallyMaintained:  # Marker class to prevent regeneration
    pass


class ARPackage(CollectableElement):
    """
    AUTOSAR package, allowing to create top level packages to structure the
    contained ARElements. ARPackages are open sets. This means that in a file
    based description system multiple files can be used to partially describe
    the contents of a package. This is an extended version of MSR’s SW-SYSTEM.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage::ARPackage
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 300, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 297, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 286, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 58, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 967, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1992, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 203, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 53, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 55, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 156, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()
        # Manually add shortName attribute for test compatibility
        # ARPackage should inherit from Identifiable but current generator doesn't support multiple inheritance
        self._shortName: Optional[str] = None
        
        # Parent attribute for V1 compatibility
        self.parent: Optional["ARObject"] = None
        
        # Initialize list attributes (these are generated outside __init__ by code generator, which is a bug)
        self._arPackage: List["ARPackage"] = []
        self._element: List["PackageableElement"] = []
        self._referenceBase: List["RefType"] = []

    # ===== Manually added methods for Identifiable compatibility =====
    @property
    def shortName(self) -> Optional[str]:
        """Get shortName (Pythonic accessor)."""
        return self._shortName

    @shortName.setter
    def shortName(self, value: Optional[str]) -> None:
        """Set shortName with validation."""
        self._shortName = value

    def getShortName(self) -> Optional[str]:
        """
        AUTOSAR-compliant getter for shortName.
        
        Returns:
            The shortName value
        """
        return self.shortName

    def setShortName(self, value: Optional[str]) -> "ARPackage":
        """
        AUTOSAR-compliant setter for shortName with method chaining.
        
        Args:
            value: The shortName to set
        
        Returns:
            self for method chaining
        """
        self.shortName = value
        return self

    # ===== V1-compatible property alias =====
    @property
    def ar_packages(self) -> List["ARPackage"]:
        """Alias for ar_package (V1 compatibility)."""
        return self.ar_package

    def getTagName(self) -> str:
        """
        Get the XML tag name for this element.
        
        Returns:
            The tag name "ARPackage"
        """
        return "ARPackage"

    # ===== V1-compatible collection methods =====
    def getARPackages(self) -> List["ARPackage"]:
        """
        Get all child ARPackages (V1-compatible method).
        
        Returns:
            List of child ARPackages
        """
        return self.ar_package

    def addARPackage(self, pkg: "ARPackage") -> None:
        """
        Add a child ARPackage (V1-compatible method).
        
        Args:
            pkg: The ARPackage to add
        """
        self.ar_package.append(pkg)
        # Set parent relationship
        if hasattr(pkg, 'parent'):
            pkg.parent = self

    # ===== Rest of the generated code =====

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a sub package within an ARPackage, for an unlimited package
                # hierarchy.
        # atpVariation.
        self._arPackage: List["ARPackage"] = []

    @property
    def ar_package(self) -> List["ARPackage"]:
        """Get arPackage (Pythonic accessor)."""
        return self._arPackage
        # Elements that are part of this package atpVariation.
        self._element: List["PackageableElement"] = []

    @property
    def element(self) -> List["PackageableElement"]:
        """Get element (Pythonic accessor)."""
        return self._element
        # This denotes the reference bases for the package.
        # This is for all relative references within the package.
        # needs to be selected according to the base the references.
        self._referenceBase: List["RefType"] = []

    @property
    def reference_base(self) -> List["RefType"]:
        """Get referenceBase (Pythonic accessor)."""
        return self._referenceBase

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArPackage(self) -> List["ARPackage"]:
        """
        AUTOSAR-compliant getter for arPackage.
        
        Returns:
            The arPackage value
        
        Note:
            Delegates to ar_package property (CODING_RULE_V2_00017)
        """
        return self.ar_package  # Delegates to property

    def getElement(self) -> List["PackageableElement"]:
        """
        AUTOSAR-compliant getter for element.
        
        Returns:
            The element value
        
        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def getReferenceBase(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for referenceBase.
        
        Returns:
            The referenceBase value
        
        Note:
            Delegates to reference_base property (CODING_RULE_V2_00017)
        """
        return self.reference_base  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class PackageableElement(CollectableElement, ABC):
    """
    This meta-class specifies the ability to be a member of an AUTOSAR package.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage::PackageableElement
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 302, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2042, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 54, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PackageableElement:
            raise TypeError("PackageableElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ReferenceBase(ARObject):
    """
    This meta-class establishes a basis for relative references. Reference bases
    are identified by the short Label which shall be unique in the current
    package.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage::ReferenceBase
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 72, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a meta-class for which the global is supported via
        # this reference base.
        self._globalElement: List["RefType"] = []

    @property
    def global_element(self) -> List["RefType"]:
        """Get globalElement (Pythonic accessor)."""
        return self._globalElement
        # This represents the ability to express that global elements in various
        # packages which do not have a common Packages mentioned by Reference used in
        # addition to the one in.
        self._globalIn: List["ARPackage"] = []

    @property
    def global_in(self) -> List["ARPackage"]:
        """Get globalIn (Pythonic accessor)."""
        return self._globalIn
        # This attribute denotes if the current ReferenceBase is the that there can
        # only be one default reference a package.
        self._isDefault: "Boolean" = None

    @property
    def is_default(self) -> "Boolean":
        """Get isDefault (Pythonic accessor)."""
        return self._isDefault

    @is_default.setter
    def is_default(self, value: "Boolean") -> None:
        """
        Set isDefault with validation.
        
        Args:
            value: The isDefault to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Boolean):
            raise TypeError(
                f"isDefault must be Boolean, got {type(value).__name__}"
            )
        self._isDefault = value
        # This association specifies the basis of all relative the base equals
        # shortLabel.
        self._package: Optional["ARPackage"] = None

    @property
    def package(self) -> Optional["ARPackage"]:
        """Get package (Pythonic accessor)."""
        return self._package

    @package.setter
    def package(self, value: Optional["ARPackage"]) -> None:
        """
        Set package with validation.
        
        Args:
            value: The package to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._package = None
            return

        if not isinstance(value, ARPackage):
            raise TypeError(
                f"package must be ARPackage or None, got {type(value).__name__}"
            )
        self._package = value
        # This is the name of the reference base.
        # By this name, can denote the applicable base.
        self._shortLabel: "Identifier" = None

    @property
    def short_label(self) -> "Identifier":
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: "Identifier") -> None:
        """
        Set shortLabel with validation.
        
        Args:
            value: The shortLabel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGlobalElement(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for globalElement.
        
        Returns:
            The globalElement value
        
        Note:
            Delegates to global_element property (CODING_RULE_V2_00017)
        """
        return self.global_element  # Delegates to property

    def getGlobalIn(self) -> List["ARPackage"]:
        """
        AUTOSAR-compliant getter for globalIn.
        
        Returns:
            The globalIn value
        
        Note:
            Delegates to global_in property (CODING_RULE_V2_00017)
        """
        return self.global_in  # Delegates to property

    def getIsDefault(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isDefault.
        
        Returns:
            The isDefault value
        
        Note:
            Delegates to is_default property (CODING_RULE_V2_00017)
        """
        return self.is_default  # Delegates to property

    def setIsDefault(self, value: "Boolean") -> "ReferenceBase":
        """
        AUTOSAR-compliant setter for isDefault with method chaining.
        
        Args:
            value: The isDefault to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to is_default property setter (gets validation automatically)
        """
        self.is_default = value  # Delegates to property setter
        return self

    def getPackage(self) -> "ARPackage":
        """
        AUTOSAR-compliant getter for package.
        
        Returns:
            The package value
        
        Note:
            Delegates to package property (CODING_RULE_V2_00017)
        """
        return self.package  # Delegates to property

    def setPackage(self, value: "ARPackage") -> "ReferenceBase":
        """
        AUTOSAR-compliant setter for package with method chaining.
        
        Args:
            value: The package to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to package property setter (gets validation automatically)
        """
        self.package = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.
        
        Returns:
            The shortLabel value
        
        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "ReferenceBase":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_default(self, value: "Boolean") -> "ReferenceBase":
        """
        Set isDefault and return self for chaining.
        
        Args:
            value: The isDefault to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_is_default("value")
        """
        self.is_default = value  # Use property setter (gets validation)
        return self

    def with_package(self, value: Optional["ARPackage"]) -> "ReferenceBase":
        """
        Set package and return self for chaining.
        
        Args:
            value: The package to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_package("value")
        """
        self.package = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: "Identifier") -> "ReferenceBase":
        """
        Set shortLabel and return self for chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self



class ARElement(PackageableElement, ABC):
    """
    An element that can be defined stand-alone, i.e. without being part of
    another element (except for packages of course).
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage::ARElement
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 300, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 297, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 286, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 58, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 967, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1992, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 71, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 54, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 55, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 156, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is ARElement:
            raise TypeError("ARElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====