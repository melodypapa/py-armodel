from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DelegationSwConnector(SwConnector):
    """
    A delegation connector delegates one inner PortPrototype (a port of a
    component that is used inside the composition) to a outer PortPrototype of
    compatible type that belongs directly to the composition (a port that is
    owned by the composition).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::DelegationSwConnector

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 80, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2016, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: PortInCompositionType.
        self._innerPortInstanceRef: RefType = None

    @property
    def inner_port_instance_ref(self) -> RefType:
        """Get innerPortInstanceRef (Pythonic accessor)."""
        return self._innerPortInstanceRef

    @inner_port_instance_ref.setter
    def inner_port_instance_ref(self, value: RefType) -> None:
        """
        Set innerPortInstanceRef with validation.

        Args:
            value: The innerPortInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._innerPortInstanceRef = None
            return

        self._innerPortInstanceRef = value
        # The port that is located on the outside of the Composition.
        self._outerPort: RefType = None

    @property
    def outer_port(self) -> RefType:
        """Get outerPort (Pythonic accessor)."""
        return self._outerPort

    @outer_port.setter
    def outer_port(self, value: RefType) -> None:
        """
        Set outerPort with validation.

        Args:
            value: The outerPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._outerPort = None
            return

        self._outerPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInnerPortInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for innerPortInstanceRef.

        Returns:
            The innerPortInstanceRef value

        Note:
            Delegates to inner_port_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.inner_port_instance_ref  # Delegates to property

    def setInnerPortInstanceRef(self, value: RefType) -> "DelegationSwConnector":
        """
        AUTOSAR-compliant setter for innerPortInstanceRef with method chaining.

        Args:
            value: The innerPortInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to inner_port_instance_ref property setter (gets validation automatically)
        """
        self.inner_port_instance_ref = value  # Delegates to property setter
        return self

    def getOuterPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for outerPort.

        Returns:
            The outerPort value

        Note:
            Delegates to outer_port property (CODING_RULE_V2_00017)
        """
        return self.outer_port  # Delegates to property

    def setOuterPort(self, value: RefType) -> "DelegationSwConnector":
        """
        AUTOSAR-compliant setter for outerPort with method chaining.

        Args:
            value: The outerPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to outer_port property setter (gets validation automatically)
        """
        self.outer_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_inner_port_instance_ref(self, value: Optional[RefType]) -> "DelegationSwConnector":
        """
        Set innerPortInstanceRef and return self for chaining.

        Args:
            value: The innerPortInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inner_port_instance_ref("value")
        """
        self.inner_port_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_outer_port(self, value: Optional[RefType]) -> "DelegationSwConnector":
        """
        Set outerPort and return self for chaining.

        Args:
            value: The outerPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_outer_port("value")
        """
        self.outer_port = value  # Use property setter (gets validation)
        return self
