from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Integer,
    NmNode,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class NmCoordinator(ARObject):
    """
    A NM coordinator is an ECU, which is connected to at least two busses, and
    where the requirement exists that shutdown of NM of at least two of these
    busses (also referred to as coordinated busses) has to be performed
    synchronously.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmCoordinator

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 675, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Identification of the NMCoordinator.
        self._index: Optional["Integer"] = None

    @property
    def index(self) -> Optional["Integer"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["Integer"]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"index must be Integer or None, got {type(value).__name__}"
            )
        self._index = value
        # Switch for enabling NmCoordinatorSync (coordination of busses) support.
        self._nmCoordSync: Optional["Boolean"] = None

    @property
    def nm_coord_sync(self) -> Optional["Boolean"]:
        """Get nmCoordSync (Pythonic accessor)."""
        return self._nmCoordSync

    @nm_coord_sync.setter
    def nm_coord_sync(self, value: Optional["Boolean"]) -> None:
        """
        Set nmCoordSync with validation.

        Args:
            value: The nmCoordSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCoordSync = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmCoordSync must be Boolean or None, got {type(value).__name__}"
            )
        self._nmCoordSync = value
        # This attribute defines the maximum shutdown time (in of a connected and
        # coordinated NM-Cluster.
        self._nmGlobal: Optional["TimeValue"] = None

    @property
    def nm_global(self) -> Optional["TimeValue"]:
        """Get nmGlobal (Pythonic accessor)."""
        return self._nmGlobal

    @nm_global.setter
    def nm_global(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmGlobal with validation.

        Args:
            value: The nmGlobal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmGlobal = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmGlobal must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmGlobal = value
        # reference to busses (via NmNodes) that are coordinated NmCoordinator.
        self._nmNode: List["NmNode"] = []

    @property
    def nm_node(self) -> List["NmNode"]:
        """Get nmNode (Pythonic accessor)."""
        return self._nmNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "Integer") -> "NmCoordinator":
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    def getNmCoordSync(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmCoordSync.

        Returns:
            The nmCoordSync value

        Note:
            Delegates to nm_coord_sync property (CODING_RULE_V2_00017)
        """
        return self.nm_coord_sync  # Delegates to property

    def setNmCoordSync(self, value: "Boolean") -> "NmCoordinator":
        """
        AUTOSAR-compliant setter for nmCoordSync with method chaining.

        Args:
            value: The nmCoordSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_coord_sync property setter (gets validation automatically)
        """
        self.nm_coord_sync = value  # Delegates to property setter
        return self

    def getNmGlobal(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmGlobal.

        Returns:
            The nmGlobal value

        Note:
            Delegates to nm_global property (CODING_RULE_V2_00017)
        """
        return self.nm_global  # Delegates to property

    def setNmGlobal(self, value: "TimeValue") -> "NmCoordinator":
        """
        AUTOSAR-compliant setter for nmGlobal with method chaining.

        Args:
            value: The nmGlobal to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_global property setter (gets validation automatically)
        """
        self.nm_global = value  # Delegates to property setter
        return self

    def getNmNode(self) -> List["NmNode"]:
        """
        AUTOSAR-compliant getter for nmNode.

        Returns:
            The nmNode value

        Note:
            Delegates to nm_node property (CODING_RULE_V2_00017)
        """
        return self.nm_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_index(self, value: Optional["Integer"]) -> "NmCoordinator":
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self

    def with_nm_coord_sync(self, value: Optional["Boolean"]) -> "NmCoordinator":
        """
        Set nmCoordSync and return self for chaining.

        Args:
            value: The nmCoordSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_coord_sync("value")
        """
        self.nm_coord_sync = value  # Use property setter (gets validation)
        return self

    def with_nm_global(self, value: Optional["TimeValue"]) -> "NmCoordinator":
        """
        Set nmGlobal and return self for chaining.

        Args:
            value: The nmGlobal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_global("value")
        """
        self.nm_global = value  # Use property setter (gets validation)
        return self
