from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification


class ApplicationValueSpecification(ValueSpecification):
    """
    This meta-class represents values for DataPrototypes typed by
    ApplicationDataTypes (this includes in particular compound primitives). For
    further details refer to ASAM CDF 2.0. This meta-class corresponds to some
    extent with SW-INSTANCE in ASAM CDF 2.0.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ApplicationValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 299, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 455, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies to which category of ApplicationDataType this be applied (e.
        # g.
        # as an thus imposing constraints on the structure of the contained values, see
                # [constr_1006] 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
                # Template R23-11.
        self._category: Optional["Identifier"] = None

    @property
    def category(self) -> Optional["Identifier"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["Identifier"]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"category must be Identifier or None, got {type(value).__name__}"
            )
        self._category = value
        # This represents the axis values of a Compound Primitive Type (curve or map).
        # swAxisCont describes the x-axis, the second sw the y-axis, the third
                # swAxisCont z-axis.
        # In addition to this, the axis can be swAxisIndex.
        self._swAxisCont: List["SwAxisCont"] = []

    @property
    def sw_axis_cont(self) -> List["SwAxisCont"]:
        """Get swAxisCont (Pythonic accessor)."""
        return self._swAxisCont
        # This represents the values of a Compound Primitive Data.
        self._swValueCont: Optional["SwValueCont"] = None

    @property
    def sw_value_cont(self) -> Optional["SwValueCont"]:
        """Get swValueCont (Pythonic accessor)."""
        return self._swValueCont

    @sw_value_cont.setter
    def sw_value_cont(self, value: Optional["SwValueCont"]) -> None:
        """
        Set swValueCont with validation.

        Args:
            value: The swValueCont to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swValueCont = None
            return

        if not isinstance(value, SwValueCont):
            raise TypeError(
                f"swValueCont must be SwValueCont or None, got {type(value).__name__}"
            )
        self._swValueCont = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "Identifier") -> "ApplicationValueSpecification":
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getSwAxisCont(self) -> List["SwAxisCont"]:
        """
        AUTOSAR-compliant getter for swAxisCont.

        Returns:
            The swAxisCont value

        Note:
            Delegates to sw_axis_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_cont  # Delegates to property

    def getSwValueCont(self) -> "SwValueCont":
        """
        AUTOSAR-compliant getter for swValueCont.

        Returns:
            The swValueCont value

        Note:
            Delegates to sw_value_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_value_cont  # Delegates to property

    def setSwValueCont(self, value: "SwValueCont") -> "ApplicationValueSpecification":
        """
        AUTOSAR-compliant setter for swValueCont with method chaining.

        Args:
            value: The swValueCont to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_value_cont property setter (gets validation automatically)
        """
        self.sw_value_cont = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional["Identifier"]) -> "ApplicationValueSpecification":
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_sw_value_cont(self, value: Optional["SwValueCont"]) -> "ApplicationValueSpecification":
        """
        Set swValueCont and return self for chaining.

        Args:
            value: The swValueCont to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_value_cont("value")
        """
        self.sw_value_cont = value  # Use property setter (gets validation)
        return self
