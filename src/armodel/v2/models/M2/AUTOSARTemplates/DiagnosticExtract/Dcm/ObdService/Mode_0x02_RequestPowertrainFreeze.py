"""
AUTOSAR Package - Mode_0x02_RequestPowertrainFreeze

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x02_RequestPowertrainFreeze
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)




class DiagnosticRequestPowertrainFreezeFrameData(DiagnosticServiceInstance):
    """
    This meta-class represents the ability to model an instance of the OBD mode
    0x02 service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x02_RequestPowertrainFreeze::DiagnosticRequestPowertrainFreezeFrameData
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 152, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the associated freeze-frame.
        self._freezeFrameFreezeFrame: Optional["DiagnosticPowertrain"] = None

    @property
    def freeze_frame_freeze_frame(self) -> Optional["DiagnosticPowertrain"]:
        """Get freezeFrameFreezeFrame (Pythonic accessor)."""
        return self._freezeFrameFreezeFrame

    @freeze_frame_freeze_frame.setter
    def freeze_frame_freeze_frame(self, value: Optional["DiagnosticPowertrain"]) -> None:
        """
        Set freezeFrameFreezeFrame with validation.
        
        Args:
            value: The freezeFrameFreezeFrame to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freezeFrameFreezeFrame = None
            return

        if not isinstance(value, DiagnosticPowertrain):
            raise TypeError(
                f"freezeFrameFreezeFrame must be DiagnosticPowertrain or None, got {type(value).__name__}"
            )
        self._freezeFrameFreezeFrame = value
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # Thereby, the reference represents the ability to access Data shared
                # attributes among all DiagnosticRequestPowertrain the given context.
        self._request: Optional["DiagnosticRequest"] = None

    @property
    def request(self) -> Optional["DiagnosticRequest"]:
        """Get request (Pythonic accessor)."""
        return self._request

    @request.setter
    def request(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set request with validation.
        
        Args:
            value: The request to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"request must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._request = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFreezeFrameFreezeFrame(self) -> "DiagnosticPowertrain":
        """
        AUTOSAR-compliant getter for freezeFrameFreezeFrame.
        
        Returns:
            The freezeFrameFreezeFrame value
        
        Note:
            Delegates to freeze_frame_freeze_frame property (CODING_RULE_V2_00017)
        """
        return self.freeze_frame_freeze_frame  # Delegates to property

    def setFreezeFrameFreezeFrame(self, value: "DiagnosticPowertrain") -> "DiagnosticRequestPowertrainFreezeFrameData":
        """
        AUTOSAR-compliant setter for freezeFrameFreezeFrame with method chaining.
        
        Args:
            value: The freezeFrameFreezeFrame to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to freeze_frame_freeze_frame property setter (gets validation automatically)
        """
        self.freeze_frame_freeze_frame = value  # Delegates to property setter
        return self

    def getRequest(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for request.
        
        Returns:
            The request value
        
        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def setRequest(self, value: "DiagnosticRequest") -> "DiagnosticRequestPowertrainFreezeFrameData":
        """
        AUTOSAR-compliant setter for request with method chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to request property setter (gets validation automatically)
        """
        self.request = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_freeze_frame_freeze_frame(self, value: Optional["DiagnosticPowertrain"]) -> "DiagnosticRequestPowertrainFreezeFrameData":
        """
        Set freezeFrameFreezeFrame and return self for chaining.
        
        Args:
            value: The freezeFrameFreezeFrame to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_freeze_frame_freeze_frame("value")
        """
        self.freeze_frame_freeze_frame = value  # Use property setter (gets validation)
        return self

    def with_request(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestPowertrainFreezeFrameData":
        """
        Set request and return self for chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self



class DiagnosticRequestPowertrainFreezeFrameDataClass(DiagnosticServiceClass):
    """
    This meta-class represents the ability to define common properties for all
    instances of the "Request Powertrain Freeze Frame Data" OBD diagnostic
    service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x02_RequestPowertrainFreeze::DiagnosticRequestPowertrainFreezeFrameDataClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 152, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticPowertrainFreezeFrame(DiagnosticCommonElement):
    """
    This meta-class represents a powertrain-related freeze-frame. In theory,
    this meta-class would need an additional id attribute. However, legal
    regulations requires only a single value for this attribute anyway.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x02_RequestPowertrainFreeze::DiagnosticPowertrainFreezeFrame
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 153, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the PID associated with this instance of OBD mode 0x02
        # service.
        self._pid: List["DiagnosticParameter"] = []

    @property
    def pid(self) -> List["DiagnosticParameter"]:
        """Get pid (Pythonic accessor)."""
        return self._pid

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPid(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for pid.
        
        Returns:
            The pid value
        
        Note:
            Delegates to pid property (CODING_RULE_V2_00017)
        """
        return self.pid  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====