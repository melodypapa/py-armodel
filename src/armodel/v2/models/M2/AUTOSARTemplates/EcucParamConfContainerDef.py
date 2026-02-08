from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucContainerDef

    RefType,
)


class EcucParamConfContainerDef(EcucContainerDef):
    """
    Used to define configuration containers that can hierarchically contain
    other containers and/or parameter definitions.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucParamConfContainerDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 39, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The parameters defined within the EcucParamConf.
        self._parameter: List["EcucParameterDef"] = []

    @property
    def parameter(self) -> List["EcucParameterDef"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter
        # The references defined within the EcucParamConf.
        self._reference: List[RefType] = []

    @property
    def reference(self) -> List[RefType]:
        """Get reference (Pythonic accessor)."""
        return self._reference
        # The containers defined within the EcucParamConf.
        self._subContainer: List["EcucContainerDef"] = []

    @property
    def sub_container(self) -> List["EcucContainerDef"]:
        """Get subContainer (Pythonic accessor)."""
        return self._subContainer

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParameter(self) -> List["EcucParameterDef"]:
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def getReference(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for reference.

        Returns:
            The reference value

        Note:
            Delegates to reference property (CODING_RULE_V2_00017)
        """
        return self.reference  # Delegates to property

    def getSubContainer(self) -> List["EcucContainerDef"]:
        """
        AUTOSAR-compliant getter for subContainer.

        Returns:
            The subContainer value

        Note:
            Delegates to sub_container property (CODING_RULE_V2_00017)
        """
        return self.sub_container  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
