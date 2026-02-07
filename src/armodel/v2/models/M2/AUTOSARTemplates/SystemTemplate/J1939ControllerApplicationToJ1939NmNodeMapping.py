from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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