"""
AUTOSAR Package - SWmapping

Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SwcToEcuMapping(Identifiable):
    """
    This meta-class is used: • to map SwComponentPrototypes to a specific ECU
    Instance unit, • optionally to map SwComponentPrototypes to a HwElement with
    category ProcessingUnit, • optionally to map SwComponentPrototypes typed by
    SensorActuatorSwComponentType to a Hw Element with category SensorActuator.
    For each combination of ECUInstance and the optional ProcessingUnit and the
    optional SensorActuator only one SwcToEcuMapping shall be used.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::SwcToEcuMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 197, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # to the referenced ECUInstance.
        # If the referenced is a composition, this all atomic software components
                # within the mapped to the ECU.
        # is aditionally a mapping of some SwComponent the Composition to another ECU
                # inner mapping overrides the outer mapping.
        # by: ComponentInSystem.
        self._component: List["SwComponent"] = []

    @property
    def component(self) -> List["SwComponent"]:
        """Get component (Pythonic accessor)."""
        return self._component
        # Optional mapping of SwComponentPrototypes that are by
        # SensorActuatorSwComponentType to a Hw category SensorActuator.
        self._controlledHw: Optional["HwElement"] = None

    @property
    def controlled_hw(self) -> Optional["HwElement"]:
        """Get controlledHw (Pythonic accessor)."""
        return self._controlledHw

    @controlled_hw.setter
    def controlled_hw(self, value: Optional["HwElement"]) -> None:
        """
        Set controlledHw with validation.
        
        Args:
            value: The controlledHw to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._controlledHw = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"controlledHw must be HwElement or None, got {type(value).__name__}"
            )
        self._controlledHw = value
        # Reference to a specific ECU Instance description.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.
        
        Args:
            value: The ecuInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # Optional mapping of software components to individual residing in one ECU.
        # A is described in the ECU Resource the HwElement of HwCategory Processing.
        self._processingUnit: Optional["HwElement"] = None

    @property
    def processing_unit(self) -> Optional["HwElement"]:
        """Get processingUnit (Pythonic accessor)."""
        return self._processingUnit

    @processing_unit.setter
    def processing_unit(self, value: Optional["HwElement"]) -> None:
        """
        Set processingUnit with validation.
        
        Args:
            value: The processingUnit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processingUnit = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"processingUnit must be HwElement or None, got {type(value).__name__}"
            )
        self._processingUnit = value

    def with_sw_comp_to_ecu(self, value):
        """
        Set sw_comp_to_ecu and return self for chaining.

        Args:
            value: The sw_comp_to_ecu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_comp_to_ecu("value")
        """
        self.sw_comp_to_ecu = value  # Use property setter (gets validation)
        return self

    def with_clustered_instance_ref(self, value):
        """
        Set clustered_instance_ref and return self for chaining.

        Args:
            value: The clustered_instance_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_clustered_instance_ref("value")
        """
        self.clustered_instance_ref = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for component.
        
        Returns:
            The component value
        
        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def getControlledHw(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for controlledHw.
        
        Returns:
            The controlledHw value
        
        Note:
            Delegates to controlled_hw property (CODING_RULE_V2_00017)
        """
        return self.controlled_hw  # Delegates to property

    def setControlledHw(self, value: "HwElement") -> "SwcToEcuMapping":
        """
        AUTOSAR-compliant setter for controlledHw with method chaining.
        
        Args:
            value: The controlledHw to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to controlled_hw property setter (gets validation automatically)
        """
        self.controlled_hw = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.
        
        Returns:
            The ecuInstance value
        
        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "SwcToEcuMapping":
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getProcessingUnit(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for processingUnit.
        
        Returns:
            The processingUnit value
        
        Note:
            Delegates to processing_unit property (CODING_RULE_V2_00017)
        """
        return self.processing_unit  # Delegates to property

    def setProcessingUnit(self, value: "HwElement") -> "SwcToEcuMapping":
        """
        AUTOSAR-compliant setter for processingUnit with method chaining.
        
        Args:
            value: The processingUnit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to processing_unit property setter (gets validation automatically)
        """
        self.processing_unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_controlled_hw(self, value: Optional["HwElement"]) -> "SwcToEcuMapping":
        """
        Set controlledHw and return self for chaining.
        
        Args:
            value: The controlledHw to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_controlled_hw("value")
        """
        self.controlled_hw = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "SwcToEcuMapping":
        """
        Set ecuInstance and return self for chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_processing_unit(self, value: Optional["HwElement"]) -> "SwcToEcuMapping":
        """
        Set processingUnit and return self for chaining.
        
        Args:
            value: The processingUnit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_processing_unit("value")
        """
        self.processing_unit = value  # Use property setter (gets validation)
        return self



class SwcToImplMapping(Identifiable):
    """
    Map instances of an AtomicSwComponentType to a specific Implementation.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::SwcToImplMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 199, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a specific Implementation description.
        # to be used by the specified SW This allows to achieve more precise the
                # resource consumption that results from instance of an atomic SW component
                # onto.
        self._component: Optional["SwcImplementation"] = None

    @property
    def component(self) -> Optional["SwcImplementation"]:
        """Get component (Pythonic accessor)."""
        return self._component

    @component.setter
    def component(self, value: Optional["SwcImplementation"]) -> None:
        """
        Set component with validation.
        
        Args:
            value: The component to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._component = None
            return

        if not isinstance(value, SwcImplementation):
            raise TypeError(
                f"component must be SwcImplementation or None, got {type(value).__name__}"
            )
        self._component = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> "SwcImplementation":
        """
        AUTOSAR-compliant getter for component.
        
        Returns:
            The component value
        
        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def setComponent(self, value: "SwcImplementation") -> "SwcToImplMapping":
        """
        AUTOSAR-compliant setter for component with method chaining.
        
        Args:
            value: The component to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to component property setter (gets validation automatically)
        """
        self.component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component(self, value: Optional["SwcImplementation"]) -> "SwcToImplMapping":
        """
        Set component and return self for chaining.
        
        Args:
            value: The component to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_component("value")
        """
        self.component = value  # Use property setter (gets validation)
        return self



class SwcToApplicationPartitionMapping(Identifiable):
    """
    Allows to map a given SwComponentPrototype to a formally defined partition
    at a point in time when the corresponding EcuInstance is not yet known or
    defined.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::SwcToApplicationPartitionMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 200, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an ApplicationPartition to which a Sw is mapped.
        self._application: Optional["ApplicationPartition"] = None

    @property
    def application(self) -> Optional["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationPartition"]) -> None:
        """
        Set application with validation.
        
        Args:
            value: The application to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, ApplicationPartition):
            raise TypeError(
                f"application must be ApplicationPartition or None, got {type(value).__name__}"
            )
        self._application = value
        # mapped to the referenced ApplicationPartition.
        # If the referenced is a composition, this all atomic software components
                # within the mapped to the ApplicationPartition.
        # is additionally a mapping of some SwComponent the Composition to another
                # Application inner mapping overrides the outer mapping.
        # by: ComponentInSystem.
        self._swComponent: Optional["SwComponent"] = None

    @property
    def sw_component(self) -> Optional["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent

    @sw_component.setter
    def sw_component(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponent with validation.
        
        Args:
            value: The swComponent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponent = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponent must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> "ApplicationPartition":
        """
        AUTOSAR-compliant getter for application.
        
        Returns:
            The application value
        
        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationPartition") -> "SwcToApplicationPartitionMapping":
        """
        AUTOSAR-compliant setter for application with method chaining.
        
        Args:
            value: The application to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.
        
        Returns:
            The swComponent value
        
        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> "SwcToApplicationPartitionMapping":
        """
        AUTOSAR-compliant setter for swComponent with method chaining.
        
        Args:
            value: The swComponent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_component property setter (gets validation automatically)
        """
        self.sw_component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional["ApplicationPartition"]) -> "SwcToApplicationPartitionMapping":
        """
        Set application and return self for chaining.
        
        Args:
            value: The application to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_sw_component(self, value: Optional["SwComponent"]) -> "SwcToApplicationPartitionMapping":
        """
        Set swComponent and return self for chaining.
        
        Args:
            value: The swComponent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_component("value")
        """
        self.sw_component = value  # Use property setter (gets validation)
        return self



class ApplicationPartition(ARElement):
    """
    ApplicationPartition to which SwComponentPrototypes are mapped at a point in
    time when the corresponding EcuInstance is not yet known or defined. In a
    later methodology step the Application Partition can be assigned to an
    EcuPartition.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ApplicationPartition
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 200, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    """
    Maps ApplicationPartitions to EcuPartitions. With this mapping an OEM has
    the option to predefine an allocation of Software Components to
    EcuPartitions in the System Design phase. The final and complete assignment
    is described in the OS Configuration.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ApplicationPartitionToEcuPartitionMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 201, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to ApplicationPartitions that are mapped to an.
        self._application: List["ApplicationPartition"] = []

    @property
    def application(self) -> List["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application
        # Reference to EcuPartition to which the Application assigned.
        self._ecuPartition: Optional["EcuPartition"] = None

    @property
    def ecu_partition(self) -> Optional["EcuPartition"]:
        """Get ecuPartition (Pythonic accessor)."""
        return self._ecuPartition

    @ecu_partition.setter
    def ecu_partition(self, value: Optional["EcuPartition"]) -> None:
        """
        Set ecuPartition with validation.
        
        Args:
            value: The ecuPartition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuPartition = None
            return

        if not isinstance(value, EcuPartition):
            raise TypeError(
                f"ecuPartition must be EcuPartition or None, got {type(value).__name__}"
            )
        self._ecuPartition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> List["ApplicationPartition"]:
        """
        AUTOSAR-compliant getter for application.
        
        Returns:
            The application value
        
        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def getEcuPartition(self) -> "EcuPartition":
        """
        AUTOSAR-compliant getter for ecuPartition.
        
        Returns:
            The ecuPartition value
        
        Note:
            Delegates to ecu_partition property (CODING_RULE_V2_00017)
        """
        return self.ecu_partition  # Delegates to property

    def setEcuPartition(self, value: "EcuPartition") -> "ApplicationPartitionToEcuPartitionMapping":
        """
        AUTOSAR-compliant setter for ecuPartition with method chaining.
        
        Args:
            value: The ecuPartition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu_partition property setter (gets validation automatically)
        """
        self.ecu_partition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_partition(self, value: Optional["EcuPartition"]) -> "ApplicationPartitionToEcuPartitionMapping":
        """
        Set ecuPartition and return self for chaining.
        
        Args:
            value: The ecuPartition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu_partition("value")
        """
        self.ecu_partition = value  # Use property setter (gets validation)
        return self



class EcuPartition(Identifiable):
    """
    Partitions are used as error containment regions. They permit the grouping
    of SWCs and resources and allow to describe recovery policies individually
    for each partition. Partitions can be terminated or restarted during
    run-time as a result of a detected error.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::EcuPartition
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 201, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A partition can execute either in CPU user mode (execIn = TRUE) or supervisor
                # mode (execInUser FALSE).
        # In user mode, the partition has a limited memory, to memory mapped hardware
                # and to user mode, the partition is mapped to a.
        self._execInUser: Optional["Boolean"] = None

    @property
    def exec_in_user(self) -> Optional["Boolean"]:
        """Get execInUser (Pythonic accessor)."""
        return self._execInUser

    @exec_in_user.setter
    def exec_in_user(self, value: Optional["Boolean"]) -> None:
        """
        Set execInUser with validation.
        
        Args:
            value: The execInUser to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._execInUser = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"execInUser must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._execInUser = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecInUser(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for execInUser.
        
        Returns:
            The execInUser value
        
        Note:
            Delegates to exec_in_user property (CODING_RULE_V2_00017)
        """
        return self.exec_in_user  # Delegates to property

    def setExecInUser(self, value: "Boolean") -> "EcuPartition":
        """
        AUTOSAR-compliant setter for execInUser with method chaining.
        
        Args:
            value: The execInUser to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to exec_in_user property setter (gets validation automatically)
        """
        self.exec_in_user = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_exec_in_user(self, value: Optional["Boolean"]) -> "EcuPartition":
        """
        Set execInUser and return self for chaining.
        
        Args:
            value: The execInUser to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_exec_in_user("value")
        """
        self.exec_in_user = value  # Use property setter (gets validation)
        return self



class MappingConstraint(ARObject, ABC):
    """
    Different constraints that may be used to limit the mapping of SW components
    to applicable ECUs, Partitions or Cores depending on the mappingScope
    attribute.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::MappingConstraint
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 202, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is MappingConstraint:
            raise TypeError("MappingConstraint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.
        
        Args:
            value: The introduction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "MappingConstraint":
        """
        AUTOSAR-compliant setter for introduction with method chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "MappingConstraint":
        """
        Set introduction and return self for chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self



class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    """
    This meta-class represents the ability to map a J1939ControllerApplication
    to a J1939NmNode. Note that this is similar but not identical to the mapping
    of SwComponentPrototypes to EcuInstances; for J1939 the semantics of an
    EcuInstance itself is basically replaced by a J1939NmNode. (cid:53) 206 of
    2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR
    CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::J1939ControllerApplicationToJ1939NmNodeMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 206, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the J1939 Controller Application that is mapped to the
        # referenced J1939NmNode.
        self._j1939Controller: Optional["J1939Controller"] = None

    @property
    def j1939_controller(self) -> Optional["J1939Controller"]:
        """Get j1939Controller (Pythonic accessor)."""
        return self._j1939Controller

    @j1939_controller.setter
    def j1939_controller(self, value: Optional["J1939Controller"]) -> None:
        """
        Set j1939Controller with validation.
        
        Args:
            value: The j1939Controller to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._j1939Controller = None
            return

        if not isinstance(value, J1939Controller):
            raise TypeError(
                f"j1939Controller must be J1939Controller or None, got {type(value).__name__}"
            )
        self._j1939Controller = value
        # J1939NmNode that is the target of the J1939Controller.
        self._j1939NmNode: Optional["J1939NmNode"] = None

    @property
    def j1939_nm_node(self) -> Optional["J1939NmNode"]:
        """Get j1939NmNode (Pythonic accessor)."""
        return self._j1939NmNode

    @j1939_nm_node.setter
    def j1939_nm_node(self, value: Optional["J1939NmNode"]) -> None:
        """
        Set j1939NmNode with validation.
        
        Args:
            value: The j1939NmNode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._j1939NmNode = None
            return

        if not isinstance(value, J1939NmNode):
            raise TypeError(
                f"j1939NmNode must be J1939NmNode or None, got {type(value).__name__}"
            )
        self._j1939NmNode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getJ1939Controller(self) -> "J1939Controller":
        """
        AUTOSAR-compliant getter for j1939Controller.
        
        Returns:
            The j1939Controller value
        
        Note:
            Delegates to j1939_controller property (CODING_RULE_V2_00017)
        """
        return self.j1939_controller  # Delegates to property

    def setJ1939Controller(self, value: "J1939Controller") -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """
        AUTOSAR-compliant setter for j1939Controller with method chaining.
        
        Args:
            value: The j1939Controller to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to j1939_controller property setter (gets validation automatically)
        """
        self.j1939_controller = value  # Delegates to property setter
        return self

    def getJ1939NmNode(self) -> "J1939NmNode":
        """
        AUTOSAR-compliant getter for j1939NmNode.
        
        Returns:
            The j1939NmNode value
        
        Note:
            Delegates to j1939_nm_node property (CODING_RULE_V2_00017)
        """
        return self.j1939_nm_node  # Delegates to property

    def setJ1939NmNode(self, value: "J1939NmNode") -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """
        AUTOSAR-compliant setter for j1939NmNode with method chaining.
        
        Args:
            value: The j1939NmNode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to j1939_nm_node property setter (gets validation automatically)
        """
        self.j1939_nm_node = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_j1939_controller(self, value: Optional["J1939Controller"]) -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """
        Set j1939Controller and return self for chaining.
        
        Args:
            value: The j1939Controller to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_j1939_controller("value")
        """
        self.j1939_controller = value  # Use property setter (gets validation)
        return self

    def with_j1939_nm_node(self, value: Optional["J1939NmNode"]) -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """
        Set j1939NmNode and return self for chaining.
        
        Args:
            value: The j1939NmNode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_j1939_nm_node("value")
        """
        self.j1939_nm_node = value  # Use property setter (gets validation)
        return self



class J1939ControllerApplication(ARElement):
    """
    This element represents a J1939 controller application.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::J1939ControllerApplication
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 207, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the numerical function id of the application.
        self._functionId: Optional["PositiveInteger"] = None

    @property
    def function_id(self) -> Optional["PositiveInteger"]:
        """Get functionId (Pythonic accessor)."""
        return self._functionId

    @function_id.setter
    def function_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set functionId with validation.
        
        Args:
            value: The functionId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"functionId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._functionId = value
        # typically typed by a CompositionSwComponentType) that the
                # J1939ControllerApplication.
        # by: ComponentInSystem.
        self._swComponent: Optional["SwComponent"] = None

    @property
    def sw_component(self) -> Optional["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent

    @sw_component.setter
    def sw_component(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponent with validation.
        
        Args:
            value: The swComponent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponent = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponent must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for functionId.
        
        Returns:
            The functionId value
        
        Note:
            Delegates to function_id property (CODING_RULE_V2_00017)
        """
        return self.function_id  # Delegates to property

    def setFunctionId(self, value: "PositiveInteger") -> "J1939ControllerApplication":
        """
        AUTOSAR-compliant setter for functionId with method chaining.
        
        Args:
            value: The functionId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to function_id property setter (gets validation automatically)
        """
        self.function_id = value  # Delegates to property setter
        return self

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.
        
        Returns:
            The swComponent value
        
        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> "J1939ControllerApplication":
        """
        AUTOSAR-compliant setter for swComponent with method chaining.
        
        Args:
            value: The swComponent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_component property setter (gets validation automatically)
        """
        self.sw_component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function_id(self, value: Optional["PositiveInteger"]) -> "J1939ControllerApplication":
        """
        Set functionId and return self for chaining.
        
        Args:
            value: The functionId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_function_id("value")
        """
        self.function_id = value  # Use property setter (gets validation)
        return self

    def with_sw_component(self, value: Optional["SwComponent"]) -> "J1939ControllerApplication":
        """
        Set swComponent and return self for chaining.
        
        Args:
            value: The swComponent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_component("value")
        """
        self.sw_component = value  # Use property setter (gets validation)
        return self



class EcuResourceEstimation(ARObject):
    """
    Resource estimations for RTE and BSW of a single ECU instance.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::EcuResourceEstimation
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 260, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Estimation for the resource consumption of the basic.
        self._bswResource: Optional["ResourceConsumption"] = None

    @property
    def bsw_resource(self) -> Optional["ResourceConsumption"]:
        """Get bswResource (Pythonic accessor)."""
        return self._bswResource

    @bsw_resource.setter
    def bsw_resource(self, value: Optional["ResourceConsumption"]) -> None:
        """
        Set bswResource with validation.
        
        Args:
            value: The bswResource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswResource = None
            return

        if not isinstance(value, ResourceConsumption):
            raise TypeError(
                f"bswResource must be ResourceConsumption or None, got {type(value).__name__}"
            )
        self._bswResource = value
        # Reference to the ECU this estimation is done for.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.
        
        Args:
            value: The ecuInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # This represents introductory documentation about the ecu.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.
        
        Args:
            value: The introduction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value
        # Estimation for the resource consumption of the run time.
        self._rteResource: Optional["ResourceConsumption"] = None

    @property
    def rte_resource(self) -> Optional["ResourceConsumption"]:
        """Get rteResource (Pythonic accessor)."""
        return self._rteResource

    @rte_resource.setter
    def rte_resource(self, value: Optional["ResourceConsumption"]) -> None:
        """
        Set rteResource with validation.
        
        Args:
            value: The rteResource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rteResource = None
            return

        if not isinstance(value, ResourceConsumption):
            raise TypeError(
                f"rteResource must be ResourceConsumption or None, got {type(value).__name__}"
            )
        self._rteResource = value
        # References to SwcToEcuMappings that have been taken account for the resource
                # estimations.
        # This way it is define dfferent EcuResourceEstimations with e.
        # g.
        # before and after mapping an component.
        self._swCompToEcu: List["RefType"] = []

    @property
    def sw_comp_to_ecu(self) -> List["RefType"]:
        """Get swCompToEcu (Pythonic accessor)."""
        return self._swCompToEcu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswResource(self) -> "ResourceConsumption":
        """
        AUTOSAR-compliant getter for bswResource.
        
        Returns:
            The bswResource value
        
        Note:
            Delegates to bsw_resource property (CODING_RULE_V2_00017)
        """
        return self.bsw_resource  # Delegates to property

    def setBswResource(self, value: "ResourceConsumption") -> "EcuResourceEstimation":
        """
        AUTOSAR-compliant setter for bswResource with method chaining.
        
        Args:
            value: The bswResource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bsw_resource property setter (gets validation automatically)
        """
        self.bsw_resource = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.
        
        Returns:
            The ecuInstance value
        
        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "EcuResourceEstimation":
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "EcuResourceEstimation":
        """
        AUTOSAR-compliant setter for introduction with method chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    def getRteResource(self) -> "ResourceConsumption":
        """
        AUTOSAR-compliant getter for rteResource.
        
        Returns:
            The rteResource value
        
        Note:
            Delegates to rte_resource property (CODING_RULE_V2_00017)
        """
        return self.rte_resource  # Delegates to property

    def setRteResource(self, value: "ResourceConsumption") -> "EcuResourceEstimation":
        """
        AUTOSAR-compliant setter for rteResource with method chaining.
        
        Args:
            value: The rteResource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rte_resource property setter (gets validation automatically)
        """
        self.rte_resource = value  # Delegates to property setter
        return self

    def getSwCompToEcu(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for swCompToEcu.
        
        Returns:
            The swCompToEcu value
        
        Note:
            Delegates to sw_comp_to_ecu property (CODING_RULE_V2_00017)
        """
        return self.sw_comp_to_ecu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_resource(self, value: Optional["ResourceConsumption"]) -> "EcuResourceEstimation":
        """
        Set bswResource and return self for chaining.
        
        Args:
            value: The bswResource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bsw_resource("value")
        """
        self.bsw_resource = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "EcuResourceEstimation":
        """
        Set ecuInstance and return self for chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "EcuResourceEstimation":
        """
        Set introduction and return self for chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self

    def with_rte_resource(self, value: Optional["ResourceConsumption"]) -> "EcuResourceEstimation":
        """
        Set rteResource and return self for chaining.
        
        Args:
            value: The rteResource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rte_resource("value")
        """
        self.rte_resource = value  # Use property setter (gets validation)
        return self



class ComponentClustering(MappingConstraint):
    """
    Constraint that forces the mapping of all referenced SW component instances
    to the same ECU, Core, Partition depending on the defined mappingScope
    attribute. If mappingScope is not specified then mappingScopeEcu shall be
    assumed.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ComponentClustering
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 203, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # together.
        # by: ComponentInSystem.
        self._clusteredInstanceRef: List["SwComponent"] = []

    @property
    def clustered_instance_ref(self) -> List["SwComponent"]:
        """Get clusteredInstanceRef (Pythonic accessor)."""
        return self._clusteredInstanceRef
        # This attribute indicates whether the ComponentClustering applies to different
        # ECUs, partitions or this attribute is not specified then mappingScope be
        # assumed.
        self._mappingScope: Optional["RefType"] = None

    @property
    def mapping_scope(self) -> Optional["RefType"]:
        """Get mappingScope (Pythonic accessor)."""
        return self._mappingScope

    @mapping_scope.setter
    def mapping_scope(self, value: Optional["RefType"]) -> None:
        """
        Set mappingScope with validation.
        
        Args:
            value: The mappingScope to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappingScope = None
            return

        self._mappingScope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClusteredInstanceRef(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for clusteredInstanceRef.
        
        Returns:
            The clusteredInstanceRef value
        
        Note:
            Delegates to clustered_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.clustered_instance_ref  # Delegates to property

    def getMappingScope(self) -> "RefType":
        """
        AUTOSAR-compliant getter for mappingScope.
        
        Returns:
            The mappingScope value
        
        Note:
            Delegates to mapping_scope property (CODING_RULE_V2_00017)
        """
        return self.mapping_scope  # Delegates to property

    def setMappingScope(self, value: "RefType") -> "ComponentClustering":
        """
        AUTOSAR-compliant setter for mappingScope with method chaining.
        
        Args:
            value: The mappingScope to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mapping_scope property setter (gets validation automatically)
        """
        self.mapping_scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapping_scope(self, value: Optional[RefType]) -> "ComponentClustering":
        """
        Set mappingScope and return self for chaining.
        
        Args:
            value: The mappingScope to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mapping_scope("value")
        """
        self.mapping_scope = value  # Use property setter (gets validation)
        return self



class ComponentSeparation(MappingConstraint):
    """
    Constraint that forces the two referenced SW components (called A and B in
    the following) not to be mapped to the same ECU, Core, Partition depending
    on the defined mappingScope attribute. If mapping Scope is not specified
    then mappingScopeEcu shall be assumed. If a SW component (e.g. A) is a
    composition, none of the atomic SW components making up the A composition
    shall be mapped together with any of the atomic SW components making up the
    B composition. Furthermore, A and B shall be disjoint.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ComponentSeparation
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 205, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates whether the Component constraint applies to
                # different ECUs, cores.
        # If this attribute is not specified then be assumed.
        # 0.
        # 2 iref The two components that have to be mapped to different ECUs by:
                # ComponentInSystem.
        self._mappingScope: Optional["RefType"] = None

    @property
    def mapping_scope(self) -> Optional["RefType"]:
        """Get mappingScope (Pythonic accessor)."""
        return self._mappingScope

    @mapping_scope.setter
    def mapping_scope(self, value: Optional["RefType"]) -> None:
        """
        Set mappingScope with validation.
        
        Args:
            value: The mappingScope to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappingScope = None
            return

        self._mappingScope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMappingScope(self) -> "RefType":
        """
        AUTOSAR-compliant getter for mappingScope.
        
        Returns:
            The mappingScope value
        
        Note:
            Delegates to mapping_scope property (CODING_RULE_V2_00017)
        """
        return self.mapping_scope  # Delegates to property

    def setMappingScope(self, value: "RefType") -> "ComponentSeparation":
        """
        AUTOSAR-compliant setter for mappingScope with method chaining.
        
        Args:
            value: The mappingScope to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mapping_scope property setter (gets validation automatically)
        """
        self.mapping_scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapping_scope(self, value: Optional[RefType]) -> "ComponentSeparation":
        """
        Set mappingScope and return self for chaining.
        
        Args:
            value: The mappingScope to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mapping_scope("value")
        """
        self.mapping_scope = value  # Use property setter (gets validation)
        return self


class MappingScopeEnum(AREnum):
    """
    MappingScopeEnum enumeration

Defines the scope for the mapping constraints. Aggregated by ComponentClustering.mappingScope, ComponentSeparation.mappingScope

Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping
    """
    # The mapping constraint applies to different Cores.
    mappingScopeCore = "0"

    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # The mapping constraint applies to different Ecus.
    mappingScopeEcu = "1"

    # The mapping constraint applies to different Partitions.
    mappingScopePartition = "2"
