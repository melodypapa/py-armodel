from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DependencyOnArtifact(Identifiable):
    """
    Dependency on the existence of another artifact, e.g. a library.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Implementation::DependencyOnArtifact
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 131, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 412, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The specified artifact needs to exist.
        self._artifact: Optional["AutosarEngineering"] = None

    @property
    def artifact(self) -> Optional["AutosarEngineering"]:
        """Get artifact (Pythonic accessor)."""
        return self._artifact

    @artifact.setter
    def artifact(self, value: Optional["AutosarEngineering"]) -> None:
        """
        Set artifact with validation.
        
        Args:
            value: The artifact to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._artifact = None
            return

        if not isinstance(value, AutosarEngineering):
            raise TypeError(
                f"artifact must be AutosarEngineering or None, got {type(value).__name__}"
            )
        self._artifact = value
        # Specification for which process step(s) this dependency is.
        self._usage: List[RefType] = []

    @property
    def usage(self) -> List[RefType]:
        """Get usage (Pythonic accessor)."""
        return self._usage

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArtifact(self) -> "AutosarEngineering":
        """
        AUTOSAR-compliant getter for artifact.
        
        Returns:
            The artifact value
        
        Note:
            Delegates to artifact property (CODING_RULE_V2_00017)
        """
        return self.artifact  # Delegates to property

    def setArtifact(self, value: "AutosarEngineering") -> "DependencyOnArtifact":
        """
        AUTOSAR-compliant setter for artifact with method chaining.
        
        Args:
            value: The artifact to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to artifact property setter (gets validation automatically)
        """
        self.artifact = value  # Delegates to property setter
        return self

    def getUsage(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for usage.
        
        Returns:
            The usage value
        
        Note:
            Delegates to usage property (CODING_RULE_V2_00017)
        """
        return self.usage  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_artifact(self, value: Optional["AutosarEngineering"]) -> "DependencyOnArtifact":
        """
        Set artifact and return self for chaining.
        
        Args:
            value: The artifact to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_artifact("value")
        """
        self.artifact = value  # Use property setter (gets validation)
        return self