from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticAging,
    DiagnosticCommonElement,
    DiagnosticDataIdentifier,
    DiagnosticExtended,
    DiagnosticFreezeFrame,
    DiagnosticMemory,
    DiagnosticSignificance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"immediateNv must be Boolean or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNumber must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
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
