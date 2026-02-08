from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import SwDataDefProps
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DataPrototype(Identifiable, ABC):
    """
    Base class for prototypical roles of any data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::DataPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 311, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 311, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 305, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2013, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataPrototype:
            raise TypeError("DataPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This property allows to specify data definition properties apply on data
        # prototype level.
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

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "DataPrototype":
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

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "DataPrototype":
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
