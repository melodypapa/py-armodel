"""
AUTOSAR Package - CryptoDeployment

Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::CryptoDeployment
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CryptoKeySlot(Identifiable):
    """
    This meta-class represents the ability to define a concrete key to be used
    for a crypto operation.

    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::CryptoDeployment::CryptoKeySlot

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 57, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines whether a shadow copy of this Key shall be allocated
        # to enable rollback of a failed Key campaign (see interface BeginTransaction).
        self._allocateShadow: Optional["Boolean"] = None

    @property
    def allocate_shadow(self) -> Optional["Boolean"]:
        """Get allocateShadow (Pythonic accessor)."""
        return self._allocateShadow

    @allocate_shadow.setter
    def allocate_shadow(self, value: Optional["Boolean"]) -> None:
        """
        Set allocateShadow with validation.

        Args:
            value: The allocateShadow to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allocateShadow = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"allocateShadow must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._allocateShadow = value
                # restriction).
        # The algorithm can be family & length, mode, padding.
        # Providers can support some crypto are not well known/ standardized today,
                # doesn’t provide a concrete list of identifiers and doesn’t suppose usage
                # identifiers.
        # Instead of this a provider supplier string names of supported algorithms in
                # The name of a crypto follow the rules defined in the specification for
                # Adaptive Platform.
        # 97 Document ID 980: AUTOSAR_FO_TPS_SecurityExtractTemplate Template R23-11.
        self._cryptoAlgId: Optional["String"] = None

    @property
    def crypto_alg_id(self) -> Optional["String"]:
        """Get cryptoAlgId (Pythonic accessor)."""
        return self._cryptoAlgId

    @crypto_alg_id.setter
    def crypto_alg_id(self, value: Optional["String"]) -> None:
        """
        Set cryptoAlgId with validation.

        Args:
            value: The cryptoAlgId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoAlgId = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"cryptoAlgId must be String or str or None, got {type(value).__name__}"
            )
        self._cryptoAlgId = value
        # If this field "Undefined" then mSlotCapacity must be larger then 0.
        self._cryptoObject: Optional["CryptoObjectTypeEnum"] = None

    @property
    def crypto_object(self) -> Optional["CryptoObjectTypeEnum"]:
        """Get cryptoObject (Pythonic accessor)."""
        return self._cryptoObject

    @crypto_object.setter
    def crypto_object(self, value: Optional["CryptoObjectTypeEnum"]) -> None:
        """
        Set cryptoObject with validation.

        Args:
            value: The cryptoObject to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoObject = None
            return

        if not isinstance(value, CryptoObjectTypeEnum):
            raise TypeError(
                f"cryptoObject must be CryptoObjectTypeEnum or None, got {type(value).__name__}"
            )
        self._cryptoObject = value
        # Status=candidate.
        self._keySlotAllowed: Optional["CryptoKeySlotAllowed"] = None

    @property
    def key_slot_allowed(self) -> Optional["CryptoKeySlotAllowed"]:
        """Get keySlotAllowed (Pythonic accessor)."""
        return self._keySlotAllowed

    @key_slot_allowed.setter
    def key_slot_allowed(self, value: Optional["CryptoKeySlotAllowed"]) -> None:
        """
        Set keySlotAllowed with validation.

        Args:
            value: The keySlotAllowed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySlotAllowed = None
            return

        if not isinstance(value, CryptoKeySlotAllowed):
            raise TypeError(
                f"keySlotAllowed must be CryptoKeySlotAllowed or None, got {type(value).__name__}"
            )
        self._keySlotAllowed = value
        # Tags: atp.
        # Status=candidate.
        self._keySlotContent: List["CryptoKeySlotContent"] = []

    @property
    def key_slot_content(self) -> List["CryptoKeySlotContent"]:
        """Get keySlotContent (Pythonic accessor)."""
        return self._keySlotContent
        # Capacity of the slot in bytes to be reserved by the stack use case is to
                # define this value in case that is undefined and the slot size can deduced
                # from cryptoObjectType and cryptoAlgId.
        # slot size can be deduced from cryptoObject cryptoAlgId.
        self._slotCapacity: Optional["PositiveInteger"] = None

    @property
    def slot_capacity(self) -> Optional["PositiveInteger"]:
        """Get slotCapacity (Pythonic accessor)."""
        return self._slotCapacity

    @slot_capacity.setter
    def slot_capacity(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set slotCapacity with validation.

        Args:
            value: The slotCapacity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slotCapacity = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"slotCapacity must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._slotCapacity = value
        # or whether it is used by Stack managed by a Key Manager Application.
        self._slotType: Optional["CryptoKeySlotType"] = None

    @property
    def slot_type(self) -> Optional["CryptoKeySlotType"]:
        """Get slotType (Pythonic accessor)."""
        return self._slotType

    @slot_type.setter
    def slot_type(self, value: Optional["CryptoKeySlotType"]) -> None:
        """
        Set slotType with validation.

        Args:
            value: The slotType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slotType = None
            return

        if not isinstance(value, CryptoKeySlotType):
            raise TypeError(
                f"slotType must be CryptoKeySlotType or None, got {type(value).__name__}"
            )
        self._slotType = value

    def with_key_slot_content(self, value):
        """
        Set key_slot_content and return self for chaining.

        Args:
            value: The key_slot_content to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_slot_content("value")
        """
        self.key_slot_content = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllocateShadow(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for allocateShadow.

        Returns:
            The allocateShadow value

        Note:
            Delegates to allocate_shadow property (CODING_RULE_V2_00017)
        """
        return self.allocate_shadow  # Delegates to property

    def setAllocateShadow(self, value: "Boolean") -> CryptoKeySlot:
        """
        AUTOSAR-compliant setter for allocateShadow with method chaining.

        Args:
            value: The allocateShadow to set

        Returns:
            self for method chaining

        Note:
            Delegates to allocate_shadow property setter (gets validation automatically)
        """
        self.allocate_shadow = value  # Delegates to property setter
        return self

    def getCryptoAlgId(self) -> "String":
        """
        AUTOSAR-compliant getter for cryptoAlgId.

        Returns:
            The cryptoAlgId value

        Note:
            Delegates to crypto_alg_id property (CODING_RULE_V2_00017)
        """
        return self.crypto_alg_id  # Delegates to property

    def setCryptoAlgId(self, value: "String") -> CryptoKeySlot:
        """
        AUTOSAR-compliant setter for cryptoAlgId with method chaining.

        Args:
            value: The cryptoAlgId to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_alg_id property setter (gets validation automatically)
        """
        self.crypto_alg_id = value  # Delegates to property setter
        return self

    def getCryptoObject(self) -> "CryptoObjectTypeEnum":
        """
        AUTOSAR-compliant getter for cryptoObject.

        Returns:
            The cryptoObject value

        Note:
            Delegates to crypto_object property (CODING_RULE_V2_00017)
        """
        return self.crypto_object  # Delegates to property

    def setCryptoObject(self, value: "CryptoObjectTypeEnum") -> CryptoKeySlot:
        """
        AUTOSAR-compliant setter for cryptoObject with method chaining.

        Args:
            value: The cryptoObject to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_object property setter (gets validation automatically)
        """
        self.crypto_object = value  # Delegates to property setter
        return self

    def getKeySlotAllowed(self) -> "CryptoKeySlotAllowed":
        """
        AUTOSAR-compliant getter for keySlotAllowed.

        Returns:
            The keySlotAllowed value

        Note:
            Delegates to key_slot_allowed property (CODING_RULE_V2_00017)
        """
        return self.key_slot_allowed  # Delegates to property

    def setKeySlotAllowed(self, value: "CryptoKeySlotAllowed") -> CryptoKeySlot:
        """
        AUTOSAR-compliant setter for keySlotAllowed with method chaining.

        Args:
            value: The keySlotAllowed to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_slot_allowed property setter (gets validation automatically)
        """
        self.key_slot_allowed = value  # Delegates to property setter
        return self

    def getKeySlotContent(self) -> List["CryptoKeySlotContent"]:
        """
        AUTOSAR-compliant getter for keySlotContent.

        Returns:
            The keySlotContent value

        Note:
            Delegates to key_slot_content property (CODING_RULE_V2_00017)
        """
        return self.key_slot_content  # Delegates to property

    def getSlotCapacity(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for slotCapacity.

        Returns:
            The slotCapacity value

        Note:
            Delegates to slot_capacity property (CODING_RULE_V2_00017)
        """
        return self.slot_capacity  # Delegates to property

    def setSlotCapacity(self, value: "PositiveInteger") -> CryptoKeySlot:
        """
        AUTOSAR-compliant setter for slotCapacity with method chaining.

        Args:
            value: The slotCapacity to set

        Returns:
            self for method chaining

        Note:
            Delegates to slot_capacity property setter (gets validation automatically)
        """
        self.slot_capacity = value  # Delegates to property setter
        return self

    def getSlotType(self) -> "CryptoKeySlotType":
        """
        AUTOSAR-compliant getter for slotType.

        Returns:
            The slotType value

        Note:
            Delegates to slot_type property (CODING_RULE_V2_00017)
        """
        return self.slot_type  # Delegates to property

    def setSlotType(self, value: "CryptoKeySlotType") -> CryptoKeySlot:
        """
        AUTOSAR-compliant setter for slotType with method chaining.

        Args:
            value: The slotType to set

        Returns:
            self for method chaining

        Note:
            Delegates to slot_type property setter (gets validation automatically)
        """
        self.slot_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_allocate_shadow(self, value: Optional["Boolean"]) -> CryptoKeySlot:
        """
        Set allocateShadow and return self for chaining.

        Args:
            value: The allocateShadow to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allocate_shadow("value")
        """
        self.allocate_shadow = value  # Use property setter (gets validation)
        return self

    def with_crypto_alg_id(self, value: Optional["String"]) -> CryptoKeySlot:
        """
        Set cryptoAlgId and return self for chaining.

        Args:
            value: The cryptoAlgId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_alg_id("value")
        """
        self.crypto_alg_id = value  # Use property setter (gets validation)
        return self

    def with_crypto_object(self, value: Optional["CryptoObjectTypeEnum"]) -> CryptoKeySlot:
        """
        Set cryptoObject and return self for chaining.

        Args:
            value: The cryptoObject to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_object("value")
        """
        self.crypto_object = value  # Use property setter (gets validation)
        return self

    def with_key_slot_allowed(self, value: Optional["CryptoKeySlotAllowed"]) -> CryptoKeySlot:
        """
        Set keySlotAllowed and return self for chaining.

        Args:
            value: The keySlotAllowed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_slot_allowed("value")
        """
        self.key_slot_allowed = value  # Use property setter (gets validation)
        return self

    def with_slot_capacity(self, value: Optional["PositiveInteger"]) -> CryptoKeySlot:
        """
        Set slotCapacity and return self for chaining.

        Args:
            value: The slotCapacity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slot_capacity("value")
        """
        self.slot_capacity = value  # Use property setter (gets validation)
        return self

    def with_slot_type(self, value: Optional["CryptoKeySlotType"]) -> CryptoKeySlot:
        """
        Set slotType and return self for chaining.

        Args:
            value: The slotType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slot_type("value")
        """
        self.slot_type = value  # Use property setter (gets validation)
        return self
