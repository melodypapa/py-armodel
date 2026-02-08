from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DataTransformation(Identifiable):
    """
    A DataTransformation represents a transformer chain. It is an ordered list
    of transformers.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 149, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 763, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the kind of DataTransformation to be applied.
        self._data: Optional["DataTransformationKind"] = None

    @property
    def data(self) -> Optional["DataTransformationKind"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["DataTransformationKind"]) -> None:
        """
        Set data with validation.

        Args:
            value: The data to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        if not isinstance(value, DataTransformationKind):
            raise TypeError(
                f"data must be DataTransformationKind or None, got {type(value).__name__}"
            )
        self._data = value
        # Specifies whether the transformer chain is executed even no input data are
                # available.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._executeDespite: Optional["Boolean"] = None

    @property
    def execute_despite(self) -> Optional["Boolean"]:
        """Get executeDespite (Pythonic accessor)."""
        return self._executeDespite

    @execute_despite.setter
    def execute_despite(self, value: Optional["Boolean"]) -> None:
        """
        Set executeDespite with validation.

        Args:
            value: The executeDespite to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executeDespite = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"executeDespite must be Boolean or None, got {type(value).__name__}"
            )
        self._executeDespite = value
        # This attribute represents the definition of a chain of Technology
        # transformers that are supposed to be executed according order of being
        # referenced from DataTransformation.
        self._transformer: List["Transformation"] = []

    @property
    def transformer(self) -> List["Transformation"]:
        """Get transformer (Pythonic accessor)."""
        return self._transformer

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "DataTransformationKind":
        """
        AUTOSAR-compliant getter for data.

        Returns:
            The data value

        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "DataTransformationKind") -> "DataTransformation":
        """
        AUTOSAR-compliant setter for data with method chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    def getExecuteDespite(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for executeDespite.

        Returns:
            The executeDespite value

        Note:
            Delegates to execute_despite property (CODING_RULE_V2_00017)
        """
        return self.execute_despite  # Delegates to property

    def setExecuteDespite(self, value: "Boolean") -> "DataTransformation":
        """
        AUTOSAR-compliant setter for executeDespite with method chaining.

        Args:
            value: The executeDespite to set

        Returns:
            self for method chaining

        Note:
            Delegates to execute_despite property setter (gets validation automatically)
        """
        self.execute_despite = value  # Delegates to property setter
        return self

    def getTransformer(self) -> List["Transformation"]:
        """
        AUTOSAR-compliant getter for transformer.

        Returns:
            The transformer value

        Note:
            Delegates to transformer property (CODING_RULE_V2_00017)
        """
        return self.transformer  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional["DataTransformationKind"]) -> "DataTransformation":
        """
        Set data and return self for chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self

    def with_execute_despite(self, value: Optional["Boolean"]) -> "DataTransformation":
        """
        Set executeDespite and return self for chaining.

        Args:
            value: The executeDespite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_execute_despite("value")
        """
        self.execute_despite = value  # Use property setter (gets validation)
        return self
