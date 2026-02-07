from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class CanXlFrameTriggeringProps(ARObject):
    """
    This element indicates the frame being CAN XL and contains further CAN XL
    specific attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication::CanXlFrameTriggeringProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2007, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Acceptance field of a CAN XL message.
        self._acceptanceField: Optional["PositiveInteger"] = None

    @property
    def acceptance_field(self) -> Optional["PositiveInteger"]:
        """Get acceptanceField (Pythonic accessor)."""
        return self._acceptanceField

    @acceptance_field.setter
    def acceptance_field(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set acceptanceField with validation.
        
        Args:
            value: The acceptanceField to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._acceptanceField = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"acceptanceField must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._acceptanceField = value
        # Priority ID of a CAN XL message.
        self._priorityId: Optional["PositiveInteger"] = None

    @property
    def priority_id(self) -> Optional["PositiveInteger"]:
        """Get priorityId (Pythonic accessor)."""
        return self._priorityId

    @priority_id.setter
    def priority_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priorityId with validation.
        
        Args:
            value: The priorityId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priorityId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priorityId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priorityId = value
        # SDU type of a CAN XL message.
        self._sduType: Optional["PositiveInteger"] = None

    @property
    def sdu_type(self) -> Optional["PositiveInteger"]:
        """Get sduType (Pythonic accessor)."""
        return self._sduType

    @sdu_type.setter
    def sdu_type(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sduType with validation.
        
        Args:
            value: The sduType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sduType = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sduType must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sduType = value
        # Virtual CAN network ID of a CAN XL message.
        self._vcid: Optional["PositiveInteger"] = None

    @property
    def vcid(self) -> Optional["PositiveInteger"]:
        """Get vcid (Pythonic accessor)."""
        return self._vcid

    @vcid.setter
    def vcid(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set vcid with validation.
        
        Args:
            value: The vcid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vcid = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"vcid must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._vcid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAcceptanceField(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for acceptanceField.
        
        Returns:
            The acceptanceField value
        
        Note:
            Delegates to acceptance_field property (CODING_RULE_V2_00017)
        """
        return self.acceptance_field  # Delegates to property

    def setAcceptanceField(self, value: "PositiveInteger") -> "CanXlFrameTriggeringProps":
        """
        AUTOSAR-compliant setter for acceptanceField with method chaining.
        
        Args:
            value: The acceptanceField to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to acceptance_field property setter (gets validation automatically)
        """
        self.acceptance_field = value  # Delegates to property setter
        return self

    def getPriorityId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priorityId.
        
        Returns:
            The priorityId value
        
        Note:
            Delegates to priority_id property (CODING_RULE_V2_00017)
        """
        return self.priority_id  # Delegates to property

    def setPriorityId(self, value: "PositiveInteger") -> "CanXlFrameTriggeringProps":
        """
        AUTOSAR-compliant setter for priorityId with method chaining.
        
        Args:
            value: The priorityId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to priority_id property setter (gets validation automatically)
        """
        self.priority_id = value  # Delegates to property setter
        return self

    def getSduType(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sduType.
        
        Returns:
            The sduType value
        
        Note:
            Delegates to sdu_type property (CODING_RULE_V2_00017)
        """
        return self.sdu_type  # Delegates to property

    def setSduType(self, value: "PositiveInteger") -> "CanXlFrameTriggeringProps":
        """
        AUTOSAR-compliant setter for sduType with method chaining.
        
        Args:
            value: The sduType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdu_type property setter (gets validation automatically)
        """
        self.sdu_type = value  # Delegates to property setter
        return self

    def getVcid(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for vcid.
        
        Returns:
            The vcid value
        
        Note:
            Delegates to vcid property (CODING_RULE_V2_00017)
        """
        return self.vcid  # Delegates to property

    def setVcid(self, value: "PositiveInteger") -> "CanXlFrameTriggeringProps":
        """
        AUTOSAR-compliant setter for vcid with method chaining.
        
        Args:
            value: The vcid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vcid property setter (gets validation automatically)
        """
        self.vcid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_acceptance_field(self, value: Optional["PositiveInteger"]) -> "CanXlFrameTriggeringProps":
        """
        Set acceptanceField and return self for chaining.
        
        Args:
            value: The acceptanceField to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_acceptance_field("value")
        """
        self.acceptance_field = value  # Use property setter (gets validation)
        return self

    def with_priority_id(self, value: Optional["PositiveInteger"]) -> "CanXlFrameTriggeringProps":
        """
        Set priorityId and return self for chaining.
        
        Args:
            value: The priorityId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_priority_id("value")
        """
        self.priority_id = value  # Use property setter (gets validation)
        return self

    def with_sdu_type(self, value: Optional["PositiveInteger"]) -> "CanXlFrameTriggeringProps":
        """
        Set sduType and return self for chaining.
        
        Args:
            value: The sduType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdu_type("value")
        """
        self.sdu_type = value  # Use property setter (gets validation)
        return self

    def with_vcid(self, value: Optional["PositiveInteger"]) -> "CanXlFrameTriggeringProps":
        """
        Set vcid and return self for chaining.
        
        Args:
            value: The vcid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vcid("value")
        """
        self.vcid = value  # Use property setter (gets validation)
        return self