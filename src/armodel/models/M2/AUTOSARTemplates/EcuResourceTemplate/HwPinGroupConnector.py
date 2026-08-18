"""
This module contains classes for representing AUTOSAR hardware pin group connectors
in the EcuResourceTemplate module.
"""

from typing import TYPE_CHECKING, List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinConnector import (
        HwPinConnector,
    )


class HwPinGroupConnector(Describable):
    """
    Represents a hardware pin group connector in AUTOSAR hardware descriptions.
    This class defines connections between hardware pin groups.

    Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.9, p.22
    Spec verified: R23-11
    Note: Represents connections at the pin group level with optional detailed pin connections.
    """

    # HwPinGroupConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.9, p.22
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addHwPinConnection           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHwPinConnections          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addHwPinGroupRef             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHwPinGroupRefs            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        """
        Initializes the HwPinGroupConnector.
        """
        super().__init__()

        # Aggregation of detailed pin connections
        self.hwPinConnections: List["HwPinConnector"] = []

        # References to hardware pin groups that are connected
        self.hwPinGroupRefs: List[RefType] = []

    def addHwPinConnection(self, value: "HwPinConnector"):
        """
        Adds a hardware pin connection to this pin group connector.

        A None value is a no-op and does not add an hwPinConnection.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwPinConnections.append(value)
        return self

    def getHwPinConnections(self) -> List["HwPinConnector"]:
        """
        Gets all hardware pin connections in this pin group connector.

        Returns:
            The list of hwPinConnections, or an empty list if none are set
        """
        return self.hwPinConnections

    def addHwPinGroupRef(self, value: RefType):
        """
        Adds a reference to a hardware pin group in this connector.

        A None value is a no-op and does not add an hwPinGroupRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwPinGroupRefs.append(value)
        return self

    def getHwPinGroupRefs(self) -> List[RefType]:
        """
        Gets all hardware pin group references in this connector.

        Returns:
            The list of hwPinGroupRefs, or an empty list if none are set
        """
        return self.hwPinGroupRefs
