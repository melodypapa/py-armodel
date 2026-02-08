from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import ConstantSpecification
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ConstantSpecificationMapping(ARObject):
    """
    This meta-class is used to create an association of two
    ConstantSpecifications. One Constant Specification is supposed to be defined
    in the application domain while the other should be defined in the
    implementation domain. Hence the ConstantSpecificationMapping needs to be
    used where a ConstantSpecification defined in one domain needs to be
    associated to a ConstantSpecification in the other domain. This information
    is crucial for the RTE generator.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ConstantSpecificationMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 443, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A ConstantSpecification defined in the application.
        self._applConstant: Optional["ConstantSpecification"] = None

    @property
    def appl_constant(self) -> Optional["ConstantSpecification"]:
        """Get applConstant (Pythonic accessor)."""
        return self._applConstant

    @appl_constant.setter
    def appl_constant(self, value: Optional["ConstantSpecification"]) -> None:
        """
        Set applConstant with validation.

        Args:
            value: The applConstant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applConstant = None
            return

        if not isinstance(value, ConstantSpecification):
            raise TypeError(
                f"applConstant must be ConstantSpecification or None, got {type(value).__name__}"
            )
        self._applConstant = value
        # A ConstantSpecification defined in the implementation.
        self._implConstant: Optional["ConstantSpecification"] = None

    @property
    def impl_constant(self) -> Optional["ConstantSpecification"]:
        """Get implConstant (Pythonic accessor)."""
        return self._implConstant

    @impl_constant.setter
    def impl_constant(self, value: Optional["ConstantSpecification"]) -> None:
        """
        Set implConstant with validation.

        Args:
            value: The implConstant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implConstant = None
            return

        if not isinstance(value, ConstantSpecification):
            raise TypeError(
                f"implConstant must be ConstantSpecification or None, got {type(value).__name__}"
            )
        self._implConstant = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplConstant(self) -> "ConstantSpecification":
        """
        AUTOSAR-compliant getter for applConstant.

        Returns:
            The applConstant value

        Note:
            Delegates to appl_constant property (CODING_RULE_V2_00017)
        """
        return self.appl_constant  # Delegates to property

    def setApplConstant(self, value: "ConstantSpecification") -> "ConstantSpecificationMapping":
        """
        AUTOSAR-compliant setter for applConstant with method chaining.

        Args:
            value: The applConstant to set

        Returns:
            self for method chaining

        Note:
            Delegates to appl_constant property setter (gets validation automatically)
        """
        self.appl_constant = value  # Delegates to property setter
        return self

    def getImplConstant(self) -> "ConstantSpecification":
        """
        AUTOSAR-compliant getter for implConstant.

        Returns:
            The implConstant value

        Note:
            Delegates to impl_constant property (CODING_RULE_V2_00017)
        """
        return self.impl_constant  # Delegates to property

    def setImplConstant(self, value: "ConstantSpecification") -> "ConstantSpecificationMapping":
        """
        AUTOSAR-compliant setter for implConstant with method chaining.

        Args:
            value: The implConstant to set

        Returns:
            self for method chaining

        Note:
            Delegates to impl_constant property setter (gets validation automatically)
        """
        self.impl_constant = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_appl_constant(self, value: Optional["ConstantSpecification"]) -> "ConstantSpecificationMapping":
        """
        Set applConstant and return self for chaining.

        Args:
            value: The applConstant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_appl_constant("value")
        """
        self.appl_constant = value  # Use property setter (gets validation)
        return self

    def with_impl_constant(self, value: Optional["ConstantSpecification"]) -> "ConstantSpecificationMapping":
        """
        Set implConstant and return self for chaining.

        Args:
            value: The implConstant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_impl_constant("value")
        """
        self.impl_constant = value  # Use property setter (gets validation)
        return self
