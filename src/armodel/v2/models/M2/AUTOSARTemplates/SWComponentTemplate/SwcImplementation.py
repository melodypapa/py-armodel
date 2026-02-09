"""
AUTOSAR Package - SwcImplementation

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwcImplementation(Implementation):
    """
    This meta-class represents a specialization of the general Implementation
    meta-class with respect to the usage in application software.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation::SwcImplementation
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 344, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 623, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2069, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The internal behavior implemented by this 381 Document ID 89:
        # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._behavior: Optional["SwcInternalBehavior"] = None

    @property
    def behavior(self) -> Optional["SwcInternalBehavior"]:
        """Get behavior (Pythonic accessor)."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: Optional["SwcInternalBehavior"]) -> None:
        """
        Set behavior with validation.
        
        Args:
            value: The behavior to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"behavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._behavior = value
                # implementation.
        # The aggregation of PerInstance subject to variability with the purpose to in
                # the software components different algorithms in the requiring different
                # number of memory this case PerInstanceMemory.
        # atpVariation.
        self._perInstance: List["PerInstanceMemory"] = []

    @property
    def per_instance(self) -> List["PerInstanceMemory"]:
        """Get perInstance (Pythonic accessor)."""
        return self._perInstance
        # Identify a specific RTE vendor.
        # This information is important at the time of integrating (in the application
                # code with the RTE.
        # The that (if the association exists) the has been created to fit to the
                # provided by this specific vendor.
        # integrate the code with another RTE vendor mode is in general not possible.
        self._required: Optional["String"] = None

    @property
    def required(self) -> Optional["String"]:
        """Get required (Pythonic accessor)."""
        return self._required

    @required.setter
    def required(self, value: Optional["String"]) -> None:
        """
        Set required with validation.
        
        Args:
            value: The required to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._required = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"required must be String or str or None, got {type(value).__name__}"
            )
        self._required = value

    def with_per_instance(self, value):
        """
        Set per_instance and return self for chaining.

        Args:
            value: The per_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_per_instance("value")
        """
        self.per_instance = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehavior(self) -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant getter for behavior.
        
        Returns:
            The behavior value
        
        Note:
            Delegates to behavior property (CODING_RULE_V2_00017)
        """
        return self.behavior  # Delegates to property

    def setBehavior(self, value: "SwcInternalBehavior") -> "SwcImplementation":
        """
        AUTOSAR-compliant setter for behavior with method chaining.
        
        Args:
            value: The behavior to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to behavior property setter (gets validation automatically)
        """
        self.behavior = value  # Delegates to property setter
        return self

    def getPerInstance(self) -> List["PerInstanceMemory"]:
        """
        AUTOSAR-compliant getter for perInstance.
        
        Returns:
            The perInstance value
        
        Note:
            Delegates to per_instance property (CODING_RULE_V2_00017)
        """
        return self.per_instance  # Delegates to property

    def getRequired(self) -> "String":
        """
        AUTOSAR-compliant getter for required.
        
        Returns:
            The required value
        
        Note:
            Delegates to required property (CODING_RULE_V2_00017)
        """
        return self.required  # Delegates to property

    def setRequired(self, value: "String") -> "SwcImplementation":
        """
        AUTOSAR-compliant setter for required with method chaining.
        
        Args:
            value: The required to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to required property setter (gets validation automatically)
        """
        self.required = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior(self, value: Optional["SwcInternalBehavior"]) -> "SwcImplementation":
        """
        Set behavior and return self for chaining.
        
        Args:
            value: The behavior to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_behavior("value")
        """
        self.behavior = value  # Use property setter (gets validation)
        return self

    def with_required(self, value: Optional["String"]) -> "SwcImplementation":
        """
        Set required and return self for chaining.
        
        Args:
            value: The required to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_required("value")
        """
        self.required = value  # Use property setter (gets validation)
        return self



class PerInstanceMemorySize(ARObject):
    """
    Resources needed by the allocation of PerInstanceMemory for each SWC
    instance. Note that these resources are not covered by an ObjectFileSection,
    because they are supposed to be allocated by the RTE.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation::PerInstanceMemorySize
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 623, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Required alignment (1,2,4,.
        # ) of the referenced Per byte.
        self._alignment: Optional["PositiveInteger"] = None

    @property
    def alignment(self) -> Optional["PositiveInteger"]:
        """Get alignment (Pythonic accessor)."""
        return self._alignment

    @alignment.setter
    def alignment(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set alignment with validation.
        
        Args:
            value: The alignment to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alignment = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"alignment must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._alignment = value
        self._perInstanceMemory: Optional["PerInstanceMemory"] = None

    @property
    def per_instance_memory(self) -> Optional["PerInstanceMemory"]:
        """Get perInstanceMemory (Pythonic accessor)."""
        return self._perInstanceMemory

    @per_instance_memory.setter
    def per_instance_memory(self, value: Optional["PerInstanceMemory"]) -> None:
        """
        Set perInstanceMemory with validation.
        
        Args:
            value: The perInstanceMemory to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._perInstanceMemory = None
            return

        if not isinstance(value, PerInstanceMemory):
            raise TypeError(
                f"perInstanceMemory must be PerInstanceMemory or None, got {type(value).__name__}"
            )
        self._perInstanceMemory = value
        # The PerInstanceMemorySize is subject to the purpose to support variability in
                # the implementations.
        # Different the implementation might require a different.
        self._size: Optional["PositiveInteger"] = None

    @property
    def size(self) -> Optional["PositiveInteger"]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set size with validation.
        
        Args:
            value: The size to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"size must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._size = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlignment(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for alignment.
        
        Returns:
            The alignment value
        
        Note:
            Delegates to alignment property (CODING_RULE_V2_00017)
        """
        return self.alignment  # Delegates to property

    def setAlignment(self, value: "PositiveInteger") -> "PerInstanceMemorySize":
        """
        AUTOSAR-compliant setter for alignment with method chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to alignment property setter (gets validation automatically)
        """
        self.alignment = value  # Delegates to property setter
        return self

    def getPerInstanceMemory(self) -> "PerInstanceMemory":
        """
        AUTOSAR-compliant getter for perInstanceMemory.
        
        Returns:
            The perInstanceMemory value
        
        Note:
            Delegates to per_instance_memory property (CODING_RULE_V2_00017)
        """
        return self.per_instance_memory  # Delegates to property

    def setPerInstanceMemory(self, value: "PerInstanceMemory") -> "PerInstanceMemorySize":
        """
        AUTOSAR-compliant setter for perInstanceMemory with method chaining.
        
        Args:
            value: The perInstanceMemory to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to per_instance_memory property setter (gets validation automatically)
        """
        self.per_instance_memory = value  # Delegates to property setter
        return self

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.
        
        Returns:
            The size value
        
        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "PerInstanceMemorySize":
        """
        AUTOSAR-compliant setter for size with method chaining.
        
        Args:
            value: The size to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alignment(self, value: Optional["PositiveInteger"]) -> "PerInstanceMemorySize":
        """
        Set alignment and return self for chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_alignment("value")
        """
        self.alignment = value  # Use property setter (gets validation)
        return self

    def with_per_instance_memory(self, value: Optional["PerInstanceMemory"]) -> "PerInstanceMemorySize":
        """
        Set perInstanceMemory and return self for chaining.
        
        Args:
            value: The perInstanceMemory to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_per_instance_memory("value")
        """
        self.per_instance_memory = value  # Use property setter (gets validation)
        return self

    def with_size(self, value: Optional["PositiveInteger"]) -> "PerInstanceMemorySize":
        """
        Set size and return self for chaining.
        
        Args:
            value: The size to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self
