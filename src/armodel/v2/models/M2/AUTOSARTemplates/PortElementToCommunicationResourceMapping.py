from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PortElementToCommunicationResourceMapping(Identifiable):
    """
    This meta class maps a communication resource to CP Software Clusters. In
    this case the kind of Port Prototype specified whether the Software Cluster
    has to provide or to require the resource.

    Package: M2::AUTOSARTemplates::SystemTemplate

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 905, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # resource by: OperationInSystem.
        self._clientServerInstanceRef: Optional["ClientServerOperation"] = None

    @property
    def client_server_instance_ref(self) -> Optional["ClientServerOperation"]:
        """Get clientServerInstanceRef (Pythonic accessor)."""
        return self._clientServerInstanceRef

    @client_server_instance_ref.setter
    def client_server_instance_ref(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set clientServerInstanceRef with validation.

        Args:
            value: The clientServerInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientServerInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"clientServerInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._clientServerInstanceRef = value
        # Communication resource for which the mapping applies.
        self._communication: Optional["CpSoftwareCluster"] = None

    @property
    def communication(self) -> Optional["CpSoftwareCluster"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"communication must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._communication = value
        # communication resource implemented by: ModeDeclarationGroup.
        self._mode: RefType = None

    @property
    def mode(self) -> RefType:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: RefType) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        self._mode = value
        # communication resource.
        # by: ParameterDataPrototype.
        self._parameterData: Optional["ParameterData"] = None

    @property
    def parameter_data(self) -> Optional["ParameterData"]:
        """Get parameterData (Pythonic accessor)."""
        return self._parameterData

    @parameter_data.setter
    def parameter_data(self, value: Optional["ParameterData"]) -> None:
        """
        Set parameterData with validation.

        Args:
            value: The parameterData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameterData = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"parameterData must be ParameterData or None, got {type(value).__name__}"
            )
        self._parameterData = value
        # by: TriggerInSystemInstance.
        self._triggerRef: RefType = None

    @property
    def trigger_ref(self) -> RefType:
        """Get triggerRef (Pythonic accessor)."""
        return self._triggerRef

    @trigger_ref.setter
    def trigger_ref(self, value: RefType) -> None:
        """
        Set triggerRef with validation.

        Args:
            value: The triggerRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerRef = None
            return

        self._triggerRef = value
        # resource by: VariableDataPrototypeIn.
        self._variableDataSystemInstanceRef: RefType = None

    @property
    def variable_data_system_instance_ref(self) -> RefType:
        """Get variableDataSystemInstanceRef (Pythonic accessor)."""
        return self._variableDataSystemInstanceRef

    @variable_data_system_instance_ref.setter
    def variable_data_system_instance_ref(self, value: RefType) -> None:
        """
        Set variableDataSystemInstanceRef with validation.

        Args:
            value: The variableDataSystemInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableDataSystemInstanceRef = None
            return

        self._variableDataSystemInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientServerInstanceRef(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for clientServerInstanceRef.

        Returns:
            The clientServerInstanceRef value

        Note:
            Delegates to client_server_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.client_server_instance_ref  # Delegates to property

    def setClientServerInstanceRef(self, value: "ClientServerOperation") -> "PortElementToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for clientServerInstanceRef with method chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_server_instance_ref property setter (gets validation automatically)
        """
        self.client_server_instance_ref = value  # Delegates to property setter
        return self

    def getCommunication(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "CpSoftwareCluster") -> "PortElementToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: RefType) -> "PortElementToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getParameterData(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for parameterData.

        Returns:
            The parameterData value

        Note:
            Delegates to parameter_data property (CODING_RULE_V2_00017)
        """
        return self.parameter_data  # Delegates to property

    def setParameterData(self, value: "ParameterData") -> "PortElementToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for parameterData with method chaining.

        Args:
            value: The parameterData to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter_data property setter (gets validation automatically)
        """
        self.parameter_data = value  # Delegates to property setter
        return self

    def getTriggerRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for triggerRef.

        Returns:
            The triggerRef value

        Note:
            Delegates to trigger_ref property (CODING_RULE_V2_00017)
        """
        return self.trigger_ref  # Delegates to property

    def setTriggerRef(self, value: RefType) -> "PortElementToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for triggerRef with method chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger_ref property setter (gets validation automatically)
        """
        self.trigger_ref = value  # Delegates to property setter
        return self

    def getVariableDataSystemInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for variableDataSystemInstanceRef.

        Returns:
            The variableDataSystemInstanceRef value

        Note:
            Delegates to variable_data_system_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.variable_data_system_instance_ref  # Delegates to property

    def setVariableDataSystemInstanceRef(self, value: RefType) -> "PortElementToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for variableDataSystemInstanceRef with method chaining.

        Args:
            value: The variableDataSystemInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable_data_system_instance_ref property setter (gets validation automatically)
        """
        self.variable_data_system_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_client_server_instance_ref(self, value: Optional["ClientServerOperation"]) -> "PortElementToCommunicationResourceMapping":
        """
        Set clientServerInstanceRef and return self for chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server_instance_ref("value")
        """
        self.client_server_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_communication(self, value: Optional["CpSoftwareCluster"]) -> "PortElementToCommunicationResourceMapping":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional[RefType]) -> "PortElementToCommunicationResourceMapping":
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_parameter_data(self, value: Optional["ParameterData"]) -> "PortElementToCommunicationResourceMapping":
        """
        Set parameterData and return self for chaining.

        Args:
            value: The parameterData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter_data("value")
        """
        self.parameter_data = value  # Use property setter (gets validation)
        return self

    def with_trigger_ref(self, value: Optional[RefType]) -> "PortElementToCommunicationResourceMapping":
        """
        Set triggerRef and return self for chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_ref("value")
        """
        self.trigger_ref = value  # Use property setter (gets validation)
        return self

    def with_variable_data_system_instance_ref(self, value: Optional[RefType]) -> "PortElementToCommunicationResourceMapping":
        """
        Set variableDataSystemInstanceRef and return self for chaining.

        Args:
            value: The variableDataSystemInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_data_system_instance_ref("value")
        """
        self.variable_data_system_instance_ref = value  # Use property setter (gets validation)
        return self
