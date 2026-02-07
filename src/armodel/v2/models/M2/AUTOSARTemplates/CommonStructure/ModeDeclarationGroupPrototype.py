from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ModeDeclarationGroupPrototype(Identifiable):
    """
    The ModeDeclarationGroupPrototype specifies a set of Modes
    (ModeDeclarationGroup) which is provided or required in the given context.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeDeclarationGroupPrototype
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 42, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 323, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 113, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2038, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 233, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This allows for specifying whether or not the enclosing
        # ModeDeclarationGroupPrototype can be measured at.
        self._swCalibration: Optional["SwCalibrationAccess"] = None

    @property
    def sw_calibration(self) -> Optional["SwCalibrationAccess"]:
        """Get swCalibration (Pythonic accessor)."""
        return self._swCalibration

    @sw_calibration.setter
    def sw_calibration(self, value: Optional["SwCalibrationAccess"]) -> None:
        """
        Set swCalibration with validation.
        
        Args:
            value: The swCalibration to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalibration = None
            return

        if not isinstance(value, SwCalibrationAccess):
            raise TypeError(
                f"swCalibration must be SwCalibrationAccess or None, got {type(value).__name__}"
            )
        self._swCalibration = value
        # by a component.
        self._type: RefType = None

    @property
    def type(self) -> RefType:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: RefType) -> None:
        """
        Set type with validation.
        
        Args:
            value: The type to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwCalibration(self) -> "SwCalibrationAccess":
        """
        AUTOSAR-compliant getter for swCalibration.
        
        Returns:
            The swCalibration value
        
        Note:
            Delegates to sw_calibration property (CODING_RULE_V2_00017)
        """
        return self.sw_calibration  # Delegates to property

    def setSwCalibration(self, value: "SwCalibrationAccess") -> "ModeDeclarationGroupPrototype":
        """
        AUTOSAR-compliant setter for swCalibration with method chaining.
        
        Args:
            value: The swCalibration to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_calibration property setter (gets validation automatically)
        """
        self.sw_calibration = value  # Delegates to property setter
        return self

    def getType(self) -> RefType:
        """
        AUTOSAR-compliant getter for type.
        
        Returns:
            The type value
        
        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: RefType) -> "ModeDeclarationGroupPrototype":
        """
        AUTOSAR-compliant setter for type with method chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_calibration(self, value: Optional["SwCalibrationAccess"]) -> "ModeDeclarationGroupPrototype":
        """
        Set swCalibration and return self for chaining.
        
        Args:
            value: The swCalibration to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_calibration("value")
        """
        self.sw_calibration = value  # Use property setter (gets validation)
        return self

    def with_type(self, value: Optional[RefType]) -> "ModeDeclarationGroupPrototype":
        """
        Set type and return self for chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self