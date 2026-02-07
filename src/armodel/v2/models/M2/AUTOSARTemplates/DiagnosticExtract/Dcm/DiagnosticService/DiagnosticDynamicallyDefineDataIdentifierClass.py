from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the
    "Dynamically Define Data Identifier" diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineDataIdentifier::DiagnosticDynamicallyDefineDataIdentifierClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 128, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If set to TRUE, the Dcm module shall check the session, and mode dependencies
                # per source DIDs with a with DID in the range 0x 0xF3FF.
        # to FALSE.
        # the Dcm module shall not check the and mode dependencies per source a
                # ReadDataByIdentifier (0x22) with DID in the to 0xF3FF.
        self._checkPer: Optional["Boolean"] = None

    @property
    def check_per(self) -> Optional["Boolean"]:
        """Get checkPer (Pythonic accessor)."""
        return self._checkPer

    @check_per.setter
    def check_per(self, value: Optional["Boolean"]) -> None:
        """
        Set checkPer with validation.
        
        Args:
            value: The checkPer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._checkPer = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"checkPer must be Boolean or None, got {type(value).__name__}"
            )
        self._checkPer = value
        # This configuration switch defines whether DDDID definition is handled as
        # non-volatile information or not.
        self._configuration: Optional["DiagnosticHandleDDDI"] = None

    @property
    def configuration(self) -> Optional["DiagnosticHandleDDDI"]:
        """Get configuration (Pythonic accessor)."""
        return self._configuration

    @configuration.setter
    def configuration(self, value: Optional["DiagnosticHandleDDDI"]) -> None:
        """
        Set configuration with validation.
        
        Args:
            value: The configuration to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configuration = None
            return

        if not isinstance(value, DiagnosticHandleDDDI):
            raise TypeError(
                f"configuration must be DiagnosticHandleDDDI or None, got {type(value).__name__}"
            )
        self._configuration = value
        # This attribute contains a list of applicable subfunctions for
        # DiagnosticDynamicallyDefineDataIdentifier that the
        # DiagnosticDynamicallyDefineDataIdentifier.
        self._subfunction: List["DiagnosticDynamically"] = []

    @property
    def subfunction(self) -> List["DiagnosticDynamically"]:
        """Get subfunction (Pythonic accessor)."""
        return self._subfunction

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCheckPer(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for checkPer.
        
        Returns:
            The checkPer value
        
        Note:
            Delegates to check_per property (CODING_RULE_V2_00017)
        """
        return self.check_per  # Delegates to property

    def setCheckPer(self, value: "Boolean") -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """
        AUTOSAR-compliant setter for checkPer with method chaining.
        
        Args:
            value: The checkPer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to check_per property setter (gets validation automatically)
        """
        self.check_per = value  # Delegates to property setter
        return self

    def getConfiguration(self) -> "DiagnosticHandleDDDI":
        """
        AUTOSAR-compliant getter for configuration.
        
        Returns:
            The configuration value
        
        Note:
            Delegates to configuration property (CODING_RULE_V2_00017)
        """
        return self.configuration  # Delegates to property

    def setConfiguration(self, value: "DiagnosticHandleDDDI") -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """
        AUTOSAR-compliant setter for configuration with method chaining.
        
        Args:
            value: The configuration to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to configuration property setter (gets validation automatically)
        """
        self.configuration = value  # Delegates to property setter
        return self

    def getSubfunction(self) -> List["DiagnosticDynamically"]:
        """
        AUTOSAR-compliant getter for subfunction.
        
        Returns:
            The subfunction value
        
        Note:
            Delegates to subfunction property (CODING_RULE_V2_00017)
        """
        return self.subfunction  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_check_per(self, value: Optional["Boolean"]) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """
        Set checkPer and return self for chaining.
        
        Args:
            value: The checkPer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_check_per("value")
        """
        self.check_per = value  # Use property setter (gets validation)
        return self

    def with_configuration(self, value: Optional["DiagnosticHandleDDDI"]) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """
        Set configuration and return self for chaining.
        
        Args:
            value: The configuration to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_configuration("value")
        """
        self.configuration = value  # Use property setter (gets validation)
        return self