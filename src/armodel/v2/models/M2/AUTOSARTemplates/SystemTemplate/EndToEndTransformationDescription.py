from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationDescription


class EndToEndTransformationDescription(TransformationDescription):
    """
    EndToEndTransformationDescription holds these attributes which are profile
    specific and have the same value for all E2E transformers.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::EndToEndTransformationDescription

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 987, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 806, Classic Platform R23-11)
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
        # Offset of the counter in the Data[] array in bits.
        self._counterOffset: Optional["PositiveInteger"] = None

    @property
    def counter_offset(self) -> Optional["PositiveInteger"]:
        """Get counterOffset (Pythonic accessor)."""
        return self._counterOffset

    @counter_offset.setter
    def counter_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set counterOffset with validation.

        Args:
            value: The counterOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterOffset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"counterOffset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._counterOffset = value
        # Offset of the CRC in the Data[] array in bits.
        self._crcOffset: Optional["PositiveInteger"] = None

    @property
    def crc_offset(self) -> Optional["PositiveInteger"]:
        """Get crcOffset (Pythonic accessor)."""
        return self._crcOffset

    @crc_offset.setter
    def crc_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set crcOffset with validation.

        Args:
            value: The crcOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcOffset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"crcOffset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._crcOffset = value
        # This attribute describes the inclusion mode that is used to implicit two-byte
        # Data ID in the one-byte CRC.
        self._dataIdMode: Optional["DataIdModeEnum"] = None

    @property
    def data_id_mode(self) -> Optional["DataIdModeEnum"]:
        """Get dataIdMode (Pythonic accessor)."""
        return self._dataIdMode

    @data_id_mode.setter
    def data_id_mode(self, value: Optional["DataIdModeEnum"]) -> None:
        """
        Set dataIdMode with validation.

        Args:
            value: The dataIdMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdMode = None
            return

        if not isinstance(value, DataIdModeEnum):
            raise TypeError(
                f"dataIdMode must be DataIdModeEnum or None, got {type(value).__name__}"
            )
        self._dataIdMode = value
        # Offset of the Data ID nibble in the Data[] array in bits.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._dataIdNibble: Optional["PositiveInteger"] = None

    @property
    def data_id_nibble(self) -> Optional["PositiveInteger"]:
        """Get dataIdNibble (Pythonic accessor)."""
        return self._dataIdNibble

    @data_id_nibble.setter
    def data_id_nibble(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataIdNibble with validation.

        Args:
            value: The dataIdNibble to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdNibble = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataIdNibble must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataIdNibble = value
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
        # The maximum allowed amount of consecutive failed checks.
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
        # Offset of the E2E header in the Data[] array in bits.
        self._offset: Optional["PositiveInteger"] = None

    @property
    def offset(self) -> Optional["PositiveInteger"]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set offset with validation.

        Args:
            value: The offset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"offset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._offset = value
        # Behavior of the check functionality.
        self._profileBehaviorBehaviorEnum: Optional["EndToEndProfile"] = None

    @property
    def profile_behavior_behavior_enum(self) -> Optional["EndToEndProfile"]:
        """Get profileBehaviorBehaviorEnum (Pythonic accessor)."""
        return self._profileBehaviorBehaviorEnum

    @profile_behavior_behavior_enum.setter
    def profile_behavior_behavior_enum(self, value: Optional["EndToEndProfile"]) -> None:
        """
        Set profileBehaviorBehaviorEnum with validation.

        Args:
            value: The profileBehaviorBehaviorEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._profileBehaviorBehaviorEnum = None
            return

        if not isinstance(value, EndToEndProfile):
            raise TypeError(
                f"profileBehaviorBehaviorEnum must be EndToEndProfile or None, got {type(value).__name__}"
            )
        self._profileBehaviorBehaviorEnum = value
        # Definition of the E2E profile.
        self._profileName: Optional["NameToken"] = None

    @property
    def profile_name(self) -> Optional["NameToken"]:
        """Get profileName (Pythonic accessor)."""
        return self._profileName

    @profile_name.setter
    def profile_name(self, value: Optional["NameToken"]) -> None:
        """
        Set profileName with validation.

        Args:
            value: The profileName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._profileName = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"profileName must be NameToken or None, got {type(value).__name__}"
            )
        self._profileName = value
        # Number of checks required for validating the consistency counter that shall
        # be received with a valid counter within the allowed lock-in range) after the
        # an unexpected behavior of a received.
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
        # This attribute describes the number of upper-header bits be shifted.
        # 0 or not present: shift of upper header is NOT 0: the E2E Transformer on the
                # protect-side, takes upperHeaderBitsToShift bits from the upper buffer header
                # part generated by SOME/IP shifts them towards the lower bytes and the Data[]
                # for the length of the E2E header bytes in case of E2E Profile 4).
        # This means the is fixed - it depends on the E2E header size is configured
                # here is the number of bits that are to This option is defined because the
                # Some/IP by SOME/IP transformer shall be, due between non-protected and at the
                # same position, before E2E header.
        self._upperHeader: Optional["PositiveInteger"] = None

    @property
    def upper_header(self) -> Optional["PositiveInteger"]:
        """Get upperHeader (Pythonic accessor)."""
        return self._upperHeader

    @upper_header.setter
    def upper_header(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set upperHeader with validation.

        Args:
            value: The upperHeader to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperHeader = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"upperHeader must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._upperHeader = value
        # Size of the monitoring window of state Init for the E2E 1228 Document ID 62:
        # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
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

    def setClearFromValid(self, value: "Boolean") -> "EndToEndTransformationDescription":
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

    def getCounterOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for counterOffset.

        Returns:
            The counterOffset value

        Note:
            Delegates to counter_offset property (CODING_RULE_V2_00017)
        """
        return self.counter_offset  # Delegates to property

    def setCounterOffset(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for counterOffset with method chaining.

        Args:
            value: The counterOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_offset property setter (gets validation automatically)
        """
        self.counter_offset = value  # Delegates to property setter
        return self

    def getCrcOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for crcOffset.

        Returns:
            The crcOffset value

        Note:
            Delegates to crc_offset property (CODING_RULE_V2_00017)
        """
        return self.crc_offset  # Delegates to property

    def setCrcOffset(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for crcOffset with method chaining.

        Args:
            value: The crcOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_offset property setter (gets validation automatically)
        """
        self.crc_offset = value  # Delegates to property setter
        return self

    def getDataIdMode(self) -> "DataIdModeEnum":
        """
        AUTOSAR-compliant getter for dataIdMode.

        Returns:
            The dataIdMode value

        Note:
            Delegates to data_id_mode property (CODING_RULE_V2_00017)
        """
        return self.data_id_mode  # Delegates to property

    def setDataIdMode(self, value: "DataIdModeEnum") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for dataIdMode with method chaining.

        Args:
            value: The dataIdMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_id_mode property setter (gets validation automatically)
        """
        self.data_id_mode = value  # Delegates to property setter
        return self

    def getDataIdNibble(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataIdNibble.

        Returns:
            The dataIdNibble value

        Note:
            Delegates to data_id_nibble property (CODING_RULE_V2_00017)
        """
        return self.data_id_nibble  # Delegates to property

    def setDataIdNibble(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for dataIdNibble with method chaining.

        Args:
            value: The dataIdNibble to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_id_nibble property setter (gets validation automatically)
        """
        self.data_id_nibble = value  # Delegates to property setter
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

    def setE2eProfile(self, value: "E2EProfileCompatibility") -> "EndToEndTransformationDescription":
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

    def setMaxDelta(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def setMaxErrorState(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def setMaxNoNewOr(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def setMinOkStateInit(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def setMinOkState(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def getOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for offset with method chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Note:
            Delegates to offset property setter (gets validation automatically)
        """
        self.offset = value  # Delegates to property setter
        return self

    def getProfileBehaviorBehaviorEnum(self) -> "EndToEndProfile":
        """
        AUTOSAR-compliant getter for profileBehaviorBehaviorEnum.

        Returns:
            The profileBehaviorBehaviorEnum value

        Note:
            Delegates to profile_behavior_behavior_enum property (CODING_RULE_V2_00017)
        """
        return self.profile_behavior_behavior_enum  # Delegates to property

    def setProfileBehaviorBehaviorEnum(self, value: "EndToEndProfile") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for profileBehaviorBehaviorEnum with method chaining.

        Args:
            value: The profileBehaviorBehaviorEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to profile_behavior_behavior_enum property setter (gets validation automatically)
        """
        self.profile_behavior_behavior_enum = value  # Delegates to property setter
        return self

    def getProfileName(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for profileName.

        Returns:
            The profileName value

        Note:
            Delegates to profile_name property (CODING_RULE_V2_00017)
        """
        return self.profile_name  # Delegates to property

    def setProfileName(self, value: "NameToken") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for profileName with method chaining.

        Args:
            value: The profileName to set

        Returns:
            self for method chaining

        Note:
            Delegates to profile_name property setter (gets validation automatically)
        """
        self.profile_name = value  # Delegates to property setter
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

    def setSyncCounterInit(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def getUpperHeader(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for upperHeader.

        Returns:
            The upperHeader value

        Note:
            Delegates to upper_header property (CODING_RULE_V2_00017)
        """
        return self.upper_header  # Delegates to property

    def setUpperHeader(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for upperHeader with method chaining.

        Args:
            value: The upperHeader to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_header property setter (gets validation automatically)
        """
        self.upper_header = value  # Delegates to property setter
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

    def setWindowSizeInit(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def setWindowSize(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def with_clear_from_valid(self, value: Optional["Boolean"]) -> "EndToEndTransformationDescription":
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

    def with_counter_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set counterOffset and return self for chaining.

        Args:
            value: The counterOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_offset("value")
        """
        self.counter_offset = value  # Use property setter (gets validation)
        return self

    def with_crc_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set crcOffset and return self for chaining.

        Args:
            value: The crcOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_offset("value")
        """
        self.crc_offset = value  # Use property setter (gets validation)
        return self

    def with_data_id_mode(self, value: Optional["DataIdModeEnum"]) -> "EndToEndTransformationDescription":
        """
        Set dataIdMode and return self for chaining.

        Args:
            value: The dataIdMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_id_mode("value")
        """
        self.data_id_mode = value  # Use property setter (gets validation)
        return self

    def with_data_id_nibble(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set dataIdNibble and return self for chaining.

        Args:
            value: The dataIdNibble to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_id_nibble("value")
        """
        self.data_id_nibble = value  # Use property setter (gets validation)
        return self

    def with_e2e_profile(self, value: Optional["E2EProfileCompatibility"]) -> "EndToEndTransformationDescription":
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

    def with_max_delta(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_max_error_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_max_no_new_or(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_min_ok_state_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_min_ok_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set offset and return self for chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_profile_behavior_behavior_enum(self, value: Optional["EndToEndProfile"]) -> "EndToEndTransformationDescription":
        """
        Set profileBehaviorBehaviorEnum and return self for chaining.

        Args:
            value: The profileBehaviorBehaviorEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_profile_behavior_behavior_enum("value")
        """
        self.profile_behavior_behavior_enum = value  # Use property setter (gets validation)
        return self

    def with_profile_name(self, value: Optional["NameToken"]) -> "EndToEndTransformationDescription":
        """
        Set profileName and return self for chaining.

        Args:
            value: The profileName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_profile_name("value")
        """
        self.profile_name = value  # Use property setter (gets validation)
        return self

    def with_sync_counter_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_upper_header(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set upperHeader and return self for chaining.

        Args:
            value: The upperHeader to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_header("value")
        """
        self.upper_header = value  # Use property setter (gets validation)
        return self

    def with_window_size_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_window_size(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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
