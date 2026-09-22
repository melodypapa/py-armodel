from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    PositiveInteger,
    String,
)

__all__ = [
    "CryptoKeySlot",
    "CryptoKeySlotAllowedModification",
    "CryptoKeySlotContentAllowedUsage",
    "CryptoKeySlotTypeEnum",
    "CryptoObjectTypeEnum",
]


class CryptoObjectTypeEnum(AREnum):
    """
    Enumeration of all types of crypto objects, i.e. types of content that can be stored to a key slot. Tags: atp.Status=candidate
    """

    # CryptoObjectTypeEnum method parity checklist:
    # Spec: CryptoObjectTypeEnum derived from AUTOSAR_00052.xsd (XSD-only; no own table in repo corpus), line 132716
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CryptoKeySlot.cryptoObjectType

    # Object type unknown Tags: atp.EnumerationLiteralIndex=0 atp.Status=candidate
    UNDEFINED = "UNDEFINED"

    # cryp::SymmetricKey object Tags: atp.EnumerationLiteralIndex=1 atp.Status=candidate
    SYMMETRIC_KEY = "SYMMETRIC-KEY"

    # cryp::PrivateKey object Tags: atp.EnumerationLiteralIndex=2 atp.Status=candidate
    PRIVATE_KEY = "PRIVATE-KEY"

    # cryp::PublicKey object Tags: atp.EnumerationLiteralIndex=3 atp.Status=candidate
    PUBLIC_KEY = "PUBLIC-KEY"

    # cryp::Signature object (asymmetric digital signature or symmetric MAC/HMAC) Tags: atp.EnumerationLiteralIndex=4 atp.Status=candidate
    SIGNATURE = "SIGNATURE"

    # cryp::SecretSeed object Tags: atp.EnumerationLiteralIndex=5 atp.Status=candidate
    SECRET_SEED = "SECRET-SEED"

    def __init__(self):
        super().__init__(
            [
                CryptoObjectTypeEnum.UNDEFINED,
                CryptoObjectTypeEnum.SYMMETRIC_KEY,
                CryptoObjectTypeEnum.PRIVATE_KEY,
                CryptoObjectTypeEnum.PUBLIC_KEY,
                CryptoObjectTypeEnum.SIGNATURE,
                CryptoObjectTypeEnum.SECRET_SEED,
            ]
        )


class CryptoKeySlotTypeEnum(AREnum):
    """
    This enumeration defines the options for the usage of a Key Slot in the platform. Tags: atp.Status=candidate
    """

    # CryptoKeySlotTypeEnum method parity checklist:
    # Spec: CryptoKeySlotTypeEnum derived from AUTOSAR_00052.xsd (XSD-only; no own table in repo corpus), line 132660
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CryptoKeySlot.slotType

    # Key slot is used by platform modules only. The application manages the key but is not able to use the key. Tags: atp.EnumerationLiteralIndex=0 atp.Status=candidate
    MACHINE = "MACHINE"

    # KeySlot is used and modified exclusively by the Application. Tags: atp.EnumerationLiteralIndex=1 atp.Status=candidate
    APPLICATION = "APPLICATION"

    def __init__(self):
        super().__init__(
            [
                CryptoKeySlotTypeEnum.MACHINE,
                CryptoKeySlotTypeEnum.APPLICATION,
            ]
        )


