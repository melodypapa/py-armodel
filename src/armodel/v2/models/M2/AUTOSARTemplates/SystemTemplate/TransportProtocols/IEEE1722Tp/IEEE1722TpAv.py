"""
AUTOSAR Package - IEEE1722TpAv

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
"""


from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.__init__ import (
    IEEE1722TpAvConnection,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAaf,
    IEEE1722TpAafAes3,
    IEEE1722TpAafFormat,
    IEEE1722TpCrfPull,
    IEEE1722TpCrfType,
    IEEE1722TpRvfColor,
    IEEE1722TpRvfFrame,
    IEEE1722TpRvfPixel,
)



class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp CRF connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv::IEEE1722TpCrfConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 640, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CRF base frequency in Hz.
        self._baseFrequency: Optional[PositiveInteger] = None

    @property
    def base_frequency(self) -> Optional[PositiveInteger]:
        """Get baseFrequency (Pythonic accessor)."""
        return self._baseFrequency

    @base_frequency.setter
    def base_frequency(self, value: Optional[PositiveInteger]) -> None:
        """
        Set baseFrequency with validation.

        Args:
            value: The baseFrequency to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseFrequency = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"baseFrequency must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._baseFrequency = value
        self._crfPullEnum: Optional[IEEE1722TpCrfPull] = None

    @property
    def crf_pull_enum(self) -> Optional[IEEE1722TpCrfPull]:
        """Get crfPullEnum (Pythonic accessor)."""
        return self._crfPullEnum

    @crf_pull_enum.setter
    def crf_pull_enum(self, value: Optional[IEEE1722TpCrfPull]) -> None:
        """
        Set crfPullEnum with validation.

        Args:
            value: The crfPullEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crfPullEnum = None
            return

        if not isinstance(value, IEEE1722TpCrfPull):
            raise TypeError(
                f"crfPullEnum must be IEEE1722TpCrfPull or None, got {type(value).__name__}"
            )
        self._crfPullEnum = value
        self._crfTypeEnum: Optional[IEEE1722TpCrfType] = None

    @property
    def crf_type_enum(self) -> Optional[IEEE1722TpCrfType]:
        """Get crfTypeEnum (Pythonic accessor)."""
        return self._crfTypeEnum

    @crf_type_enum.setter
    def crf_type_enum(self, value: Optional[IEEE1722TpCrfType]) -> None:
        """
        Set crfTypeEnum with validation.

        Args:
            value: The crfTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crfTypeEnum = None
            return

        if not isinstance(value, IEEE1722TpCrfType):
            raise TypeError(
                f"crfTypeEnum must be IEEE1722TpCrfType or None, got {type(value).__name__}"
            )
        self._crfTypeEnum = value
        # atp.
        # Status=candidate.
        self._frameSync: Optional[Boolean] = None

    @property
    def frame_sync(self) -> Optional[Boolean]:
        """Get frameSync (Pythonic accessor)."""
        return self._frameSync

    @frame_sync.setter
    def frame_sync(self, value: Optional[Boolean]) -> None:
        """
        Set frameSync with validation.

        Args:
            value: The frameSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frameSync = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"frameSync must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._frameSync = value
        # atp.
        # Status=candidate.
        self._timestamp: Optional[PositiveInteger] = None

    @property
    def timestamp(self) -> Optional[PositiveInteger]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional[PositiveInteger]) -> None:
        """
        Set timestamp with validation.

        Args:
            value: The timestamp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestamp = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timestamp must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timestamp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseFrequency(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for baseFrequency.

        Returns:
            The baseFrequency value

        Note:
            Delegates to base_frequency property (CODING_RULE_V2_00017)
        """
        return self.base_frequency  # Delegates to property

    def setBaseFrequency(self, value: PositiveInteger) -> IEEE1722TpCrfConnection:
        """
        AUTOSAR-compliant setter for baseFrequency with method chaining.

        Args:
            value: The baseFrequency to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_frequency property setter (gets validation automatically)
        """
        self.base_frequency = value  # Delegates to property setter
        return self

    def getCrfPullEnum(self) -> "IEEE1722TpCrfPull":
        """
        AUTOSAR-compliant getter for crfPullEnum.

        Returns:
            The crfPullEnum value

        Note:
            Delegates to crf_pull_enum property (CODING_RULE_V2_00017)
        """
        return self.crf_pull_enum  # Delegates to property

    def setCrfPullEnum(self, value: "IEEE1722TpCrfPull") -> IEEE1722TpCrfConnection:
        """
        AUTOSAR-compliant setter for crfPullEnum with method chaining.

        Args:
            value: The crfPullEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to crf_pull_enum property setter (gets validation automatically)
        """
        self.crf_pull_enum = value  # Delegates to property setter
        return self

    def getCrfTypeEnum(self) -> "IEEE1722TpCrfType":
        """
        AUTOSAR-compliant getter for crfTypeEnum.

        Returns:
            The crfTypeEnum value

        Note:
            Delegates to crf_type_enum property (CODING_RULE_V2_00017)
        """
        return self.crf_type_enum  # Delegates to property

    def setCrfTypeEnum(self, value: "IEEE1722TpCrfType") -> IEEE1722TpCrfConnection:
        """
        AUTOSAR-compliant setter for crfTypeEnum with method chaining.

        Args:
            value: The crfTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to crf_type_enum property setter (gets validation automatically)
        """
        self.crf_type_enum = value  # Delegates to property setter
        return self

    def getFrameSync(self) -> Boolean:
        """
        AUTOSAR-compliant getter for frameSync.

        Returns:
            The frameSync value

        Note:
            Delegates to frame_sync property (CODING_RULE_V2_00017)
        """
        return self.frame_sync  # Delegates to property

    def setFrameSync(self, value: Boolean) -> IEEE1722TpCrfConnection:
        """
        AUTOSAR-compliant setter for frameSync with method chaining.

        Args:
            value: The frameSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_sync property setter (gets validation automatically)
        """
        self.frame_sync = value  # Delegates to property setter
        return self

    def getTimestamp(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for timestamp.

        Returns:
            The timestamp value

        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: PositiveInteger) -> IEEE1722TpCrfConnection:
        """
        AUTOSAR-compliant setter for timestamp with method chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_frequency(self, value: Optional[PositiveInteger]) -> IEEE1722TpCrfConnection:
        """
        Set baseFrequency and return self for chaining.

        Args:
            value: The baseFrequency to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_frequency("value")
        """
        self.base_frequency = value  # Use property setter (gets validation)
        return self

    def with_crf_pull_enum(self, value: Optional[IEEE1722TpCrfPull]) -> IEEE1722TpCrfConnection:
        """
        Set crfPullEnum and return self for chaining.

        Args:
            value: The crfPullEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crf_pull_enum("value")
        """
        self.crf_pull_enum = value  # Use property setter (gets validation)
        return self

    def with_crf_type_enum(self, value: Optional[IEEE1722TpCrfType]) -> IEEE1722TpCrfConnection:
        """
        Set crfTypeEnum and return self for chaining.

        Args:
            value: The crfTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crf_type_enum("value")
        """
        self.crf_type_enum = value  # Use property setter (gets validation)
        return self

    def with_frame_sync(self, value: Optional[Boolean]) -> IEEE1722TpCrfConnection:
        """
        Set frameSync and return self for chaining.

        Args:
            value: The frameSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_sync("value")
        """
        self.frame_sync = value  # Use property setter (gets validation)
        return self

    def with_timestamp(self, value: Optional[PositiveInteger]) -> IEEE1722TpCrfConnection:
        """
        Set timestamp and return self for chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value  # Use property setter (gets validation)
        return self



