from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SignalServiceTranslationEventProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the
    signal/service translation event.
    
    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation::SignalServiceTranslationEventProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 731, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines properties for a single translated element.
        self._elementProps: List["SignalService"] = []

    @property
    def element_props(self) -> List["SignalService"]:
        """Get elementProps (Pythonic accessor)."""
        return self._elementProps
        # Defined whether the translation shall happen in a safe.
        self._safeTranslation: Optional["Boolean"] = None

    @property
    def safe_translation(self) -> Optional["Boolean"]:
        """Get safeTranslation (Pythonic accessor)."""
        return self._safeTranslation

    @safe_translation.setter
    def safe_translation(self, value: Optional["Boolean"]) -> None:
        """
        Set safeTranslation with validation.
        
        Args:
            value: The safeTranslation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._safeTranslation = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"safeTranslation must be Boolean or None, got {type(value).__name__}"
            )
        self._safeTranslation = value
        # Defined whether the translation shall happen in a secure.
        self._secure: Optional["Boolean"] = None

    @property
    def secure(self) -> Optional["Boolean"]:
        """Get secure (Pythonic accessor)."""
        return self._secure

    @secure.setter
    def secure(self, value: Optional["Boolean"]) -> None:
        """
        Set secure with validation.
        
        Args:
            value: The secure to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secure = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"secure must be Boolean or None, got {type(value).__name__}"
            )
        self._secure = value
        # of signal/service translation.
        # by: VariableDataPrototypeIn.
        self._translation: RefType = None

    @property
    def translation(self) -> RefType:
        """Get translation (Pythonic accessor)."""
        return self._translation

    @translation.setter
    def translation(self, value: RefType) -> None:
        """
        Set translation with validation.
        
        Args:
            value: The translation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._translation = None
            return

        self._translation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElementProps(self) -> List["SignalService"]:
        """
        AUTOSAR-compliant getter for elementProps.
        
        Returns:
            The elementProps value
        
        Note:
            Delegates to element_props property (CODING_RULE_V2_00017)
        """
        return self.element_props  # Delegates to property

    def getSafeTranslation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for safeTranslation.
        
        Returns:
            The safeTranslation value
        
        Note:
            Delegates to safe_translation property (CODING_RULE_V2_00017)
        """
        return self.safe_translation  # Delegates to property

    def setSafeTranslation(self, value: "Boolean") -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for safeTranslation with method chaining.
        
        Args:
            value: The safeTranslation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to safe_translation property setter (gets validation automatically)
        """
        self.safe_translation = value  # Delegates to property setter
        return self

    def getSecure(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for secure.
        
        Returns:
            The secure value
        
        Note:
            Delegates to secure property (CODING_RULE_V2_00017)
        """
        return self.secure  # Delegates to property

    def setSecure(self, value: "Boolean") -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for secure with method chaining.
        
        Args:
            value: The secure to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to secure property setter (gets validation automatically)
        """
        self.secure = value  # Delegates to property setter
        return self

    def getTranslation(self) -> RefType:
        """
        AUTOSAR-compliant getter for translation.
        
        Returns:
            The translation value
        
        Note:
            Delegates to translation property (CODING_RULE_V2_00017)
        """
        return self.translation  # Delegates to property

    def setTranslation(self, value: RefType) -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for translation with method chaining.
        
        Args:
            value: The translation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to translation property setter (gets validation automatically)
        """
        self.translation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_safe_translation(self, value: Optional["Boolean"]) -> "SignalServiceTranslationEventProps":
        """
        Set safeTranslation and return self for chaining.
        
        Args:
            value: The safeTranslation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_safe_translation("value")
        """
        self.safe_translation = value  # Use property setter (gets validation)
        return self

    def with_secure(self, value: Optional["Boolean"]) -> "SignalServiceTranslationEventProps":
        """
        Set secure and return self for chaining.
        
        Args:
            value: The secure to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_secure("value")
        """
        self.secure = value  # Use property setter (gets validation)
        return self

    def with_translation(self, value: Optional[RefType]) -> "SignalServiceTranslationEventProps":
        """
        Set translation and return self for chaining.
        
        Args:
            value: The translation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_translation("value")
        """
        self.translation = value  # Use property setter (gets validation)
        return self