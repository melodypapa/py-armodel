from abc import ABC
from typing import Any, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class IdsPlatformInstantiation(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class for platform modules that
    implement the intrusion detection system. Tags: atp.Status=candidate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 63, Foundation R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IdsPlatformInstantiation:
            raise TypeError("IdsPlatformInstantiation is an abstract class.")
        super().__init__(parent, short_name)

        # Type: PlatformModule.
        # This association contains the network configuration that shall be applied to
        # an instance of an IDS entity.
        # atp.
        # Status=candidate.
        self.networks: List[Any] = []
        # Type: TimeBaseResource.
        # This reference identifies the applicable time base atpVariation.
        self.timeBases: Optional[Any] = None

    def getNetworks(self) -> List[Any]:
        return self.networks

    def setNetworks(self, value: List[Any]) -> "IdsPlatformInstantiation":
        self.networks = value
        return self

    def addNetwork(self, value: Any) -> "IdsPlatformInstantiation":
        """Adds a value to the networks list."""
        self.networks.append(value)
        return self

    def getTimeBases(self) -> Any:
        return self.timeBases

    def setTimeBases(self, value: Any) -> "IdsPlatformInstantiation":
        self.timeBases = value
        return self