class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp AAF connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv::IEEE1722TpAafConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 642, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the AAF AES3 stream aes3_data_type reference.
        self._aafAes3Data: Optional[IEEE1722TpAafAes3] = None

    @property
    def aaf_aes3_data(self) -> Optional[IEEE1722TpAafAes3]:
        """Get aafAes3Data (Pythonic accessor)."""
        return self._aafAes3Data

    @aaf_aes3_data.setter
    def aaf_aes3_data(self, value: Optional[IEEE1722TpAafAes3]) -> None:
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
        self._aafFormatEnum: Optional[IEEE1722TpAafFormat] = None

    @property
    def aaf_format_enum(self) -> Optional[IEEE1722TpAafFormat]:
        """Get aafFormatEnum (Pythonic accessor)."""
        return self._aafFormatEnum

    @aaf_format_enum.setter
    def aaf_format_enum(self, value: Optional[IEEE1722TpAafFormat]) -> None:
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
        # an AAF PCM stream this is the nominal sample rate.
        # AAF AES3 stream this is the nominal frame rate.
        self._aafNominalRate: Optional[IEEE1722TpAaf] = None

    @property
    def aaf_nominal_rate(self) -> Optional[IEEE1722TpAaf]:
        """Get aafNominalRate (Pythonic accessor)."""
        return self._aafNominalRate

    @aaf_nominal_rate.setter
    def aaf_nominal_rate(self, value: Optional[IEEE1722TpAaf]) -> None:
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
        self._aes3DataTypeH: Optional[PositiveInteger] = None

    @property
    def aes3_data_type_h(self) -> Optional[PositiveInteger]:
        """Get aes3DataTypeH (Pythonic accessor)."""
        return self._aes3DataTypeH

    @aes3_data_type_h.setter
    def aes3_data_type_h(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"aes3DataTypeH must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._aes3DataTypeH = value
        # Definition of the AAF AES3 aes3_data_type_l default.
        self._aes3DataTypeL: Optional[PositiveInteger] = None

    @property
    def aes3_data_type_l(self) -> Optional[PositiveInteger]:
        """Get aes3DataTypeL (Pythonic accessor)."""
        return self._aes3DataTypeL

    @aes3_data_type_l.setter
    def aes3_data_type_l(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"aes3DataTypeL must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._aes3DataTypeL = value
        # Definition of the AAF PCM stream channels_per_frame.
        # 1: mono, 2: stereo, 8: 7.
        # 1 multicannel.
        self._channelsPer: Optional[PositiveInteger] = None

    @property
    def channels_per(self) -> Optional[PositiveInteger]:
        """Get channelsPer (Pythonic accessor)."""
        return self._channelsPer

    @channels_per.setter
    def channels_per(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"channelsPer must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._channelsPer = value
        # atp.
        # Status=candidate 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._eventDefault: Optional[PositiveInteger] = None

    @property
    def event_default(self) -> Optional[PositiveInteger]:
        """Get eventDefault (Pythonic accessor)."""
        return self._eventDefault

    @event_default.setter
    def event_default(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"eventDefault must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._eventDefault = value
        # 24, 32.
        self._pcmBitDepth: Optional[PositiveInteger] = None

    @property
    def pcm_bit_depth(self) -> Optional[PositiveInteger]:
        """Get pcmBitDepth (Pythonic accessor)."""
        return self._pcmBitDepth

    @pcm_bit_depth.setter
    def pcm_bit_depth(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pcmBitDepth must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pcmBitDepth = value
        # timestamp in every AAF mode, timestamp in every eighth AAF.
        self._sparse: Optional[Boolean] = None

    @property
    def sparse(self) -> Optional[Boolean]:
        """Get sparse (Pythonic accessor)."""
        return self._sparse

    @sparse.setter
    def sparse(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"sparse must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._sparse = value
        # atp.
        # Status=candidate.
        self._streamsPer: Optional[PositiveInteger] = None

    @property
    def streams_per(self) -> Optional[PositiveInteger]:
        """Get streamsPer (Pythonic accessor)."""
        return self._streamsPer

    @streams_per.setter
    def streams_per(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"streamsPer must be PositiveInteger or str or None, got {type(value).__name__}"
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

    def setAafAes3Data(self, value: "IEEE1722TpAafAes3") -> IEEE1722TpAafConnection:
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

    def setAafFormatEnum(self, value: "IEEE1722TpAafFormat") -> IEEE1722TpAafConnection:
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

    def setAafNominalRate(self, value: "IEEE1722TpAaf") -> IEEE1722TpAafConnection:
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

    def getAes3DataTypeH(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for aes3DataTypeH.

        Returns:
            The aes3DataTypeH value

        Note:
            Delegates to aes3_data_type_h property (CODING_RULE_V2_00017)
        """
        return self.aes3_data_type_h  # Delegates to property

    def setAes3DataTypeH(self, value: PositiveInteger) -> IEEE1722TpAafConnection:
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

    def getAes3DataTypeL(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for aes3DataTypeL.

        Returns:
            The aes3DataTypeL value

        Note:
            Delegates to aes3_data_type_l property (CODING_RULE_V2_00017)
        """
        return self.aes3_data_type_l  # Delegates to property

    def setAes3DataTypeL(self, value: PositiveInteger) -> IEEE1722TpAafConnection:
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

    def getChannelsPer(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for channelsPer.

        Returns:
            The channelsPer value

        Note:
            Delegates to channels_per property (CODING_RULE_V2_00017)
        """
        return self.channels_per  # Delegates to property

    def setChannelsPer(self, value: PositiveInteger) -> IEEE1722TpAafConnection:
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

    def getEventDefault(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for eventDefault.

        Returns:
            The eventDefault value

        Note:
            Delegates to event_default property (CODING_RULE_V2_00017)
        """
        return self.event_default  # Delegates to property

    def setEventDefault(self, value: PositiveInteger) -> IEEE1722TpAafConnection:
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

    def getPcmBitDepth(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pcmBitDepth.

        Returns:
            The pcmBitDepth value

        Note:
            Delegates to pcm_bit_depth property (CODING_RULE_V2_00017)
        """
        return self.pcm_bit_depth  # Delegates to property

    def setPcmBitDepth(self, value: PositiveInteger) -> IEEE1722TpAafConnection:
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

    def getSparse(self) -> Boolean:
        """
        AUTOSAR-compliant getter for sparse.

        Returns:
            The sparse value

        Note:
            Delegates to sparse property (CODING_RULE_V2_00017)
        """
        return self.sparse  # Delegates to property

    def setSparse(self, value: Boolean) -> IEEE1722TpAafConnection:
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

    def getStreamsPer(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for streamsPer.

        Returns:
            The streamsPer value

        Note:
            Delegates to streams_per property (CODING_RULE_V2_00017)
        """
        return self.streams_per  # Delegates to property

    def setStreamsPer(self, value: PositiveInteger) -> IEEE1722TpAafConnection:
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

    def with_aaf_aes3_data(self, value: Optional[IEEE1722TpAafAes3]) -> IEEE1722TpAafConnection:
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

    def with_aaf_format_enum(self, value: Optional[IEEE1722TpAafFormat]) -> IEEE1722TpAafConnection:
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

    def with_aaf_nominal_rate(self, value: Optional[IEEE1722TpAaf]) -> IEEE1722TpAafConnection:
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

    def with_aes3_data_type_h(self, value: Optional[PositiveInteger]) -> IEEE1722TpAafConnection:
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

    def with_aes3_data_type_l(self, value: Optional[PositiveInteger]) -> IEEE1722TpAafConnection:
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

    def with_channels_per(self, value: Optional[PositiveInteger]) -> IEEE1722TpAafConnection:
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

    def with_event_default(self, value: Optional[PositiveInteger]) -> IEEE1722TpAafConnection:
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

    def with_pcm_bit_depth(self, value: Optional[PositiveInteger]) -> IEEE1722TpAafConnection:
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

    def with_sparse(self, value: Optional[Boolean]) -> IEEE1722TpAafConnection:
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

    def with_streams_per(self, value: Optional[PositiveInteger]) -> IEEE1722TpAafConnection:
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



class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp IIDC connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv::IEEE1722TpIidcConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 648, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the IIDC channel.
        self._iidcChannel: Optional[PositiveInteger] = None

    @property
    def iidc_channel(self) -> Optional[PositiveInteger]:
        """Get iidcChannel (Pythonic accessor)."""
        return self._iidcChannel

    @iidc_channel.setter
    def iidc_channel(self, value: Optional[PositiveInteger]) -> None:
        """
        Set iidcChannel with validation.

        Args:
            value: The iidcChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcChannel = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"iidcChannel must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._iidcChannel = value
        # atp.
        # Status=candidate.
        self._iidcDataBlock: Optional[PositiveInteger] = None

    @property
    def iidc_data_block(self) -> Optional[PositiveInteger]:
        """Get iidcDataBlock (Pythonic accessor)."""
        return self._iidcDataBlock

    @iidc_data_block.setter
    def iidc_data_block(self, value: Optional[PositiveInteger]) -> None:
        """
        Set iidcDataBlock with validation.

        Args:
            value: The iidcDataBlock to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcDataBlock = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"iidcDataBlock must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._iidcDataBlock = value
        # atp.
        # Status=candidate.
        self._iidcFraction: Optional[PositiveInteger] = None

    @property
    def iidc_fraction(self) -> Optional[PositiveInteger]:
        """Get iidcFraction (Pythonic accessor)."""
        return self._iidcFraction

    @iidc_fraction.setter
    def iidc_fraction(self, value: Optional[PositiveInteger]) -> None:
        """
        Set iidcFraction with validation.

        Args:
            value: The iidcFraction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcFraction = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"iidcFraction must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._iidcFraction = value
        # atp.
        # Status=candidate.
        self._iidcSource: Optional[Boolean] = None

    @property
    def iidc_source(self) -> Optional[Boolean]:
        """Get iidcSource (Pythonic accessor)."""
        return self._iidcSource

    @iidc_source.setter
    def iidc_source(self, value: Optional[Boolean]) -> None:
        """
        Set iidcSource with validation.

        Args:
            value: The iidcSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcSource = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"iidcSource must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._iidcSource = value
        # atp.
        # Status=candidate.
        self._iidcStream: Optional[PositiveInteger] = None

    @property
    def iidc_stream(self) -> Optional[PositiveInteger]:
        """Get iidcStream (Pythonic accessor)."""
        return self._iidcStream

    @iidc_stream.setter
    def iidc_stream(self, value: Optional[PositiveInteger]) -> None:
        """
        Set iidcStream with validation.

        Args:
            value: The iidcStream to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcStream = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"iidcStream must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._iidcStream = value
        self._iidcSy: Optional[PositiveInteger] = None

    @property
    def iidc_sy(self) -> Optional[PositiveInteger]:
        """Get iidcSy (Pythonic accessor)."""
        return self._iidcSy

    @iidc_sy.setter
    def iidc_sy(self, value: Optional[PositiveInteger]) -> None:
        """
        Set iidcSy with validation.

        Args:
            value: The iidcSy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcSy = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"iidcSy must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._iidcSy = value
        self._iidcTag: Optional[PositiveInteger] = None

    @property
    def iidc_tag(self) -> Optional[PositiveInteger]:
        """Get iidcTag (Pythonic accessor)."""
        return self._iidcTag

    @iidc_tag.setter
    def iidc_tag(self, value: Optional[PositiveInteger]) -> None:
        """
        Set iidcTag with validation.

        Args:
            value: The iidcTag to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcTag = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"iidcTag must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._iidcTag = value
        self._iidcTCode: Optional[PositiveInteger] = None

    @property
    def iidc_t_code(self) -> Optional[PositiveInteger]:
        """Get iidcTCode (Pythonic accessor)."""
        return self._iidcTCode

    @iidc_t_code.setter
    def iidc_t_code(self, value: Optional[PositiveInteger]) -> None:
        """
        Set iidcTCode with validation.

        Args:
            value: The iidcTCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iidcTCode = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"iidcTCode must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._iidcTCode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIidcChannel(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for iidcChannel.

        Returns:
            The iidcChannel value

        Note:
            Delegates to iidc_channel property (CODING_RULE_V2_00017)
        """
        return self.iidc_channel  # Delegates to property

    def setIidcChannel(self, value: PositiveInteger) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcChannel with method chaining.

        Args:
            value: The iidcChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_channel property setter (gets validation automatically)
        """
        self.iidc_channel = value  # Delegates to property setter
        return self

    def getIidcDataBlock(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for iidcDataBlock.

        Returns:
            The iidcDataBlock value

        Note:
            Delegates to iidc_data_block property (CODING_RULE_V2_00017)
        """
        return self.iidc_data_block  # Delegates to property

    def setIidcDataBlock(self, value: PositiveInteger) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcDataBlock with method chaining.

        Args:
            value: The iidcDataBlock to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_data_block property setter (gets validation automatically)
        """
        self.iidc_data_block = value  # Delegates to property setter
        return self

    def getIidcFraction(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for iidcFraction.

        Returns:
            The iidcFraction value

        Note:
            Delegates to iidc_fraction property (CODING_RULE_V2_00017)
        """
        return self.iidc_fraction  # Delegates to property

    def setIidcFraction(self, value: PositiveInteger) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcFraction with method chaining.

        Args:
            value: The iidcFraction to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_fraction property setter (gets validation automatically)
        """
        self.iidc_fraction = value  # Delegates to property setter
        return self

    def getIidcSource(self) -> Boolean:
        """
        AUTOSAR-compliant getter for iidcSource.

        Returns:
            The iidcSource value

        Note:
            Delegates to iidc_source property (CODING_RULE_V2_00017)
        """
        return self.iidc_source  # Delegates to property

    def setIidcSource(self, value: Boolean) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcSource with method chaining.

        Args:
            value: The iidcSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_source property setter (gets validation automatically)
        """
        self.iidc_source = value  # Delegates to property setter
        return self

    def getIidcStream(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for iidcStream.

        Returns:
            The iidcStream value

        Note:
            Delegates to iidc_stream property (CODING_RULE_V2_00017)
        """
        return self.iidc_stream  # Delegates to property

    def setIidcStream(self, value: PositiveInteger) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcStream with method chaining.

        Args:
            value: The iidcStream to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_stream property setter (gets validation automatically)
        """
        self.iidc_stream = value  # Delegates to property setter
        return self

    def getIidcSy(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for iidcSy.

        Returns:
            The iidcSy value

        Note:
            Delegates to iidc_sy property (CODING_RULE_V2_00017)
        """
        return self.iidc_sy  # Delegates to property

    def setIidcSy(self, value: PositiveInteger) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcSy with method chaining.

        Args:
            value: The iidcSy to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_sy property setter (gets validation automatically)
        """
        self.iidc_sy = value  # Delegates to property setter
        return self

    def getIidcTag(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for iidcTag.

        Returns:
            The iidcTag value

        Note:
            Delegates to iidc_tag property (CODING_RULE_V2_00017)
        """
        return self.iidc_tag  # Delegates to property

    def setIidcTag(self, value: PositiveInteger) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcTag with method chaining.

        Args:
            value: The iidcTag to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_tag property setter (gets validation automatically)
        """
        self.iidc_tag = value  # Delegates to property setter
        return self

    def getIidcTCode(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for iidcTCode.

        Returns:
            The iidcTCode value

        Note:
            Delegates to iidc_t_code property (CODING_RULE_V2_00017)
        """
        return self.iidc_t_code  # Delegates to property

    def setIidcTCode(self, value: PositiveInteger) -> IEEE1722TpIidcConnection:
        """
        AUTOSAR-compliant setter for iidcTCode with method chaining.

        Args:
            value: The iidcTCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to iidc_t_code property setter (gets validation automatically)
        """
        self.iidc_t_code = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_iidc_channel(self, value: Optional[PositiveInteger]) -> IEEE1722TpIidcConnection:
        """
        Set iidcChannel and return self for chaining.

        Args:
            value: The iidcChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_channel("value")
        """
        self.iidc_channel = value  # Use property setter (gets validation)
        return self

    def with_iidc_data_block(self, value: Optional[PositiveInteger]) -> IEEE1722TpIidcConnection:
        """
        Set iidcDataBlock and return self for chaining.

        Args:
            value: The iidcDataBlock to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_data_block("value")
        """
        self.iidc_data_block = value  # Use property setter (gets validation)
        return self

    def with_iidc_fraction(self, value: Optional[PositiveInteger]) -> IEEE1722TpIidcConnection:
        """
        Set iidcFraction and return self for chaining.

        Args:
            value: The iidcFraction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_fraction("value")
        """
        self.iidc_fraction = value  # Use property setter (gets validation)
        return self

    def with_iidc_source(self, value: Optional[Boolean]) -> IEEE1722TpIidcConnection:
        """
        Set iidcSource and return self for chaining.

        Args:
            value: The iidcSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_source("value")
        """
        self.iidc_source = value  # Use property setter (gets validation)
        return self

    def with_iidc_stream(self, value: Optional[PositiveInteger]) -> IEEE1722TpIidcConnection:
        """
        Set iidcStream and return self for chaining.

        Args:
            value: The iidcStream to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_stream("value")
        """
        self.iidc_stream = value  # Use property setter (gets validation)
        return self

    def with_iidc_sy(self, value: Optional[PositiveInteger]) -> IEEE1722TpIidcConnection:
        """
        Set iidcSy and return self for chaining.

        Args:
            value: The iidcSy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_sy("value")
        """
        self.iidc_sy = value  # Use property setter (gets validation)
        return self

    def with_iidc_tag(self, value: Optional[PositiveInteger]) -> IEEE1722TpIidcConnection:
        """
        Set iidcTag and return self for chaining.

        Args:
            value: The iidcTag to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_tag("value")
        """
        self.iidc_tag = value  # Use property setter (gets validation)
        return self

    def with_iidc_t_code(self, value: Optional[PositiveInteger]) -> IEEE1722TpIidcConnection:
        """
        Set iidcTCode and return self for chaining.

        Args:
            value: The iidcTCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iidc_t_code("value")
        """
        self.iidc_t_code = value  # Use property setter (gets validation)
        return self



class IEEE1722TpRvfConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp RVF connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv::IEEE1722TpRvfConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 649, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the RVF stream active_pixels.
        self._rvfActivePixels: Optional[PositiveInteger] = None

    @property
    def rvf_active_pixels(self) -> Optional[PositiveInteger]:
        """Get rvfActivePixels (Pythonic accessor)."""
        return self._rvfActivePixels

    @rvf_active_pixels.setter
    def rvf_active_pixels(self, value: Optional[PositiveInteger]) -> None:
        """
        Set rvfActivePixels with validation.

        Args:
            value: The rvfActivePixels to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfActivePixels = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"rvfActivePixels must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._rvfActivePixels = value
        # atp.
        # Status=candidate 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._rvfColorSpace: Optional[IEEE1722TpRvfColor] = None

    @property
    def rvf_color_space(self) -> Optional[IEEE1722TpRvfColor]:
        """Get rvfColorSpace (Pythonic accessor)."""
        return self._rvfColorSpace

    @rvf_color_space.setter
    def rvf_color_space(self, value: Optional[IEEE1722TpRvfColor]) -> None:
        """
        Set rvfColorSpace with validation.

        Args:
            value: The rvfColorSpace to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfColorSpace = None
            return

        if not isinstance(value, IEEE1722TpRvfColor):
            raise TypeError(
                f"rvfColorSpace must be IEEE1722TpRvfColor or None, got {type(value).__name__}"
            )
        self._rvfColorSpace = value
        self._rvfEventDefault: Optional[PositiveInteger] = None

    @property
    def rvf_event_default(self) -> Optional[PositiveInteger]:
        """Get rvfEventDefault (Pythonic accessor)."""
        return self._rvfEventDefault

    @rvf_event_default.setter
    def rvf_event_default(self, value: Optional[PositiveInteger]) -> None:
        """
        Set rvfEventDefault with validation.

        Args:
            value: The rvfEventDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfEventDefault = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"rvfEventDefault must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._rvfEventDefault = value
        # atp.
        # Status=candidate.
        self._rvfFrameRate: Optional[IEEE1722TpRvfFrame] = None

    @property
    def rvf_frame_rate(self) -> Optional[IEEE1722TpRvfFrame]:
        """Get rvfFrameRate (Pythonic accessor)."""
        return self._rvfFrameRate

    @rvf_frame_rate.setter
    def rvf_frame_rate(self, value: Optional[IEEE1722TpRvfFrame]) -> None:
        """
        Set rvfFrameRate with validation.

        Args:
            value: The rvfFrameRate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfFrameRate = None
            return

        if not isinstance(value, IEEE1722TpRvfFrame):
            raise TypeError(
                f"rvfFrameRate must be IEEE1722TpRvfFrame or None, got {type(value).__name__}"
            )
        self._rvfFrameRate = value
        self._rvfInterlaced: Optional[Boolean] = None

    @property
    def rvf_interlaced(self) -> Optional[Boolean]:
        """Get rvfInterlaced (Pythonic accessor)."""
        return self._rvfInterlaced

    @rvf_interlaced.setter
    def rvf_interlaced(self, value: Optional[Boolean]) -> None:
        """
        Set rvfInterlaced with validation.

        Args:
            value: The rvfInterlaced to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfInterlaced = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"rvfInterlaced must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._rvfInterlaced = value
        # atp.
        # Status=candidate.
        self._rvfPixelDepth: Optional[IEEE1722TpRvfPixel] = None

    @property
    def rvf_pixel_depth(self) -> Optional[IEEE1722TpRvfPixel]:
        """Get rvfPixelDepth (Pythonic accessor)."""
        return self._rvfPixelDepth

    @rvf_pixel_depth.setter
    def rvf_pixel_depth(self, value: Optional[IEEE1722TpRvfPixel]) -> None:
        """
        Set rvfPixelDepth with validation.

        Args:
            value: The rvfPixelDepth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfPixelDepth = None
            return

        if not isinstance(value, IEEE1722TpRvfPixel):
            raise TypeError(
                f"rvfPixelDepth must be IEEE1722TpRvfPixel or None, got {type(value).__name__}"
            )
        self._rvfPixelDepth = value
        # atp.
        # Status=candidate.
        self._rvfPixelFormat: Optional[IEEE1722TpRvfPixel] = None

    @property
    def rvf_pixel_format(self) -> Optional[IEEE1722TpRvfPixel]:
        """Get rvfPixelFormat (Pythonic accessor)."""
        return self._rvfPixelFormat

    @rvf_pixel_format.setter
    def rvf_pixel_format(self, value: Optional[IEEE1722TpRvfPixel]) -> None:
        """
        Set rvfPixelFormat with validation.

        Args:
            value: The rvfPixelFormat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfPixelFormat = None
            return

        if not isinstance(value, IEEE1722TpRvfPixel):
            raise TypeError(
                f"rvfPixelFormat must be IEEE1722TpRvfPixel or None, got {type(value).__name__}"
            )
        self._rvfPixelFormat = value
        self._rvfTotalLines: Optional[PositiveInteger] = None

    @property
    def rvf_total_lines(self) -> Optional[PositiveInteger]:
        """Get rvfTotalLines (Pythonic accessor)."""
        return self._rvfTotalLines

    @rvf_total_lines.setter
    def rvf_total_lines(self, value: Optional[PositiveInteger]) -> None:
        """
        Set rvfTotalLines with validation.

        Args:
            value: The rvfTotalLines to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfTotalLines = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"rvfTotalLines must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._rvfTotalLines = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRvfActivePixels(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for rvfActivePixels.

        Returns:
            The rvfActivePixels value

        Note:
            Delegates to rvf_active_pixels property (CODING_RULE_V2_00017)
        """
        return self.rvf_active_pixels  # Delegates to property

    def setRvfActivePixels(self, value: PositiveInteger) -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfActivePixels with method chaining.

        Args:
            value: The rvfActivePixels to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_active_pixels property setter (gets validation automatically)
        """
        self.rvf_active_pixels = value  # Delegates to property setter
        return self

    def getRvfColorSpace(self) -> "IEEE1722TpRvfColor":
        """
        AUTOSAR-compliant getter for rvfColorSpace.

        Returns:
            The rvfColorSpace value

        Note:
            Delegates to rvf_color_space property (CODING_RULE_V2_00017)
        """
        return self.rvf_color_space  # Delegates to property

    def setRvfColorSpace(self, value: "IEEE1722TpRvfColor") -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfColorSpace with method chaining.

        Args:
            value: The rvfColorSpace to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_color_space property setter (gets validation automatically)
        """
        self.rvf_color_space = value  # Delegates to property setter
        return self

    def getRvfEventDefault(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for rvfEventDefault.

        Returns:
            The rvfEventDefault value

        Note:
            Delegates to rvf_event_default property (CODING_RULE_V2_00017)
        """
        return self.rvf_event_default  # Delegates to property

    def setRvfEventDefault(self, value: PositiveInteger) -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfEventDefault with method chaining.

        Args:
            value: The rvfEventDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_event_default property setter (gets validation automatically)
        """
        self.rvf_event_default = value  # Delegates to property setter
        return self

    def getRvfFrameRate(self) -> "IEEE1722TpRvfFrame":
        """
        AUTOSAR-compliant getter for rvfFrameRate.

        Returns:
            The rvfFrameRate value

        Note:
            Delegates to rvf_frame_rate property (CODING_RULE_V2_00017)
        """
        return self.rvf_frame_rate  # Delegates to property

    def setRvfFrameRate(self, value: "IEEE1722TpRvfFrame") -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfFrameRate with method chaining.

        Args:
            value: The rvfFrameRate to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_frame_rate property setter (gets validation automatically)
        """
        self.rvf_frame_rate = value  # Delegates to property setter
        return self

    def getRvfInterlaced(self) -> Boolean:
        """
        AUTOSAR-compliant getter for rvfInterlaced.

        Returns:
            The rvfInterlaced value

        Note:
            Delegates to rvf_interlaced property (CODING_RULE_V2_00017)
        """
        return self.rvf_interlaced  # Delegates to property

    def setRvfInterlaced(self, value: Boolean) -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfInterlaced with method chaining.

        Args:
            value: The rvfInterlaced to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_interlaced property setter (gets validation automatically)
        """
        self.rvf_interlaced = value  # Delegates to property setter
        return self

    def getRvfPixelDepth(self) -> "IEEE1722TpRvfPixel":
        """
        AUTOSAR-compliant getter for rvfPixelDepth.

        Returns:
            The rvfPixelDepth value

        Note:
            Delegates to rvf_pixel_depth property (CODING_RULE_V2_00017)
        """
        return self.rvf_pixel_depth  # Delegates to property

    def setRvfPixelDepth(self, value: "IEEE1722TpRvfPixel") -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfPixelDepth with method chaining.

        Args:
            value: The rvfPixelDepth to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_pixel_depth property setter (gets validation automatically)
        """
        self.rvf_pixel_depth = value  # Delegates to property setter
        return self

    def getRvfPixelFormat(self) -> "IEEE1722TpRvfPixel":
        """
        AUTOSAR-compliant getter for rvfPixelFormat.

        Returns:
            The rvfPixelFormat value

        Note:
            Delegates to rvf_pixel_format property (CODING_RULE_V2_00017)
        """
        return self.rvf_pixel_format  # Delegates to property

    def setRvfPixelFormat(self, value: "IEEE1722TpRvfPixel") -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfPixelFormat with method chaining.

        Args:
            value: The rvfPixelFormat to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_pixel_format property setter (gets validation automatically)
        """
        self.rvf_pixel_format = value  # Delegates to property setter
        return self

    def getRvfTotalLines(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for rvfTotalLines.

        Returns:
            The rvfTotalLines value

        Note:
            Delegates to rvf_total_lines property (CODING_RULE_V2_00017)
        """
        return self.rvf_total_lines  # Delegates to property

    def setRvfTotalLines(self, value: PositiveInteger) -> IEEE1722TpRvfConnection:
        """
        AUTOSAR-compliant setter for rvfTotalLines with method chaining.

        Args:
            value: The rvfTotalLines to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_total_lines property setter (gets validation automatically)
        """
        self.rvf_total_lines = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rvf_active_pixels(self, value: Optional[PositiveInteger]) -> IEEE1722TpRvfConnection:
        """
        Set rvfActivePixels and return self for chaining.

        Args:
            value: The rvfActivePixels to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_active_pixels("value")
        """
        self.rvf_active_pixels = value  # Use property setter (gets validation)
        return self

    def with_rvf_color_space(self, value: Optional[IEEE1722TpRvfColor]) -> IEEE1722TpRvfConnection:
        """
        Set rvfColorSpace and return self for chaining.

        Args:
            value: The rvfColorSpace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_color_space("value")
        """
        self.rvf_color_space = value  # Use property setter (gets validation)
        return self

    def with_rvf_event_default(self, value: Optional[PositiveInteger]) -> IEEE1722TpRvfConnection:
        """
        Set rvfEventDefault and return self for chaining.

        Args:
            value: The rvfEventDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_event_default("value")
        """
        self.rvf_event_default = value  # Use property setter (gets validation)
        return self

    def with_rvf_frame_rate(self, value: Optional[IEEE1722TpRvfFrame]) -> IEEE1722TpRvfConnection:
        """
        Set rvfFrameRate and return self for chaining.

        Args:
            value: The rvfFrameRate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_frame_rate("value")
        """
        self.rvf_frame_rate = value  # Use property setter (gets validation)
        return self

    def with_rvf_interlaced(self, value: Optional[Boolean]) -> IEEE1722TpRvfConnection:
        """
        Set rvfInterlaced and return self for chaining.

        Args:
            value: The rvfInterlaced to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_interlaced("value")
        """
        self.rvf_interlaced = value  # Use property setter (gets validation)
        return self

    def with_rvf_pixel_depth(self, value: Optional[IEEE1722TpRvfPixel]) -> IEEE1722TpRvfConnection:
        """
        Set rvfPixelDepth and return self for chaining.

        Args:
            value: The rvfPixelDepth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_pixel_depth("value")
        """
        self.rvf_pixel_depth = value  # Use property setter (gets validation)
        return self

    def with_rvf_pixel_format(self, value: Optional[IEEE1722TpRvfPixel]) -> IEEE1722TpRvfConnection:
        """
        Set rvfPixelFormat and return self for chaining.

        Args:
            value: The rvfPixelFormat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_pixel_format("value")
        """
        self.rvf_pixel_format = value  # Use property setter (gets validation)
        return self

    def with_rvf_total_lines(self, value: Optional[PositiveInteger]) -> IEEE1722TpRvfConnection:
        """
        Set rvfTotalLines and return self for chaining.

        Args:
            value: The rvfTotalLines to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_total_lines("value")
        """
        self.rvf_total_lines = value  # Use property setter (gets validation)
        return self


class IEEE1722TpCrfTypeEnum(AREnum):
    """
    IEEE1722TpCrfTypeEnum enumeration

Definition of the CRF stream type. Tags: atp.Status=candidate Aggregated by IEEE1722TpCrfConnection.crfType

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # CRF_AUDIO_SAMPLE, Audio sample timestamp
    audioSample = "0"

    # CRF_MACHINE_CYCLE, Machine cycle timestamp
    machineCycle = "3"

    # CRF_USER, User specified
    user = "4"

    # CRF_VIDEO_FRAME, Video frame sync timestamp
    videoFrame = "1"

    # CRF_VIDEO_LINE, Video line sync timestamp
    videoLine = "2"



class IEEE1722TpCrfPullEnum(AREnum):
    """
    IEEE1722TpCrfPullEnum enumeration

Definition of the CRF stream pull value. Tags: atp.Status=candidate Aggregated by IEEE1722TpCrfConnection.crfPull (cid:53) 640 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # Multiply base_frequency field by 1.0
    _1_0 = "0"

    # Multiply base_frequency field by 1.001
    _1_001 = "2"

    # Multiply base_frequency field by 1/1.001
    _1_1_001 = "1"

    # Multiply base_frequency field by 1/8
    _1_8 = "5"

    # Multiply base_frequency field by 24/25
    _24_25 = "3"

    # Multiply base_frequency field by 25/24
    _25_24 = "4"



class IEEE1722TpAafNominalRateEnum(AREnum):
    """
    IEEE1722TpAafNominalRateEnum enumeration

Definition of the AAF nominal sample / frame rate. Tags: atp.Status=candidate Aggregated by IEEE1722TpAafConnection.aafNominalRate

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # 16 kHz
    _16kHz = "2"

    # 176.4 kHz
    _176_4kHz = "8"

    # 192 kHz
    _192kHz = "9"

    # 24 kHz
    _24kHz = "10"

    # 32 kHz
    _32kHz = "3"

    # 44.1 kHz
    _44_1kHz = "4"

    # 48 kHz
    _48kHz = "5"

    # Template
    System = "None"

    # CP R23-11
    AUTOSAR_88_2kHz = "6"

    # 8 kHz
    _8kHz = "1"

    # 96 kHz
    _96kHz = "7"

    # User specified
    user = "0"



class IEEE1722TpAafFormatEnum(AREnum):
    """
    IEEE1722TpAafFormatEnum enumeration

Definition of the AAF stream format. Tags: atp.Status=candidate Aggregated by IEEE1722TpAafConnection.aafFormat

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # AES3_32BIT, 32-bit AES3 format, AES3
    aes3_32bit = "5"

    # FLOAT_32BIT, 32bit floating, PCM
    float_32bit = "1"

    # INT_16BIT, 16 bit integer, PCM
    int_16bit = "4"

    # INT_24BIT, 24 bit integer, PCM
    int_24bit = "3"

    # INT_32BIT, 32bit integer, PCM
    int_32bit = "2"

    # USER, user specific, PCM
    user = "0"



class IEEE1722TpAafAes3DataTypeEnum(AREnum):
    """
    IEEE1722TpAafAes3DataTypeEnum enumeration

Definition of the AAF AES3 stream aes3_data_type reference. Tags: atp.Status=candidate Aggregated by IEEE1722TpAafConnection.aafAes3DataType

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # Data type reference is IEC 61937-2
    iec61937 = "4"

    # Data type is PCM
    pcm = "2"

    # Data type reference is SMPTE ST 338
    smpte338 = "3"

    # Data type not specified
    unspecified = "1"

    # Data type reference is defined by vendor
    vendor = "0"



class IEEE1722TpRvfPixelDepthEnum(AREnum):
    """
    IEEE1722TpRvfPixelDepthEnum enumeration

Definition of the RVF Pixel Depth. Tags: atp.Status=candidate Aggregated by IEEE1722TpRvfConnection.rvfPixelDepth

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # pixel depth 10 _12 pixel depth 12 _16 pixel depth 16 _8 pixel depth 8 user pixel depth user defined
    _10 = "4"



class IEEE1722TpRvfPixelFormatEnum(AREnum):
    """
    IEEE1722TpRvfPixelFormatEnum enumeration

Definition of the RVF Pixel Format. Tags: atp.Status=candidate (cid:53) 650 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # pixel format 4:1:1 _4_2_0 pixel format 4:2:0 _4_2_2 pixel format 4:2:2 _4_2_2_4 pixel format 4:2:2:4 _4_4_4 pixel format 4:4:4 _4_4_4_4 pixel format 4:4:4:4 bayer_bggr pixel format Bayer bggr bayer_gbrg pixel format Bayer gbrg bayer_grbg pixel format Bayer grbg bayer_rggb pixel format Bayer rggb monochrome pixel format Monochrome user pixel format User defined
    _4_1_1 = "11"



class IEEE1722TpRvfColorSpaceEnum(AREnum):
    """
    IEEE1722TpRvfColorSpaceEnum enumeration

Definition of the RVF stream colorspace. Tags: atp.Status=candidate Aggregated by IEEE1722TpRvfConnection.rvfColorSpace

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # BT Rec.601
    bt_rec_601 = "0"

    # BT Rec.709
    bt_rec_709 = "1"

    # Grayscale
    grayscale = "2"

    # ITU BT 2020 srgb sRGB
    itu_bt_2020 = "9"

    # User defined
    user = "4"

    # XYZ
    xyz = "5"

    # YCbCr
    ycbcr = "7"

    # YCgCo
    ycgco = "8"

    # YCM
    ycm = "6"



class IEEE1722TpRvfFrameRateEnum(AREnum):
    """
    IEEE1722TpRvfFrameRateEnum enumeration

Definition of the RVF stream frame_rate. Tags: atp.Status=candidate Aggregated by IEEE1722TpRvfConnection.rvfFrameRate

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv
    """
    # frame rate 1 _10 frame rate 10
    _1 = "3"

    # Template
    System = "None"

    # CP R23-11 _100 frame rate 100 _120 frame rate 120 _15 frame rate 15 _150 frame rate 150 _2 frame rate 2 _20 frame rate 20 _200 frame rate 200 _24 frame rate 24 _240 frame rate 240 _25 frame rate 25 _30 frame rate 30 _300 frame rate 300 _48 frame rate 48
    AUTOSAR = "9"

    # Template
    System = "None"

    # CP R23-11 _5 frame rate 5 _50 frame rate 50 _60 frame rate 60 _72 frame rate 72 _85 frame rate 85 user frame rate User defined
    AUTOSAR = "20"
