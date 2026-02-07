from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwServiceArg(Identifiable):
    """
    Specifies the properties of a data object exchanged during the call of an
    SwService, e.g. an argument or a return value. The SwServiceArg can also be
    used in the argument list of a C-macro. For this purpose the category shall
    be set to "MACRO". A reference to implementationDataType can optional be
    added if the actual argument has an implementationDataType.

    Package: M2::MSR::DataDictionary::ServiceProcessTask::SwServiceArg

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 38, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 312, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1006, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 472, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 215, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the direction of the data transfer.
        # The direction indicate the direction of the actual information that is by the
                # caller and/or the callee, not the formal arguments in C.
        # is optional for backwards compatibility example, if a pointer is used to pass
                # a for the expected result, the direction "out".
        # If a pointer is used to pass a memory content to be read by the callee, its
                # direction "in".
        self._direction: Optional["ArgumentDirection"] = None

    @property
    def direction(self) -> Optional["ArgumentDirection"]:
        """Get direction (Pythonic accessor)."""
        return self._direction

    @direction.setter
    def direction(self, value: Optional["ArgumentDirection"]) -> None:
        """
        Set direction with validation.

        Args:
            value: The direction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._direction = None
            return

        if not isinstance(value, ArgumentDirection):
            raise TypeError(
                f"direction must be ArgumentDirection or None, got {type(value).__name__}"
            )
        self._direction = value
        # This turns the argument of the service to an array.
        self._swArraysize: RefType = None

    @property
    def sw_arraysize(self) -> RefType:
        """Get swArraysize (Pythonic accessor)."""
        return self._swArraysize

    @sw_arraysize.setter
    def sw_arraysize(self, value: RefType) -> None:
        """
        Set swArraysize with validation.

        Args:
            value: The swArraysize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swArraysize = None
            return

        self._swArraysize = value
        # Data properties of this SwServiceArg.
        # atpSplitable.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.

        Args:
            value: The swDataDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirection(self) -> "ArgumentDirection":
        """
        AUTOSAR-compliant getter for direction.

        Returns:
            The direction value

        Note:
            Delegates to direction property (CODING_RULE_V2_00017)
        """
        return self.direction  # Delegates to property

    def setDirection(self, value: "ArgumentDirection") -> "SwServiceArg":
        """
        AUTOSAR-compliant setter for direction with method chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Note:
            Delegates to direction property setter (gets validation automatically)
        """
        self.direction = value  # Delegates to property setter
        return self

    def getSwArraysize(self) -> RefType:
        """
        AUTOSAR-compliant getter for swArraysize.

        Returns:
            The swArraysize value

        Note:
            Delegates to sw_arraysize property (CODING_RULE_V2_00017)
        """
        return self.sw_arraysize  # Delegates to property

    def setSwArraysize(self, value: RefType) -> "SwServiceArg":
        """
        AUTOSAR-compliant setter for swArraysize with method chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_arraysize property setter (gets validation automatically)
        """
        self.sw_arraysize = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "SwServiceArg":
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direction(self, value: Optional["ArgumentDirection"]) -> "SwServiceArg":
        """
        Set direction and return self for chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direction("value")
        """
        self.direction = value  # Use property setter (gets validation)
        return self

    def with_sw_arraysize(self, value: Optional[RefType]) -> "SwServiceArg":
        """
        Set swArraysize and return self for chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_arraysize("value")
        """
        self.sw_arraysize = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "SwServiceArg":
        """
        Set swDataDef and return self for chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self
