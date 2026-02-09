"""
AUTOSAR Package - DiagnosticTroubleCode

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class EventObdReadinessGroup(ARObject):
    """
    This meta-class represents the ability to define the value of attribute
    eventObdReadinessGroup. It is only introduced to allow for a variant
    modeling of this attribute.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::EventObdReadinessGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 176, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the Event OBD Readiness group PID $01 and PID $41
                # computation.
        # This attribute is applicable for emission-related ECUs.
        self._eventObd: Optional["NameToken"] = None

    @property
    def event_obd(self) -> Optional["NameToken"]:
        """Get eventObd (Pythonic accessor)."""
        return self._eventObd

    @event_obd.setter
    def event_obd(self, value: Optional["NameToken"]) -> None:
        """
        Set eventObd with validation.
        
        Args:
            value: The eventObd to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventObd = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"eventObd must be NameToken or str or None, got {type(value).__name__}"
            )
        self._eventObd = value

    def with_dtc(self, value):
        """
        Set dtc and return self for chaining.

        Args:
            value: The dtc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dtc("value")
        """
        self.dtc = value  # Use property setter (gets validation)
        return self

    def with_extended_data(self, value):
        """
        Set extended_data and return self for chaining.

        Args:
            value: The extended_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_extended_data("value")
        """
        self.extended_data = value  # Use property setter (gets validation)
        return self

    def with_freeze_frame(self, value):
        """
        Set freeze_frame and return self for chaining.

        Args:
            value: The freeze_frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_freeze_frame("value")
        """
        self.freeze_frame = value  # Use property setter (gets validation)
        return self

    def with_data_identifier(self, value):
        """
        Set data_identifier and return self for chaining.

        Args:
            value: The data_identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_identifier("value")
        """
        self.data_identifier = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventObd(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for eventObd.
        
        Returns:
            The eventObd value
        
        Note:
            Delegates to event_obd property (CODING_RULE_V2_00017)
        """
        return self.event_obd  # Delegates to property

    def setEventObd(self, value: "NameToken") -> "EventObdReadinessGroup":
        """
        AUTOSAR-compliant setter for eventObd with method chaining.
        
        Args:
            value: The eventObd to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_obd property setter (gets validation automatically)
        """
        self.event_obd = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_obd(self, value: Optional["NameToken"]) -> "EventObdReadinessGroup":
        """
        Set eventObd and return self for chaining.
        
        Args:
            value: The eventObd to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_obd("value")
        """
        self.event_obd = value  # Use property setter (gets validation)
        return self



