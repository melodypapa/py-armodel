from typing import Optional


class LGraphic(LanguageSpecific):
    """
    This meta-class represents the figure in one particular language.

    Package: M2::MSR::Documentation::BlockElements::Figure

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 307, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the actual graphic represented in the figure.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._graphic: "Graphic" = None

    @property
    def graphic(self) -> "Graphic":
        """Get graphic (Pythonic accessor)."""
        return self._graphic

    @graphic.setter
    def graphic(self, value: "Graphic") -> None:
        """
        Set graphic with validation.

        Args:
            value: The graphic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Graphic):
            raise TypeError(
                f"graphic must be Graphic, got {type(value).__name__}"
            )
        self._graphic = value
        # specific action to each.
        self._map: Optional["Map"] = None

    @property
    def map(self) -> Optional["Map"]:
        """Get map (Pythonic accessor)."""
        return self._map

    @map.setter
    def map(self, value: Optional["Map"]) -> None:
        """
        Set map with validation.

        Args:
            value: The map to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._map = None
            return

        if not isinstance(value, Map):
            raise TypeError(
                f"map must be Map or None, got {type(value).__name__}"
            )
        self._map = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGraphic(self) -> "Graphic":
        """
        AUTOSAR-compliant getter for graphic.

        Returns:
            The graphic value

        Note:
            Delegates to graphic property (CODING_RULE_V2_00017)
        """
        return self.graphic  # Delegates to property

    def setGraphic(self, value: "Graphic") -> "LGraphic":
        """
        AUTOSAR-compliant setter for graphic with method chaining.

        Args:
            value: The graphic to set

        Returns:
            self for method chaining

        Note:
            Delegates to graphic property setter (gets validation automatically)
        """
        self.graphic = value  # Delegates to property setter
        return self

    def getMap(self) -> "Map":
        """
        AUTOSAR-compliant getter for map.

        Returns:
            The map value

        Note:
            Delegates to map property (CODING_RULE_V2_00017)
        """
        return self.map  # Delegates to property

    def setMap(self, value: "Map") -> "LGraphic":
        """
        AUTOSAR-compliant setter for map with method chaining.

        Args:
            value: The map to set

        Returns:
            self for method chaining

        Note:
            Delegates to map property setter (gets validation automatically)
        """
        self.map = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_graphic(self, value: "Graphic") -> "LGraphic":
        """
        Set graphic and return self for chaining.

        Args:
            value: The graphic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_graphic("value")
        """
        self.graphic = value  # Use property setter (gets validation)
        return self

    def with_map(self, value: Optional["Map"]) -> "LGraphic":
        """
        Set map and return self for chaining.

        Args:
            value: The map to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_map("value")
        """
        self.map = value  # Use property setter (gets validation)
        return self
