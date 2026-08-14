"""
This module contains the SwComponentType base class for AUTOSAR software components.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
        PPortPrototype,
        PortGroup,
        PortPrototype,
        PRPortPrototype,
        RPortPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
        ConsistencyNeeds,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import (
        SwComponentDocumentation,
    )


class SwComponentType(AtpType, ABC):
    """
    Base class for AUTOSAR software components.
    """

    # SwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.1, p.64
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createConsistencyNeeds       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConsistencyNeeds          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createPPortPrototype         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createRPortPrototype         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createPRPortPrototype        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPorts                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPPortPrototypes           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRPortPrototypes           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPRPortPrototypes          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPortPrototypes            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createPortGroup              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPortGroups                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSwcMappingConstraintRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwcMappingConstraintsRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getSwComponentDocumentation   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwComponentDocumentation   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addUnitGroupRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUnitGroupRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is SwComponentType:
            raise TypeError("SwComponentType is an abstract class.")
        super().__init__(parent, short_name)

        # This represents the collection of ConsistencyNeeds owned by the enclosing SwComponentType.
        self.consistencyNeeds: List[ConsistencyNeeds] = []

        # The PortPrototypes through which this SwComponent Type can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        self.ports: List[PortPrototype] = []

        # A port group being part of this component.
        self.portGroups: List[PortGroup] = []

        # Reference to constraints that are valid for this SwComponentType.
        self.swcMappingConstraintsRefs: List[RefType] = []

        # This adds a documentation to the SwComponentType.
        self.swComponentDocumentation: Optional[SwComponentDocumentation] = None

        # This allows for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.
        self.unitGroupRefs: List[RefType] = []

    def createConsistencyNeeds(self, short_name: str) -> ConsistencyNeeds:
        """
        Creates a ConsistencyNeeds owned by the enclosing SwComponentType.
        Returns the existing ConsistencyNeeds when the short name already exists.

        Args:
            short_name: The short name of the ConsistencyNeeds

        Returns:
            The created or existing ConsistencyNeeds
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import ConsistencyNeeds

        if not self.IsElementExists(short_name, ConsistencyNeeds):
            consistency_needs = ConsistencyNeeds(self, short_name)
            self.addElement(consistency_needs)
            self.consistencyNeeds.append(consistency_needs)
        return self.getElement(short_name, ConsistencyNeeds)

    def getConsistencyNeeds(self) -> List[ConsistencyNeeds]:
        """
        Gets the collection of ConsistencyNeeds owned by the enclosing SwComponentType.

        Returns:
            List of ConsistencyNeeds instances
        """
        return self.consistencyNeeds

    def createPPortPrototype(self, short_name: str) -> PPortPrototype:
        """
        Creates a PPortPrototype of this SwComponentType. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing PPortPrototype when the short name already exists.

        Args:
            short_name: The short name of the PPortPrototype

        Returns:
            The created or existing PPortPrototype
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

        if not self.IsElementExists(short_name, PPortPrototype):
            prototype = PPortPrototype(self, short_name)
            self.addElement(prototype)
            self.ports.append(prototype)
        return self.getElement(short_name, PPortPrototype)

    def createRPortPrototype(self, short_name: str) -> RPortPrototype:
        """
        Creates an RPortPrototype of this SwComponentType. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing RPortPrototype when the short name already exists.

        Args:
            short_name: The short name of the RPortPrototype

        Returns:
            The created or existing RPortPrototype
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import RPortPrototype

        if not self.IsElementExists(short_name, RPortPrototype):
            prototype = RPortPrototype(self, short_name)
            self.addElement(prototype)
            self.ports.append(prototype)
        return self.getElement(short_name, RPortPrototype)

    def createPRPortPrototype(self, short_name: str) -> PRPortPrototype:
        """
        Creates a PRPortPrototype of this SwComponentType. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing PRPortPrototype when the short name already exists.

        Args:
            short_name: The short name of the PRPortPrototype

        Returns:
            The created or existing PRPortPrototype
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype

        if not self.IsElementExists(short_name, PRPortPrototype):
            prototype = PRPortPrototype(self, short_name)
            self.addElement(prototype)
            self.ports.append(prototype)
        return self.getElement(short_name, PRPortPrototype)

    def getPorts(self) -> List[PortPrototype]:
        """
        Gets the PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.

        Returns:
            List of PortPrototype instances
        """
        return self.ports

    def getPPortPrototypes(self) -> List[PPortPrototype]:
        """
        Convenience getter for the PPortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of PPortPrototype instances
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

        return list(sorted(filter(lambda c: isinstance(c, PPortPrototype), self.ports), key=lambda o: o.short_name))

    def getRPortPrototypes(self) -> List[RPortPrototype]:
        """
        Convenience getter for the RPortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of RPortPrototype instances
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import RPortPrototype

        return list(sorted(filter(lambda c: isinstance(c, RPortPrototype), self.ports), key=lambda o: o.short_name))

    def getPRPortPrototypes(self) -> List[PRPortPrototype]:
        """
        Convenience getter for the PRPortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of PRPortPrototype instances
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype

        return list(sorted(filter(lambda c: isinstance(c, PRPortPrototype), self.ports), key=lambda o: o.short_name))

    def getPortPrototypes(self) -> List[PortPrototype]:
        """
        Convenience getter for all PortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of PortPrototype instances
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype

        return list(sorted(filter(lambda c: isinstance(c, PortPrototype), self.ports), key=lambda o: o.short_name))

    def createPortGroup(self, short_name: str) -> PortGroup:
        """
        Creates a PortGroup being part of this component.
        Returns the existing PortGroup when the short name already exists.

        Args:
            short_name: The short name of the PortGroup

        Returns:
            The created or existing PortGroup
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortGroup

        if not self.IsElementExists(short_name, PortGroup):
            port_group = PortGroup(self, short_name)
            self.addElement(port_group)
            self.portGroups.append(port_group)
        return self.getElement(short_name, PortGroup)

    def getPortGroups(self) -> List[PortGroup]:
        """
        Gets the PortGroups being part of this component.

        Returns:
            List of PortGroup instances
        """
        return self.portGroups

    def addSwcMappingConstraintRef(self, value: Optional[RefType]) -> "SwComponentType":
        """
        Adds a reference to constraints that are valid for this SwComponentType.
        A None value is a no-op and does not append anything.

        Args:
            value: The SwComponentMappingConstraints reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swcMappingConstraintsRefs.append(value)
        return self

    def getSwcMappingConstraintsRefs(self) -> List[RefType]:
        """
        Gets the references to constraints that are valid for this SwComponentType.

        Returns:
            List of RefType instances
        """
        return self.swcMappingConstraintsRefs

    def getSwComponentDocumentation(self) -> Optional[SwComponentDocumentation]:
        """
        Gets the documentation that is added to the SwComponentType.

        Returns:
            SwComponentDocumentation, or None if not set
        """
        return self.swComponentDocumentation

    def setSwComponentDocumentation(self, value: Optional[SwComponentDocumentation]) -> "SwComponentType":
        """
        Sets the documentation that is added to the SwComponentType.
        A None value is a no-op and does not overwrite an existing documentation.

        Args:
            value: The SwComponentDocumentation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swComponentDocumentation = value
        return self

    def addUnitGroupRef(self, value: Optional[RefType]) -> "SwComponentType":
        """
        Adds a reference which allows for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.
        A None value is a no-op and does not append anything.

        Args:
            value: The UnitGroup reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.unitGroupRefs.append(value)
        return self

    def getUnitGroupRefs(self) -> List[RefType]:
        """
        Gets the references which allow for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.

        Returns:
            List of RefType instances
        """
        return self.unitGroupRefs
