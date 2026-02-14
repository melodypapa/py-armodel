"""
AUTOSAR Package - InstanceRef

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.__init__ import (
    DataPrototypeReference,
    PortInterface,
)


class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """
    This meta-class represents the ability to refer to the internal structure of
    an AutosarDataPrototype which is typed by an ImplementationDatatype in the
    context of a PortInterface. In other words, this meta-class shall not be
    used to model a reference to the AutosarDataPrototype as a target itself,
    even if the AutosarDataPrototype is typed by an ImplementationDataType and
    even if that ImplementationDataType represents a composite data type.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::ImplementationDataTypeElementInPortInterfaceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 789, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a context in case there are subelements with explicit types.
        # The reference has to be ordered to reflect the nested structure.
        # xml.
        # sequenceOffset=20.
        self._context: List[AbstractImplementation] = []

    @property
    def context(self) -> List[AbstractImplementation]:
        """Get context (Pythonic accessor)."""
        return self._context
        # This refers to the AutosarDataPrototype which is typed by
                # ImplementationDatatype.
        # The targetDataPrototype defined contextDataPrototypes can be found
                # rootDataPrototype.
        self._rootData: Optional[RefType] = None

    @property
    def root_data(self) -> Optional[RefType]:
        """Get rootData (Pythonic accessor)."""
        return self._rootData

    @root_data.setter
    def root_data(self, value: Optional[RefType]) -> None:
        """
        Set rootData with validation.

        Args:
            value: The rootData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootData = None
            return

        self._rootData = value
                # rootDataPrototype is composite and the target is subElement of the
                # rootDataPrototype.
        # xml.
        # sequenceOffset=30.
        self._target: Optional["AbstractImplementation"] = None

    @property
    def target(self) -> Optional["AbstractImplementation"]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional["AbstractImplementation"]) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"target must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._target = value

    def with_context(self, value):
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context_data(self, value):
        """
        Set context_data and return self for chaining.

        Args:
            value: The context_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    def with_context_data(self, value):
        """
        Set context_data and return self for chaining.

        Args:
            value: The context_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    def with_context_data(self, value):
        """
        Set context_data and return self for chaining.

        Args:
            value: The context_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> List[AbstractImplementation]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getRootData(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootData.

        Returns:
            The rootData value

        Note:
            Delegates to root_data property (CODING_RULE_V2_00017)
        """
        return self.root_data  # Delegates to property

    def setRootData(self, value: RefType) -> ImplementationDataTypeElementInPortInterfaceRef:
        """
        AUTOSAR-compliant setter for rootData with method chaining.

        Args:
            value: The rootData to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_data property setter (gets validation automatically)
        """
        self.root_data = value  # Delegates to property setter
        return self

    def getTarget(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "AbstractImplementation") -> ImplementationDataTypeElementInPortInterfaceRef:
        """
        AUTOSAR-compliant setter for target with method chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_root_data(self, value: Optional[RefType]) -> ImplementationDataTypeElementInPortInterfaceRef:
        """
        Set rootData and return self for chaining.

        Args:
            value: The rootData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_data("value")
        """
        self.root_data = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: Optional["AbstractImplementation"]) -> ImplementationDataTypeElementInPortInterfaceRef:
        """
        Set target and return self for chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self



class DataPrototypeInPortInterfaceInstanceRef(ARObject, ABC):
    """
    This meta-class represents the ability to: • refer to a DataPrototype in the
    context of a PortInterface. • refer to the internal structure of a
    DataPrototype which is typed by an ApplicationDatatype in the context of a
    PortInterface.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::DataPrototypeInPortInterfaceInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1009, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataPrototypeInPortInterfaceInstanceRef:
            raise TypeError("DataPrototypeInPortInterfaceInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpAbstract.
        self._abstractBase: Optional["PortInterface"] = None

    @property
    def abstract_base(self) -> Optional["PortInterface"]:
        """Get abstractBase (Pythonic accessor)."""
        return self._abstractBase

    @abstract_base.setter
    def abstract_base(self, value: Optional["PortInterface"]) -> None:
        """
        Set abstractBase with validation.

        Args:
            value: The abstractBase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._abstractBase = None
            return

        if not isinstance(value, PortInterface):
            raise TypeError(
                f"abstractBase must be PortInterface or None, got {type(value).__name__}"
            )
        self._abstractBase = value
        # sequenceOffset=20.
        self._contextData: List[ApplicationComposite] = []

    @property
    def context_data(self) -> List[ApplicationComposite]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # Stereotypes: atpAbstract xml.
        # sequenceOffset=10.
        self._rootData: Optional[RefType] = None

    @property
    def root_data(self) -> Optional[RefType]:
        """Get rootData (Pythonic accessor)."""
        return self._rootData

    @root_data.setter
    def root_data(self, value: Optional[RefType]) -> None:
        """
        Set rootData with validation.

        Args:
            value: The rootData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootData = None
            return

        self._rootData = value
        # sequenceOffset=30.
        self._targetData: RefType = None

    @property
    def target_data(self) -> RefType:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: RefType) -> None:
        """
        Set targetData with validation.

        Args:
            value: The targetData to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbstractBase(self) -> PortInterface:
        """
        AUTOSAR-compliant getter for abstractBase.

        Returns:
            The abstractBase value

        Note:
            Delegates to abstract_base property (CODING_RULE_V2_00017)
        """
        return self.abstract_base  # Delegates to property

    def setAbstractBase(self, value: PortInterface) -> DataPrototypeInPortInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for abstractBase with method chaining.

        Args:
            value: The abstractBase to set

        Returns:
            self for method chaining

        Note:
            Delegates to abstract_base property setter (gets validation automatically)
        """
        self.abstract_base = value  # Delegates to property setter
        return self

    def getContextData(self) -> List[ApplicationComposite]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getRootData(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootData.

        Returns:
            The rootData value

        Note:
            Delegates to root_data property (CODING_RULE_V2_00017)
        """
        return self.root_data  # Delegates to property

    def setRootData(self, value: RefType) -> DataPrototypeInPortInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for rootData with method chaining.

        Args:
            value: The rootData to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_data property setter (gets validation automatically)
        """
        self.root_data = value  # Delegates to property setter
        return self

    def getTargetData(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetData.

        Returns:
            The targetData value

        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: RefType) -> DataPrototypeInPortInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for targetData with method chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data property setter (gets validation automatically)
        """
        self.target_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_abstract_base(self, value: Optional["PortInterface"]) -> DataPrototypeInPortInterfaceInstanceRef:
        """
        Set abstractBase and return self for chaining.

        Args:
            value: The abstractBase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_abstract_base("value")
        """
        self.abstract_base = value  # Use property setter (gets validation)
        return self

    def with_root_data(self, value: Optional[RefType]) -> DataPrototypeInPortInterfaceInstanceRef:
        """
        Set rootData and return self for chaining.

        Args:
            value: The rootData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_data("value")
        """
        self.root_data = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: RefType) -> DataPrototypeInPortInterfaceInstanceRef:
        """
        Set targetData and return self for chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data("value")
        """
        self.target_data = value  # Use property setter (gets validation)
        return self



class DataPrototypeInSenderReceiverInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::DataPrototypeInSenderReceiverInterfaceInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 788, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._baseInterface: Optional["SenderReceiver"] = None

    @property
    def base_interface(self) -> Optional["SenderReceiver"]:
        """Get baseInterface (Pythonic accessor)."""
        return self._baseInterface

    @base_interface.setter
    def base_interface(self, value: Optional["SenderReceiver"]) -> None:
        """
        Set baseInterface with validation.

        Args:
            value: The baseInterface to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseInterface = None
            return

        if not isinstance(value, SenderReceiver):
            raise TypeError(
                f"baseInterface must be SenderReceiver or None, got {type(value).__name__}"
            )
        self._baseInterface = value
        # sequenceOffset=20.
        self._contextData: List[ApplicationComposite] = []

    @property
    def context_data(self) -> List[ApplicationComposite]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # Tags: xml.
        # sequenceOffset=10.
        self._rootDataPrototypeInSr: Optional[RefType] = None

    @property
    def root_data_prototype_in_sr(self) -> Optional[RefType]:
        """Get rootDataPrototypeInSr (Pythonic accessor)."""
        return self._rootDataPrototypeInSr

    @root_data_prototype_in_sr.setter
    def root_data_prototype_in_sr(self, value: Optional[RefType]) -> None:
        """
        Set rootDataPrototypeInSr with validation.

        Args:
            value: The rootDataPrototypeInSr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootDataPrototypeInSr = None
            return

        self._rootDataPrototypeInSr = value
        # sequenceOffset=30.
        self._targetDataPrototypeInSr: Optional[RefType] = None

    @property
    def target_data_prototype_in_sr(self) -> Optional[RefType]:
        """Get targetDataPrototypeInSr (Pythonic accessor)."""
        return self._targetDataPrototypeInSr

    @target_data_prototype_in_sr.setter
    def target_data_prototype_in_sr(self, value: Optional[RefType]) -> None:
        """
        Set targetDataPrototypeInSr with validation.

        Args:
            value: The targetDataPrototypeInSr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetDataPrototypeInSr = None
            return

        self._targetDataPrototypeInSr = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseInterface(self) -> "SenderReceiver":
        """
        AUTOSAR-compliant getter for baseInterface.

        Returns:
            The baseInterface value

        Note:
            Delegates to base_interface property (CODING_RULE_V2_00017)
        """
        return self.base_interface  # Delegates to property

    def setBaseInterface(self, value: "SenderReceiver") -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for baseInterface with method chaining.

        Args:
            value: The baseInterface to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_interface property setter (gets validation automatically)
        """
        self.base_interface = value  # Delegates to property setter
        return self

    def getContextData(self) -> List[ApplicationComposite]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getRootDataPrototypeInSr(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootDataPrototypeInSr.

        Returns:
            The rootDataPrototypeInSr value

        Note:
            Delegates to root_data_prototype_in_sr property (CODING_RULE_V2_00017)
        """
        return self.root_data_prototype_in_sr  # Delegates to property

    def setRootDataPrototypeInSr(self, value: RefType) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for rootDataPrototypeInSr with method chaining.

        Args:
            value: The rootDataPrototypeInSr to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_data_prototype_in_sr property setter (gets validation automatically)
        """
        self.root_data_prototype_in_sr = value  # Delegates to property setter
        return self

    def getTargetDataPrototypeInSr(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetDataPrototypeInSr.

        Returns:
            The targetDataPrototypeInSr value

        Note:
            Delegates to target_data_prototype_in_sr property (CODING_RULE_V2_00017)
        """
        return self.target_data_prototype_in_sr  # Delegates to property

    def setTargetDataPrototypeInSr(self, value: RefType) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for targetDataPrototypeInSr with method chaining.

        Args:
            value: The targetDataPrototypeInSr to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data_prototype_in_sr property setter (gets validation automatically)
        """
        self.target_data_prototype_in_sr = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_interface(self, value: Optional["SenderReceiver"]) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """
        Set baseInterface and return self for chaining.

        Args:
            value: The baseInterface to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_interface("value")
        """
        self.base_interface = value  # Use property setter (gets validation)
        return self

    def with_root_data_prototype_in_sr(self, value: Optional[RefType]) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """
        Set rootDataPrototypeInSr and return self for chaining.

        Args:
            value: The rootDataPrototypeInSr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_data_prototype_in_sr("value")
        """
        self.root_data_prototype_in_sr = value  # Use property setter (gets validation)
        return self

    def with_target_data_prototype_in_sr(self, value: Optional[RefType]) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """
        Set targetDataPrototypeInSr and return self for chaining.

        Args:
            value: The targetDataPrototypeInSr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data_prototype_in_sr("value")
        """
        self.target_data_prototype_in_sr = value  # Use property setter (gets validation)
        return self



class DataPrototypeInClientServerInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::DataPrototypeInClientServerInterfaceInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 788, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["ClientServerInterface"] = None

    @property
    def base(self) -> Optional["ClientServerInterface"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["ClientServerInterface"]) -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, ClientServerInterface):
            raise TypeError(
                f"base must be ClientServerInterface or None, got {type(value).__name__}"
            )
        self._base = value
        # sequenceOffset=20.
        self._contextData: List[ApplicationComposite] = []

    @property
    def context_data(self) -> List[ApplicationComposite]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # Tags: xml.
        # sequenceOffset=10.
        self._rootDataPrototypeInCs: Optional[RefType] = None

    @property
    def root_data_prototype_in_cs(self) -> Optional[RefType]:
        """Get rootDataPrototypeInCs (Pythonic accessor)."""
        return self._rootDataPrototypeInCs

    @root_data_prototype_in_cs.setter
    def root_data_prototype_in_cs(self, value: Optional[RefType]) -> None:
        """
        Set rootDataPrototypeInCs with validation.

        Args:
            value: The rootDataPrototypeInCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootDataPrototypeInCs = None
            return

        self._rootDataPrototypeInCs = value
        # sequenceOffset=30.
        self._targetDataPrototypeInCs: Optional[RefType] = None

    @property
    def target_data_prototype_in_cs(self) -> Optional[RefType]:
        """Get targetDataPrototypeInCs (Pythonic accessor)."""
        return self._targetDataPrototypeInCs

    @target_data_prototype_in_cs.setter
    def target_data_prototype_in_cs(self, value: Optional[RefType]) -> None:
        """
        Set targetDataPrototypeInCs with validation.

        Args:
            value: The targetDataPrototypeInCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetDataPrototypeInCs = None
            return

        self._targetDataPrototypeInCs = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "ClientServerInterface":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "ClientServerInterface") -> DataPrototypeInClientServerInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContextData(self) -> List[ApplicationComposite]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getRootDataPrototypeInCs(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootDataPrototypeInCs.

        Returns:
            The rootDataPrototypeInCs value

        Note:
            Delegates to root_data_prototype_in_cs property (CODING_RULE_V2_00017)
        """
        return self.root_data_prototype_in_cs  # Delegates to property

    def setRootDataPrototypeInCs(self, value: RefType) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for rootDataPrototypeInCs with method chaining.

        Args:
            value: The rootDataPrototypeInCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_data_prototype_in_cs property setter (gets validation automatically)
        """
        self.root_data_prototype_in_cs = value  # Delegates to property setter
        return self

    def getTargetDataPrototypeInCs(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetDataPrototypeInCs.

        Returns:
            The targetDataPrototypeInCs value

        Note:
            Delegates to target_data_prototype_in_cs property (CODING_RULE_V2_00017)
        """
        return self.target_data_prototype_in_cs  # Delegates to property

    def setTargetDataPrototypeInCs(self, value: RefType) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """
        AUTOSAR-compliant setter for targetDataPrototypeInCs with method chaining.

        Args:
            value: The targetDataPrototypeInCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data_prototype_in_cs property setter (gets validation automatically)
        """
        self.target_data_prototype_in_cs = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["ClientServerInterface"]) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_root_data_prototype_in_cs(self, value: Optional[RefType]) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """
        Set rootDataPrototypeInCs and return self for chaining.

        Args:
            value: The rootDataPrototypeInCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_data_prototype_in_cs("value")
        """
        self.root_data_prototype_in_cs = value  # Use property setter (gets validation)
        return self

    def with_target_data_prototype_in_cs(self, value: Optional[RefType]) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """
        Set targetDataPrototypeInCs and return self for chaining.

        Args:
            value: The targetDataPrototypeInCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data_prototype_in_cs("value")
        """
        self.target_data_prototype_in_cs = value  # Use property setter (gets validation)
        return self
