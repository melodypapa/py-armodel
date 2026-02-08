from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DataTransformation,
    FibexElement,
    ISignal,
    TransformationISignal,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ISignalGroup(FibexElement):
    """
    SignalGroup of the Interaction Layer. The RTE supports a "signal fan-out"
    where the same System Signal Group is sent in different SignalIPdus to
    multiple receivers. An ISignalGroup refers to a set of ISignals that shall
    always be kept together. A ISignalGroup represents a COM Signal Group.
    Therefore it is recommended to put the ISignalGroup in the same Package as
    ISignals (see atp.recommendedPackage)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalGroup

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 993, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 323, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional reference to a DataTransformation which the transformer chain that
                # is used to transform data that shall be placed inside this ISignalGroup the
                # COMBasedTransformer approach.
        # atpVariation.
        self._comBased: Optional["DataTransformation"] = None

    @property
    def com_based(self) -> Optional["DataTransformation"]:
        """Get comBased (Pythonic accessor)."""
        return self._comBased

    @com_based.setter
    def com_based(self, value: Optional["DataTransformation"]) -> None:
        """
        Set comBased with validation.

        Args:
            value: The comBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._comBased = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"comBased must be DataTransformation or None, got {type(value).__name__}"
            )
        self._comBased = value
        # Reference to a set of ISignals that shall always be kept.
        self._iSignal: List["ISignal"] = []

    @property
    def i_signal(self) -> List["ISignal"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal
        # Reference to the SystemSignalGroup that is defined on level and that is
        # supposed to be transmitted in the.
        self._systemSignal: RefType = None

    @property
    def system_signal(self) -> RefType:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: RefType) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        self._systemSignal = value
        # A transformer chain consists of an ordered list of transformers.
        # The ISignalGroup specific configuration each transformer are defined in the
                # The transformer that are common for all ISignal described in the
                # TransformationTechnology.
        self._transformation: List["TransformationISignal"] = []

    @property
    def transformation(self) -> List["TransformationISignal"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComBased(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for comBased.

        Returns:
            The comBased value

        Note:
            Delegates to com_based property (CODING_RULE_V2_00017)
        """
        return self.com_based  # Delegates to property

    def setComBased(self, value: "DataTransformation") -> "ISignalGroup":
        """
        AUTOSAR-compliant setter for comBased with method chaining.

        Args:
            value: The comBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to com_based property setter (gets validation automatically)
        """
        self.com_based = value  # Delegates to property setter
        return self

    def getISignal(self) -> List["ISignal"]:
        """
        AUTOSAR-compliant getter for iSignal.

        Returns:
            The iSignal value

        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def getSystemSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: RefType) -> "ISignalGroup":
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    def getTransformation(self) -> List["TransformationISignal"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_com_based(self, value: Optional["DataTransformation"]) -> "ISignalGroup":
        """
        Set comBased and return self for chaining.

        Args:
            value: The comBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com_based("value")
        """
        self.com_based = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional[RefType]) -> "ISignalGroup":
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self
