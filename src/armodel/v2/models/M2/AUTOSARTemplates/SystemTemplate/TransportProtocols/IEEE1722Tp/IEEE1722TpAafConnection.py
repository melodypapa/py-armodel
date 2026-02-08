from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpAvConnection,
)


class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp AAF connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 642, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the AAF AES3 stream aes3_data_type reference.
        self._aafAes3Data: Optional["IEEE1722TpAafAes3"] = None

    @property
    def aaf_aes3_data(self) -> Optional["IEEE1722TpAafAes3"]:
        """Get aafAes3Data (Pythonic accessor)."""
        return self._aafAes3Data

    @aaf_aes3_data.setter
    def aaf_aes3_data(self, value: Optional["IEEE1722TpAafAes3"]) -> None:
        """
        Set aafAes3Data with validation.

        Args:
            value: The aafAes3Data to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aafAes3Data = None
            return

        if not isinstance(value, IEEE1722TpAafAes3):
            raise TypeError(
                f"aafAes3Data must be IEEE1722TpAafAes3 or None, got {type(value).__name__}"
            )
        self._aafAes3Data = value
        # Definition of the AAF stream format.
        self._aafFormatEnum: Optional["IEEE1722TpAafFormat"] = None

    @property
    def aaf_format_enum(self) -> Optional["IEEE1722TpAafFormat"]:
        """Get aafFormatEnum (Pythonic accessor)."""
        return self._aafFormatEnum

    @aaf_format_enum.setter
    def aaf_format_enum(self, value: Optional["IEEE1722TpAafFormat"]) -> None:
        """
        Set aafFormatEnum with validation.

        Args:
            value: The aafFormatEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aafFormatEnum = None
            return

        if not isinstance(value, IEEE1722TpAafFormat):
            raise TypeError(
                f"aafFormatEnum must be IEEE1722TpAafFormat or None, got {type(value).__name__}"
            )
        self._aafFormatEnum = value
        # Definition of the AAF stream nominal sample / frame rate.
        # an AAF PCM stream this is the nominal sample rate.
        # AAF AES3 stream this is the nominal frame rate.
        self._aafNominalRate: Optional["IEEE1722TpAaf"] = None

    @property
    def aaf_nominal_rate(self) -> Optional["IEEE1722TpAaf"]:
        """Get aafNominalRate (Pythonic accessor)."""
        return self._aafNominalRate

    @aaf_nominal_rate.setter
    def aaf_nominal_rate(self, value: Optional["IEEE1722TpAaf"]) -> None:
        """
        Set aafNominalRate with validation.

        Args:
            value: The aafNominalRate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aafNominalRate = None
            return

        if not isinstance(value, IEEE1722TpAaf):
            raise TypeError(
                f"aafNominalRate must be IEEE1722TpAaf or None, got {type(value).__name__}"
            )
        self._aafNominalRate = value
        # Definition of the AAF AES3 aes3_data_type_h default.
        self._aes3DataTypeH: Optional["PositiveInteger"] = None

    @property
    def aes3_data_type_h(self) -> Optional["PositiveInteger"]:
        """Get aes3DataTypeH (Pythonic accessor)."""
        return self._aes3DataTypeH

    @aes3_data_type_h.setter
    def aes3_data_type_h(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set aes3DataTypeH with validation.

        Args:
            value: The aes3DataTypeH to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aes3DataTypeH = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"aes3DataTypeH must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._aes3DataTypeH = value
        # Definition of the AAF AES3 aes3_data_type_l default.
        self._aes3DataTypeL: Optional["PositiveInteger"] = None

    @property
    def aes3_data_type_l(self) -> Optional["PositiveInteger"]:
        """Get aes3DataTypeL (Pythonic accessor)."""
        return self._aes3DataTypeL

    @aes3_data_type_l.setter
    def aes3_data_type_l(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set aes3DataTypeL with validation.

        Args:
            value: The aes3DataTypeL to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aes3DataTypeL = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"aes3DataTypeL must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._aes3DataTypeL = value
        # Definition of the AAF PCM stream channels_per_frame.
        # 1: mono, 2: stereo, 8: 7.
        # 1 multicannel.
        self._channelsPer: Optional["PositiveInteger"] = None

    @property
    def channels_per(self) -> Optional["PositiveInteger"]:
        """Get channelsPer (Pythonic accessor)."""
        return self._channelsPer

    @channels_per.setter
    def channels_per(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set channelsPer with validation.

        Args:
            value: The channelsPer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channelsPer = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"channelsPer must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._channelsPer = value
        # Definition of a value to be used for the 4-bit "evt" field.
        # atp.
        # Status=candidate 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._eventDefault: Optional["PositiveInteger"] = None

    @property
    def event_default(self) -> Optional["PositiveInteger"]:
        """Get eventDefault (Pythonic accessor)."""
        return self._eventDefault

    @event_default.setter
    def event_default(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set eventDefault with validation.

        Args:
            value: The eventDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventDefault = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"eventDefault must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._eventDefault = value
        # Definition of the AAF PCM stream bit_depth.
        # 24, 32.
        self._pcmBitDepth: Optional["PositiveInteger"] = None

    @property
    def pcm_bit_depth(self) -> Optional["PositiveInteger"]:
        """Get pcmBitDepth (Pythonic accessor)."""
        return self._pcmBitDepth

    @pcm_bit_depth.setter
    def pcm_bit_depth(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pcmBitDepth with validation.

        Args:
            value: The pcmBitDepth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pcmBitDepth = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pcmBitDepth must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pcmBitDepth = value
        # Defines whether the "sp" (sparse timestamp) shall be Normal operation,
        # timestamp in every AAF mode, timestamp in every eighth AAF.
        self._sparse: Optional["Boolean"] = None

    @property
    def sparse(self) -> Optional["Boolean"]:
        """Get sparse (Pythonic accessor)."""
        return self._sparse

    @sparse.setter
    def sparse(self, value: Optional["Boolean"]) -> None:
        """
        Set sparse with validation.

        Args:
            value: The sparse to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sparse = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"sparse must be Boolean or None, got {type(value).__name__}"
            )
        self._sparse = value
        # AAF AES3 stream streams_per_frame.
        # atp.
        # Status=candidate.
        self._streamsPer: Optional["PositiveInteger"] = None

    @property
    def streams_per(self) -> Optional["PositiveInteger"]:
        """Get streamsPer (Pythonic accessor)."""
        return self._streamsPer

    @streams_per.setter
    def streams_per(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set streamsPer with validation.

        Args:
            value: The streamsPer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamsPer = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"streamsPer must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._streamsPer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAafAes3Data(self) -> "IEEE1722TpAafAes3":
        """
        AUTOSAR-compliant getter for aafAes3Data.

        Returns:
            The aafAes3Data value

        Note:
            Delegates to aaf_aes3_data property (CODING_RULE_V2_00017)
        """
        return self.aaf_aes3_data  # Delegates to property

    def setAafAes3Data(self, value: "IEEE1722TpAafAes3") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for aafAes3Data with method chaining.

        Args:
            value: The aafAes3Data to set

        Returns:
            self for method chaining

        Note:
            Delegates to aaf_aes3_data property setter (gets validation automatically)
        """
        self.aaf_aes3_data = value  # Delegates to property setter
        return self

    def getAafFormatEnum(self) -> "IEEE1722TpAafFormat":
        """
        AUTOSAR-compliant getter for aafFormatEnum.

        Returns:
            The aafFormatEnum value

        Note:
            Delegates to aaf_format_enum property (CODING_RULE_V2_00017)
        """
        return self.aaf_format_enum  # Delegates to property

    def setAafFormatEnum(self, value: "IEEE1722TpAafFormat") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for aafFormatEnum with method chaining.

        Args:
            value: The aafFormatEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to aaf_format_enum property setter (gets validation automatically)
        """
        self.aaf_format_enum = value  # Delegates to property setter
        return self

    def getAafNominalRate(self) -> "IEEE1722TpAaf":
        """
        AUTOSAR-compliant getter for aafNominalRate.

        Returns:
            The aafNominalRate value

        Note:
            Delegates to aaf_nominal_rate property (CODING_RULE_V2_00017)
        """
        return self.aaf_nominal_rate  # Delegates to property

    def setAafNominalRate(self, value: "IEEE1722TpAaf") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for aafNominalRate with method chaining.

        Args:
            value: The aafNominalRate to set

        Returns:
            self for method chaining

        Note:
            Delegates to aaf_nominal_rate property setter (gets validation automatically)
        """
        self.aaf_nominal_rate = value  # Delegates to property setter
        return self

    def getAes3DataTypeH(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for aes3DataTypeH.

        Returns:
            The aes3DataTypeH value

        Note:
            Delegates to aes3_data_type_h property (CODING_RULE_V2_00017)
        """
        return self.aes3_data_type_h  # Delegates to property

    def setAes3DataTypeH(self, value: "PositiveInteger") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for aes3DataTypeH with method chaining.

        Args:
            value: The aes3DataTypeH to set

        Returns:
            self for method chaining

        Note:
            Delegates to aes3_data_type_h property setter (gets validation automatically)
        """
        self.aes3_data_type_h = value  # Delegates to property setter
        return self

    def getAes3DataTypeL(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for aes3DataTypeL.

        Returns:
            The aes3DataTypeL value

        Note:
            Delegates to aes3_data_type_l property (CODING_RULE_V2_00017)
        """
        return self.aes3_data_type_l  # Delegates to property

    def setAes3DataTypeL(self, value: "PositiveInteger") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for aes3DataTypeL with method chaining.

        Args:
            value: The aes3DataTypeL to set

        Returns:
            self for method chaining

        Note:
            Delegates to aes3_data_type_l property setter (gets validation automatically)
        """
        self.aes3_data_type_l = value  # Delegates to property setter
        return self

    def getChannelsPer(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for channelsPer.

        Returns:
            The channelsPer value

        Note:
            Delegates to channels_per property (CODING_RULE_V2_00017)
        """
        return self.channels_per  # Delegates to property

    def setChannelsPer(self, value: "PositiveInteger") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for channelsPer with method chaining.

        Args:
            value: The channelsPer to set

        Returns:
            self for method chaining

        Note:
            Delegates to channels_per property setter (gets validation automatically)
        """
        self.channels_per = value  # Delegates to property setter
        return self

    def getEventDefault(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for eventDefault.

        Returns:
            The eventDefault value

        Note:
            Delegates to event_default property (CODING_RULE_V2_00017)
        """
        return self.event_default  # Delegates to property

    def setEventDefault(self, value: "PositiveInteger") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for eventDefault with method chaining.

        Args:
            value: The eventDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_default property setter (gets validation automatically)
        """
        self.event_default = value  # Delegates to property setter
        return self

    def getPcmBitDepth(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pcmBitDepth.

        Returns:
            The pcmBitDepth value

        Note:
            Delegates to pcm_bit_depth property (CODING_RULE_V2_00017)
        """
        return self.pcm_bit_depth  # Delegates to property

    def setPcmBitDepth(self, value: "PositiveInteger") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for pcmBitDepth with method chaining.

        Args:
            value: The pcmBitDepth to set

        Returns:
            self for method chaining

        Note:
            Delegates to pcm_bit_depth property setter (gets validation automatically)
        """
        self.pcm_bit_depth = value  # Delegates to property setter
        return self

    def getSparse(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for sparse.

        Returns:
            The sparse value

        Note:
            Delegates to sparse property (CODING_RULE_V2_00017)
        """
        return self.sparse  # Delegates to property

    def setSparse(self, value: "Boolean") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for sparse with method chaining.

        Args:
            value: The sparse to set

        Returns:
            self for method chaining

        Note:
            Delegates to sparse property setter (gets validation automatically)
        """
        self.sparse = value  # Delegates to property setter
        return self

    def getStreamsPer(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for streamsPer.

        Returns:
            The streamsPer value

        Note:
            Delegates to streams_per property (CODING_RULE_V2_00017)
        """
        return self.streams_per  # Delegates to property

    def setStreamsPer(self, value: "PositiveInteger") -> "IEEE1722TpAafConnection":
        """
        AUTOSAR-compliant setter for streamsPer with method chaining.

        Args:
            value: The streamsPer to set

        Returns:
            self for method chaining

        Note:
            Delegates to streams_per property setter (gets validation automatically)
        """
        self.streams_per = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aaf_aes3_data(self, value: Optional["IEEE1722TpAafAes3"]) -> "IEEE1722TpAafConnection":
        """
        Set aafAes3Data and return self for chaining.

        Args:
            value: The aafAes3Data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aaf_aes3_data("value")
        """
        self.aaf_aes3_data = value  # Use property setter (gets validation)
        return self

    def with_aaf_format_enum(self, value: Optional["IEEE1722TpAafFormat"]) -> "IEEE1722TpAafConnection":
        """
        Set aafFormatEnum and return self for chaining.

        Args:
            value: The aafFormatEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aaf_format_enum("value")
        """
        self.aaf_format_enum = value  # Use property setter (gets validation)
        return self

    def with_aaf_nominal_rate(self, value: Optional["IEEE1722TpAaf"]) -> "IEEE1722TpAafConnection":
        """
        Set aafNominalRate and return self for chaining.

        Args:
            value: The aafNominalRate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aaf_nominal_rate("value")
        """
        self.aaf_nominal_rate = value  # Use property setter (gets validation)
        return self

    def with_aes3_data_type_h(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAafConnection":
        """
        Set aes3DataTypeH and return self for chaining.

        Args:
            value: The aes3DataTypeH to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aes3_data_type_h("value")
        """
        self.aes3_data_type_h = value  # Use property setter (gets validation)
        return self

    def with_aes3_data_type_l(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAafConnection":
        """
        Set aes3DataTypeL and return self for chaining.

        Args:
            value: The aes3DataTypeL to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aes3_data_type_l("value")
        """
        self.aes3_data_type_l = value  # Use property setter (gets validation)
        return self

    def with_channels_per(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAafConnection":
        """
        Set channelsPer and return self for chaining.

        Args:
            value: The channelsPer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channels_per("value")
        """
        self.channels_per = value  # Use property setter (gets validation)
        return self

    def with_event_default(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAafConnection":
        """
        Set eventDefault and return self for chaining.

        Args:
            value: The eventDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_default("value")
        """
        self.event_default = value  # Use property setter (gets validation)
        return self

    def with_pcm_bit_depth(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAafConnection":
        """
        Set pcmBitDepth and return self for chaining.

        Args:
            value: The pcmBitDepth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pcm_bit_depth("value")
        """
        self.pcm_bit_depth = value  # Use property setter (gets validation)
        return self

    def with_sparse(self, value: Optional["Boolean"]) -> "IEEE1722TpAafConnection":
        """
        Set sparse and return self for chaining.

        Args:
            value: The sparse to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sparse("value")
        """
        self.sparse = value  # Use property setter (gets validation)
        return self

    def with_streams_per(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAafConnection":
        """
        Set streamsPer and return self for chaining.

        Args:
            value: The streamsPer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_streams_per("value")
        """
        self.streams_per = value  # Use property setter (gets validation)
        return self
