from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TransmissionComSpecProps(ARObject):
    """
    This meta-class defines a set of transmission attributes which the
    application software is assumed to implement.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::TransmissionComSpecProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2075, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the period in which the application is to transmit the
                # respective data.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._dataUpdate: Optional["TimeValue"] = None

    @property
    def data_update(self) -> Optional["TimeValue"]:
        """Get dataUpdate (Pythonic accessor)."""
        return self._dataUpdate

    @data_update.setter
    def data_update(self, value: Optional["TimeValue"]) -> None:
        """
        Set dataUpdate with validation.

        Args:
            value: The dataUpdate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataUpdate = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"dataUpdate must be TimeValue or None, got {type(value).__name__}"
            )
        self._dataUpdate = value
        # This attribute defines the minimum interval between two transmissions of the
        # respective data the assumed to ensure.
        self._minimumSend: Optional["TimeValue"] = None

    @property
    def minimum_send(self) -> Optional["TimeValue"]:
        """Get minimumSend (Pythonic accessor)."""
        return self._minimumSend

    @minimum_send.setter
    def minimum_send(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimumSend with validation.

        Args:
            value: The minimumSend to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumSend = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimumSend must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimumSend = value
        # The attribute defines the mode in which the application is assumed to
        # transmit the respective data.
        self._transmission: Optional["TransmissionMode"] = None

    @property
    def transmission(self) -> Optional["TransmissionMode"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TransmissionMode"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TransmissionMode):
            raise TypeError(
                f"transmission must be TransmissionMode or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataUpdate(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for dataUpdate.

        Returns:
            The dataUpdate value

        Note:
            Delegates to data_update property (CODING_RULE_V2_00017)
        """
        return self.data_update  # Delegates to property

    def setDataUpdate(self, value: "TimeValue") -> "TransmissionComSpecProps":
        """
        AUTOSAR-compliant setter for dataUpdate with method chaining.

        Args:
            value: The dataUpdate to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_update property setter (gets validation automatically)
        """
        self.data_update = value  # Delegates to property setter
        return self

    def getMinimumSend(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimumSend.

        Returns:
            The minimumSend value

        Note:
            Delegates to minimum_send property (CODING_RULE_V2_00017)
        """
        return self.minimum_send  # Delegates to property

    def setMinimumSend(self, value: "TimeValue") -> "TransmissionComSpecProps":
        """
        AUTOSAR-compliant setter for minimumSend with method chaining.

        Args:
            value: The minimumSend to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_send property setter (gets validation automatically)
        """
        self.minimum_send = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "TransmissionMode":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TransmissionMode") -> "TransmissionComSpecProps":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_update(self, value: Optional["TimeValue"]) -> "TransmissionComSpecProps":
        """
        Set dataUpdate and return self for chaining.

        Args:
            value: The dataUpdate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_update("value")
        """
        self.data_update = value  # Use property setter (gets validation)
        return self

    def with_minimum_send(self, value: Optional["TimeValue"]) -> "TransmissionComSpecProps":
        """
        Set minimumSend and return self for chaining.

        Args:
            value: The minimumSend to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_send("value")
        """
        self.minimum_send = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["TransmissionMode"]) -> "TransmissionComSpecProps":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self
