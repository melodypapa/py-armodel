from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import TimeValue
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ReceptionComSpecProps(ARObject):
    """
    This meta-class defines a set of reception attributes which the application
    software is assumed to implement.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ReceptionComSpecProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 174, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the period in which the application check for updated
                # data.
        # This attribute is used for the the E2E protection, but may also indicate data
                # reception period.
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
        # This attribute defines the time interval after which the assume that the to
                # be received data timed out, i.
        # e.
        # the respective data has not for that amount of time.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

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

    def setDataUpdate(self, value: "TimeValue") -> "ReceptionComSpecProps":
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

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "ReceptionComSpecProps":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_update(self, value: Optional["TimeValue"]) -> "ReceptionComSpecProps":
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

    def with_timeout(self, value: Optional["TimeValue"]) -> "ReceptionComSpecProps":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self
