from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    RPortComSpec,
)

    RefType,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ReceiverComSpec(RPortComSpec, ABC):
    """
    that if the receiver does not receive new Data at a consecutive read, then
    the receiver increments the tolerance by 1. Caveat: The E2E wrapper approach
    involves technologies that are not subjected to the AUTOSAR standard and is
    superseded by the superior E2E transformer approach (which is fully
    standardized by AUTOSAR). Hence, new projects (without legacy constraints
    due to carry-over parts) shall use the fully standardized E2E transformer
    approach. Stereotypes: atpVariation vh.latestBindingTime=preCompileTime
    maxNoNewOr PositiveInteger 0..1 attr The maximum amount of missing or
    repeated Data which RepeatedData the receiver does not expect to exceed
    under normal communication conditions. Caveat: The E2E wrapper approach
    involves technologies that are not subjected to the AUTOSAR standard and is
    superseded by the superior E2E transformer approach (which is fully
    standardized by AUTOSAR). Hence, new projects (without legacy constraints
    due to carry-over parts) shall use the fully standardized E2E transformer
    approach. network SwDataDefProps 0..1 aggr A networkRepresentation is used
    to define how the data Representation Element is mapped to a communication
    bus. Stereotypes: atpSplitable receptionProps ReceptionComSpec 0..1 aggr
    "This aggregation represents the definition transmission Props props in the
    context of the enclosing ReceiverComSpec. replaceWith VariableAccess 0..1
    aggr This aggregation is used to identify the AutosarData Prototype to be
    taken for sourcing an external replacement in the out-of-range and
    invalidValue handling. (cid:53) 171 of 1228 Document ID 62:
    AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 170, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2047, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ReceiverComSpec:
            raise TypeError("ReceiverComSpec is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a CompositeNetworkRepresentation defined in the context of a
                # ReceiverComSpec.
        # The of this aggregation is to be able to specify the of leaf elements of
                # Application.
        self._composite: List["CompositeNetwork"] = []

    @property
    def composite(self) -> List["CompositeNetwork"]:
        """Get composite (Pythonic accessor)."""
        return self._composite
        # Data element these attributes belong to.
        self._dataElement: RefType = None

    @property
    def data_element(self) -> RefType:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: RefType) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # situation.
        self._handleOutOf: Optional["HandleOutOfRange"] = None

    @property
    def handle_out_of(self) -> Optional["HandleOutOfRange"]:
        """Get handleOutOf (Pythonic accessor)."""
        return self._handleOutOf

    @handle_out_of.setter
    def handle_out_of(self, value: Optional["HandleOutOfRange"]) -> None:
        """
        Set handleOutOf with validation.

        Args:
            value: The handleOutOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleOutOf = None
            return

        if not isinstance(value, HandleOutOfRange):
            raise TypeError(
                f"handleOutOf must be HandleOutOfRange or None, got {type(value).__name__}"
            )
        self._handleOutOf = value
                # received valid Data, i.
        # e.
        # how many data is accepted.
        # For example, if the Data with counter 1 and MaxDeltaCounter 1, then at the
                # next reception the receiver can accept values 2 and 3, but not 4.
        self._maxDelta: Optional["PositiveInteger"] = None

    @property
    def max_delta(self) -> Optional["PositiveInteger"]:
        """Get maxDelta (Pythonic accessor)."""
        return self._maxDelta

    @max_delta.setter
    def max_delta(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDelta with validation.

        Args:
            value: The maxDelta to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDelta = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxDelta must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxDelta = value
                # received with a valid counter (i.
        # e.
        # the allowed lock-in range) after the an unexpected behavior of a received E2E
                # wrapper approach involves are not subjected to the AUTOSAR is superseded by
                # the superior E2E (which is fully standardized by new projects (without legacy
                # to carry-over parts) shall use the fully transformer approach.
        self._syncCounterInit: Optional["PositiveInteger"] = None

    @property
    def sync_counter_init(self) -> Optional["PositiveInteger"]:
        """Get syncCounterInit (Pythonic accessor)."""
        return self._syncCounterInit

    @sync_counter_init.setter
    def sync_counter_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set syncCounterInit with validation.

        Args:
            value: The syncCounterInit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncCounterInit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"syncCounterInit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._syncCounterInit = value
        # configuration for data transformation.
        self._transformation: List["TransformationCom"] = []

    @property
    def transformation(self) -> List["TransformationCom"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation
        # This indicates whether the corresponding dataElement be transmitted using
                # end-to-end protection.
        # E2E wrapper approach involves are not subjected to the AUTOSAR is superseded
                # by the superior E2E (which is fully standardized by new projects (without
                # legacy to carry-over parts) shall use the fully transformer approach.
        self._usesEndToEnd: Optional["Boolean"] = None

    @property
    def uses_end_to_end(self) -> Optional["Boolean"]:
        """Get usesEndToEnd (Pythonic accessor)."""
        return self._usesEndToEnd

    @uses_end_to_end.setter
    def uses_end_to_end(self, value: Optional["Boolean"]) -> None:
        """
        Set usesEndToEnd with validation.

        Args:
            value: The usesEndToEnd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesEndToEnd = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"usesEndToEnd must be Boolean or None, got {type(value).__name__}"
            )
        self._usesEndToEnd = value

    def with_composite(self, value):
        """
        Set composite and return self for chaining.

        Args:
            value: The composite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_composite("value")
        """
        self.composite = value  # Use property setter (gets validation)
        return self

    def with_transformation(self, value):
        """
        Set transformation and return self for chaining.

        Args:
            value: The transformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformation("value")
        """
        self.transformation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComposite(self) -> List["CompositeNetwork"]:
        """
        AUTOSAR-compliant getter for composite.

        Returns:
            The composite value

        Note:
            Delegates to composite property (CODING_RULE_V2_00017)
        """
        return self.composite  # Delegates to property

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getHandleOutOf(self) -> "HandleOutOfRange":
        """
        AUTOSAR-compliant getter for handleOutOf.

        Returns:
            The handleOutOf value

        Note:
            Delegates to handle_out_of property (CODING_RULE_V2_00017)
        """
        return self.handle_out_of  # Delegates to property

    def setHandleOutOf(self, value: "HandleOutOfRange") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleOutOf with method chaining.

        Args:
            value: The handleOutOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_out_of property setter (gets validation automatically)
        """
        self.handle_out_of = value  # Delegates to property setter
        return self

    def getMaxDelta(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDelta.

        Returns:
            The maxDelta value

        Note:
            Delegates to max_delta property (CODING_RULE_V2_00017)
        """
        return self.max_delta  # Delegates to property

    def setMaxDelta(self, value: "PositiveInteger") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for maxDelta with method chaining.

        Args:
            value: The maxDelta to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_delta property setter (gets validation automatically)
        """
        self.max_delta = value  # Delegates to property setter
        return self

    def getSyncCounterInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for syncCounterInit.

        Returns:
            The syncCounterInit value

        Note:
            Delegates to sync_counter_init property (CODING_RULE_V2_00017)
        """
        return self.sync_counter_init  # Delegates to property

    def setSyncCounterInit(self, value: "PositiveInteger") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for syncCounterInit with method chaining.

        Args:
            value: The syncCounterInit to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_counter_init property setter (gets validation automatically)
        """
        self.sync_counter_init = value  # Delegates to property setter
        return self

    def getTransformation(self) -> List["TransformationCom"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    def getUsesEndToEnd(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for usesEndToEnd.

        Returns:
            The usesEndToEnd value

        Note:
            Delegates to uses_end_to_end property (CODING_RULE_V2_00017)
        """
        return self.uses_end_to_end  # Delegates to property

    def setUsesEndToEnd(self, value: "Boolean") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for usesEndToEnd with method chaining.

        Args:
            value: The usesEndToEnd to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_end_to_end property setter (gets validation automatically)
        """
        self.uses_end_to_end = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> "ReceiverComSpec":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_handle_out_of(self, value: Optional["HandleOutOfRange"]) -> "ReceiverComSpec":
        """
        Set handleOutOf and return self for chaining.

        Args:
            value: The handleOutOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_out_of("value")
        """
        self.handle_out_of = value  # Use property setter (gets validation)
        return self

    def with_max_delta(self, value: Optional["PositiveInteger"]) -> "ReceiverComSpec":
        """
        Set maxDelta and return self for chaining.

        Args:
            value: The maxDelta to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_delta("value")
        """
        self.max_delta = value  # Use property setter (gets validation)
        return self

    def with_sync_counter_init(self, value: Optional["PositiveInteger"]) -> "ReceiverComSpec":
        """
        Set syncCounterInit and return self for chaining.

        Args:
            value: The syncCounterInit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_counter_init("value")
        """
        self.sync_counter_init = value  # Use property setter (gets validation)
        return self

    def with_uses_end_to_end(self, value: Optional["Boolean"]) -> "ReceiverComSpec":
        """
        Set usesEndToEnd and return self for chaining.

        Args:
            value: The usesEndToEnd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_end_to_end("value")
        """
        self.uses_end_to_end = value  # Use property setter (gets validation)
        return self
