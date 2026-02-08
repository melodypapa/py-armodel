from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SwComponentType

    RefType,
)


class CompositionSwComponentType(SwComponentType):
    """
    A CompositionSwComponentType aggregates SwComponentPrototypes (that in turn
    are typed by SwComponentTypes) as well as SwConnectors for primarily
    connecting SwComponentPrototypes among each others and towards the surface
    of the CompositionSwComponentType. By this means, a hierarchical structures
    of software-components can be created.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 307, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 291, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 75, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 895, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 219, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 21, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 434, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instantiated components that are part of this The aggregation of subject
                # to variability with to support the conditional existence of a be aware: if
                # the of SwComponentPrototypes is the deselected still contained in the but the
                # instances are inactive in that they are by the RTE.
        # is marked as atpSplitable in order to addition of service components to the
                # ECU the ECU integration.
        # case for having 0 components owned by the be to deliver an to e.
        # g.
        # a filling the internal structure.
        # atpVariation.
        self._component: List["SwComponent"] = []

    @property
    def component(self) -> List["SwComponent"]:
        """Get component (Pythonic accessor)."""
        return self._component
        # SwConnectors have the principal ability to establish a PortPrototypes.
        # They can have in the context of a are refined of SwConnectors is subject to
                # the purpose to support variant data flow.
        # is marked as atpSplitable in order to extension of the ECU extract with the
                # ECU atpVariation.
        self._connector: List["SwConnector"] = []

    @property
    def connector(self) -> List["SwConnector"]:
        """Get connector (Pythonic accessor)."""
        return self._connector
        # Reference to the ConstantSpecificationMapping to be applied for initValues of
        # PPortComSpecs and 719 Document ID 673:
        # AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._constantValue: List["ConstantSpecification"] = []

    @property
    def constant_value(self) -> List["ConstantSpecification"]:
        """Get constantValue (Pythonic accessor)."""
        return self._constantValue
        # Reference to the DataTypeMappingSet to be applied the used
                # ApplicationDataTypes in developing subsystems it may happen are used on the
                # surface In this case it reasonable to be able to also provide the to the
                # ImplementationDataTypes.
        # mapping shall be informal and not for the implementors mainly because
                # generator is not concerned about the the mapping of ApplicationDataTypes
                # delegated and inner PortPrototype matches mapping to ImplementationDataTypes
                # is not.
        self._dataType: List[RefType] = []

    @property
    def data_type(self) -> List[RefType]:
        """Get dataType (Pythonic accessor)."""
        return self._dataType
        # This allows to define instantiation specific properties for RTE Events, in
                # particular for instance specific scheduling.
        # atpVariation.
        self._instantiation: List["InstantiationRTEEvent"] = []

    @property
    def instantiation(self) -> List["InstantiationRTEEvent"]:
        """Get instantiation (Pythonic accessor)."""
        return self._instantiation
        # This reference identifies the PhysicalDimensionMappingSet that is applicable
        # in context of the enclosing in the be taken into the assessment of the
        # compatibility of the context of creation of a the scope of the.
        self._physical: Optional["PhysicalDimension"] = None

    @property
    def physical(self) -> Optional["PhysicalDimension"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalDimension"]) -> None:
        """
        Set physical with validation.

        Args:
            value: The physical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalDimension):
            raise TypeError(
                f"physical must be PhysicalDimension or None, got {type(value).__name__}"
            )
        self._physical = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for component.

        Returns:
            The component value

        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def getConnector(self) -> List["SwConnector"]:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def getConstantValue(self) -> List["ConstantSpecification"]:
        """
        AUTOSAR-compliant getter for constantValue.

        Returns:
            The constantValue value

        Note:
            Delegates to constant_value property (CODING_RULE_V2_00017)
        """
        return self.constant_value  # Delegates to property

    def getDataType(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataType.

        Returns:
            The dataType value

        Note:
            Delegates to data_type property (CODING_RULE_V2_00017)
        """
        return self.data_type  # Delegates to property

    def getInstantiation(self) -> List["InstantiationRTEEvent"]:
        """
        AUTOSAR-compliant getter for instantiation.

        Returns:
            The instantiation value

        Note:
            Delegates to instantiation property (CODING_RULE_V2_00017)
        """
        return self.instantiation  # Delegates to property

    def getPhysical(self) -> "PhysicalDimension":
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalDimension") -> "CompositionSwComponentType":
        """
        AUTOSAR-compliant setter for physical with method chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_physical(self, value: Optional["PhysicalDimension"]) -> "CompositionSwComponentType":
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self
