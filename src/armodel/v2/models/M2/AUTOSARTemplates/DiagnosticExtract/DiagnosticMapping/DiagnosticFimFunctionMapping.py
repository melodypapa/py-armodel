from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticFimFunctionMapping(DiagnosticSwMapping):
    """
    This meta-class represents the ability to define a mapping between a
    function identifier (FID) and the corresponding SwcServiceDependency in the
    application software resp. basic software.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping::DiagnosticFimFunctionMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 264, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is supposed to represent a reference to a Bsw ServiceDependency.
        # the latter is not derived from and therefore this detour needs to be still
                # let BswServiceDependency become of a reference.
        self._mappedBsw: Optional["BswService"] = None

    @property
    def mapped_bsw(self) -> Optional["BswService"]:
        """Get mappedBsw (Pythonic accessor)."""
        return self._mappedBsw

    @mapped_bsw.setter
    def mapped_bsw(self, value: Optional["BswService"]) -> None:
        """
        Set mappedBsw with validation.
        
        Args:
            value: The mappedBsw to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedBsw = None
            return

        if not isinstance(value, BswService):
            raise TypeError(
                f"mappedBsw must be BswService or None, got {type(value).__name__}"
            )
        self._mappedBsw = value
        # This represents the ability to refer to an AtomicSw ComponentType that is
        # available without the definition of it will be embedded into the component
        # hierarchy.
        self._mappedFlatSwc: Optional["SwcService"] = None

    @property
    def mapped_flat_swc(self) -> Optional["SwcService"]:
        """Get mappedFlatSwc (Pythonic accessor)."""
        return self._mappedFlatSwc

    @mapped_flat_swc.setter
    def mapped_flat_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set mappedFlatSwc with validation.
        
        Args:
            value: The mappedFlatSwc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedFlatSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"mappedFlatSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._mappedFlatSwc = value
        # This represents the mapped FID.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._mapped: Optional["DiagnosticFunction"] = None

    @property
    def mapped(self) -> Optional["DiagnosticFunction"]:
        """Get mapped (Pythonic accessor)."""
        return self._mapped

    @mapped.setter
    def mapped(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set mapped with validation.
        
        Args:
            value: The mapped to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mapped = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"mapped must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._mapped = value
        # hierarchy (under possible consideration of the root by: SwcServiceDependency.
        self._mappedSwc: Optional["SwcService"] = None

    @property
    def mapped_swc(self) -> Optional["SwcService"]:
        """Get mappedSwc (Pythonic accessor)."""
        return self._mappedSwc

    @mapped_swc.setter
    def mapped_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set mappedSwc with validation.
        
        Args:
            value: The mappedSwc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"mappedSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._mappedSwc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMappedBsw(self) -> "BswService":
        """
        AUTOSAR-compliant getter for mappedBsw.
        
        Returns:
            The mappedBsw value
        
        Note:
            Delegates to mapped_bsw property (CODING_RULE_V2_00017)
        """
        return self.mapped_bsw  # Delegates to property

    def setMappedBsw(self, value: "BswService") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mappedBsw with method chaining.
        
        Args:
            value: The mappedBsw to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mapped_bsw property setter (gets validation automatically)
        """
        self.mapped_bsw = value  # Delegates to property setter
        return self

    def getMappedFlatSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for mappedFlatSwc.
        
        Returns:
            The mappedFlatSwc value
        
        Note:
            Delegates to mapped_flat_swc property (CODING_RULE_V2_00017)
        """
        return self.mapped_flat_swc  # Delegates to property

    def setMappedFlatSwc(self, value: "SwcService") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mappedFlatSwc with method chaining.
        
        Args:
            value: The mappedFlatSwc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mapped_flat_swc property setter (gets validation automatically)
        """
        self.mapped_flat_swc = value  # Delegates to property setter
        return self

    def getMapped(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for mapped.
        
        Returns:
            The mapped value
        
        Note:
            Delegates to mapped property (CODING_RULE_V2_00017)
        """
        return self.mapped  # Delegates to property

    def setMapped(self, value: "DiagnosticFunction") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mapped with method chaining.
        
        Args:
            value: The mapped to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mapped property setter (gets validation automatically)
        """
        self.mapped = value  # Delegates to property setter
        return self

    def getMappedSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for mappedSwc.
        
        Returns:
            The mappedSwc value
        
        Note:
            Delegates to mapped_swc property (CODING_RULE_V2_00017)
        """
        return self.mapped_swc  # Delegates to property

    def setMappedSwc(self, value: "SwcService") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mappedSwc with method chaining.
        
        Args:
            value: The mappedSwc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mapped_swc property setter (gets validation automatically)
        """
        self.mapped_swc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapped_bsw(self, value: Optional["BswService"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mappedBsw and return self for chaining.
        
        Args:
            value: The mappedBsw to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mapped_bsw("value")
        """
        self.mapped_bsw = value  # Use property setter (gets validation)
        return self

    def with_mapped_flat_swc(self, value: Optional["SwcService"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mappedFlatSwc and return self for chaining.
        
        Args:
            value: The mappedFlatSwc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mapped_flat_swc("value")
        """
        self.mapped_flat_swc = value  # Use property setter (gets validation)
        return self

    def with_mapped(self, value: Optional["DiagnosticFunction"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mapped and return self for chaining.
        
        Args:
            value: The mapped to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mapped("value")
        """
        self.mapped = value  # Use property setter (gets validation)
        return self

    def with_mapped_swc(self, value: Optional["SwcService"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mappedSwc and return self for chaining.
        
        Args:
            value: The mappedSwc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mapped_swc("value")
        """
        self.mapped_swc = value  # Use property setter (gets validation)
        return self