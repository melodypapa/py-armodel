from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class MsrQueryArg(ARObject):
    """
    This represents an argument to the query. Note that the arguments are not
    standardized and therefore subject to mutual agreement.

    Package: M2::MSR::Documentation::MsrQuery

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 344, Foundation
      R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the value of the argument.
        self._arg: Union[String, str] = None

    @property
    def arg(self) -> Union[String, str]:
        """Get arg (Pythonic accessor)."""
        return self._arg

    @arg.setter
    def arg(self, value: Union[String, str]) -> None:
        """
        Set arg with validation.

        Args:
            value: The arg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"arg must be String or str, got {type(value).__name__}"
            )
        self._arg = value
        self._si: Union[NameToken, str] = None

    @property
    def si(self) -> Union[NameToken, str]:
        """Get si (Pythonic accessor)."""
        return self._si

    @si.setter
    def si(self, value: Union[NameToken, str]) -> None:
        """
        Set si with validation.

        Args:
            value: The si to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"si must be NameToken or str, got {type(value).__name__}"
            )
        self._si = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArg(self) -> Union[String, str]:
        """
        AUTOSAR-compliant getter for arg.

        Returns:
            The arg value

        Note:
            Delegates to arg property (CODING_RULE_V2_00017)
        """
        return self.arg  # Delegates to property

    def setArg(self, value: Union[String, str]) -> "MsrQueryArg":
        """
        AUTOSAR-compliant setter for arg with method chaining.

        Args:
            value: The arg to set

        Returns:
            self for method chaining

        Note:
            Delegates to arg property setter (gets validation automatically)
        """
        self.arg = value  # Delegates to property setter
        return self

    def getSi(self) -> Union[NameToken, str]:
        """
        AUTOSAR-compliant getter for si.

        Returns:
            The si value

        Note:
            Delegates to si property (CODING_RULE_V2_00017)
        """
        return self.si  # Delegates to property

    def setSi(self, value: Union[NameToken, str]) -> "MsrQueryArg":
        """
        AUTOSAR-compliant setter for si with method chaining.

        Args:
            value: The si to set

        Returns:
            self for method chaining

        Note:
            Delegates to si property setter (gets validation automatically)
        """
        self.si = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_arg(self, value: Union[String, str]) -> "MsrQueryArg":
        """
        Set arg and return self for chaining.

        Args:
            value: The arg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arg("value")
        """
        self.arg = value  # Use property setter (gets validation)
        return self

    def with_si(self, value: Union[NameToken, str]) -> "MsrQueryArg":
        """
        Set si and return self for chaining.

        Args:
            value: The si to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_si("value")
        """
        self.si = value  # Use property setter (gets validation)
        return self
