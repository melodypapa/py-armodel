from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class CryptoServicePrimitive(ARElement):
    """
    This meta-class has the ability to represent a crypto primitive.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServicePrimitive

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 376, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 59, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a description of the family (e.
        # g.
        # crypto algorithm implemented by the crypto.
        self._algorithmFamily: Optional["String"] = None

    @property
    def algorithm_family(self) -> Optional["String"]:
        """Get algorithmFamily (Pythonic accessor)."""
        return self._algorithmFamily

    @algorithm_family.setter
    def algorithm_family(self, value: Optional["String"]) -> None:
        """
        Set algorithmFamily with validation.

        Args:
            value: The algorithmFamily to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmFamily = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"algorithmFamily must be String or None, got {type(value).__name__}"
            )
        self._algorithmFamily = value
        # This attribute represents a description of the mode of the implemented by the
        # crypto primitive.
        self._algorithmMode: Optional["String"] = None

    @property
    def algorithm_mode(self) -> Optional["String"]:
        """Get algorithmMode (Pythonic accessor)."""
        return self._algorithmMode

    @algorithm_mode.setter
    def algorithm_mode(self, value: Optional["String"]) -> None:
        """
        Set algorithmMode with validation.

        Args:
            value: The algorithmMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmMode = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"algorithmMode must be String or None, got {type(value).__name__}"
            )
        self._algorithmMode = value
        # This attribute represents a further description of the family of crypto
                # algorithm implemented by the primitive.
        # family is needed for the specification of algorithm for a signature check, e.
        # g.
        # using RSA.
        self._algorithm: Optional["String"] = None

    @property
    def algorithm(self) -> Optional["String"]:
        """Get algorithm (Pythonic accessor)."""
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value: Optional["String"]) -> None:
        """
        Set algorithm with validation.

        Args:
            value: The algorithm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithm = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"algorithm must be String or None, got {type(value).__name__}"
            )
        self._algorithm = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlgorithmFamily(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithmFamily.

        Returns:
            The algorithmFamily value

        Note:
            Delegates to algorithm_family property (CODING_RULE_V2_00017)
        """
        return self.algorithm_family  # Delegates to property

    def setAlgorithmFamily(self, value: "String") -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant setter for algorithmFamily with method chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_family property setter (gets validation automatically)
        """
        self.algorithm_family = value  # Delegates to property setter
        return self

    def getAlgorithmMode(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithmMode.

        Returns:
            The algorithmMode value

        Note:
            Delegates to algorithm_mode property (CODING_RULE_V2_00017)
        """
        return self.algorithm_mode  # Delegates to property

    def setAlgorithmMode(self, value: "String") -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant setter for algorithmMode with method chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_mode property setter (gets validation automatically)
        """
        self.algorithm_mode = value  # Delegates to property setter
        return self

    def getAlgorithm(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithm.

        Returns:
            The algorithm value

        Note:
            Delegates to algorithm property (CODING_RULE_V2_00017)
        """
        return self.algorithm  # Delegates to property

    def setAlgorithm(self, value: "String") -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant setter for algorithm with method chaining.

        Args:
            value: The algorithm to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm property setter (gets validation automatically)
        """
        self.algorithm = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional["String"]) -> "CryptoServicePrimitive":
        """
        Set algorithmFamily and return self for chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_family("value")
        """
        self.algorithm_family = value  # Use property setter (gets validation)
        return self

    def with_algorithm_mode(self, value: Optional["String"]) -> "CryptoServicePrimitive":
        """
        Set algorithmMode and return self for chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_mode("value")
        """
        self.algorithm_mode = value  # Use property setter (gets validation)
        return self

    def with_algorithm(self, value: Optional["String"]) -> "CryptoServicePrimitive":
        """
        Set algorithm and return self for chaining.

        Args:
            value: The algorithm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm("value")
        """
        self.algorithm = value  # Use property setter (gets validation)
        return self
