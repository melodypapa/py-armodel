from typing import Any, List, Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment.CryptoKeySlotContent import (
    CryptoKeySlotContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)


class CryptoKeySlot(Identifiable):
    """
    This meta-class represents the ability to define a concrete key to be used
    for a crypto operation. Tags: atp.ManifestKind=MachineManifest

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 57, Foundation R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines whether a shadow copy of this Key shall be allocated
        # to enable rollback of a failed Key campaign (see interface BeginTransaction).
        self.allocateShadows: Optional[Boolean] = None
        # This attribute defines a crypto algorithm restriction (kAlgId without
        # restriction).
        # The algorithm can be family & length, mode, padding.
        # Providers can support some crypto are not well known/ standardized today,
        # doesn’t provide a concrete list of identifiers and doesn’t suppose usage
        # identifiers.
        # Instead of this a provider supplier string names of supported algorithms in
        # The name of a crypto follow the rules defined in the specification for
        # Adaptive Platform.
        # 97 Document ID 980: AUTOSAR_FO_TPS_SecurityExtractTemplate Template R23-11.
        self.cryptoAlgIds: Optional[String] = None
        # Type: CryptoObjectTypeEnum.
        # Object type that can be stored in the slot.
        # If this field "Undefined" then mSlotCapacity must be larger then 0.
        self.cryptoObjects: Optional[Any] = None
        # Type: CryptoKeySlotAllowed.
        # Restricts how this keySlot may be used Tags: atp.
        # Status=candidate.
        self.keySlotAlloweds: Optional[Any] = None
        # Type: CryptoKeySlotContent.
        # Restriction of allowed usage of a key stored to the slot.
        # Tags: atp.
        # Status=candidate.
        self.keySlotContents: List[Any] = []
        # Capacity of the slot in bytes to be reserved by the stack use case is to
        # define this value in case that is undefined and the slot size can deduced
        # from cryptoObjectType and cryptoAlgId.
        # slot size can be deduced from cryptoObject cryptoAlgId.
        self.slotCapacitys: Optional[PositiveInteger] = None
        # Type: CryptoKeySlotType.
        # This attribute defines whether the keySlot is exclusively by the Application;
        # or whether it is used by Stack managed by a Key Manager Application.
        self.slotTypes: Optional[Any] = None

    def getAllocateShadows(self) -> Boolean:
        return self.allocateShadows

    def setAllocateShadows(self, value: Boolean) -> "CryptoKeySlot":
        self.allocateShadows = value
        return self

    def getCryptoAlgIds(self) -> String:
        return self.cryptoAlgIds

    def setCryptoAlgIds(self, value: String) -> "CryptoKeySlot":
        self.cryptoAlgIds = value
        return self

    def getCryptoObjects(self) -> Any:
        return self.cryptoObjects

    def setCryptoObjects(self, value: Any) -> "CryptoKeySlot":
        self.cryptoObjects = value
        return self

    def getKeySlotAlloweds(self) -> Any:
        return self.keySlotAlloweds

    def setKeySlotAlloweds(self, value: Any) -> "CryptoKeySlot":
        self.keySlotAlloweds = value
        return self

    def getKeySlotContents(self) -> List[Any]:
        return self.keySlotContents

    def setKeySlotContents(self, value: List[Any]) -> "CryptoKeySlot":
        self.keySlotContents = value
        return self

    def createKeySlotContent(self, short_name: str) -> CryptoKeySlotContent:
        """Creates and adds a keySlotContent to this CryptoKeySlot."""
        if short_name not in self.elements:
            new_element = CryptoKeySlotContent(self, short_name)
            # Only call addElement if child has getShortName method (Referrable subclasses)
            if hasattr(new_element, "getShortName"):
                self.addElement(new_element)
            self.keySlotContents.append(new_element)
        return new_element

    def getSlotCapacitys(self) -> PositiveInteger:
        return self.slotCapacitys

    def setSlotCapacitys(self, value: PositiveInteger) -> "CryptoKeySlot":
        self.slotCapacitys = value
        return self

    def getSlotTypes(self) -> Any:
        return self.slotTypes

    def setSlotTypes(self, value: Any) -> "CryptoKeySlot":
        self.slotTypes = value
        return self
