from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinConfigurationEntry


class ConditionalChangeNad(LinConfigurationEntry):
    """
    Generates an conditional change NAD request. See ISO 17987 protocol
    specification for more information.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::ConditionalChangeNad

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 438, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Byte Position of Data Byte that should be used for the with Invert and the
        # bitwise AND with Mask.
        self._byte: Optional["Integer"] = None

    @property
    def byte(self) -> Optional["Integer"]:
        """Get byte (Pythonic accessor)."""
        return self._byte

    @byte.setter
    def byte(self, value: Optional["Integer"]) -> None:
        """
        Set byte with validation.

        Args:
            value: The byte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._byte = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"byte must be Integer or None, got {type(value).__name__}"
            )
        self._byte = value
        # Byte Position of Id.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # Byte Position of Invert.
        self._invert: Optional["Integer"] = None

    @property
    def invert(self) -> Optional["Integer"]:
        """Get invert (Pythonic accessor)."""
        return self._invert

    @invert.setter
    def invert(self, value: Optional["Integer"]) -> None:
        """
        Set invert with validation.

        Args:
            value: The invert to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._invert = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"invert must be Integer or None, got {type(value).__name__}"
            )
        self._invert = value
        # Byte Position of Mask.
        self._mask: Optional["Integer"] = None

    @property
    def mask(self) -> Optional["Integer"]:
        """Get mask (Pythonic accessor)."""
        return self._mask

    @mask.setter
    def mask(self, value: Optional["Integer"]) -> None:
        """
        Set mask with validation.

        Args:
            value: The mask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mask = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"mask must be Integer or None, got {type(value).__name__}"
            )
        self._mask = value
        # The newly assigned NAD value (Byte Position).
        self._newNad: Optional["Integer"] = None

    @property
    def new_nad(self) -> Optional["Integer"]:
        """Get newNad (Pythonic accessor)."""
        return self._newNad

    @new_nad.setter
    def new_nad(self, value: Optional["Integer"]) -> None:
        """
        Set newNad with validation.

        Args:
            value: The newNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._newNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"newNad must be Integer or None, got {type(value).__name__}"
            )
        self._newNad = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getByte(self) -> "Integer":
        """
        AUTOSAR-compliant getter for byte.

        Returns:
            The byte value

        Note:
            Delegates to byte property (CODING_RULE_V2_00017)
        """
        return self.byte  # Delegates to property

    def setByte(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for byte with method chaining.

        Args:
            value: The byte to set

        Returns:
            self for method chaining

        Note:
            Delegates to byte property setter (gets validation automatically)
        """
        self.byte = value  # Delegates to property setter
        return self

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getInvert(self) -> "Integer":
        """
        AUTOSAR-compliant getter for invert.

        Returns:
            The invert value

        Note:
            Delegates to invert property (CODING_RULE_V2_00017)
        """
        return self.invert  # Delegates to property

    def setInvert(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for invert with method chaining.

        Args:
            value: The invert to set

        Returns:
            self for method chaining

        Note:
            Delegates to invert property setter (gets validation automatically)
        """
        self.invert = value  # Delegates to property setter
        return self

    def getMask(self) -> "Integer":
        """
        AUTOSAR-compliant getter for mask.

        Returns:
            The mask value

        Note:
            Delegates to mask property (CODING_RULE_V2_00017)
        """
        return self.mask  # Delegates to property

    def setMask(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for mask with method chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Note:
            Delegates to mask property setter (gets validation automatically)
        """
        self.mask = value  # Delegates to property setter
        return self

    def getNewNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for newNad.

        Returns:
            The newNad value

        Note:
            Delegates to new_nad property (CODING_RULE_V2_00017)
        """
        return self.new_nad  # Delegates to property

    def setNewNad(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for newNad with method chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to new_nad property setter (gets validation automatically)
        """
        self.new_nad = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_byte(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set byte and return self for chaining.

        Args:
            value: The byte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_byte("value")
        """
        self.byte = value  # Use property setter (gets validation)
        return self

    def with_id(self, value: Optional["PositiveInteger"]) -> "ConditionalChangeNad":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_invert(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set invert and return self for chaining.

        Args:
            value: The invert to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_invert("value")
        """
        self.invert = value  # Use property setter (gets validation)
        return self

    def with_mask(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set mask and return self for chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mask("value")
        """
        self.mask = value  # Use property setter (gets validation)
        return self

    def with_new_nad(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set newNad and return self for chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_new_nad("value")
        """
        self.new_nad = value  # Use property setter (gets validation)
        return self
