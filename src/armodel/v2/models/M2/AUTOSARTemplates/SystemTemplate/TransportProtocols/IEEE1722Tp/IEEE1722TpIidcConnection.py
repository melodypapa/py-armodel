from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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
        self._iidcChannel: Optional["PositiveInteger"] = None

    @property
    def iidc_channel(self) -> Optional["PositiveInteger"]:
        """Get iidcChannel (Pythonic accessor)."""
        return self._iidcChannel

    @iidc_channel.setter
    def iidc_channel(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"iidcChannel must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._iidcChannel = value
        # Definition of the IIDC data block size (DBS).
        # atp.
        # Status=candidate.
        self._iidcDataBlock: Optional["PositiveInteger"] = None

    @property
    def iidc_data_block(self) -> Optional["PositiveInteger"]:
        """Get iidcDataBlock (Pythonic accessor)."""
        return self._iidcDataBlock

    @iidc_data_block.setter
    def iidc_data_block(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"iidcDataBlock must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._iidcDataBlock = value
        # Definition of the IIDC fractionNumber (FN).
        # atp.
        # Status=candidate.
        self._iidcFraction: Optional["PositiveInteger"] = None

    @property
    def iidc_fraction(self) -> Optional["PositiveInteger"]:
        """Get iidcFraction (Pythonic accessor)."""
        return self._iidcFraction

    @iidc_fraction.setter
    def iidc_fraction(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"iidcFraction must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._iidcFraction = value
        # Defines the IIDC source packet header (SPH) existence.
        # atp.
        # Status=candidate.
        self._iidcSource: Optional["Boolean"] = None

    @property
    def iidc_source(self) -> Optional["Boolean"]:
        """Get iidcSource (Pythonic accessor)."""
        return self._iidcSource

    @iidc_source.setter
    def iidc_source(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"iidcSource must be Boolean or None, got {type(value).__name__}"
            )
        self._iidcSource = value
        # Definition of the IIDC stream format (FMT).
        # atp.
        # Status=candidate.
        self._iidcStream: Optional["PositiveInteger"] = None

    @property
    def iidc_stream(self) -> Optional["PositiveInteger"]:
        """Get iidcStream (Pythonic accessor)."""
        return self._iidcStream

    @iidc_stream.setter
    def iidc_stream(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"iidcStream must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._iidcStream = value
        # Definition of the IIDC sy.
        self._iidcSy: Optional["PositiveInteger"] = None

    @property
    def iidc_sy(self) -> Optional["PositiveInteger"]:
        """Get iidcSy (Pythonic accessor)."""
        return self._iidcSy

    @iidc_sy.setter
    def iidc_sy(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"iidcSy must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._iidcSy = value
        # Definition of the IIDC tag.
        self._iidcTag: Optional["PositiveInteger"] = None

    @property
    def iidc_tag(self) -> Optional["PositiveInteger"]:
        """Get iidcTag (Pythonic accessor)."""
        return self._iidcTag

    @iidc_tag.setter
    def iidc_tag(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"iidcTag must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._iidcTag = value
        # Definition of the IIDC tcode.
        self._iidcTCode: Optional["PositiveInteger"] = None

    @property
    def iidc_t_code(self) -> Optional["PositiveInteger"]:
        """Get iidcTCode (Pythonic accessor)."""
        return self._iidcTCode

    @iidc_t_code.setter
    def iidc_t_code(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"iidcTCode must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._iidcTCode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIidcChannel(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for iidcChannel.
        
        Returns:
            The iidcChannel value
        
        Note:
            Delegates to iidc_channel property (CODING_RULE_V2_00017)
        """
        return self.iidc_channel  # Delegates to property

    def setIidcChannel(self, value: "PositiveInteger") -> "IEEE1722TpIidcConnection":
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

    def getIidcDataBlock(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for iidcDataBlock.
        
        Returns:
            The iidcDataBlock value
        
        Note:
            Delegates to iidc_data_block property (CODING_RULE_V2_00017)
        """
        return self.iidc_data_block  # Delegates to property

    def setIidcDataBlock(self, value: "PositiveInteger") -> "IEEE1722TpIidcConnection":
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

    def getIidcFraction(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for iidcFraction.
        
        Returns:
            The iidcFraction value
        
        Note:
            Delegates to iidc_fraction property (CODING_RULE_V2_00017)
        """
        return self.iidc_fraction  # Delegates to property

    def setIidcFraction(self, value: "PositiveInteger") -> "IEEE1722TpIidcConnection":
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

    def getIidcSource(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for iidcSource.
        
        Returns:
            The iidcSource value
        
        Note:
            Delegates to iidc_source property (CODING_RULE_V2_00017)
        """
        return self.iidc_source  # Delegates to property

    def setIidcSource(self, value: "Boolean") -> "IEEE1722TpIidcConnection":
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

    def getIidcStream(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for iidcStream.
        
        Returns:
            The iidcStream value
        
        Note:
            Delegates to iidc_stream property (CODING_RULE_V2_00017)
        """
        return self.iidc_stream  # Delegates to property

    def setIidcStream(self, value: "PositiveInteger") -> "IEEE1722TpIidcConnection":
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

    def getIidcSy(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for iidcSy.
        
        Returns:
            The iidcSy value
        
        Note:
            Delegates to iidc_sy property (CODING_RULE_V2_00017)
        """
        return self.iidc_sy  # Delegates to property

    def setIidcSy(self, value: "PositiveInteger") -> "IEEE1722TpIidcConnection":
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

    def getIidcTag(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for iidcTag.
        
        Returns:
            The iidcTag value
        
        Note:
            Delegates to iidc_tag property (CODING_RULE_V2_00017)
        """
        return self.iidc_tag  # Delegates to property

    def setIidcTag(self, value: "PositiveInteger") -> "IEEE1722TpIidcConnection":
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

    def getIidcTCode(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for iidcTCode.
        
        Returns:
            The iidcTCode value
        
        Note:
            Delegates to iidc_t_code property (CODING_RULE_V2_00017)
        """
        return self.iidc_t_code  # Delegates to property

    def setIidcTCode(self, value: "PositiveInteger") -> "IEEE1722TpIidcConnection":
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

    def with_iidc_channel(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpIidcConnection":
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

    def with_iidc_data_block(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpIidcConnection":
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

    def with_iidc_fraction(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpIidcConnection":
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

    def with_iidc_source(self, value: Optional["Boolean"]) -> "IEEE1722TpIidcConnection":
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

    def with_iidc_stream(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpIidcConnection":
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

    def with_iidc_sy(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpIidcConnection":
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

    def with_iidc_tag(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpIidcConnection":
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

    def with_iidc_t_code(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpIidcConnection":
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