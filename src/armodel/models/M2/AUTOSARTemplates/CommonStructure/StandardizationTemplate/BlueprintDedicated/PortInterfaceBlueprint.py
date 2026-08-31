from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

__all__ = ["PortInterfaceBlueprintMapping"]


class PortInterfaceBlueprintMapping(AtpBlueprintMapping):
    """
    This meta-class represents the ability to map two PortInterfaces of which one acts as the blueprint for the other.
    """

    # PortInterfaceBlueprintMapping method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType PORT-INTERFACE-BLUEPRINT-MAPPING l.92477, group l.92440 (XSD-only; no own table in repo corpus; atp.Status="removed")
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPortInterfaceBlueprintRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortInterfaceBlueprintRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDerivedPortInterfaceRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDerivedPortInterfaceRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the interface blueprint. Note that this interface needs to live in a package of category BLUEPRINT.
        self.portInterfaceBlueprintRef: Optional[RefType] = None

        # This represents the derived interface.
        self.derivedPortInterfaceRef: Optional[RefType] = None

    def getPortInterfaceBlueprintRef(self) -> Optional[RefType]:
        """
        This represents the interface blueprint. Note that this interface needs to live in a package of category BLUEPRINT.
        """
        return self.portInterfaceBlueprintRef

    def setPortInterfaceBlueprintRef(self, value: Optional[RefType]) -> "PortInterfaceBlueprintMapping":
        """
        This represents the interface blueprint. Note that this interface needs to live in a package of category BLUEPRINT. A None value is a no-op and is not set.
        """
        if value is not None:
            self.portInterfaceBlueprintRef = value
        return self

    def getDerivedPortInterfaceRef(self) -> Optional[RefType]:
        """
        This represents the derived interface.
        """
        return self.derivedPortInterfaceRef

    def setDerivedPortInterfaceRef(self, value: Optional[RefType]) -> "PortInterfaceBlueprintMapping":
        """
        This represents the derived interface. A None value is a no-op and is not set.
        """
        if value is not None:
            self.derivedPortInterfaceRef = value
        return self
