from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """
    This meta-class is used to map an OsTaskProxy that was created in the
    context of a SwComponent to an OsTaskProxy that was created in the context
    of an Ecu.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 209, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an OsTaskProxy that is created in the a SwComponent.
        self._appTaskProxy: Optional["OsTaskProxy"] = None

    @property
    def app_task_proxy(self) -> Optional["OsTaskProxy"]:
        """Get appTaskProxy (Pythonic accessor)."""
        return self._appTaskProxy

    @app_task_proxy.setter
    def app_task_proxy(self, value: Optional["OsTaskProxy"]) -> None:
        """
        Set appTaskProxy with validation.

        Args:
            value: The appTaskProxy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._appTaskProxy = None
            return

        if not isinstance(value, OsTaskProxy):
            raise TypeError(
                f"appTaskProxy must be OsTaskProxy or None, got {type(value).__name__}"
            )
        self._appTaskProxy = value
        # Reference to an OsTaskProxy that is created in the an EcuInstance.
        self._ecuTaskProxy: Optional["OsTaskProxy"] = None

    @property
    def ecu_task_proxy(self) -> Optional["OsTaskProxy"]:
        """Get ecuTaskProxy (Pythonic accessor)."""
        return self._ecuTaskProxy

    @ecu_task_proxy.setter
    def ecu_task_proxy(self, value: Optional["OsTaskProxy"]) -> None:
        """
        Set ecuTaskProxy with validation.

        Args:
            value: The ecuTaskProxy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuTaskProxy = None
            return

        if not isinstance(value, OsTaskProxy):
            raise TypeError(
                f"ecuTaskProxy must be OsTaskProxy or None, got {type(value).__name__}"
            )
        self._ecuTaskProxy = value
        # This attribute is used to describe the position of the app an ecuTaskProxy as
                # a relative value, i.
        # e.
        # the only the relative position of the appTask the ecuTaskProxy.
        self._offset: Optional["Integer"] = None

    @property
    def offset(self) -> Optional["Integer"]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional["Integer"]) -> None:
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"offset must be Integer or None, got {type(value).__name__}"
            )
        self._offset = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAppTaskProxy(self) -> "OsTaskProxy":
        """
        AUTOSAR-compliant getter for appTaskProxy.

        Returns:
            The appTaskProxy value

        Note:
            Delegates to app_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.app_task_proxy  # Delegates to property

    def setAppTaskProxy(self, value: "OsTaskProxy") -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """
        AUTOSAR-compliant setter for appTaskProxy with method chaining.

        Args:
            value: The appTaskProxy to set

        Returns:
            self for method chaining

        Note:
            Delegates to app_task_proxy property setter (gets validation automatically)
        """
        self.app_task_proxy = value  # Delegates to property setter
        return self

    def getEcuTaskProxy(self) -> "OsTaskProxy":
        """
        AUTOSAR-compliant getter for ecuTaskProxy.

        Returns:
            The ecuTaskProxy value

        Note:
            Delegates to ecu_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.ecu_task_proxy  # Delegates to property

    def setEcuTaskProxy(self, value: "OsTaskProxy") -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """
        AUTOSAR-compliant setter for ecuTaskProxy with method chaining.

        Args:
            value: The ecuTaskProxy to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_task_proxy property setter (gets validation automatically)
        """
        self.ecu_task_proxy = value  # Delegates to property setter
        return self

    def getOffset(self) -> "Integer":
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: "Integer") -> "AppOsTaskProxyToEcuTaskProxyMapping":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_app_task_proxy(self, value: Optional["OsTaskProxy"]) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """
        Set appTaskProxy and return self for chaining.

        Args:
            value: The appTaskProxy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_app_task_proxy("value")
        """
        self.app_task_proxy = value  # Use property setter (gets validation)
        return self

    def with_ecu_task_proxy(self, value: Optional["OsTaskProxy"]) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """
        Set ecuTaskProxy and return self for chaining.

        Args:
            value: The ecuTaskProxy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_task_proxy("value")
        """
        self.ecu_task_proxy = value  # Use property setter (gets validation)
        return self

    def with_offset(self, value: Optional["Integer"]) -> "AppOsTaskProxyToEcuTaskProxyMapping":
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
