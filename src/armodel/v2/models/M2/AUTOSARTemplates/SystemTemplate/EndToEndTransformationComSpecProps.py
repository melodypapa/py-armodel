from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """
    The class EndToEndTransformationIComSpecProps specifies port specific
    configuration properties for EndToEnd transformer attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::EndToEndTransformationComSpecProps
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 200, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2023, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Clear monitoring window on transition from state Valid to Invalid.
        self._clearFromValid: Optional["Boolean"] = None

    @property
    def clear_from_valid(self) -> Optional["Boolean"]:
        """Get clearFromValid (Pythonic accessor)."""
        return self._clearFromValid

    @clear_from_valid.setter
    def clear_from_valid(self, value: Optional["Boolean"]) -> None:
        """
        Set clearFromValid with validation.
        
        Args:
            value: The clearFromValid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clearFromValid = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"clearFromValid must be Boolean or None, got {type(value).__name__}"
            )
        self._clearFromValid = value
        # Disables the E2EStateMachine (only E2E check is performed).
        self._disableEndTo: Optional["Boolean"] = None

    @property
    def disable_end_to(self) -> Optional["Boolean"]:
        """Get disableEndTo (Pythonic accessor)."""
        return self._disableEndTo

    @disable_end_to.setter
    def disable_end_to(self, value: Optional["Boolean"]) -> None:
        """
        Set disableEndTo with validation.
        
        Args:
            value: The disableEndTo to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._disableEndTo = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"disableEndTo must be Boolean or None, got {type(value).__name__}"
            )
        self._disableEndTo = value
        # Reference to additional settings for the E2E state machine.
        self._e2eProfile: Optional["E2EProfileCompatibility"] = None

    @property
    def e2e_profile(self) -> Optional["E2EProfileCompatibility"]:
        """Get e2eProfile (Pythonic accessor)."""
        return self._e2eProfile

    @e2e_profile.setter
    def e2e_profile(self, value: Optional["E2EProfileCompatibility"]) -> None:
        """
        Set e2eProfile with validation.
        
        Args:
            value: The e2eProfile to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._e2eProfile = None
            return

        if not isinstance(value, E2EProfileCompatibility):
            raise TypeError(
                f"e2eProfile must be E2EProfileCompatibility or None, got {type(value).__name__}"
            )
        self._e2eProfile = value
        # Maximum allowed difference between two counter values two consecutively
                # received valid messages.
        # For the receiver gets data with counter 1 and Max 3, then at the next
                # reception the receiver Counters with values 2, 3 or 4.
        self._maxDelta: Optional["PositiveInteger"] = None

    @property
    def max_delta(self) -> Optional["PositiveInteger"]:
        """Get maxDelta (Pythonic accessor)."""
        return self._maxDelta

    @max_delta.setter
    def max_delta(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDelta with validation.
        
        Args:
            value: The maxDelta to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDelta = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxDelta must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxDelta = value
        # Maximal number of checks in which ProfileStatus equal to was determined,
                # within the last Window for the state E2E_SM_VALID.
        # value is 0.
        self._maxErrorState: Optional["PositiveInteger"] = None

    @property
    def max_error_state(self) -> Optional["PositiveInteger"]:
        """Get maxErrorState (Pythonic accessor)."""
        return self._maxErrorState

    @max_error_state.setter
    def max_error_state(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxErrorState with validation.
        
        Args:
            value: The maxErrorState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxErrorState = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxErrorState must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxErrorState = value
        # EndToEndTransformationDescription holds these which are profile specific and
        # have the same all E2E transformers.
        self._maxNoNewOr: Optional["PositiveInteger"] = None

    @property
    def max_no_new_or(self) -> Optional["PositiveInteger"]:
        """Get maxNoNewOr (Pythonic accessor)."""
        return self._maxNoNewOr

    @max_no_new_or.setter
    def max_no_new_or(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNoNewOr with validation.
        
        Args:
            value: The maxNoNewOr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNoNewOr = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNoNewOr must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxNoNewOr = value
        # Minimal number of checks in which ProfileStatus equal to determined, within
                # the last WindowSize the state E2E_SM_INIT.
        # value is 1.
        self._minOkStateInit: Optional["PositiveInteger"] = None

    @property
    def min_ok_state_init(self) -> Optional["PositiveInteger"]:
        """Get minOkStateInit (Pythonic accessor)."""
        return self._minOkStateInit

    @min_ok_state_init.setter
    def min_ok_state_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minOkStateInit with validation.
        
        Args:
            value: The minOkStateInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minOkStateInit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minOkStateInit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minOkStateInit = value
        # Minimal number of checks in which ProfileStatus equal to was determined,
                # within the last WindowSize the state E2E_SM_VALID.
        # value is 1.
        self._minOkState: Optional["PositiveInteger"] = None

    @property
    def min_ok_state(self) -> Optional["PositiveInteger"]:
        """Get minOkState (Pythonic accessor)."""
        return self._minOkState

    @min_ok_state.setter
    def min_ok_state(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minOkState with validation.
        
        Args:
            value: The minOkState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minOkState = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minOkState must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minOkState = value
        # EndToEndTransformationDescription holds these are profile specific and have
        # the same all E2E transformers.
        self._syncCounterInit: Optional["PositiveInteger"] = None

    @property
    def sync_counter_init(self) -> Optional["PositiveInteger"]:
        """Get syncCounterInit (Pythonic accessor)."""
        return self._syncCounterInit

    @sync_counter_init.setter
    def sync_counter_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set syncCounterInit with validation.
        
        Args:
            value: The syncCounterInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncCounterInit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"syncCounterInit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._syncCounterInit = value
        # Size of the monitoring window of state Init for the E2E.
        self._windowSizeInit: Optional["PositiveInteger"] = None

    @property
    def window_size_init(self) -> Optional["PositiveInteger"]:
        """Get windowSizeInit (Pythonic accessor)."""
        return self._windowSizeInit

    @window_size_init.setter
    def window_size_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set windowSizeInit with validation.
        
        Args:
            value: The windowSizeInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._windowSizeInit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"windowSizeInit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._windowSizeInit = value
        # Size of the monitoring window of state Valid for the E2E machine.
        self._windowSize: Optional["PositiveInteger"] = None

    @property
    def window_size(self) -> Optional["PositiveInteger"]:
        """Get windowSize (Pythonic accessor)."""
        return self._windowSize

    @window_size.setter
    def window_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set windowSize with validation.
        
        Args:
            value: The windowSize to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._windowSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"windowSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._windowSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClearFromValid(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for clearFromValid.
        
        Returns:
            The clearFromValid value
        
        Note:
            Delegates to clear_from_valid property (CODING_RULE_V2_00017)
        """
        return self.clear_from_valid  # Delegates to property

    def setClearFromValid(self, value: "Boolean") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for clearFromValid with method chaining.
        
        Args:
            value: The clearFromValid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to clear_from_valid property setter (gets validation automatically)
        """
        self.clear_from_valid = value  # Delegates to property setter
        return self

    def getDisableEndTo(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for disableEndTo.
        
        Returns:
            The disableEndTo value
        
        Note:
            Delegates to disable_end_to property (CODING_RULE_V2_00017)
        """
        return self.disable_end_to  # Delegates to property

    def setDisableEndTo(self, value: "Boolean") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for disableEndTo with method chaining.
        
        Args:
            value: The disableEndTo to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to disable_end_to property setter (gets validation automatically)
        """
        self.disable_end_to = value  # Delegates to property setter
        return self

    def getE2eProfile(self) -> "E2EProfileCompatibility":
        """
        AUTOSAR-compliant getter for e2eProfile.
        
        Returns:
            The e2eProfile value
        
        Note:
            Delegates to e2e_profile property (CODING_RULE_V2_00017)
        """
        return self.e2e_profile  # Delegates to property

    def setE2eProfile(self, value: "E2EProfileCompatibility") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for e2eProfile with method chaining.
        
        Args:
            value: The e2eProfile to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to e2e_profile property setter (gets validation automatically)
        """
        self.e2e_profile = value  # Delegates to property setter
        return self

    def getMaxDelta(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDelta.
        
        Returns:
            The maxDelta value
        
        Note:
            Delegates to max_delta property (CODING_RULE_V2_00017)
        """
        return self.max_delta  # Delegates to property

    def setMaxDelta(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for maxDelta with method chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_delta property setter (gets validation automatically)
        """
        self.max_delta = value  # Delegates to property setter
        return self

    def getMaxErrorState(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxErrorState.
        
        Returns:
            The maxErrorState value
        
        Note:
            Delegates to max_error_state property (CODING_RULE_V2_00017)
        """
        return self.max_error_state  # Delegates to property

    def setMaxErrorState(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for maxErrorState with method chaining.
        
        Args:
            value: The maxErrorState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_error_state property setter (gets validation automatically)
        """
        self.max_error_state = value  # Delegates to property setter
        return self

    def getMaxNoNewOr(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNoNewOr.
        
        Returns:
            The maxNoNewOr value
        
        Note:
            Delegates to max_no_new_or property (CODING_RULE_V2_00017)
        """
        return self.max_no_new_or  # Delegates to property

    def setMaxNoNewOr(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for maxNoNewOr with method chaining.
        
        Args:
            value: The maxNoNewOr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_no_new_or property setter (gets validation automatically)
        """
        self.max_no_new_or = value  # Delegates to property setter
        return self

    def getMinOkStateInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minOkStateInit.
        
        Returns:
            The minOkStateInit value
        
        Note:
            Delegates to min_ok_state_init property (CODING_RULE_V2_00017)
        """
        return self.min_ok_state_init  # Delegates to property

    def setMinOkStateInit(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for minOkStateInit with method chaining.
        
        Args:
            value: The minOkStateInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_ok_state_init property setter (gets validation automatically)
        """
        self.min_ok_state_init = value  # Delegates to property setter
        return self

    def getMinOkState(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minOkState.
        
        Returns:
            The minOkState value
        
        Note:
            Delegates to min_ok_state property (CODING_RULE_V2_00017)
        """
        return self.min_ok_state  # Delegates to property

    def setMinOkState(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for minOkState with method chaining.
        
        Args:
            value: The minOkState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_ok_state property setter (gets validation automatically)
        """
        self.min_ok_state = value  # Delegates to property setter
        return self

    def getSyncCounterInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for syncCounterInit.
        
        Returns:
            The syncCounterInit value
        
        Note:
            Delegates to sync_counter_init property (CODING_RULE_V2_00017)
        """
        return self.sync_counter_init  # Delegates to property

    def setSyncCounterInit(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for syncCounterInit with method chaining.
        
        Args:
            value: The syncCounterInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sync_counter_init property setter (gets validation automatically)
        """
        self.sync_counter_init = value  # Delegates to property setter
        return self

    def getWindowSizeInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for windowSizeInit.
        
        Returns:
            The windowSizeInit value
        
        Note:
            Delegates to window_size_init property (CODING_RULE_V2_00017)
        """
        return self.window_size_init  # Delegates to property

    def setWindowSizeInit(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for windowSizeInit with method chaining.
        
        Args:
            value: The windowSizeInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to window_size_init property setter (gets validation automatically)
        """
        self.window_size_init = value  # Delegates to property setter
        return self

    def getWindowSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for windowSize.
        
        Returns:
            The windowSize value
        
        Note:
            Delegates to window_size property (CODING_RULE_V2_00017)
        """
        return self.window_size  # Delegates to property

    def setWindowSize(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for windowSize with method chaining.
        
        Args:
            value: The windowSize to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to window_size property setter (gets validation automatically)
        """
        self.window_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_clear_from_valid(self, value: Optional["Boolean"]) -> "EndToEndTransformationComSpecProps":
        """
        Set clearFromValid and return self for chaining.
        
        Args:
            value: The clearFromValid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_clear_from_valid("value")
        """
        self.clear_from_valid = value  # Use property setter (gets validation)
        return self

    def with_disable_end_to(self, value: Optional["Boolean"]) -> "EndToEndTransformationComSpecProps":
        """
        Set disableEndTo and return self for chaining.
        
        Args:
            value: The disableEndTo to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_disable_end_to("value")
        """
        self.disable_end_to = value  # Use property setter (gets validation)
        return self

    def with_e2e_profile(self, value: Optional["E2EProfileCompatibility"]) -> "EndToEndTransformationComSpecProps":
        """
        Set e2eProfile and return self for chaining.
        
        Args:
            value: The e2eProfile to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_e2e_profile("value")
        """
        self.e2e_profile = value  # Use property setter (gets validation)
        return self

    def with_max_delta(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set maxDelta and return self for chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_delta("value")
        """
        self.max_delta = value  # Use property setter (gets validation)
        return self

    def with_max_error_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set maxErrorState and return self for chaining.
        
        Args:
            value: The maxErrorState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_error_state("value")
        """
        self.max_error_state = value  # Use property setter (gets validation)
        return self

    def with_max_no_new_or(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set maxNoNewOr and return self for chaining.
        
        Args:
            value: The maxNoNewOr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_no_new_or("value")
        """
        self.max_no_new_or = value  # Use property setter (gets validation)
        return self

    def with_min_ok_state_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set minOkStateInit and return self for chaining.
        
        Args:
            value: The minOkStateInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_ok_state_init("value")
        """
        self.min_ok_state_init = value  # Use property setter (gets validation)
        return self

    def with_min_ok_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set minOkState and return self for chaining.
        
        Args:
            value: The minOkState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_ok_state("value")
        """
        self.min_ok_state = value  # Use property setter (gets validation)
        return self

    def with_sync_counter_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set syncCounterInit and return self for chaining.
        
        Args:
            value: The syncCounterInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sync_counter_init("value")
        """
        self.sync_counter_init = value  # Use property setter (gets validation)
        return self

    def with_window_size_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set windowSizeInit and return self for chaining.
        
        Args:
            value: The windowSizeInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_window_size_init("value")
        """
        self.window_size_init = value  # Use property setter (gets validation)
        return self

    def with_window_size(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set windowSize and return self for chaining.
        
        Args:
            value: The windowSize to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_window_size("value")
        """
        self.window_size = value  # Use property setter (gets validation)
        return self