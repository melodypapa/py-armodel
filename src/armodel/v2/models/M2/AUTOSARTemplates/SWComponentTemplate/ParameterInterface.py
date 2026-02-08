from typing import List


class ParameterInterface(DataInterface):
    """
    A parameter interface declares a number of parameter and characteristic
    values to be exchanged between parameter components and software components.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ParameterInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 41, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2042, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The ParameterDataPrototype of this ParameterInterface.
        self._parameter: List["ParameterData"] = []

    @property
    def parameter(self) -> List["ParameterData"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParameter(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