class CryptoKeySlotAllowedModification(ARObject):
    """
    This meta-class restricts the allowed modification of a key stored in the key slot. Tags: atp.Status=candidate
    """

    # CryptoKeySlotAllowedModification method parity checklist:
    # Spec: CryptoKeySlotAllowedModification derived from AUTOSAR_00052.xsd (XSD-only; no own table in repo corpus), line 25744
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAllowContentTypeChange    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAllowContentTypeChange    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExportability    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExportability    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumberOfAllowedUpdates    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumberOfAllowedUpdates    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRestrictUpdate    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRestrictUpdate    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute describes whether the key content type can be changed (true) or not (false), e.g. changing the key from symmetric to RSA.
        self.allowContentTypeChange: Optional[Boolean] = None

        # This attribute describes whether the key slot content is allowed to be exported or not.
        self.exportability: Optional[Boolean] = None

        # This attribute describes the maximum updates that are allowed to the slot.
        self.maxNumberOfAllowedUpdates: Optional[PositiveInteger] = None

        # This attribute defines whether restrictions on the number of updates are defined or not. * false: no restriction is placed on the number of updates. * true: restrictions are placed on the number of updates with the attribute maxNumberOfAllowedUpdates.
        self.restrictUpdate: Optional[Boolean] = None

    def getAllowContentTypeChange(self) -> Optional[Boolean]:
        """This attribute describes whether the key content type can be changed (true) or not (false), e.g. changing the key from symmetric to RSA."""
        return self.allowContentTypeChange

    def setAllowContentTypeChange(self, value: Optional[Boolean]) -> "CryptoKeySlotAllowedModification":
        """
        This attribute describes whether the key content type can be changed (true) or not (false), e.g. changing the key from symmetric to RSA.
        A None value is a no-op and does not overwrite an existing allowContentTypeChange.
        """
        if value is not None:
            self.allowContentTypeChange = value
        return self

    def getExportability(self) -> Optional[Boolean]:
        """This attribute describes whether the key slot content is allowed to be exported or not."""
        return self.exportability

    def setExportability(self, value: Optional[Boolean]) -> "CryptoKeySlotAllowedModification":
        """
        This attribute describes whether the key slot content is allowed to be exported or not.
        A None value is a no-op and does not overwrite an existing exportability.
        """
        if value is not None:
            self.exportability = value
        return self

    def getMaxNumberOfAllowedUpdates(self) -> Optional[PositiveInteger]:
        """This attribute describes the maximum updates that are allowed to the slot."""
        return self.maxNumberOfAllowedUpdates

    def setMaxNumberOfAllowedUpdates(self, value: Optional[PositiveInteger]) -> "CryptoKeySlotAllowedModification":
        """
        This attribute describes the maximum updates that are allowed to the slot.
        A None value is a no-op and does not overwrite an existing maxNumberOfAllowedUpdates.
        """
        if value is not None:
            self.maxNumberOfAllowedUpdates = value
        return self

    def getRestrictUpdate(self) -> Optional[Boolean]:
        """This attribute defines whether restrictions on the number of updates are defined or not. * false: no restriction is placed on the number of updates. * true: restrictions are placed on the number of updates with the attribute maxNumberOfAllowedUpdates."""
        return self.restrictUpdate

    def setRestrictUpdate(self, value: Optional[Boolean]) -> "CryptoKeySlotAllowedModification":
        """
        This attribute defines whether restrictions on the number of updates are defined or not. * false: no restriction is placed on the number of updates. * true: restrictions are placed on the number of updates with the attribute maxNumberOfAllowedUpdates.
        A None value is a no-op and does not overwrite an existing restrictUpdate.
        """
        if value is not None:
            self.restrictUpdate = value
        return self


class CryptoKeySlotContentAllowedUsage(ARObject):
    """
    This meta-class restricts the allowed usage of a key stored in the key slot. Tags: atp.Status=candidate
    """

    # CryptoKeySlotContentAllowedUsage method parity checklist:
    # Spec: CryptoKeySlotContentAllowedUsage derived from AUTOSAR_00052.xsd (XSD-only; no own table in repo corpus), line 25795
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAllowedKeyslotUsage    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAllowedKeyslotUsage    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines for which operations the KeySlot may be used.
        self.allowedKeyslotUsage: Optional[String] = None

    def getAllowedKeyslotUsage(self) -> Optional[String]:
        """This attribute defines for which operations the KeySlot may be used."""
        return self.allowedKeyslotUsage

    def setAllowedKeyslotUsage(self, value: Optional[String]) -> "CryptoKeySlotContentAllowedUsage":
        """
        This attribute defines for which operations the KeySlot may be used.
        A None value is a no-op and does not overwrite an existing allowedKeyslotUsage.
        """
        if value is not None:
            self.allowedKeyslotUsage = value
        return self


