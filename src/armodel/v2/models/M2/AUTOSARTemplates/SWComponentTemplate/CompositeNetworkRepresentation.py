from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class CompositeNetworkRepresentation(ARObject):
    """
    This meta-class is used to define the network representation of leaf
    elements of composite application data types.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::CompositeNetworkRepresentation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 181, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # data type.
        # by: ApplicationComposite.
        self._leafElementElementInPortInterfaceInstanceRef: Optional["ApplicationComposite"] = None

    @property
    def leaf_element_element_in_port_interface_instance_ref(self) -> Optional["ApplicationComposite"]:
        """Get leafElementElementInPortInterfaceInstanceRef (Pythonic accessor)."""
        return self._leafElementElementInPortInterfaceInstanceRef

    @leaf_element_element_in_port_interface_instance_ref.setter
    def leaf_element_element_in_port_interface_instance_ref(self, value: Optional["ApplicationComposite"]) -> None:
        """
        Set leafElementElementInPortInterfaceInstanceRef with validation.

        Args:
            value: The leafElementElementInPortInterfaceInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._leafElementElementInPortInterfaceInstanceRef = None
            return

        if not isinstance(value, ApplicationComposite):
            raise TypeError(
                f"leafElementElementInPortInterfaceInstanceRef must be ApplicationComposite or None, got {type(value).__name__}"
            )
        self._leafElementElementInPortInterfaceInstanceRef = value
        # The SwDataDefProps owned by the CompositeNetwork are used to define the
        # network the leaf element of an Application.
        self._network: Optional["SwDataDefProps"] = None

    @property
    def network(self) -> Optional["SwDataDefProps"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"network must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._network = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLeafElementElementInPortInterfaceInstanceRef(self) -> "ApplicationComposite":
        """
        AUTOSAR-compliant getter for leafElementElementInPortInterfaceInstanceRef.

        Returns:
            The leafElementElementInPortInterfaceInstanceRef value

        Note:
            Delegates to leaf_element_element_in_port_interface_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.leaf_element_element_in_port_interface_instance_ref  # Delegates to property

    def setLeafElementElementInPortInterfaceInstanceRef(self, value: "ApplicationComposite") -> "CompositeNetworkRepresentation":
        """
        AUTOSAR-compliant setter for leafElementElementInPortInterfaceInstanceRef with method chaining.

        Args:
            value: The leafElementElementInPortInterfaceInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to leaf_element_element_in_port_interface_instance_ref property setter (gets validation automatically)
        """
        self.leaf_element_element_in_port_interface_instance_ref = value  # Delegates to property setter
        return self

    def getNetwork(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "SwDataDefProps") -> "CompositeNetworkRepresentation":
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_leaf_element_element_in_port_interface_instance_ref(self, value: Optional["ApplicationComposite"]) -> "CompositeNetworkRepresentation":
        """
        Set leafElementElementInPortInterfaceInstanceRef and return self for chaining.

        Args:
            value: The leafElementElementInPortInterfaceInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_leaf_element_element_in_port_interface_instance_ref("value")
        """
        self.leaf_element_element_in_port_interface_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["SwDataDefProps"]) -> "CompositeNetworkRepresentation":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self
