from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import TDEventVfb

    RefType,
)


class TDEventVfbPort(TDEventVfb, ABC):
    """
    This is the abstract parent class to describe specific timing event types at
    Virtual Functional Bus (VFB) level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 52, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 221, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is TDEventVfbPort:
            raise TypeError("TDEventVfbPort is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to refer to external events that are hardware I/O,
        # like physical sensors and Virtual Functional Bus (VFB) level.
        self._isExternal: Optional["Boolean"] = None

    @property
    def is_external(self) -> Optional["Boolean"]:
        """Get isExternal (Pythonic accessor)."""
        return self._isExternal

    @is_external.setter
    def is_external(self, value: Optional["Boolean"]) -> None:
        """
        Set isExternal with validation.

        Args:
            value: The isExternal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isExternal = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isExternal must be Boolean or None, got {type(value).__name__}"
            )
        self._isExternal = value
        # port on which the TimingEvent shall apply.
        self._port: RefType = None

    @property
    def port(self) -> RefType:
        """Get port (Pythonic accessor)."""
        return self._port

    @port.setter
    def port(self, value: RefType) -> None:
        """
        Set port with validation.

        Args:
            value: The port to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._port = None
            return

        self._port = value
        # port on which the TimingEvent shall apply (in the context an AUTOSAR
        # blueprint).
        self._portPrototype: RefType = None

    @property
    def port_prototype(self) -> RefType:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: RefType) -> None:
        """
        Set portPrototype with validation.

        Args:
            value: The portPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portPrototype = None
            return

        self._portPrototype = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIsExternal(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isExternal.

        Returns:
            The isExternal value

        Note:
            Delegates to is_external property (CODING_RULE_V2_00017)
        """
        return self.is_external  # Delegates to property

    def setIsExternal(self, value: "Boolean") -> "TDEventVfbPort":
        """
        AUTOSAR-compliant setter for isExternal with method chaining.

        Args:
            value: The isExternal to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_external property setter (gets validation automatically)
        """
        self.is_external = value  # Delegates to property setter
        return self

    def getPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for port.

        Returns:
            The port value

        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def setPort(self, value: RefType) -> "TDEventVfbPort":
        """
        AUTOSAR-compliant setter for port with method chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Note:
            Delegates to port property setter (gets validation automatically)
        """
        self.port = value  # Delegates to property setter
        return self

    def getPortPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: RefType) -> "TDEventVfbPort":
        """
        AUTOSAR-compliant setter for portPrototype with method chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_prototype property setter (gets validation automatically)
        """
        self.port_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_external(self, value: Optional["Boolean"]) -> "TDEventVfbPort":
        """
        Set isExternal and return self for chaining.

        Args:
            value: The isExternal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_external("value")
        """
        self.is_external = value  # Use property setter (gets validation)
        return self

    def with_port(self, value: Optional[RefType]) -> "TDEventVfbPort":
        """
        Set port and return self for chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port("value")
        """
        self.port = value  # Use property setter (gets validation)
        return self

    def with_port_prototype(self, value: Optional[RefType]) -> "TDEventVfbPort":
        """
        Set portPrototype and return self for chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_prototype("value")
        """
        self.port_prototype = value  # Use property setter (gets validation)
        return self