class CryptoKeySlot(Identifiable):
    """
    This meta-class represents the ability to define a concrete key to be used for a crypto operation. Tags: atp.ManifestKind=MachineManifest
    """

    # CryptoKeySlot method parity checklist:
    # Spec: AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf, Table B.5, p.58
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAllocateShadowCopy    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAllocateShadowCopy    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCryptoAlgId    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCryptoAlgId    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCryptoObjectType    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCryptoObjectType    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeySlotAllowedModification    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setKeySlotAllowedModification    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addKeySlotContentAllowedUsage    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeySlotContentAllowedUsages    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSlotCapacity    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSlotCapacity    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSlotType    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSlotType    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines whether a shadow copy of this Key Slot shall be allocated to enable rollback of a failed Key Slot update campaign (see interface BeginTransaction).
        self.allocateShadowCopy: Optional[Boolean] = None

        # This attribute defines a crypto algorithm restriction (kAlgIdAny means without restriction). The algorithm can be specified partially: family & length, mode, padding. Future Crypto Providers can support some crypto algorithms that are not well known/ standardized today, therefore AUTOSAR doesn't provide a concrete list of crypto algorithms' identifiers and doesn't suppose usage of numerical identifiers. Instead of this a provider supplier should provide string names of supported algorithms in accompanying documentation. The name of a crypto algorithm shall follow the rules defined in the specification of cryptography for Adaptive Platform.
        self.cryptoAlgId: Optional[String] = None

        # Object type that can be stored in the slot. If this field contains "Undefined" then mSlotCapacity must be provided and larger then 0. Tags: atp.Status=candidate
        self.cryptoObjectType: Optional[CryptoObjectTypeEnum] = None

        # Restricts how this keySlot may be used Tags: atp.Status=candidate
        self.keySlotAllowedModification: Optional[CryptoKeySlotAllowedModification] = None

        # Restriction of allowed usage of a key stored to the slot. Tags: atp.Status=candidate
        self.keySlotContentAllowedUsages: List[CryptoKeySlotContentAllowedUsage] = []

        # Capacity of the slot in bytes to be reserved by the stack vendor. One use case is to define this value in case that the cryptoObjectType is undefined and the slot size can not be deduced from cryptoObjectType and cryptoAlgId. "0" means slot size can be deduced from cryptoObjectType and cryptoAlgId.
        self.slotCapacity: Optional[PositiveInteger] = None

        # This attribute defines whether the keySlot is exclusively used by the Application; or whether it is used by Stack Services and managed by a Key Manager Application. Tags: atp.Status=candidate
        self.slotType: Optional[CryptoKeySlotTypeEnum] = None

    def getAllocateShadowCopy(self) -> Optional[Boolean]:
        """This attribute defines whether a shadow copy of this Key Slot shall be allocated to enable rollback of a failed Key Slot update campaign (see interface BeginTransaction)."""
        return self.allocateShadowCopy

    def setAllocateShadowCopy(self, value: Optional[Boolean]) -> "CryptoKeySlot":
        """
        This attribute defines whether a shadow copy of this Key Slot shall be allocated to enable rollback of a failed Key Slot update campaign (see interface BeginTransaction).
        A None value is a no-op and does not overwrite an existing allocateShadowCopy.
        """
        if value is not None:
            self.allocateShadowCopy = value
        return self

    def getCryptoAlgId(self) -> Optional[String]:
        """This attribute defines a crypto algorithm restriction (kAlgIdAny means without restriction). The algorithm can be specified partially: family & length, mode, padding. Future Crypto Providers can support some crypto algorithms that are not well known/ standardized today, therefore AUTOSAR doesn't provide a concrete list of crypto algorithms' identifiers and doesn't suppose usage of numerical identifiers. Instead of this a provider supplier should provide string names of supported algorithms in accompanying documentation. The name of a crypto algorithm shall follow the rules defined in the specification of cryptography for Adaptive Platform."""
        return self.cryptoAlgId

    def setCryptoAlgId(self, value: Optional[String]) -> "CryptoKeySlot":
        """
        This attribute defines a crypto algorithm restriction (kAlgIdAny means without restriction). The algorithm can be specified partially: family & length, mode, padding. Future Crypto Providers can support some crypto algorithms that are not well known/ standardized today, therefore AUTOSAR doesn't provide a concrete list of crypto algorithms' identifiers and doesn't suppose usage of numerical identifiers. Instead of this a provider supplier should provide string names of supported algorithms in accompanying documentation. The name of a crypto algorithm shall follow the rules defined in the specification of cryptography for Adaptive Platform.
        A None value is a no-op and does not overwrite an existing cryptoAlgId.
        """
        if value is not None:
            self.cryptoAlgId = value
        return self

    def getCryptoObjectType(self) -> Optional[CryptoObjectTypeEnum]:
        """Object type that can be stored in the slot. If this field contains "Undefined" then mSlotCapacity must be provided and larger then 0. Tags: atp.Status=candidate"""
        return self.cryptoObjectType

    def setCryptoObjectType(self, value: Optional[CryptoObjectTypeEnum]) -> "CryptoKeySlot":
        """
        Object type that can be stored in the slot. If this field contains "Undefined" then mSlotCapacity must be provided and larger then 0. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing cryptoObjectType.
        """
        if value is not None:
            self.cryptoObjectType = value
        return self

    def getKeySlotAllowedModification(self) -> Optional[CryptoKeySlotAllowedModification]:
        """Restricts how this keySlot may be used Tags: atp.Status=candidate"""
        return self.keySlotAllowedModification

    def setKeySlotAllowedModification(self, value: Optional[CryptoKeySlotAllowedModification]) -> "CryptoKeySlot":
        """
        Restricts how this keySlot may be used Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing keySlotAllowedModification.
        """
        if value is not None:
            self.keySlotAllowedModification = value
        return self

    def addKeySlotContentAllowedUsage(self, value: Optional[CryptoKeySlotContentAllowedUsage]) -> "CryptoKeySlot":
        """
        Restriction of allowed usage of a key stored to the slot. Tags: atp.Status=candidate
        A None value is a no-op and does not extend the keySlotContentAllowedUsages list.
        """
        if value is not None:
            self.keySlotContentAllowedUsages.append(value)
        return self

    def getKeySlotContentAllowedUsages(self) -> List[CryptoKeySlotContentAllowedUsage]:
        """Restriction of allowed usage of a key stored to the slot. Tags: atp.Status=candidate"""
        return self.keySlotContentAllowedUsages

    def getSlotCapacity(self) -> Optional[PositiveInteger]:
        """Capacity of the slot in bytes to be reserved by the stack vendor. One use case is to define this value in case that the cryptoObjectType is undefined and the slot size can not be deduced from cryptoObjectType and cryptoAlgId. "0" means slot size can be deduced from cryptoObjectType and cryptoAlgId."""
        return self.slotCapacity

    def setSlotCapacity(self, value: Optional[PositiveInteger]) -> "CryptoKeySlot":
        """
        Capacity of the slot in bytes to be reserved by the stack vendor. One use case is to define this value in case that the cryptoObjectType is undefined and the slot size can not be deduced from cryptoObjectType and cryptoAlgId. "0" means slot size can be deduced from cryptoObjectType and cryptoAlgId.
        A None value is a no-op and does not overwrite an existing slotCapacity.
        """
        if value is not None:
            self.slotCapacity = value
        return self

    def getSlotType(self) -> Optional[CryptoKeySlotTypeEnum]:
        """This attribute defines whether the keySlot is exclusively used by the Application; or whether it is used by Stack Services and managed by a Key Manager Application. Tags: atp.Status=candidate"""
        return self.slotType

    def setSlotType(self, value: Optional[CryptoKeySlotTypeEnum]) -> "CryptoKeySlot":
        """
        This attribute defines whether the keySlot is exclusively used by the Application; or whether it is used by Stack Services and managed by a Key Manager Application. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing slotType.
        """
        if value is not None:
            self.slotType = value
        return self