class DiagnosticTroubleCode(DiagnosticCommonElement, ABC):
    """
    A diagnostic trouble code defines a unique identifier that is shown to the
    diagnostic tester.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCode
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 176, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticTroubleCode:
            raise TypeError("DiagnosticTroubleCode is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticTroubleCodeGroup(DiagnosticCommonElement):
    """
    The diagnostic trouble code group defines the DTCs belonging together and
    thereby forming a group.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 177, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of DiagnosticTroubleCodes this
                # DiagnosticTroubleCodeGroup.
        # atpVariation.
        self._dtc: List["DiagnosticTroubleCode"] = []

    @property
    def dtc(self) -> List["DiagnosticTroubleCode"]:
        """Get dtc (Pythonic accessor)."""
        return self._dtc
        # This represents the base number of the DTC group.
        self._groupNumber: Optional["PositiveInteger"] = None

    @property
    def group_number(self) -> Optional["PositiveInteger"]:
        """Get groupNumber (Pythonic accessor)."""
        return self._groupNumber

    @group_number.setter
    def group_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set groupNumber with validation.
        
        Args:
            value: The groupNumber to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._groupNumber = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"groupNumber must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._groupNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDtc(self) -> List["DiagnosticTroubleCode"]:
        """
        AUTOSAR-compliant getter for dtc.
        
        Returns:
            The dtc value
        
        Note:
            Delegates to dtc property (CODING_RULE_V2_00017)
        """
        return self.dtc  # Delegates to property

    def getGroupNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for groupNumber.
        
        Returns:
            The groupNumber value
        
        Note:
            Delegates to group_number property (CODING_RULE_V2_00017)
        """
        return self.group_number  # Delegates to property

    def setGroupNumber(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeGroup":
        """
        AUTOSAR-compliant setter for groupNumber with method chaining.
        
        Args:
            value: The groupNumber to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to group_number property setter (gets validation automatically)
        """
        self.group_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_group_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeGroup":
        """
        Set groupNumber and return self for chaining.
        
        Args:
            value: The groupNumber to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_group_number("value")
        """
        self.group_number = value  # Use property setter (gets validation)
        return self



class DiagnosticTroubleCodeProps(DiagnosticCommonElement):
    """
    This element defines common Dtc properties that can be reused by different
    non OBD-relevant DTCs.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeProps
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 185, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an aging algorithm in case that an aging/ the event is allowed.
        self._aging: Optional["DiagnosticAging"] = None

    @property
    def aging(self) -> Optional["DiagnosticAging"]:
        """Get aging (Pythonic accessor)."""
        return self._aging

    @aging.setter
    def aging(self, value: Optional["DiagnosticAging"]) -> None:
        """
        Set aging with validation.
        
        Args:
            value: The aging to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aging = None
            return

        if not isinstance(value, DiagnosticAging):
            raise TypeError(
                f"aging must be DiagnosticAging or None, got {type(value).__name__}"
            )
        self._aging = value
        # Reference to the applicable DiagnosticMemory Destination.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._diagnostic: Optional["DiagnosticMemory"] = None

    @property
    def diagnostic(self) -> Optional["DiagnosticMemory"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["DiagnosticMemory"]) -> None:
        """
        Set diagnostic with validation.
        
        Args:
            value: The diagnostic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, DiagnosticMemory):
            raise TypeError(
                f"diagnostic must be DiagnosticMemory or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        # Defines the links to an extended data class sampler.
        # Stereotypes: atpSplitable; atpVariation.
        self._extendedData: List["DiagnosticExtended"] = []

    @property
    def extended_data(self) -> List["DiagnosticExtended"]:
        """Get extendedData (Pythonic accessor)."""
        return self._extendedData
        # Define the links to a freeze frame class sampler.
        # atpVariation.
        self._freezeFrame: List["DiagnosticFreezeFrame"] = []

    @property
    def freeze_frame(self) -> List["DiagnosticFreezeFrame"]:
        """Get freezeFrame (Pythonic accessor)."""
        return self._freezeFrame
        # Change description for Class immediateNvDataStorage table "Table A.
        # 111: DiagnosticTroubleCodeProps": enable immediate storage triggering of an
                # memory entry persistently to NVRAM.
        # non-volatile storage triggering on first shutdown.
        # non-volatile storage triggering on.
        self._immediateNv: Optional["Boolean"] = None

    @property
    def immediate_nv(self) -> Optional["Boolean"]:
        """Get immediateNv (Pythonic accessor)."""
        return self._immediateNv

    @immediate_nv.setter
    def immediate_nv(self, value: Optional["Boolean"]) -> None:
        """
        Set immediateNv with validation.
        
        Args:
            value: The immediateNv to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._immediateNv = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"immediateNv must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._immediateNv = value
        # This reference identifies the layout of legislated freeze frames used for
                # emission related diagnostics over the protocol such as OBDonUDS or WWH-OBD.
        # atpVariation.
        self._legislated: Optional["DiagnosticDataIdentifier"] = None

    @property
    def legislated(self) -> Optional["DiagnosticDataIdentifier"]:
        """Get legislated (Pythonic accessor)."""
        return self._legislated

    @legislated.setter
    def legislated(self, value: Optional["DiagnosticDataIdentifier"]) -> None:
        """
        Set legislated with validation.
        
        Args:
            value: The legislated to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._legislated = None
            return

        if not isinstance(value, DiagnosticDataIdentifier):
            raise TypeError(
                f"legislated must be DiagnosticDataIdentifier or None, got {type(value).__name__}"
            )
        self._legislated = value
        # This attribute defines the number of according freeze records, which can
        # maximal be stored for this Therefore all these freeze frame records have the
        # frame class.
        self._maxNumber: Optional["PositiveInteger"] = None

    @property
    def max_number(self) -> Optional["PositiveInteger"]:
        """Get maxNumber (Pythonic accessor)."""
        return self._maxNumber

    @max_number.setter
    def max_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumber with validation.
        
        Args:
            value: The maxNumber to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumber = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNumber must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNumber = value
        # Priority of the event, in view of full event buffer.
        # A lower higher priority.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.
        
        Args:
            value: The priority to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # Significance of the event, which indicates additional concerning fault
        # classification and resolution.
        self._significance: Optional["DiagnosticSignificance"] = None

    @property
    def significance(self) -> Optional["DiagnosticSignificance"]:
        """Get significance (Pythonic accessor)."""
        return self._significance

    @significance.setter
    def significance(self, value: Optional["DiagnosticSignificance"]) -> None:
        """
        Set significance with validation.
        
        Args:
            value: The significance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._significance = None
            return

        if not isinstance(value, DiagnosticSignificance):
            raise TypeError(
                f"significance must be DiagnosticSignificance or None, got {type(value).__name__}"
            )
        self._significance = value
        # This represents the freeze frame layout as a set of DIDs.
        # Stereotypes: atpSplitable; atpVariation.
        self._snapshot: Optional["DiagnosticDataIdentifier"] = None

    @property
    def snapshot(self) -> Optional["DiagnosticDataIdentifier"]:
        """Get snapshot (Pythonic accessor)."""
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value: Optional["DiagnosticDataIdentifier"]) -> None:
        """
        Set snapshot with validation.
        
        Args:
            value: The snapshot to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._snapshot = None
            return

        if not isinstance(value, DiagnosticDataIdentifier):
            raise TypeError(
                f"snapshot must be DiagnosticDataIdentifier or None, got {type(value).__name__}"
            )
        self._snapshot = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAging(self) -> "DiagnosticAging":
        """
        AUTOSAR-compliant getter for aging.
        
        Returns:
            The aging value
        
        Note:
            Delegates to aging property (CODING_RULE_V2_00017)
        """
        return self.aging  # Delegates to property

    def setAging(self, value: "DiagnosticAging") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for aging with method chaining.
        
        Args:
            value: The aging to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to aging property setter (gets validation automatically)
        """
        self.aging = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> "DiagnosticMemory":
        """
        AUTOSAR-compliant getter for diagnostic.
        
        Returns:
            The diagnostic value
        
        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "DiagnosticMemory") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getExtendedData(self) -> List["DiagnosticExtended"]:
        """
        AUTOSAR-compliant getter for extendedData.
        
        Returns:
            The extendedData value
        
        Note:
            Delegates to extended_data property (CODING_RULE_V2_00017)
        """
        return self.extended_data  # Delegates to property

    def getFreezeFrame(self) -> List["DiagnosticFreezeFrame"]:
        """
        AUTOSAR-compliant getter for freezeFrame.
        
        Returns:
            The freezeFrame value
        
        Note:
            Delegates to freeze_frame property (CODING_RULE_V2_00017)
        """
        return self.freeze_frame  # Delegates to property

    def getImmediateNv(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for immediateNv.
        
        Returns:
            The immediateNv value
        
        Note:
            Delegates to immediate_nv property (CODING_RULE_V2_00017)
        """
        return self.immediate_nv  # Delegates to property

    def setImmediateNv(self, value: "Boolean") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for immediateNv with method chaining.
        
        Args:
            value: The immediateNv to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to immediate_nv property setter (gets validation automatically)
        """
        self.immediate_nv = value  # Delegates to property setter
        return self

    def getLegislated(self) -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant getter for legislated.
        
        Returns:
            The legislated value
        
        Note:
            Delegates to legislated property (CODING_RULE_V2_00017)
        """
        return self.legislated  # Delegates to property

    def setLegislated(self, value: "DiagnosticDataIdentifier") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for legislated with method chaining.
        
        Args:
            value: The legislated to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to legislated property setter (gets validation automatically)
        """
        self.legislated = value  # Delegates to property setter
        return self

    def getMaxNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumber.
        
        Returns:
            The maxNumber value
        
        Note:
            Delegates to max_number property (CODING_RULE_V2_00017)
        """
        return self.max_number  # Delegates to property

    def setMaxNumber(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for maxNumber with method chaining.
        
        Args:
            value: The maxNumber to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_number property setter (gets validation automatically)
        """
        self.max_number = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.
        
        Returns:
            The priority value
        
        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for priority with method chaining.
        
        Args:
            value: The priority to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getSignificance(self) -> "DiagnosticSignificance":
        """
        AUTOSAR-compliant getter for significance.
        
        Returns:
            The significance value
        
        Note:
            Delegates to significance property (CODING_RULE_V2_00017)
        """
        return self.significance  # Delegates to property

    def setSignificance(self, value: "DiagnosticSignificance") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for significance with method chaining.
        
        Args:
            value: The significance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to significance property setter (gets validation automatically)
        """
        self.significance = value  # Delegates to property setter
        return self

    def getSnapshot(self) -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant getter for snapshot.
        
        Returns:
            The snapshot value
        
        Note:
            Delegates to snapshot property (CODING_RULE_V2_00017)
        """
        return self.snapshot  # Delegates to property

    def setSnapshot(self, value: "DiagnosticDataIdentifier") -> "DiagnosticTroubleCodeProps":
        """
        AUTOSAR-compliant setter for snapshot with method chaining.
        
        Args:
            value: The snapshot to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to snapshot property setter (gets validation automatically)
        """
        self.snapshot = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aging(self, value: Optional["DiagnosticAging"]) -> "DiagnosticTroubleCodeProps":
        """
        Set aging and return self for chaining.
        
        Args:
            value: The aging to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_aging("value")
        """
        self.aging = value  # Use property setter (gets validation)
        return self

    def with_diagnostic(self, value: Optional["DiagnosticMemory"]) -> "DiagnosticTroubleCodeProps":
        """
        Set diagnostic and return self for chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic("value")
        """
        self.diagnostic = value  # Use property setter (gets validation)
        return self

    def with_immediate_nv(self, value: Optional["Boolean"]) -> "DiagnosticTroubleCodeProps":
        """
        Set immediateNv and return self for chaining.
        
        Args:
            value: The immediateNv to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_immediate_nv("value")
        """
        self.immediate_nv = value  # Use property setter (gets validation)
        return self

    def with_legislated(self, value: Optional["DiagnosticDataIdentifier"]) -> "DiagnosticTroubleCodeProps":
        """
        Set legislated and return self for chaining.
        
        Args:
            value: The legislated to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_legislated("value")
        """
        self.legislated = value  # Use property setter (gets validation)
        return self

    def with_max_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeProps":
        """
        Set maxNumber and return self for chaining.
        
        Args:
            value: The maxNumber to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_number("value")
        """
        self.max_number = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeProps":
        """
        Set priority and return self for chaining.
        
        Args:
            value: The priority to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_significance(self, value: Optional["DiagnosticSignificance"]) -> "DiagnosticTroubleCodeProps":
        """
        Set significance and return self for chaining.
        
        Args:
            value: The significance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_significance("value")
        """
        self.significance = value  # Use property setter (gets validation)
        return self

    def with_snapshot(self, value: Optional["DiagnosticDataIdentifier"]) -> "DiagnosticTroubleCodeProps":
        """
        Set snapshot and return self for chaining.
        
        Args:
            value: The snapshot to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_snapshot("value")
        """
        self.snapshot = value  # Use property setter (gets validation)
        return self



class DiagnosticDataIdentifierSet(DiagnosticCommonElement):
    """
    This represents the ability to define a list of DiagnosticDataIdentifiers
    that can be reused in different contexts.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticDataIdentifierSet
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 187, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an ordered list of Data Identifiers.
        self._dataIdentifier: List["DiagnosticDataIdentifier"] = []

    @property
    def data_identifier(self) -> List["DiagnosticDataIdentifier"]:
        """Get dataIdentifier (Pythonic accessor)."""
        return self._dataIdentifier

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataIdentifier(self) -> List["DiagnosticDataIdentifier"]:
        """
        AUTOSAR-compliant getter for dataIdentifier.
        
        Returns:
            The dataIdentifier value
        
        Note:
            Delegates to data_identifier property (CODING_RULE_V2_00017)
        """
        return self.data_identifier  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticTroubleCodeUds(DiagnosticTroubleCode):
    """
    This element is used to describe non OBD-relevant DTCs.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeUds
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 173, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute describes the affection of the event by the PTO handling.
        # event is affected by the Dem PTO handling.
        # event is not affected by the Dem PTO handling.
        self._considerPto: Optional["Boolean"] = None

    @property
    def consider_pto(self) -> Optional["Boolean"]:
        """Get considerPto (Pythonic accessor)."""
        return self._considerPto

    @consider_pto.setter
    def consider_pto(self, value: Optional["Boolean"]) -> None:
        """
        Set considerPto with validation.
        
        Args:
            value: The considerPto to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._considerPto = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"considerPto must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._considerPto = value
        # Defined properties associated with the DemDTC.
        self._dtcPropsProps: Optional["DiagnosticTroubleCode"] = None

    @property
    def dtc_props_props(self) -> Optional["DiagnosticTroubleCode"]:
        """Get dtcPropsProps (Pythonic accessor)."""
        return self._dtcPropsProps

    @dtc_props_props.setter
    def dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set dtcPropsProps with validation.
        
        Args:
            value: The dtcPropsProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dtcPropsProps = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"dtcPropsProps must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._dtcPropsProps = value
        # This attribute specifies the Event OBD Readiness group for PID $01 and PID
                # $41 computation.
        # This attribute is for emission-related ECUs.
        # atpVariation 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
                # Template R23-11.
        self._eventReadiness: Optional["EventObdReadiness"] = None

    @property
    def event_readiness(self) -> Optional["EventObdReadiness"]:
        """Get eventReadiness (Pythonic accessor)."""
        return self._eventReadiness

    @event_readiness.setter
    def event_readiness(self, value: Optional["EventObdReadiness"]) -> None:
        """
        Set eventReadiness with validation.
        
        Args:
            value: The eventReadiness to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventReadiness = None
            return

        if not isinstance(value, EventObdReadiness):
            raise TypeError(
                f"eventReadiness must be EventObdReadiness or None, got {type(value).__name__}"
            )
        self._eventReadiness = value
        # This attribute specifies a 1-byte value which identifies the vehicle / system
                # function which DTC.
        # This parameter is necessary for the severity information.
        self._functionalUnit: Optional["PositiveInteger"] = None

    @property
    def functional_unit(self) -> Optional["PositiveInteger"]:
        """Get functionalUnit (Pythonic accessor)."""
        return self._functionalUnit

    @functional_unit.setter
    def functional_unit(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set functionalUnit with validation.
        
        Args:
            value: The functionalUnit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionalUnit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"functionalUnit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._functionalUnit = value
        # 3 Byte OBD DTC value based on the definition from SAE The existence of this
        # attribute is only required if and OBD DTC values are used for SAE this
        # attribute does not exist, then UDS DTC used with J1979-2.
        self._obdDtc: Optional["PositiveInteger"] = None

    @property
    def obd_dtc(self) -> Optional["PositiveInteger"]:
        """Get obdDtc (Pythonic accessor)."""
        return self._obdDtc

    @obd_dtc.setter
    def obd_dtc(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set obdDtc with validation.
        
        Args:
            value: The obdDtc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdDtc = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"obdDtc must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._obdDtc = value
        # DTC severity according to ISO 14229-1.
        # atpVariation.
        self._severity: Optional["DiagnosticUdsSeverity"] = None

    @property
    def severity(self) -> Optional["DiagnosticUdsSeverity"]:
        """Get severity (Pythonic accessor)."""
        return self._severity

    @severity.setter
    def severity(self, value: Optional["DiagnosticUdsSeverity"]) -> None:
        """
        Set severity with validation.
        
        Args:
            value: The severity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._severity = None
            return

        if not isinstance(value, DiagnosticUdsSeverity):
            raise TypeError(
                f"severity must be DiagnosticUdsSeverity or None, got {type(value).__name__}"
            )
        self._severity = value
        # Unique Diagnostic Trouble Code value for UDS.
        self._udsDtcValue: Optional["PositiveInteger"] = None

    @property
    def uds_dtc_value(self) -> Optional["PositiveInteger"]:
        """Get udsDtcValue (Pythonic accessor)."""
        return self._udsDtcValue

    @uds_dtc_value.setter
    def uds_dtc_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set udsDtcValue with validation.
        
        Args:
            value: The udsDtcValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udsDtcValue = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"udsDtcValue must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._udsDtcValue = value
        # This attribute is used to identify (if applicable) the.
        self._wwhObdDtc: Optional["DiagnosticWwhObdDtc"] = None

    @property
    def wwh_obd_dtc(self) -> Optional["DiagnosticWwhObdDtc"]:
        """Get wwhObdDtc (Pythonic accessor)."""
        return self._wwhObdDtc

    @wwh_obd_dtc.setter
    def wwh_obd_dtc(self, value: Optional["DiagnosticWwhObdDtc"]) -> None:
        """
        Set wwhObdDtc with validation.
        
        Args:
            value: The wwhObdDtc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wwhObdDtc = None
            return

        if not isinstance(value, DiagnosticWwhObdDtc):
            raise TypeError(
                f"wwhObdDtc must be DiagnosticWwhObdDtc or None, got {type(value).__name__}"
            )
        self._wwhObdDtc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsiderPto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for considerPto.
        
        Returns:
            The considerPto value
        
        Note:
            Delegates to consider_pto property (CODING_RULE_V2_00017)
        """
        return self.consider_pto  # Delegates to property

    def setConsiderPto(self, value: "Boolean") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for considerPto with method chaining.
        
        Args:
            value: The considerPto to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to consider_pto property setter (gets validation automatically)
        """
        self.consider_pto = value  # Delegates to property setter
        return self

    def getDtcPropsProps(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for dtcPropsProps.
        
        Returns:
            The dtcPropsProps value
        
        Note:
            Delegates to dtc_props_props property (CODING_RULE_V2_00017)
        """
        return self.dtc_props_props  # Delegates to property

    def setDtcPropsProps(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for dtcPropsProps with method chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dtc_props_props property setter (gets validation automatically)
        """
        self.dtc_props_props = value  # Delegates to property setter
        return self

    def getEventReadiness(self) -> "EventObdReadiness":
        """
        AUTOSAR-compliant getter for eventReadiness.
        
        Returns:
            The eventReadiness value
        
        Note:
            Delegates to event_readiness property (CODING_RULE_V2_00017)
        """
        return self.event_readiness  # Delegates to property

    def setEventReadiness(self, value: "EventObdReadiness") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for eventReadiness with method chaining.
        
        Args:
            value: The eventReadiness to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_readiness property setter (gets validation automatically)
        """
        self.event_readiness = value  # Delegates to property setter
        return self

    def getFunctionalUnit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for functionalUnit.
        
        Returns:
            The functionalUnit value
        
        Note:
            Delegates to functional_unit property (CODING_RULE_V2_00017)
        """
        return self.functional_unit  # Delegates to property

    def setFunctionalUnit(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for functionalUnit with method chaining.
        
        Args:
            value: The functionalUnit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to functional_unit property setter (gets validation automatically)
        """
        self.functional_unit = value  # Delegates to property setter
        return self

    def getObdDtc(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for obdDtc.
        
        Returns:
            The obdDtc value
        
        Note:
            Delegates to obd_dtc property (CODING_RULE_V2_00017)
        """
        return self.obd_dtc  # Delegates to property

    def setObdDtc(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for obdDtc with method chaining.
        
        Args:
            value: The obdDtc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to obd_dtc property setter (gets validation automatically)
        """
        self.obd_dtc = value  # Delegates to property setter
        return self

    def getSeverity(self) -> "DiagnosticUdsSeverity":
        """
        AUTOSAR-compliant getter for severity.
        
        Returns:
            The severity value
        
        Note:
            Delegates to severity property (CODING_RULE_V2_00017)
        """
        return self.severity  # Delegates to property

    def setSeverity(self, value: "DiagnosticUdsSeverity") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for severity with method chaining.
        
        Args:
            value: The severity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to severity property setter (gets validation automatically)
        """
        self.severity = value  # Delegates to property setter
        return self

    def getUdsDtcValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for udsDtcValue.
        
        Returns:
            The udsDtcValue value
        
        Note:
            Delegates to uds_dtc_value property (CODING_RULE_V2_00017)
        """
        return self.uds_dtc_value  # Delegates to property

    def setUdsDtcValue(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for udsDtcValue with method chaining.
        
        Args:
            value: The udsDtcValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to uds_dtc_value property setter (gets validation automatically)
        """
        self.uds_dtc_value = value  # Delegates to property setter
        return self

    def getWwhObdDtc(self) -> "DiagnosticWwhObdDtc":
        """
        AUTOSAR-compliant getter for wwhObdDtc.
        
        Returns:
            The wwhObdDtc value
        
        Note:
            Delegates to wwh_obd_dtc property (CODING_RULE_V2_00017)
        """
        return self.wwh_obd_dtc  # Delegates to property

    def setWwhObdDtc(self, value: "DiagnosticWwhObdDtc") -> "DiagnosticTroubleCodeUds":
        """
        AUTOSAR-compliant setter for wwhObdDtc with method chaining.
        
        Args:
            value: The wwhObdDtc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to wwh_obd_dtc property setter (gets validation automatically)
        """
        self.wwh_obd_dtc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_consider_pto(self, value: Optional["Boolean"]) -> "DiagnosticTroubleCodeUds":
        """
        Set considerPto and return self for chaining.
        
        Args:
            value: The considerPto to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_consider_pto("value")
        """
        self.consider_pto = value  # Use property setter (gets validation)
        return self

    def with_dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeUds":
        """
        Set dtcPropsProps and return self for chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dtc_props_props("value")
        """
        self.dtc_props_props = value  # Use property setter (gets validation)
        return self

    def with_event_readiness(self, value: Optional["EventObdReadiness"]) -> "DiagnosticTroubleCodeUds":
        """
        Set eventReadiness and return self for chaining.
        
        Args:
            value: The eventReadiness to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_readiness("value")
        """
        self.event_readiness = value  # Use property setter (gets validation)
        return self

    def with_functional_unit(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeUds":
        """
        Set functionalUnit and return self for chaining.
        
        Args:
            value: The functionalUnit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_functional_unit("value")
        """
        self.functional_unit = value  # Use property setter (gets validation)
        return self

    def with_obd_dtc(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeUds":
        """
        Set obdDtc and return self for chaining.
        
        Args:
            value: The obdDtc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_obd_dtc("value")
        """
        self.obd_dtc = value  # Use property setter (gets validation)
        return self

    def with_severity(self, value: Optional["DiagnosticUdsSeverity"]) -> "DiagnosticTroubleCodeUds":
        """
        Set severity and return self for chaining.
        
        Args:
            value: The severity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_severity("value")
        """
        self.severity = value  # Use property setter (gets validation)
        return self

    def with_uds_dtc_value(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeUds":
        """
        Set udsDtcValue and return self for chaining.
        
        Args:
            value: The udsDtcValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_uds_dtc_value("value")
        """
        self.uds_dtc_value = value  # Use property setter (gets validation)
        return self

    def with_wwh_obd_dtc(self, value: Optional["DiagnosticWwhObdDtc"]) -> "DiagnosticTroubleCodeUds":
        """
        Set wwhObdDtc and return self for chaining.
        
        Args:
            value: The wwhObdDtc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_wwh_obd_dtc("value")
        """
        self.wwh_obd_dtc = value  # Use property setter (gets validation)
        return self



class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):
    """
    This element is used to define OBD-relevant DTCs.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeObd
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 174, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute describes the affection of the event by the PTO handling.
        # event is affected by the Dem PTO handling.
        # event is not affected by the Dem PTO handling.
        self._considerPto: Optional["Boolean"] = None

    @property
    def consider_pto(self) -> Optional["Boolean"]:
        """Get considerPto (Pythonic accessor)."""
        return self._considerPto

    @consider_pto.setter
    def consider_pto(self, value: Optional["Boolean"]) -> None:
        """
        Set considerPto with validation.
        
        Args:
            value: The considerPto to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._considerPto = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"considerPto must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._considerPto = value
        # Defined properties associated with the DemDTC.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._dtcPropsProps: Optional["DiagnosticTroubleCode"] = None

    @property
    def dtc_props_props(self) -> Optional["DiagnosticTroubleCode"]:
        """Get dtcPropsProps (Pythonic accessor)."""
        return self._dtcPropsProps

    @dtc_props_props.setter
    def dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set dtcPropsProps with validation.
        
        Args:
            value: The dtcPropsProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dtcPropsProps = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"dtcPropsProps must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._dtcPropsProps = value
        # This aggregation allows for the variant definition of the attribute
                # eventObdReadinessGroup.
        # atpVariation.
        self._eventReadiness: Optional["EventObdReadiness"] = None

    @property
    def event_readiness(self) -> Optional["EventObdReadiness"]:
        """Get eventReadiness (Pythonic accessor)."""
        return self._eventReadiness

    @event_readiness.setter
    def event_readiness(self, value: Optional["EventObdReadiness"]) -> None:
        """
        Set eventReadiness with validation.
        
        Args:
            value: The eventReadiness to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventReadiness = None
            return

        if not isinstance(value, EventObdReadiness):
            raise TypeError(
                f"eventReadiness must be EventObdReadiness or None, got {type(value).__name__}"
            )
        self._eventReadiness = value
        # Unique Diagnostic Trouble Code value for OBD.
        self._obdDTCValue: Optional["PositiveInteger"] = None

    @property
    def obd_dtc_value(self) -> Optional["PositiveInteger"]:
        """Get obdDTCValue (Pythonic accessor)."""
        return self._obdDTCValue

    @obd_dtc_value.setter
    def obd_dtc_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set obdDTCValue with validation.
        
        Args:
            value: The obdDTCValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdDTCValue = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"obdDTCValue must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._obdDTCValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsiderPto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for considerPto.
        
        Returns:
            The considerPto value
        
        Note:
            Delegates to consider_pto property (CODING_RULE_V2_00017)
        """
        return self.consider_pto  # Delegates to property

    def setConsiderPto(self, value: "Boolean") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for considerPto with method chaining.
        
        Args:
            value: The considerPto to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to consider_pto property setter (gets validation automatically)
        """
        self.consider_pto = value  # Delegates to property setter
        return self

    def getDtcPropsProps(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for dtcPropsProps.
        
        Returns:
            The dtcPropsProps value
        
        Note:
            Delegates to dtc_props_props property (CODING_RULE_V2_00017)
        """
        return self.dtc_props_props  # Delegates to property

    def setDtcPropsProps(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for dtcPropsProps with method chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dtc_props_props property setter (gets validation automatically)
        """
        self.dtc_props_props = value  # Delegates to property setter
        return self

    def getEventReadiness(self) -> "EventObdReadiness":
        """
        AUTOSAR-compliant getter for eventReadiness.
        
        Returns:
            The eventReadiness value
        
        Note:
            Delegates to event_readiness property (CODING_RULE_V2_00017)
        """
        return self.event_readiness  # Delegates to property

    def setEventReadiness(self, value: "EventObdReadiness") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for eventReadiness with method chaining.
        
        Args:
            value: The eventReadiness to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_readiness property setter (gets validation automatically)
        """
        self.event_readiness = value  # Delegates to property setter
        return self

    def getObdDTCValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for obdDTCValue.
        
        Returns:
            The obdDTCValue value
        
        Note:
            Delegates to obd_dtc_value property (CODING_RULE_V2_00017)
        """
        return self.obd_dtc_value  # Delegates to property

    def setObdDTCValue(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeObd":
        """
        AUTOSAR-compliant setter for obdDTCValue with method chaining.
        
        Args:
            value: The obdDTCValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to obd_dtc_value property setter (gets validation automatically)
        """
        self.obd_dtc_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_consider_pto(self, value: Optional["Boolean"]) -> "DiagnosticTroubleCodeObd":
        """
        Set considerPto and return self for chaining.
        
        Args:
            value: The considerPto to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_consider_pto("value")
        """
        self.consider_pto = value  # Use property setter (gets validation)
        return self

    def with_dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeObd":
        """
        Set dtcPropsProps and return self for chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dtc_props_props("value")
        """
        self.dtc_props_props = value  # Use property setter (gets validation)
        return self

    def with_event_readiness(self, value: Optional["EventObdReadiness"]) -> "DiagnosticTroubleCodeObd":
        """
        Set eventReadiness and return self for chaining.
        
        Args:
            value: The eventReadiness to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_readiness("value")
        """
        self.event_readiness = value  # Use property setter (gets validation)
        return self

    def with_obd_dtc_value(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeObd":
        """
        Set obdDTCValue and return self for chaining.
        
        Args:
            value: The obdDTCValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_obd_dtc_value("value")
        """
        self.obd_dtc_value = value  # Use property setter (gets validation)
        return self



class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):
    """
    This meta-class represents the ability to model specific trouble-code
    related properties for J1939.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeJ1939
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 221, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defined properties associated with the J1939 DTC.
        self._dtcPropsProps: Optional["DiagnosticTroubleCode"] = None

    @property
    def dtc_props_props(self) -> Optional["DiagnosticTroubleCode"]:
        """Get dtcPropsProps (Pythonic accessor)."""
        return self._dtcPropsProps

    @dtc_props_props.setter
    def dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set dtcPropsProps with validation.
        
        Args:
            value: The dtcPropsProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dtcPropsProps = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"dtcPropsProps must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._dtcPropsProps = value
        # This attribute represents the behavior of the Failure Mode 719 Document ID
        # 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._fmi: Optional["PositiveInteger"] = None

    @property
    def fmi(self) -> Optional["PositiveInteger"]:
        """Get fmi (Pythonic accessor)."""
        return self._fmi

    @fmi.setter
    def fmi(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set fmi with validation.
        
        Args:
            value: The fmi to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fmi = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"fmi must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._fmi = value
        # This attribute further specifies the DTC in terms of its.
        self._kind: Optional["DiagnosticTroubleCode"] = None

    @property
    def kind(self) -> Optional["DiagnosticTroubleCode"]:
        """Get kind (Pythonic accessor)."""
        return self._kind

    @kind.setter
    def kind(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set kind with validation.
        
        Args:
            value: The kind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._kind = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"kind must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._kind = value
        # This represents the related DiagnosticJ1939Node.
        self._node: Optional["DiagnosticJ1939Node"] = None

    @property
    def node(self) -> Optional["DiagnosticJ1939Node"]:
        """Get node (Pythonic accessor)."""
        return self._node

    @node.setter
    def node(self, value: Optional["DiagnosticJ1939Node"]) -> None:
        """
        Set node with validation.
        
        Args:
            value: The node to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._node = None
            return

        if not isinstance(value, DiagnosticJ1939Node):
            raise TypeError(
                f"node must be DiagnosticJ1939Node or None, got {type(value).__name__}"
            )
        self._node = value
        # This represents the releated SPN.
        self._spn: Optional["DiagnosticJ1939Spn"] = None

    @property
    def spn(self) -> Optional["DiagnosticJ1939Spn"]:
        """Get spn (Pythonic accessor)."""
        return self._spn

    @spn.setter
    def spn(self, value: Optional["DiagnosticJ1939Spn"]) -> None:
        """
        Set spn with validation.
        
        Args:
            value: The spn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._spn = None
            return

        if not isinstance(value, DiagnosticJ1939Spn):
            raise TypeError(
                f"spn must be DiagnosticJ1939Spn or None, got {type(value).__name__}"
            )
        self._spn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDtcPropsProps(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for dtcPropsProps.
        
        Returns:
            The dtcPropsProps value
        
        Note:
            Delegates to dtc_props_props property (CODING_RULE_V2_00017)
        """
        return self.dtc_props_props  # Delegates to property

    def setDtcPropsProps(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for dtcPropsProps with method chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dtc_props_props property setter (gets validation automatically)
        """
        self.dtc_props_props = value  # Delegates to property setter
        return self

    def getFmi(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for fmi.
        
        Returns:
            The fmi value
        
        Note:
            Delegates to fmi property (CODING_RULE_V2_00017)
        """
        return self.fmi  # Delegates to property

    def setFmi(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for fmi with method chaining.
        
        Args:
            value: The fmi to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to fmi property setter (gets validation automatically)
        """
        self.fmi = value  # Delegates to property setter
        return self

    def getKind(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for kind.
        
        Returns:
            The kind value
        
        Note:
            Delegates to kind property (CODING_RULE_V2_00017)
        """
        return self.kind  # Delegates to property

    def setKind(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for kind with method chaining.
        
        Args:
            value: The kind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to kind property setter (gets validation automatically)
        """
        self.kind = value  # Delegates to property setter
        return self

    def getNode(self) -> "DiagnosticJ1939Node":
        """
        AUTOSAR-compliant getter for node.
        
        Returns:
            The node value
        
        Note:
            Delegates to node property (CODING_RULE_V2_00017)
        """
        return self.node  # Delegates to property

    def setNode(self, value: "DiagnosticJ1939Node") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for node with method chaining.
        
        Args:
            value: The node to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to node property setter (gets validation automatically)
        """
        self.node = value  # Delegates to property setter
        return self

    def getSpn(self) -> "DiagnosticJ1939Spn":
        """
        AUTOSAR-compliant getter for spn.
        
        Returns:
            The spn value
        
        Note:
            Delegates to spn property (CODING_RULE_V2_00017)
        """
        return self.spn  # Delegates to property

    def setSpn(self, value: "DiagnosticJ1939Spn") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for spn with method chaining.
        
        Args:
            value: The spn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to spn property setter (gets validation automatically)
        """
        self.spn = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set dtcPropsProps and return self for chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dtc_props_props("value")
        """
        self.dtc_props_props = value  # Use property setter (gets validation)
        return self

    def with_fmi(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set fmi and return self for chaining.
        
        Args:
            value: The fmi to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_fmi("value")
        """
        self.fmi = value  # Use property setter (gets validation)
        return self

    def with_kind(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set kind and return self for chaining.
        
        Args:
            value: The kind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_kind("value")
        """
        self.kind = value  # Use property setter (gets validation)
        return self

    def with_node(self, value: Optional["DiagnosticJ1939Node"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set node and return self for chaining.
        
        Args:
            value: The node to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_node("value")
        """
        self.node = value  # Use property setter (gets validation)
        return self

    def with_spn(self, value: Optional["DiagnosticJ1939Spn"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set spn and return self for chaining.
        
        Args:
            value: The spn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_spn("value")
        """
        self.spn = value  # Use property setter (gets validation)
        return self


class DiagnosticTypeOfDtcSupportedEnum(AREnum):
    """
    DiagnosticTypeOfDtcSupportedEnum enumeration

Supported Dtc Types Aggregated by DiagnosticMemoryDestinationPrimary.typeOfDtcSupported

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode
    """
    # ISO11992-4 DTC format
    iso11992_4 = "0"

    # ISO14229-1 DTC format (3 byte format)
    iso14229_1 = "1"

    # ISO15031-6 DTC format (2 byte format)
    iso15031_6 = "2"

    # SAEJ1939-73 DTC format
    saeJ1939_73 = "3"

    # SAE_J2012-DA_DTCFormat_00 (3 byte format)
    saeJ2012_da = "4"



class DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum(AREnum):
    """
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum enumeration

This enumeration controls whether the aging and displacement mechanism shall be applied to the ’TestFailedSinceLastClear’ status bits. Aggregated by DiagnosticMemoryDestination.statusBitHandlingTestFailedSinceLastClear (cid:53) 183 of 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR CP R23-11 (cid:52)

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode
    """
    # The "TestFailedSinceLastClear" status bits are reset to 0, if aging or displacement applies.
    statusBitAgingAndDisplacement = "0"

    # Aging and displacement has no impact on the "TestFailedSinceLastClear" status bits.
    statusBitNormal = "1"



class DiagnosticSignificanceEnum(AREnum):
    """
    DiagnosticSignificanceEnum enumeration

Significance level of a diagnostic event. Aggregated by DiagnosticTroubleCodeProps.significance

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode
    """
    # Failure, which affects the component/ECU itself.
    fault = "0"

    # Issue, which indicates additional information concerning insufficient system behavior.
    occurence = "1"



class DiagnosticUdsSeverityEnum(AREnum):
    """
    DiagnosticUdsSeverityEnum enumeration

Severity types for a DTC according to ISO 14229-1. Aggregated by DiagnosticTroubleCodeUds.severity

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode
    """
    # Check at next halt.
    checkAtNextHalt = "0"

    # Check immediately.
    immediately = "1"

    # Maintenance required.
    maintenanceOnly = "2"

    # No severity information available.
    noSeverity = "3"



class DiagnosticWwhObdDtcClassEnum(AREnum):
    """
    DiagnosticWwhObdDtcClassEnum enumeration

This meta-class represents the ability to model severity classes of an WWH-OBD DTC. Aggregated by DiagnosticTroubleCodeUds.wwhObdDtcClass

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode
    """
    # Extract Template
    Diagnostic = "None"

    # CP R23-11
    AUTOSAR = "None"

    # This attribute represents the severity class A.
    demDtcWwhObdClassA = "0"

    # This attribute represents the severity class B1.
    demDtcWwhObdClassB1 = "1"

    # This attribute represents the severity class B2.
    demDtcWwhObdClassB2 = "2"

    # This attribute represents the severity class C.
    demDtcWwhObdClassC = "3"

    # This attribute represents the option to intentionally not describe a dedicated severity class of an
    demDtcWwhObd = "None"

    # WWH-OBD DTC.
    ClassNoInformation = "4"



class DiagnosticTroubleCodeJ1939DtcKindEnum(AREnum):
    """
    DiagnosticTroubleCodeJ1939DtcKindEnum enumeration

This meta-class represents the ability to further specify a J1939 DTC in terms of its semantics. Aggregated by DiagnosticTroubleCodeJ1939.kind

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode
    """
    # this represents a DTC that is only relevant for service in a garage, reported by e.g. DM53.
    serviceOnly = "0"

    # This represents a non-specific DTC reported by e.g. DM1.
    standard = "1"
